from pysendpulse.pysendpulse import PySendPulse

REST_API_ID = 'cc52c1fdb1a2e780f67933823ef39cb6'
REST_API_SECRET = '9a862107101e063ae3956a78f07d6b8c'
TOKEN_STORAGE = 'memcached'
MEMCACHED_HOST = '127.0.0.1:11211'
SENDER_NAME = 'osman'
SPApiProxy = PySendPulse(REST_API_ID, REST_API_SECRET, TOKEN_STORAGE, memcached_host=MEMCACHED_HOST)

# Send sms by some phones
phones_for_send = [
    '8801784835226'
]
SPApiProxy.sms_send(SENDER_NAME, phones_for_send, 'test')
