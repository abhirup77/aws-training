from flask import Flask, render_template

import boto3


app = Flask(__name__)

@app.route("/")
def display_files():

    boto3.setup_default_session(profile_name='mle-intern-emr')
    s3 = boto3.resource('s3')
    my_bucket = s3.Bucket('tiger-mle-pg')
    contents = []
    for object_summary in my_bucket.objects.filter(Prefix="home/abhirup.sahoo/"):
        contents.append(object_summary.key)

    return render_template('storage.html', contents=contents)

if __name__ == '__main__':
    app.run(debug=True)