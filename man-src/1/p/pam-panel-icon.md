---
title: "pam-panel-icon(1)"
name: "pam-panel-icon"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pam-panel-icon/"
description: "pam-panel-icon – A notification area indicator of pam_timestamp status"
---

<h2>NAME</h2>
<p> pam-panel-icon &#8211; A notification area indicator of pam_timestamp status</p>
<h2>SYNOPSIS</h2>
<p> <code>pam-panel-icon</code></p>
<h2>DESCRIPTION</h2>
<p> <code>pam-panel-icon</code> should be automatically started when starting an X11 desktop environment. For example, in GNOME <code>gnome-session</code> should be configured to start <code>pam-panel-icon</code>. In a properly configured system it should never be necessary to start <code>pam-panel-icon</code> manually. </p>
<p> <code>pam-panel-icon</code> uses <code><a href="/docs/linux/man/8-pam_timestamp_check/">pam_timestamp_check</a></code>(8) to watch the <code>pam_timestamp</code> timestamp status. If the <code>pam_timestamp</code> authorization is active, allowing an unprivileted user to temporarily authenticate as the <code>root</code> user without providing a password, an icon in the notification area of the panel is displayed. The icon allows dropping the authorization immediately. </p>
<h2>EXIT STATUS</h2>
<p> Ordinarily, <code>pam-panel-icon</code> keeps running until the X11 desktop session ends, and then returns 0. <code>pam-panel-icon</code> only returns with non-zero status on unexpected error. </p>
<h2>FILES</h2>
<dl>
<dt><code>/sbin/pam_timestamp_check</code></p>
<dd> A hard-coded location of the <code>pam_timestamp_check</code> executable. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-pam_timestamp/">pam_timestamp</a></code>(8), <code><a href="/docs/linux/man/8-pam_timestamp_check/">pam_timestamp_check</a></code>(8) </p>
<h2>Index</h2>
