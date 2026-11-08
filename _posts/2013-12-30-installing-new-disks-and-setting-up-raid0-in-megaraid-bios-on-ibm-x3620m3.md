---
title: "Setting Up and Verifying RAID 0 on MegaRAID Controllers"
date: 2013-12-30 08:54:10 +0000
modified: 2026-04-11 16:40:36 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /installing-new-disks-and-setting-up-raid0-in-megaraid-bios-on-ibm-x3620m3/
---

RAID0 (striping) on enterprise RAID controllers like Broadcom MegaRAID is used to expose multiple disks as a single logical volume with no redundancy. This configuration is appropriate only for performance-critical workloads where data loss from a single disk failure is acceptable, or for temporary/cache storage. This guide covers the full setup process on servers with MegaRAID controllers.

## Prerequisites

- Physical or IPMI/console access to the server BIOS
- New disk(s) physically installed and detected by the controller
- Clear understanding that RAID0 offers zero fault tolerance — any single disk failure destroys all data on the array
- Controller firmware up to date (check Broadcom’s support site for your specific model)

## Step 1: Initialize Disks to Unconfigured Good Status

New disks arrive in an unconfigured state and must be initialized before RAID configuration.

**Via MegaRAID BIOS Interface:**

1.  Reboot and enter the MegaRAID controller BIOS (typically Ctrl+H during POST; check your server’s boot messages)
2.  Navigate to **Physical View** or **Disk Groups → Physical Disks**
3.  Select the new disk and press Enter
4.  Choose **Make Unconf Good** or **Initialize Disk**
5.  Confirm the operation

The disk status should now display as “Unconf Good” or “Online (Unconfigured)”. Verify disk details—capacity, model, firmware version—in this view. Some newer firmware versions auto-initialize new disks; consult your controller’s release notes if disks appear ready without manual intervention.

## Step 2: Create the RAID0 Array

Once disks show “Unconf Good” status, configure them into a RAID group.

**Via MegaRAID Configuration Wizard:**

1.  From the Home screen, select **Configuration Wizard** or **Add Configuration**
2.  Choose **Manual Configuration** (avoid Auto Configure to maintain control over stripe settings)
3.  Select disk(s) from the left panel and click **Add to Array**
4.  Selected disks appear as a new group on the right
5.  Click **Accept DG** to proceed
6.  Select **Add to SPAN** and confirm the stripe block size:
    - **64KB**: default, suited for random I/O workloads
    - **256KB or larger**: better for sequential I/O (databases, video streaming)
7.  Click **Next** and verify the RAID level shows **RAID0**
8.  Configure read/write cache settings based on your workload:
    - **Write-Through**: safest, no data loss on power failure but slower writes
    - **Write-Back**: faster writes, requires capacitor-backed cache or battery backup
9.  Review the final summary showing all disk assignments and click **Accept**
10. Confirm initialization — the controller writes RAID metadata to all disks

The array initializes in the background. Monitor progress from the Home screen. Initialization time varies with disk size, typically 10-30 minutes. Performance may be reduced during initialization if the init rate is set aggressively.

## Step 3: Verify Configuration in Linux

Reboot into Linux and verify the RAID0 array is recognized by the OS.

**Check for the new logical drive:**

``` bash
lsblk
sudo fdisk -l
```

**For Broadcom MegaRAID (newer controllers) using perccli:**

``` bash
sudo perccli /c0 show
sudo perccli /c0/v0 show
sudo perccli /c0/v0 /all show
```

**For older LSI MegaRAID controllers using MegaCLI:**

``` bash
# Install MegaCLI if not present
sudo apt install megacli    # Debian/Ubuntu
sudo dnf install megacli    # RHEL/Fedora

# Display logical drive info
sudo megacli -LDInfo -Lall -a0

# Display physical disk info
sudo megacli -PDList -a0

# Check controller status
sudo megacli -AdpAllInfo -a0
```

The logical drive should appear as `/dev/sdX` or `/dev/nvmeX` depending on your controller type. Partition and format as needed for your application.

## Important Considerations

### Data Loss Risk

RAID0 provides **zero redundancy**. Use only for:

- Temporary or scratch storage
- Non-critical cache directories
- High-performance cache tiers with external redundancy
- Development/testing environments
- Performance-critical applications (HPC, real-time analytics) where availability is managed at a higher layer

**Never** use RAID0 for primary application storage, databases, or any data you cannot afford to lose.

### Performance Tuning

**Stripe Block Size:** Start with 64KB for mixed workloads. Monitor I/O patterns and adjust if needed:

- Reduce for random I/O-heavy workloads (databases, general-purpose)
- Increase to 256KB+ for sequential workloads (streaming, backups)

**Read/Write Cache:**

- Enable **Write-Back** only if your controller has capacitor-backed cache (CBC) or a battery backup unit (BBU)
- Use **Write-Through** in virtual environments or if power loss risk is high
- Enable **Read-Ahead** for sequential workloads

**Initialization Rate:** Balance init speed against production workload impact:

- Fast init (100%) reduces time but impacts performance
- Slow init (10-30%) spreads load but extends completion time

### Ongoing Monitoring

Check array health regularly:

``` bash
sudo megacli -LDInfo -Lall -a0 | grep State
sudo megacli -PDList -a0 | grep "Firmware state"
```

Watch for:

- **Offline** or **Failed** physical disks — immediate data loss in RAID0
- **Predictive Failures** — replace disks before failure
- High temperature warnings — verify cooling

Set up alerting through your monitoring system (Prometheus, Nagios, etc.) to notify on disk state changes.

### Remote Management

For hands-off deployments, configure RAID through IPMI or Redfish:

``` bash
ipmitool -I lanplus -H <bmc_ip> -U <user> -P <pass> chassis power status
```

Consult your specific controller and server documentation for remote RAID configuration APIs.

## Troubleshooting

**Disks not detected:**

- Verify disks are fully seated in the controller’s backplane
- Check BIOS for drive enumeration
- Update controller firmware to latest version

**RAID0 creation fails:**

- Ensure all disks have identical or compatible firmware versions
- Verify disks are not already assigned to another array
- Check for disk capacity mismatches (larger disks can be used, but wasteful)

**Performance lower than expected:**

- Check stripe block size matches your workload
- Verify cache is properly configured (CBC installed and functioning)
- Monitor for concurrent initialization or background tasks
- Check for host-side I/O bottlenecks (network, CPU, memory)
