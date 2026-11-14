---
title: "lxc-ps(1)"
name: "lxc-ps"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lxc-ps/"
description: "lxc-ps – list the processes belonging to a specific container."
---

<h2>NAME</h2>
<p> lxc-ps &#8211; list the processes belonging to a specific container.</p>
<h2>SYNOPSIS</h2>
<p> <code>lxc-ps [&#8211;name name] [&#8211;lxc] [ps option] </code>.SH &quot;DESCRIPTION&quot; </p>
<p> <code>lxc-ps</code> is a wrapper tp ps command to report the name of lxc container associated to reported processes. </p>
<p> The cgroup fs must be mounted before container creation, to be able to have <code>lxc-ps</code> to find the container associated to processes. </p>
<p> The additionnal specified ps options must not remove the default ps header and the pid information, to be able to have the <code>lxc-ps</code> to find the container associated to processes.</p>
<h2>OPTIONS</h2>
<dl>
<dt><i>&#8211;name NAME</i></p>
<dd> specify the container <i>NAME</i> to limit the output to the processes belonging to this container name.</p>
<dt><i>&#8211;lxc</i></p>
<dd> limit the output to the processes belonging to all lxc containers.</p>
<dt><code>[ps options]</code></p>
<dd> The option passed to <code>lxc-ps</code> are the same as the <code>ps</code> command.</dl>
<h2>EXAMPLE</h2>
<dl>
<dt><code>lxc-ps &#8211;name foo &#8211;forest</code></p>
<dd> list all the processes belonging to container &#8216;foo&#8217; and show dependencies.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ps/">ps</a></code>(1),</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-lxc/">lxc</a></code>(1), <code><a href="/docs/linux/man/1-lxc-create/">lxc-create</a></code>(1), <code><a href="/docs/linux/man/1-lxc-destroy/">lxc-destroy</a></code>(1), <code><a href="/docs/linux/man/1-lxc-start/">lxc-start</a></code>(1), <code><a href="/docs/linux/man/1-lxc-stop/">lxc-stop</a></code>(1), <code><a href="/docs/linux/man/1-lxc-execute/">lxc-execute</a></code>(1), <code><a href="/docs/linux/man/1-lxc-console/">lxc-console</a></code>(1), <code><a href="/docs/linux/man/1-lxc-monitor/">lxc-monitor</a></code>(1), <code><a href="/docs/linux/man/1-lxc-wait/">lxc-wait</a></code>(1), <code><a href="/docs/linux/man/1-lxc-cgroup/">lxc-cgroup</a></code>(1), <code><a href="/docs/linux/man/1-lxc-ls/">lxc-ls</a></code>(1), <code><a href="/docs/linux/man/1-lxc-ps/">lxc-ps</a></code>(1), <code><a href="/docs/linux/man/1-lxc-info/">lxc-info</a></code>(1), <code><a href="/docs/linux/man/1-lxc-freeze/">lxc-freeze</a></code>(1), <code><a href="/docs/linux/man/1-lxc-unfreeze/">lxc-unfreeze</a></code>(1), <code><a href="/docs/linux/man/5-lxc-conf/">lxc.conf</a></code>(5)</p>
<h2>AUTHOR</h2>
<p> Daniel Lezcano &lt;daniel.lezcano [at] free.fr&gt; </p>
<h2>Index</h2>
