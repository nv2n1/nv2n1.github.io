---

title: "devkit-power(1)"
name: "devkit-power"
section: "1"
letter: "d"
url: "/docs/linux/man/1-devkit-power/"
description: "devkit-power – DeviceKit-power command line tool"
---

<dl>
<dt> <code>devkit-power</code> [<code>&#8211;enumerate</code>] [<code>&#8211;monitor</code>] [<code>&#8211;monitor-detail</code>] [<code>&#8211;help</code>]</dt></dl>
<p> <i>devkit-power</i></p>
<dd>is a simple command line client for the <code><a href="/docs/linux/man/7-devicekit-power/">DeviceKit-power</a></code>(7) daemon. TODO: not fully documented.</dd>
<h2>OPTIONS</h2>
<p> <code>&#8211;monitor</code></p>
<dl>
<dt>
</dt><dd> Connect to the DeviceKit-power daemon and print a line every time a power source is added, removed or changed.</dd></dl>
<p> <code>&#8211;monitor-detail</code></p>
<dl>
<dt>
</dt><dd> Like <code>&#8211;monitor</code> but prints the full details of the power source whenever an event happens.</dd></dl>
<p> <code>&#8211;help</code></p>
<dl>
<dt>
</dt><dd> Show help options.</dd></dl>
<h2>AUTHOR</h2>
<p> Written by David Zeuthen davidz [at] redhat.com with a lot of help from many others.</p>
<h2>BUGS</h2>
<p> Please send bug reports to either the distribution or the DeviceKit mailing list, see m[blue]<code><a rel="nofollow" href="http://lists.freedesktop.org/mailman/listinfo/devkit-devel">http://lists.freedesktop.org/mailman/listinfo/devkit-devel</a></code>m[] on how to subscribe.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-devkit-power-daemon/">devkit-power-daemon</a></code>(8), <code><a href="/docs/linux/man/7-devicekit-power/">DeviceKit-power</a></code>(7), </p>
