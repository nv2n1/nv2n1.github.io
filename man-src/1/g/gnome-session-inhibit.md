---
title: "gnome-session-inhibit(1)"
name: "gnome-session-inhibit"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gnome-session-inhibit/"
description: "gnome-session-inhibit – inhibit gnome-session functionality"
---

<h2>SYNOPSIS</h2>
<dl>
<dt> <code>gnome-session-inhibit</code> [OPTION&#8230;] [COMMAND]</dt></dl>
<h2>DESCRIPTION</h2>
<p> <code>gnome-session-inhibit</code></p>
<dd>can inhibit certain gnome-session functionality while executing the given COMMAND. To achieve this, it calls the Inhibit() method of the gnome-session D-Bus API and creates an inhibitor. The inhibitor is automatically removed when gnome-session-inhibit exits. </dd>
<p> A typical use case is to prevent the session from going idle (and thus locking the screen) while a movie player is running.</p>
<h2>OPTIONS</h2>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
</dt><dd> print help and exit</dd></dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
</dt><dd> print version information and exit</dd></dl>
<p> <code>&#8211;app-id</code> ID</p>
<dl>
<dt>
</dt><dd> The application id to use when calling the gnome-session Inhibit() method. If this option is not specified, &quot;unknown&quot; is used.</dd></dl>
<p> <code>&#8211;reason</code> REASON</p>
<dl>
<dt>
</dt><dd> A human-readable reason to pass along when calling the gnome-session Inhibit() method. If this option is not specified, &quot;not specified&quot; is used.</dd></dl>
<p> <code>&#8211;inhibit</code> ARG</p>
<dl>
<dt>
</dt><dd> ARG specifies the things to inhibit, as a colon-separated list. The possible values are logout, switch-user, suspend, idle, automount. If this option is used more than once, the values are combined. If this option is not specified, &quot;idle&quot; is assumed.</dd></dl>
<p> <code>&#8211;inhibit-only</code></p>
<dl>
<dt>
</dt><dd> Do not launch COMMAND and wait forever instead</dd></dl>
<p> <code>-l</code>, <code>&#8211;list</code></p>
<dl>
<dt>
</dt><dd> list the existing inhibitions and exit</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-systemd-inhibit/">systemd-inhibit</a></code>(1) </p>
