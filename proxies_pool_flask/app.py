import random

from flask import Flask, redirect, url_for, render_template
import redis
app = Flask(__name__)


@app.route('/proxies')
def one_proxie():
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    list = r.srandmember('ip_port_list', number=-1)

    return random.choice(list)


@app.route('/')
def proxie():

    return redirect(url_for('one_proxie'))


@app.route('/del_proxie/<ip>')
def del_proxie(ip):
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    r.srem("ip_port_list", ip)
    return redirect(url_for('one_proxie'))


@app.route('/proxies/all', methods=['GET'])
def all_proxie():
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    list = r.smembers('ip_port_list')

    return render_template('all_proxie.html', list=list)


@app.errorhandler(404)
def catch_404(error):

    return '<h1>404</h1>'


if __name__ == '__main__':
    app.run()
