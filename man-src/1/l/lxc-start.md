---
title: "lxc-start(1)"
name: "lxc-start"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lxc-start/"
description: "lxc-start – run an application inside a container."
---

<h2>NAME</h2>
<p> lxc-start &#8211; run an application inside a container.</p>
<h2>SYNOPSIS</h2>
<p> <code>lxc-start</code> {-n <i>name</i>} [-f <i>config_file</i>] [-c <i>console_device</i>] [-L <i>console_logfile</i>] [-d] [-F] [-p <i>pid_file</i>] [-s KEY=VAL] [-C] [&#8211;share-[net|ipc|uts] <i>name|pid</i>] [command]</p>
<h2>DESCRIPTION</h2>
<p> <code>lxc-start</code> runs the specified <i>command</i> inside the container specified by <i>name</i>. </p>
<p> It will setup the container according to the configuration previously defined with the lxc-create command or with the configuration file parameter. If no configuration is defined, the default isolation is used. </p>
<p> If no command is specified, <code>lxc-start</code> will use the default <code>&quot;/sbin/init&quot;</code> command to run a system container.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d, &#8211;daemon</code></dt>
<dd> Run the container as a daemon. As the container has no more tty, if an error occurs nothing will be displayed, the log file can be used to check the error.</dd>
<dt><code>-F, &#8211;foreground</code></dt>
<dd> Run the container in the foreground. In this mode, the container console will be attached to the current tty and signals will be routed directly to the container. (This is the default mode)</dd>
<dt><code>-p, &#8211;pidfile </code><i>pid_file</i></dt>
<dd> Create a file with the process id.</dd>
<dt><code>-f, &#8211;rcfile </code><i>config_file</i></dt>
<dd> Specify the configuration file to configure the virtualization and isolation functionalities for the container. </dd>
<p> This configuration file if present will be used even if there is already a configuration file present in the previously created container (via lxc-create).</p>
<dt><code>-c, &#8211;console </code><i>console_device</i></dt>
<dd> Specify a device to use for the container&#8217;s console, for example /dev/tty8. If this option is not specified the current terminal will be used unless <code>-d</code> is specified.</dd>
<dt><code>-L, &#8211;console-log </code><i>console_logfile</i></dt>
<dd> Specify a file to log the container&#8217;s console output to.</dd>
<dt><code>-s, &#8211;define </code><i>KEY=VAL</i></dt>
<dd> Assign value <i>VAL</i> to configuration variable <i>KEY</i>. This overrides any assignment done in <i>config_file</i>.</dd>
<dt><code>-C, &#8211;close-all-fds</code></dt>
<dd> If any file descriptors are inherited, close them. If this option is not specified, then <code>lxc-start</code> will exit with failure instead. Note: <i>&#8211;daemon</i> implies <i>&#8211;close-all-fds</i>.</dd>
<dt><code>&#8211;share-net </code><i>name|pid</i></dt>
<dd> Inherit a network namespace from a <i>name</i> container or a <i>pid</i>. The network namespace will continue to be managed by the original owner. The network configuration of the starting container is ignored and the up/down scripts won&#8217;t be executed.</dd>
<dt><code>&#8211;share-ipc </code><i>name|pid</i></dt>
<dd> Inherit an IPC namespace from a <i>name</i> container or a <i>pid</i>.</dd>
<dt><code>&#8211;share-uts </code><i>name|pid</i></dt>
<dd> Inherit a UTS namespace from a <i>name</i> container or a <i>pid</i>. The starting LXC will not set the hostname, but the container OS may do it anyway.</dd></dl>
<h2>COMMON OPTIONS</h2>
<p> These options are common to most of lxc commands.</p>
<dl>
<dt><code>-?, -h, &#8211;help</code></dt>
<dd> Print a longer usage message than normal.</dd>
<dt><code>&#8211;usage</code></dt>
<dd> Give the usage message</dd>
<dt><code>-q, &#8211;quiet</code></dt>
<dd> mute on</dd>
<dt><code>-P, &#8211;lxcpath=</code><i>PATH</i></dt>
<dd> Use an alternate container path. The default is /var/lib/lxc.</dd>
<dt><code>-o, &#8211;logfile=</code><i>FILE</i></dt>
<dd> Output to an alternate log <i>FILE</i>. The default is no log.</dd>
<dt><code>-l, &#8211;logpriority=</code><i>LEVEL</i></dt>
<dd> Set log priority to <i>LEVEL</i>. The default log priority is ERROR. Possible values are : FATAL, CRIT, WARN, ERROR, NOTICE, INFO, DEBUG. </dd>
<p> Note that this option is setting the priority of the events log in the alternate log file. It do not have effect on the ERROR events log on stderr.</p>
<dt><code>-n, &#8211;name=</code><i>NAME</i></dt>
<dd> Use container identifier <i>NAME</i>. The container identifier format is an alphanumeric string.</dd>
<dt><code>&#8211;version</code></dt>
<dd> Show the version number.</dd></dl>
<h2>DIAGNOSTIC</h2>
<dl>
<dt>The container is busy</dt>
<dd> The specified container is already running an application. You should stop it before reuse this container or create a new one.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-lxc/">lxc</a></code>(7), <code><a href="/docs/linux/man/1-lxc-create/">lxc-create</a></code>(1), <code><a href="/docs/linux/man/1-lxc-destroy/">lxc-destroy</a></code>(1), <code><a href="/docs/linux/man/1-lxc-start/">lxc-start</a></code>(1), <code><a href="/docs/linux/man/1-lxc-stop/">lxc-stop</a></code>(1), <code><a href="/docs/linux/man/1-lxc-execute/">lxc-execute</a></code>(1), <code><a href="/docs/linux/man/1-lxc-console/">lxc-console</a></code>(1), <code><a href="/docs/linux/man/1-lxc-monitor/">lxc-monitor</a></code>(1), <code><a href="/docs/linux/man/1-lxc-wait/">lxc-wait</a></code>(1), <code><a href="/docs/linux/man/1-lxc-cgroup/">lxc-cgroup</a></code>(1), <code><a href="/docs/linux/man/1-lxc-ls/">lxc-ls</a></code>(1), <code><a href="/docs/linux/man/1-lxc-info/">lxc-info</a></code>(1), <code><a href="/docs/linux/man/1-lxc-freeze/">lxc-freeze</a></code>(1), <code><a href="/docs/linux/man/1-lxc-unfreeze/">lxc-unfreeze</a></code>(1), <code><a href="/docs/linux/man/1-lxc-attach/">lxc-attach</a></code>(1), <code><a href="/docs/linux/man/5-lxc-conf/">lxc.conf</a></code>(5)</p>
<h2>AUTHOR</h2>
<p> Daniel Lezcano &lt;daniel.lezcano [at] free.fr&gt; </p>
