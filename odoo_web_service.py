url = "http://localhost:8070"
db = "pilot1"
username = 'erp.support@seatek.vn'
password = "dnremember"

import xmlrpc.client

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
version=common.version()
print("details...", version)


uid = common.authenticate(db, username, password, {})
print("UID", uid)


models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
partners_ids= models.execute_kw(db, uid, password, 'res.partner','search',[[['customer', '=', True]]], {'offset':10, 'limit':10})
print("partners...", partners_ids)

partners_count= models.execute_kw(db, uid, password, 'res.partner','search_count',[[]])
print("partners count...", partners_count)

partner_rec = models.execute_kw(db, uid, password,
    'res.partner', 'read', [partners_ids], {'fields':['id','name']})
print("partner_rec..." )
for partner in partner_rec:
    print(partner)

abcd = models.execute_kw(db, uid, password,
    'res.partner', 'search_read',[[]],
    {'fields': ['id', 'name'], 'limit': 10})
print("Search Read Result",abcd)
for ab in abcd:
    print(ab)

