- hosts: webservers incoming
  become: true
  strategy: free
  gather_facts: no
  tasks:
  - name: webserver http https port allow
    community.general.ufw:
      rule: allow
      proto: tcp
      direction: in
      port: '{{ item }}'
    loop:
      - 80
      - 443
  - name: webserver http https port allow
    community.general.ufw:
      rule: allow
      proto: tcp
      direction: out
      port: '{{ item }}'
    loop:
      - 80
      - 443

- hosts: all
  become: true
  strategy: free
  gather_facts: no
  tasks:
  - name: Allow securityOnion incoming
    community.general.ufw:
      rule: allow
      proto: tcp
      to_ip: 192.168.2.10
      direction: in
      port: '{{ item }}'
    loop:
      - 9200
      - 8090
      - 514
      - 1514
      - 8090
      - 5044
- hosts: all
  become: true
  strategy: free
  gather_facts: no
  tasks:
  - name: Allow securityOnion outcoming
    community.general.ufw:
      rule: allow
      proto: tcp
      to_ip: 192.168.2.10
      direction: out
      port: '{{ item }}'
    loop:
      - 9200
      - 8090
      - 514
      - 1514
      - 8090
      - 5044

- hosts: all
  become: true
  strategy: free
  gather_facts: no
  tasks:
  - name: Allow NFS server access TCP
    community.general.ufw:
      rule: allow
      port: 2049
      src: 10.11.1.3
      proto: '{{ item }}'
      direction: in
    with_items:
      - tcp
      - udp

- hosts: all
  become: true
  strategy: free
  gather_facts: no
  tasks:
  - name: Allow all access to port 53
    community.general.ufw:
      rule: allow
      port: '53'
      direction: in

- hosts: all
  become: true
  strategy: free
  gather_facts: no
  tasks:
  - name: Allow all access to port 53
    community.general.ufw:
      rule: allow
      port: '53'
      direction: out

- hosts: all
  become: true
  strategy: free
  gather_facts: no
  tasks:
  - name: Allow passive mode for VSFTPD
    community.general.ufw:
      rule: allow
      proto: tcp
      to_ip: 10.20.1.2
      direction: in
      port: '{{ item }}'
    loop:
      - 21
      - 10000:10100

- hosts: all
  become: true
  strategy: free
  gather_facts: no
  tasks:
  - name: Allow passive mode for VSFTPD
    community.general.ufw:
      rule: allow
      proto: tcp
      to_ip: 10.20.1.2
      direction: out
      port: '{{ item }}'
    loop:
      - 21
      - 10000:10100

- hosts: all
  become: true
  strategy: free
  gather_facts: no
  tasks:
  - name: Allow kubernetes incoming
    community.general.ufw:
      rule: allow
      proto: tcp
      src: 10.0.0.0/8
      direction: in
      port: '{{ item }}'
    loop:
      - 16443
      - 6443
      - 4001
      - 2379:2380
      - 10250
      - 10251
      - 10252
      - 10255
      - 30000:32767

- hosts: all
  become: true
  strategy: free
  gather_facts: no
  tasks:
  - name: Allow kubernetes outcoming
    community.general.ufw:
      rule: allow
      proto: tcp
      src: 10.0.0.0/8
      direction: out
      port: '{{ item }}'
    loop:
      - 16443
      - 6443
      - 4001
      - 2379:2380
      - 10250
      - 10251
      - 10252
      - 10255
      - 30000:32767

- hosts: all
  become: true
  strategy: free
  gather_facts: no
  tasks:
  - name: Allow kubernetes incoming
    community.general.ufw:
      rule: allow
      proto: tcp
      src: 192.168.2.0/24
      direction: in
      port: '{{ item }}'
    loop:
      - 16443
      - 6443
      - 4001
      - 2379:2380
      - 10250
      - 10251
      - 10252
      - 10255
      - 30000:32767
- hosts: all
  become: true
  strategy: free
  gather_facts: no
  tasks:
  - name: Allow kubernetes outcoming
    community.general.ufw:
      rule: allow
      proto: tcp
      src: 192.168.2.0/24
      direction: out
      port: '{{ item }}'
    loop:
      - 16443
      - 6443
      - 4001
      - 2379:2380
      - 10250
      - 10251
      - 10252
      - 10255
      - 30000:32767


- hosts: all
  gather_facts: no
  become: true
  tasks:
    - name: Outgoing deny
      community.general.ufw:
        state: enabled
        direction: outgoing
        policy: allow

    - name: Incoming deny
      community.general.ufw:
        state: enabled
        policy: allow