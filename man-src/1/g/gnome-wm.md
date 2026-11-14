---
title: "gnome-wm(1)"
name: "gnome-wm"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gnome-wm/"
description: "gnome-wm – Launches the user selected window manager for the GNOME session"
---

<h2>NAME</h2>
<p> gnome-wm &#8211; Launches the user selected window manager for the GNOME session</p>
<h2>SYNOPSIS</h2>
<p> <code>gnome-wm [&#8211;default-wm windowmanager] [&#8211;sm-client-id id]</code></p>
<h2>DESCRIPTION</h2>
<p> The <i>gnome-wm</i> script invokes the user selected window manager. If the user has not chosen a window manager it will launch a GNOME compliant window manager. </p>
<p> The user can overwrite the selection of a window manager by setting the <code>WINDOW_MANAGER</code> environment variable. If a <code>&#8211;default-wm</code> option is given the script uses that window manager in case <code>WINDOW_MANAGER</code> is not set. </p>
<p> The script takes the <code>&#8211;sm-client-id</code> option and translates the id to an appropriate option depending on which window manager was selected. </p>
<h2>ENVIRONMENT</h2>
<p> The <i>gnome-wm</i> program uses the value of the <code>WINDOW_MANAGER </code> environment variable to let the user override the configured window manager.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gnome-session/">gnome-session</a>(1)</code></p>
<h2>BUGS</h2>
<p> If you find bugs in the <i>gnome-wm</i> program, please report these on <a rel="nofollow" href="http://bugzilla.gnome.org.">http://bugzilla.gnome.org.</a> </p>
<h2>Index</h2>
