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
<dt> <code>xdg-user-dir</code> [NAME]</dt></dl>
<h2>DESCRIPTION</h2>
<p> <code>xdg-user-dir</code></p>
<dd>looks up the current path for one of the special XDG user dirs. </dd>
<p> This command expects the name of an XDG user dir as argument. The possible names are:</p>
<dl>
<dt>
</dt><dd> DESKTOP</dd></dl>
<dl>
<dt>
</dt><dd> DOWNLOAD</dd></dl>
<dl>
<dt>
</dt><dd> TEMPLATES</dd></dl>
<dl>
<dt>
</dt><dd> PUBLICSHARE</dd></dl>
<dl>
<dt>
</dt><dd> DOCUMENTS</dd></dl>
<dl>
<dt>
</dt><dd> MUSIC</dd></dl>
<dl>
<dt>
</dt><dd> PICTURES</dd></dl>
<dl>
<dt>
</dt><dd> VIDEOS</dd></dl>
<h2>FILES</h2>
<p> The values are looked up in the user-dirs.dir file. This file is created by the xdg-user-dirs-update utility.</p>
<h2>ENVIRONMENT</h2>
<p> The <code>XDG_CONFIG_HOME</code> environment variable determines where the user-dirs.dirs file is located.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-xdg-user-dirs-update/">xdg-user-dirs-update</a></code>(1) </p>
<h2>Index</h2>
