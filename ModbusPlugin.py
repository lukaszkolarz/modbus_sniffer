from nfstream import NFPlugin
import csv
import datetime

headers = ['src_ip',
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
           'dst2src_bytes']


class Plugin(NFPlugin):
    def on_update(self, packet, flow):
        if packet.protocol == 6:
            protocol = 'TCP'
        else:
            protocol = "NO_TCP"
        if (packet.dst_port == 5020) or (packet.src_port == 5020):
            myCsvRow = {'src_ip': packet.src_ip,
                        'src_port': packet.src_port,
                        'dst_ip': packet.dst_ip,
                        'dst_port': packet.dst_port,
                        'protocol': protocol,
                        'src2dst_first_seen_ms': datetime.datetime.fromtimestamp(flow.src2dst_first_seen_ms / 1e3),
                        'src2dst_last_seen_ms': datetime.datetime.fromtimestamp(flow.src2dst_last_seen_ms / 1e3),
                        'src2dst_duration_ms': flow.src2dst_duration_ms,
                        'src2dst_packets': flow.src2dst_packets,
                        'src2dst_bytes': flow.src2dst_bytes,
                        'dst2src_first_seen_ms': datetime.datetime.fromtimestamp(flow.dst2src_first_seen_ms / 1e3),
                        'dst2src_last_seen_ms': datetime.datetime.fromtimestamp(flow.dst2src_last_seen_ms / 1e3),
                        'dst2src_duration_ms': flow.dst2src_duration_ms,
                        'dst2src_packets': flow.dst2src_packets,
                        'dst2src_bytes': flow.dst2src_bytes}

            with open('document.csv', 'a') as f:
                writer = csv.DictWriter(f, fieldnames=headers)
                writer.writerow(myCsvRow)
                f.close()

            return
