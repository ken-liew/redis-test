import redis

r = redis.Redis(host='ivh-redis-redis-ha',port=6379')

r.set('foo', 'bar')
value = r.get('foo')
print(value)