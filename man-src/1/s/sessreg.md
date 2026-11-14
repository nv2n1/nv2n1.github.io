---
title: "sessreg(1)"
name: "sessreg"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sessreg/"
description: "sessreg – manage utmpx/wtmpx entries for non-init clients"
---

<h2 class="name">NAME</h2>
<p> sessreg &#8211; manage utmpx/wtmpx entries for non-init clients </p>
<h2>SYNOPSIS</h2>
<p> <code>sessreg</code> [-w <i>wtmpx-file</i>] [-u <i>utmpx-file</i>] [-L <i>lastlog-file</i>] [-l <i>line-name</i>] [-h <i>host-name</i>] [-s <i>slot-number</i>] [-x <i>Xservers-file</i>] [-t <i>ttys-file</i>] [-V] [-a] [-d] <i>user-name</i></p>
<h2>DESCRIPTION</h2>
<p> <i>Sessreg</i> is a simple program for managing utmpx/wtmpx and lastlog entries for xdm sessions. </p>
<p> This version of <i>sessreg</i> is built using the modern POSIX <code><a href="//www.systutorials.com/docs/linux/man/3c-pututxline/">pututxline</a></code>(3c) interfaces, which no longer require the slot-number, ttys-file, or Xservers-file mappings. For compatibility with older versions and other operating systems, the <code>-s</code>, <code>-t</code>, and <code>-x</code> flags are accepted, but ignored.</p>
<h2>USAGE</h2>
<p> In Xstartup, place a call like: </p>
<pre>
       sessreg -a -l $DISPLAY -x /etc/X11/xdm/Xservers $USER
</pre>
<p> and in Xreset: </p>
<pre>
       sessreg -d -l $DISPLAY -x /etc/X11/xdm/Xservers $USER
</pre>
<h2>OPTIONS</h2>
<dl>
<dt><code>-w</code> <i>wtmpx-file</i></p>
<dd> This specifies an alternate wtmpx file, instead of <code>/var/log/wtmp</code>. The special name &quot;none&quot; disables writing records to the wtmpx file.</p>
<dt><code>-u</code> <i>utmpx-file</i></p>
<dd> This specifies an alternate utmpx file, instead of <code>/var/run/utmp</code>. The special name &quot;none&quot; disables writing records to the utmpx file.</p>
<dt><code>-L</code> <i>lastlog-file</i></p>
<dd> This specifies an alternate lastlog file, instead of <code>/var/log/lastlog</code>, if the platform supports lastlog files. The special name &quot;none&quot; disables writing records to the lastlog file.</p>
<dt><code>-l</code> <i>line-name</i></p>
<dd> This describes the &quot;line&quot; name of the entry. For terminal sessions, this is the final pathname segment of the terminal device filename (e.g. ttyd0). For X sessions, it should probably be the local display name given to the users session (e.g. :0). If none is specified, the terminal name will be determined with <a href="/docs/linux/man/3-ttyname/">ttyname</a>(3) and stripped of leading components.</p>
<dt><code>-h</code> <i>host-name</i></p>
<dd> This is set to indicate that the session was initiated from a remote host. In typical xdm usage, this options is not used.</p>
<dt><code>-s</code> <i>slot-number</i></p>
<dd> This option is accepted for compatibility, but does nothing in this version of <i>sessreg</i>.</p>
<dt><code>-x</code> <i>Xservers-file</i></p>
<dd> This option is accepted for compatibility, but does nothing in this version of <i>sessreg</i>.</p>
<dt><code>-t</code> <i>ttys-file</i></p>
<dd> This option is accepted for compatibility, but does nothing in this version of <i>sessreg</i>.</p>
<dt><code>-V</code></p>
<dd> This option causes the command to print its version and exit.</p>
<dt><code>-a</code></p>
<dd> This session should be added to utmpx/wtmpx.</p>
<dt><code>-d</code></p>
<dd> This session should be deleted from utmpx/wtmpx. One of -a/-d must be specified.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-xdm/">xdm</a></code>(1), <code><a href="/docs/linux/man/5-utmpx/">utmpx</a></code>(5), <code><a href="/docs/linux/man/5-wtmpx/">wtmpx</a></code>(5)</p>
<h2>AUTHOR</h2>
<p> Keith Packard, MIT X Consortium </p>
<h2>Index</h2>
