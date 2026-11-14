---
title: "systemd-logind(5)"
name: "systemd-logind"
section: "5"
letter: "s"
url: "/docs/linux/man/5-systemd-logind/"
description: "systemd-logind.conf – Login manager configuration file"
---

<p>systemd-logind.conf &#8211; Login manager configuration file</p>
<h2>Synopsis</h2>
<p>/etc/systemd/systemd-logind.conf</p>
<h2>Description</h2>
<p>This files configures various parameters of the systemd login manager <code><a href="/docs/linux/man/8-systemd-logind-service/">systemd-logind.service</a></code>(8).</p>
<h2>Options</h2>
<p>All options are configured in the [Login] section: </p>
<p> <i>NAutoVTs=</i></p>
<dl>
<dd>Takes a positive integer. How many virtual terminals to allocate by default and when switched to autospawn autovt services on (if they are otherwise unused). These services are instantiated from a template of autovt [at] .service with the virtual terminal TTY name, e.g. autovt [at] tty4.service. By default autovt [at] .service is linked to getty [at] .service, i.e. login prompts are started dynamically as the user switches to unused virtual terminals, and this parameter hence controls how many gettys are available on the virtual terminals. Defaults to 6. When set to 0, automatic spawning of autovt services is disabled.</dl>
<p> <i>KillUserProcesses=</i></p>
<dl>
<dd>Takes a boolean argument. Configures whether the processes of a user should be killed when she or he completely logs out (i.e. after her/his last session ended). Defaults to no.</dl>
<p> <i>KillOnlyUsers=</i>, <i>KillExcludeUsers=</i></p>
<dl>
<dd>These settings take space separated lists of user names that influence the effect of <i>KillUserProcesses=</i>. If not empty only processes of users listed in <i>KillOnlyUsers</i> will be killed when they log out entirely. Processes of users listed in <i>KillExcludeUsers=</i> are excluded from being killed. <i>KillExcludeUsers=</i> defaults to root and takes precedence over <i>KillOnlyUsers=</i> which defaults to the empty list.</dl>
<p> <i>Controllers=</i>, <i>ResetControllers=</i></p>
<dl>
<dd>These settings control the default control group hierarchies users logging are added to. When logging in users will get private control groups in all hierarchies listed in <i>Controllers=</i> and be reset to the root control group in all hierarchies listed in <i>ResetControllers=</i>. <i>Controllers=</i> defaults to the empty list, <i>ResetControllers=</i> defaults to cpu.</dl>
<p> <i>InhibitDelayMaxSec=</i></p>
<dl>
<dd>Specifies the maximum time a system shutdown or sleep request is delayed due to an inhibitor lock of type delay being taken before it is ignored and the operation executed anyway. Defaults to 5s.</dl>
<p> Note that setting <i>KillUserProcesses=1</i> will break tools like <code><a href="/docs/linux/man/1-screen/">screen</a></code>(1). </p>
<p> Note that <i>KillUserProcesses=1</i> is a weaker version of <i>kill-session-processes=1</i> which may be configured per-service for <code><a href="/docs/linux/man/8-pam_systemd/">pam_systemd</a></code>(8). The latter kills processes of a session as soon as it ends, the former kills processes as soon as the last session of the user ends.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/8-systemd-logind-service/">systemd-logind.service</a></code>(8), <code><a href="/docs/linux/man/1-loginctl/">loginctl</a></code>(1), <code><a href="/docs/linux/man/5-systemd-conf/">systemd.conf</a></code>(5)</p>
<h2>Author</h2>
<p><code>Lennart Poettering</code> &lt;lennart [at] poettering.net&gt;</p>
<dl>
<dd>Developer</dl>
