# THIS FILE IS USED TO HELP IMPLEMENT ETLs in Python

class extract:
    def fromCSV(self):
        pass

    def fromJSON(self):
        pass

    def fromMYSQL(self):
        pass

    def fromMONGODB(self):
        pass


#

class extract:
    def fromCSV(self, file_path, delimiter = ",", quotechar = "|"):
        if not file_path:
            raise Exception("You must provide a valid file path.")
        import csv
        dataset = list()
        with open(file_path) as f:
            csv_file = csv.DictReader(f, delimiter = delimiter, quotechar = quotechar)
            for row in csv_file:
                dataset.append(row)
        return dataset

    def fromJSON(self):
        pass

    def fromMYSQL(self):
        pass

    def fromMONGODB(self):
        pass

e = extract()
dataset = e.fromCSV(file_path="data/got_chars.csv")
for row in dataset:
    print(row)


#

class extract:
    def fromCSV(self, file_path, delimiter = ",", quotechar = "|"):
        if not file_path:
            raise Exception("You must provide a valid file path.")
        import csv
        dataset = list()
        with open(file_path) as f:
            csv_file = csv.DictReader(f, delimiter = delimiter,quotechar = quotechar)
            for row in csv_file:
                dataset.append(row)
        return dataset

    def fromJSON(self, file_path):
        if not file_path:
            raise Exception("You must provide a valid file path.")
        import json
        dataset = list()
        with open(file_path) as json_file:
            dataset = json.load(json_file)
        return dataset

    def fromMYSQL(self):
        pass

    def fromMONGODB(self):
        pass

e = extract()
dataset = e.fromJSON(file_path = "data/person.json")
print(dataset)
print(len(dataset))



#

class extract:
    def fromMYSQL(self, host, username, password, db, query):
        if not host or not username or not db or not query:
            raise Exception("Please make sure that you input a valid host, username, password, \
            database, and query.")
        import pymysql
        db = pymysql.connect(host = host, user = username, password = password, db = db,
                             cursorclass = pymysql.cursors.DictCursor)
        cur = db.cursor()
        cur.execute(query)
        dataset = list()
        for r in cur:
            dataset.append(r)
        db.commit()
        cur.close()
        db.close()
        return dataset

e = extract()

query = "select * from artist;"

dataset = e.fromMYSQL(host = "localhost", username = "root", password = "admin",
                      db = "vinylrecordshop",query = query)

print(dataset)
print(len(dataset))


#

class extract:
    def fromCSV(self, file_path, delimiter = ",", quotechar = "|"):
        if not file_path:
            raise Exception("You must provide a valid file path.")
        import csv
        dataset = list()
        with open(file_path) as f:
            csv_file = csv.DictReader(f, delimiter = delimiter,quotechar = quotechar)
            for row in csv_file:
                dataset.append(row)
        return dataset

    def fromJSON(self, file_path):
        if not file_path:
            raise Exception("You must provide a valid file path.")
        import json
        dataset = list()
        with open(file_path) as json_file:
            dataset = json.load(json_file)
        return dataset

    def fromMYSQL(self, host, username, password, db, query):
        if not host or not username or not db or not query:
            raise Exception("Please make sure that you input a valid host, \
            username, password, database, and query.")
        import pymysql
        db = pymysql.connect(host = host, user = username, password = password, db = db,
                             cursorclass = pymysql.cursors.DictCursor)
        cur = db.cursor()
        cur.execute(query)
        dataset = list()
        for r in cur:
            dataset.append(r)
        db.commit()
        cur.close()
        db.close()
        return dataset

    def fromMONGODB(self):
        pass


# ---------------------------------------------------------------------------

class extract:
    def fromMONGODB(self, host, port, username, password, db, collection, query = None):
        if not host or not port or not username or not db or not collection:
            raise Exception("Please make sure that you input a valid host, username, password, \
            database, and collection name")
        import pymongo
        client = pymongo.MongoClient(host = host, port = port,username  = username, password = password)
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

e = extract()

#update the values here based on your own mongodb options if necessary
dataset = e.fromMONGODB(host = "localhost", port = 27017, username = "admin", password = "admin",
                        db = "amazon_reviews", collection = "musical_instruments")
print(len(dataset))
print(dataset[0])



#

class extract:
    def fromCSV(self, file_path, delimiter = ",", quotechar = "|"):
        if not file_path:
            raise Exception("You must provide a valid file path.")
        import csv
        dataset = list()
        with open(file_path) as f:
            csv_file = csv.DictReader(f, delimiter = delimiter,quotechar = quotechar)
            for row in csv_file:
                dataset.append(row)
        return dataset

    def fromJSON(self, file_path):
        if not file_path:
            raise Exception("You must provide a valid file path.")
        import json
        dataset = list()
        with open(file_path) as json_file:
            dataset = json.load(json_file)
        return dataset

    def fromMYSQL(self, host, username, password, db, query):
        if not host or not username or not db or not query:
            raise Exception("Please make sure that you input a valid host, \
             username, password, database, and query.")
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

    def fromMONGODB(self, host, port, username, password, db,
                    collection, query = None):
        if not host or not port or not username or not db or not collection:
            raise Exception("Please make sure that you input a valid host,
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



#

from extract import extract

e = extract()
dataset = e.fromCSV(file_path="data/got_chars.csv")
for row in dataset:
    print(row)


#

class transform:
    def head(self, dataset, step): #return the top N records from the dataset
        pass

    def tail(self): #return the last N records from the dataset
        pass

    def rename_attribute(self): #rename a column in the dataset
        pass

    def remove_attribute(self): #remove a column from the dataset
        pass

    def rename_attributes(self): #rename a list of columns in the dataset
        pass

    def remove_attributes(self): #remove a list of columns in the dataset
        pass

    def transform(self):
        pass



#

from extract import extract #import our custom built extract module

class transform:
    #return the top N records from the dataset
    def head(self, dataset, step):
        if not dataset:
            raise Exception("Dataset cannot be empty.")
        if step < 1:
            raise Exception("The step value must be positive.")
        return dataset[0:step]

    #return the last N records from the dataset
    def tail(self, dataset, step):
        if not dataset:
            raise Exception("Dataset cannot be empty.")
        if step < 1:
            raise Exception("The step value must be positive.")
        return dataset[len(dataset) - step:len(dataset)]

    def rename_attribute(self): #rename a column in the dataset
        pass

    def remove_attribute(self): #remove a column from the dataset
        pass

    def rename_attributes(self): #rename a list of columns in the dataset
        pass

    def remove_attributes(self): #remove a list of columns in the dataset
        pass

    def transform(self):
        pass

e = extract()
# connect to mongodb; change values if necessary
dataset = e.fromMONGODB(host = "localhost", port = 27017, username = "admin",
                        password = "admin", db = "amazon_reviews",
                        collection = "musical_instruments")

t = transform()
dataset_1 = t.head(dataset = dataset, step = 5) # retrieve the top 5 records
                                                # in the dataset
print("Top 5 records in the dataset:")
for row in dataset_1:
    print(row['_id'])

dataset_2 = t.tail(dataset = dataset, step = 5) #retrieve the bottom 5 records
                                                #in the dataset
print("\nBottom 5 records in the dataset:")
for row in dataset_2:
    print(row['_id'])


#

from extract import extract #import our custom built extract module

class transform:
    #return the top N records from the dataset
    def head(self, dataset, step):
        if not dataset:
            raise Exception("Dataset cannot be empty.")
        if step < 1:
            raise Exception("The step value must be positive.")
        return dataset[0:step]

    #return the last N records from the dataset
    def tail(self, dataset, step):
        if not dataset:
            raise Exception("Dataset cannot be empty.")
        if step < 1:
            raise Exception("The step value must be positive.")
        return dataset[len(dataset) - step:len(dataset)]

    def rename_attribute(self): #rename a column in the dataset
        pass

    def remove_attribute(self): #remove a column from the dataset
        pass

    def rename_attributes(self): #rename a list of columns in the dataset
        pass

    def remove_attributes(self): #remove a list of columns in the dataset
        pass

    def transform(self):
        pass

e = extract()
# connect to mongodb; change values if necessary
dataset = e.fromMONGODB(host = "localhost", port = 27017, username = "admin",
                        password = "admin", db = "amazon_reviews",
                        collection = "musical_instruments")

t = transform()
dataset_1 = t.head(dataset = dataset, step = 5) # retrieve the top 5 records
                                                # in the dataset
print("Top 5 records in the dataset:")
for row in dataset_1:
    print(row['_id'])

dataset_2 = t.tail(dataset = dataset, step = 5) #retrieve the bottom 5 records
                                                #in the dataset
print("\nBottom 5 records in the dataset:")
for row in dataset_2:
    print(row['_id'])



#

class transform:
    def head(self, dataset, step): #return the top N records from the dataset
        if not dataset:
            raise Exception("Dataset cannot be empty.")
        if step < 1:
            raise Exception("The step value must be positive.")
        return dataset[0:step]

    def tail(self, dataset, step): #return the last N records from the dataset
        if not dataset:
            raise Exception("Dataset cannot be empty.")
        if step < 1:
            raise Exception("The step value must be positive.")
        return dataset[len(dataset) - step:len(dataset)]

    def rename_attribute(self): #rename a column in the dataset
        pass

    def remove_attribute(self): #remove a column from the dataset
        pass

    def rename_attributes(self): #rename a list of columns in the dataset
        pass

    def remove_attributes(self): #remove a list of columns in the dataset
        pass

    def transform(self):
        pass

#

from extract import extract #import our custom built extract module

class transform:
    #return the top N records from the dataset
    def head(self, dataset, step):
        if not dataset:
            raise Exception("Dataset cannot be empty.")
        if step < 1:
            raise Exception("The step value must be positive.")
        return dataset[0:step]

    #return the last N records from the dataset
    def tail(self, dataset, step):
        if not dataset:
            raise Exception("Dataset cannot be empty.")
        if step < 1:
            raise Exception("The step value must be positive.")
        return dataset[len(dataset) - step:len(dataset)]

    #rename a column in the dataset
    def rename_attribute(self, dataset, attribute, new_attribute):
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
                raise Exception("Operation is not possible because the column " +  \
                                str(column_name) \
                                + " does not exist in one of the rows in the dataset")
        return new_dataset

e = extract()
dataset = e.fromCSV(file_path="data/got_chars.csv")
print("Dataset before renaming the column:")
print(dataset[0])

t = transform()
new_dataset = t.rename_attribute(dataset = dataset, attribute = "character", new_attribute = "character_name")
print("\nDataset after renaming the column:")
print(new_dataset[0])



#

from extract import extract #import our custom built extract module

class transform:

   #return the top N records from the dataset
   def head(self, dataset, step):
       if not dataset:
           raise Exception("Dataset cannot be empty.")
       if step < 1:
           raise Exception("The step value must be positive.")
       return dataset[0:step]

   #return the last N records from the dataset
   def tail(self, dataset, step):
       if not dataset:
           raise Exception("Dataset cannot be empty.")
       if step < 1:
           raise Exception("The step value must be positive.")
       return dataset[len(dataset) - step:len(dataset)]

   #rename a column in the dataset
   def rename_attribute(self, dataset, attribute, new_attribute):
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
               raise Exception("Operation is not possible because the column " + \
                               str(column_name) \
                               + " does not exist in one of the rows in the dataset")
       return new_dataset

   #remove a column from the dataset
   def remove_attribute(self, dataset, attribute):
       new_dataset = list()
       for row in dataset:
           new_row = row
           if attribute in new_row.keys():
               del new_row[attribute]
               new_dataset.append(new_row)
       return new_dataset

e = extract()
dataset = e.fromCSV(file_path = "data/stocks.csv")
print("Original dataset:")
print(dataset[0])

t = transform()
new_dataset = t.remove_attribute(dataset = dataset, attribute = "Open")
print("\nTransformed dataset:")
print(new_dataset[0])



#

class transform:

    # return the top N records from the dataset
    def head(self, dataset, step):
        if not dataset:
            raise Exception("Dataset cannot be empty.")
        if step < 1:
            raise Exception("The step value must be positive.")
        return dataset[0:step]

        # return the last N records from the dataset

    def tail(self, dataset, step):
        if not dataset:
            raise Exception("Dataset cannot be empty.")
        if step < 1:
            raise Exception("The step value must be positive.")
        return dataset[len(dataset) - step:len(dataset)]

    # rename a column in the dataset
    def rename_attribute(self, dataset, attribute, new_attribute):
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
                raise Exception("Operation is not possible because the column " + \
                                str(column_name) \
                                + " does not exist in one of the rows in the dataset")
        return new_dataset

    # remove a column from the dataset
    def remove_attribute(self, dataset, attribute):
        new_dataset = list()
        for row in dataset:
            new_row = row
            if attribute in new_row.keys():
                del new_row[attribute]
                new_dataset.append(new_row)
        return new_dataset

    def rename_attributes(self):  # rename a list of columns in the dataset
        pass

    def remove_attributes(self):  # remove a list of columns in the dataset
        pass

    def transform(self):
        pass



#

from extract import extract #import our custom built extract module

class transform:
   #return the top N records from the dataset
   def head(self, dataset, step):
       if not dataset:
           raise Exception("Dataset cannot be empty.")
       if step < 1:
           raise Exception("The step value must be positive.")
       return dataset[0:step]

   #return the last N records from the dataset
   def tail(self, dataset, step):
       if not dataset:
           raise Exception("Dataset cannot be empty.")
       if step < 1:
           raise Exception("The step value must be positive.")
       return dataset[len(dataset) - step:len(dataset)]

   #rename a column in the dataset
   def rename_attribute(self, dataset, attribute, new_attribute):
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
            raise Exception("Operation is not possible because the column " + \
                            str(column_name) \
                            + " does not exist in one of the rows in the dataset.")
      return new_dataset

   #remove a column from the dataset
   def remove_attribute(self, dataset, attribute):
       new_dataset = list()
       for row in dataset:
           new_row = row
           if attribute in new_row.keys():
               del new_row[attribute]
               new_dataset.append(new_row)
       return new_dataset

    #remove multiple columns from the dataset
   def rename_attributes(self,dataset,attributes,new_attributes):
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
               raise Exception("Operation is not possible because the key " + \
                               str(key)+ \
                            " does not exist in one of the rows in the dataset.")
         new_dataset.append(new_row)
      return new_dataset

e = extract()
dataset = e.fromCSV(file_path="data/stocks.csv")
print("Original dataset:")
print(dataset[0])

t = transform()
new_dataset = t.rename_attributes(dataset = dataset, attributes = ["Open","Close"],
                                  new_attributes = ["open_price", "close_price"])
print("\nUpdated dataset:")
print(new_dataset[0])




#


from extract import extract #import our custom built extract module

class transform:
   #return the top N records from the dataset
   def head(self, dataset, step):
       if not dataset:
           raise Exception("Dataset cannot be empty.")
       if step < 1:
           raise Exception("The step value must be positive.")
       return dataset[0:step]

   #return the last N records from the dataset
   def tail(self, dataset, step):
       if not dataset:
           raise Exception("Dataset cannot be empty.")
       if step < 1:
           raise Exception("The step value must be positive.")
       return dataset[len(dataset) - step:len(dataset)]

   #rename a column in the dataset
   def rename_attribute(self, dataset, attribute, new_attribute):
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
               raise Exception("Operation is not possible because the column " + \
                               str(column_name) + \
                               " does not exist in one of the rows in the dataset.")
       return new_dataset

   #remove a column from the dataset
   def remove_attribute(self, dataset, attribute):
       new_dataset = list()
       for row in dataset:
           new_row = row
           if attribute in new_row.keys():
               del new_row[attribute]
               new_dataset.append(new_row)
       return new_dataset

   def rename_attributes(self,dataset,attributes,new_attributes):
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
                   raise Exception("Operation is not possible because the key " + \
                                   str(key)+ \
                               " does not exist in one of the rows in the dataset.")
           new_dataset.append(new_row)
       return new_dataset

   #remove a column from the dataset
   def remove_attributes(self, dataset, attributes):
       if not dataset:
           raise Exception("Dataset cannot be empty")
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


e = extract()
dataset = e.fromCSV(file_path = "data/stocks.csv")
print("Original dataset:")
print(dataset[0])

t = transform()
new_dataset = t.remove_attributes(dataset = dataset, attributes = ["Open","Close"])
print("\nTransformed dataset:")
print(new_dataset[0])


#

class transform:
   #return the top N records from the dataset
   def head(self, dataset, step):
       if not dataset:
           raise Exception("Dataset cannot be empty.")
       if step < 1:
           raise Exception("The step value must be positive.")
       return dataset[0:step]

   #return the last N records from the dataset
   def tail(self, dataset, step):
       if not dataset:
           raise Exception("Dataset cannot be empty.")
       if step < 1:
           raise Exception("The step value must be positive.")
       return dataset[len(dataset) - step:len(dataset)]

   #rename a column in the dataset
   def rename_attribute(self, dataset, attribute, new_attribute):
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
               raise Exception("Operation is not possible because the column " + \
                               str(column_name) + \
                               " does not exist in one of the rows in the dataset.")
       return new_dataset

   #remove a column from the dataset
   def remove_attribute(self, dataset, attribute):
       new_dataset = list()
       for row in dataset:
           new_row = row
           if attribute in new_row.keys():
               del new_row[attribute]
               new_dataset.append(new_row)
       return new_dataset

   def rename_attributes(self,dataset,attributes,new_attributes):
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
                   raise Exception("Operation is not possible because the key " + \
                                   str(key)+ \
                               " does not exist in one of the rows in the dataset.")
           new_dataset.append(new_row)
       return new_dataset

   #remove a column from the dataset
   def remove_attributes(self, dataset, attributes):
       if not dataset:
           raise Exception("Dataset cannot be empty")
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


#

from extract import extract #import our custom built extract module

class transform:
   #return the top N records from the dataset
   def head(self, dataset, step):
       if not dataset:
           raise Exception("Dataset cannot be empty.")
       if step < 1:
           raise Exception("The step value must be positive.")
       return dataset[0:step]

   #return the last N records from the dataset
   def tail(self, dataset, step):
       if not dataset:
           raise Exception("Dataset cannot be empty.")
       if step < 1:
           raise Exception("The step value must be positive.")
       return dataset[len(dataset) - step:len(dataset)]

   #rename a column in the dataset
   def rename_attribute(self, dataset, attribute, new_attribute):
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
               raise Exception("Operation is not possible because the column " + \
                               str(column_name) + \
                               " does not exist in one of the rows in the dataset.")
       return new_dataset

   #remove a column from the dataset
   def remove_attribute(self, dataset, attribute):
       new_dataset = list()
       for row in dataset:
           new_row = row
           if attribute in new_row.keys():
               del new_row[attribute]
               new_dataset.append(new_row)
       return new_dataset

   def rename_attributes(self,dataset,attributes,new_attributes):
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
                   raise Exception("Operation is not possible because the key " + \
                                   str(key)+ \
                               " does not exist in one of the rows in the dataset.")
           new_dataset.append(new_row)
       return new_dataset

   #remove a column from the dataset
   def remove_attributes(self, dataset, attributes):
       if not dataset:
           raise Exception("Dataset cannot be empty")
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

   def transform(self, dataset, attribute, new_attribute, transform_function, *args):
       if not dataset:
           raise Exception("Dataset cannot be empty.")
       if not attribute or not new_attribute:
           raise Exception("The input attribute cannot be empty.")
       if not transform_function:
           raise Exception("The transform_function cannot be None.")
       new_dataset = list() #output of this function
       for row in dataset:  #iterate through the input data
           t = transform_function(row[attribute], *args) #apply transformation function on column
           z = row.copy()
           z.update({new_attribute:t}) #create new column in the data
           new_dataset.append(z)
       return new_dataset

def round_open_price(value, *args):
    return round(float(value))

e = extract()
dataset = e.fromCSV(file_path="data/stocks.csv")
print("Original dataset:")
print(dataset[0])
t = transform()
new_dataset = t.transform(dataset = dataset, attribute = "Open",
                          new_attribute = "open_price_rounded",
                          transform_function = round_open_price)
print("\nTransformed dataset:")
print(new_dataset[0])



#


class transform:
   #return the top N records from the dataset
   def head(self, dataset, step):
       if not dataset:
           raise Exception("Dataset cannot be empty.")
       if step < 1:
           raise Exception("The step value must be positive.")
       return dataset[0:step]

   #return the last N records from the dataset
   def tail(self, dataset, step):
       if not dataset:
           raise Exception("Dataset cannot be empty.")
       if step < 1:
           raise Exception("The step value must be positive.")
       return dataset[len(dataset) - step:len(dataset)]

   #rename a column in the dataset
   def rename_attribute(self, dataset, attribute, new_attribute):
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
               raise Exception("Operation is not possible because the column " + \
                               str(column_name) + \
                               " does not exist in one of the rows in the dataset.")
       return new_dataset

   #remove a column from the dataset
   def remove_attribute(self, dataset, attribute):
       new_dataset = list()
       for row in dataset:
           new_row = row
           if attribute in new_row.keys():
               del new_row[attribute]
               new_dataset.append(new_row)
       return new_dataset

   def rename_attributes(self,dataset,attributes,new_attributes):
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
                   raise Exception("Operation is not possible because the key " + \
                                   str(key)+ \
                               " does not exist in one of the rows in the dataset.")
           new_dataset.append(new_row)
       return new_dataset

   #remove a column from the dataset
   def remove_attributes(self, dataset, attributes):
       if not dataset:
           raise Exception("Dataset cannot be empty")
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

   def transform(self, dataset, attribute, new_attribute, transform_function, *args):
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



#

class load:
    def toCSV(self):
        pass

    def toJSON(self):
        pass

    def toMYSQL(self):
        pass

    def toMONGODB(self):
        pass



#

class load:
    def toCSV(self, file_path, dataset):
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

    def toJSON(self):
        pass

    def toMYSQL(self):
        pass

    def toMONGODB(self):
        pass

#

from extract import extract #import our custom built extract module

class load:
    def toCSV(self, file_path, dataset):
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

    def toJSON(self):
        pass

    def toMYSQL(self):
        pass

    def toMONGODB(self):
        pass

e = extract()
dataset = e.fromCSV(file_path = 'data/stocks.csv',delimiter = ',')

l = load()
l.toCSV(file_path = "data/stocks_copy.csv", dataset = dataset)


#

class load:
    def toCSV(self, file_path, dataset):
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

    def toJSON(self, file_path, dataset):
        if not dataset:
            raise Exception("Input dataset must have at least one item.")
        if not file_path:
            raise Exception("You must provide a valid JSON file path.")
        import json
        with open(file_path, 'w') as jsonfile:
            json.dump(dataset, jsonfile)

    def toMYSQL(self):
        pass

    def toMONGODB(self):
        pass


#

from extract import extract #import our custom built extract module

class load:
    def toCSV(self, file_path, dataset):
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

    def toJSON(self, file_path, dataset):
        if not dataset:
            raise Exception("Input dataset must have at least one item.")
        if not file_path:
            raise Exception("You must provide a valid JSON file path.")
        import json
        with open(file_path, 'w') as jsonfile:
            json.dump(dataset, jsonfile)

    def toMYSQL(self):
        pass

    def toMONGODB(self):
        pass

e = extract()
dataset = e.fromCSV(file_path = 'data/stocks.csv', delimiter = ',')

l = load()
l.toJSON(file_path = "data/stocks_copy.json", dataset = dataset)



#

class load:
    def toCSV(self, file_path, dataset):
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

    def toJSON(self, file_path, dataset):
        if not dataset:
            raise Exception("Input dataset must have at least one item.")
        if not file_path:
            raise Exception("You must provide a valid JSON file path.")
        import json
        with open(file_path, 'w') as jsonfile:
            json.dump(dataset, jsonfile)

    def toMYSQL(self, host, username, password, db, table, dataset):
        if not dataset:
            raise Exception("Input dataset must have at least one item.")
        if not db:
            raise Exception("You must input a valid database name.")
        if not table:
            raise Exception("You must input a valid table name")
        import pymysql
        db = pymysql.connect(host = host, user=username, password = password, db = db,
                             cursorclass = pymysql.cursors.DictCursor)
        cur = db.cursor()
        for row in dataset:
            placeholder = ", ".join(["%s"] * len(row))
            stmt = "insert into {table} ({columns}) values ({values});".format(table=table,
                    columns=",".join(row.keys()), values = placeholder)

            cur.execute(stmt, list(row.values()))
        db.commit()
        cur.close()
        db.close()

    def toMONGODB(self):
        pass




#  DATABASE

DROP DATABASE IF EXISTS test;
CREATE DATABASE test;

USE test;

CREATE TABLE cstocks(
    date VARCHAR(10) NOT NULL,
    open FLOAT(10) NOT NULL,
    high FLOAT(10) NOT NULL,
    low FLOAT(10) NOT NULL,
    close FLOAT(10) NOT NULL,
    volume INT(10) NOT NULL
);

SHOW TABLES;



#

from extract import extract #import our custom built extract module

class load:
    def toCSV(self, file_path, dataset):
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

    def toJSON(self, file_path, dataset):
        if not dataset:
            raise Exception("Input dataset must have at least one item.")
        if not file_path:
            raise Exception("You must provide a valid JSON file path.")
        import json
        with open(file_path, 'w') as jsonfile:
            json.dump(dataset, jsonfile)

    def toMYSQL(self, host, username, password, db, table, dataset):
        if not dataset:
            raise Exception("Input dataset must have at least one item.")
        if not db:
            raise Exception("You must input a valid database name.")
        if not table:
            raise Exception("You must input a valid table name")
        import pymysql
        db = pymysql.connect(host = host, user=username, password = password, db = db,
                             cursorclass = pymysql.cursors.DictCursor)
        cur = db.cursor()
        for row in dataset:
            placeholder = ", ".join(["%s"] * len(row))
            stmt = "insert into {table} ({columns}) values ({values});".format(table=table,
                    columns=",".join(row.keys()), values = placeholder)

            cur.execute(stmt, list(row.values()))
        db.commit()
        cur.close()
        db.close()

e = extract()
dataset = e.fromCSV(file_path = 'data/stocks.csv', delimiter = ',')

l=load()
#change these values if necessary to connect to your MySQL instance
l.toMYSQL(host = "localhost", username = "root", password = "admin", db = "test",
          table = "cstocks", dataset = dataset)



#

class load:
    def toCSV(self, file_path, dataset):
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

    def toJSON(self, file_path, dataset):
        if not dataset:
            raise Exception("Input dataset must have at least one item.")
        if not file_path:
            raise Exception("You must provide a valid JSON file path.")
        import json
        with open(file_path, 'w') as jsonfile:
            json.dump(dataset, jsonfile)

    def toMYSQL(self, host, username, password, db, table, dataset):
        if not dataset:
            raise Exception("Input dataset must have at least one item.")
        if not db:
            raise Exception("You must input a valid database name.")
        if not table:
            raise Exception("You must input a valid table name")
        import pymysql
        db = pymysql.connect(host = host, user=username, password = password, db = db,
                             cursorclass = pymysql.cursors.DictCursor)
        cur = db.cursor()
        for row in dataset:
            placeholder = ", ".join(["%s"] * len(row))
            stmt = "insert into {table} ({columns}) values ({values});".format(table=table,
                    columns=",".join(row.keys()), values = placeholder)

            cur.execute(stmt, list(row.values()))
        db.commit()
        cur.close()
        db.close()

    def toMONGODB(self, host, port, username, password, db, collection, dataset):
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



#

use test
db.dropDatabase()
from extract import extract #import our custom built extract module

class load:
    def toCSV(self, file_path, dataset):
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

    def toJSON(self, file_path, dataset):
        if not dataset:
            raise Exception("Input dataset must have at least one item.")
        if not file_path:
            raise Exception("You must provide a valid JSON file path.")
        import json
        with open(file_path, 'w') as jsonfile:
            json.dump(dataset, jsonfile)

    def toMYSQL(self, host, username, password, db, table, dataset):
        if not dataset:
            raise Exception("Input dataset must have at least one item.")
        if not db:
            raise Execption("You must input a valid database name.")
        if not table:
            raise Exception("You must input a valid table name")
        import pymysql
        db = pymysql.connect(host = host, user=username, password = password, db = db,
                             cursorclass = pymysql.cursors.DictCursor)
        cur = db.cursor()
        for row in dataset:
            placeholder = ", ".join(["%s"] * len(row))
            stmt = "insert into {table} ({columns}) values ({values});".format(table=table,
                    columns=",".join(row.keys()), values = placeholder)

            cur.execute(stmt, list(row.values()))
        db.commit()
        cur.close()
        db.close()

    def toMONGODB(self, host, port, username, password, db, collection, dataset):
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

e = extract()
dataset = e.fromCSV(file_path = 'data/stocks.csv', delimiter = ',')

l=load()
#change values here as necessary for your MongoDB instance
l.toMONGODB(host = "localhost", port = 27017, username = "admin", password = "admin",
            db = "test", collection = "cstocks", dataset = dataset)



#









































