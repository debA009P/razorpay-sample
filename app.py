import razorpay
import json

from flask import Flask, render_template, request

app = Flask(__name__,static_folder = "static", static_url_path='')
razorpay_client = razorpay.Client(auth=("rzp_test_Oz0izbPeTpMjdn", "<qwpdhWQuXToKaCRyJoqmlQbv>"))


@app.route('/')
def app_create():
    return render_template('app.html')


@app.route('/charge', methods=['POST'])
def app_charge():
    amount = 11.00
    payment_id = request.form['razorpay_payxment_id']
    razorpay_client.payment.capture(payment_id, amount)
    return json.dumps(razorpay_client.payment.fetch(payment_id))

if __name__ == '__main__':
    app.run()
