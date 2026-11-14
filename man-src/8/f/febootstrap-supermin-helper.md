---
title: "febootstrap-supermin-helper(8)"
name: "febootstrap-supermin-helper"
section: "8"
letter: "f"
url: "/docs/linux/man/8-febootstrap-supermin-helper/"
description: "febootstrap-supermin-helper – Reconstruct initramfs from supermin appliance."
---

<p>febootstrap-supermin-helper &#8211; Reconstruct initramfs from supermin appliance.</p>
<h2>Synopsis</h2>
<pre> febootstrap-supermin-helper supermin.img hostfiles.txt kernel initrd</pre>
<h2>Description</h2>
<p><i>febootstrap-supermin-helper</i> reconstructs a bootable kernel and initramfs from a supermin appliance. First you should be familiar with <i><a href="/docs/linux/man/8-febootstrap/">febootstrap</a></i>(8), <i><a href="/docs/linux/man/8-febootstrap-to-initramfs/">febootstrap-to-initramfs</a></i>(8) and <i><a href="/docs/linux/man/8-febootstrap-to-supermin/">febootstrap-to-supermin</a></i>(8).</p>
<h2>Parameters</h2>
<p>Of the four parameters, the first two are <i>input</i> files, and the last two are <i>output</i> files. </p>
<p> <tt>&quot;supermin.img&quot;</tt> and <tt>&quot;hostfiles.txt&quot;</tt> are the input files which describe the supermin appliance. </p>
<p> <tt>&quot;kernel&quot;</tt> and <tt>&quot;initrd&quot;</tt> are the temporary output files that this script produces. These output files are meant to be used just for booting the appliance, and should be deleted straight afterwards.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;kmods file</code></p>
<dd>If this option is specified, then <tt>&quot;file&quot;</tt> should be a list of wildcards matching kernel module names, eg: </p>
<pre> virtio*.ko
 scsi*.ko
 piix.ko</pre>
<p>In this case, only kernel modules matching those wildcards will be included in the output appliance. Note: You must resolve any dependencies yourself as this does not pull in dependent modules automatically. </p>
<p> If this option is not specified, then every kernel module from the host will be included. This is safer, but can produce rather large appliances which need a lot more memory to boot.</dl>
<h2>Speed</h2>
<p>In libguestfs, on a mid-range Intel-based <font SIZE="-1">PC</font>, we reconstruct the initramfs using this script in around 1/5th of a second (assuming a &#8220;hot cache&#8221; &#8211; it&#8217;s rather slower when run the first time on a cold cache). </p>
<p> Some tips to improve performance:</p>
<dl>
<dt>*</p>
<dd>Use a kernel module whitelist (the <tt>&quot;--kmods&quot;</tt> option), and only list the kernel modules you really need.</p>
<dt>*</p>
<dd>Minimize the appliance, removing as much extraneous junk as possible. </p>
<p> As well as using <i><a href="/docs/linux/man/8-febootstrap-minimize/">febootstrap-minimize</a></i>(8) it is worth checking for anything that is not necessary for your particular application and removing it by hand.</dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-febootstrap/">febootstrap</a></i>(8), <i><a href="/docs/linux/man/8-febootstrap-to-initramfs/">febootstrap-to-initramfs</a></i>(8), <i><a href="/docs/linux/man/8-febootstrap-to-supermin/">febootstrap-to-supermin</a></i>(8).</p>
<h2>Authors</h2>
<p>Richard W.M. Jones &lt;rjones @ redhat . com&gt;</p>
<h2>Copyright</h2>
<p>(C) Copyright 2009 Red Hat Inc., &lt;<a rel="nofollow" href="http://et.redhat.com/~rjones/febootstrap">http://et.redhat.com/~rjones/febootstrap</a>&gt;. </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT</font> <font SIZE="-1">ANY</font> <font SIZE="-1">WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS</font> <font SIZE="-1">FOR</font> A <font SIZE="-1">PARTICULAR</font> <font SIZE="-1">PURPOSE</font>. See the <font SIZE="-1">GNU</font> General Public License for more details. </p>
<p> You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, <font SIZE="-1">MA</font> 02139, <font SIZE="-1">USA</font>.</p>
