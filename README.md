
# Syslog lab

## Overview
Syslog is a standard protocol used for system message logging. It allows network devices like servers, routers, firewalls, and switches to send log or event messages to a centralized log server, known as a Syslog server or collector. In this case, syslog was used to have centralized log management, incident detection and feedling logs into a SIEM tool.

This lab's objectives were to setup a network, configure syslog, categorize logs and configure an IDS. 

The network was setup using docker, suricata was used as a syslog server and an IDS while the logs were categorized using Grafana. Futhermore, Kali Linux was used as an attack machine. It utilized Nikto; a web vulnerability scanner to generate logs. Nginx was the victim machine that was scanned using Nikto. Nginx had an open port 80 which was exploited by Nikto. Moreover, suricata as an IDS was able to detect malicious activity in the network and the logs were aggregated to grafana using loki and promtail. 

Finally, during the lab I encountered challenges of system resources which pivoted me to use docker. Utilizing docker enabled me to have consistency in other labs since I didn't have to start other labs from scratch. In future, I would like to implement a syslog server that collects logs from several machines like ubuntu and apache as virtual machines.




## Run Locally

Clone the project

```bash
  git clone https://github.com/te70/syslab.git
```

Go to the project directory

```bash
  cd syslab
```

Pull containers (make sure docker is already installed)

```bash
  sudo docker compose build
```

Start 

```bash
  sudo docker compose up
```


## Tests

Once docker compose is up, open the Kali Linux container. Nikto has already been installed, run; 

``` bash
    nikto -h <target>

```
where target will be the IP address of nginx.
## License

[MIT](https://choosealicense.com/licenses/mit/)
