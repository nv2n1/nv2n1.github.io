---
title: "findfs(8)"
name: "findfs"
section: "8"
letter: "f"
url: "/docs/linux/man/8-findfs/"
description: "findfs – find a filesystem by label or UUID"
---

<p>findfs &#8211; find a filesystem by label or UUID</p>
<h2>Synopsis</h2>
<p><code>findfs</code> <code>NAME</code>=<i>value</i></p>
<h2>Description</h2>
<p><code>findfs</code> will search the block devices in the system looking for a filesystem or partition with specified tag. The currently supported tags are: </p>
<p> <code>LABEL</code>=<i>&lt;label&gt;</i></p>
<dl>
<dd>Specifies filesystem label.</dl>
<p> <code>UUID</code>=<i>&lt;uuid&gt;</i></p>
<dl>
<dd>Specifies filesystem UUID.</dl>
<p> <code>PARTUUID</code>=<i>&lt;uuid&gt;</i></p>
<dl>
<dd>Specifies partition UUID. This partition identifier is supported for example for GUID Partition Table (GPT) partition tables.</dl>
<p> <code>PARTLABEL</code>=<i>&lt;label&gt;</i></p>
<dl>
<dd>Specifies partition label (name). The partition labels are supported for example for GUID Partition Table (GPT) or MAC partition tables.</dl>
<p> If the filesystem or partition is found, the device name will be printed on stdout. </p>
<p> The complete overview about filesystems and partitions you can get for example by</p>
<dl>
<dd><code>lsblk &#8211;fs</code> </p>
<p> <code>partx &#8211;show &lt;disk&gt;</code> </p>
<p> <code>blkid</code>
</dl>
<h2>Exit Status</h2>
<p><code>0</code></p>
<dl>
<dd>success</dl>
<p> <code>1</code></p>
<dl>
<dd>label or uuid cannot be found</dl>
<p> <code>2</code></p>
<dl>
<dd>usage error, wrong number of arguments or unknown option</dl>
<h2>Environment</h2>
<p>LIBBLKID_DEBUG=all</p>
<dl>
<dd>enables libblkid debug output.</dl>
<h2>Authors</h2>
<p><code>findfs</code> was originally written by and re-written for the util-linux package by</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-blkid/">blkid</a></code>(8), <code><a href="/docs/linux/man/8-lsblk/">lsblk</a></code>(8), <code><a href="/docs/linux/man/8-partx/">partx</a></code>(8)</p>
<h2>Reporting Bugs</h2>
<p>For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>Availability</h2>
<p>The <code>findfs</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;.</p>
