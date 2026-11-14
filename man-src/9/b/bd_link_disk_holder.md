---
title: "bd_link_disk_holder(9)"
name: "bd_link_disk_holder"
section: "9"
letter: "b"
url: "/docs/linux/man/9-bd_link_disk_holder/"
description: "bd_link_disk_holder – create symlinks between holding disk and slave bdev"
---

<p>bd_link_disk_holder &#8211; create symlinks between holding disk and slave bdev</p>
<h2>Synopsis</h2>
<pre><code>int bd_link_disk_holder(struct block_device *bdev, struct gendisk *disk);</code></pre>
<h2>Arguments</h2>
<p><i>bdev</i></p>
<dl>
<dd>
<dd>the claimed slave bdev</dl>
<p> <i>disk</i></p>
<dl>
<dd>the holding disk</dl>
<h2>Description</h2>
<p>DON&#8217;T USE THIS UNLESS YOU&#8217;RE ALREADY USING IT. </p>
<p> This functions creates the following sysfs symlinks. </p>
<p> &#8211; from &#8220;slaves&#8221; directory of the holder <i>disk</i> to the claimed <i>bdev</i> &#8211; from &#8220;holders&#8221; directory of the <i>bdev</i> to the holder <i>disk</i> </p>
<p> For example, if /dev/dm-0 maps to /dev/sda and disk for dm-0 is passed to <code>bd_link_disk_holder</code>, then: </p>
<p> /sys/block/dm-0/slaves/sda &#8211;&gt; /sys/block/sda /sys/block/sda/holders/dm-0 &#8211;&gt; /sys/block/dm-0 </p>
<p> The caller must have claimed <i>bdev</i> before calling this function and ensure that both <i>bdev</i> and <i>disk</i> are valid during the creation and lifetime of these symlinks.</p>
<h2>Context</h2>
<p>Might sleep.</p>
<h2>Return</h2>
<p>0 on success, -errno on failure.</p>
<h2>Copyright</h2>
