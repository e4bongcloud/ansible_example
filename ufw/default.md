---
- hosts: all
  become: true
  tasks:
  - name: Enable firewall
    community.general.ufw:
      state: enabled
  - name: Enable logging
    community.general.ufw:
      logging: on
      state: enabled

  - name: ufw ssh bruteforce attack deny
    ufw:
      rule: limit
      port: ssh
      proto: tcp

  - name: Allow all access from RFC1918 networks to this host
    ufw:
      rule: allow
      src: '{{ item }}'
    loop:
      - 10.0.0.0/8
      - 192.168.0.0/16

  - name: Allow SSH access
    community.general.ufw:
      rule: allow
      port: ssh
      proto: tcp
      src: '{{ item }}'
    loop:
      - 10.0.0.0/8
      - 192.168.0.0/16
