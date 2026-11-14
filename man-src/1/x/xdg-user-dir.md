---
title: "xdg-user-dir(1)"
name: "xdg-user-dir"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xdg-user-dir/"
description: "xdg-user-dir – Find an XDG user dir"
---

<h2 class="name">NAME</h2>
<p> xdg-user-dir &#8211; Find an XDG user dir </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>xdg-user-dir</code> [NAME]</dl>
<h2>DESCRIPTION</h2>
<p> <code>xdg-user-dir</code></p>
<dd>looks up the current path for one of the special XDG user dirs. </p>
<p> This command expects the name of an XDG user dir as argument. The possible names are:</p>
<dl>
<dt>
<dd> DESKTOP</dl>
<dl>
<dt>
<dd> DOWNLOAD</dl>
<dl>
<dt>
<dd> TEMPLATES</dl>
<dl>
<dt>
<dd> PUBLICSHARE</dl>
<dl>
<dt>
<dd> DOCUMENTS</dl>
<dl>
<dt>
<dd> MUSIC</dl>
<dl>
<dt>
<dd> PICTURES</dl>
<dl>
<dt>
<dd> VIDEOS</dl>
<h2>FILES</h2>
<p> The values are looked up in the user-dirs.dir file. This file is created by the xdg-user-dirs-update utility.</p>
<h2>ENVIRONMENT</h2>
<p> The <code>XDG_CONFIG_HOME</code> environment variable determines where the user-dirs.dirs file is located.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-xdg-user-dirs-update/">xdg-user-dirs-update</a></code>(1) </p>
<h2>Index</h2>
