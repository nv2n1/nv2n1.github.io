---
title: "docker-container-exec(1)"
name: "docker-container-exec"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-container-exec/"
description: "docker-container-exec – Run a command in a running container"
---

<h2 class="name">NAME</h2>
<p> docker-container-exec &#8211; Run a command in a running container </p>
<h2>SYNOPSIS</h2>
<p> <code>docker container exec [OPTIONS] CONTAINER COMMAND [ARG&#8230;]</code> </p>
<h2>DESCRIPTION</h2>
<p> Run a process in a running container. </p>
<p> The command started using docker exec will only run while the container&#8217;s primary process (PID 1) is running, and will not be restarted if the container is restarted. </p>
<p> If the container is paused, then the docker exec command will wait until the container is unpaused, and then run </p>
<h2>CAPABILITIES</h2>
<p> privileged gives the process extended Linux capabilities &lt;<a rel="nofollow" href="http://man7.org/linux/man-pages/man7/capabilities.7.html">http://man7.org/linux/man-pages/man7/capabilities.7.html</a>&gt; when running in a container. </p>
<p> Without this flag, the process run by docker exec in a running container has the same capabilities as the container, which may be limited. Set &#8211;privileged to give all capabilities to the process. </p>
<h2>USER</h2>
<p> user sets the username or UID used and optionally the groupname or GID for the specified command. </p>
<p> The followings examples are all valid:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211;user&nbsp;[user | user:group | uid | uid:gid | user:gid | uid:group&nbsp;] </p>
<p> Without this argument the command will be run as root in the container. </p>
<h2>Exit Status</h2>
<p> The exit code from docker exec gives information about why the container failed to exec or why it exited. When docker exec exits with a non-zero code, the exit codes follow the chroot standard, see below: </p>
<p> <i>126</i> if the <i>contained command</i> cannot be invoked </p>
<dl>
<dt>
<dd>
<pre>
$ docker exec busybox /etc; echo $?
# exec: &quot;/etc&quot;: permission denied
  docker: Error response from daemon: Contained command could not be invoked
  126
</pre>
</dl>
<p> <i>127</i> if the <i>contained command</i> cannot be found </p>
<dl>
<dt>
<dd>
<pre>
$ docker exec busybox foo; echo $?
# exec: &quot;foo&quot;: executable file not found in $PATH
  docker: Error response from daemon: Contained command not found or does not exist
  127
</pre>
</dl>
<p> <i>Exit code</i> of <i>contained command</i> otherwise </p>
<dl>
<dt>
<dd>
<pre>
$ docker exec busybox /bin/sh -c 'exit 3' 
# 3
</pre>
</dl>
<h2>OPTIONS</h2>
<p> <code>-d</code>, <code>&#8211;detach</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Detached mode: run command in the background</p>
<p> <code>&#8211;detach-keys</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Override the key sequence for detaching a container</p>
<p> <code>-e</code>, <code>&#8211;env</code>= <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Set environment variables</p>
<p> <code>&#8211;env-file</code>= <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Read in a file of environment variables</p>
<p> <code>-h</code>, <code>&#8211;help</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>help for exec</p>
<p> <code>-i</code>, <code>&#8211;interactive</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Keep STDIN open even if not attached</p>
<p> <code>&#8211;privileged</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Give extended privileges to the command</p>
<p> <code>-t</code>, <code>&#8211;tty</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Allocate a pseudo-TTY</p>
<p> <code>-u</code>, <code>&#8211;user</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Username or UID (format: [:])</p>
<p> <code>-w</code>, <code>&#8211;workdir</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Working directory inside the container</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-docker-container/">docker-container</a>(1)</code> </p>
<h2>Index</h2>
