---
title: "lxc-stop(1)"
name: "lxc-stop"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lxc-stop/"
description: "lxc-stop – stop the application running inside a container"
---

<h2>NAME</h2>
<p> lxc-stop &#8211; stop the application running inside a container</p>
<h2>SYNOPSIS</h2>
<p> <code>lxc-stop</code> {-n <i>name</i>} [-W] [-r] [-t <i>timeout</i>] [-k] [&#8211;nokill] [&#8211;nolock]</p>
<h2>DESCRIPTION</h2>
<p> <code>lxc-stop</code> reboots, cleanly shuts down, or kills all the processes inside the container. By default, it will request a clean shutdown of the container by sending <code>lxc.haltsignal</code> (defaults to SIGPWR) to the container&#8217;s init process, waiting up to 60 seconds for the container to exit, and then returning. If the container fails to cleanly exit in 60 seconds, it will be sent the <code>lxc.stopsignal</code> (defaults to SIGKILL) to force it to shut down. </p>
<p> The [-W], [-r], [-k] and [&#8211;nokill] options specify the action to perform. [-W] indicates that after performing the specified action, <code>lxc-stop</code> should immediately exit, while [-t TIMEOUT] specifies the maximum amount of time to wait for the container to complete the shutdown or reboot.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-r,&#8211;reboot </code></p>
<dd> Request a reboot of the container.</p>
<dt><code>-k,&#8211;kill </code></p>
<dd> Rather than requesting a clean shutdown of the container, explicitly kill all tasks in the container. This is the legacy <code>lxc-stop</code> behavior.</p>
<dt><code>&#8211;nokill</code></p>
<dd> Only request a clean shutdown, do not kill the container tasks if the clean shutdown fails.</p>
<dt><code>&#8211;nolock </code></p>
<dd> This option avoids the use of any of the API lxc locking, and should only be used if <code>lxc-stop</code> is hanging due to a bad system state.</p>
<dt><code>-W,&#8211;nowait </code></p>
<dd> Simply perform the requestion action (reboot, shutdown, or hard kill) and exit.</p>
<dt><code>-t,&#8211;timeout </code><i>TIMEOUT</i></p>
<dd> Wait TIMEOUT seconds before hard-stopping the container.</dl>
<h2>EXIT VALUE</h2>
<dl>
<dt>0</p>
<dd> The container was successfully stopped.</p>
<dt>1</p>
<dd> An error occurred while stopping the container.</p>
<dt>2</p>
<dd> The specified container exists but was not running.</dl>
<h2>DIAGNOSTIC</h2>
<dl>
<dt>The container was not found</p>
<dd> The specified container was not created before with the <code>lxc-create</code> command.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-lxc/">lxc</a></code>(7), <code><a href="/docs/linux/man/1-lxc-create/">lxc-create</a></code>(1), <code><a href="/docs/linux/man/1-lxc-destroy/">lxc-destroy</a></code>(1), <code><a href="/docs/linux/man/1-lxc-start/">lxc-start</a></code>(1), <code><a href="/docs/linux/man/1-lxc-stop/">lxc-stop</a></code>(1), <code><a href="/docs/linux/man/1-lxc-execute/">lxc-execute</a></code>(1), <code><a href="/docs/linux/man/1-lxc-console/">lxc-console</a></code>(1), <code><a href="/docs/linux/man/1-lxc-monitor/">lxc-monitor</a></code>(1), <code><a href="/docs/linux/man/1-lxc-wait/">lxc-wait</a></code>(1), <code><a href="/docs/linux/man/1-lxc-cgroup/">lxc-cgroup</a></code>(1), <code><a href="/docs/linux/man/1-lxc-ls/">lxc-ls</a></code>(1), <code><a href="/docs/linux/man/1-lxc-info/">lxc-info</a></code>(1), <code><a href="/docs/linux/man/1-lxc-freeze/">lxc-freeze</a></code>(1), <code><a href="/docs/linux/man/1-lxc-unfreeze/">lxc-unfreeze</a></code>(1), <code><a href="/docs/linux/man/1-lxc-attach/">lxc-attach</a></code>(1), <code><a href="/docs/linux/man/5-lxc-conf/">lxc.conf</a></code>(5)</p>
<h2>AUTHOR</h2>
<p> Daniel Lezcano &lt;daniel.lezcano [at] free.fr&gt; </p>
<h2>Index</h2>
