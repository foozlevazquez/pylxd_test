## Make cert
```
openssl req -newkey rsa:2048 -nodes \
    -keyout /tmp/lxd.key -out /tmp/lxd.csr
openssl x509 -signkey /tmp/lxd.key -in /tmp/lxd.csr \
    -req -days 3650 -out /tmp/lxd.crt
export LXD_CERT_FILENAME=/tmp/lxd.crt
export LXD_KEY_FILENAME=/tmp/lxd.key
lxc config trust add /tmp/lxd.crt
```

## Setup virtualenv

```
VPY=/tmp/testpylxd
virtualenv -p python3 ${VPY}
${VPY}/bin/pip install pylxd
```


## Run test, note hanging execs.
```
${VPY}/bin/python3 test.py
```
