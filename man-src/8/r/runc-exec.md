---
title: "runc-exec(8)"
name: "runc-exec"
section: "8"
letter: "r"
url: "/docs/linux/man/8-runc-exec/"
description: "runc-exec – execute new process inside the container"
---

<p><code>runc-exec</code> &#8211; execute new process inside the container </p>
<h2>Synopsis</h2>
<p><code>runc exec</code> [<i>option</i> &#8230;] <i>container-id</i> [&#8211;] <i>command</i> [<i>arg</i> &#8230;] <code>runc exec</code> [<i>option</i> &#8230;] <code>-p</code> <i>process.json</i> <i>container-id</i> </p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;console-socket</code> <i>path</i></p>
<dd>Path to an <code>AF_UNIX</code> socket which will receive a file descriptor referencing the master end of the console&#8217;s pseudoterminal. See docs/terminals &lt;<a rel="nofollow" href="https://github.com/opencontainers/runc/blob/master/docs/terminals.md">https://github.com/opencontainers/runc/blob/master/docs/terminals.md</a>&gt;. </p>
<dt><code>&#8211;cwd</code> <i>path</i></p>
<dd>Change to <i>path</i> in the container before executing the command. </p>
<dt><code>&#8211;env</code>|<code>-e</code> <i>name</i>=<i>value</i></p>
<dd>Set an environment variable <i>name</i> to <i>value</i>. Can be specified multiple times. </p>
<dt><code>&#8211;tty</code>|<code>-t</code></p>
<dd>Allocate a pseudo-TTY. </p>
<dt><code>&#8211;user</code>|<code>-u</code> <i>uid</i>[:<i>gid</i>]</p>
<dd>Run the <i>command</i> as a user (and, optionally, group) specified by <i>uid</i> (and <i>gid</i>). </p>
<dt><code>&#8211;additional-gids</code>|<code>-g</code> <i>gid</i></p>
<dd>Add additional group IDs. Can be specified multiple times. </p>
<dt><code>&#8211;process</code>|<code>-p</code> <i>process.json</i></p>
<dd>Instead of specifying all the exec parameters directly on the command line, get them from a <i>process.json</i>, a JSON file containing the process specification as defined by the OCI runtime spec &lt;<a rel="nofollow" href="https://github.com/opencontainers/runtime-spec/blob/master/config.md#process">https://github.com/opencontainers/runtime-spec/blob/master/config.md#process</a>&gt;. </p>
<dt><code>&#8211;detach</code>|<code>-d</code></p>
<dd>Detach from the container&#8217;s process. </p>
<dt><code>&#8211;pid-file</code> <i>path</i></p>
<dd>Specify the file to write the container process&#8217; PID to. </p>
<dt><code>&#8211;process-label</code> <i>label</i></p>
<dd>Set the asm process label for the process commonly used with <code><a href="/docs/linux/man/7-selinux/">selinux</a></code>(7). </p>
<dt><code>&#8211;apparmor</code> <i>profile</i></p>
<dd>Set the <code><a href="/docs/linux/man/7-apparmor/">apparmor</a></code>(7) <i>profile</i> for the process. </p>
<dt><code>&#8211;no-new-privs</code></p>
<dd>Set the &quot;no new privileges&quot; value for the process. </p>
<dt><code>&#8211;cap</code> <i>cap</i></p>
<dd>Add a capability to the bounding set for the process. Can be specified multiple times. </p>
<dt><code>&#8211;preserve-fds</code> <i>N</i></p>
<dd>Pass <i>N</i> additional file descriptors to the container (<code>stdio</code> + <code>$LISTEN_FDS</code> + <i>N</i> in total). Default is <code>0</code>. </p>
<dt><code>&#8211;ignore-paused</code></p>
<dd>Allow exec in a paused container. By default, if a container is paused, <code>runc exec</code> errors out; this option can be used to override it. A paused container needs to be resumed for the exec to complete. </p>
<dt><code>&#8211;cgroup</code> <i>path</i> | <i>controller</i>[,<i>controller</i>&#8230;]:<i>path</i></p>
<dd>Execute a process in a sub-cgroup. If the specified cgroup does not exist, an error is returned. Default is empty path, which means to use container&#8217;s top level cgroup. </p>
<p> For cgroup v1 only, a particular <i>controller</i> (or multiple comma-separated controllers) can be specified, and the option can be used multiple times to set different paths for different controllers. </p>
<p> Note for cgroup v2, in case the process can&#8217;t join the top level cgroup, <code>runc exec</code> fallback is to try joining the cgroup of container&#8217;s init. This fallback can be disabled by using <code>&#8211;cgroup /</code>. </p>
</dl>
<h2>Exit Status</h2>
<p>Exits with a status of <i>command</i> (unless <code>-d</code> is used), or <code>255</code> if an error occurred.</p>
<h2>Examples</h2>
<p>If the container can run <code><a href="/docs/linux/man/1-ps/">ps</a></code>(1) command, the following will output a list of processes running in the container:  </p>
<pre># runc exec &lt;container-id&gt; ps</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-runc/">runc</a></code>(8). </p>
