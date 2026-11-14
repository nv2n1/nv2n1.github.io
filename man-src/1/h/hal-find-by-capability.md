---
title: "hal-find-by-capability(1)"
name: "hal-find-by-capability"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hal-find-by-capability/"
description: "hal-find-by-capability – find device objects by capability matching"
---

<h2>NAME</h2>
<p> hal-find-by-capability &#8211; find device objects by capability matching</p>
<h2>SYNOPSIS</h2>
<p> <code>hal-find-by-capability</code> [options] </p>
<h2>DESCRIPTION</h2>
<p> <i>hal-get-capability</i> finds device object in the <code>HAL </code> device database by looking at device capabilities. For more information about both the big picture and specific <code>HAL</code> properties, refer to the <i>HAL spec</i> which can be found in <i>/usr/share/doc/hal-0.5.13/spec/hal-spec.html</i> depending on the distribution. </p>
<h2>OPTIONS</h2>
<p> The following options are supported:</p>
<dl>
<dt><i>&#8211;capability</i></p>
<dd> The name of the capability.</p>
<dt><i>&#8211;verbose</i></p>
<dd> Verbose output.</p>
<dt><i>&#8211;help</i></p>
<dd> Print out usage.</p>
<dt><i>&#8211;version</i></p>
<dd> Print the version. </p>
</dl>
<h2>RETURN VALUE</h2>
<p> If devices matching the given capability are found each UDI (<i>Unique Device Identifier</i>) is printed on stdout and the program exits with exit code 0. If no devices are found or an error occured, the program exits with a non-zero exit code. </p>
<h2>BUGS</h2>
<p> Please send bug reports to either the distribution or the HAL mailing list, see <i><a rel="nofollow" href="http://lists.freedesktop.org/mailman/listinfo/hal">http://lists.freedesktop.org/mailman/listinfo/hal</a></i> on how to subscribe. </p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/8-hald/">hald</a></i>(8), <i><a href="/docs/linux/man/1-lshal/">lshal</a></i>(1), <i><a href="/docs/linux/man/1-hal-set-property/">hal-set-property</a></i>(1), <i><a href="/docs/linux/man/1-hal-get-property/">hal-get-property</a></i>(1), <i><a href="/docs/linux/man/1-hal-find-by-property/">hal-find-by-property</a></i>(1), <i><a href="/docs/linux/man/1-dbus-send/">dbus-send</a></i>(1) </p>
<h2>AUTHOR</h2>
<p> Written by David Zeuthen &lt;david [at] fubar.dk&gt; with a lot of help from many others. </p>
<h2>Index</h2>
