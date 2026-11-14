---
title: "fxload(8)"
name: "fxload"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fxload/"
description: "fxload – Firmware download to EZ-USB devices"
---

<p>fxload &#8211; Firmware download to EZ-USB devices</p>
<h2>Synopsis</h2>
<p><code>fxload</code> <code>[ -v ]</code> <code>[ -D </code><i>devpath</i><code> ]</code> <code>[ -I </code><i>hexfile</i><code> ]</code> <code>[ -2 ]</code> <code>[ -t </code><i>type</i><code> ]</code> <code>[ -c </code><i>config</i><code> ]</code> <code>[ -s </code><i>loader</i><code> ]</code><br />
 <code>fxload</code> <code>[ -D </code><i>devpath</i><code> ]</code> <code>[ -L </code><i>link</i><code> ]</code> <code>[ -m </code><i>mode</i><code> ]</code><br />
 <code>fxload</code> <code>[ -V ]</code> <code>[ -? ]</code></p>
<h2>Description</h2>
<p><code>fxload</code> is a program which downloads firmware to USB devices based on AnchorChips EZ-USB, Cypress EZ-USB FX, or Cypress EZ-USB FX2 microcontrollers. These have 8-bit 8051 cores with special extensions for USB I/O. The FX2 supports high speed USB 2.0 transfers (480 Mbit/sec) as well as full speed USB 1.1 transfers (12 Mbit/sec), while the earlier parts supports only full speed transfers. These controllers have several package options, and can be set up with external memory (on-chip memory is usually about 8K), EEPROMs, and ROMs when device costs allow. </p>
<p> This uses &quot;usbfs&quot; (older name: &quot;usbdevfs&quot;) to access devices, and issues vendor specific control requests to download and reset the EZ-USB devices. Normally, firmware will then &quot;renumerate&quot; by disconnecting from USB and then reconnecting as a new device. It then appears with new device descriptors and functionality, as provided by the firmware which has been downloaded. </p>
<p> To support some non-firmware applications, this can also set up symbolic links for those usbfs names. It can also change their access modes. Both of these can help simplify software applications that need to talk to USB devices using user mode drivers, don&#8217;t want to run with privileges or to examine all of the existing USB devices, and which don&#8217;t need more kernel drivers. </p>
<p> See the <i>Linux-Hotplug</i> web site for information about how to use <code>fxload</code> to download device firmware when hotplugging USB devices, using driver-specific scripts stored in the <i>/etc/hotplug/usb</i> directory.</p>
<h2>Function Letters</h2>
<p>At least one of the following options must be specified. Note that as usual with UNIX and Linux commands, the order of command option flags does not matter. You may use these in any order.</p>
<dl>
<dt><code>-I </code><i>hexfile</i></p>
<dd>Downloads the specified firmware file. This firmware is provided in standard Intel hexfile format. (Common naming conventions include <i>*.hex</i> and <i>*.ihx</i>.) Depending on the device and firmware in use, the <code>-s</code> option may also be necessary to specify a second stage loader. Firmware is normally downloaded to RAM and executed, but there is also an option for downloading into bootable I2C EEPROMs.</p>
<dt><code>-L </code><i>link</i></p>
<dd>Creates the specified symbolic link to the usbfs device path. This would typically be used to create a name in a directory that would be searched by an application. The symlink would be removed by some other component on device unplug.</p>
<dt><code>-m </code><i>mode</i></p>
<dd>Changes permissions on the &quot;usbfs&quot; device node. By default, those nodes are only accessible by privileged users, which doesn&#8217;t help when the user mode device driver needs to run without root privileges. Note that usbfs mount options like <i>devmode=0666</i> are also available.</p>
<dt><code>-V</code></p>
<dd>Identifies the version of fxload being invoked, and exits without performing other actions.</p>
<dt><code>-?</code></p>
<dd>Show usage.</dl>
<p> Note that when downloading firmware that renumerates, there&#8217;s no point in changing the device permissions or creating a symbolic link.</p>
<h2>Options</h2>
<p>By default, <code>fxload</code> assumes the device uses an EZ-USB or EZ-USB FX. It also assumes that the device in question has been specified by USB kernel hotplugging conventions, using the <i>DEVICE</i> environment variable to name a &quot;usbfs&quot; file that can be used to talk to the device.</p>
<dl>
<dt><code>-c </code><i>config</i></p>
<dd>Indicates the specified firmware should be downloaded to an I2C boot EEPROM rather than to RAM. The parameter is the EZ-USB FX or FX2 configuration byte, and for AnchorChips devices the value should be zero. This requires a second stage loader that knows how to write to I2C EEPROMs specified using the <code>-s</code> option, as well as a device that&#8217;s provided with an EEPROM large enough to store the boot firmware. After downloading to a device&#8217;s EEPROM, you should retest it starting from power off.</p>
<dt><code>-s </code><i>loader</i></p>
<dd>This identifies the hex file holding a second stage loader (in the same hex file format as the firmware itself), which is loaded into internal memory. This loader understands additional vendor control requests, beyond the one built into all EZ-USB hardware, which are needed to write external RAM or EEPROM. As a last step when loading firmware, <code>fxload</code> normally overwrites this second stage loader with parts of the firmware residing on-chip.</p>
<dt><code>-2</code></p>
<dd>Same as &quot;-t fx2&quot;.</p>
<dt><code>-t </code><i>type</i></p>
<dd>Indicates which type of microcontroller is used in the device; type may be one of <i>an21</i> (the original AnchorChips devices), <i>fx</i> (Cypress&#8217; updated version, the EZ-USB FX), or <i>fx2</i> (the Cypress EZ-USB FX2, supporting high speed transfers). Except when writing to EEPROM, all that normally matters when downloading firmware is whether or not the device uses an FX2.</p>
<dt><code>-v</code></p>
<dd>Prints some diagnostics, such as download addresses and sizes, to standard error. Repeat the flag (<code>-vv</code>, <code>-vvv</code>) to get more diagnostics.</p>
<dt><code>-D </code><i>devpath</i></p>
<dd>Specifies the &quot;usbfs&quot; path name for the device in question, such as <i>/proc/bus/usb/004/080</i>. This takes precedence over any <i>DEVICE</i> environment variable that may be set.</dl>
<h2>Notes</h2>
<p>This program implements one extension to the standard &quot;hex file&quot; format. Lines beginning with a &quot;#&quot; character are ignored, and may be used to hold copyright statements and other information. Other tools may not handle hexfiles using this extension. </p>
<p> At this writing, &quot;usbfs&quot; is a kernel configuration option. That means that device drivers relying on user mode firmware downloading may need to depend on that kernel configuration option. A less preferable alternative involves compiling the firmware into the kernel and managing downloads and renumeration there. This is less preferable in part because much device firmware is provided with GPL-incompatible licensing, and in part because storing such firmware firmware wastes kernel memory. </p>
<p> For EZ-USB family devices, the hardware&#8217;s first stage loader (supporting the 0xA0 vendor request) can&#8217;t write into external memory. Configurations that put firmware into external memory thus need a second stage loader. For typical &quot;flat&quot; memory architectures, a loader supporting the 0xA3 vendor request is used to write into that memory. Similarly, a second stage loader that supports the 0xA2 vendor request is needed when writing boot firmware into an I2C EEPROM. These 0xA2 and 0xA3 vendor commands are conventions defined by Cypress. Devices that use bank switching or similar mechanisms to stretch the 64KByte address space may need different approach to loading firmware. </p>
<p> Not all devices support EEPROM updates. Some EZ-USB based devices don&#8217;t have an I2C EEPROM; many such EEPROMs are too small to store firmware; and some firmware can&#8217;t be placed in bootable I2C EEPROMs.</p>
<h2>Environment Variables</h2>
<dl>
<dt><code>DEVICE</code></p>
<dd>normally names a &quot;usbfs&quot; file that will be used to talk to the device. This is provided by the Linux kernel as part of USB hotplugging.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-hotplug/">hotplug</a></code>(8)</p>
<h2>Authors</h2>
<p>Linux Hotplugging Project <i><a rel="nofollow" href="http://linux-hotplug.sourceforge.net/">http://linux-hotplug.sourceforge.net/</a></i></p>
