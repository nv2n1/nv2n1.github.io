---
title: "supermin-helper(8)"
name: "supermin-helper"
section: "8"
letter: "s"
url: "/docs/linux/man/8-supermin-helper/"
description: "supermin-helper – Reconstruct initramfs from supermin appliance."
---

<p>supermin-helper &#8211; Reconstruct initramfs from supermin appliance.</p>
<h2>Synopsis</h2>
<pre> supermin-helper supermin.img hostfiles.txt host_cpu kernel initrd
 supermin-helper input [...] host_cpu kernel initrd
 supermin-helper -f ext2 input [...] host_cpu kernel initrd appliance
 supermin-helper -f checksum input [...] host_cpu</pre>
<h2>Description</h2>
<p><i>supermin-helper</i> reconstructs a bootable kernel and initramfs from a supermin appliance. First you should be familiar with <i><a href="/docs/linux/man/8-supermin/">supermin</a></i>(8).</p>
<h2>Parameters</h2>
<p>Of the required parameters, the first few are <i>input</i> files, and the last two or three are <i>output</i> files. </p>
<p> <tt>&quot;supermin.img&quot;</tt> and <tt>&quot;hostfiles.txt&quot;</tt> are the input files which describe the supermin appliance. (You can also use a directory name here which is searched for files). </p>
<p> <tt>&quot;host_cpu&quot;</tt> should be the host <font SIZE="-1">CPU,</font> eg. <tt>&quot;x86_64&quot;</tt> or <tt>&quot;i686&quot;</tt>. </p>
<p> <tt>&quot;kernel&quot;</tt>, <tt>&quot;initrd&quot;</tt> and <tt>&quot;appliance&quot;</tt> are the temporary output files that this script produces. These output files are meant to be used just for booting the appliance, and should be deleted straight afterwards. The extra <tt>&quot;appliance&quot;</tt> parameter is only required when the format is <tt>&quot;ext2&quot;</tt>. None of these parameters are needed for the checksum output <tt>&quot;-f checksum&quot;</tt>.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd>Display brief command line usage, and exit.</p>
<dt><code>-f fmt</code></p>
<dd>
<dt><code>&#8211;format fmt</code></p>
<dd>Select the output format for the appliance. Possible formats are:</p>
<dl>
<dd>
<dl>
<dt>cpio</p>
<dd>A Linux initramfs. This is the default. </p>
<p> In this case you have to supply names for the <tt>&quot;kernel&quot;</tt> and <tt>&quot;initrd&quot;</tt>, where the <tt>&quot;initrd&quot;</tt> is the appliance. </p>
<p> Note that <i><a href="/docs/linux/man/1-cpio/">cpio</a></i>(1) might not be able to extract this file fully. The format used by the Linux kernel is not quite a true cpio file.</p>
<dt>ext2</p>
<dd>An ext2 filesystem. </p>
<p> In this case you have to supply names for the <tt>&quot;kernel&quot;</tt>, a small <tt>&quot;initrd&quot;</tt> which is used just to locate the appliance, and the <tt>&quot;appliance&quot;</tt> (the ext2 filesystem).</p>
<dt>checksum</p>
<dd>Output a checksum. </p>
<p> This prints a checksum which only changes when one of the input files changes. </p>
<p> You can use this in order to cache the output of a previous run of this program: computing the checksum is much quicker than building an appliance, and you only need to invalidate the cache (and consequently rebuild the appliance) when the checksum changes. Note that the host_cpu and the <font SIZE="-1">UID</font> of the current user are included in the checksum.</dl>
</dl>
<dl>
<dd></dl>
<dt><code>&#8211;copy-kernel</code></p>
<dd>Copy the kernel instead of symlinking to the kernel in <tt>&quot;/boot&quot;</tt>. </p>
<p> This is fractionally slower, but is necessary if you want to change the permissions or SELinux label on the kernel.</p>
<dt><code>-k file</code></p>
<dd>
<dt><code>&#8211;kmods file</code></p>
<dd>If this option is specified, then <tt>&quot;file&quot;</tt> should be a list of wildcards matching kernel module names, eg: </p>
<pre> virtio*.ko
 scsi*.ko
 piix.ko</pre>
<p>In this case, only kernel modules matching those wildcards will be included in the output appliance. Note: You must resolve any dependencies yourself as this does not pull in dependent modules automatically. </p>
<p> If this option is not specified, then every kernel module from the host will be included. This is safer, but can produce rather large appliances which need a lot more memory to boot.</p>
<dt><code>-u user</code></p>
<dd>
<dt><code>&#8211;user user</code></p>
<dd>
<dt><code>-g group</code></p>
<dd>
<dt><code>&#8211;group group</code></p>
<dd>Run supermin-helper as an alternate user and/or group. <tt>&quot;user&quot;</tt> and <tt>&quot;group&quot;</tt> can be specified as either a name, which will be resolved using the system name service, or a uid/gid. Use of these options requires root privileges. </p>
<p> Use of these options is required if running supermin-helper as root with the effective uid/gid set to non-root. Bash will reset the effective uid/gid to the real uid/gid when invoked. As supermin-helper uses bash in parts, this will result in the creation of an appliance with a mixture of ownerships.</p>
<dt><code>-v</code></p>
<dd>
<dt><code>&#8211;verbose</code></p>
<dd>Enable verbose messages (give multiple times for more verbosity).</p>
<dt><code>-V</code></p>
<dd>
<dt><code>&#8211;version</code></p>
<dd>Display version number and exit.</dl>
<h2>Compressed Input Files</h2>
<p>supermin-helper ≥ 4.1.4 supports gzip-compressed input cpio image files. <tt>&quot;hostfiles&quot;</tt> cannot be compressed. </p>
<p> Compressing input files saves space, but can make supermin-helper run fractionally slower.</p>
<h2>Speed</h2>
<p>In libguestfs, on a mid-range Intel-based <font SIZE="-1">PC,</font> we reconstruct the initramfs using this script in around 1/5th of a second (assuming a &#8220;hot cache&#8221; &#8211; it&#8217;s rather slower when run the first time on a cold cache). </p>
<p> Some tips to improve performance:</p>
<dl>
<dt>&bull;</p>
<dd>Use a kernel module whitelist (the <tt>&quot;--kmods&quot;</tt> option), and only list the kernel modules you really need.</p>
<dt>&bull;</p>
<dd>Minimize the appliance, removing as much extraneous junk as possible.</dl>
<h2>Environment Variables</h2>
<dl>
<dt><font SIZE="-1">SUPERMIN_KERNEL</font></p>
<dd>If this environment variable is set, then automatic selection of the kernel is bypassed and this kernel is used. </p>
<p> The environment variable should point to a kernel file, eg. <tt>&quot;/boot/vmlinuz-3.0.x86_64&quot;</tt> </p>
<p> The corresponding module path is guessed from the kernel name, but you can override that by setting <tt>&quot;SUPERMIN_MODULES&quot;</tt>.</p>
<dt><font SIZE="-1">SUPERMIN_MODULES</font></p>
<dd>If <tt>&quot;SUPERMIN_KERNEL&quot;</tt> and <tt>&quot;SUPERMIN_MODULES&quot;</tt> are both set, then automatic selection of the kernel is bypassed and the kernel and module path are set to these values. </p>
<p> The environment variable should point to a module directory, eg. <tt>&quot;/lib/modules/3.0.x86_64/&quot;</tt> </p>
<p> This has no effect if <tt>&quot;SUPERMIN_KERNEL&quot;</tt> is not set.</dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-supermin/">supermin</a></i>(8).</p>
<h2>Authors</h2>
<p>Richard W.M. Jones &lt;rjones @ redhat . com&gt;</p>
<h2>Copyright</h2>
<p>(C) Copyright 2009-2013 Red Hat Inc., &lt;<a rel="nofollow" href="http://people.redhat.com/~rjones/supermin">http://people.redhat.com/~rjones/supermin</a>&gt;. </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT ANY WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE. </font> See the <font SIZE="-1">GNU</font> General Public License for more details. </p>
<p> You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, <font SIZE="-1">MA 02139, USA.</font></p>
