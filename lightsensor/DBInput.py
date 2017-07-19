# _*_ coding: utf-8 _*_
import MySQLdb
import json
import collections

if __name__ == "__main__":
	
    connector = MySQLdb.connect(host="localhost",db="j14010",user="root",passwd="teikyo",charset="utf8")
    cursor = connector.cursor()


    f = open('data.json', 'r')
    json_dict = json.load(f, object_pairs_hook=collections.OrderedDict)
    f.close()

    for index in json_dict:
        sql = "insert into sensors (value) values(" + str(json_dict[index]) + ")"
        cursor.execute(sql)


    connector.commit()
    cursor.close()
    connector.close()

