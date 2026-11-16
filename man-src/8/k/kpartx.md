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
<dt><code>-a</code></dt>
<dd>Add partition mappings.</dd>
<dt><code>-d</code></dt>
<dd>Delete partition mappings.</dd>
<dt><code>-u</code></dt>
<dd>Update partition mappings.</dd>
<dt><code>-l</code></dt>
<dd>List partition mappings that would be added -a.</dd>
<dt><code>-r</code></dt>
<dd>Read-only partition mappings.</dd>
<dt><code>-p</code></dt>
<dd>Set device name-partition number delimiter.</dd>
<dt><code>-f</code></dt>
<dd>Force creation of mappings; overrides &#8216;no_partitions&#8217; feature.</dd>
<dt><code>-g</code></dt>
<dd>Force GUID partition table (GPT).</dd>
<dt><code>-s</code></dt>
<dd>Sync mode (Default). Don&#8217;t return until the partitions are created.</dd>
<dt><code>-n</code></dt>
<dd>Nosync mode. Return before the partitions are created.</dd>
<dt><code>-v</code></dt>
<dd>Operate verbosely.</dd></dl>
<h2>Example</h2>
<p>To mount all the partitions in a raw disk image:</p>
<dl>
<dd>kpartx -av disk.img</dd></dl>
<p> This will output lines such as:</p>
<dl>
<dd>add map loop1p1 (254:4): 0 409597 linear 7:1 3</dd></dl>
<p> The <i>loop1p1</i> is the name of a device file under <i>/dev/mapper</i> which you can use to access the partition, for example to fsck it:</p>
<dl>
<dd>fsck /dev/mapper/loop1p1</dd></dl>
<p> When you&#8217;re done, you need to remove the devices:</p>
<dl>
<dd>kpartx -d disk.img</dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-multipath/">multipath</a></code>(8) <code><a href="/docs/linux/man/8-multipathd/">multipathd</a></code>(8) <code>hotplug</code>(8)</p>
<h2>Authors</h2>
<p>This man page was assembled By Patrick Caulfield for the Debian project. </p>
<p> <i>multipath-tools</i> was developed by Christophe Varoqui &lt;christophe.varoqui [at] opensvc.com&gt; and others.</p>
