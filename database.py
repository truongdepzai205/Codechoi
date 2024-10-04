import sys
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# Đảm bảo sử dụng UTF-8 cho đầu ra
sys.stdout.reconfigure(encoding='utf-8')

# Tạo một lớp cơ sở
Base = declarative_base()

# Định nghĩa bảng User
class User(Base):
    __tablename__ = 'users'

    Id_user = Column(Integer, primary_key=True, autoincrement=True)
    Ho_ten = Column(String, nullable=False)
    Tai_khoan = Column(String, nullable=False, unique=True)
    Mat_khau = Column(String, nullable=False)
    Dia_chi_camera = Column(String)

    # Liên kết với bảng Infomation
    infomations = relationship('Infomation', back_populates='user')

# Định nghĩa bảng Infomation
class Infomation(Base):
    __tablename__ = 'infomation'

    id = Column(Integer, primary_key=True, autoincrement=True)
    Id_user = Column(Integer, ForeignKey('users.Id_user'), nullable=False)
    id_nguoi_nhan = Column(Integer, nullable=False)
    Ho_ten_nguoi_nhan = Column(String, nullable=False)
    SDT = Column(String, nullable=False)

    # Liên kết trở lại với bảng User
    user = relationship('User', back_populates='infomations')

# Thiết lập cơ sở dữ liệu SQLite
engine = create_engine('sqlite:///mydatabase.db')
Base.metadata.create_all(engine)

# Tạo session
Session = sessionmaker(bind=engine)
session = Session()

# Hàm thêm thông tin người nhận
def them_nguoi_nhan(session, Id_user, id_nguoi_nhan, Ho_ten_nguoi_nhan, SDT):
    try:
        # Tạo đối tượng Infomation mới
        new_info = Infomation(
            Id_user=Id_user,
            id_nguoi_nhan=id_nguoi_nhan,
            Ho_ten_nguoi_nhan=Ho_ten_nguoi_nhan,
            SDT=SDT
        )
        # Thêm vào session và commit
        session.add(new_info)
        session.commit()
        print(f"Đã thêm người nhận {Ho_ten_nguoi_nhan} thành công.")
    except Exception as e:
        session.rollback()  # Rollback nếu có lỗi
        print(f"Lỗi khi thêm người nhận: {e}")

# Hàm xóa thông tin người nhận
def xoa_nguoi_nhan(session, id_nguoi_nhan):
    try:
        # Truy vấn thông tin người nhận theo id_nguoi_nhan
        info = session.query(Infomation).filter_by(id_nguoi_nhan=id_nguoi_nhan).first()
        if info:
            # Xóa thông tin người nhận nếu tìm thấy
            session.delete(info)
            session.commit()
            print(f"Đã xóa người nhận với ID {id_nguoi_nhan} thành công.")
        else:
            print(f"Không tìm thấy người nhận với ID {id_nguoi_nhan}.")
    except Exception as e:
        session.rollback()  # Rollback nếu có lỗi
        print(f"Lỗi khi xóa người nhận: {e}")


