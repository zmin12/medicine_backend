from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from database import Base
from sqlalchemy import func
# 1. 用户表（已有）
class User(Base):
    __tablename__="user"

    id=Column(
        Integer,
        primary_key=True
    )

    username=Column(
        String(50),
        unique=True
    )

    password_hash=Column(
        String(255)
    )

    role=Column(
        String(20)
    )

    created_at=Column(
        DateTime,
        server_default=func.now()
    )

# 2. 用药计划表（已有）
class MedicinePlan(Base):
    __tablename__ = "medicine_plan"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    medicine_name = Column(String(100), nullable=False)
    time = Column(String(20))  # 如 "08:00", "饭后"
    frequency = Column(String(50), default="每日一次")
    created_at = Column(DateTime, server_default=func.now())

# 🔑 3. 设备表（智能药盒硬件）
class Device(Base):
    __tablename__ = "device"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)  # 绑定用户
    device_name = Column(String(50), default="智能药盒")
    sn_code = Column(String(50), unique=True)  # 设备序列号/MAC
    status = Column(String(20), default="online")  # online/offline/maintenance
    last_active = Column(DateTime, server_default=func.now())

# 🔑 4. 药仓表（设备内的物理格子/库存）
class MedicineBox(Base):
    __tablename__ = "medicine_box"
    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(Integer, ForeignKey("device.id"), nullable=False)  # 属于哪个设备
    slot_name = Column(String(20))  # 仓位编号，如 "A1", "B2"
    medicine_name = Column(String(100))
    capacity = Column(Integer, default=10)  # 最大容量
    current_amount = Column(Integer, default=0)  # 当前余量
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

# 🔑 5. 用药任务表（计划触发的具体执行记录）
class MedicineTask(Base):
    __tablename__ = "medicine_task"
    id = Column(Integer, primary_key=True, index=True)
    plan_id = Column(Integer, ForeignKey("medicine_plan.id"), nullable=False)  # 关联计划
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    device_id = Column(Integer, ForeignKey("device.id"))
    medicine_name = Column(String(100), nullable=False)
    scheduled_time = Column(DateTime, nullable=False)  # 计划服药时间
    actual_time = Column(DateTime, nullable=True)  # 实际服药时间
    status = Column(String(20), default="pending")  # pending/completed/missed

class FamilyRelation(Base):

    __tablename__="family_relation"

    id=Column(
        Integer,
        primary_key=True
    )

    elder_id=Column(
        Integer,
        ForeignKey("user.id")
    )

    family_id=Column(
        Integer,
        ForeignKey("user.id")
    )

    relation=Column(
        String(20)
    )