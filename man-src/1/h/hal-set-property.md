---
title: "hal-set-property(1)"
name: "hal-set-property"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hal-set-property/"
description: "hal-set-property – set a property on a device object"
---

<h2>NAME</h2>
<p> hal-set-property &#8211; set a property on a device object</p>
<h2>SYNOPSIS</h2>
<p> <code>hal-set-property</code> [options] </p>
<h2>DESCRIPTION</h2>
<p> <i>hal-set-property</i> sets a property on a device object in the <code>HAL </code> device database. For more information about both the big picture and specific <code>HAL</code> properties, refer to the <i>HAL spec</i> which can be found in <i>/usr/share/doc/hal-0.5.13/spec/hal-spec.html</i> depending on the distribution. </p>
<h2>OPTIONS</h2>
<p> The following options are supported:</p>
<dl>
<dt><i>&#8211;udi</i></p>
<dd> The UDI (<i>Unique Device Identifier</i>) of the device object.</p>
<dt><i>&#8211;key</i></p>
<dd> The name of the property.</p>
<dt><i>&#8211;int</i></p>
<dd> Set value property of the property to a 32-bit signed integer. The value passed is assumed to be decimal unless it&#8217;s prefixed with <code>0x</code> or <code>x</code> for hexadecimal values.</p>
<dt><i>&#8211;uint64</i></p>
<dd> Set value property of the property to a 64-bit unsigned integer. The value passed is assumed to be decimal unless it&#8217;s prefixed with <code>0x</code> or <code>x</code> for hexadecimal values.</p>
<dt><i>&#8211;string</i></p>
<dd> Set value property of the property to a string.</p>
<dt><i>&#8211;double</i></p>
<dd> Set value property of the property to a floating point number.</p>
<dt><i>&#8211;bool</i></p>
<dd> Set value property of the property to boolean, e.g. <code>true </code> or <code>false.</code></p>
<dt><i>&#8211;strlist-pre</i></p>
<dd> Prepend an item to a string list.</p>
<dt><i>&#8211;strlist-post</i></p>
<dd> Append an item to a string list.</p>
<dt><i>&#8211;strlist-rem</i></p>
<dd> Remove an item from a string list.</p>
<dt><i>&#8211;remove</i></p>
<dd> Remove a property.</p>
<dt><i>&#8211;help</i></p>
<dd> Print out usage.</p>
<dt><i>&#8211;version</i></p>
<dd> Print the version. </p>
</dl>
<h2>RETURN VALUE</h2>
<p> If setting the property succeeds, this program will exit with exit code 0. On errors a non-zero the program will exit with a non-zero exit code. Note that setting properties on the <code>HAL</code> device database usually requires super user privileges. </p>
<h2>BUGS</h2>
<p> Please send bug reports to either the distribution or the HAL mailing list, see <i><a rel="nofollow" href="http://lists.freedesktop.org/mailman/listinfo/hal">http://lists.freedesktop.org/mailman/listinfo/hal</a></i> on how to subscribe. </p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/8-hald/">hald</a></i>(8), <i><a href="/docs/linux/man/1-lshal/">lshal</a></i>(1), <i><a href="/docs/linux/man/1-hal-get-property/">hal-get-property</a></i>(1), <i><a href="/docs/linux/man/1-hal-find-by-property/">hal-find-by-property</a></i>(1), <i><a href="/docs/linux/man/1-hal-find-by-capability/">hal-find-by-capability</a></i>(1) </p>
<h2>AUTHOR</h2>
<p> Written by David Zeuthen &lt;david [at] fubar.dk&gt; with a lot of help from many others. </p>
<h2>Index</h2>
