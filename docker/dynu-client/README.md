A dns update client for Dynu

docker run -d --restart=always --name ddns \
  -e DYN_HOSTNAME="${DYN_HOSTNAME}" \
  -e DYN_USER="${DYN_USER}" \
  -e DYN_PASS="${DYN_PASS}" \
  deliganli/dynu:armv7

version: "3"

services:
  ddns:
    container_name: ddns
    image: beringbullet/dynu
    environment:
      - DYN_HOSTNAME=${DYN_HOSTNAME}
      - DYN_USER=${DYN_USER}
      - DYN_PASS=${DYN_PASS}
    restart: always
