from flask import Flask, render_template
import ListeningThread
import pandas

thread = ListeningThread.ListeningThread().start()
app = Flask(__name__, template_folder='./templates', static_folder='./static')

@app.route('/')
def modbus():
    headings = ('src_ip',
               'src_port',
               'dst_ip',
               'dst_port',
               'protocol',
               'src2dst_first_seen_ms',
               'src2dst_last_seen_ms',
               'src2dst_duration_ms',
               'src2dst_packets',
               'src2dst_bytes',
               'dst2src_first_seen_ms',
               'dst2src_last_seen_ms',
               'dst2src_duration_ms',
               'dst2src_packets',
               'dst2src_bytes')
    df = pandas.read_csv('document.csv', header=0)
    # df = pandas.read_csv('test.csv', header=0)
    data = list(df.values)[-10:]
    return render_template('modbus.html', headings=headings, data=data)


if __name__ == '__main__':
    app.run(debug=True)
