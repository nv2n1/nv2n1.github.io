---
title: "systemd-loginctl(1)"
name: "systemd-loginctl"
section: "1"
letter: "s"
url: "/docs/linux/man/1-systemd-loginctl/"
description: "loginctl, systemd-loginctl – Control the systemd login manager"
---

<h2 class="name">NAME</h2>
<p> loginctl, systemd-loginctl &#8211; Control the systemd login manager </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>loginctl </code><code>[OPTIONS&#8230;]</code><code>{COMMAND}</code><code>[NAME&#8230;]</code></dl>
<h2>DESCRIPTION</h2>
<p> <code>loginctl</code></p>
<dd>may be used to introspect and control the state of the <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) login manager <code><a href="/docs/linux/man/8-systemd-logind-service/">systemd-logind.service</a></code>(8).</p>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>&#8211;help</code>, <code>-h</code></p>
<dl>
<dt>
<dd> Prints a short help text and exits.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Prints a short version string and exits.</dl>
<p> <code>&#8211;property=</code>, <code>-p</code></p>
<dl>
<dt>
<dd> When showing session/user/ properties, limit display to certain properties as specified as argument. If not specified all set properties are shown. The argument should be a property name, such as Sessions. If specified more than once all properties with the specified names are shown.</dl>
<p> <code>&#8211;all</code>, <code>-a</code></p>
<dl>
<dt>
<dd> When showing unit/job/manager properties, show all properties regardless whether they are set or not.</dl>
<p> <code>&#8211;no-pager</code></p>
<dl>
<dt>
<dd> Do not pipe output into a pager.</dl>
<p> <code>&#8211;no-ask-password</code></p>
<dl>
<dt>
<dd> Don&#8217;t query the user for authentication for privileged operations.</dl>
<p> <code>&#8211;kill-who=</code></p>
<dl>
<dt>
<dd> When used with <code>kill-session</code>, choose which processes to kill. Must be one of <code>leader</code>, or <code>all</code> to select whether to kill only the leader process of the session or all processes of the session. If omitted defaults to <code>all</code>.</dl>
<p> <code>&#8211;signal=</code>, <code>-s</code></p>
<dl>
<dt>
<dd> When used with <code>kill-session</code> or <code>kill-user</code>, choose which signal to send to selected processes. Must be one of the well known signal specifiers such as SIGTERM, SIGINT or SIGSTOP. If omitted defaults to <code>SIGTERM</code>.</dl>
<p> <code>-H</code>, <code>&#8211;host</code></p>
<dl>
<dt>
<dd> Execute operation remotely. Specify a hostname, or username and hostname separated by @, to connect to. This will use SSH to talk to the remote login manager instance.</dl>
<p> <code>-P</code>, <code>&#8211;privileged</code></p>
<dl>
<dt>
<dd> Acquire privileges via PolicyKit before executing the operation.</dl>
<p> The following commands are understood: </p>
<p> <code>list-sessions</code></p>
<dl>
<dt>
<dd> List current sessions.</dl>
<p> <code>session-status [ID&#8230;]</code></p>
<dl>
<dt>
<dd> Show terse runtime status information about one or more sessions. This function is intended to generate human-readable output. If you are looking for computer-parsable output, use <code>show-session</code> instead.</dl>
<p> <code>show-session [ID&#8230;]</code></p>
<dl>
<dt>
<dd> Show properties of one or more sessions or the manager itself. If no argument is specified properties of the manager will be shown. If a session ID is specified properties of the session is shown. By default, empty properties are suppressed. Use <code>&#8211;all</code> to show those too. To select specific properties to show use <code>&#8211;property=</code>. This command is intended to be used whenever computer-parsable output is required. Use <code>session-status</code> if you are looking for formatted human-readable output.</dl>
<p> <code>activate [ID&#8230;]</code></p>
<dl>
<dt>
<dd> Activate one or more sessions. This brings one or more sessions into the foreground, if another session is currently in the foreground on the respective seat.</dl>
<p> <code>lock-session [ID&#8230;]</code>, <code>unlock-session [ID&#8230;]</code></p>
<dl>
<dt>
<dd> Activates/deactivates the screen lock on one or more sessions, if the session supports it.</dl>
<p> <code>terminate-session [ID&#8230;]</code></p>
<dl>
<dt>
<dd> Terminates a session. This kills all processes of the session and deallocates all resources attached to the session.</dl>
<p> <code>kill-session [ID&#8230;]</code></p>
<dl>
<dt>
<dd> Send a signal to one or more processes of the session. Use <code>&#8211;kill-who=</code> to select which process to kill. Use <code>&#8211;signal=</code> to select the signal to send.</dl>
<p> <code>list-users</code></p>
<dl>
<dt>
<dd> List currently logged in users.</dl>
<p> <code>user-status [USER&#8230;]</code></p>
<dl>
<dt>
<dd> Show terse runtime status information about one or more logged in users. This function is intended to generate human-readable output. If you are looking for computer-parsable output, use <code>show-user</code> instead. Users may be specified by their usernames or numeric user IDs.</dl>
<p> <code>show-user [USER&#8230;]</code></p>
<dl>
<dt>
<dd> Show properties of one or more users or the manager itself. If no argument is specified properties of the manager will be shown. If a user is specified properties of the user is shown. By default, empty properties are suppressed. Use <code>&#8211;all</code> to show those too. To select specific properties to show use <code>&#8211;property=</code>. This command is intended to be used whenever computer-parsable output is required. Use <code>user-status</code> if you are looking for formatted human-readable output.</dl>
<p> <code>enable-linger [USER&#8230;]</code>, <code>disable-linger [USER&#8230;]</code></p>
<dl>
<dt>
<dd> Enable/disable user lingering for one or more users. If enabled for a specific user a user manager is spawned for him/her at boot, and kept around after logouts. This allows users who aren&#8217;t logged in to run long-running services.</dl>
<p> <code>terminate-user [USER&#8230;]</code></p>
<dl>
<dt>
<dd> Terminates all sessions of a user. This kills all processes of all sessions of the user and deallocates all runtime resources attached to the user.</dl>
<p> <code>kill-user [USER&#8230;]</code></p>
<dl>
<dt>
<dd> Send a signal to all processes of a user. Use <code>&#8211;signal=</code> to select the signal to send.</dl>
<p> <code>list-seats</code></p>
<dl>
<dt>
<dd> List currently available seats on the local system.</dl>
<p> <code>seat-status [NAME&#8230;]</code></p>
<dl>
<dt>
<dd> Show terse runtime status information about one or more seats. This function is intended to generate human-readable output. If you are looking for computer-parsable output, use <code>show-seat</code> instead.</dl>
<p> <code>show-seat [NAME&#8230;]</code></p>
<dl>
<dt>
<dd> Show properties of one or more seats or the manager itself. If no argument is specified properties of the manager will be shown. If a seat is specified properties of the seat are shown. By default, empty properties are suppressed. Use <code>&#8211;all</code> to show those too. To select specific properties to show use <code>&#8211;property=</code>. This command is intended to be used whenever computer-parsable output is required. Use <code>seat-status</code> if you are looking for formatted human-readable output.</dl>
<p> <code>attach [NAME] [DEVICE&#8230;]</code></p>
<dl>
<dt>
<dd> Attach one or more devices to a seat. The devices should be specified via device paths in the /sys file system. To create a new seat attach at least one graphics card to a previously unused seat names. seat names may consist only of a-z, A-Z, 0-9, &quot;-&quot; and &quot;_&quot; and must be prefixed with &quot;seat&quot;. To drop assignment of a device to a specific seat just reassign it to a different seat, or use <code>flush-devices</code>.</dl>
<p> <code>flush-devices</code></p>
<dl>
<dt>
<dd> Removes all device assignments previously created with <code>attach</code>. After this call only automatically generated seats will remain and all seat hardware is assigned to them.</dl>
<p> <code>terminate-seat [NAME&#8230;]</code></p>
<dl>
<dt>
<dd> Terminates all sessions on a seat. This kills all processes of all sessions on a seat and deallocates all runtime resources attached to them.</dl>
<h2>EXIT STATUS</h2>
<p> On success 0 is returned, a non-zero failure code otherwise.</p>
<h2>ENVIRONMENT</h2>
<p> <i>$SYSTEMD_PAGER</i></p>
<dl>
<dt>
<dd> Pager to use when <code>&#8211;no-pager</code> is not given; overrides <i>$PAGER</i>. Setting this to an empty string or the value cat is equivalent to passing <code>&#8211;no-pager</code>.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1), <code><a href="/docs/linux/man/8-systemd-logind-service/">systemd-logind.service</a></code>(8), <code><a href="/docs/linux/man/5-systemd-logind-conf/">systemd-logind.conf</a></code>(5)</p>
<h2>AUTHOR</h2>
<p> <code>Lennart Poettering</code> &lt;lennart [at] poettering.net&gt;</p>
<dl>
<dt>
<dd> Developer</dl>
<h2>Index</h2>
