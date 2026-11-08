---
title: "Managing VirtualBox VMs from the Linux Command Line"
date: 2020-02-29 12:47:30 +0000
layout: post
canonical: https://www.systutorials.com/how-to-list-and-start-virtualbox-vms-in-command-line-in-linux/
---

View all virtual machines registered with VirtualBox:

``` bash
vboxmanage list vms
```

Output example:

    "ubuntu-server" {a1b2c3d4-e5f6-7890-abcd-ef1234567890}
    "debian-test" {b2c3d4e5-f6a7-8901-bcde-f12345678901}
    "centos-prod" {d6c938d8-0bec-57f0-9fd3-8e395ba3d218}

Each VM appears with its name and UUID. The UUID uniquely identifies the VM in VirtualBox’s database.

## List running VMs only

See only active virtual machines:

``` bash
vboxmanage list runningvms
```

This is useful when you have many VMs and need to check what’s currently executing.

## Start a VM

Start a VM by name:

``` bash
vboxmanage startvm ubuntu-server --type headless
```

Or use the UUID:

``` bash
vboxmanage startvm a1b2c3d4-e5f6-7890-abcd-ef1234567890 --type headless
```

Use `--type headless` for server environments. For display-capable systems with the VirtualBox GUI:

``` bash
vboxmanage startvm ubuntu-server --type gui
```

The command returns after launch is initiated, but the guest OS may take additional time to fully boot.

## Stop a VM gracefully

Send an ACPI shutdown signal to the guest OS:

``` bash
vboxmanage controlvm ubuntu-server acpipowerbutton
```

This allows the guest to perform clean shutdown procedures. Allow reasonable time for the guest to power down before issuing another command.

## Force power off a VM

If a VM is hung or unresponsive to graceful shutdown:

``` bash
vboxmanage controlvm ubuntu-server poweroff
```

This immediately terminates the VM without warning—use only when necessary to avoid data corruption.

## Pause and resume a VM

Temporarily suspend a running VM:

``` bash
vboxmanage controlvm ubuntu-server pause
```

Resume it:

``` bash
vboxmanage controlvm ubuntu-server resume
```

This preserves VM state without powering it off, useful for temporary resource freeing.

## Get detailed VM information

View comprehensive details about a specific VM:

``` bash
vboxmanage showvminfo ubuntu-server
```

Output includes CPU count, memory allocation, network configuration, storage devices, and current state. Useful for troubleshooting or verifying VM settings.

Filter for specific information:

``` bash
vboxmanage showvminfo ubuntu-server | grep -E "State:|Memory:|CPUs:"
```

## Check VM state programmatically

Get machine-readable output for scripts:

``` bash
vboxmanage showvminfo ubuntu-server --machinereadable | grep "VMState="
```

Output:

    VMState="running"

This is more reliable than parsing text output and essential for automation.

## List all VMs with their state

Display all VMs and their current state:

``` bash
vboxmanage list vms | while IFS='{}' read -r name uuid; do
  state=$(vboxmanage showvminfo --machinereadable "$name" 2>/dev/null | grep "^VMState=" | cut -d'=' -f2 | tr -d '"')
  printf "%-30s %s\n" "${name//\"/}" "${state:-unknown}"
done
```

This produces a clean formatted list without complex parsing.

## Start multiple VMs with delay

Start several VMs sequentially with spacing between launches:

``` bash
for vm in ubuntu-server debian-test centos-prod; do
  vboxmanage startvm "$vm" --type headless
  if [ $? -eq 0 ]; then
    echo "Started: $vm"
    sleep 5
  else
    echo "Failed to start: $vm" >&2
  fi
done
```

The delay prevents resource contention during boot sequences.

## Shut down all running VMs gracefully

Gracefully shut down every active VM:

``` bash
vboxmanage list runningvms | awk -F'{' '{print $1}' | sed 's/"//g' | while read vm; do
  echo "Shutting down: $vm"
  vboxmanage controlvm "$vm" acpipowerbutton
  sleep 2
done
```

## Wait for all VMs to power down

Use a timeout to ensure all VMs shut down within a time limit:

``` bash
timeout 120 bash -c 'while vboxmanage list runningvms | grep -q .; do sleep 1; done' && echo "All VMs stopped" || echo "Timeout waiting for VMs"
```

This waits up to 120 seconds, checking status every second.

## Automation with error handling

For cron jobs or automated deployment, always use `--type headless`:

``` bash
if vboxmanage startvm myvm --type headless; then
  echo "VM started successfully"
else
  echo "Failed to start VM" >&2
  exit 1
fi
```

For reliable unattended shutdown, combine graceful and force methods:

``` bash
vboxmanage controlvm myvm acpipowerbutton
sleep 30
if vboxmanage list runningvms | grep -q myvm; then
  echo "VM did not shut down gracefully, forcing power off"
  vboxmanage controlvm myvm poweroff
fi
```

## Permissions and access control

VBoxManage requires adequate permissions. Add your user to the vboxusers group:

``` bash
sudo usermod -aG vboxusers $USER
```

Log out and back in for changes to take effect. Verify membership:

``` bash
groups | grep vboxusers
```

For unattended automation outside interactive sessions, use a systemd user service instead of cron. This provides better session management and environment handling:

``` bash
mkdir -p ~/.config/systemd/user
# Create service file with appropriate VM startup commands
systemctl --user daemon-reload
systemctl --user enable vm-startup.service
```

## Common issues and solutions

**UUID vs name**: Both work interchangeably, but names with special characters require quoting.

**Headless mode in cron**: Forgetting `--type headless` in automated contexts causes startup failure when no display is available. Always specify it explicitly.

**ACPI support**: Older guest operating systems may not respond to ACPI shutdown signals. Verify support with `vboxmanage showvminfo <name> | grep -i acpi`.

**State transition delays**: VMs take time to change states. Check actual state with `showvminfo` before issuing conflicting commands in scripts rather than relying on timing assumptions.

**Name parsing in scripts**: Use `awk` or `while read` with proper field separators to avoid issues with spaces in VM names. The UUID approach is safer for automation.
