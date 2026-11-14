---
title: "aoe-stat(8)"
name: "aoe-stat"
section: "8"
letter: "a"
url: "/docs/linux/man/8-aoe-stat/"
description: "aoe-stat – print aoe device status report"
---

<p>aoe-stat &#8211; print aoe device status report</p>
<h2>Synopsis</h2>
<pre><code>modprobe aoe</code>
<code>aoe-stat</code>
<code>env sysfs_dir=/sys aoe-stat</code></pre>
<h2>Description</h2>
<p>The <i>aoe-stat</i> script collects information on ATA over Ethernet devices from sysfs. </p>
<p> For each AoE device the kernel has discovered, there is one row in the script&#8217;s output. Each row has the following columns.</p>
<dl>
<dt><code>devicename</code></p>
<dd>The device name is of the form <i>eX.Y,</i><br />
&nbsp;<wbr>with&nbsp;<wbr> <i>X</i> being the AoE device shelf address, and <i>Y </i> being the AoE slot address.</p>
<dt><code>size</code></p>
<dd>The size of the AoE device is in gigabytes (billions of bytes).</p>
<dt><code>ifname</code></p>
<dd>The network interface name is printed in the third column.</p>
<dt><code>payload</code></p>
<dd>If the driver exports the per-packet data payload size, it will appear in the fourth column, expressed in bytes.</p>
<dt><code>status</code></p>
<dd>The device status is in the last column. Possible values are <i> up</i>, <i> down</i>, and <i> down,closewait</i>. The &quot;up&quot; status means the aoe driver considers this device ready for I/O. The &quot;down&quot; status means the opposite. The &quot;down,closewait&quot; status means that some software still has the device open, and when this straggler closes the device, it will enter the &quot;down&quot; state.</dl>
<h2>Environment Variables</h2>
<p>If the <i>sysfs_dir</i> variable is set in the environment, it will override the default location where <i>aoe-stat</i> will look for sysfs, namely <i> /sys</i>.</p>
<h2>Warnings</h2>
<p>If the minor device number of a device node does not match that of its namesake, <i>aoe-stat</i> will print a warning as shown below.</p>
<dl>
<dd>
<pre>nai:~# aoe-stat
 e0.3 0.104GB eth0 up 
 e0.4 4398.046GB eth0 up 
 e20.0 1000.215GB eth0 up 
 e42.0 2000.431GB eth0 up 
aoe-stat Warning: device node /dev/etherd/e45.1 has wrong minor device number
 e45.1 1152.874GB eth0 up </pre>
</dl>
<p> Using such a device node is dangerous, because its name doesn&#8217;t match the actual device that you would be reading from and writing to. Such a broken device node should be removed. Device nodes are created by <i>udev</i> or (on systems without <i>udev</i>) by <i>aoe-mkdevs</i>.</p>
<h2>Example</h2>
<p>In this example, the root user on a host named <i>nai</i> loads the aoe driver module and then prints a list of all the available aoe devices. Then he remembers to bring up the storage network interfaces, does an AoE discovery, and prints the list again. This time the list shows all the devices in shelf seven.</p>
<dl>
<dd>
<pre>nai:~# modprobe aoe
nai:~# aoe-stat
nai:~# ifconfig eth3 up
nai:~# aoe-discover 
nai:~# aoe-stat
 e0.0 10995.116GB eth0 up 
 e0.1 10995.116GB eth0 up 
 e0.2 10995.116GB eth0 up 
 e1.0 1152.874GB eth0 up 
 e7.0 370.566GB eth0 up 
nai:~# </pre>
</dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-aoe-discover/">aoe-discover</a></i>(8), <i><a href="/docs/linux/man/8-aoe-interfaces/">aoe-interfaces</a></i>(8), <i><a href="/docs/linux/man/8-aoe-mkdevs/">aoe-mkdevs</a></i>(8), <i><a href="/docs/linux/man/8-aoe-mkshelf/">aoe-mkshelf</a></i>(8), <i><a href="/docs/linux/man/8-aoetools/">aoetools</a></i>(8), <i><a href="/docs/linux/man/7-udev/">udev</a></i>(7).</p>
<h2>Author</h2>
<p>Ed L. Cashin (ecashin [at] coraid.com)</p>
