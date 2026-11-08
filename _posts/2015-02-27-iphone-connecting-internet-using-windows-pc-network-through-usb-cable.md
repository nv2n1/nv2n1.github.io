---
title: "Share Your Windows PC\u2019s Internet with iPhone via USB"
date: 2015-02-27 15:47:30 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/iphone-connecting-internet-using-windows-pc-network-through-usb-cable/
---

Sharing internet from a Windows PC to an iPhone via USB is possible but requires careful network configuration. This is less common than tethering the other direction, but useful when you need a stable wired connection without draining your phone’s battery.

## Prerequisites

- Windows 10 or Windows 11
- iPhone with iOS 12 or later
- USB-A to Lightning or USB-C cable (depending on your iPhone model)
- Administrator access on the PC
- Active internet connection on the PC

This method won’t work reliably on Windows 7 or earlier. For older systems, use Wi-Fi hotspot instead.

## How It Works

When configured correctly, Windows creates a bridge between the iPhone’s USB connection and your PC’s internet adapter. The PC acts as a router, forwarding traffic from the iPhone to the internet:

    iPhone → USB adapter → PC → Internet adapter → ISP

Internet Connection Sharing (ICS) handles the NAT and DHCP configuration automatically. The key is disabling and re-enabling your main internet adapter to reset Windows’ routing table and prevent conflicts.

## Step-by-Step Setup

### Step 1: Open Network Connections

On Windows 11, go to **Settings \> Network & Internet \> Advanced network settings \> More network adapter options**.

On Windows 10, open **Control Panel \> Network and Sharing Center \> Change adapter settings**.

### Step 2: Disable your internet adapter

Right-click your primary internet adapter (usually Ethernet or Wi-Fi, labeled with your connection type). Select **Disable**. This clears the routing table and prevents conflicts during setup.

### Step 3: Connect iPhone via USB

Plug your iPhone into a USB port on the PC with a genuine or MFi-certified cable. Windows should recognize it after a few seconds.

### Step 4: Enable USB sharing on iPhone

On your iPhone, go to **Settings \> General \> Network \> Personal Hotspot** and toggle it on. Then tap **USB Only**.

A new network adapter should appear in Device Manager within 10-15 seconds, typically labeled “Local Area Connection 2” or “Ethernet 2”.

### Step 5: Configure Internet Connection Sharing

In Network Connections, right-click your primary internet adapter and select **Properties**.

Click the **Sharing** tab.

Check **Allow other network users to connect through this computer’s Internet connection**.

From the dropdown menu, select the new USB adapter (the one that appeared when you connected the iPhone).

Click **OK**. Windows may prompt to configure the private network automatically — allow it.

### Step 6: Re-enable your internet adapter

Right-click your primary internet adapter and select **Enable**. Wait 30-60 seconds for it to fully reconnect and establish routing.

### Step 7: Verify connection on iPhone

Open Safari or another browser on your iPhone. Try loading a webpage. If successful, open a terminal on the PC and run:

``` bash
ipconfig /all
```

Check that the iPhone’s USB adapter shows an IP in the 192.168.x.x range. Then verify on your iPhone that its IP matches (Settings \> General \> About \> IP Address).

## Troubleshooting

### No internet despite showing connected

**Check ICS settings:**

- Open Network Connections, right-click your internet adapter, go to **Sharing** tab
- Confirm “Allow other network users…” is checked
- Confirm the iPhone’s USB adapter is selected in the dropdown
- If grayed out, ensure you have administrator privileges

**Restart both devices:**

``` bash
ipconfig /release
ipconfig /renew
```

On iPhone, toggle Personal Hotspot off and on again.

### USB adapter doesn’t appear in Windows

- Try a different USB port (USB 3.0 ports sometimes have better driver support)
- Update iPhone drivers: right-click any Apple device in Device Manager, select **Update driver \> Search automatically**
- On iPhone, unplug and plug back in while Personal Hotspot is already enabled
- Restart both devices completely

### Connection drops frequently

- Use a shorter, high-quality USB cable
- Don’t let the iPhone screen lock during setup (go to Settings \> Display & Brightness \> Auto-Lock and set to Never temporarily)
- Check Windows Event Viewer for network errors: right-click **Start \> Event Viewer \> Windows Logs \> System**, filter for errors with “Network” in the description
- Disable airplane mode on iPhone

### Windows Firewall is blocking traffic

ICS typically bypasses firewall rules, but if you’ve heavily customized your firewall:

``` bash
netsh advfirewall show allprofiles
```

If ICS is still failing, temporarily disable Windows Defender Firewall (Settings \> Privacy & Security \> Windows Security \> Firewall & network protection), test the connection, then re-enable it. If it works without the firewall, you may need to create an exception for the USB adapter.

## When to Use Alternatives

If USB sharing remains unstable, Windows’ built-in **Mobile hotspot** is simpler:

1.  Go to **Settings \> Network & Internet \> Mobile hotspot**
2.  Toggle it on
3.  Connect your iPhone via Wi-Fi to the network name shown

This avoids USB driver issues but uses more battery on the PC and is slightly slower than USB.

If your PC is a laptop on battery, USB tethering will extend total runtime since the iPhone charges while connected, offsetting some power drain.

## Performance Notes

USB internet sharing typically provides 50-100 Mbps on USB 2.0 and up to 480 Mbps theoretical on USB 3.0, though real throughput depends on your PC’s internet speed. It’s stable for browsing, email, and streaming, but less ideal for large file downloads or gaming due to slight latency introduced by the bridging layer.

For temporary connectivity only — say, when your iPhone’s cellular is slow — USB tethering is more reliable than relying on weak Wi-Fi hotspot signals.
