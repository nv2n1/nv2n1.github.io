---
title: "Cannot Start VM: Missing Default Network"
date: 2018-03-24 11:51:35 +0000
author: "Weiwei Jia"
layout: post
categories: [programming-languages]
canonical: /cannot-start-vm-with-error-no-network-with-matching-name-default/
---

After a libvirt upgrade, VMs fail to start with the error:

    error: Failed to start domain kvm1
    error: Network not found: no network with matching name 'default'

This happens when the default NAT network (`virbr0`) isn’t automatically created during the upgrade.

## Quick fix: Restore the default network

The fastest solution is to recreate the default network definition. If you have another libvirt host with a working default network, dump its config:

``` bash
sudo virsh net-dumpxml default > default.xml
```

On the affected host, edit `default.xml` and remove the `<uuid>` element — libvirt will generate a new one:

``` xml
<network>
  <name>default</name>
  <forward mode='nat'>
    <nat>
      <port start='1024' end='65535'/>
    </nat>
  </forward>
  <bridge name='virbr0' stp='on' delay='0'/>
  <ip address='192.168.122.1' netmask='255.255.255.0'>
    <dhcp>
      <range start='192.168.122.2' end='192.168.122.254'/>
    </dhcp>
  </ip>
</network>
```

Create the network:

``` bash
sudo virsh net-create default.xml
```

Verify it’s active:

``` bash
sudo virsh net-list
```

## If you don’t have a reference config

You can generate a minimal default network without a template. Use the standard libvirt defaults (192.168.122.0/24 with NAT):

``` bash
cat > default.xml << 'EOF'
<network>
  <name>default</name>
  <forward mode='nat'/>
  <bridge name='virbr0' stp='on' delay='0'/>
  <ip address='192.168.122.1' netmask='255.255.255.0'>
    <dhcp>
      <range start='192.168.122.2' end='192.168.122.254'/>
    </dhcp>
  </ip>
</network>
EOF

sudo virsh net-create default.xml
```

## Firewall backend errors

If you encounter:

    error: Failed to create network from default.xml
    error: internal error: Failed to initialize a valid firewall backend

This occurs when libvirt can’t find a firewall backend. Install the required dependencies:

``` bash
sudo apt-get update
sudo apt-get install firewalld ebtables iptables
```

Then restart libvirtd:

``` bash
sudo systemctl restart libvirtd
```

(On older systems using init.d, replace the above with `sudo /etc/init.d/libvirt-bin restart`)

## Making the network persistent

The `virsh net-create` command creates a transient network that disappears on reboot. To make it permanent, use `virsh net-define`:

``` bash
sudo virsh net-define default.xml
sudo virsh net-start default
sudo virsh net-autostart default
```

Verify it’s persistent:

``` bash
sudo virsh net-list --all
```

The output should show `default` with `Persistent` set to `yes`.

## Verify VM connectivity

Once the default network is running, start your VM and confirm it can reach the host:

``` bash
sudo virsh start kvm1
sudo virsh console kvm1
# Inside the VM:
ip route
ping 192.168.122.1
```

## Network Diagnostic Commands

When troubleshooting network connectivity:

- ping host – Test basic connectivity
- traceroute host – Trace the path packets take
- ss -tulpn – Show listening ports
- ip addr show – Display network interfaces
- nmcli device status – NetworkManager device status
- curl -I url – Check HTTP headers

## Quick Reference

This article covered the essential concepts and commands for the topic. For more information, consult the official documentation or manual pages. The key takeaway is to understand the fundamentals before applying advanced configurations.

Practice in a test environment before making changes on production systems. Keep notes of what works and what does not for future reference.

## 2026 Best Practices and Advanced Techniques

For Cannot Start VM: Missing Default Network, understanding both the fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

## Troubleshooting and Debugging

When issues arise, a systematic approach saves time. Start by checking logs for error messages or warnings. Test individual components in isolation before integrating them. Use verbose modes and debug flags to gather more information when standard output is not enough to diagnose the problem.

## Performance Optimization

- Monitor system resources to identify bottlenecks
- Use caching strategies to reduce redundant computation
- Keep software updated for security patches and performance improvements
- Profile code before applying optimizations
- Use connection pooling and keep-alive for network operations

## Security Considerations

Security should be built into workflows from the start. Use strong authentication methods, encrypt sensitive data in transit, and follow the principle of least privilege for access controls. Regular security audits and penetration testing help maintain system integrity.

## Related Tools and Commands

These complementary tools expand your capabilities:

- Monitoring: top, htop, iotop, vmstat for system resources
- Networking: ping, traceroute, ss, tcpdump for connectivity
- Files: find, locate, fd for searching; rsync for syncing
- Logs: journalctl, dmesg, tail -f for real-time monitoring
- Testing: curl for HTTP requests, nc for ports, openssl for crypto

## Integration with Modern Workflows

Consider automation and containerization for consistency across environments. Infrastructure as code tools enable reproducible deployments. CI/CD pipelines automate testing and deployment, reducing human error and speeding up delivery cycles.

## Quick Reference

This extended guide covers the topic beyond the original article scope. For specialized needs, refer to official documentation or community resources. Practice in test environments before production deployment.
