---
title: "usb_modeswitch(1)"
name: "usb_modeswitch"
section: "1"
letter: "u"
url: "/docs/linux/man/1-usb_modeswitch/"
description: "usb_modeswitch – control the mode of ‘multi-state’ USB devices"
---

<h2 class="name">NAME</h2>
<p> usb_modeswitch &#8211; control the mode of &#8216;multi-state&#8217; USB devices </p>
<h2>SYNOPSIS</h2>
<p> <code>usb_modeswitch</code> [<code>-heWQDIvpVPmM23rwKdHSOBGTNALnsRiuagft</code>] [<code>-c </code><i>filename</i>]</p>
<h2>DESCRIPTION</h2>
<p> Several new USB devices have their proprietary Windows drivers onboard, most of them WWAN and WLAN dongles. When plugged in for the first time, they act like a flash storage and start installing the Windows driver from there. If the driver is installed, it makes the storage device disappear and a new device, mainly composite (e.g. with modem ports), shows up. </p>
<p> On Linux, in most cases the drivers are available as kernel modules, such as &quot;usbserial&quot; or &quot;option&quot;. However, the device initially binds to &quot;usb-storage&quot; by default. <code>usb_modeswitch</code> can then send a provided bulk message (most likely a mass storage command) to the device; this message has to be determined by analyzing the actions of the Windows driver. </p>
<p> In some cases, USB control commands are used for switching. These cases are handled by custom functions, and no bulk message needs to be provided. </p>
<p> Usually, the program is distributed with a set of configurations for many known devices, which allows a fully automatic handling of a device upon insertion, made possible by combining usb_modeswitch with the wrapper script <code>usb_modeswitch_dispatcher</code> which is launched by the udev daemon. This requires a Linux-flavoured system though. </p>
<p> Note that <code>usb_modeswitch</code> itself has no specific Linux dependencies. </p>
<h2>OPTIONS</h2>
<p> This program follows the usual GNU command line syntax, with long options starting with two dashes (&#8216;&#8211;&#8216;). A summary of options is included below.</p>
<dl>
<dt><code>-h</code> <code>&#8211;help</code></dt>
<dd> Show summary of options.</dd>
<dt><code>-e</code> <code>&#8211;version</code></dt>
<dd> Print version information and exit</dd>
<dt><code>-v</code> <code>&#8211;default-vendor NUM</code></dt>
<dd> Vendor ID to look for (mandatory), usually given as hex number (example: 0x12d1). Each USB device is identified by a number officially assigned to the vendor by the USB association and a number for the respective model (product ID) chosen by the vendor</dd>
<dt><code>-p</code> <code>&#8211;default-product NUM</code></dt>
<dd> Product ID to look for (mandatory)</dd>
<dt><code>-V</code> <code>&#8211;target-vendor NUM</code></dt>
<dd> Target vendor ID. When given will be searched for and detected initially for information purposes. If success checking (option -s) is active, providing target IDs (vendor/product) or target class is recommended</dd>
<dt><code>-j</code> <code>&#8211;find-mbim</code></dt>
<dd> Return configuration number with MBIM interface and exit.</dd>
<dt><code>-P</code> <code>&#8211;target-product NUM</code></dt>
<dd> Target product ID</dd>
<dt><code>-b</code> <code>&#8211;bus-num NUM</code></dt>
<dd>
</dd><dt><code>-g</code> <code>&#8211;device-num NUM</code></dt>
<dd> If bus and device number are provided, the handling of a specific device on a specific USB port is guaranteed, in contrast to using only the USB ID. This is important if there are multiple similar devices on a system</dd>
<dt><code>-C</code> <code>&#8211;target-class NUM</code></dt>
<dd> Target Device Class according to the USB specification. Some devices keep their original vendor/product ID after successful switching. To prevent them from being treated again, the device class can be checked. For unswitched devices it is always 8 (storage class), for switched modems it is often 0xff (vendor specific). In composite modes, the class of the first interface is watched</dd>
<dt><code>-m</code> <code>&#8211;message-endpoint NUM</code></dt>
<dd> A specific endpoint to use for data transfers. Only for testing purposes; usually endpoints are determined from the device attributes</dd>
<dt><code>-M</code> <code>&#8211;message-content STRING</code></dt>
<dd> A bulk message to send as a switching command. Provided as a hexadecimal string</dd>
<dt><code>-2</code> <code>&#8211;message-content2 STRING</code></dt>
<dd>
</dd><dt><code>-3</code> <code>&#8211;message-content3 STRING</code></dt>
<dd> Additional bulk messages to send as switching commands. Provided as hexadecimal strings. When used with mass storage commands, setting <code>&#8211;need-response</code> is strongly advised to comply with specifications and to avoid likely errors</dd>
<dt><code>-w</code> <code>&#8211;release-delay &lt;milliseconds&gt;</code></dt>
<dd> After issuing all bulk messages, wait for the given time before releasing the interface. Required for some modems on older systems (especially after an EJECT message)</dd>
<dt><code>-n</code> <code>&#8211;need-response</code></dt>
<dd> Obsolete. CSW is always attempted to being read after mass storage transfers. No downside</dd>
<dt><code>-r</code> <code>&#8211;response-endpoint NUM</code></dt>
<dd> Try to read the response to a storage command from there. Only for testing purposes; usually endpoints are determined from the device attributes</dd>
<dt><code>-K</code> <code>&#8211;std-eject</code></dt>
<dd> Apply the standard SCSI sequence of &quot;Allow Medium Removal&quot; and &quot;Eject&quot;. Implies <code>-n</code>. One &#8216;Message&#8217; can be added with <code>-M</code> that will be transmitted after the eject sequence. Used by many modems</dd>
<dt><code>-d</code> <code>&#8211;detach-only</code></dt>
<dd> Just detach the current driver. This is sufficient for some early devices to switch successfully. Otherwise this feature can be used as a &#8216;scalpel&#8217; for special cases, like separating the driver from individual interfaces</dd>
<dt><code>-H</code> <code>&#8211;huawei-mode</code></dt>
<dd> Send a special control message used by older Huawei devices</dd>
<dt><code>-J</code> <code>&#8211;huawei-new-mode</code></dt>
<dd> Send a specific bulk message used by all newer Huawei devices</dd>
<dt><code>-X</code> <code>&#8211;huawei-alt-mode</code></dt>
<dd> Send an alternative bulk message to Huawei devices</dd>
<dt><code>-S</code> <code>&#8211;sierra-mode</code></dt>
<dd> Send a special control message used by Sierra devices</dd>
<dt><code>-G</code> <code>&#8211;gct-mode</code></dt>
<dd> Send a special control message used by GCT chipsets</dd>
<dt><code>-T</code> <code>&#8211;kobil-mode</code></dt>
<dd> Send a special control message used by Kobil devices</dd>
<dt><code>-N</code> <code>&#8211;sequans-mode</code></dt>
<dd> Send a special control message used by Sequans chipset</dd>
<dt><code>-A</code> <code>&#8211;mobileaction-mode</code></dt>
<dd> Send a special control message used by the MobileAction device</dd>
<dt><code>-B</code> <code>&#8211;qisda-mode</code></dt>
<dd> Send a special control message used by Qisda devices</dd>
<dt><code>-E</code> <code>&#8211;quanta-mode</code></dt>
<dd> Send a special control message used by Quanta devices</dd>
<dt><code>-F</code> <code>&#8211;pantech-mode NUM</code></dt>
<dd> Send a special control message used by Pantech devices. Value NUM will be used in control message as &#8216;wValue&#8217;</dd>
<dt><code>-Z</code> <code>&#8211;blackberry-mode</code></dt>
<dd> Send a special control message used by some newer Blackberry devices</dd>
<dt><code>-S</code> <code>&#8211;option-mode</code></dt>
<dd> Send a special control message used by all Option devices</dd>
<dt><code>-O</code> <code>&#8211;sony-mode</code></dt>
<dd> Apply a special sequence used by Sony Ericsson devices. Implies option &#8211;check-success</dd>
<dt><code>-L</code> <code>&#8211;cisco-mode</code></dt>
<dd> Send a sequence of bulk messages used by Cisco devices</dd>
<dt><code>-R</code> <code>&#8211;reset-usb</code></dt>
<dd> Send a USB reset command to the device. Can be combined with any switching method or stand alone. It is always done as the last step of all device interactions. Few devices need it to complete the switching; apart from that it may be useful during testing</dd>
<dt><code>-c</code> <code>&#8211;config-file FILENAME</code></dt>
<dd> Use a specific config file. If any ID or switching options are given as command line parameters, this option is ignored. In that case all mandatory parameters have to be provided on the command line</dd>
<dt><code>-f</code> <code>&#8211;long-config STRING</code></dt>
<dd> Provide device details in config file syntax as a multiline string on the command line</dd>
<dt><code>-t</code> <code>&#8211;stdinput</code></dt>
<dd> Read the device details in config file syntax from standard input, e.g. redirected from a command pipe (multiline text)</dd>
<dt><code>-Q</code> <code>&#8211;quiet</code></dt>
<dd> Don&#8217;t show progress or error messages</dd>
<dt><code>-W</code> <code>&#8211;verbose</code></dt>
<dd> Print all settings before running and show libusb debug messages</dd>
<dt><code>-D</code> <code>&#8211;sysmode</code></dt>
<dd> Changes the behaviour of the program slightly. A success message including the effective target device ID is put out and a syslog notice is issued. Mainly for integration with a wrapper script</dd>
<dt><code>-s</code> <code>&#8211;check-success &lt;seconds&gt;</code></dt>
<dd> After switching, keep checking for the result up to the given time. If target IDs or target class were provided, their appearance indicates certain success. Otherwise the disconnection of the original device is rated as likely proof</dd>
<dt><code>-I</code> <code>&#8211;inquire</code></dt>
<dd> Obsolete. Formerly obtained SCSI attributes, now ignored</dd>
<dt><code>-i</code> <code>&#8211;interface NUM</code></dt>
<dd> Select initial USB interface (default: 0). Only for testing purposes</dd>
<dt><code>-u</code> <code>&#8211;configuration NUM</code></dt>
<dd> Select USB configuration (applied after any other possible switching actions)</dd>
<dt><code>-a</code> <code>&#8211;altsetting NUM</code></dt>
<dd> Select alternative USB interface setting (applied after switching). Mainly for testing</dd></dl>
<h2>AUTHOR</h2>
<p> This manual page was originally written by Didier Raboud (didier [at] raboud.com) for the <code>Debian</code> system. Additions made by Josua Dietze. Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 or any later version published by the Free Software Foundation. </p>
<p> The complete text of the current GNU General Public License can be found in <a rel="nofollow" href="http://www.gnu.org/licenses/gpl.txt">http://www.gnu.org/licenses/gpl.txt</a> </p>
<h2>Index</h2>
