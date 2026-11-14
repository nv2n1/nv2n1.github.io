---
title: "bcharge(1)"
name: "bcharge"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bcharge/"
description: "bcharge – program to set BlackBerry handhelds to 500mA"
---

<h2 class="name">NAME</h2>
<p> bcharge &#8211; program to set BlackBerry handhelds to 500mA </p>
<h2>SYNOPSIS</h2>
<p> <code>bcharge</code></p>
<h2>DESCRIPTION</h2>
<p> <code>bcharge</code> is a program that sends a special handshake to all BlackBerry devices it finds on the USB bus. This handshake causes the device to reset itself, and then request 500mA instead of the usual 100mA. This allows proper charging on Linux. </p>
<p> It is safe to run this command multiple times, as it only changes devices that are not already set to 500mA. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-o</code></p>
<dd> For Blackberry Pearl devices, using this switch causes bcharge to set the Product ID to 0001. Otherwise, the default is to use Product ID 0004. When the Pearl is in 0004 mode, two USB interfaces are presented: one for database access and one for mass storage. In 0001 mode, only the database access is available. </p>
<p> Before bcharge is run, the Pearl shows up with a Product ID of 0006, which only gives mass storage functionality. You must run bcharge for the Pearl before using btool.</p>
<dt><code>-d</code></p>
<dd> Again, this switch is for the Blackberry Pearl to switch it back to 0004 dual mode after having run bcharge with the -o option. Since a Pearl in mode 0001 is practically indistinguishable from a classic Blackberry, the -d switch is needed to tell bcharge that you really are working with a Pearl.</p>
<dt><code>-h</code></p>
<dd> Help summary.</p>
<dt><code>-p devpath</code></p>
<dd> If your system runs a kernel with CONFIG_USB_SUSPEND enabled (some Ubuntu kernels have this turned on, as well as some Fedora 7 kernels), then you also need to adjust the suspend state to avoid going into power saving mode. This option is used when run from udev, using a rule such as: </p>
<p> BUS==&quot;usb&quot;, SUBSYSTEM==&quot;usb_device&quot;, ACTION==&quot;add&quot;, SYSFS{idVendor}==&quot;0fca&quot;, SYSFS{idProduct}==&quot;0001&quot;, SYMLINK+=&quot;bb-%k&quot;, GROUP=&quot;plugdev&quot;, MODE=&quot;0660&quot;, RUN=&quot;/usr/sbin/bcharge -p %p&quot; </p>
<p> When using this option, you will almost always need to be root.</p>
<dt><code>-s path</code></p>
<dd> Specify the mount point for the sysfs filesystem. On most systems this is mounted at /sys which is the default. </p>
</dl>
<h2>AUTHOR</h2>
<p> bcharge and this manual page were written by Chris Frey &lt;cdfrey [at] foursquare.net&gt; for the Barry project. </p>
<p> <a rel="nofollow" href="http://www.netdirect.ca/software/packages/barry">http://www.netdirect.ca/software/packages/barry</a> </p>
<h2>Index</h2>
