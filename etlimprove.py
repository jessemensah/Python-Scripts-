
#

class extract:
    @staticmethod
    def fromCSV(file_path, delimiter = ",", quotechar = "|"):
        if not file_path:
            raise Exception("You must provide a valid file path.")
        import csv
        dataset = list()
        with open(file_path) as f:
            csv_file = csv.DictReader(f, delimiter = delimiter,quotechar = quotechar)
            for row in csv_file:
                dataset.append(row)
        return dataset

    @staticmethod
    def fromJSON(file_path):
        if not file_path:
            raise Exception("You must provide a valid file path.")
        import json
        dataset = list()
        with open(file_path) as json_file:
            dataset = json.load(json_file)
        return dataset

    @staticmethod
    def fromMYSQL(host, username, password, db, query):
        if not host or not username or not db or not query:
            raise Exception("Please make sure that you input a valid host, username, \
                            password, database, and query.")
        import pymysql
        db = pymysql.connect(host = host, user = username, password = password,
                             db = db, cursorclass = pymysql.cursors.DictCursor)
        cur = db.cursor()
        cur.execute(query)
        dataset = list()
        for r in cur:
            dataset.append(r)
        db.commit()
        cur.close()
        db.close()
        return dataset

    @staticmethod
    def fromMONGODB(host, port, username, password, db, collection, query = None):
        if not host or not port or not username or not db or not collection:
            raise Exception("Please make sure that you input a valid host, \
            username, password, database, and collection name")
        import pymongo
        client = pymongo.MongoClient(host = host, port = port,username  = username,
                                     password = password)
        tmp_database = client[db]
        tmp_collection = tmp_database[collection]
        dataset = list()
        if query:
            for document in tmp_collection.find(query):
                dataset.append(document)
            return dataset
        for document in tmp_collection.find():
                dataset.append(document)
        return dataset

dataset = extract.fromCSV(file_path = "data/stocks.csv")
print(dataset[0])




#

from extract import extract

dataset = extract.fromCSV(file_path = "data/stocks.csv")
print(dataset[0])


#

from extract import extract

class transform:
    #return the top N records from the dataset
    @staticmethod
    def head(dataset, step):
        if not dataset:
            raise Exception("Dataset cannot be empty.")
        if step < 1:
            raise Exception("The step value must be positive.")
        return dataset[0:step]

    #return the last N records from the dataset
    @staticmethod
    def tail(dataset, step):
        if not dataset:
            raise Exception("Dataset cannot be empty.")
        if step < 1:
            raise Exception("The step value must be positive.")
        return dataset[len(dataset) - step:len(dataset)]

    #rename a column in the dataset
    @staticmethod
    def rename_attribute(dataset, attribute, new_attribute):
        if not dataset:
            raise Exception("Dataset cannot be empty.")
        if not attribute:
            raise Exception("The attribute key must be a valid key.")
        new_dataset = list()
        for row in dataset:
            if attribute in row.keys():
                val = row[attribute]
                new_row = row.copy()
                del new_row[attribute]
                new_row[new_attribute] = val
                new_dataset.append(new_row)
            else:
                raise Exception("Operation is not possible because the column "
                        + str(column_name)
                        + " does not exist in one of the rows in the dataset.")
        return new_dataset

    #remove a column from the dataset
    @staticmethod
    def remove_attribute(dataset, attribute):
        new_dataset = list()
        for row in dataset:
            new_row = row
            if attribute in new_row.keys():
                del new_row[attribute]
                new_dataset.append(new_row)
        return new_dataset

    @staticmethod
    def rename_attributes(dataset, attributes, new_attributes):
        if not attributes or not new_attributes:
            raise Exception("The attributes cannot be empty.")
        if len(attributes) != len(new_attributes):
            raise Exception("The number of new column names must match the number of \
            existing column names.")
        new_dataset = list()
        for row in dataset:
            new_row = row
            for i in range(0,len(attributes)):
                attribute = attributes[i]
                new_attribute = new_attributes[i]
                if attribute in new_row.keys():
                    val = row[attribute]
                    del new_row[attribute]
                    new_row[new_attribute] = val
                else:
                    raise Exception("Operation is not possible because the key "
                            + str(key)+
                            " does not exist in one of the rows in the dataset.")
            new_dataset.append(new_row)
        return new_dataset

    #remove a column from the dataset
    @staticmethod
    def remove_attributes(dataset, attributes):
        if not dataset:
            raise Exception("Dataset cannot be empty.")
        if not attributes:
            raise Exception("The list of attributes cannot be empty.")
        new_dataset= list()
        for row in dataset:
            new_row = row
            for attribute in attributes:
                if attribute in new_row.keys():
                    del new_row[attribute]
            new_dataset.append(new_row)
        return new_dataset

    @staticmethod
    def transform(dataset, attribute, new_attribute, transform_function, *args):
        if not dataset:
            raise Exception("Dataset cannot be empty.")
        if not attribute or not new_attribute:
            raise Exception("The input attribute cannot be empty.")
        if not transform_function:
            raise Exception("The transform_function cannot be None.")
        new_dataset = list() #output of this function
        for row in dataset: #iterate through the input data
            t = transform_function(row[attribute], *args) #apply transformation
                                                          #function on column
            z = row.copy()
            z.update({new_attribute:t}) #create new column in the data
            new_dataset.append(z)
        return new_dataset


def round_open_price(value,*args):
    return round(float(value))


dataset = extract.fromCSV(file_path = "data/stocks.csv")
print(dataset[0])
new_dataset = transform.transform(dataset = dataset, attribute = "Open",
                                  new_attribute = "open_price_rounded",
                                  transform_function = round_open_price)
print(new_dataset[0])



#
from extract import extract
from transform import transform

def round_open_price(value,*args):
    return round(float(value))


dataset = extract.fromCSV(file_path = "data/stocks.csv")
print(dataset[0])

new_dataset = transform.transform(dataset = dataset, attribute = "Open",
                                  new_attribute = "open_price_rounded",
                                  transform_function = round_open_price)
print(new_dataset[0])


#

from extract import extract

class load:
    @staticmethod
    def toCSV(file_path, dataset):
        if not dataset:
            raise Exception("Input dataset must have at least one item.")
        if not file_path:
            raise Exception("You must provide a valid CSV file path.")
        import csv
        with open(file_path, 'w') as csvfile:
            fieldnames = dataset[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
            writer.writeheader()
            writer.writerows(dataset)

    @staticmethod
    def toJSON(file_path, dataset):
        if not dataset:
            raise Exception("Input dataset must have at least one item.")
        if not file_path:
            raise Exception("You must provide a valid JSON file path.")
        import json
        with open(file_path, 'w') as jsonfile:
            json.dump(dataset, jsonfile)

    @staticmethod
    def toMYSQL(host, username, password, db, table, dataset):
        if not dataset:
            raise Exception("Input dataset must have at least one item.")
        if not db:
            raise Exception("You must input a valid database name.")
        if not table:
            raise Exception("You must input a valid table name")
        import pymysql
        db = pymysql.connect(host = host, user=username, password = password,
                             db = db, cursorclass = pymysql.cursors.DictCursor)
        cur = db.cursor()
        for row in dataset:
            placeholder = ", ".join(["%s"] * len(row))
            stmt = "insert into {table} ({columns}) values ({values});".format(table=table,
                    columns=",".join(row.keys()), values = placeholder)

            cur.execute(stmt, list(row.values()))
        db.commit()
        cur.close()
        db.close()

    @staticmethod
    def toMONGODB(host, port, username, password, db, collection, dataset):
        if not dataset:
            raise Exception("Input dataset must have at least one item.")
        if not db:
            raise Exception("You must input a valid database name.")
        if not collection:
            raise Exception("You must input a valid collection name.")
        import pymongo
        client = pymongo.MongoClient(host = host, port = port, username = username,
                                     password = password)
        tmp_database = client[db]
        tmp_collection = tmp_database[collection]
        tmp_collection.insert_many(dataset)


dataset = extract.fromCSV(file_path="data/ stocks.csv")
load.toCSV(file_path="data/stocks_copy.csv",dataset=dataset)




#


from extract import extract
from load import load

dataset = extract.fromCSV(file_path="data/stocks.csv")
load.toCSV(file_path="data/stocks_copy.csv",dataset=dataset)



#

class extract:
    @staticmethod
    def fromCSV(file_path, delimiter = ",", quotechar = "|"):
        if not file_path:
            # message to display if the user fails to provide a file path at all
            raise Exception("You must provide a valid file path.")
        try:
            import csv
            dataset = list()
            with open(file_path) as f:
                csv_file = csv.DictReader(f, delimiter = delimiter,
                                          quotechar = quotechar)
                for row in csv_file:
                    dataset.append(row)
            return dataset
        except (IOError, OSError):
            raise Exception("You must provide a valid CSV file.")

    @staticmethod
    def fromJSON(file_path):
        if not file_path:
            raise Exception("You must provide a valid file path.")
        import json
        dataset = list()
        with open(file_path) as json_file:
            dataset = json.load(json_file)
        return dataset

    @staticmethod
    def fromMYSQL(host, username, password, db, query):
        if not host or not username or not db or not query:
            raise Exception("Please make sure that you input a valid host, username, \
                            password, database, and query.")
        import pymysql
        db = pymysql.connect(host = host, user = username, password = password,
                             db = db, cursorclass = pymysql.cursors.DictCursor)
        cur = db.cursor()
        cur.execute(query)
        dataset = list()
        for r in cur:
            dataset.append(r)
        db.commit()
        cur.close()
        db.close()
        return dataset

    @staticmethod
    def fromMONGODB(host, port, username, password, db, collection, query = None):
        if not host or not port or not username or not db or not collection:
            raise Exception("Please make sure that you input a valid host, username, \
            password, database, and collection name")
        import pymongo
        client = pymongo.MongoClient(host = host, port = port,username  = username,
                                     password = password)
        tmp_database = client[db]
        tmp_collection = tmp_database[collection]
        dataset = list()
        if query:
            for document in tmp_collection.find(query):
                dataset.append(document)
            return dataset
        for document in tmp_collection.find():
                dataset.append(document)
        return dataset

dataset = extract.fromCSV(file_path="data/wrong_name.csv")
print(dataset[0])


#

class extract:
    @staticmethod
    def fromCSV(file_path, delimiter=",", quotechar="|"):
        if not file_path:
            # message to display if the user fails to provide a file path at all
            raise Exception("You must provide a valid file path.")
        try:
            import csv
            dataset = list()
            with open(file_path) as f:
                csv_file = csv.DictReader(f, delimiter=delimiter,
                                          quotechar=quotechar)
                for row in csv_file:
                    dataset.append(row)
            return dataset
        except (IOError, OSError):
            raise Exception("You must provide a valid CSV file.")

    @staticmethod
    def fromJSON(file_path):
        if not file_path:
            raise Exception("You must provide a valid file path.")
        try:
            import json
            dataset = list()
            with open(file_path) as json_file:
                dataset = json.load(json_file)
            return dataset
        except (IOError, OSError):
            raise Exception("You must provide a valid JSON file.")

    @staticmethod
    def fromMYSQL(host, username, password, db, query):
        if not host or not username or not db or not query:
            raise Exception("Please make sure that you input a valid host, username, \
                           password, database, and query.")
        try:
            import pymysql
            db = pymysql.connect(host=host, user=username, password=password,
                                 db=db, cursorclass=pymysql.cursors.DictCursor)
            cur = db.cursor()
            cur.execute(query)
            dataset = list()
            for r in cur:
                dataset.append(r)
            db.commit()
            cur.close()
            db.close()
            return dataset
        except pymysql.InternalError as error:
            print(error)
            raise Exception("Error while reading data from MySQL.")

    @staticmethod
    def fromMONGODB(host, port, username, password, db, collection, query=None):
        if not host or not port or not username or not db or not collection:
            raise Exception("Please make sure that you input a valid host, username, \
           password, database, and collection name")
        try:
            import pymongo
            client = pymongo.MongoClient(host=host, port=port, username=username,
                                         password=password)
            tmp_database = client[db]
            tmp_collection = tmp_database[collection]
            dataset = list()
            if query:
                for document in tmp_collection.find(query):
                    dataset.append(document)
                return dataset
            for document in tmp_collection.find():
                dataset.append(document)
            return dataset
        except pymongo.errors.PyMongoError as e:
            print(e)
            raise Exception("Error while reading data from MongoDB.")




#

from extract import extract

class load:
   @staticmethod
   def toCSV(file_path, dataset):
       if not dataset:
           raise Exception("Input dataset must have at least one item.")
       if not file_path:
           raise Exception("You must provide a valid CSV file path.")
       import csv
       with open(file_path, 'w') as csvfile:
           fieldnames = dataset[0].keys()
           writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
           writer.writeheader()
           writer.writerows(dataset)

   @staticmethod
   def toJSON(file_path, dataset):
       if not dataset:
           raise Exception("Input dataset must have at least one item.")
       if not file_path:
           raise Exception("You must provide a valid JSON file path.")
       import json
       with open(file_path, 'w') as jsonfile:
           json.dump(dataset, jsonfile)

   @staticmethod
   def toMYSQL(host, username, password, db, table, dataset):
       if not host or not username or not db or not query:
           raise Exception("Please make sure that you input a valid host, username, \
                           password, database, and query.")
       try:
          import pymysql
          db = pymysql.connect(host = host, user = username, password = password,
                               db = db, cursorclass = pymysql.cursors.DictCursor)
          cur = db.cursor()
          cur.execute(query)
          dataset = list()
          for r in cur:
              dataset.append(r)
          db.commit()
          cur.close()
          db.close()
          return dataset
       except pymysql.InternalError as error:
          print(error)
          raise Exception("Error while reading data from MySQL.")

   @staticmethod
   def toMONGODB(host, port, username, password, db, collection, dataset):
       if not host or not port or not username or not db or not collection:
           raise Exception("Please make sure that you input a valid host, username, \
           password, database, and collection name")
       try:
          import pymongo
          client = pymongo.MongoClient(host = host, port = port,username  = username,
                                       password = password)
          tmp_database = client[db]
          tmp_collection = tmp_database[collection]
          dataset = list()
          if query:
              for document in tmp_collection.find(query):
                  dataset.append(document)
              return dataset
          for document in tmp_collection.find():
                  dataset.append(document)
          return dataset
       except pymongo.errors.PyMongoError as e:
           print(e)
           raise Exception("Error while reading data from MongoDB.")


#

def xml_extractor(xmlfile):
    import xml.etree.ElementTree as ET
    # create element tree object
    tree = ET.parse(xmlfile)
    # get root element
    root = tree.getroot()
    # create empty list for news items
    newsitems = []
    # iterate news items
    for item in root.findall('./channel/item'):
        # empty news dictionary
        news = {}
        # iterate child elements of item
        for child in item:
            # special checking for namespace object content:media
            if child.tag == '{http://search.yahoo.com/mrss/}content':
                news['media'] = child.attrib['url']
            else:
                news[child.tag] = child.text.encode('utf8')
        # append news dictionary to news items list
        newsitems.append(news)
    # return news items list
    return newsitems


#
# new custom extract method
@staticmethod
def fromCustom(custom_extractor,**kwds):

    #this will execute the custom_extractor and store the data in dataset.
    dataset = custom_extractor(**kwds)

    #if the type of dataset is not a list then we need to throw an error
    if type(dataset)!= list:
        raise ValueError("Output data from extract step should a be list of items.")
    return dataset



#
class extract:
    @staticmethod
    def fromCSV(file_path, delimiter = ",", quotechar = "|"):
        if not file_path:
            raise Exception("You must provide a valid file path.")
        import csv
        dataset = list()
        with open(file_path) as f:
            csv_file = csv.DictReader(f, delimiter = delimiter,quotechar = quotechar)
            for row in csv_file:
                dataset.append(row)
        return dataset

    @staticmethod
    def fromJSON(file_path):
        if not file_path:
            raise Exception("You must provide a valid file path.")
        import json
        dataset = list()
        with open(file_path) as json_file:
            dataset = json.load(json_file)
        return dataset

    @staticmethod
    def fromMYSQL(host, username, password, db, query):
        if not host or not username or not db or not query:
            raise Exception("Please make sure that you input a valid host, username, \
                            password, database, and query.")
        import pymysql
        db = pymysql.connect(host = host, user = username, password = password,
                             db = db, cursorclass = pymysql.cursors.DictCursor)
        cur = db.cursor()
        cur.execute(query)
        dataset = list()
        for r in cur:
            dataset.append(r)
        db.commit()
        cur.close()
        db.close()
        return dataset

    @staticmethod
    def fromMONGODB(host, port, username, password, db, collection, query = None):
        if not host or not port or not username or not db or not collection:
            raise Exception("Please make sure that you input a valid host, username, \
            password, database, and collection name")
        import pymongo
        client = pymongo.MongoClient(host = host, port = port,username  = username,
                                     password = password)
        tmp_database = client[db]
        tmp_collection = tmp_database[collection]
        dataset = list()
        if query:
            for document in tmp_collection.find(query):
                dataset.append(document)
            return dataset
        for document in tmp_collection.find():
                dataset.append(document)
        return dataset

    # new custom extract method
    @staticmethod
    def fromCustom(custom_extractor,**kwds):
        #we do not check for path. Path must be defined in the standalone function.

        #this will execute the custom_extractor and store the data in dataset.
        dataset = custom_extractor(**kwds)
        #if the type of dataset is not a list then we need to throw an error
        if type(dataset)!= list:
            raise ValueError("Output data from extract step should a be list of items.")
        return dataset


#standalone function to extract data from XML
def xml_extractor(xmlfile):
    import xml.etree.ElementTree as ET
    # create element tree object
    tree = ET.parse(xmlfile)
    # get root element
    root = tree.getroot()
    # create empty list for news items
    newsitems = []
    # iterate news items
    for item in root.findall('./channel/item'):
        # empty news dictionary
        news = {}
        # iterate child elements of item
        for child in item:
            # special checking for namespace object content:media
            if child.tag == '{http://search.yahoo.com/mrss/}content':
                news['media'] = child.attrib['url']
            else:
                news[child.tag] = child.text.encode('utf8')
        # append news dictionary to news items list
        newsitems.append(news)
    # return news items list
    return newsitems

dataset = extract.fromCustom(xml_extractor,xmlfile="data/newsfeed.xml")
print(dataset[0])


#

from extract import extract

def xml_extractor(xmlfile):
    import xml.etree.ElementTree as ET
    # create element tree object
    tree = ET.parse(xmlfile)
    # get root element
    root = tree.getroot()
    # create empty list for news items
    newsitems = []
    # iterate news items
    for item in root.findall('./channel/item'):
        # empty news dictionary
        news = {}
        # iterate child elements of item
        for child in item:
            # special checking for namespace object content:media
            if child.tag == '{http://search.yahoo.com/mrss/}content':
                news['media'] = child.attrib['url']
            else:
                news[child.tag] = child.text.encode('utf8')
        # append news dictionary to news items list
        newsitems.append(news)
    # return news items list
    return newsitems

dataset = extract.fromCustom(xml_extractor,xmlfile="data/newsfeed.xml")
print(dataset[0])

















































































