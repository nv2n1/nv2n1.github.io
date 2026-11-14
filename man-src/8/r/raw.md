---
title: "raw(8)"
name: "raw"
section: "8"
letter: "r"
url: "/docs/linux/man/8-raw/"
description: "raw – bind a Linux raw character device"
---

<p>raw &#8211; bind a Linux raw character device</p>
<h2>Synopsis</h2>
<p><code>raw</code> <i>/dev/raw/raw&lt;N&gt; &lt;major&gt; &lt;minor&gt;</i> </p>
<p> <code>raw</code> <i>/dev/raw/raw&lt;N&gt; /dev/&lt;blockdev&gt;</i> </p>
<p> <code>raw -q</code> <i>/dev/raw/raw&lt;N&gt;</i> </p>
<p> <code>raw -qa</code></p>
<h2>Description</h2>
<p><code>raw</code> is used to bind a Linux raw character device to a block device. Any block device may be used: at the time of binding, the device driver does not even have to be accessible (it may be loaded on demand as a kernel module later). </p>
<p> <code>raw</code> is used in two modes: it either sets raw device bindings, or it queries existing bindings. When setting a raw device, <i>/dev/raw/raw&lt;N&gt;</i> is the device name of an existing raw device node in the filesystem. The block device to which it is to be bound can be specified either in terms of its <i>major</i> and <i>minor</i> device numbers, or as a path name <i>/dev/&lt;blockdev&gt;</i> to an existing block device file. </p>
<p> The bindings already in existence can be queried with the <i>-q</i> option, which is used either with a raw device filename to query that one device, or with the <i>-a</i> option to query all bound raw devices. </p>
<p> Unbinding can be done by specifying major and minor 0. </p>
<p> Once bound to a block device, a raw device can be opened, read and written, just like the block device it is bound to. However, the raw device does not behave exactly like the block device. In particular, access to the raw device bypasses the kernel&#8217;s block buffer cache entirely: all I/O is done directly to and from the address space of the process performing the I/O. If the underlying block device driver can support DMA, then no data copying at all is required to complete the I/O. </p>
<p> Because raw I/O involves direct hardware access to a process&#8217;s memory, a few extra restrictions must be observed. All I/Os must be correctly aligned in memory and on disk: they must start at a sector offset on disk, they must be an exact number of sectors long, and the data buffer in virtual memory must also be aligned to a multiple of the sector size. The sector size is 512 bytes for most devices.</p>
<h2>Options</h2>
<dl>
<dt><code>-q</code>, <code>&#8211;query</code></p>
<dd>Set query mode. <code>raw</code> will query an existing binding instead of setting a new one.</p>
<dt><code>-a</code>, <code>&#8211;all</code></p>
<dd>With <code>-q</code> , specify that all bound raw devices should be queried.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Display help text and exit.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Display version information and exit. </p>
</dl>
<h2>Bugs</h2>
<p>The Linux <code><a href="/docs/linux/man/1-dd/">dd</a></code>(1) command should be used without the <code>bs=</code> option, or the blocksize needs to be a multiple of the sector size of the device (512 bytes usually), otherwise it will fail with &quot;Invalid Argument&quot; messages (EINVAL). </p>
<p> Raw I/O devices do not maintain cache coherency with the Linux block device buffer cache. If you use raw I/O to overwrite data already in the buffer cache, the buffer cache will no longer correspond to the contents of the actual storage device underneath. This is deliberate, but is regarded either a bug or a feature depending on who you ask!</p>
<h2>Notes</h2>
<p>Rather than using raw devices applications should prefer <code><a href="/docs/linux/man/2-open/">open</a></code>(2) devices, such as /dev/sda1, with the O_DIRECT flag.</p>
<h2>Author</h2>
<p>Stephen Tweedie (sct [at] redhat.com)</p>
<h2>Availability</h2>
<p>The raw command is part of the util-linux package and is available from <a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/.">https://www.kernel.org/pub/linux/utils/util-linux/.</a></p>
