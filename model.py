from database import Base
from sqlalchemy import Column, Integer, Text, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_utils.types import ChoiceType

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key = True)
    username = Column(String(30), unique = True)
    email = Column(String(80), unique = True)
    password = Column(Text, nullable = False)
    is_active = Column(Boolean, default= False)
    is_staff = Column(Boolean, default= False)
    orders = relationship('Order', back_populates='user')
    
    def __repr__(self):
        return f"<User: {self.username}>"
    
class Order(Base):
    
    ORDER_STATUSES = (
        ('IN-KITCHEN', 'in-kitchen'),
        ('IN-TRANSIT', 'in-transit'),
        ('DELIVERED', 'DELIVERED')
    )
    
    PIZZA_SIZE = (
        ('LARGE', 'large'),
        ('MEDIUM', 'medium'),
        ('PERSONAL', 'personal')
    )
    __tablename__ = "orders"
    id = Column(Integer, primary_key = True)
    quantity = Column(Integer, nullable = False)
    order_status = Column(ChoiceType(choices=ORDER_STATUSES), default = "PENDING")
    pizza_size = Column(ChoiceType(choices=PIZZA_SIZE), nullable=False)
    flavour = Column(String(60), nullable = False)
    user_id = Column(Integer, ForeignKey(User.id))
    user = relationship('User', back_populates='orders')
    
    def __repr__(self):
        return f"<Order ID: {self.id}>\n<Order Status: {self.order_status}>\n<User ID: {self.user_id}>"