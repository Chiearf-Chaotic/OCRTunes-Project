from BasicUtils import array_to_string
import _sqlite3 as connector


class SQLManager:
    def __init__(self, url):
        self.url = url
        self.db = connector.connect(self.url)
        self.cursor = self.db.cursor()

    def change_url(self, new_url):
        self.url = new_url

    def commit_changes(self):
        self.db.commit()

    def close_connection(self):
        self.db.close()
        print("Successfully Closed Connection!")

    def create_table(self, **args):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS {} ({});'''.format(args["name"],
                                                                            array_to_string(args["fields"]).replace("'", "")))
        self.commit_changes()

    def delete_table(self, tblName):
        self.cursor.execute('''DROP TABLE {}.{}'''.format(self.url, tblName))
        self.commit_changes()

    def insert_data(self, **args):
        if "fields" in args.keys():
            self.cursor.execute('''INSERT INTO {}({}) VALUES ({});'''.format(args["name"],
                                                                            array_to_string(str(args["fields"])).replace("'", ""),
                                                                            array_to_string(str(args["values"]))))
        else:
            self.cursor.execute('''INSERT INTO {} VALUES ({});'''.format(args["name"],
                                                                        array_to_string(str(args["values"]))))
        self.commit_changes()

    def update_data(self, **args):
        setters = array_to_string(args["fields"]).replace("'", "")
        self.cursor.execute('''UPDATE {} SET {} WHERE {}'''.format(args["name"], setters, args["condition"]))
        self.commit_changes()

    def select_all_data(self, tbl_name, condition=None):
        if condition is None:
            self.cursor.execute('''SELECT * FROM {}'''.format(tbl_name))
        else:
            self.cursor.execute('''SELECT * FROM {} WHERE {}'''.format(tbl_name, condition))
        self.commit_changes()
        return self.cursor.fetchall()

    def select_certain_data(self, **args):
        if "condition" in args.keys():
            self.cursor.execute('''SELECT {} FROM {} WHERE {}'''.format(array_to_string(args["fields"]).replace("'", ""), args["name"],
                                                                        args["condition"]))
        else:
            self.cursor.execute('''SELECT {} FROM {}'''.format(array_to_string(args["fields"]).replace("'", ""), args["name"]))
        self.commit_changes()
        return self.cursor.fetchmany()
