---
- name: basic secure package download and check
  hosts: all
  tasks:
    - name: Update
      ansible.builtin.apt:
        update_cache: yes
    - name: ufw basic firewall
      ansible.builtin.apt:
        name: ufw
        state: present
    - name: pwquality install
      ansible.builtin.apt:
        name: libpam-pwquality
        state: present