---
title: "Installing RTL8192CU WiFi Driver on CentOS 7"
date: 2018-03-24 11:50:52 +0000
layout: post
canonical: https://www.systutorials.com/rtl8192cu-driver-for-centos-7/
---

\[md\]\
The RTL8192cu is a legacy USB WiFi adapter that’s still in use, but it has known stability issues on modern kernels. If your adapter keeps dropping connections or fails to resume after sleep, you’re likely hitting the same power management bug that affects many devices.

\## Disable Power Management

The most reliable workaround is to disable power management in the driver. Create `/etc/modprobe.d/8192cu-disable-power-management.conf`:

```wp-block-code
sudo tee /etc/modprobe.d/8192cu-disable-power-management.conf > /dev/null << 'EOF'
# Disable power management in the 8192cu driver
# Works around a bug where the device fails to wake from suspend
# rtw_power_mgnt=0 disables power saving
# rtw_enusbss=0 disables USB autosuspend
options 8192cu rtw_power_mgnt=0 rtw_enusbss=0
EOF
```

Then rebuild your initramfs and reboot:

```wp-block-code
sudo dracut -f
sudo reboot
```

\## Verify the Settings Are Applied

After rebooting, check that the module loaded with the correct parameters:

```wp-block-code
cat /sys/module/8192cu/parameters/rtw_power_mgnt
cat /sys/module/8192cu/parameters/rtw_enusbss
```

Both should return `0`.

You can also monitor the driver in real-time:

```wp-block-code
dmesg | grep 8192cu
iwconfig wlan0
```

Check the connection quality:

```wp-block-code
iwconfig wlan0 | grep -i quality
iwconfig wlan0 | grep -i "signal level"
```

\## Alternative: Build from Source

If the prebuilt driver is unavailable or unstable, compile the driver from the maintained fork:

```wp-block-code
# Install build dependencies
sudo yum groupinstall "Development Tools"
sudo yum install kernel-devel

# Clone and build
git clone https://github.com/pvaret/rtl8192cu-fixes.git
cd rtl8192cu-fixes
make
sudo make install
sudo depmod -a
sudo modprobe 8192cu
```

Then apply the same modprobe configuration above to disable power management.

Blacklist the default driver to avoid conflicts:

```wp-block-code
echo "blacklist rtl8192cu" | sudo tee /etc/modprobe.d/blacklist-rtl8192cu.conf
```

\## NetworkManager Integration

If you're using NetworkManager, it may conflict with manual driver configuration. Ensure NetworkManager is managing the WiFi interface:

```wp-block-code
nmcli device status
nmcli connection show
```

If the device shows as `unmanaged`, add it to NetworkManager's control:

```wp-block-code
sudo nmcli device set wlan0 managed yes
```

Connect to a network:

```wp-block-code
nmcli device wifi connect "SSID" password "password"
```

\## Troubleshooting Common Issues

\*\*Adapter not recognized:\*\*

```wp-block-code
lsusb | grep -i realtek
dmesg | grep -i usb | grep -i 8192
```

\*\*Connection drops periodically:\*\*

This is the power management bug. Ensure the modprobe configuration is loaded:

```wp-block-code
cat /etc/modprobe.d/8192cu-disable-power-management.conf
```

\*\*Slow speeds:\*\*

Try forcing a specific channel or disabling 802.11n:

```wp-block-code
iwconfig wlan0 channel 6
# Or disable 802.11n if causing issues
echo 'options 8192cu rtw_power_mgnt=0 rtw_enusbss=0' | sudo tee /etc/modprobe.d/8192cu.conf
```

\*\*Driver conflicts:\*\*

Check for conflicting drivers:

```wp-block-code
lsmod | grep 8192
modinfo 8192cu | head -20
```

\*\*USB disconnects:\*\*

Some USB 3.0 ports cause issues with this adapter. Try a USB 2.0 port, or disable USB autosuspend system-wide:

```wp-block-code
echo 'options usbcore autosuspend=-1' | sudo tee /etc/modprobe.d/disable-usb-autosuspend.conf
```

\## Consider Upgrading the Hardware

If stability remains an issue even with power management disabled, the RTL8192cu is aging by 2026 standards. Modern USB WiFi adapters using MediaTek (MT7921AU) or newer Realtek chipsets (RTL8852) have better driver support and kernel integration. Most modern distributions include these drivers out-of-the-box without additional configuration.

Recommended modern alternatives:\
\- \*\*Alfa AWUS036ACHM\*\* — MT7610U chipset, excellent Linux support\
\- \*\*Panda PAU09\*\* — RT5572 chipset, dual-band, well-supported\
\- \*\*Any MT7921-based adapter\*\* — Mainline kernel driver, no compilation needed

If you must continue using this adapter, disabling power management is the most practical solution for production use.

\## Checking Adapter Status

Use these commands to quickly diagnose the adapter's state:

```wp-block-code
# Check if adapter is detected
lsusb | grep -i realtek

# Check driver module status
lsmod | grep 8192cu

# Check wireless interface
ip link show wlan0
iwconfig wlan0

# Check signal strength
iwconfig wlan0 | grep "Signal level"

# Check connection speed
iwconfig wlan0 | grep "Bit Rate"

# Scan available networks
iwlist wlan0 scan | grep ESSID
```

\## DKMS Auto-Rebuild Setup

If you compiled the driver from source, set up DKMS to automatically rebuild it when the kernel updates:

```wp-block-code
sudo mkdir -p /usr/src/rtl8192cu-1.0
sudo cp -r rtl8192cu-fixes/* /usr/src/rtl8192cu-1.0/

# Create dkms.conf
cat << 'EOF' | sudo tee /usr/src/rtl8192cu-1.0/dkms.conf
PACKAGE_NAME="rtl8192cu"
PACKAGE_VERSION="1.0"
MAKE[0]="make"
BUILT_MODULE_NAME[0]="8192cu"
DEST_MODULE_LOCATION[0]="/kernel/drivers/net/wireless/"
AUTOINSTALL="yes"
EOF

sudo dkms add rtl8192cu/1.0
sudo dkms build rtl8192cu/1.0
sudo dkms install rtl8192cu/1.0
```

This ensures the driver survives kernel updates without manual intervention.
