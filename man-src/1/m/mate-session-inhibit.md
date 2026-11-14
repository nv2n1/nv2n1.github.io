---
title: "mate-session-inhibit(1)"
name: "mate-session-inhibit"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mate-session-inhibit/"
description: "mate-session-inhibit – inhibit mate-session functionality"
---

<h2 class="name">NAME</h2>
<p> mate-session-inhibit &#8211; inhibit mate-session functionality </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>mate-session-inhibit</code> [OPTION&#8230;] {COMMAND}</dl>
<h2>DESCRIPTION</h2>
<p> <code>mate-session-inhibit</code></p>
<dd>can inhibit certain mate-session functionality while executing the given COMMAND. To achieve this, it calls the Inhibit() method of the mate-session D-Bus API and creates an inhibitor. The inhibitor is automatically removed when mate-session-inhibit exits. </p>
<p> A typical use case is to prevent the session from going idle (and thus locking the screen) while a movie player is running.</p>
<h2>OPTIONS</h2>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> print help and exit</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> print version information and exit</dl>
<p> <code>&#8211;app-id</code> ID</p>
<dl>
<dt>
<dd> The application id to use when calling the mate-session Inhibit() method. If this option is not specified, &quot;unknown&quot; is used.</dl>
<p> <code>&#8211;reason</code> REASON</p>
<dl>
<dt>
<dd> A human-readable reason to pass along when calling the mate-session Inhibit() method. If this option is not specified, &quot;not specified&quot; is used.</dl>
<p> <code>&#8211;inhibit</code> ARG</p>
<dl>
<dt>
<dd> ARG specifies the things to inhibit, as a colon-separated list. The possible values are logout, switch-user, suspend, idle, automount. If this option is used more than once, the values are combined. If this option is not specified, &quot;idle&quot; is assumed.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-systemd-inhibit/">systemd-inhibit</a></code>(1) </p>
<h2>Index</h2>
