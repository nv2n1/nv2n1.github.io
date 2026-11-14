---
title: "gnome-session-save(1)"
name: "gnome-session-save"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gnome-session-save/"
description: "gnome-session-save – Saves or ends the current GNOME session"
---

<h2>NAME</h2>
<p> gnome-session-save &#8211; Saves or ends the current GNOME session</p>
<h2>SYNOPSIS</h2>
<p> <code>gnome-session-save [&#8211;logout] [&#8211;force-logout] [&#8211;logout-dialog] [&#8211;shutdown-dialog] [&#8211;gui] [&#8211;kill [&#8211;silent]]</code></p>
<h2>DESCRIPTION</h2>
<p> <i>gnome-session-save</i> can be used from a GNOME session to save a snapshot of the currently running applications. This session will be later restored at your next GNOME session. </p>
<p> The <code>&#8211;gui</code> option will report errors in dialog boxes instead of printing to stderr. </p>
<p> If called with the <code>&#8211;logout</code> option, the current GNOME session will be ended, unless logging out has been inhibited by an application. The <code>&#8211;force-logout</code> option can be used to end the session regardless of the inhibition state. </p>
<p> When the <code>&#8211;logout-dialog</code> option is given, the standard dialog displaying logout options is displayed. When <code>&#8211;shutdown-dialog</code> option is given, the standard dialog displaying shutdown options is displayed. </p>
<p> The <code>&#8211;kill</code> and <code>&#8211;silent</code> options are deprecated. The <code>&#8211;kill</code> option is equivalent to the <code>&#8211;logout-dialog</code> option. If <code>&#8211;silent</code> is used with <code>&#8211;kill</code>, then it will behave as if <code>&#8211;logout</code> was used. </p>
<p> The session is not saved when <i>gnome-session-save</i> is called with any of the options ending the session. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gnome-session/">gnome-session</a>(1)</code></p>
<h2>BUGS</h2>
<p> If you find bugs in the <i>gnome-session-save</i> program, please report these on <a rel="nofollow" href="http://bugzilla.gnome.org.">http://bugzilla.gnome.org.</a> </p>
<h2>Index</h2>
