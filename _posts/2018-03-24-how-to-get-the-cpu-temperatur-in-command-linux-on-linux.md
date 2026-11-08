---
title: "How to Check CPU Temperature in Linux"
date: 2018-03-24 11:50:17 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-get-the-cpu-temperatur-in-command-linux-on-linux/
---

Most modern systems have thermal sensors built into the CPU and motherboard. Reading these sensors is essential for monitoring system health, diagnosing performance issues, and preventing thermal throttling or hardware damage.

## Install lm-sensors

The standard tool for reading hardware sensors on Linux is `lm-sensors`. Install it on your system:

**Debian/Ubuntu:**

``` bash
sudo apt install lm-sensors
```

**RHEL/CentOS/Fedora:**

``` bash
sudo dnf install lm_sensors
```

**Arch:**

``` bash
sudo pacman -S lm_sensors
```

After installation, run the sensor detection:

``` bash
sudo sensors-detect
```

This interactive script probes your hardware and configures the kernel modules needed to read sensors. Answer `yes` to most prompts to enable detection of all available sensors.

## Reading CPU Temperature

Once configured, use the `sensors` command to display all detected temperatures:

``` bash
sensors
```

You’ll see output like this:

    coretemp-isa-0000
    Adapter: ISA adapter
    Core 0:       +52.0°C  (high = +100.0°C, crit = +100.0°C)
    Core 1:       +48.0°C  (high = +100.0°C, crit = +100.0°C)
    Core 2:       +50.0°C  (high = +100.0°C, crit = +100.0°C)
    Core 3:       +49.0°C  (high = +100.0°C, crit = +100.0°C)

## Extract Specific Core Temperature

If you need to extract a single core’s temperature programmatically, use `sensors -u` for uniform output:

``` bash
sensors -u | grep "Core 0" | grep "input" | awk '{print $2}'
```

For a cleaner approach with better parsing:

``` bash
sensors -A -u coretemp-isa-0000 | awk '/Core 0:/{getline; print $2}'
```

Or using `grep` and `cut`:

``` bash
sensors | grep "Core 0" | awk '{print $3}' | tr -d '°C'
```

## Get Average CPU Temperature

To get the average temperature across all cores:

``` bash
sensors -A -u | grep "input" | awk '{sum+=$2; count++} END {print sum/count}'
```

## Monitor Temperature in Real-Time

For continuous monitoring, use `watch`:

``` bash
watch -n 1 sensors
```

This refreshes the output every second.

## Alternative: psensors

For a GUI alternative, install `psensors`:

``` bash
sudo apt install psensors
```

Then run `psensors` to display a graphical interface.

## Scripting Example

Here’s a practical script to log CPU temperatures:

``` bash
#!/bin/bash

while true; do
    timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    temp=$(sensors -A -u coretemp-isa-0000 | grep "input" | head -1 | awk '{print $2}')
    echo "$timestamp: $temp°C" >> /var/log/cpu_temp.log
    sleep 60
done
```

Run this in the background or via cron to periodically log temperatures for trend analysis.

## Troubleshooting

If `sensors` returns no output or error messages:

- Verify the kernel module is loaded: `lsmod | grep coretemp`
- Load it manually: `sudo modprobe coretemp`
- Check your BIOS settings — some systems disable sensor access
- On virtual machines, sensors may not be available at all

## Check Maximum Temperature Support

View the critical temperature threshold for your CPU:

``` bash
sensors | grep "crit"
```

Most modern Intel and AMD CPUs safely handle up to 100°C, but throttling typically starts at 80-90°C depending on the processor.

## 2026 Best Practices and Advanced Techniques

For How to Check CPU Temperature in Linux, understanding both the fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

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
