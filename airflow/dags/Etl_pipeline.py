from unidecode import unidecode
import pandas as pd
import numpy as np
import requests

from Database_creator import engine


class Etl():

    def __init__(self):
        
        self.geolocation = None
        self.customers = None
        self.sellers = None
        self.orders = None
        self.order_reviews = None
        self.order_payments = None
        self.product_category = None
        self.products = None
        self.order_items = None
        self.mql = None
        self.close_deals = None
    

    def extract(self):
        
        self.customers = pd.read_csv('https://raw.githubusercontent.com/olist/work-at-olist-data/master/datasets/olist_customers_dataset.csv')
        self.sellers = pd.read_csv('https://raw.githubusercontent.com/olist/work-at-olist-data/master/datasets/olist_sellers_dataset.csv')
        self.orders = pd.read_csv('https://raw.githubusercontent.com/olist/work-at-olist-data/master/datasets/olist_orders_dataset.csv')
        self.order_reviews = pd.read_csv('https://raw.githubusercontent.com/olist/work-at-olist-data/master/datasets/olist_order_reviews_dataset.csv')
        self.order_payments = pd.read_csv('https://raw.githubusercontent.com/olist/work-at-olist-data/master/datasets/olist_order_payments_dataset.csv')
        self.product_category = pd.read_csv('https://raw.githubusercontent.com/olist/work-at-olist-data/master/datasets/product_category_name_translation.csv')
        self.products = pd.read_csv('https://raw.githubusercontent.com/olist/work-at-olist-data/master/datasets/olist_products_dataset.csv')
        self.order_items = pd.read_csv('https://raw.githubusercontent.com/olist/work-at-olist-data/master/datasets/olist_order_items_dataset.csv')
        self.mql = pd.read_csv('datasets\olist_marketing_qualified_leads_dataset.csv')
        self.close_deals = pd.read_csv('datasets\olist_closed_deals_dataset.csv')


    def transform(self, add_product_category={}, validate=False):
        
        self.customers.rename(columns={'customer_zip_code_prefix': 'CEP', 'customer_city': 'cidade', 'customer_state': 'cod_estado'}, inplace=True)
        self.sellers.rename(columns={'seller_zip_code_prefix': 'CEP', 'seller_city': 'cidade', 'seller_state': 'cod_estado'}, inplace=True)

        if validate:

            def get_diff(table, table_db, id, drop_inplace=True):

                table = table[~table[id].isin(table_db[id])].dropna()
                table.drop_duplicates(id, keep='last', inplace=drop_inplace)

                return table

            geolocation_DB = pd.read_sql_table('geolocation', engine.connect())
            customers_geo_DB_diff = get_diff(self.customers, geolocation_DB, 'CEP')
            self.geolocation = pd.concat([self.geolocation, customers_geo_DB_diff[['CEP', 'cidade', 'cod_estado']]], ignore_index=True)
            sellers_geo_DB_diff = get_diff(self.sellers, geolocation_DB, 'CEP')
            self.geolocation = pd.concat([self.geolocation, sellers_geo_DB_diff[['CEP', 'cidade', 'cod_estado']]], ignore_index=True)

            customers_DB = pd.read_sql_table('customers', engine.connect())
            self.customers = get_diff(self.customers, customers_DB, 'customer_id')
            
            sellers_DB = pd.read_sql_table('sellers', engine.connect())
            self.sellers = get_diff(self.sellers, sellers_DB, 'seller_id')

            product_category_DB = pd.read_sql_table('product_category', engine.connect())
            if add_product_category and type(add_product_category) == dict:
                self.product_category = pd.DataFrame(add_product_category)
                self.product_category.index += (len(product_category_DB) + 1)
                self.product_category = self.product_category.rename_axis('product_category_id').reset_index()
                self.product_category = pd.concat([product_category_DB, self.product_category], ignore_index=True)
            else:
                self.product_category = product_category_DB.copy()

            products_DB = pd.read_sql_table('products', engine.connect())
            self.products = get_diff(self.products, products_DB, 'product_id')

            orders_DB = pd.read_sql_table('orders', engine.connect())
            self.orders = get_diff(self.orders, orders_DB, 'order_id')

            order_reviews_DB = pd.read_sql_table('order_reviews', engine.connect())
            self.order_reviews = get_diff(self.order_reviews, order_reviews_DB, 'review_code')

            order_items_DB = pd.read_sql_table('order_items', engine.connect())
            self.order_items = get_diff(self.order_items, order_items_DB, 'order_id', drop_inplace=False)

            order_payments_DB = pd.read_sql_table('order_payments', engine.connect())
            self.order_payments = get_diff(self.order_payments, order_payments_DB, 'order_id', drop_inplace=False)

            mql_DB = pd.read_sql_table('marketing_qualified_leads', engine.connect())
            self.mql = get_diff(self.mql, mql_DB, 'mql_id')

            close_deals_DB = pd.read_sql_table('close_deals', engine.connect())
            self.close_deals = get_diff(self.close_deals, close_deals_DB, 'mql_id', drop_inplace=False)

        else:
            
            url = 'https://parseapi.back4app.com/classes/CEP?limit=730321&order=cidade&keys=CEP,cidade,estado'
            headers = {'X-Parse-Application-Id': '0yGhkskBgC6LMtROXg0SoyHMyl6yYa4SStdCLBpX',
                'X-Parse-Master-Key': 'Dv9aEYXQtwEQRmeR4BMXX8YadeE9CyNy6PJFJPQe'}

            self.geolocation = pd.DataFrame(requests.get(url, headers=headers).json()['results'])
            self.geolocation.drop(['objectId', 'createdAt', 'updatedAt'], axis=1, inplace=True)
            self.geolocation['estado'] = self.geolocation['estado'].str.split(expand=True)[0]
            self.geolocation['CEP'] = self.geolocation['CEP'].apply(lambda x: x[:-3])
            self.geolocation['cidade'] = self.geolocation['cidade'].str.extract(r'\((.*)\)', expand=False).fillna(self.geolocation['cidade'])
            self.geolocation.drop_duplicates('CEP', keep='last', inplace=True)
            self.geolocation['CEP'] = self.geolocation['CEP'].astype('int64')
            self.geolocation.rename(columns={'estado': 'cod_estado'}, inplace=True)

            customers_geo_diff = self.customers[~self.customers['CEP'].isin(self.geolocation['CEP'])].dropna().drop_duplicates('CEP', keep='last')
            self.geolocation = pd.concat([self.geolocation, customers_geo_diff[['CEP', 'cidade', 'cod_estado']]], ignore_index=True)

            sellers_geo_diff = self.sellers[~self.sellers['CEP'].isin(self.geolocation['CEP'])].dropna().drop_duplicates('CEP', keep='last')
            self.geolocation = pd.concat([self.geolocation, sellers_geo_diff[['CEP', 'cidade', 'cod_estado']]], ignore_index=True)

            categories = pd.DataFrame({'product_category_name': ['pc_gamer', 'sem dados', 'portateis_cozinha_e_preparadores_de_alimentos'],
                'product_category_name_english': ['pc gamer', 'no data','kitchen portables and food preparators']})
            self.product_category = pd.concat([self.product_category, categories], ignore_index=True)
            self.product_category['product_category_name_spanish'] = pd.DataFrame({'product_category_name_spanish': 
                ['Salud y belleza', 'Accesorios de computadores', 'Automovil', 'Cama, mesa y baño', 'Decoracion y muebles', 'Ocio y deportes', 'Perfumeria',
                'Articulos del hogar', 'Telefonia', 'Relojes y regalos', 'Alimentos y bebidas', 'Bebes', 'Papeleria', 'Impresion de imagen y tablets', 'Juguetes',
                'Telefonia fija', 'Herramientas de jardin', 'Bolsos, moda y accesorios', 'Pequeños accesorios', 'Consolas y juegos', 'Audio', 'Moda y zapatos',
                'Cosas interesantes', 'Accesorios de equipaje', 'Aire acondicionado', 'Herramientas de construccion', 'Cocina, comedor, lavanderia, jardin y muebles',
                'Herramientas de construccion de jardin', 'Ropa moda hombre', 'Tienda de mascotas', 'Muebles de oficina', 'Mercado', 'Electronica', 'Electrodomesticos',
                'Suministros fiesta', 'Comodidad del hogar', 'Herramientas de construccion y herramientas', 'Agroindustria y comercio', 'Muebles, colchones y tapiceria',
                'Libros tecnicos', 'Construccion del hogar', 'Instrumentos musicales', 'Muebles de sala', 'Herramientas de construccion y luces',
                'Industria, comercio y negocios', 'Comida', 'Arte', 'Muebles de dormitorio', 'Libros de interes general', 'Herramientas de construccion y seguridad',
                'Moda, ropa interior, playa', 'Moda y deportes', 'Señalizacion y seguridad', 'Computadores', 'Suministros de navidad', 'Ropa moda mujer',
                'Electrodomesticos 2', 'Libros importados', 'Bebidas', 'Cine y fotografia', 'Cocina', 'Musica', 'Comodidad del hogar 2', 
                'Pequeños accesorios del hogar, horno y cafe', 'CDs, DVDs y musicales', 'DVDs y blu-ray', 'Flores', 'Arte y artesania', 'Pañales e higiene',
                'Moda ropa de niños', 'Seguridad y servicios', 'Computadores gamer', 'Sin dato', 'Portatiles de cocina y preparadores de comida',  'Decoracion muebles']})
            self.product_category.index += 1
            self.product_category = self.product_category.rename_axis('product_category_id').reset_index()
            
        self.products['product_category_name'].replace({np.nan: 'sem dados'}, inplace=True)
        self.products.fillna(0, inplace=True)
        self.products = self.products.astype({'product_name_lenght': 'int64', 'product_description_lenght': 'int64', 'product_photos_qty': 'int64',
            'product_weight_g': 'int64', 'product_length_cm': 'int64', 'product_height_cm': 'int64', 'product_width_cm': 'int64'})
        self.products = self.products.merge(self.product_category, how='left', on=['product_category_name'])
        self.products.drop(['product_category_name', 'product_category_name_english', 'product_category_name_spanish'], axis=1, inplace=True)

        self.orders.fillna('2016-01-01 00:00:00', inplace=True)
        self.orders = self.orders.astype({'order_purchase_timestamp': 'datetime64', 'order_approved_at': 'datetime64', 'order_delivered_carrier_date': 'datetime64',
            'order_delivered_customer_date': 'datetime64', 'order_estimated_delivery_date': 'datetime64'})

        self.order_reviews = self.order_reviews[['order_id', 'review_score']].drop_duplicates('order_id', keep='last')
                        
        self.order_items.drop(['order_item_id'], axis=1, inplace=True)
        self.order_items.drop_duplicates(inplace=True)
        self.order_items = self.order_items.merge(self.order_reviews[['order_id', 'review_score']], how='left', on=['order_id'])
        self.order_items.dropna(inplace=True)
        self.order_items['shipping_limit_date'] = self.order_items['shipping_limit_date'].astype('datetime64')

        self.order_payments.drop_duplicates('order_id', keep='last', inplace=True) # Hay duplicados con valores diferentes, se conserva el ultimo registro

        self.mql.fillna('no_data', inplace=True)
        self.mql = self.mql.astype({'first_contact_date': 'datetime64'})

        self.close_deals.drop(['lead_behaviour_profile', 'has_company', 'has_gtin', 'average_stock', 'declared_product_catalog_size'], axis=1, inplace=True)
        self.close_deals.fillna('no_data', inplace=True)
        self.close_deals = self.close_deals.astype({'won_date': 'datetime64'})

        self.geolocation.sort_values(by='CEP', inplace=True)
        self.geolocation['cidade'] = self.geolocation['cidade'].apply(lambda x: unidecode(x).title())
        estados = ['Acre', 'Alagoas', 'Amapa', 'Amazonas', 'Bahia', 'Ceara', 'Brasilia', 'Espírito Santo', 'Goias', 'Maranhao', 'Mato Grosso',
            'Mato Grosso do Sul', 'Minas Gerais', 'Para', 'Paraíba', 'Parana', 'Pernambuco', 'Piaui', 'Rio de Janeiro', 'Rio Grande do Norte',
            'Rio Grande do Sul', 'Rondonia', 'Roraima', 'Santa Catarina', 'Sao Paulo', 'Sergipe', 'Tocantins']
        cod_estados = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS',
            'RO', 'RR', 'SC', 'SP', 'SE', 'TO']
        self.geolocation = self.geolocation.merge(pd.DataFrame({'estado': estados, 'cod_estado': cod_estados}), on='cod_estado')

        self.customers.drop(['customer_unique_id', 'cidade', 'cod_estado'], axis=1, inplace=True)
        
        self.sellers.drop(['cidade', 'cod_estado'], axis=1, inplace=True)


    def load(self):

        self.geolocation.to_sql('geolocation', engine, if_exists='append', index=False)
        self.customers.to_sql('customers', engine, if_exists='append', index=False)
        self.sellers.to_sql('sellers', engine, if_exists='append', index=False)
        self.orders.to_sql('orders', engine, if_exists='append', index=False)
        self.order_payments.to_sql('order_payments', engine, if_exists='append', index=False)
        self.product_category.to_sql('product_category', engine, if_exists='append', index=False)
        self.products.to_sql('products', engine, if_exists='append', index=False)
        self.order_items.to_sql('order_items', engine, if_exists='append', index=False)
        self.mql.to_sql('marketing_qualified_leads', engine, if_exists='append', index=False)
        self.close_deals.to_sql('close_deals', engine, if_exists='append', index=False)

    
    def train_test_predict_split(self):
        
        ml_df = self.order_items.copy()
        ml_df = ml_df.merge(self.orders, how='left', on='order_id')
        ml_df = ml_df.merge(self.products, how='left', on='product_id')
        ml_df = ml_df.merge(self.customers, how='left', on='customer_id')
        ml_df = ml_df.merge(self.geolocation[['CEP', 'cod_estado']], how='left', on='CEP')
        ml_df = ml_df.merge(self.sellers, how='left', on='seller_id', suffixes=('_customer', '_seller'))
        ml_df = ml_df.merge(self.geolocation[['CEP', 'cod_estado']], how='left', left_on='CEP_seller', right_on='CEP', suffixes=('_customer', '_seller'))
        ml_df = ml_df.merge(self.order_payments, on=['order_id'])
        ml_df[ml_df.select_dtypes(include=['datetime']).columns] = (ml_df.select_dtypes(include=['datetime']).astype('int64') / 10**9).astype(int)
        ml_df.drop(ml_df[ml_df['order_status'] == 'canceled'].index, inplace=True)
        ml_df.drop(ml_df[ml_df['order_delivered_customer_date'] == 1451606400].index, inplace=True)
        ml_df.drop(['order_id', 'CEP', 'order_status'], axis=1, inplace=True)
        ml_df = ml_df.astype({'review_score': 'int64', 'payment_sequential': 'int64', 'payment_installments': 'int64'})
        ml_df.query("order_purchase_timestamp < 1534896000").to_csv('datasets\olist_to_train_test', index=False)
        ml_df.query("order_purchase_timestamp >= 1534896000").to_csv('datasets\olist_to_predict', index=False)


if __name__ == '__main__':
    etl = Etl()
    etl.extract()
    etl.transform()
    etl.load()
