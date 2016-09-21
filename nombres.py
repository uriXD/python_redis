import redis


r = redis.StrictRedis(host='localhost', port=6379, db=0)


print "Bienvenido al Uri server \n"

Name = raw_input("ingresa Tu nombre: \n")

r.lpush('Names',Name)

print r.lrange('Names','0 -1')



