---
title: "runc-run(8)"
name: "runc-run"
section: "8"
letter: "r"
url: "/docs/linux/man/8-runc-run/"
description: "runc-run – create and start a container"
---

<p><code>runc-run</code> &#8211; create and start a container </p>
<h2>Synopsis</h2>
<p><code>runc run</code> [<i>option</i> &#8230;] <i>container-id</i> </p>
<h2>Description</h2>
<p>The <code>run</code> command creates an instance of a container from a bundle, and starts it. You can think of <code>run</code> as a shortcut for <code>create</code> followed by <code>start</code>. </p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;bundle</code>|<code>-b</code> <i>path</i></p>
<dd>Path to the root of the bundle directory. Default is current directory. </p>
<dt><code>&#8211;console-socket</code> <i>path</i></p>
<dd>Path to an <code>AF_UNIX</code> socket which will receive a file descriptor referencing the master end of the console&#8217;s pseudoterminal. See docs/terminals &lt;<a rel="nofollow" href="https://github.com/opencontainers/runc/blob/master/docs/terminals.md">https://github.com/opencontainers/runc/blob/master/docs/terminals.md</a>&gt;. </p>
<dt><code>&#8211;detach</code>|<code>-d</code></p>
<dd>Detach from the container&#8217;s process. </p>
<dt><code>&#8211;pid-file</code> <i>path</i></p>
<dd>Specify the file to write the initial container process&#8217; PID to. </p>
<dt><code>&#8211;no-subreaper</code></p>
<dd>Disable the use of the subreaper used to reap reparented processes. </p>
<dt><code>&#8211;no-pivot</code></p>
<dd>Do not use pivot root to jail process inside rootfs. This should not be used except in exceptional circumstances, and may be unsafe from the security standpoint. </p>
<dt><code>&#8211;no-new-keyring</code></p>
<dd>Do not create a new session keyring for the container. This will cause the container to inherit the calling processes session key. </p>
<dt><code>&#8211;preserve-fds</code> <i>N</i></p>
<dd>Pass <i>N</i> additional file descriptors to the container (<code>stdio</code> + <code>$LISTEN_FDS</code> + <i>N</i> in total). Default is <code>0</code>. </p>
<dt><code>&#8211;keep</code></p>
<dd>Keep container&#8217;s state directory and cgroup. This can be helpful if a user wants to check the state (e.g. of cgroup controllers) after the container has exited. If this option is used, a manual <code>runc delete</code> is needed afterwards to clean an exited container&#8217;s artefacts. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-runc/">runc</a></code>(8). </p>
