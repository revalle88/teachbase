import redis
import requests

redis_host = "redis"
redis_port = 6379
redis_password = ""


class TbTokenMiddleware:
    def __init__(self, get_response):
        self._get_response = get_response

    def __call__(self, request):
        body = {
            'client_id': '8bdf8070ca5eb1ee7565aa4722e9772a60612310f62f0a04ba4774e7527c836b',
            'client_secret': 'c2c76197cc8de37d0d04a9cc4127ef7bb5c0961d4f96eeec6fff403e30b304dd',
            'grant_type': 'client_credentials'
        }

        try:

            # The decode_repsonses flag here directs the client to convert the responses from Redis into Python strings
            # using the default encoding utf-8.  This is client specific.
            r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True, db=6)
            token = r.get("tb_token")
            # if token is None:
            if True:
                response = requests.post('https://go.teachbase.ru/oauth/token/', json=body)
                resp = response.json()
                token = resp.get('access_token')
                ttl = resp.get('expires_in')
                r.set('tb_token', token)
                r.expire('tb_token', ttl)

            # step 5: Retrieve the hello message from Redis
            request.tb_token = token
        except Exception as e:
            print(e)
        response = self._get_response(request)
        return response
