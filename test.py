#!/home/ivan/pylxd_test_vpy3/bin/python

#   $ openssl req -newkey rsa:2048 -nodes \
#       -keyout /tmp/lxd.key -out /tmp/lxd.csr
#   $ openssl x509 -signkey /tmp/lxd.key -in /tmp/lxd.csr \
#       -req -days 3650 -out /tmp/lxd.crt
#   $ lxc config trust add /tmp/lxd.crt
#
# When running tests:
# set env vars LXD_CERT_FILENAME and LXD_KEY_FILENAME to point to .crt and
# .key above
# i.e.
#
#   $ export LXD_CERT_FILENAME=/tmp/lxd.crt
#   $ export LXD_KEY_FILENAME=/tmp/lxd.key

import os

from datetime import datetime, timedelta
import pylxd

# Insert local LXD server here
endpoint = 'https://10.20.5.1:8443'

_cert = os.getenv("LXD_CERT_FILENAME")
_key = os.getenv("LXD_KEY_FILENAME")

cert = (_cert, _key)

client = pylxd.Client(endpoint=endpoint, cert=cert, verify=False)
inst_name = 'pytest-lxd-foo2'
image_name = 'ubuntu/focal'

cfg = {'name': inst_name,
       'source': {'type': 'image', 'alias': image_name},
       }

instance = client.instances.create(cfg, wait=True)
instance.start(wait=True)

while True:
    start = datetime.utcnow()
    instance.execute(['hostname'])
    print(datetime.utcnow() - start)
