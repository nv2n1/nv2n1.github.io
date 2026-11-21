---
title: "lxpanel(1)"
name: "lxpanel"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lxpanel/"
description: "lxpanel – a lightweight GTK2-based panel for the LXDE desktop."
---

<p>lxpanel &#8211; a lightweight GTK2-based panel for the LXDE desktop.</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>lxpanel</code></dt></dl>
<h2>DESCRIPTION</h2>
<dd>This manual page documents briefly the <code>lxpanel</code> command. </dd>
<p> <code>lxpanel</code> is a program that provides a panel for the desktop, usually for LXDE. It is a lightweight GTK+ 2.x based desktop panel. </p>
<p> <code>Features</code> </p>
<dl>
<dt>
</dt><dd> * User-friendly application menu automatically generated from FC.desktopF[] files on the system.</dd></dl>
<dl>
<dt>
</dt><dd> * Launcher bar (small icons clicked to launch apps)</dd></dl>
<dl>
<dt>
</dt><dd> * Task bar supporting ICCCM/EWMH `urgency&#8217; hint (Pidgin IM windows can flash on new incoming messages)</dd></dl>
<dl>
<dt>
</dt><dd> * Notification area (system tray)</dd></dl>
<dl>
<dt>
</dt><dd> * Digital clock</dd></dl>
<dl>
<dt>
</dt><dd> * Run dialog (type command to run, without opening a terminal )</dd></dl>
<dl>
<dt>
</dt><dd> * Net status icon plug-in (optional)</dd></dl>
<dl>
<dt>
</dt><dd> * Volume control plug-in (optional)</dd></dl>
<dl>
<dt>
</dt><dd> * lxpanelctl, an external controller lets you control lxpanel in other programs. For example, &quot;lxpanelctl run&quot; will show the Run dialog in lxpanel, and &quot;lxpanelctl menu&quot; will show the application menu. This is useful in key bindings provided by window managers.</dd></dl>
<h2>OPTIONS</h2>
<p> This program follows the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). A summary of options is included below. </p>
<p> <code>-h</code> <code>&#8211;help</code></p>
<dl>
<dt>
</dt><dd> Print help on the options.</dd></dl>
<p> <code>-v</code> <code>&#8211;version</code></p>
<dl>
<dt>
</dt><dd> Print the program version.</dd></dl>
<p> <code>&#8211;log </code><i>level</i></p>
<dl>
<dt>
</dt><dd> Set the logging level in the range 0 (silent) through 5 (verbose).</dd></dl>
<p> <code>-p </code><i>NAME</i>, <code>&#8211;profile </code><i>NAME</i></p>
<dl>
<dt>
</dt><dd> Set the profile to be loaded.</dd></dl>
<h2>FILES</h2>
<p> FC~/.config/lxpanel/<i>PROFILE</i>F[]</p>
<dl>
<dt>
</dt><dd> config file, can be edited by preference dialog.</dd></dl>
<h2>SEE ALSO</h2>
<p> lxsession (1), lxpanelctl (1).</p>
<h2>AUTHOR</h2>
<p> This manual page was written by paulliu FCgrandpaul [at] gmail.comF[] for the Debian system (but may be used by others). Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 any later version published by the Free Software Foundation. </p>
<p> On Debian systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL.</p>
<h2>Author</h2>
<p> <code>Ying-Chun Liu</code></p>
<dl>
<dt>
</dt><dd> Author.</dd></dl>
<h2>Copyright</h2>
<p> Copyright &#169; 2008 paulliu </p>
