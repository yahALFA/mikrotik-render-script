from flask import Flask, Response, request
import os

app = Flask(__name__)

@app.route("/")
def mikrotik_script():
    secret_key = "mySecret123"
    header_key = request.headers.get("X-Script-Key")

    if header_key != secret_key:
        return Response("Unauthorized", status=401)

    script = """:local activeCount [/ip hotspot active print count-only]
/log info ("عدد المستخدمين النشطين حالياً: $activeCount")"""
    return Response(script, mimetype='text/plain')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
