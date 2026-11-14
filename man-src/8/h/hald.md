---
title: "hald(8)"
name: "hald"
section: "8"
letter: "h"
url: "/docs/linux/man/8-hald/"
description: "hald – HAL daemon"
---

<p>hald &#8211; HAL daemon</p>
<h2>Synopsis</h2>
<p><code>hald</code> [options] </p>
<h2>Description</h2>
<p><i>hald</i> is a daemon that maintains a database of the devices connected to the system system in real-time. The daemon connects to the <i>D-Bus</i> system message bus to provide an API that applications can use to discover, monitor and invoke operations on devices. For more information about both the big picture and specific API details, refer to the <i>HAL spec</i> which can be found in <i>/usr/share/doc/hal-0.5.13/spec/hal-spec.html</i> depending on the distribution. </p>
<h2>Options</h2>
<p>The following options are supported:</p>
<dl>
<dt><i>&#8211;daemon=yes|no</i></p>
<dd>Specify whether to run in the foreground or the background.</p>
<dt><i>&#8211;verbose=yes|no</i></p>
<dd>Enable verbose debug output.</p>
<dt><i>&#8211;use-syslog</i></p>
<dd>Enable logging of debug output to the syslog instead of stderr. Use this option only together with &#8211;verbose.</p>
<dt><i>&#8211;help</i></p>
<dd>Print out usage.</p>
<dt><i>&#8211;version</i></p>
<dd>Print the version of the daemon and exit. </p>
</dl>
<h2>Bugs And Debugging</h2>
<p>Please send bug reports to either the distribution or the HAL mailing list, see <i><a rel="nofollow" href="http://lists.freedesktop.org/mailman/listinfo/hal">http://lists.freedesktop.org/mailman/listinfo/hal</a></i> on how to subscribe. </p>
<p> First, to obtain useful debug traces you will need to have <code>debuginfo</code> packages installed. On a Fedora system this is in the <code>hal-debuginfo </code> package and can be installed via the <i>yum</i> update program. </p>
<p> Second, shut down the existing <code>hald</code> daemon instance; on a Fedora system this is achieved by </p>
<p> <i>/etc/init.d/haldaemon stop</i> </p>
<p> After having shut down the daemon, you might want to run </p>
<p> <i>pkill hald</i> </p>
<p> to ensure that all the helper processe of <code>hald</code> are killed too. To start the HAL daemon, use </p>
<p> <i>/usr/sbin/hald &#8211;daemon=no &#8211;verbose=yes</i> </p>
<p> If the daemon crashes, you can start it under a debugger via </p>
<p> <i>gdb /usr/sbin/hald</i> </p>
<p> and then typing </p>
<p> <i>run &#8211;daemon=no &#8211;verbose=yes</i> </p>
<p> at the <code>(gdb)</code> prompt. To capture a back trace, use the <code>bt</code> command and attach this to the bug report. </p>
<p> Please also attach the output of <i><a href="/docs/linux/man/1-lshal/">lshal</a></i>(1) in the bug report if possible (it&#8217;s not possible if the <code>hald</code> daemon crashed). If the nature of the bug has to do with hotplugging, attach two outputs of <i><a href="/docs/linux/man/1-lshal/">lshal</a></i>(1) &#8211; one before the device hotplug event and one after.</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/7-udev/">udev</a></i>(7), <i><a href="/docs/linux/man/1-dbus-daemon/">dbus-daemon</a></i>(1), <i><a href="/docs/linux/man/1-lshal/">lshal</a></i>(1), <i><a href="/docs/linux/man/1-hal-set-property/">hal-set-property</a></i>(1), <i><a href="/docs/linux/man/1-hal-get-property/">hal-get-property</a></i>(1), <i><a href="/docs/linux/man/1-hal-find-by-property/">hal-find-by-property</a></i>(1), <i><a href="/docs/linux/man/1-hal-find-by-capability/">hal-find-by-capability</a></i>(1), <i><a href="/docs/linux/man/1-hal-is-caller-locked-out/">hal-is-caller-locked-out</a></i>(1) </p>
<h2>Author</h2>
<p>Written by David Zeuthen &lt;david [at] fubar.dk&gt; with a lot of help from many others.</p>
