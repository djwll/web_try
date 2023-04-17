from flask import Flask, render_template , request

app = Flask(__name__)
#创建了网址/show/info/，和函数index的对应关系
#以后用户在浏览器上访问/show/info，网站自动执行 index

@app.route("/show/info")#装饰器
def index():
    return render_template("index.html")

@app.route("/get/more")#装饰器
def get_news():
    return render_template("get_more.html")

@app.route("/xiaomi/get")#装饰器
def get_xiaomi():
    return render_template("xiaomi.html")

@app.route("/register")
def do_register():
    return render_template("register.html")

@app.route("/post/reg", method=["GET"])
def post_register():
    return "注册成功"
if __name__ =="__main__":
    app.run()
