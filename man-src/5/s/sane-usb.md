---
title: "sane-usb(5)"
name: "sane-usb"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-usb/"
description: "sane-usb – USB configuration tips for SANE"
---

<p>sane-usb &#8211; USB configuration tips for SANE</p>
<h2>Description</h2>
<p>This manual page contains information on how to access scanners with a USB interface. It focuses on two main topics: getting the scanner detected by the operating system kernel and using it with SANE. This page applies to USB most backends and scanners, as they use the generic sanei_usb interface. However, there is one exception: USB Scanners supported by the <code><a href="/docs/linux/man/5-sane-microtek2/">sane-microtek2</a></code>(5) backend need a special USB kernel driver. </p>
<h2>Quick Start</h2>
<p>This is a short HOWTO-like section. For the full details, read the following sections. The goal of this section is to get the scanner detected by <code><a href="/docs/linux/man/1-sane-find-scanner/">sane-find-scanner</a></code>(1). </p>
<p> Run <code><a href="/docs/linux/man/1-sane-find-scanner/">sane-find-scanner</a></code>(1). If it lists your scanner with the correct vendor and product ids, you are done. See section <code>SANE ISSUES</code> for details on how to go on. </p>
<p> <code><a href="/docs/linux/man/1-sane-find-scanner/">sane-find-scanner</a></code>(1) doesn&#8217;t list your scanner? Does it work as root? If yes, there is a permission issue. See the <code>LIBUSB</code> section for details. </p>
<p> Nothing is found even as root? Check that your kernel supports USB and that libusb is installed (see section <code>LIBUSB</code>).</p>
<h2>Usb Access Methods</h2>
<p>For accessing USB devices, the USB library libusb is used. There used to exist another method to access USB devices: the kernel scanner driver. The kernel scanner driver method is deprecated and shouldn&#8217;t be used anymore. It may be removed from SANE at any time. In Linux, the kernel scanner driver has been removed in the 2.6.* kernel series. Only libusb access is documented in this manual page.</p>
<h2>Libusb</h2>
<p>SANE can only use libusb 0.1.6 or newer. It needs to be installed at build-time. Modern Linux distributions and other operating systems come with libusb. </p>
<p> Libusb can only access your scanner if it&#8217;s not claimed by the kernel scanner driver. If you want to use libusb, unload the kernel driver (e.g. rmmod scanner under Linux) or disable the driver when compiling a new kernel. For Linux, your kernel needs support for the USB filesystem (usbfs). For kernels older than 2.4.19, replace &quot;usbfs&quot; with &quot;usbdevfs&quot; because the name has changed. This filesystem must be mounted. That&#8217;s done automatically at boot time, if /etc/fstab contains a line like this: </p>
<dl>
<dd>none /proc/bus/usb usbfs defaults 0 0</dl>
<p> The permissions for the device files used by libusb must be adjusted for user access. Otherwise only root can use SANE devices. For <i>Linux</i>, the devices are located in <i>/proc/bus/usb/</i> or in <i>/dev/bus/usb</i>, if you use udev. There are directories named e.g. &quot;001&quot; (the bus name) containing files &quot;001&quot;, &quot;002&quot; etc. (the device files). The right device files can be found out by running: <i>scanimage -L:</i> as root. Setting permissions with <code><a href="/docs/linux/man/1-chmod/">chmod</a></code>(1) is not permanent, however. They will be reset after reboot or replugging the scanner. </p>
<p> Usually <code><a href="/docs/linux/man/7-udev/">udev</a></code>(7) or for older distributions the hotplug utilities are used, which support dynamic setting of access permissions. SANE comes with udev and hotplug scripts in the directory <i>tools/udev</i> and <i>tools/hotplug</i>. They can be used for setting permissions, see <i>/usr/share/doc/libsane/README.linux</i>, <i>tools/README</i> and the <i>README</i> in the <i>tools/hotplug</i> directory for more details. </p>
<p> For the <code>BSDs</code>, the device files used by libusb are named <i>/dev/ugen*</i>. Use chmod to apply appropriate permissions.</p>
<h2>Sane Issues</h2>
<p>This section assumes that your scanner is detected by <code><a href="/docs/linux/man/1-sane-find-scanner/">sane-find-scanner</a></code>(1). It doesn&#8217;t make sense to go on, if this is not the case. While <code><a href="/docs/linux/man/1-sane-find-scanner/">sane-find-scanner</a></code>(1) is able to detect any USB scanner, actual scanning will only work if the scanner is supported by a SANE backend. Information on the level of support can be found on the SANE webpage (<i><a rel="nofollow" href="http://www.sane-project.org/">http://www.sane-project.org/</a></i>), and the individual backend manpages. </p>
<p> Most backends can detect USB scanners automatically using &quot;usb&quot; configuration file lines. This method allows one to identify scanners by the USB vendor and product numbers. The syntax for specifying a scanner this way is: </p>
<dl>
<dd>usb <i>VENDOR PRODUCT</i></dl>
<p> where <i>VENDOR</i> is the USB vendor id, and <i>PRODUCT</i> is the USB product id of the scanner. Both ids are non-negative integer numbers in decimal or hexadecimal format. The correct values for these fields can be found by running <code><a href="/docs/linux/man/1-sane-find-scanner/">sane-find-scanner</a></code>(1), looking into the syslog (e.g., <i>/var/log/messages</i>) or under Linux by issuing the command <i>cat /proc/bus/usb/devices</i>. This is an example of a config file line: </p>
<dl>
<dd>usb 0x055f 0x0006</dl>
<p> would have the effect that all USB devices in the system with a vendor id of 0x55f and a product id of 0x0006 would be probed and recognized by the backend. </p>
<p> If your scanner is not detected automatically, it may be necessary to edit the appropriate backend configuration file before using SANE for the first time. For a detailed description of each backend&#8217;s configuration file, please refer to the relevant backend manual page (e.g. <code><a href="/docs/linux/man/5-sane-mustek_usb/">sane-mustek_usb</a></code>(5) for Mustek USB scanners). </p>
<p> Do <code>not</code> create a symlink from <i>/dev/scanner</i> to the USB device because this link is used by the SCSI backends. The scanner may be confused if it receives SCSI commands.</p>
<h2>Environment</h2>
<dl>
<dt><code>SANE_DEBUG_SANEI_USB</code></p>
<dd>If the library was compiled with debug support enabled, this environment variable controls the debug level for the USB I/O subsystem. E.g., a value of 128 requests all debug output to be printed. Smaller levels reduce verbosity. Values greater than 4 enable libusb debugging (if available). Example: <i>export SANE_DEBUG_SANEI_USB=4</i>.</dl>
<dl>
<dt><code>SANE_USB_WORKAROUND</code></p>
<dd>If your scanner does not work when plugged into a USB3 port, try setting the environment variable <code>SANE_USB_WORKAROUND</code> to 1. This may work around issues which happen with particular kernel versions. Example: <i>export SANE_USB_WORKAROUND=1.</i> </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7), <code><a href="/docs/linux/man/1-sane-find-scanner/">sane-find-scanner</a></code>(1), <code><a href="/docs/linux/man/5-sane-backendname/">sane-backendname</a></code>(5), <code><a href="/docs/linux/man/5-sane-scsi/">sane-scsi</a></code>(5) </p>
<h2>Author</h2>
<p>Henning Meier-Geinitz &lt;<i>henning [at] meier-geinitz.de</i>&gt;</p>
