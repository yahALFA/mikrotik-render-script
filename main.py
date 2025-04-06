from flask import Flask, Response
import os

app = Flask(__name__)

@app.route("/")
def mikrotik_script():
    script = """:local activeCount [/ip hotspot active print count-only]
/log info ("عدد المستخدمين النشطين حالياً: $activeCount")"""
    return Response(script, mimetype='text/plain')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
