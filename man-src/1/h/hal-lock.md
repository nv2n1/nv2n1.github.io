---
title: "hal-lock(1)"
name: "hal-lock"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hal-lock/"
description: "hal-lock – lock an interface"
---

<h2>NAME</h2>
<p> hal-lock &#8211; lock an interface</p>
<h2>SYNOPSIS</h2>
<p> <code>hal-lock</code> [options] </p>
<h2>DESCRIPTION</h2>
<p> <i>hal-lock</i> can be used to acquire a lock on a given interface either on a given device or globally. For more information about both the big picture and the semantics of <code>HAL</code> locks, refer to the <i>HAL spec</i> which can be found in <i>/usr/share/doc/hal-0.5.13/spec/hal-spec.html</i> depending on the distribution. </p>
<h2>OPTIONS</h2>
<p> The following options are supported:</p>
<dl>
<dt><i>&#8211;interface</i></p>
<dd> The name of the interface to lock.</p>
<dt><i>&#8211;run</i></p>
<dd> Program to run if the lock was acquired.</p>
<dt><i>&#8211;udi</i></p>
<dd> The UDI (<i>Unique Device Identifier</i>) of the device object. If this is ommitted, the global lock will be tried.</p>
<dt><i>&#8211;exclusive</i></p>
<dd> Whether the lock can be held by others.</p>
<dt><i>&#8211;exit-with-lock</i></p>
<dd> Kill the program if the acquired lock is lost. This only makes sense if you pass a specific <i>UDI</i> due to the semantics of HAL locks.</p>
<dt><i>&#8211;exit-with-dev</i></p>
<dd> Kill the program if the device is removed. This only makes sense if you pass a specific <i>UDI</i> due to the semantics of HAL locks.</p>
<dt><i>&#8211;help</i></p>
<dd> Print out usage.</p>
<dt><i>&#8211;version</i></p>
<dd> Print the version. </p>
</dl>
<h2>RETURN VALUE</h2>
<p> This program will attempt to grab a lock on a given interface. Unless, a specific <i>UDI </i> is given, the global lock will be tried. If the lock was succesfully acquired the program specified by the option &#8211;run will be run and upon termination this program will exit with exit code 0. If the lock wasn&#8217;t acquired or an error occured while taking the lock, this program will exit with a non-zero exit code and the given program will not be run. </p>
<h2>NOTES</h2>
<p> This program is only useful for launching software that doesn&#8217;t use HAL at all (since such software launched using <i>hal-lock </i> would be locked out itself); for example a partition table editor <i>part-foo</i> may use wrapper script like this </p>
<p> <i>hal-lock &#8211;interface org.freedesktop.Hal.Device.Storage &#8211;exclusive &#8211;run /path/to/part-foo-program</i> </p>
<h2>BUGS</h2>
<p> Please send bug reports to either the distribution or the HAL mailing list, see <i><a rel="nofollow" href="http://lists.freedesktop.org/mailman/listinfo/hal">http://lists.freedesktop.org/mailman/listinfo/hal</a></i> on how to subscribe. </p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/8-hald/">hald</a></i>(8), <i><a href="/docs/linux/man/1-lshal/">lshal</a></i>(1), <i><a href="/docs/linux/man/1-hal-get-property/">hal-get-property</a></i>(1), <i><a href="/docs/linux/man/1-hal-set-property/">hal-set-property</a></i>(1), <i><a href="/docs/linux/man/1-hal-find-by-property/">hal-find-by-property</a></i>(1), <i><a href="/docs/linux/man/1-hal-find-by-capability/">hal-find-by-capability</a></i>(1) </p>
<h2>AUTHOR</h2>
<p> Written by David Zeuthen &lt;david [at] fubar.dk&gt; with a lot of help from many others. </p>
<h2>Index</h2>
