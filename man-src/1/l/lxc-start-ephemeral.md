---
title: "lxc-start-ephemeral(1)"
name: "lxc-start-ephemeral"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lxc-start-ephemeral/"
description: "lxc-start-ephemeral – start an ephemeral copy of an existing container"
---

<h2>NAME</h2>
<p> lxc-start-ephemeral &#8211; start an ephemeral copy of an existing container</p>
<h2>SYNOPSIS</h2>
<p> <code>lxc-start-ephemeral</code> [-o] [-n] [-d] [&#8211;bdir] [&#8211;user] [&#8211;key] [&#8211;storage-type] [&#8211;union-type] [&#8211;keep-data] [COMMAND]</p>
<h2>DESCRIPTION</h2>
<p> <code>lxc-start-ephemeral</code> start an ephemeral copy of an existing container.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-o</code></p>
<dd> Original container name</p>
<dt><code>[-n]</code></p>
<dd> Name of the ephemeral container (defaults to a random suffix).</p>
<dt><code>[-d]</code></p>
<dd> Start the container in background and print the name and IP. This option can&#8217;t be used if a command is passed.</p>
<dt><code>[&#8211;bdir]</code></p>
<dd> Directory to bind mount into container. Can be passed multiple times.</p>
<dt><code>[&#8211;user]</code></p>
<dd> The user to connect to the container as. Used when passing a command to lxc-start-ephemeral.</p>
<dt><code>[&#8211;key]</code></p>
<dd> Copy the provided SSH public key into the container.</p>
<dt><code>[&#8211;storage-type]</code></p>
<dd> Specify the type of storage used by the container. Valid types are tmpfs or dir.</p>
<dt><code>[&#8211;union-type]</code></p>
<dd> Force a specific union file system. Can be one of: overlayfs aufs</p>
<dt><code>[&#8211;keep-data]</code></p>
<dd> Use a persistent backend instead of tmpfs. With this option, you can lxc-stop and lxc-start the no longer so ephemeral container (it&#8217;s still an overlay, but a persistent one).</p>
<dt><code>[COMMAND]</code></p>
<dd> Immediately run the provided command in the container. This uses attach if the kernel supports it, otherwise uses ssh. This is incompatible with daemon mode.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-lxc-start/">lxc-start</a></code>(1),</p>
<h2>EXAMPLES</h2>
<dl>
<dt>lxc-start-ephemeral -o p1</p>
<dd> Simply start an ephemeral container and attach to the console. This container will be based on existing container &quot;p1&quot;.</p>
<dt>lxc-start-ephemeral -o p1 -n p1-ephemeral -d</p>
<dd> Start an ephemeral container based on p1 called p1-ephemeral and print its IP and name to the console instead of attaching.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-lxc/">lxc</a></code>(7), <code><a href="/docs/linux/man/1-lxc-create/">lxc-create</a></code>(1), <code><a href="/docs/linux/man/1-lxc-destroy/">lxc-destroy</a></code>(1), <code><a href="/docs/linux/man/1-lxc-start/">lxc-start</a></code>(1), <code><a href="/docs/linux/man/1-lxc-stop/">lxc-stop</a></code>(1), <code><a href="/docs/linux/man/1-lxc-execute/">lxc-execute</a></code>(1), <code><a href="/docs/linux/man/1-lxc-console/">lxc-console</a></code>(1), <code><a href="/docs/linux/man/1-lxc-monitor/">lxc-monitor</a></code>(1), <code><a href="/docs/linux/man/1-lxc-wait/">lxc-wait</a></code>(1), <code><a href="/docs/linux/man/1-lxc-cgroup/">lxc-cgroup</a></code>(1), <code><a href="/docs/linux/man/1-lxc-ls/">lxc-ls</a></code>(1), <code><a href="/docs/linux/man/1-lxc-info/">lxc-info</a></code>(1), <code><a href="/docs/linux/man/1-lxc-freeze/">lxc-freeze</a></code>(1), <code><a href="/docs/linux/man/1-lxc-unfreeze/">lxc-unfreeze</a></code>(1), <code><a href="/docs/linux/man/1-lxc-attach/">lxc-attach</a></code>(1), <code><a href="/docs/linux/man/5-lxc-conf/">lxc.conf</a></code>(5)</p>
<h2>AUTHOR</h2>
<p> St&eacute;phane Graber &lt;stgraber [at] ubuntu.com&gt; </p>
<h2>Index</h2>
