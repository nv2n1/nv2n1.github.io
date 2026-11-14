---
title: "os_type(3)"
name: "os_type"
section: "3"
letter: "o"
url: "/docs/linux/man/3-os_type/"
description: "os_type – Stores the detected type of the OS. Allegro game programming library."
---

<p>os_type &#8211; Stores the detected type of the OS. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;
</code></pre>
<p> <code>extern int os_type;</code></p>
<h2>Description</h2>
<p>Set by allegro_init() to one of the values: </p>
<pre> OSTYPE_UNKNOWN - unknown, or regular MSDOS
 OSTYPE_WIN3 - Windows 3.1 or earlier
 OSTYPE_WIN95 - Windows 95
 OSTYPE_WIN98 - Windows 98
 OSTYPE_WINME - Windows ME
 OSTYPE_WINNT - Windows NT
 OSTYPE_WIN2000 - Windows 2000
 OSTYPE_WINXP - Windows XP
 OSTYPE_WIN2003 - Windows 2003
 OSTYPE_WINVISTA - Windows Vista
 OSTYPE_OS2 - OS/2
 OSTYPE_WARP - OS/2 Warp 3
 OSTYPE_DOSEMU - Linux DOSEMU
 OSTYPE_OPENDOS - Caldera OpenDOS
 OSTYPE_LINUX - Linux
 OSTYPE_SUNOS - SunOS/Solaris
 OSTYPE_FREEBSD - FreeBSD
 OSTYPE_NETBSD - NetBSD
 OSTYPE_IRIX - IRIX
 OSTYPE_DARWIN - Darwin
 OSTYPE_QNX - QNX
 OSTYPE_UNIX - Unknown Unix variant
 OSTYPE_BEOS - BeOS
 OSTYPE_MACOS - MacOS
 OSTYPE_MACOSX - MacOS X</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-allegro_init/">allegro_init</a></code>(3), <code><a href="/docs/linux/man/3-os_version/">os_version</a></code>(3), <code><a href="/docs/linux/man/3-os_multitasking/">os_multitasking</a></code>(3) </p>
