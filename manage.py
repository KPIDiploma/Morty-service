#!/usr/bin/env python
import os
import sys


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)

#
# if __name__ == '__main__':
#     import hmac
#     import hashlib
#     import rsa
#     import base64
#     import datetime
#
#
#     # from django.conf import settings
#     SANYA_CLINIC_PRIVATE_KEY = {
#         'coef': 4401183538040482587875823978285158131417330169668017981947719886910003590263237349,
#         'd': 7235561538393313013904881722804928933963412790572385574905638073566783357358587140154200735178067948036434460696341672657975502541865722862429896854887137,
#         'e': 65537,
#         'exp1': 5228051118787289033585816110336966585333110189768923402832050990822645981773233137,
#         'exp2': 1229322516917447479319464714279025698411391989781765262722689006524223151,
#         'n': 12394390771888511330465622035794626821013622521648303233816639285588914534345084462139530608550723780799747504415810019868596810914864758238899565020383051,
#         'p': 7274075667621225004651797771334177846484853247285436873477360800491343432636400657,
#         'q': 1703912818374865288838689570875462792056075055185321363345322196573356443,
#     }
#
#     SANYA_CLINIC_PUBLIC_KEY = {
#         'e': 65537,
#         'n': 12394390771888511330465622035794626821013622521648303233816639285588914534345084462139530608550723780799747504415810019868596810914864758238899565020383051
#     }
#
#     # pub, priv = rsa.newkeys(512)
#     pub = rsa.PublicKey(**SANYA_CLINIC_PUBLIC_KEY)
#     priv = rsa.PrivateKey(**SANYA_CLINIC_PRIVATE_KEY)
#
#     timestamp = '2008-09-03T20:56:35.450686Z'
#
#     message = '{}/{}'.format(timestamp, 1).encode()
#
#     hash_text = rsa.encrypt(message, pub)
#
#     test = rsa.decrypt(hash_text, priv).decode()
#
#     get_time, vrach_id = test.split('/')
#
#     time = datetime.datetime.strptime(get_time[:19], '%Y-%m-%dT%H:%M:%S')
#     now_time = datetime.datetime.utcnow()
#     delta = now_time - time
#     # d_hours, remainder = divmod(delta.seconds, 3600)
#     # d_minutes, seconds = divmod(remainder, 60)
#     if delta.seconds > 300:
#         print("LOL")
#     else:
#         print("OK")
#     print(test)
