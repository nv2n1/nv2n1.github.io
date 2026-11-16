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
<dt><code>linux-sysfs</code></dt>
<dd>The <code>/sys</code> filesystem on Linux 2.6 and newer. The standard header of the config space is available to all users, the rest only to root. Supports extended configuration space, PCI domains, VPD (from Linux 2.6.26), physical slots (also since Linux 2.6.26) and information on attached kernel drivers.</dd>
<dt><code>linux-proc</code></dt>
<dd>The <code>/proc/bus/pci</code> interface supported by Linux 2.1 and newer. The standard header of the config space is available to all users, the rest only to root.</dd>
<dt><code>intel-conf1</code></dt>
<dd>Direct hardware access via Intel configuration mechanism 1. Available on i386 and compatibles on Linux, Solaris/x86, GNU Hurd, Windows, BeOS and Haiku. Requires root privileges.</dd>
<dt><code>intel-conf2</code></dt>
<dd>Direct hardware access via Intel configuration mechanism 2. Available on i386 and compatibles on Linux, Solaris/x86, GNU Hurd, Windows, BeOS and Haiku. Requires root privileges. Warning: This method is able to address only the first 16 devices on any bus and it seems to be very unreliable in many cases.</dd>
<dt><code>fbsd-device</code></dt>
<dd>The <code>/dev/pci</code> device on FreeBSD. Requires root privileges.</dd>
<dt><code>aix-device</code></dt>
<dd>Access method used on AIX. Requires root privileges.</dd>
<dt><code>nbsd-libpci</code></dt>
<dd>The <code>/dev/pci0</code> device on NetBSD accessed using the local libpci library.</dd>
<dt><code>obsd-device</code></dt>
<dd>The <code>/dev/pci</code> device on OpenBSD. Requires root privileges.</dd>
<dt><code>dump</code></dt>
<dd>Read the contents of configuration registers from a file specified in the <code>dump.name</code> parameter. The format corresponds to the output of <i>lspci</i> <code>-x</code>.</dd>
<dt><code>darwin</code></dt>
<dd>Access method used on Mac OS X / Darwin. Must be run as root and the system must have been booted with debug=0x144. </dd>
</dl>
<h2>Parameters</h2>
<p>The library is controlled by several parameters. They should have sensible default values, but in case you want to do something unusual (or even something weird), you can override them (see the <code>-O</code> switch of <i>lspci</i>).</p>
<h3>Parameters of specific access methods</h3>
<dl>
<dt><code>dump.name</code></dt>
<dd>Name of the bus dump file to read from.</dd>
<dt><code>fbsd.path</code></dt>
<dd>Path to the FreeBSD PCI device.</dd>
<dt><code>nbsd.path</code></dt>
<dd>Path to the NetBSD PCI device.</dd>
<dt><code>obsd.path</code></dt>
<dd>Path to the OpenBSD PCI device.</dd>
<dt><code>proc.path</code></dt>
<dd>Path to the procfs bus tree.</dd>
<dt><code>sysfs.path</code></dt>
<dd>Path to the sysfs device tree. </dd>
</dl>
<h3>Parameters for resolving of ID&#8217;s via DNS</h3>
<dl>
<dt><code>net.domain</code></dt>
<dd>DNS domain containing the ID database.</dd>
<dt><code>net.cache_name</code></dt>
<dd>Name of the file used for caching of resolved ID&#8217;s. </dd>
</dl>
<h3>Parameters for resolving of ID&#8217;s via UDEV&#8217;s HWDB</h3>
<dl>
<dt><code>hwdb.disable</code></dt>
<dd>Disable use of HWDB if set to a non-zero value. </dd>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-lspci/">lspci</a></code>(8), <code><a href="/docs/linux/man/8-setpci/">setpci</a></code>(8), <code><a href="/docs/linux/man/5-pci-ids/">pci.ids</a></code>(5), <code><a href="/docs/linux/man/8-update-pciids/">update-pciids</a></code>(8) </p>
<h2>Author</h2>
<p>The PCI Utilities are maintained by Martin Mares &lt;mj [at] ucw.cz&gt;.</p>
