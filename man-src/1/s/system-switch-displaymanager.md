---
title: "system-switch-displaymanager(1)"
name: "system-switch-displaymanager"
section: "1"
letter: "s"
url: "/docs/linux/man/1-system-switch-displaymanager/"
description: "system-switch-displaymanager – graphical and text mode interface for choosing graphical display manager"
---

<h2 class="name">NAME</h2>
<p> system-switch-displaymanager &#8211; graphical and text mode interface for choosing graphical display manager </p>
<h2>SYNOPSIS</h2>
<p> <code>system-switch-displaymanager</code> [display manager name]</p>
<h2>DESCRIPTION</h2>
<p> <code>system-switch-displaymanager</code> provides a simple method of choosing between the various display manager available under Fedora, including GDM, KDM, XDM and WDM. If X Windows is running, switchdesk will bring up a dialog box which allows the user to choose between the available display manager installed on the system. This dialog follows the appearance of the user&#8217;s current desktop as closely as possible. If a display manager name (GDM, KDM, XDM, WDM) is supplied as an argument, or X is not running, system-switch-displaymanager can be used from the command line. </p>
<h2>RETURN CODES</h2>
<p> <code>system-switch-displaymanager</code> returns 0 on success, 1 on error. </p>
<h2>AUTHOR</h2>
<pre>
Than Ngo &lt;than [at] redhat.com&gt;
</pre>
<h2>Index</h2>
