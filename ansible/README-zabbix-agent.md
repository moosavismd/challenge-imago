# Zabbix Agent

Monitoring agent setup.

## Configuration

Set in `inventories/group_vars/all.yaml`:

```yaml
agent_param_server: "192.168.10.5"
agent_param_serveractive: "192.168.10.5"
agent_param_hostname: "{{ inventory_hostname }}"
agent_param_listenport: 10050
```

## Usage

```bash
ansible-playbook -i inventories/hosts site.yaml
```

## Features

- Installs Zabbix agent2
- Connects to Zabbix server
- System monitoring
