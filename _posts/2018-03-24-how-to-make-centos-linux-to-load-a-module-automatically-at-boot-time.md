---
title: "Loading a Kernel Module Automatically at Boot on CentOS"
date: 2018-03-24 11:53:32 +0000
layout: post
canonical: https://www.systutorials.com/how-to-make-centos-linux-to-load-a-module-automatically-at-boot-time/
---

To load a kernel module automatically at system startup, create a configuration file in `/etc/modules-load.d/` with a `.conf` extension. The systemd-modules-load.service daemon reads these files during early boot and loads the specified modules.

## Basic method

Create a new configuration file. For the ixgbe driver example:

``` bash
echo "ixgbe" | sudo tee /etc/modules-load.d/ixgbe.conf
```

Or use your editor of choice:

``` bash
sudo nano /etc/modules-load.d/ixgbe.conf
```

Add the module name, one per line:

    ixgbe

Save and reboot to verify the module loads:

``` bash
sudo reboot
```

After reboot, confirm the module is loaded:

``` bash
lsmod | grep ixgbe
```

Or check with modinfo:

``` bash
modinfo ixgbe
```

## Loading multiple modules

If you need to load several related modules, add them all to the same file or create separate files — both approaches work fine:

``` bash
sudo tee /etc/modules-load.d/network-drivers.conf << EOF
ixgbe
bnx2x
mlx5_core
EOF
```

The filename doesn’t matter, only the `.conf` extension. systemd processes all files in the directory, so you can organize them however makes sense for your infrastructure.

## Module dependencies and ordering

systemd-modules-load.service respects module dependencies automatically. If module B depends on module A, listing only B will load both. However, if you need explicit ordering (rare), you can split into multiple files and use numeric prefixes:

``` bash
/etc/modules-load.d/10-base-drivers.conf
/etc/modules-load.d/20-network-drivers.conf
```

Files are processed in lexicographic order, so 10 loads before 20.

## Passing module parameters

If your module requires parameters, use `/etc/modprobe.d/` instead. For example, with ixgbe:

``` bash
sudo tee /etc/modprobe.d/ixgbe.conf << EOF
options ixgbe max_vfs=7
options ixgbe interrupt_type=msix
EOF
```

Then add the module name to `/etc/modules-load.d/` as usual. The parameters defined in modprobe.d are applied when the module loads.

## Troubleshooting

If a module fails to load at boot, check the journal:

``` bash
sudo journalctl -u systemd-modules-load.service
```

Verify the module exists and is available for your kernel:

``` bash
modprobe -l | grep ixgbe
```

If the module isn’t found, you may need to install a dkms package or verify the driver is available for your kernel version.

Test loading the module manually first:

``` bash
sudo modprobe ixgbe
```

If it works manually but not at boot, check for parameter conflicts or missing dependencies in your modprobe.d configuration.

## Checking boot-loaded modules

List all currently loaded modules:

``` bash
lsmod
```

Verify your specific module is present in the output, or use grep for cleaner output:

``` bash
lsmod | grep ixgbe
```

Check when the module was loaded during boot with dmesg:

``` bash
dmesg | grep ixgbe
```

For detailed documentation on the modules-load.d configuration format, consult the man page:

``` bash
man modules-load.d
```

## Troubleshooting Common Issues

When encountering problems on Linux systems, follow a systematic approach. Check system logs first using journalctl for systemd-based distributions. Verify service status with systemctl before attempting restarts. For network issues, use ip addr and ss -tulpn to diagnose connectivity problems.

Package management issues often stem from stale caches. Run dnf clean all on Fedora or apt clean on Ubuntu before retrying failed installations. If a package has unmet dependencies, try resolving them with dnf autoremove or apt autoremove.

## Related System Commands

These commands are frequently used alongside the tools discussed in this article:

- systemctl status service-name – Check if a service is running
- journalctl -u service-name -f – Follow service logs in real time
- rpm -qi package-name – Query installed package information
- dnf history – View package transaction history
- top or htop – Monitor system resource usage

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
