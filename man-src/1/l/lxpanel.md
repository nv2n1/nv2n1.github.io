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
<dt> <code>lxpanel</code></dl>
<h2>DESCRIPTION</h2>
<dd>This manual page documents briefly the <code>lxpanel</code> command. </p>
<p> <code>lxpanel</code> is a program that provides a panel for the desktop, usually for LXDE. It is a lightweight GTK+ 2.x based desktop panel. </p>
<p> <code>Features</code> </p>
<dl>
<dt>
<dd> * User-friendly application menu automatically generated from FC.desktopF[] files on the system.</dl>
<dl>
<dt>
<dd> * Launcher bar (small icons clicked to launch apps)</dl>
<dl>
<dt>
<dd> * Task bar supporting ICCCM/EWMH `urgency&#8217; hint (Pidgin IM windows can flash on new incoming messages)</dl>
<dl>
<dt>
<dd> * Notification area (system tray)</dl>
<dl>
<dt>
<dd> * Digital clock</dl>
<dl>
<dt>
<dd> * Run dialog (type command to run, without opening a terminal )</dl>
<dl>
<dt>
<dd> * Net status icon plug-in (optional)</dl>
<dl>
<dt>
<dd> * Volume control plug-in (optional)</dl>
<dl>
<dt>
<dd> * lxpanelctl, an external controller lets you control lxpanel in other programs. For example, &quot;lxpanelctl run&quot; will show the Run dialog in lxpanel, and &quot;lxpanelctl menu&quot; will show the application menu. This is useful in key bindings provided by window managers.</dl>
<h2>OPTIONS</h2>
<p> This program follows the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). A summary of options is included below. </p>
<p> <code>-h</code> <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Print help on the options.</dl>
<p> <code>-v</code> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print the program version.</dl>
<p> <code>&#8211;log </code><i>level</i></p>
<dl>
<dt>
<dd> Set the logging level in the range 0 (silent) through 5 (verbose).</dl>
<p> <code>-p </code><i>NAME</i>, <code>&#8211;profile </code><i>NAME</i></p>
<dl>
<dt>
<dd> Set the profile to be loaded.</dl>
<h2>FILES</h2>
<p> FC~/.config/lxpanel/<i>PROFILE</i>F[]</p>
<dl>
<dt>
<dd> config file, can be edited by preference dialog.</dl>
<h2>SEE ALSO</h2>
<p> lxsession (1), lxpanelctl (1).</p>
<h2>AUTHOR</h2>
<p> This manual page was written by paulliu FCgrandpaul [at] gmail.comF[] for the Debian system (but may be used by others). Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 any later version published by the Free Software Foundation. </p>
<p> On Debian systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL.</p>
<h2>Author</h2>
<p> <code>Ying-Chun Liu</code></p>
<dl>
<dt>
<dd> Author.</dl>
<h2>Copyright</h2>
<p> Copyright &#169; 2008 paulliu </p>
<h2>Index</h2>
