import redis

r = redis.Redis(host='ivh-redis-redis-ha.ns-redis',port=6379)

r.set('foo', 'bar')
value = r.get('foo')
print(value)