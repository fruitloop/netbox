# -*- coding: utf-8 -*-

"""
Use SSL Client Certs for authentication
"""

def _dictify_dn(dn):
    # XXX
    with open('/tmp/dictify_dn','a') as f: f.write('line:%s\n\n' % dn)

    return dict(x.split('=') for x in dn.split('/') if '=' in x)

def user_dict_from_cert(dn):
    # XXX
    with open('/tmp/user_dict_from_cert','a') as f: f.write('line:%s\n\n' % dn)

    d = _dictify_dn(dn)
    out = dict()
    out['username'] = d['CN']
    out['first_name'] = ''
    out['last_name'] = ''
    out['email'] = ''
    return out
