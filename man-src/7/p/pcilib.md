---
title: "pcilib(7)"
name: "pcilib"
section: "7"
letter: "p"
url: "/docs/linux/man/7-pcilib/"
description: "pcilib – a library for accessing PCI devices"
---

<p>pcilib &#8211; a library for accessing PCI devices</p>
<h2>Description</h2>
<p>The PCI library (also known as <i>pcilib</i> and <i>libpci</i>) is a portable library for accessing PCI devices and their configuration space. </p>
<h2>Access Methods</h2>
<p>The library supports a variety of methods to access the configuration space on different operating systems. By default, the first matching method in this list is used, but you can specify override the decision (see the <code>-A</code> switch of <i>lspci</i>). </p>
<dl>
<dt><code>linux-sysfs</code></p>
<dd>The <code>/sys</code> filesystem on Linux 2.6 and newer. The standard header of the config space is available to all users, the rest only to root. Supports extended configuration space, PCI domains, VPD (from Linux 2.6.26), physical slots (also since Linux 2.6.26) and information on attached kernel drivers.</p>
<dt><code>linux-proc</code></p>
<dd>The <code>/proc/bus/pci</code> interface supported by Linux 2.1 and newer. The standard header of the config space is available to all users, the rest only to root.</p>
<dt><code>intel-conf1</code></p>
<dd>Direct hardware access via Intel configuration mechanism 1. Available on i386 and compatibles on Linux, Solaris/x86, GNU Hurd, Windows, BeOS and Haiku. Requires root privileges.</p>
<dt><code>intel-conf2</code></p>
<dd>Direct hardware access via Intel configuration mechanism 2. Available on i386 and compatibles on Linux, Solaris/x86, GNU Hurd, Windows, BeOS and Haiku. Requires root privileges. Warning: This method is able to address only the first 16 devices on any bus and it seems to be very unreliable in many cases.</p>
<dt><code>fbsd-device</code></p>
<dd>The <code>/dev/pci</code> device on FreeBSD. Requires root privileges.</p>
<dt><code>aix-device</code></p>
<dd>Access method used on AIX. Requires root privileges.</p>
<dt><code>nbsd-libpci</code></p>
<dd>The <code>/dev/pci0</code> device on NetBSD accessed using the local libpci library.</p>
<dt><code>obsd-device</code></p>
<dd>The <code>/dev/pci</code> device on OpenBSD. Requires root privileges.</p>
<dt><code>dump</code></p>
<dd>Read the contents of configuration registers from a file specified in the <code>dump.name</code> parameter. The format corresponds to the output of <i>lspci</i> <code>-x</code>.</p>
<dt><code>darwin</code></p>
<dd>Access method used on Mac OS X / Darwin. Must be run as root and the system must have been booted with debug=0x144. </p>
</dl>
<h2>Parameters</h2>
<p>The library is controlled by several parameters. They should have sensible default values, but in case you want to do something unusual (or even something weird), you can override them (see the <code>-O</code> switch of <i>lspci</i>).</p>
<h3>Parameters of specific access methods</h3>
<dl>
<dt><code>dump.name</code></p>
<dd>Name of the bus dump file to read from.</p>
<dt><code>fbsd.path</code></p>
<dd>Path to the FreeBSD PCI device.</p>
<dt><code>nbsd.path</code></p>
<dd>Path to the NetBSD PCI device.</p>
<dt><code>obsd.path</code></p>
<dd>Path to the OpenBSD PCI device.</p>
<dt><code>proc.path</code></p>
<dd>Path to the procfs bus tree.</p>
<dt><code>sysfs.path</code></p>
<dd>Path to the sysfs device tree. </p>
</dl>
<h3>Parameters for resolving of ID&#8217;s via DNS</h3>
<dl>
<dt><code>net.domain</code></p>
<dd>DNS domain containing the ID database.</p>
<dt><code>net.cache_name</code></p>
<dd>Name of the file used for caching of resolved ID&#8217;s. </p>
</dl>
<h3>Parameters for resolving of ID&#8217;s via UDEV&#8217;s HWDB</h3>
<dl>
<dt><code>hwdb.disable</code></p>
<dd>Disable use of HWDB if set to a non-zero value. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-lspci/">lspci</a></code>(8), <code><a href="/docs/linux/man/8-setpci/">setpci</a></code>(8), <code><a href="/docs/linux/man/5-pci-ids/">pci.ids</a></code>(5), <code><a href="/docs/linux/man/8-update-pciids/">update-pciids</a></code>(8) </p>
<h2>Author</h2>
<p>The PCI Utilities are maintained by Martin Mares &lt;mj [at] ucw.cz&gt;.</p>
