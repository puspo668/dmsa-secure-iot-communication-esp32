from flask import Flask, request, render_template_string

app = Flask(__name__)

received_data = {}

# HOME
@app.route("/")

def home():

    decrypted_text = ""
 
    reverse_rotated = []
    reverse_swapped = []
    reverse_shifted = []

    if received_data:

        # REVERSE ROTATION
        for row in received_data["rotated"]:

            new_row = [row[-1]] + row[:-1]

            reverse_rotated.append(new_row)

        # REVERSE SWAP
        for row in reverse_rotated:

            row = row.copy()

            row[0],row[3] = row[3],row[0]

            reverse_swapped.append(row)

        # REVERSE SHIFT
        for i,row in enumerate(reverse_swapped):

            shift = int(received_data["key"][i % len(received_data["key"])])

            new_row = row[shift:] + row[:shift]

            reverse_shifted.append(new_row)

        # TEXT
        for row in reverse_shifted:

            binary = ''.join(row)

            decrypted_text += chr(int(binary,2))

    return render_template_string("""

    <html>

    <head>

    <meta http-equiv="refresh" content="3">

    <style>

    body{
        background:#0f2027;
        color:white;
        font-family:Arial;
    }

    .box{
        width:1000px;
        margin:20px auto;
        background:#203a43;
        padding:30px;
        border-radius:15px;
    }

    pre{
        background:#111;
        padding:10px;
        border-radius:10px;
        overflow:auto;
    }

    </style>

    </head>

    <body>

    <div class='box'>

    <h1>📥 DMSA Receiver</h1>

    <h2>🌡 Original Sensor Data</h2>
    <pre>{{data.plain}}</pre>

    <h2>🔢 ASCII Conversion</h2>
    <pre>{{data.ascii}}</pre>

    <h2>💻 Binary Conversion</h2>
    <pre>{{data.binary}}</pre>

    <h2>📊 Original Matrix</h2>
    <pre>{{data.matrix}}</pre>

    <h2>🔄 Row Shift Matrix</h2>
    <pre>{{data.shifted}}</pre>

    <h2>🔀 Column Swap Matrix</h2>
    <pre>{{data.swapped}}</pre>

    <h2>♻ Binary Rotation Matrix</h2>
    <pre>{{data.rotated}}</pre>

    <h2>🔒 Cipher Text</h2>
    <pre>{{data.cipher}}</pre>

    <h2>🔓 Decrypted Data</h2>
    <pre>{{decrypted}}</pre>

    </div>

    </body>

    </html>

    """,
    data=received_data,
    decrypted=decrypted_text)

# RECEIVE
@app.route("/receive",methods=["POST"])

def receive():

    global received_data

    received_data = request.json

    return {"status":"success"}

# RUN
if __name__ == "__main__":

    app.run(port=5001)