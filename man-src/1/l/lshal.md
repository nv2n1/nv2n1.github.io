---
title: "lshal(1)"
name: "lshal"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lshal/"
description: "lshal – list HAL devices"
---

<h2>NAME</h2>
<p> lshal &#8211; list HAL devices</p>
<h2>SYNOPSIS</h2>
<p> <code>lshal</code> [options] </p>
<h2>DESCRIPTION</h2>
<p> <i>lshal</i> is a utility for displaying items in the <code>HAL </code> device database. For more information about both the big picture and specific <code>HAL</code> properties, refer to the <i>HAL spec</i> which can be found in <i>/usr/share/doc/hal-0.5.13/spec/hal-spec.html</i> depending on the distribution. </p>
<h2>OPTIONS</h2>
<p> The following options are supported:</p>
<dl>
<dt><i>-m, &#8211;monitor</i></p>
<dd> Print changes emitted by the <code>hald</code> daemon.</p>
<dt><i>-s, &#8211;short</i></p>
<dd> Short output.</p>
<dt><i>-t, &#8211;tree</i></p>
<dd> Display the devices organized in a tree.</p>
<dt><i>-u, &#8211;show</i></p>
<dd> Show only the given UDI (<i>Unique Device Identifier</i>).</p>
<dt><i>-h, &#8211;help</i></p>
<dd> Print out usage.</p>
<dt><i>-V, &#8211;version</i></p>
<dd> Print the version. </p>
</dl>
<h2>BUGS</h2>
<p> Please send bug reports to either the distribution or the HAL mailing list, see <i><a rel="nofollow" href="http://lists.freedesktop.org/mailman/listinfo/hal">http://lists.freedesktop.org/mailman/listinfo/hal</a></i> on how to subscribe. </p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/8-hald/">hald</a></i>(8), <i><a href="/docs/linux/man/1-hal-get-property/">hal-get-property</a></i>(1), <i><a href="/docs/linux/man/1-hal-set-property/">hal-set-property</a></i>(1), <i><a href="/docs/linux/man/1-hal-find-by-property/">hal-find-by-property</a></i>(1), <i><a href="/docs/linux/man/1-hal-find-by-capability/">hal-find-by-capability</a></i>(1) </p>
<h2>AUTHOR</h2>
<p> Written by David Zeuthen &lt;david [at] fubar.dk&gt; with a lot of help from many others. </p>
<h2>Index</h2>
