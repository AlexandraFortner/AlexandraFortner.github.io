from flask import Flask, render_template, redirect, request
app = Flask(__name__)


@app.route('/')
def root():
    return render_template('base.html')


def main():
    app.run()


if __name__ == '__main__':
    main()