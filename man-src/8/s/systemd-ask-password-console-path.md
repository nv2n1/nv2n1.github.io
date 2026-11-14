---
title: "systemd-ask-password-console-path(8)"
name: "systemd-ask-password-console-path"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-ask-password-console-path/"
description: "systemd-ask-password-console.service, systemd-ask-password-console.path, systemd-ask-password-wall.service, systemd-ask-password-wall.path – Query the user for system passwords on the console and v..."
---

<p>systemd-ask-password-console.service, systemd-ask-password-console.path, systemd-ask-password-wall.service, systemd-ask-password-wall.path &#8211; Query the user for system passwords on the console and via wall</p>
<h2>Synopsis</h2>
<p>systemd-ask-password-console.service </p>
<p> systemd-ask-password-console.path </p>
<p> systemd-ask-password-wall.service </p>
<p> systemd-ask-password-wall.path</p>
<h2>Description</h2>
<p>systemd-ask-password-console.service is a system service that queries the user for system passwords (such as hard disk encryption keys and SSL certificate passphrases) on the console. It is intended to be used during boot to ensure proper handling of passwords necessary for boot. systemd-ask-password-wall.service is a system service that informs all logged in users for system passwords via <code><a href="/docs/linux/man/1-wall/">wall</a></code>(1). It is intended to be used after boot to ensure that users are properly notified. </p>
<p> See the m[blue]<code>developer documentation</code>m[]<font SIZE="-2">[1]</font> for more information about the system password logic. </p>
<p> Note that these services invoke <code><a href="/docs/linux/man/1-systemd-tty-ask-password-agent/">systemd-tty-ask-password-agent</a></code>(1) with either the <code>&#8211;watch &#8211;console</code> or <code>&#8211;watch &#8211;wall</code> command line parameters.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/1-systemd-tty-ask-password-agent/">systemd-tty-ask-password-agent</a></code>(1), <code><a href="/docs/linux/man/1-wall/">wall</a></code>(1)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>developer documentation</p>
<dl>
<dd><a rel="nofollow" href="https://systemd.io/PASSWORD_AGENTS/">https://systemd.io/PASSWORD_AGENTS/</a></dl>
