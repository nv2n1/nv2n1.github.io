---
title: "lxc-execute(1)"
name: "lxc-execute"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lxc-execute/"
description: "lxc-execute – run an application inside a container."
---

<h2>NAME</h2>
<p> lxc-execute &#8211; run an application inside a container.</p>
<h2>SYNOPSIS</h2>
<p> <code>lxc-execute</code> {-n <i>name</i>} [-f <i>config_file</i>] [-s KEY=VAL] [&#8211; <i>command</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>lxc-execute</code> runs the specified <i>command</i> inside the container specified by <i>name</i>. </p>
<p> It will setup the container according to the configuration previously defined with the lxc-create command or with the configuration file parameter. If no configuration is defined, the default isolation is used. </p>
<p> This command is mainly used when you want to quickly launch an application in an isolated environment. </p>
<p> <code>lxc-execute</code> command will run the specified command into the container via an intermediate process, <code>lxc-init</code>. This lxc-init after launching the specified command, will wait for its end and all other reparented processes. (to support daemons in the container). In other words, in the container, <code>lxc-init</code> has the pid 1 and the first process of the application has the pid 2. </p>
<p> The above <code>lxc-init</code> is designed to forward received signals to the started command.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f, &#8211;rcfile </code><i>config_file</i></p>
<dd> Specify the configuration file to configure the virtualization and isolation functionalities for the container. </p>
<p> This configuration file if present will be used even if there is already a configuration file present in the previously created container (via lxc-create).</p>
<dt><code>-s, &#8211;define </code><i>KEY=VAL</i></p>
<dd> Assign value <i>VAL</i> to configuration variable <i>KEY</i>. This overrides any assignment done in <i>config_file</i>.</p>
<dt><code>&#8212;</code></p>
<dd> Signal the end of options and disables further option processing. Any arguments after the &#8212; are treated as arguments to <i>command</i>. </p>
<p> This option is useful when you want specify options to <i>command</i> and don&#8217;t want <code>lxc-execute</code> to interpret them.</dl>
<h2>COMMON OPTIONS</h2>
<p> These options are common to most of lxc commands.</p>
<dl>
<dt><code>-?, -h, &#8211;help</code></p>
<dd> Print a longer usage message than normal.</p>
<dt><code>&#8211;usage</code></p>
<dd> Give the usage message</p>
<dt><code>-q, &#8211;quiet</code></p>
<dd> mute on</p>
<dt><code>-P, &#8211;lxcpath=</code><i>PATH</i></p>
<dd> Use an alternate container path. The default is /var/lib/lxc.</p>
<dt><code>-o, &#8211;logfile=</code><i>FILE</i></p>
<dd> Output to an alternate log <i>FILE</i>. The default is no log.</p>
<dt><code>-l, &#8211;logpriority=</code><i>LEVEL</i></p>
<dd> Set log priority to <i>LEVEL</i>. The default log priority is ERROR. Possible values are : FATAL, CRIT, WARN, ERROR, NOTICE, INFO, DEBUG. </p>
<p> Note that this option is setting the priority of the events log in the alternate log file. It do not have effect on the ERROR events log on stderr.</p>
<dt><code>-n, &#8211;name=</code><i>NAME</i></p>
<dd> Use container identifier <i>NAME</i>. The container identifier format is an alphanumeric string.</p>
<dt><code>&#8211;version</code></p>
<dd> Show the version number.</dl>
<h2>DIAGNOSTIC</h2>
<dl>
<dt>The container is busy</p>
<dd> The specified container is already running an application. You should stop it before reuse this container or create a new one.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-lxc/">lxc</a></code>(7), <code><a href="/docs/linux/man/1-lxc-create/">lxc-create</a></code>(1), <code><a href="/docs/linux/man/1-lxc-destroy/">lxc-destroy</a></code>(1), <code><a href="/docs/linux/man/1-lxc-start/">lxc-start</a></code>(1), <code><a href="/docs/linux/man/1-lxc-stop/">lxc-stop</a></code>(1), <code><a href="/docs/linux/man/1-lxc-execute/">lxc-execute</a></code>(1), <code><a href="/docs/linux/man/1-lxc-console/">lxc-console</a></code>(1), <code><a href="/docs/linux/man/1-lxc-monitor/">lxc-monitor</a></code>(1), <code><a href="/docs/linux/man/1-lxc-wait/">lxc-wait</a></code>(1), <code><a href="/docs/linux/man/1-lxc-cgroup/">lxc-cgroup</a></code>(1), <code><a href="/docs/linux/man/1-lxc-ls/">lxc-ls</a></code>(1), <code><a href="/docs/linux/man/1-lxc-info/">lxc-info</a></code>(1), <code><a href="/docs/linux/man/1-lxc-freeze/">lxc-freeze</a></code>(1), <code><a href="/docs/linux/man/1-lxc-unfreeze/">lxc-unfreeze</a></code>(1), <code><a href="/docs/linux/man/1-lxc-attach/">lxc-attach</a></code>(1), <code><a href="/docs/linux/man/5-lxc-conf/">lxc.conf</a></code>(5)</p>
<h2>AUTHOR</h2>
<p> Daniel Lezcano &lt;daniel.lezcano [at] free.fr&gt; </p>
<h2>Index</h2>
