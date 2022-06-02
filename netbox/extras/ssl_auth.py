# -*- coding: utf-8 -*-

"""
Use SSL Client Certs for authentication
"""

def _dictify_dn(dn):
    return dict(x.split('=') for x in dn.split('/') if '=' in x)

def user_dict_from_cert(dn):
    print(dn)
    out = dict()
    out['username'] = d['CN']
    out['first_name'] = 'Arno'
    out['last_name'] = 'Nym'
    out['email'] = ''
    return out
