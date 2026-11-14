---
title: "dbus-uuidgen(1)"
name: "dbus-uuidgen"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dbus-uuidgen/"
description: "dbus-uuidgen – Utility to generate UUIDs"
---

<h2 class="name">NAME</h2>
<p> dbus-uuidgen &#8211; Utility to generate UUIDs </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>dbus-uuidgen</code> [&#8211;version] [&#8211;ensure&nbsp;[<i>=FILENAME</i>]] [&#8211;get&nbsp;[<i>=FILENAME</i>]]</p>
<dd>
</dl>
<h2>DESCRIPTION</h2>
<dd>The <code>dbus-uuidgen</code> command generates or reads a universally unique ID. </p>
<p> Note that the D-Bus UUID has no relationship to RFC 4122 and does not generate UUIDs compatible with that spec. Many systems have a separate command for that (often called &quot;uuidgen&quot;). </p>
<p> See m[blue]<code><a rel="nofollow" href="http://www.freedesktop.org/software/dbus/">http://www.freedesktop.org/software/dbus/</a></code>m[] for more information about D-Bus. </p>
<p> The primary usage of <code>dbus-uuidgen</code> is to run in the post-install script of a D-Bus package like this: </p>
<dl>
<dt>
<dd>
<pre>
  dbus-uuidgen --ensure
</pre>
</dl>
<p> This will ensure that /var/lib/dbus/machine-id exists and has the uuid in it. It won&#8217;t overwrite an existing uuid, since this id should remain fixed for a single machine until the next reboot at least. </p>
<p> The important properties of the machine UUID are that 1) it remains unchanged until the next reboot and 2) it is different for any two running instances of the OS kernel. That is, if two processes see the same UUID, they should also see the same shared memory, UNIX domain sockets, local X displays, localhost.localdomain resolution, process IDs, and so forth. </p>
<p> If you run <code>dbus-uuidgen</code> with no options it just prints a new uuid made up out of thin air. </p>
<p> If you run it with &#8211;get, it prints the machine UUID by default, or the UUID in the specified file if you specify a file. </p>
<p> If you try to change an existing machine-id on a running system, it will probably result in bad things happening. Don&#8217;t try to change this file. Also, don&#8217;t make it the same on two different systems; it needs to be different anytime there are two different kernels running. </p>
<p> The UUID should be different on two different virtual machines, because there are two different kernels.</p>
<h2>OPTIONS</h2>
<p> The following options are supported: </p>
<p> <code>&#8211;get[=FILENAME]</code></p>
<dl>
<dt>
<dd> If a filename is not given, defaults to localstatedir/lib/dbus/machine-id (localstatedir is usually /var). If this file exists and is valid, the uuid in the file is printed on stdout. Otherwise, the command exits with a nonzero status.</dl>
<p> <code>&#8211;ensure[=FILENAME]</code></p>
<dl>
<dt>
<dd> If a filename is not given, defaults to localstatedir/lib/dbus/machine-id (localstatedir is usually /var). If this file exists then it will be validated, and a failure code returned if it contains the wrong thing. If the file does not exist, it will be created with a new uuid in it. On success, prints no output.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print the version of dbus-uuidgen</dl>
<h2>AUTHOR</h2>
<p> See m[blue]<code><a rel="nofollow" href="http://www.freedesktop.org/software/dbus/doc/AUTHORS">http://www.freedesktop.org/software/dbus/doc/AUTHORS</a></code>m[]</p>
<h2>BUGS</h2>
<p> Please send bug reports to the D-Bus mailing list or bug tracker, see m[blue]<code><a rel="nofollow" href="http://www.freedesktop.org/software/dbus/">http://www.freedesktop.org/software/dbus/</a></code>m[] </p>
<h2>Index</h2>
