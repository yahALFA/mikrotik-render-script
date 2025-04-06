from flask import Flask, Response

app = Flask(__name__)

@app.route("/")
def mikrotik_script():
    script = """:local activeCount [/ip hotspot active print count-only]
/log info ("عدد المستخدمين النشطين حالياً: $activeCount")"""
    return Response(script, mimetype='text/plain')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
