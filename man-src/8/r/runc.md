---
title: "runc(8)"
name: "runc"
section: "8"
letter: "r"
url: "/docs/linux/man/8-runc/"
description: "runc – Open Container Initiative runtime"
---

<p><code>runc</code> &#8211; Open Container Initiative runtime </p>
<h2>Synopsis</h2>
<p><code>runc</code> [<i>global-option</i> &#8230;] <i>command</i> [<i>command-option</i> &#8230;] [<i>argument</i> &#8230;] </p>
<h2>Description</h2>
<p>runc is a command line client for running applications packaged according to the Open Container Initiative (OCI) format and is a compliant implementation of the Open Container Initiative specification. runc integrates well with existing process supervisors to provide a production container runtime environment for applications. It can be used with your existing process monitoring tools and the container will be spawned as a direct child of the process supervisor. Containers are configured using bundles. A bundle for a container is a directory that includes a specification file named <i>config.json</i> and a root filesystem. The root filesystem contains the contents of the container. To run a new instance of a container:  </p>
<pre># runc run [ -b bundle ] container-id</pre>
</dl>
<p> Where <i>container-id</i> is your name for the instance of the container that you are starting. The name you provide for the container instance must be unique on your host. Providing the bundle directory using <code>-b</code> is optional. The default value for <i>bundle</i> is the current directory. </p>
<h2>Commands</h2>
<dl>
<dt><code>checkpoint</code></p>
<dd>Checkpoint a running container. See <code><a href="/docs/linux/man/8-runc-checkpoint/">runc-checkpoint</a></code>(8). </p>
<dt><code>create</code></p>
<dd>Create a container. See <code><a href="/docs/linux/man/8-runc-create/">runc-create</a></code>(8). </p>
<dt><code>delete</code></p>
<dd>Delete any resources held by the container often used with detached containers. See <code><a href="/docs/linux/man/8-runc-delete/">runc-delete</a></code>(8). </p>
<dt><code>events</code></p>
<dd>Display container events such as OOM notifications, cpu, memory, IO and network stats. See <code><a href="/docs/linux/man/8-runc-events/">runc-events</a></code>(8). </p>
<dt><code>exec</code></p>
<dd>Execute a new process inside the container. See <code><a href="/docs/linux/man/8-runc-exec/">runc-exec</a></code>(8). </p>
<dt><code>init</code></p>
<dd>Initialize the namespaces and launch the container init process. This command is not supposed to be used directly. </p>
<dt><code>kill</code></p>
<dd>Send a specified signal to the container&#8217;s init process. See <code><a href="/docs/linux/man/8-runc-kill/">runc-kill</a></code>(8). </p>
<dt><code>list</code></p>
<dd>List containers started by runc with the given <code>&#8211;root</code>. See <code><a href="/docs/linux/man/8-runc-list/">runc-list</a></code>(8). </p>
<dt><code>pause</code></p>
<dd>Suspend all processes inside the container. See <code><a href="/docs/linux/man/8-runc-pause/">runc-pause</a></code>(8). </p>
<dt><code>ps</code></p>
<dd>Show processes running inside the container. See <code><a href="/docs/linux/man/8-runc-ps/">runc-ps</a></code>(8). </p>
<dt><code>restore</code></p>
<dd>Restore a container from a previous checkpoint. See <code><a href="/docs/linux/man/8-runc-restore/">runc-restore</a></code>(8). </p>
<dt><code>resume</code></p>
<dd>Resume all processes that have been previously paused. See <code><a href="/docs/linux/man/8-runc-resume/">runc-resume</a></code>(8). </p>
<dt><code>run</code></p>
<dd>Create and start a container. See <code><a href="/docs/linux/man/8-runc-run/">runc-run</a></code>(8). </p>
<dt><code>spec</code></p>
<dd>Create a new specification file (<i>config.json</i>). See <code><a href="/docs/linux/man/8-runc-spec/">runc-spec</a></code>(8). </p>
<dt><code>start</code></p>
<dd>Start a container previously created by <code>runc create</code>. See <code><a href="/docs/linux/man/8-runc-start/">runc-start</a></code>(8). </p>
<dt><code>state</code></p>
<dd>Show the container state. See <code><a href="/docs/linux/man/8-runc-state/">runc-state</a></code>(8). </p>
<dt><code>update</code></p>
<dd>Update container resource constraints. See <code><a href="/docs/linux/man/8-runc-update/">runc-update</a></code>(8). </p>
<dt><code>help</code>, <code>h</code></p>
<dd>Show a list of commands or help for a particular command. </p>
</dl>
<h2>Global Options</h2>
<p>These options can be used with any command, and must precede the <code>command</code>. </p>
<dl>
<dt><code>&#8211;debug</code></p>
<dd>Enable debug logging. </p>
<dt><code>&#8211;log</code> <i>path</i></p>
<dd>Set the log destination to <i>path</i>. The default is to log to stderr. </p>
<dt><code>&#8211;log-format</code> <code>text</code>|<code>json</code></p>
<dd>Set the log format (default is <code>text</code>). </p>
<dt><code>&#8211;root</code> <i>path</i></p>
<dd>Set the root directory to store containers&#8217; state. The <i>path</i> should be located on tmpfs. Default is <i>/run/runc</i>, or <i>$XDG_RUNTIME_DIR/runc</i> for rootless containers. </p>
<dt><code>&#8211;criu</code> <i>path</i></p>
<dd>Set the path to the <code><a href="/docs/linux/man/8-criu/">criu</a></code>(8) binary used for checkpoint and restore. Default is <code>criu</code>. </p>
<dt><code>&#8211;systemd-cgroup</code></p>
<dd>Enable systemd cgroup support. If this is set, the container spec (<i>config.json</i>) is expected to have <code>cgroupsPath</code> value in the <i>slice:prefix:name</i> form (e.g. <code>system.slice:runc:434234</code>). </p>
<dt><code>&#8211;rootless</code> <code>true</code>|<code>false</code>|<code>auto</code></p>
<dd>Enable or disable rootless mode. Default is <code>auto</code>, meaning to auto-detect whether rootless should be enabled. </p>
<dt><code>&#8211;help</code>|<code>-h</code></p>
<dd>Show help. </p>
<dt><code>&#8211;version</code>|<code>-v</code></p>
<dd>Show version. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-runc-checkpoint/">runc-checkpoint</a></code>(8), <code><a href="/docs/linux/man/8-runc-create/">runc-create</a></code>(8), <code><a href="/docs/linux/man/8-runc-delete/">runc-delete</a></code>(8), <code><a href="/docs/linux/man/8-runc-events/">runc-events</a></code>(8), <code><a href="/docs/linux/man/8-runc-exec/">runc-exec</a></code>(8), <code><a href="/docs/linux/man/8-runc-kill/">runc-kill</a></code>(8), <code><a href="/docs/linux/man/8-runc-list/">runc-list</a></code>(8), <code><a href="/docs/linux/man/8-runc-pause/">runc-pause</a></code>(8), <code><a href="/docs/linux/man/8-runc-ps/">runc-ps</a></code>(8), <code><a href="/docs/linux/man/8-runc-restore/">runc-restore</a></code>(8), <code><a href="/docs/linux/man/8-runc-resume/">runc-resume</a></code>(8), <code><a href="/docs/linux/man/8-runc-run/">runc-run</a></code>(8), <code><a href="/docs/linux/man/8-runc-spec/">runc-spec</a></code>(8), <code><a href="/docs/linux/man/8-runc-start/">runc-start</a></code>(8), <code><a href="/docs/linux/man/8-runc-state/">runc-state</a></code>(8), <code><a href="/docs/linux/man/8-runc-update/">runc-update</a></code>(8). </p>
