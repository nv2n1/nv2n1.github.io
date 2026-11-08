---
title: "Resolving UnrecovData 10B8B BadCRC and READ FPDMA QUEUED Errors"
date: 2018-03-24 11:47:16 +0000
layout: post
canonical: https://www.systutorials.com/whats-wrong-with-the-messages-like-unrecovdata-10b8b-badcrc-and-failed-command-read-fpdma-queued-on-linux/
---

These kernel messages from the libata driver indicate SATA link-layer errors between your drive and controller. They look alarming, but they’re usually fixable — and the fix is typically hardware-related, not a software or drive firmware issue.

## What These Error Messages Mean

When you see messages like this in `dmesg`:

    ata4.00: exception Emask 0x10 SAct 0xe000 SErr 0x280100 action 0x6 frozen
    ata4.00: irq_stat 0x08000000, interface fatal error
    ata4: SError: { UnrecovData 10B8B BadCRC }
    ata4.00: failed command: READ FPDMA QUEUED
    ata4: hard resetting link

Here’s what’s happening:

- **BadCRC**: A cyclic redundancy check error occurred at the link layer. The SATA cable or connection failed to transmit data cleanly.
- **UnrecovData**: The interface detected a data integrity error that it couldn’t recover from.
- **10B8B**: An encoding error in the 8B/10B link protocol (used by SATA).
- **READ FPDMA QUEUED**: The command that was executing when the error occurred (FPDMA = First Party Direct Memory Access, a Native Command Queuing operation).
- **Emask 0x10**: ATA bus error (not a drive command error — a hardware communication problem).
- **hard resetting link**: The driver is attempting to recover by resetting the SATA link.

The key thing: **SMART shows no errors** because these are not disk faults — they’re communication faults between the drive and controller.

## Why SMART Checks Pass

Your `smartctl` output looks healthy: SMART overall-health assessment passed, no current pending sectors, no offline uncorrectable sectors, and the UDMA_CRC_Error_Count is only 5 (low). This is actually diagnostic information that narrows down the problem.

If the drive itself were failing, you’d see:

- Current_Pending_Sector \> 0
- Offline_Uncorrectable \> 0
- Reallocated_Sector_Ct increasing
- Raw_Read_Error_Rate spiking rapidly

You have none of these, which means **the drive is fine**.

## Common Causes (In Order of Likelihood)

### 1. Bad or Damaged SATA Cable

BadCRC errors are the strongest indicator of a faulty SATA cable. The cable may have:

- Physical damage or kinks
- Poor connector contacts (especially if the drive is hot-swapped or moved frequently)
- Excessive length or poor shielding
- Internal wire corrosion

**Fix**: Replace the SATA cable with a new one. Use a short, high-quality cable. Test with the new cable before replacing anything else.

### 2. Power Supply Issues

The second most common cause, especially if you see these errors sporadically:

- Loose power connector on the drive or backplane
- Faulty power supply rail (overloaded or failing)
- Poor quality power splitter
- Degraded power supply

**Fix**:

- Check that the SATA power connector is fully seated and not loose.
- If the drive is in an external enclosure or backplane, reseat it.
- Check that your PSU isn’t overloaded (use `turbostat` or monitor power draw).
- Test with a known-good power supply if available.

### 3. Incompatible Drive/Controller Negotiation

Some drive and controller combinations have issues negotiating the SATA speed. The log shows `SATA 3.1, 6.0 Gb/s (current: 3.0 Gb/s)` — your drive supports 6 Gbps but is running at 3 Gbps, which suggests a fallback has already occurred.

**Fix**:

- Try forcing a different SATA speed in BIOS (if available).
- Update the drive firmware to the latest version. For your Seagate ST2000DM001-1CH164, check Seagate’s support site.
- Update the chipset/SATA controller driver or BIOS.

### 4. SATA Controller or Motherboard Issue

Less common, but possible if cables and power check out:

- Faulty SATA port on the motherboard
- Faulty SATA controller

**Fix**:

- Try connecting the drive to a different SATA port on the motherboard.
- If errors persist on the new port, the controller itself may be faulty.

## Diagnostic Steps

### Step 1: Check System Logs in Real-Time

Monitor for error recurrence:

``` bash
journalctl -f | grep -i "ata\|sata"
```

Or watch dmesg as it happens:

``` bash
dmesg -W | grep -i "exception\|sError"
```

### Step 2: Run SMART Extended Self-Test

Your SMART log shows no tests have been run. Run a full scan:

``` bash
smartctl -t long /dev/sdd
```

This takes time (your output suggests ~225 minutes for this drive). Check progress:

``` bash
smartctl -a /dev/sdd | grep "Self-test execution"
```

When done, view results:

``` bash
smartctl -a /dev/sdd | grep -A 20 "Self-test log"
```

### Step 3: Check for Sector Errors

Use `badblocks` to scan for unreadable sectors (this is destructive; only run on unmounted, non-critical drives):

``` bash
badblocks -v /dev/sdd
```

Or non-destructively read-test:

``` bash
badblocks -n /dev/sdd
```

### Step 4: Monitor SATA Link Status

Check the current link speed and state:

``` bash
cat /sys/class/ata_link/link*/sata_spd_limit
cat /sys/class/ata_link/link*/sata_spd
```

If the speed keeps negotiating down (from 6 Gbps to 3 Gbps), that’s a sign of repeated errors forcing fallback.

### Step 5: Test the Cable and Power

- Visually inspect the SATA and power cables for damage.
- Reseat both connections firmly.
- If possible, swap in a different SATA cable.
- If the drive is external, test with a different enclosure or adapter.

## Recovery and Prevention

### If Errors Stop After Cable Replacement

You’ve found your problem. No further action needed beyond replacing any damaged hardware.

### If Errors Continue

1.  Update motherboard BIOS to the latest version.
2.  Try a different SATA port on the motherboard.
3.  If you have another drive, test whether *that* drive has the same issue on the same port (narrows down controller vs. drive vs. cable).
4.  Run the SMART extended self-test to completion to rule out drive failure.

### Preventing Future Issues

- Replace cables every few years if the drive is frequently hot-swapped.
- Keep SATA cables away from power supplies and other heat sources.
- Ensure adequate power supply capacity (20% headroom minimum).
- Don’t overload a single power rail with too many drives.
- Use quality SATA cables and connectors.

## Key Takeaway

These errors are **communication problems, not data loss**. The kernel driver’s recovery mechanism (link reset) works, as evidenced by your log showing `SATA link up 6.0 Gbps` and `EH complete` (error handling complete) after the error sequence. However, repeated errors will eventually exhaust the drive’s reliability. Start with the cheapest fix (a new SATA cable), then move to power and firmware updates if needed.
