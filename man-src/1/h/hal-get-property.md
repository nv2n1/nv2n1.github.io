---
title: "hal-get-property(1)"
name: "hal-get-property"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hal-get-property/"
description: "hal-get-property – get a property from a device object"
---

<h2>NAME</h2>
<p> hal-get-property &#8211; get a property from a device object</p>
<h2>SYNOPSIS</h2>
<p> <code>hal-get-property</code> [options] </p>
<h2>DESCRIPTION</h2>
<p> <i>hal-get-property</i> retrieves a property from a device object in the <code>HAL </code> device database. For more information about both the big picture and specific <code>HAL</code> properties, refer to the <i>HAL spec</i> which can be found in <i>/usr/share/doc/hal-0.5.13/spec/hal-spec.html</i> depending on the distribution. </p>
<h2>OPTIONS</h2>
<p> The following options are supported:</p>
<dl>
<dt><i>&#8211;udi</i></p>
<dd> The UDI (<i>Unique Device Identifier</i>) of the device object.</p>
<dt><i>&#8211;key</i></p>
<dd> The name of the property.</p>
<dt><i>&#8211;hex</i></p>
<dd> Show int32/uint64 values in hex (without a leading 0x).</p>
<dt><i>&#8211;verbose</i></p>
<dd> Verbose output.</p>
<dt><i>&#8211;help</i></p>
<dd> Print out usage.</p>
<dt><i>&#8211;version</i></p>
<dd> Print the version. </p>
</dl>
<h2>RETURN VALUE</h2>
<p> If both the property and device object exists the value of the property is printed on <i>stdout</i> and the program will exit with exit code 0. Otherwise the exit code will be non-zero. </p>
<h2>BUGS</h2>
<p> Please send bug reports to either the distribution or the HAL mailing list, see <i><a rel="nofollow" href="http://lists.freedesktop.org/mailman/listinfo/hal">http://lists.freedesktop.org/mailman/listinfo/hal</a></i> on how to subscribe. </p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/8-hald/">hald</a></i>(8), <i><a href="/docs/linux/man/1-lshal/">lshal</a></i>(1), <i><a href="/docs/linux/man/1-hal-set-property/">hal-set-property</a></i>(1), <i><a href="/docs/linux/man/1-hal-find-by-property/">hal-find-by-property</a></i>(1), <i><a href="/docs/linux/man/1-hal-find-by-capability/">hal-find-by-capability</a></i>(1) </p>
<h2>AUTHOR</h2>
<p> Written by David Zeuthen &lt;david [at] fubar.dk&gt; with a lot of help from many others. </p>
<h2>Index</h2>
