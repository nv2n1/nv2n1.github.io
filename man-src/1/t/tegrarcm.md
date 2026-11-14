---
title: "tegrarcm(1)"
name: "tegrarcm"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tegrarcm/"
description: "tegrarcm – tegra firmware download utility"
---

<h2 class="name">NAME</h2>
<p> tegrarcm &#8211; tegra firmware download utility </p>
<h2>SYNOPSIS</h2>
<p> <code>tegrarcm</code> [ <i>options</i> ]</p>
<h2>DESCRIPTION</h2>
<p> This program is used to send code to a Tegra device in recovery mode. It does not supported locked devices with an encrypted boot key, only open devices such as the ventana or cardhu reference boards. It is not capable of flashing firmware to a device, but can be used to download firmware that is then capable of flashing. For example in ChromeOS tegrarcm is used to download a special build of u-boot to the target Tegra device with a payload that it then flashes to the boot device. </p>
<h3>Platforms supported</h3>
<dl>
<dt>&bull;</p>
<dd> <code>Tegra20</code></p>
<dt>&bull;</p>
<dd> <code>Tegra30</code></p>
<dt>&bull;</p>
<dd> <code>Tegra114</code></p>
<dt>&bull;</p>
<dd> <code>Tegra124</code> </p>
</dl>
<h3>How to use</h3>
<dl>
<dt>&#8212;</p>
<dd> Connect a USB cable from your development system to your Tegra device. You will either need a USB A to A cable or A to micro B depending on the target board.</p>
<dt>&#8212;</p>
<dd> Find the appropriate BCT file for your board. For reference boards, BCT files can be found in the L4T distribution from NVIDIA.</p>
<dt>&#8212;</p>
<dd> Build some firmware for your device (such as u-boot)</p>
<dt>&#8212;</p>
<dd> Run tegrarcm to download the firmware </p>
</dl>
<h2>COMMANDS</h2>
<dl>
<dt><code>readbct</code></p>
<dd> Read the BCT from the target device and write it to <i>bctfile</i>. </p>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;bct </code><i>bctfile</i></p>
<dd> Specify the BCT file to download to the Tegra device. This file contains memory configuation information for the board. BCT files can be obtained through the NVIDIA L4T distribution or generated with cbootimage and a proper configuration file.</p>
<dt><code>&#8211;bootloader </code><i>blfile</i></p>
<dd> Specify the bootloader file to download to the Tegra device. This is the firmware file that will be downloaded and executed.</p>
<dt><code>&#8211;loadaddr </code><i>loadaddr</i></p>
<dd> Specify the address the bootloader will be loaded at. This should be specified in hex and is typically 0x108000 for a Tegra20 device or 0x80108000 for a Tegra30, Tegra114, or Tegra124 device.</p>
<dt><code>&#8211;entryaddr </code><i>entryaddr</i></p>
<dd> Specify the entry address that control will be passed to after the firmware is loaded. This should be specified in hex. If this option is omitted it is assumed to be the same as the load address.</p>
<dt><code>&#8211;version</code></p>
<dd> Print the version number and exit.</p>
<dt><code>&#8211;help</code></p>
<dd> Print help text and exit.</p>
<dt><code>&#8211;miniloader </code><i>mlfile</i></p>
<dd> Read the miniloader from the specified file instead of using the built-in one.</p>
<dt><code>&#8211;miniloader_entry </code><i>mlentry</i></p>
<dd> Specify the entry address of the miniloader.</p>
<dt><code>&#8211;usb-port-path </code><i>path</i></p>
<dd> Specify the physical USB port path of the Tegra device to control. </p>
</dl>
<h2>USB PORT PATH</h2>
<p> By default, tegrarcm operates on the first USB applicable device it finds. In a system that contains multiple Tegra devices, the user may wish to specify which device tegrarcm should operate upon. The &#8211;usb-port-path option allows this, and in a manner that is most immune to the set of attached USB devices varying. </p>
<p> Note that the USB port path is associated with a physical USB port on a particular hub. This value will vary if you physically re-organize your USB connections. This feature is still useful even if your USB topology changes, providing you have some other mechanism to differentiate attached devices. For example, you could use a wrapper script around tegrarcm that identifies the appropriate device by other means, then automatically calculates the USB port path using the procedures below, and passes the value to tegrarcm. </p>
<p> To determine the USB port path of a device, you must plug it in and find the current USB bus and USB device number of the device, then map that to the USB port path. Simply run lsusb to find the current USB bus and device number. If you have multiple NVIDIA devices attached, you may need to unplug and replug the Tegra device to ensure you know which is which (all while not changing the state of any other USB devices so you don&#8217;t confuse yourself). </p>
<pre>
$ lsusb
Bus 003 Device 039: ID 0955:7721 NVidia Corp.
Bus 003 Device 045: ID 0955:7140 NVidia Corp.
fi
Then, to determine the USB port path, do one of:
<dl>
<dt>1.<dd>
Execute udevmadm on the USB device, and look for the DEVPATH entry. The
final component in the path is the USB port path:
$ udevadm info /dev/bus/usb/003/045
P: /devices/pci0000:00/0000:00:14.0/usb3/3-10/3-10.4
N: bus/usb/003/045
E: BUSNUM=003
E: DEVNUM=045
E: DEVPATH=/devices/pci0000:00/0000:00:14.0/usb3/3-10/3-10.4
</pre>
<dt>2.</p>
<dd>
<p> Look at all the sub-directories of /sys/bus/usb/devices/* that do not contain either &quot;:&quot; or &quot;usb&quot;. Each of these will contain a busnum and devnum file. Find the directory which matches the lsusb output, and use its name: </p>
<pre>
$ cat /sys/bus/usb/devices/3-10.4/busnum
3
$ cat /sys/bus/usb/devices/3-10.4/devnum
45
</pre>
<p> Alternatively, you may already have udev rules that create a device node symlink for the device (after some specific identification algorithm). In that case, you can search the udev output for MAJOR/MINOR values, or /sys/bus/usb/devices/* directories for &quot;dev&quot; files, that match the device node the symlink points to. </p>
<p> Once the port path is known, this value will not vary unless your USB connections are physically changed, so you can use it over and over without repeating the steps above. </p>
</dl>
<h2>EXAMPLES</h2>
<p> To download u-boot firmware to a Tegra20 seaboard: </p>
<pre>
$ sudo tegrarcm --bct seaboard.bct --bootloader u-boot.bin --loadaddr 0x108000
bct file: seaboard.bct
booloader file: u-boot.bin
load addr 0x108000
entry addr 0x108000
device id: 0x7820
uid:  0x33c20c0413fb217
RCM version: 2.1
downloading miniloader to target...
miniloader downloaded successfully
Chip UID:                0x33c20c0413fb217
Chip ID:                 0x20
Chip ID Major Version:   0x1
Chip ID Minor Version:   0x4
Chip SKU:                0x18 (t25)
Boot ROM Version:        0x1
Boot Device:             0x3 (SPI)
Operating Mode:          0x3 (developer mode)
Device Config Strap:     0x0
Device Config Fuse:      0x0
SDRAM Config Strap:      0x0
sending file: seaboard.bct
- 4080/4080 bytes sent
seaboard.bct sent successfully
sending file: u-boot.bin
- 268314/268314 bytes sent
u-boot.bin sent successfully
</pre>
<p> To read the BCT from a system: </p>
<pre>
$ sudo tegrarcm --bct ventana.bct readbct
bct file: ventana.bct
device id: 0x7820
reading BCT from system, writing to ventana.bct...done!
</pre>
<h2>RETURN VALUE</h2>
<p> If any error occurs a non zero exit status is returned. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-cbootimage/">cbootimage</a></code>(1), </p>
<h2>AUTHOR</h2>
<p> Allen Martin, &lt;amartin [at] nvidia.com&gt; </p>
<h2>Index</h2>
