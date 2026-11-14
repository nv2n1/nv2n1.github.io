---
title: "gnome-session-selector(1)"
name: "gnome-session-selector"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gnome-session-selector/"
description: "gnome-session-selector – Selects a session to use with gnome-session"
---

<h2 class="name">NAME</h2>
<p> gnome-session-selector &#8211; Selects a session to use with gnome-session </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>gnome-session-selector</code> [session]</dl>
<h2>DESCRIPTION</h2>
<p> <code>gnome-session-selector</code></p>
<dd>can be used from a xsession desktop file to select a session before gnome-session is run. gnome-session reads and stores its session in the <code>$XDG_DATA_HOME</code>/gnome-session/saved-session directory. <code>gnome-session-selector</code> works by replacing the saved-session directory by a symlink to another directory. Since the session name is used as the directory name, it may not contain &#8216;/&#8217; characters or begin with a &#8216;.&#8217;. </p>
<p> When a session name is specified, <code>gnome-session-selector</code> will create a symlink to select this session. </p>
<p> When started without arguments, <code>gnome-session-selector</code> will present a dialog that allows to choose one of the existing sessions or create a new one.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gnome-session/">gnome-session</a></code>(1) </p>
<h2>Index</h2>
