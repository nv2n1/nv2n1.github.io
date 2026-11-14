---
title: "systemd-logind(8)"
name: "systemd-logind"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-logind/"
description: "systemd-logind.service, systemd-logind – Login manager"
---

<p>systemd-logind.service, systemd-logind &#8211; Login manager</p>
<h2>Synopsis</h2>
<p>systemd-logind.service </p>
<p> /lib/systemd/systemd-logind</p>
<h2>Description</h2>
<p><code>systemd-logind</code> is a system service that manages user logins. It is responsible for: </p>
<dl>
<dd>&bull; Keeping track of users and sessions, their processes and their idle state. This is implemented by allocating a systemd slice unit for each user below user.slice, and a scope unit below it for each concurrent session of a user. Also, a per-user service manager is started as system service instance of user [at] .service for each logged in user.</dl>
<dl>
<dd>&bull; Generating and managing session IDs. If auditing is available and an audit session ID is already set for a session, then this ID is reused as the session ID. Otherwise, an independent session counter is used.</dl>
<dl>
<dd>&bull; Providing m[blue]<code>polkit</code>m[]<font SIZE="-2">[1]</font>-based access for users for operations such as system shutdown or sleep</dl>
<dl>
<dd>&bull; Implementing a shutdown/sleep inhibition logic for applications</dl>
<dl>
<dd>&bull; Handling of power/sleep hardware keys</dl>
<dl>
<dd>&bull; Multi-seat management</dl>
<dl>
<dd>&bull; Session switch management</dl>
<dl>
<dd>&bull; Device access management for users</dl>
<dl>
<dd>&bull; Automatic spawning of text logins (gettys) on virtual console activation and user runtime directory management</dl>
<p> User sessions are registered with logind via the <code><a href="/docs/linux/man/8-pam_systemd/">pam_systemd</a></code>(8) PAM module. </p>
<p> See <code><a href="/docs/linux/man/5-logind-conf/">logind.conf</a></code>(5) for information about the configuration of this service. </p>
<p> See <code><a href="/docs/linux/man/3-sd-login/">sd-login</a></code>(3) for information about the basic concepts of logind such as users, sessions and seats. </p>
<p> See <code><a href="/docs/linux/man/5-org-freedesktop-login1/">org.freedesktop.login1</a></code>(5) and <code><a href="/docs/linux/man/5-org-freedesktop-logcontrol1/">org.freedesktop.LogControl1</a></code>(5) for information about the D-Bus APIs systemd-logind provides. </p>
<p> For more information on the inhibition logic see the m[blue]<code>Inhibitor Lock Developer Documentation</code>m[]<font SIZE="-2">[2]</font>. </p>
<p> If you are interested in writing a display manager that makes use of logind, please have look at m[blue]<code>Writing Display Managers</code>m[]<font SIZE="-2">[3]</font>. If you are interested in writing a desktop environment that makes use of logind, please have look at m[blue]<code>Writing Desktop Environments</code>m[]<font SIZE="-2">[4]</font>.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/8-systemd-user-sessions-service/">systemd-user-sessions.service</a></code>(8), <code><a href="/docs/linux/man/1-loginctl/">loginctl</a></code>(1), <code><a href="/docs/linux/man/5-logind-conf/">logind.conf</a></code>(5), <code><a href="/docs/linux/man/8-pam_systemd/">pam_systemd</a></code>(8), <code><a href="/docs/linux/man/3-sd-login/">sd-login</a></code>(3)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>polkit</p>
<dl>
<dd><a rel="nofollow" href="https://www.freedesktop.org/wiki/Software/polkit">https://www.freedesktop.org/wiki/Software/polkit</a></dl>
<dt> 2.</p>
<dd>Inhibitor Lock Developer Documentation</p>
<dl>
<dd><a rel="nofollow" href="https://www.freedesktop.org/wiki/Software/systemd/inhibit">https://www.freedesktop.org/wiki/Software/systemd/inhibit</a></dl>
<dt> 3.</p>
<dd>Writing Display Managers</p>
<dl>
<dd><a rel="nofollow" href="https://www.freedesktop.org/wiki/Software/systemd/writing-display-managers">https://www.freedesktop.org/wiki/Software/systemd/writing-display-managers</a></dl>
<dt> 4.</p>
<dd>Writing Desktop Environments</p>
<dl>
<dd><a rel="nofollow" href="https://www.freedesktop.org/wiki/Software/systemd/writing-desktop-environments">https://www.freedesktop.org/wiki/Software/systemd/writing-desktop-environments</a></dl>
