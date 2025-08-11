# Zabbix Agent Setup

Uses the official `zabbix.zabbix.agent` role for monitoring.

## Configuration

Set in `inventories/group_vars/all.yaml`:

```yaml
agent_param_server: "37.32.25.44"        # Zabbix server IP
agent_param_serveractive: "37.32.25.44"  # Zabbix server IP
agent_param_hostname: "{{ inventory_hostname }}"
agent_param_listenport: 10050
```

## Usage

```bash
ansible-playbook -i inventories/hosts site.yaml
```

## Features

- Installs Zabbix agent2
- Configures connection to Zabbix server
- Sets up monitoring for infrastructure
