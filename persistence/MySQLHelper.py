# '''
# Created on 18 Jul 2016
#
# @author: xusheng
# '''
# import pymysql.cursors
# from util import EnumUtil
#
# class MySQLHelper(object):
#     '''
#     this class for operate with MySQL DB
#     classdocs
#     '''
#     #masterBO = RoomMasterBO.RoomMaster()
#
#     def __init__(self, params):
#         '''
#         Constructor
#         '''
#
#
#     '''
#     initial the connection
#     '''
#     connection = pymysql.connect(host='db-server',
#                              user='dbguru',
#                              password='password',
#                              db='smartlife',
#                              charset='utf8mb4',
#                              cursorclass=pymysql.cursors.DictCursor);
#     '''
#     method to insert master record
#     '''
#     def InsertRecord(self, tableName, masterBOList):
#         #masterBO = RoomMasterBO.RoomMaster()
#         try:
#             with MySQLHelper.connection.cursor() as cursor:
#                 # Create a new record
#                 for masterBO in masterBOList:
#                     if EnumUtil.TablesEnum.Master == tableName:
#                         sql = "INSERT INTO sr_room_master (title,url, mrt) VALUES (%s, %s, %s)"
#                         cursor.execute(sql, (masterBO.title,masterBO.url, masterBO.mrt))
#                     elif EnumUtil.TablesEnum.Detail == tableName:
#                         sql = "INSERT INTO sr_rental_room (title,url) VALUES (%s, %s)"
#                         cursor.execute(sql, (masterBO.title,masterBO.url))
#
#             # connection is not autocommit by default. So you must commit to save
#             # your changes.
#             MySQLHelper.connection.commit()
#
#         finally:
#             MySQLHelper.connection.close()
#
#     def QueryRecord(self):
#         try:
#             with MySQLHelper.connection.cursor() as cursor:
#                 # Read a single record
#                 sql = "SELECT id, room_id FROM sr_room_master WHERE id=%s"
#                 cursor.execute(sql, (1,))
#                 result = cursor.fetchone()
#                 print(result)
#                 return result
#         finally:
#             MySQLHelper.connection.close()