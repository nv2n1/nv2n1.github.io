---
title: "systemd-tty-ask-password-agent(1)"
name: "systemd-tty-ask-password-agent"
section: "1"
letter: "s"
url: "/docs/linux/man/1-systemd-tty-ask-password-agent/"
description: "systemd-tty-ask-password-agent – List or process pending systemd password requests"
---

<h2 class="name">NAME</h2>
<p> systemd-tty-ask-password-agent &#8211; List or process pending systemd password requests </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>systemd-tty-ask-password-agent</code> [OPTIONS&#8230;] [VARIABLE=VALUE&#8230;]</dl>
<h2>DESCRIPTION</h2>
<p> <code>systemd-tty-ask-password-agent</code></p>
<dd>is a password agent that handles password requests of the system, for example for hard disk encryption passwords or SSL certificate passwords that need to be queried at boot-time or during runtime. </p>
<p> <code>systemd-tty-ask-password-agent</code> implements the m[blue]<code>Password Agents Specification</code>m[]<font SIZE="-2">[1]</font>, and is one of many possible response agents which answer to queries formulated with <code><a href="/docs/linux/man/1-systemd-ask-password/">systemd-ask-password</a></code>(1).</p>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>&#8211;list</code></p>
<dl>
<dt>
<dd> Lists all currently pending system password requests.</dl>
<p> <code>&#8211;query</code></p>
<dl>
<dt>
<dd> Process all currently pending system password requests by querying the user on the calling TTY.</dl>
<p> <code>&#8211;watch</code></p>
<dl>
<dt>
<dd> Continuously process password requests.</dl>
<p> <code>&#8211;wall</code></p>
<dl>
<dt>
<dd> Forward password requests to <code><a href="/docs/linux/man/1-wall/">wall</a></code>(1) instead of querying the user on the calling TTY.</dl>
<p> <code>&#8211;plymouth</code></p>
<dl>
<dt>
<dd> Ask question with <code><a href="/docs/linux/man/8-plymouth/">plymouth</a></code>(8) instead of querying the user on the calling TTY.</dl>
<p> <code>&#8211;console</code>[=<i>DEVICE</i>]</p>
<dl>
<dt>
<dd> Ask question on TTY <i>DEVICE</i> instead of querying the user on the calling TTY. If <i>DEVICE</i> is not specified, /dev/console will be used.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Print a short help text and exit.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print a short version string and exit.</dl>
<h2>EXIT STATUS</h2>
<p> On success, 0 is returned, a non-zero failure code otherwise.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1), <code><a href="/docs/linux/man/8-systemd-ask-password-console-service/">systemd-ask-password-console.service</a></code>(8), <code><a href="/docs/linux/man/1-wall/">wall</a></code>(1), <code><a href="/docs/linux/man/8-plymouth/">plymouth</a></code>(8)</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> Password Agents Specification</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://systemd.io/PASSWORD_AGENTS/">https://systemd.io/PASSWORD_AGENTS/</a></dl>
</dl>
<h2>Index</h2>
