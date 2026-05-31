from flask import Flask, render_template_string, request
import serial
import requests

app = Flask(__name__)

# SERIAL
try:

    esp32 = serial.Serial('COM8',115200)

except:

    esp32 = None

latest_data = "Waiting Sensor Data..."

# HOME
@app.route("/")

def home():

    global latest_data

    # SENSOR READ
    if esp32:

        try:

            latest_data = esp32.readline().decode().strip()

        except:

            latest_data = "Sensor Read Error"

    else:

        latest_data = "ESP32 Not Connected"

    return render_template_string("""

    <html>

    <head>

    <meta http-equiv="refresh" content="3">

    <style>

    body{
        background:#141e30;
        color:white;
        font-family:Arial;
    }

    .box{
        width:800px;
        margin:40px auto;
        background:#243b55;
        padding:30px;
        border-radius:15px;
    }

    pre{
        background:#111;
        padding:10px;
        border-radius:10px;
    }

    button{
        padding:12px 25px;
        background:#00c6ff;
        border:none;
        border-radius:10px;
        font-weight:bold;
        cursor:pointer;
    }

    </style>

    </head>

    <body>

    <div class='box'>

    <h1>📤 DMSA Sender</h1>

    <h2>🌡 Real-Time Sensor Data</h2>

    <pre>{{data}}</pre>

    <form method="POST" action="/send">

    <button type="submit">

    Send To Receiver

    </button>

    </form>

    </div>

    </body>

    </html>

    """,data=latest_data)

# SEND
@app.route("/send",methods=["POST"])

def send():

    global latest_data

    key = "21211"

    # ASCII
    ascii_values = [ord(c) for c in latest_data]

    # BINARY
    binary_values = [format(x,'08b') for x in ascii_values]

    # MATRIX
    matrix = []

    for b in binary_values:

        matrix.append(list(b))

    # ROW SHIFT
    shifted = []

    for i,row in enumerate(matrix):

        shift = int(key[i % len(key)])

        new_row = row[-shift:] + row[:-shift]

        shifted.append(new_row)

    # COLUMN SWAP
    swapped = []

    for row in shifted:

        row = row.copy()

        row[0],row[3] = row[3],row[0]

        swapped.append(row)

    # ROTATION
    rotated = []

    for row in swapped:

        new_row = row[1:] + [row[0]]

        rotated.append(new_row)

    # CIPHER
    cipher = ""

    for row in rotated:

        binary = ''.join(row)

        cipher += chr(int(binary,2))

    result = {

        "plain":latest_data,

        "ascii":ascii_values,

        "binary":binary_values,

        "matrix":matrix,

        "shifted":shifted,

        "swapped":swapped,

        "rotated":rotated,

        "cipher":cipher,

        "key":key
    }

    try:

        requests.post(
            "http://127.0.0.1:5001/receive",
            json=result
        )

        return """

        <script>

        alert("Data Sent Successfully!");

        window.location.href="/";

        </script>

        """

    except:

        return """

        <script>

        alert("Receiver Not Running!");

        window.location.href="/";

        </script>

        """

# RUN
if __name__ == "__main__":

    app.run(port=5000)