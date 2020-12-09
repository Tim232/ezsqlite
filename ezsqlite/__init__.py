import sqlite3

class Database:
    def __init__(self, database: str, table: str, **kwargs):
        self.table = table

        self.con = sqlite3.connect(str(database), **kwargs)
        self.cur = self.con.cursor()
    
    def execute(self, sql: str, *args):
        if args: res = self.cur.execute(sql, args)
        else: res = self.cur.execute(sql)
        self.con.commit()
        return res
    
    def update(self, insert: dict, where: dict = None): self.execute(f'delete from {self.table} where ' + ' and '.join(['='.join(map(str, i)) for i in map(list, where.items())]) + ('' if not where else ' where ' + ' and '.join(['='.join(map(str, i)) for i in map(list, where.items())])))
    def insert(self, *insert): self.execute(f'insert into {self.table} values (' + ','.join(['?' for i in insert]) + ')', tuple(insert))
    def select(self, **where): return list(self.execute(f'select * from {self.table} where ' + ' and '.join(['='.join(map(str, i)) for i in map(list, where.items())])).fetchall())
    def delete(self, **where): return self.execute(f'delete from {self.table} where ' + ' and '.join(['='.join(map(str, i)) for i in map(list, where.items())]))

    def check_same(self, where: str, what): return self.check_one(self.select(where = what))
    def slctall(self): return list(self.execute(f'select * from {self.table}'))
    def check_one(self, cur): bool(len(cur))