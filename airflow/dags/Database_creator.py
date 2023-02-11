from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Se define  una variable "Base" con declarative_base para la creacion de las tablas.
Base = declarative_base()

# Se crean clases base para la definición de tablas

class Geolocation(Base):
    __tablename__ = 'geolocation'
    CEP = Column(Integer, primary_key=True, index=True)
    cidade = Column(String(100))
    cod_estado = Column(String(100))
    estado = Column(String(100))
    customers = relationship('Customers', backref='geolocation')
    sellers = relationship('Sellers', backref='geolocation')

class Customers(Base):
    __tablename__ = 'customers'
    customer_id = Column(String(100), primary_key=True, index=True)
    CEP = Column(Integer, ForeignKey('geolocation.CEP'), index=True)
    orders = relationship('Orders', backref='customers')

class Sellers(Base):
    __tablename__ = 'sellers'
    seller_id = Column(String(100), primary_key=True, index=True)
    CEP = Column(Integer, ForeignKey('geolocation.CEP'), index=True)
    order_items = relationship('Order_items', backref='sellers')
    close_deals = relationship('Close_deals', backref='sellers')

class Orders(Base):
    __tablename__ = 'orders'
    order_id = Column(String(100), primary_key=True, index=True)
    customer_id = Column(String(100), ForeignKey('customers.customer_id'), index=True)
    order_status = Column(String(100))
    order_purchase_timestamp = Column(DateTime)
    order_approved_at = Column(DateTime)
    order_delivered_carrier_date = Column(DateTime)
    order_delivered_customer_date = Column(DateTime)
    order_estimated_delivery_date = Column(DateTime)
    order_reviews = relationship('Order_reviews', backref='orders')
    order_payments = relationship('Order_payments', backref='orders')
    order_items = relationship('Order_items', backref='orders')

'''
class Order_reviews(Base):
    __tablename__ = 'order_reviews'
    review_id = Column(Integer, primary_key=True, index=True)
    review_code = Column(String(100))
    order_id = Column(String(100), ForeignKey('orders.order_id'), index=True)
    review_score = Column(Integer)
    review_creation_date = Column(DateTime)
    review_answer_timestamp = Column(DateTime)
'''

class Order_payments(Base):
    __tablename__ = 'order_payments'
    order_payment_id = Column(Integer, primary_key=True, index=True)
    order_id = Column(String(100), ForeignKey('orders.order_id'), index=True)
    payment_sequential = Column(Integer)
    payment_type = Column(String(100))
    payment_installments = Column(Integer)
    payment_value = Column(Float)

class Product_category(Base):
    __tablename__ = 'product_category'
    product_category_id = Column(Integer, primary_key=True, index=True)
    product_category_name = Column(String(100))
    product_category_name_english = Column(String(100))
    product_category_name_spanish = Column(String(100))
    products = relationship('Products', backref='product_category')

class Products(Base):
    __tablename__ = 'products'
    product_id = Column(String(100), primary_key=True, index=True)
    product_name_lenght = Column(Integer)
    product_description_lenght = Column(Integer)
    product_photos_qty = Column(Integer)
    product_weight_g = Column(Integer)
    product_length_cm = Column(Integer)
    product_height_cm = Column(Integer)
    product_width_cm = Column(Integer)
    product_category_id = Column(Integer, ForeignKey('product_category.product_category_id'), index=True)
    order_items = relationship('Order_items', backref='products')

class Order_items(Base):
    __tablename__ = 'order_items'
    order_item_id = Column(Integer, primary_key=True, index=True)
    order_id = Column(String(100), ForeignKey('orders.order_id'), index=True)
    product_id = Column(String(100), ForeignKey('products.product_id'), index=True)
    seller_id = Column(String(100), ForeignKey('sellers.seller_id'), index=True)
    shipping_limit_date = Column(DateTime)
    price = Column(Float)
    freight_value = Column(Float)
    review_score = Column(Integer)

class Marketing_qualified_leads(Base):
    __tablename__ = 'marketing_qualified_leads'
    mql_id = Column(String(100), primary_key=True, index=True)
    first_contact_date = Column(DateTime)
    landing_page_id = Column(String(100))
    origin = Column(String(100))
    close_deals = relationship('Close_deals', backref='marketing_qualified_leads')

class Close_deals(Base):
    __tablename__ = 'close_deals'
    close_deal_id = Column(Integer, primary_key=True, index=True)
    mql_id = Column(String(100), ForeignKey('marketing_qualified_leads.mql_id'), index=True)
    seller_id = Column(String(100), ForeignKey('sellers.seller_id'), index=True)
    sdr_id = Column(String(100))
    sr_id = Column(String(100))
    won_date = Column(DateTime)
    business_segment = Column(String(100))
    lead_type = Column(String(100))
    business_type = Column(String(100))
    declared_monthly_revenue = Column(Integer)


# Se crea una instancia del motor de base de datos SQLite
engine = create_engine('sqlite:///../../Database/Olist.db', connect_args={'check_same_thread': False}, pool_pre_ping=True, echo=True)

# Se crean las tablas en base de datos enlazadas al motor de base de datos
Base.metadata.create_all(bind=engine)
