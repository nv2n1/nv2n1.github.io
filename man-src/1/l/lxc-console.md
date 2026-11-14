---
title: "lxc-console(1)"
name: "lxc-console"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lxc-console/"
description: "lxc-console – Launch a console for the specified container"
---

<h2>NAME</h2>
<p> lxc-console &#8211; Launch a console for the specified container</p>
<h2>SYNOPSIS</h2>
<p> <code>lxc-console</code> {-n <i>name</i>} [-e <i>escape character</i>] [-t <i>ttynum</i>]</p>
<h2>DESCRIPTION</h2>
<p> If the tty service has been configured and is available for the container specified as parameter, this command will launch a console allowing to log on the container. </p>
<p> The available tty are free slots taken by this command. That means if the container has four ttys available and the command has been launched four times each taking a different tty, the fifth command will fail because no console will be available. </p>
<p> The command will connect to a tty. If the connection is lost or broken, the command can be launched again and regain the tty at the state it was before the disconnection. </p>
<p> A <i>ttynum</i> of 0 may be given to attach to the container&#8217;s /dev/console instead of its dev/tty&lt;<i>ttynum</i>&gt;. </p>
<p> A keyboard escape sequence may be used to disconnect from the tty and quit lxc-console. The default escape sequence is &lt;Ctrl+a q&gt;.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-e </code><code>[</code><i>escape character</i><code>]</code></p>
<dd> Specify the escape sequence prefix to use instead of &lt;Ctrl a&gt;. This may be given as &#8216;^letter&#8217; or just &#8216;letter&#8217;. For example to use &lt;Ctrl+b q&gt; as the escape sequence use -e &#8216;^b&#8217;.</p>
<dt><code>-t </code><code>[</code><i>ttynum</i><code>]</code></p>
<dd> Specify the tty number to connect to or 0 for the console. If not specified the next available tty number will be automatically chosen by the container.</dl>
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
<dt>tty service denied</p>
<dd> No tty is available or there is not enough privilege to use the console. For example, the container belongs to user &quot;foo&quot; and &quot;bar&quot; is trying to open a console to it.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-lxc/">lxc</a></code>(7), <code><a href="/docs/linux/man/1-lxc-create/">lxc-create</a></code>(1), <code><a href="/docs/linux/man/1-lxc-destroy/">lxc-destroy</a></code>(1), <code><a href="/docs/linux/man/1-lxc-start/">lxc-start</a></code>(1), <code><a href="/docs/linux/man/1-lxc-stop/">lxc-stop</a></code>(1), <code><a href="/docs/linux/man/1-lxc-execute/">lxc-execute</a></code>(1), <code><a href="/docs/linux/man/1-lxc-console/">lxc-console</a></code>(1), <code><a href="/docs/linux/man/1-lxc-monitor/">lxc-monitor</a></code>(1), <code><a href="/docs/linux/man/1-lxc-wait/">lxc-wait</a></code>(1), <code><a href="/docs/linux/man/1-lxc-cgroup/">lxc-cgroup</a></code>(1), <code><a href="/docs/linux/man/1-lxc-ls/">lxc-ls</a></code>(1), <code><a href="/docs/linux/man/1-lxc-info/">lxc-info</a></code>(1), <code><a href="/docs/linux/man/1-lxc-freeze/">lxc-freeze</a></code>(1), <code><a href="/docs/linux/man/1-lxc-unfreeze/">lxc-unfreeze</a></code>(1), <code><a href="/docs/linux/man/1-lxc-attach/">lxc-attach</a></code>(1), <code><a href="/docs/linux/man/5-lxc-conf/">lxc.conf</a></code>(5)</p>
<h2>AUTHOR</h2>
<p> Daniel Lezcano &lt;daniel.lezcano [at] free.fr&gt; </p>
<h2>Index</h2>
