---
title: "dbus-cleanup-sockets(1)"
name: "dbus-cleanup-sockets"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dbus-cleanup-sockets/"
description: "dbus-cleanup-sockets – clean up leftover sockets in a directory"
---

<h2 class="name">NAME</h2>
<p> dbus-cleanup-sockets &#8211; clean up leftover sockets in a directory </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>dbus-cleanup-sockets</code> [<i>DIRECTORY</i>]</p>
<dd>
</dl>
<h2>DESCRIPTION</h2>
<dd>The <code>dbus-cleanup-sockets</code> command cleans up unused D-Bus connection sockets. See m[blue]<code><a rel="nofollow" href="http://www.freedesktop.org/software/dbus/">http://www.freedesktop.org/software/dbus/</a></code>m[] for more information about the big picture. </p>
<p> If given no arguments, <code>dbus-cleanup-sockets</code> cleans up sockets in the standard default socket directory for the per-user-login-session message bus; this is usually /tmp. Optionally, you can pass a different directory on the command line. </p>
<p> On Linux, this program is essentially useless, because D-Bus defaults to using &quot;abstract sockets&quot; that exist only in memory and don&#8217;t have a corresponding file in /tmp. </p>
<p> On most other flavors of UNIX, it&#8217;s possible for the socket files to leak when programs using D-Bus exit abnormally or without closing their D-Bus connections. Thus, it might be interesting to run dbus-cleanup-sockets in a cron job to mop up any leaked sockets. Or you can just ignore the leaked sockets, they aren&#8217;t really hurting anything, other than cluttering the output of &quot;ls /tmp&quot;</p>
<h2>AUTHOR</h2>
<p> dbus-cleanup-sockets was adapted by Havoc Pennington from linc-cleanup-sockets written by Michael Meeks.</p>
<h2>BUGS</h2>
<p> Please send bug reports to the D-Bus mailing list or bug tracker, see m[blue]<code><a rel="nofollow" href="http://www.freedesktop.org/software/dbus/">http://www.freedesktop.org/software/dbus/</a></code>m[] </p>
<h2>Index</h2>
