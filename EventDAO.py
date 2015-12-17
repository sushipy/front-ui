# coding: utf-8

import MySQLdb

class Event:
    def __init__(self):
        self._connect()
        return

    def _connect(self):
        self.connection = MySQLdb.connect(\
            host="10.194.23.240", \
            db="bmi22", \
            user="bmi22", \
            passwd="bmi22")
        return

    def _disconnect(self):
        self.connection.close()
        return

    def _get_cursor(self):
        self.connection.cursorclass = MySQLdb.cursors.DictCursor
        return self.connection.cursor()

    # 新規イベント作成
    def create(self, query_array):
        cursor = self._get_cursor()
        stmt = ("insert into event "
#                "(date, ftime, time, title, room, promotor_name, promotor_mail, capacity, descri, agenda, note, participant) "
#                "values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
                "(date, ftime, time, title, room, promotor_name, promotor_mail, capacity, descri, agenda, note) "
                "values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        data = query_array
        cursor.execute(stmt, data)
        self.connection.commit()
        cursor.close()
        self._disconnect()
        return

    # 全イベント一覧取得
    def find_event_all(self):
        cursor = self._get_cursor()
#        stmt = "select date, ftime, time, title, room, promotor_name, promotor_mail, capacity, descri, agenda, note, participant from event"
        stmt = "select id, date, ftime, time, title, room, promotor_name, promotor_mail, capacity, descri, agenda, note from event"

        cursor.execute(stmt)
        rows = cursor.fetchall()
        cursor.close()
        self._disconnect()
        return rows

    # イベント更新
    # 排他制御は未実装・・・
    def update(self, id, query_array):
        cursor = self._get_cursor()
        stmt = ("update event "
                "set date=%s, ftime=%s, time=%s, title=%s, room=%s, promotor_name=%s, promotor_mail=%s, capacity=%s, descri=%s, agenda=%s, note=%s, participant=%s "
                "where id=%s")
        query_array.append(id)
        data = query_array
        cursor.execute(stmt, data)
        self.connection.commit()
        cursor.close()
        self._disconnect()
        return

    # イベント参加
    def participate(self, id, participant_name):
        cursor = self._get_cursor()

        # 更新前のイベント参加人数取得
        #stmt_select = ("select participant from event "
        #               "where id=%s")
        #cursor.execute(stmt_select, id)
        #row = cursor.fetchall()

        # 参加者名登録
        stmt_insert = ("insert into participate_history "
                       "(id, participant_name) "
                       "values (%s, %s)")
        data = [id, participant_name]
        cursor.execute(stmt_insert, data)

        # 参加者人数更新
        #stmt_update = ("update event "
        #               "set participant=%s "
        #               "where id=%s")
        #participant = row[0]["participant"] + 1
        #data = [participant, id]
        #cursor.execute(stmt_update, data)

        self.connection.commit()
        cursor.close()
        self._disconnect()
        return

    # 全参加者リスト取得
    def find_participants_all(self, id):
        cursor = self._get_cursor()
        stmt = "select event.title, participant_name from participate_history inner join event on (participate_history.id = event.id)"
        cursor.execute(stmt)
        rows = cursor.fetchall()
        cursor.close()
        self._disconnect()
        return rows

    # イベント検索（イベント名で）
    def find_by_name(self, name):
        cursor = self._get_cursor()
        stmt = ("select date, ftime, time, title, room, promotor_name, promotor_mail, capacity, descri, agenda, note, participant from event "
                "where title=%s")
        data = [name]
        cursor.execute(stmt, data)
        rows = cursor.fetchall()
        cursor.close()
        self._disconnect()
        return rows
