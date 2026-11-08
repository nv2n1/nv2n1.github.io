---
title: "Installing Xen on Fedora 17 as Domain-0"
date: 2013-07-12 16:32:31 +0000
layout: post
canonical: https://www.systutorials.com/installing-xen-domain-0-on-fedora-17/
---

Xen remains relevant for certain production workloads, particularly in cloud infrastructure (AWS EC2, Citrix Hypervisor) and enterprise environments requiring strong VM isolation. However, most Linux distributions now default to KVM for virtualization due to simpler setup and broader ecosystem support. If you’re evaluating hypervisors, consider KVM or container-based solutions like Podman and Kubernetes for new deployments.

This guide covers setting up Xen Domain-0 on modern Fedora (tested on Fedora 41+). The process is significantly simpler than early Xen setups, which required manual kernel patching and compilation. Current Fedora and upstream Linux kernels include native Xen support via PV ops technology.

### Installation

Install Xen and dependencies:

``` bash
dnf install xen xen-libs xen-devel
```

On Fedora 41+, the standard Linux kernel includes Domain-0 support. The toolstack has transitioned from the legacy `xm`/`xend` to `xl`, which is faster and more reliable.

### Configure the Boot Entry

After installation, regenerate the GRUB2 configuration to ensure Xen appears as a boot option:

``` bash
grub2-mkconfig -o /boot/grub2/grub.cfg
```

Enable and start the Xen daemon:

``` bash
systemctl enable xen
systemctl start xen
```

Reboot and select the Xen entry from the GRUB2 menu. After booting into Domain-0, verify the installation:

``` bash
xl info
```

You should see output similar to:

    host                   : myhost.example.com
    release                : 6.8.0-1.fc41.x86_64
    version                : #1 SMP Mon Jan 13 12:34:56 UTC 2025
    machine                : x86_64
    nr_cpus                : 8
    nr_nodes               : 1
    cores_per_socket       : 4
    threads_per_core       : 2
    cpu_mhz                : 3400
    total_memory           : 16384
    free_memory            : 8192
    xen_major              : 4
    xen_minor              : 18
    virt_caps              : hvm
    xen_scheduler          : credit2

### Network Configuration

Network setup is manual and varies by Fedora version and your environment. The legacy NetworkManager integration with Xen is unreliable, so we configure bridges directly.

#### Using Traditional Bridge Networking

Stop and disable NetworkManager:

``` bash
systemctl disable NetworkManager
systemctl mask NetworkManager
systemctl restart networking
```

Create `/etc/sysconfig/network-scripts/ifcfg-xenbr0` for a DHCP-based bridge:

    DEVICE=xenbr0
    TYPE=Bridge
    ONBOOT=yes
    DELAY=0
    BOOTPROTO=dhcp
    IPV6INIT=no

Edit the physical interface configuration (e.g., `/etc/sysconfig/network-scripts/ifcfg-eno1`), replacing it with:

    DEVICE=eno1
    TYPE=Ethernet
    ONBOOT=yes
    BRIDGE=xenbr0
    NM_CONTROLLED=no

Apply the changes:

``` bash
systemctl restart networking
```

Verify the bridge:

``` bash
ip link show
ip addr show xenbr0
```

#### Using Netplan (Alternative)

On systems using Netplan (some Fedora spins), create `/etc/netplan/01-xen-bridge.yaml`:

``` yaml
network:
  version: 2
  ethernets:
    eno1:
      dhcp4: false
  bridges:
    xenbr0:
      interfaces: [eno1]
      dhcp4: true
```

Apply with:

``` bash
netplan apply
```

#### Private Network with Dummy Device

For laptops with only wireless connectivity, create a dummy bridge:

``` bash
#!/bin/bash
# Create dummy bridge for isolated VM network

modprobe dummy
ip link add xenbr0 type bridge
ip link set xenbr0 up
ip addr add 10.0.0.2/16 dev xenbr0

# Enable NAT and forwarding
iptables -I FORWARD -j ACCEPT
iptables -t nat -I POSTROUTING -o wlan0 -j MASQUERADE
echo 1 > /proc/sys/net/ipv4/ip_forward
```

Save as `/usr/local/bin/xen-bridge-setup.sh` and make executable:

``` bash
chmod +x /usr/local/bin/xen-bridge-setup.sh
```

Create a systemd service to run at boot. Create `/etc/systemd/system/xen-bridge.service`:

``` ini
[Unit]
Description=Xen Bridge Setup
After=network-online.target
Wants=network-online.target

[Service]
Type=oneshot
ExecStart=/usr/local/bin/xen-bridge-setup.sh
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target
```

Enable it:

``` bash
systemctl daemon-reload
systemctl enable xen-bridge
systemctl start xen-bridge
```

### Creating a Domain-U Configuration

Create a VM configuration file at `/etc/xen/vm-example.cfg`:

    name = "vm-example"
    vcpus = 2
    memory = 2048
    disk = ['phy:/dev/vg_xen/vm-example-root,xvda,w']
    vif = ['bridge=xenbr0']
    bootloader = "/usr/bin/pygrub"
    on_reboot = "restart"
    on_crash = "restart"

Key options:

- `disk`: Use `phy:` for LVM volumes or raw partitions, `file:` for image files
- `vif`: Defines virtual network interfaces; `bridge=xenbr0` attaches to the bridge
- `bootloader`: Use `pygrub` for PV guests with a bootable kernel, or `hvmloader` for HVM guests
- `vcpus` and `memory`: CPU and RAM allocation

Create the LVM volume first:

``` bash
lvcreate -L 20G -n vm-example-root /dev/vg_xen
```

Start the VM:

``` bash
xl create /etc/xen/vm-example.cfg
xl list
```

### Common xl Commands

- `xl create <config>` — Create and start a domain
- `xl console <domain>` — Attach to serial console
- `xl shutdown <domain>` — Graceful shutdown
- `xl destroy <domain>` — Force shutdown
- `xl reboot <domain>` — Reboot domain
- `xl save <domain> <file>` — Suspend to disk
- `xl restore <file>` — Resume from disk
- `xl vcpu-set <domain> <count>` — Adjust vCPUs (if supported)
- `xl mem-set <domain> <MB>` — Adjust memory (if supported)

Most operations replace the legacy `xm` command directly.

### Troubleshooting

**Domain fails to boot**: Check `/var/log/xen/` for hypervisor messages. Ensure the kernel is Domain-0 compatible.

**Bridge not working**: Verify with `brctl show` and `iptables -t filter -L FORWARD` if NAT is required.

**Console access denied**: Use `xl console <domain>` and ensure the serial console is configured in the guest kernel parameters.

**Memory pressure**: Monitor with `xl info` and `free -h`. Overallocation without ballooning causes performance degradation.
