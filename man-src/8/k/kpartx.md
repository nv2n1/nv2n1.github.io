---
title: "kpartx(8)"
name: "kpartx"
section: "8"
letter: "k"
url: "/docs/linux/man/8-kpartx/"
description: "kpartx – Create device maps from partition tables."
---

<p>kpartx &#8211; Create device maps from partition tables.</p>
<h2>Synopsis</h2>
<p><code>kpartx</code> [<code>-a</code>|<code>-d</code>|<code>-u</code>|<code>-l</code>] [<code>-r</code>] [<code>-p</code>] [<code>-f</code>] [<code>-g</code>] [<code>-s</code>|<code>-n</code>] [<code>-v</code>] <code>wholedisk</code></p>
<h2>Description</h2>
<p>This tool, derived from util-linux&#8217; partx, reads partition tables on specified device and create device maps over partitions segments detected. It is called from hotplug upon device maps creation and deletion.</p>
<h2>Options</h2>
<dl>
<dt><code>-a</code></p>
<dd>Add partition mappings.</p>
<dt><code>-d</code></p>
<dd>Delete partition mappings.</p>
<dt><code>-u</code></p>
<dd>Update partition mappings.</p>
<dt><code>-l</code></p>
<dd>List partition mappings that would be added -a.</p>
<dt><code>-r</code></p>
<dd>Read-only partition mappings.</p>
<dt><code>-p</code></p>
<dd>Set device name-partition number delimiter.</p>
<dt><code>-f</code></p>
<dd>Force creation of mappings; overrides &#8216;no_partitions&#8217; feature.</p>
<dt><code>-g</code></p>
<dd>Force GUID partition table (GPT).</p>
<dt><code>-s</code></p>
<dd>Sync mode (Default). Don&#8217;t return until the partitions are created.</p>
<dt><code>-n</code></p>
<dd>Nosync mode. Return before the partitions are created.</p>
<dt><code>-v</code></p>
<dd>Operate verbosely.</dl>
<h2>Example</h2>
<p>To mount all the partitions in a raw disk image:</p>
<dl>
<dd>kpartx -av disk.img</dl>
<p> This will output lines such as:</p>
<dl>
<dd>add map loop1p1 (254:4): 0 409597 linear 7:1 3</dl>
<p> The <i>loop1p1</i> is the name of a device file under <i>/dev/mapper</i> which you can use to access the partition, for example to fsck it:</p>
<dl>
<dd>fsck /dev/mapper/loop1p1</dl>
<p> When you&#8217;re done, you need to remove the devices:</p>
<dl>
<dd>kpartx -d disk.img</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-multipath/">multipath</a></code>(8) <code><a href="/docs/linux/man/8-multipathd/">multipathd</a></code>(8) <code><a href="/docs/linux/man/8-hotplug/">hotplug</a></code>(8)</p>
<h2>Authors</h2>
<p>This man page was assembled By Patrick Caulfield for the Debian project. </p>
<p> <i>multipath-tools</i> was developed by Christophe Varoqui &lt;christophe.varoqui [at] opensvc.com&gt; and others.</p>
