---
title: "libblkid(3)"
name: "libblkid"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libblkid/"
description: "libblkid – block device identification library"
---

<h2 class="name">NAME</h2>
<p> libblkid &#8211; block device identification library </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;blkid.h&gt;</code> </p>
<p> <code>cc</code> <i>file.c</i> <code>-lblkid</code></p>
<h2>DESCRIPTION</h2>
<p> The <code>libblkid</code> library is used to identify block devices (disks) as to their content (e.g. filesystem type) as well as extracting additional information such as filesystem labels/volume names, unique identifiers/serial numbers. A common use is to allow use of LABEL= and UUID= tags instead of hard-coding specific block device names into configuration files. </p>
<p> The low-level part of the library also allows to extract information about partitions and block device topology. </p>
<p> The high-level part of the library keeps information about block devices in a cache file and is verified to still be valid before being returned to the user (if the user has read permission on the raw block device, otherwise not). The cache file also allows unprivileged users (normally anyone other than root, or those not in the &quot;disk&quot; group) to locate devices by label/id. The standard location of the cache file can be overridden by the environment variable BLKID_FILE. </p>
<p> In situations where one is getting information about a single known device, it does not impact performance whether the cache is used or not (unless you are not able to read the block device directly). </p>
<p> The high-level part of the library supports two methods to evaluate LABEL/UUID. It reads information directly from a block device or read information from /dev/disk/by-* udev symlinks. The udev is preferred method by default. </p>
<p> If you are dealing with multiple devices, use of the cache is highly recommended (even if empty) as devices will be scanned at most one time and the on-disk cache will be updated if possible. </p>
<p> In some cases (modular kernels), block devices are not even visible until after they are accessed the first time, so it is critical that there is some way to locate these devices without enumerating only visible devices, so the use of the cache file is <code>required</code> in this situation.</p>
<h2>CONFIGURATION FILE</h2>
<p> The standard location of the <i>/etc/blkid.conf</i> config file can be overridden by the environment variable BLKID_CONF. For more details about the config file see <code><a href="/docs/linux/man/8-blkid/">blkid</a></code>(8) man page.</p>
<h2>AUTHOR</h2>
<p> <code>libblkid</code> was written by Andreas Dilger for the ext2 filesystem utilities, with input from Ted Ts&#8217;o. The library was subsequently heavily modified by Ted Ts&#8217;o. </p>
<p> The low-level probing code was rewritten by Karel Zak.</p>
<h2>COPYING</h2>
<p> <code>libblkid</code> is available under the terms of the GNU Library General Public License (LGPL), version 2 (or at your discretion any later version).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-blkid/">blkid</a></code>(8), <code><a href="/docs/linux/man/8-findfs/">findfs</a></code>(8)</p>
<h2>AVAILABILITY</h2>
<p> libblkid is part of the util-linux package since version 2.15 and is available from <a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/.">https://www.kernel.org/pub/linux/utils/util-linux/.</a> </p>
<h2>Index</h2>
