---
title: "pktsetup(8)"
name: "pktsetup"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pktsetup/"
description: "pktsetup – set up and tear down packet device associations"
---

<p>pktsetup &#8211; set up and tear down packet device associations</p>
<h2>Synopsis</h2>
<p><code>pktsetup</code> <i>packet_device block_device</i><br />
 <code>pktsetup</code> <code>-d</code> <i>packet_device</i><br />
 <code>pktsetup</code> <code>-s</code></p>
<h2>Description</h2>
<p><code>Pktsetup</code> is used to associate packet devices with CD or DVD block devices, so that the packet device can then be mounted and potentially used as a read/write filesystem. This requires kernel support for the packet device, and the UDF filesystem. See: <a rel="nofollow" href="http://packet-cd.sourceforge.net/">http://packet-cd.sourceforge.net/</a> </p>
<h2>Exit Status</h2>
<p><code>Pktsetup</code> returns 0 on success, nonzero on failure.</p>
<h2>Options</h2>
<dl>
<dt><code>-d </code><i>packet-device</i></p>
<dd>Delete the association between the specified <i>packet-device</i> and its block device.</p>
<dt><code>-s</p>
<dd>Show device mappings. </p>
</dl>
<p> </code></p>
<h2>Example</h2>
<p>The following commands provide an example of using the packet device. </p>
<pre><dl><dt><dd>cdrwtool -d /dev/sr0 -q
pktsetup /dev/pktcdvd0 /dev/sr0
mount -t udf /dev/pktcdvd0 /mnt
 ...
umount /dev/pktcdvd0
pktsetup -d /dev/pktcdvd0</pre>
</dl>
<h2>Files</h2>
<pre>/dev/pktcdvd0,/dev/pktcdvd1,... CD/DVD packet devices (block major=97)</pre>
<h2>Author</h2>
<pre>Jens Axboe &lt;axboe [at] suse.de&gt;</pre>
<h2>Availability</h2>
<p><code>pktsetup</code> is part of the udftools package and is available from <a rel="nofollow" href="http://linux-udf.sourceforge.net.">http://linux-udf.sourceforge.net.</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-cdrwtool/">cdrwtool</a></code>(1) </p>
