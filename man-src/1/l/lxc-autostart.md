---
title: "lxc-autostart(1)"
name: "lxc-autostart"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lxc-autostart/"
description: "lxc-autostart – start/stop/kill auto-started containers"
---

<h2>NAME</h2>
<p> lxc-autostart &#8211; start/stop/kill auto-started containers</p>
<h2>SYNOPSIS</h2>
<p> <code>lxc-autostart</code> [-k] [-L] [-r] [-s] [-a] [-g <i>groups</i>] [-t <i>timeout</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>lxc-autostart</code> processes containers with lxc.start.auto set. It lets the user start, shutdown, kill, restart containers in the right order, waiting the right time. Supports filtering by lxc.group or just run against all defined containers. It can also be used by external tools in list mode where no action will be performed and the list of affected containers (and if relevant, delays) will be shown. </p>
<p> The [-r], [-s] and [-k] options specify the action to perform. If none is specified, then the containers will be started. [-a] and [-g] are used to specify which containers will be affected. By default only containers without a lxc.group set will be affected. [-t TIMEOUT] specifies the maximum amount of time to wait for the container to complete the shutdown or reboot.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-r,&#8211;reboot </code></p>
<dd> Request a reboot of the container.</p>
<dt><code>-s,&#8211;shutdown </code></p>
<dd> Request a clean shutdown. If a [-t timeout] greater than 0 is given and the container has not shut down within this period, it will be killed as with the [-k kill] option.</p>
<dt><code>-k,&#8211;kill </code></p>
<dd> Rather than requesting a clean shutdown of the container, explicitly kill all tasks in the container.</p>
<dt><code>-L,&#8211;list </code></p>
<dd> Rather than performing the action, just print the container name and wait delays until starting the next container.</p>
<dt><code>-t,&#8211;timeout </code><i>TIMEOUT</i></p>
<dd> Wait TIMEOUT seconds before hard-stopping the container.</p>
<dt><code>-g,&#8211;group </code><i>GROUP</i></p>
<dd> Comma separated list of groups to select (defaults to those without a lxc.group &#8211; the NULL group). This option may be specified multiple times and the arguments concatenated. The NULL or empty group may be specified as a leading comma, trailing comma, embedded double comma, or empty argument where the NULL group should be processed. Groups are processed in the order specified on the command line. Multiple invocations of the -g option may be freely intermixed with the comma separated lists and will be combined in specified order.</p>
<dt><code>-a,&#8211;all</code></p>
<dd> Ignore lxc.group and select all auto-started containers.</dl>
<h2>AUTOSTART AND SYSTEM BOOT</h2>
<p> The <code>lxc-autostart</code> command is used as part of the LXC system service, when enabled to run on host system at bootup and at shutdown. It&#8217;s used to select which containers to start in what order and how much to delay between each startup when the host system boots. </p>
<p> Each container can be part of any number of groups or no group at all. Two groups are special. One is the NULL group, i.e. the container does not belong to any group. The other group is the &quot;onboot&quot; group. </p>
<p> When the system boots with the LXC service enabled, it will first attempt to boot any containers with lxc.start.auto == 1 that is a member of the &quot;onboot&quot; group. The startup will be in order of lxc.start.order. If an lxc.start.delay has been specified, that delay will be honored before attempting to start the next container to give the current container time to begin initialization and reduce overloading the host system. After starting the members of the &quot;onboot&quot; group, the LXC system will proceed to boot containers with lxc.start.auto == 1 which are not members of any group (the NULL group) and proceed as with the onboot group.</p>
<h2>STARTUP GROUP EXAMPLES</h2>
<dl>
<dt><code>-g &quot;onboot,&quot;</code></p>
<dd> Start the &quot;onboot&quot; group first then the NULL group. </p>
<p> This is the equivalent of: <code>-g onboot -g &quot;&quot;</code>.</p>
<dt><code>-g &quot;dns,web,,onboot&quot;</code></p>
<dd> Starts the &quot;dns&quot; group first, the &quot;web&quot; group second, then the NULL group followed by the &quot;onboot&quot; group. </p>
<p> This is the equivalent of: <code>-g dns,web -g ,onboot</code> or <code>-g dns -g web -g &quot;&quot; -g onboot</code>.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-lxc/">lxc</a></code>(7), <code><a href="/docs/linux/man/1-lxc-create/">lxc-create</a></code>(1), <code><a href="/docs/linux/man/1-lxc-destroy/">lxc-destroy</a></code>(1), <code><a href="/docs/linux/man/1-lxc-start/">lxc-start</a></code>(1), <code><a href="/docs/linux/man/1-lxc-stop/">lxc-stop</a></code>(1), <code><a href="/docs/linux/man/1-lxc-execute/">lxc-execute</a></code>(1), <code><a href="/docs/linux/man/1-lxc-console/">lxc-console</a></code>(1), <code><a href="/docs/linux/man/1-lxc-monitor/">lxc-monitor</a></code>(1), <code><a href="/docs/linux/man/1-lxc-wait/">lxc-wait</a></code>(1), <code><a href="/docs/linux/man/1-lxc-cgroup/">lxc-cgroup</a></code>(1), <code><a href="/docs/linux/man/1-lxc-ls/">lxc-ls</a></code>(1), <code><a href="/docs/linux/man/1-lxc-info/">lxc-info</a></code>(1), <code><a href="/docs/linux/man/1-lxc-freeze/">lxc-freeze</a></code>(1), <code><a href="/docs/linux/man/1-lxc-unfreeze/">lxc-unfreeze</a></code>(1), <code><a href="/docs/linux/man/1-lxc-attach/">lxc-attach</a></code>(1), <code><a href="/docs/linux/man/5-lxc-conf/">lxc.conf</a></code>(5)</p>
<h2>AUTHOR</h2>
<p> St&eacute;phane Graber &lt;stgraber [at] ubuntu.com&gt; </p>
<h2>Index</h2>
