---
title: "user-runtime-dir-service(5)"
name: "user-runtime-dir-service"
section: "5"
letter: "u"
url: "/docs/linux/man/5-user-runtime-dir-service/"
description: "user [at] .service, user-runtime-dir [at] .service, systemd-user-runtime-dir – System units to start the user manager"
---

<p>user [at] .service, user-runtime-dir [at] .service, systemd-user-runtime-dir &#8211; System units to start the user manager</p>
<h2>Synopsis</h2>
<p>user@<i>UID</i>.service </p>
<p> user-runtime-dir@<i>UID</i>.service </p>
<p> /lib/systemd/systemd-user-runtime-dir </p>
<p> user-<i>UID</i>.slice</p>
<h2>Description</h2>
<p>The <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) system manager (PID 1) starts user manager instances as user@<i>UID</i>.service, with the user&#8217;s numerical UID used as the instance identifier. These instances use the same executable as the system manager, but running in a mode where it starts a different set of units. Each <code>systemd &#8211;user</code> instance manages a hierarchy of units specific to that user. See <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) for a discussion of units and <code><a href="/docs/linux/man/7-systemd-special/">systemd.special</a></code>(7) for a list of units that form the basis of the unit hierarchies of system and user units. </p>
<p> user@<i>UID</i>.service is accompanied by the system unit user-runtime-dir@<i>UID</i>.service, which creates the user&#8217;s runtime directory /run/user/<i>UID</i>, and then removes it when this unit is stopped. user-runtime-dir@<i>UID</i>.service executes the systemd-user-runtime-dir binary to do the actual work. </p>
<p> User processes may be started by the user [at] .service instance, in which case they will be part of that unit in the system hierarchy. They may also be started elsewhere, for example by <code><a href="/docs/linux/man/8-sshd/">sshd</a></code>(8) or a display manager like <code>gdm</code>, in which case they form a .scope unit (see <code><a href="/docs/linux/man/5-systemd-scope/">systemd.scope</a></code>(5)). Both user@<i>UID</i>.service and the scope units are collected under the user-<i>UID</i>.slice. </p>
<p> Individual user-<i>UID</i>.slice slices are collected under user.slice, see <code><a href="/docs/linux/man/7-systemd-special/">systemd.special</a></code>(7).</p>
<h2>Controlling Resources For Logged-In Users</h2>
<p>Options that control resources available to logged-in users can be configured at a few different levels. As described in the previous section, user.slice contains processes of all users, so any resource limits on that slice apply to all users together. The usual way to configure them would be through drop-ins, e.g. /etc/systemd/system/user.slice.d/resources.conf. </p>
<p> The processes of a single user are collected under user-<i>UID</i>.slice. Resource limits for that user can be configured through drop-ins for that unit, e.g. /etc/systemd/system/user-1000.slice.d/resources.conf. If the limits should apply to all users instead, they may be configured through drop-ins for the truncated unit name, user-.slice. For example, configuration in /etc/systemd/system/user-.slice.d/resources.conf is included in all user-<i>UID</i>.slice units, see <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5) for a discussion of the drop-in mechanism. </p>
<p> When a user logs in and a .scope unit is created for the session (see previous section), the creation of the scope may be managed through <code><a href="/docs/linux/man/8-pam_systemd/">pam_systemd</a></code>(8). This PAM module communicates with <code><a href="/docs/linux/man/8-systemd-logind/">systemd-logind</a></code>(8) to create the session scope and provide access to hardware resources. Resource limits for the scope may be configured through the PAM module configuration, see <code><a href="/docs/linux/man/8-pam_systemd/">pam_systemd</a></code>(8). Configuring them through the normal unit configuration is also possible, but since the name of the slice unit is generally unpredictable, this is less useful. </p>
<p> In general any resources that apply to units may be set for user@<i>UID</i>.service and the slice units discussed above, see <code><a href="/docs/linux/man/5-systemd-resource-control/">systemd.resource-control</a></code>(5) for an overview.</p>
<h2>Examples</h2>
<p><code>Example 1. Hierarchy of control groups with two logged in users</code> </p>
<dl>
<dd>
<pre>$ systemd-cgls
Control group /:
-.slice
├─user.slice
│ ├─user-1000.slice
│ │ ├─user [at] 1000.service
│ │ │ ├─pulseaudio.service
│ │ │ │ └─2386 /usr/bin/pulseaudio --daemonize=no
│ │ │ └─gnome-terminal-server.service
│ │ │ └─init.scope
│ │ │ ├─ 4127 /libexec/gnome-terminal-server
│ │ │ └─ 4198 zsh
│ │ ...
│ │ └─session-4.scope
│ │ ├─ 1264 gdm-session-worker [pam/gdm-password]
│ │ ├─ 2339 /usr/bin/gnome-shell
│ │ ...
│ │ ├─session-19.scope
│ │ ├─6497 sshd: zbyszek [priv]
│ │ ├─6502 sshd: zbyszek@pts/6
│ │ ├─6509 -zsh
│ │ └─6602 systemd-cgls --no-pager
│ ...
│ └─user-1001.slice
│ ├─session-20.scope
│ │ ├─6675 sshd: guest [priv]
│ │ ├─6708 sshd: guest@pts/6
│ │ └─6717 -bash
│ └─user [at] 1001.service
│ ├─init.scope
│ │ ├─6680 /lib/systemd/systemd --user
│ │ └─6688 (sd-pam)
│ └─sleep.service
│ └─6706 /usr/bin/sleep 30
...</pre>
</dl>
<p> User with UID 1000 is logged in using <code>gdm</code> (session-4.scope) and <code><a href="/docs/linux/man/1-ssh/">ssh</a></code>(1) (session-19.scope), and also has a user manager instance running (user [at] 1000.service). User with UID 1001 is logged in using <code>ssh</code> (session-20.scope) and also has a user manager instance running (user [at] 1001.service). Those are all (leaf) system units, and form part of the slice hierarchy, with user-1000.slice and user-1001.slice below user.slice. User units are visible below the user [at] .service instances (pulseaudio.service, gnome-terminal-server.service, init.scope, sleep.service). </p>
<p> <code>Example 2. Default user resource limits</code> </p>
<dl>
<dd>
<pre>$ systemctl cat user-1000.slice
# /lib/systemd/system/user-.slice.d/10-defaults.conf
# ...
[Unit]
Description=User Slice of UID %j
After=systemd-user-sessions.service
[Slice]
TasksMax=33%</pre>
</dl>
<p> The user-<i>UID</i>.slice units by default don&#8217;t have a unit file. The resource limits are set through a drop-in, which can be easily replaced or extended following standard drop-in mechanisms discussed in the first section.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5), <code><a href="/docs/linux/man/5-systemd-slice/">systemd.slice</a></code>(5), <code><a href="/docs/linux/man/5-systemd-resource-control/">systemd.resource-control</a></code>(5), <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5), <code><a href="/docs/linux/man/7-systemd-special/">systemd.special</a></code>(7), <code><a href="/docs/linux/man/8-pam/">pam</a></code>(8) </p>
