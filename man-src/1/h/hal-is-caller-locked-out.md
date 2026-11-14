---
title: "hal-is-caller-locked-out(1)"
name: "hal-is-caller-locked-out"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hal-is-caller-locked-out/"
description: "hal-is-caller-locked-out – determine if a caller is locked out"
---

<h2>NAME</h2>
<p> hal-is-caller-locked-out &#8211; determine if a caller is locked out</p>
<h2>SYNOPSIS</h2>
<p> <code>hal-is-caller-locked-out</code> [options] </p>
<h2>DESCRIPTION</h2>
<p> <i>hal-is-caller-locked-out</i> determines if a specific caller is locked out of a specific D-Bus interface on a specific device. For more information about both the big picture and specific <code>HAL</code> properties, refer to the <i>HAL spec</i> which can be found in <i>/usr/share/doc/hal-0.5.13/spec/hal-spec.html</i> depending on the distribution. </p>
<h2>OPTIONS</h2>
<p> The following options are supported:</p>
<dl>
<dt><i>&#8211;udi</i></p>
<dd> The UDI (<i>Unique Device Identifier</i>) of the device object.</p>
<dt><i>&#8211;interface</i></p>
<dd> The name of the interface to check for.</p>
<dt><i>&#8211;caller</i></p>
<dd> The unique D-Bus name on the system bus of the caller.</p>
<dt><i>&#8211;help</i></p>
<dd> Print out usage.</p>
<dt><i>&#8211;version</i></p>
<dd> Print the version. </p>
</dl>
<h2>RETURN VALUE</h2>
<p> If the given process is locked out or an error occurs, this program exits with exit code 1. Otherwise it exits with exit code 0. Note that only the super user (root) or other privileged users can use this tool. </p>
<h2>BUGS</h2>
<p> Please send bug reports to either the distribution or the HAL mailing list, see <i><a rel="nofollow" href="http://lists.freedesktop.org/mailman/listinfo/hal">http://lists.freedesktop.org/mailman/listinfo/hal</a></i> on how to subscribe. </p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/8-hald/">hald</a></i>(8), <i><a href="/docs/linux/man/1-lshal/">lshal</a></i>(1), <i><a href="/docs/linux/man/1-hal-get-property/">hal-get-property</a></i>(1), <i><a href="/docs/linux/man/1-hal-set-property/">hal-set-property</a></i>(1), <i><a href="/docs/linux/man/1-hal-find-by-property/">hal-find-by-property</a></i>(1), <i><a href="/docs/linux/man/1-hal-find-by-capability/">hal-find-by-capability</a></i>(1) </p>
<h2>AUTHOR</h2>
<p> Written by David Zeuthen &lt;david [at] fubar.dk&gt; with a lot of help from many others. </p>
<h2>Index</h2>
