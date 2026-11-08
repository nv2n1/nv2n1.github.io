---
title: "Installing and Configuring MySQL Cluster on CentOS 6.3"
date: 2018-03-24 08:14:16 +0000
author: "Q A"
layout: post
canonical: https://www.systutorials.com/how-to-install-and-configure-a-mysql-cluster-on-centos-rhel-6-3/
---

MySQL Cluster uses NDB (Network Database) storage engine to provide high availability and data redundancy across multiple nodes. This guide covers installation and configuration on modern RHEL-compatible systems.

### Prerequisites

- Three or more servers (minimum: one management node, two data nodes, one SQL node)
- Rocky Linux 9 or AlmaLinux 9
- Root or sudo access
- Static IP addresses on all nodes
- Network connectivity between all cluster nodes

### System Preparation

Update all systems and install dependencies:

``` bash
sudo dnf update -y
sudo dnf install -y gcc make cmake libaio-dev libnuma-dev openssl-devel
```

Disable SELinux for cluster communication (or configure appropriate policies):

``` bash
sudo setenforce 0
sudo sed -i 's/^SELINUX=.*/SELINUX=disabled/' /etc/selinux/config
```

Create the mysql user and directories:

``` bash
sudo useradd -r -s /bin/false mysql
sudo mkdir -p /var/lib/mysql-cluster/{data,logs}
sudo chown -R mysql:mysql /var/lib/mysql-cluster
```

### Download and Install MySQL Cluster

Download the latest MySQL NDB Cluster binaries from mysql.com:

``` bash
cd /tmp
wget https://dev.mysql.com/get/Downloads/MySQL-Cluster-9.0/mysql-cluster-9.0.36-linux-glibc2.28-x86_64.tar.gz
sudo tar xzf mysql-cluster-9.0.36-linux-glibc2.28-x86_64.tar.gz -C /opt
sudo ln -s /opt/mysql-cluster-9.0.36-linux-glibc2.28-x86_64 /opt/mysql-cluster
```

Set permissions and add to PATH:

``` bash
sudo chown -R mysql:mysql /opt/mysql-cluster
echo 'export PATH=/opt/mysql-cluster/bin:$PATH' | sudo tee -a /etc/profile.d/mysql-cluster.sh
source /etc/profile.d/mysql-cluster.sh
```

### Configure Management Node

Create the management node configuration:

``` bash
sudo mkdir -p /etc/mysql-cluster
sudo tee /etc/mysql-cluster/config.ini > /dev/null <<'EOF'
[ndbd default]
NoOfReplicas=2
MaxNoOfConcurrentOperations=32000
HeartbeatIntervalMgmt=1500
HeartbeatInterval=3000
DataMemory=2G
IndexMemory=512M
SharedMemory=0

[ndb_mgmd]
Id=1
Hostname=192.168.1.10
LogDestination=FILE:/var/lib/mysql-cluster/logs/ndb_mgmd.log

[ndbd]
Id=2
Hostname=192.168.1.11
DataDir=/var/lib/mysql-cluster/data

[ndbd]
Id=3
Hostname=192.168.1.12
DataDir=/var/lib/mysql-cluster/data

[mysqld]
Id=4
Hostname=192.168.1.13
EOF
```

Adjust memory settings based on your hardware. Replace IPs with your actual node addresses.

Initialize and start the management node:

``` bash
sudo /opt/mysql-cluster/bin/ndb_mgmd -f /etc/mysql-cluster/config.ini \
  --configdir=/var/lib/mysql-cluster/data
```

Create a systemd service for the management node:

``` bash
sudo tee /etc/systemd/system/ndb-mgmd.service > /dev/null <<'EOF'
[Unit]
Description=MySQL NDB Management Node
After=network.target

[Service]
Type=simple
User=mysql
ExecStart=/opt/mysql-cluster/bin/ndb_mgmd -f /etc/mysql-cluster/config.ini --configdir=/var/lib/mysql-cluster/data
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl enable --now ndb-mgmd
```

### Configure Data Nodes

On each data node, create the startup configuration:

``` bash
sudo tee /etc/mysql-cluster/my.cnf > /dev/null <<'EOF'
[mysqld_safe]
ndb-connectstring=192.168.1.10

[mysqld]
ndb-connectstring=192.168.1.10
default-storage-engine=ndbcluster
EOF
```

Initialize the NDB data directory:

``` bash
sudo /opt/mysql-cluster/bin/ndb_mgmd --version
sudo /opt/mysql-cluster/bin/ndbd -c 192.168.1.10 --initial
```

Create a systemd service for data nodes:

``` bash
sudo tee /etc/systemd/system/ndbd.service > /dev/null <<'EOF'
[Unit]
Description=MySQL NDB Data Node
After=network.target ndb-mgmd.service

[Service]
Type=simple
User=mysql
ExecStart=/opt/mysql-cluster/bin/ndbd -c 192.168.1.10
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl enable --now ndbd
```

### Configure SQL Node

Initialize the MySQL database on the SQL node:

``` bash
sudo /opt/mysql-cluster/bin/mysqld --initialize-insecure --user=mysql
```

Update the SQL node MySQL configuration:

``` bash
sudo tee /etc/my.cnf > /dev/null <<'EOF'
[mysqld]
ndb-connectstring=192.168.1.10
default-storage-engine=ndbcluster
bind-address=192.168.1.13
EOF
```

Start MySQL:

``` bash
sudo /opt/mysql-cluster/bin/mysqld_safe &
```

### Verify Cluster Status

Connect to the management node console:

``` bash
ndb_mgm -e "show"
```

You should see output showing all nodes as connected. From the SQL node, verify cluster tables:

``` bash
mysql -u root -e "SELECT * FROM INFORMATION_SCHEMA.ENGINES WHERE ENGINE='ndbcluster';"
```

### Performance Tuning

Key parameters to adjust based on workload:

- `DataMemory`: Increase for large datasets (typically 50-80% of available RAM)
- `IndexMemory`: Set to 10-20% of DataMemory
- `MaxNoOfConcurrentOperations`: Tune based on concurrent connections
- `HeartbeatInterval`: Lower values increase cluster sensitivity to network latency

Monitor cluster health with:

``` bash
ndb_mgm -e "all report MemoryUsage"
ndb_mgm -e "all report BackupStatus"
```

Enable backups via the management console for disaster recovery.

## 2026 Comprehensive Guide: Best Practices

This extended guide covers Installing and Configuring MySQL Cluster on CentOS 6.3 with advanced techniques and troubleshooting tips for 2026. Following modern best practices ensures reliable, maintainable, and secure systems.

## Advanced Implementation Strategies

For complex deployments, consider these approaches: Infrastructure as Code for reproducible environments, container-based isolation for dependency management, and CI/CD pipelines for automated testing and deployment. Always document your custom configurations and maintain separate development, staging, and production environments.

## Security and Hardening

Security is foundational to all system administration. Implement layered defense: network segmentation, host-based firewalls, intrusion detection, and regular security audits. Use SSH key-based authentication instead of passwords. Encrypt sensitive data at rest and in transit. Follow the principle of least privilege for access controls.

## Performance Optimization

- Monitor resources continuously with tools like top, htop, iotop
- Profile application performance before and after optimizations
- Use caching strategically: application caches, database query caching, CDN for static assets
- Optimize database queries with proper indexing and query analysis
- Implement connection pooling for network services

## Troubleshooting Methodology

Follow a systematic approach to debugging: reproduce the issue, isolate variables, check logs, test fixes. Keep detailed logs and document solutions found. For intermittent issues, add monitoring and alerting. Use verbose modes and debug flags when needed.

## Related Tools and Utilities

These tools complement the techniques covered in this article:

- System monitoring: htop, vmstat, iostat, dstat for resource tracking
- Network analysis: tcpdump, wireshark, netstat, ss for connectivity debugging
- Log management: journalctl, tail, less for log analysis
- File operations: find, locate, fd, tree for efficient searching
- Package management: dnf, apt, rpm, zypper for package operations

## Integration with Modern Workflows

Modern operations emphasize automation, observability, and version control. Use orchestration tools like Ansible, Terraform, or Kubernetes for infrastructure. Implement centralized logging and metrics. Maintain comprehensive documentation for all systems and processes.

## Quick Reference Summary

This comprehensive guide provides extended knowledge for Installing and Configuring MySQL Cluster on CentOS 6.3. For specialized requirements, refer to official documentation. Practice in test environments before production deployment. Keep backups of critical configurations and data.
