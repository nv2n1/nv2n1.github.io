---
title: "docker-latest-exec(1)"
name: "docker-latest-exec"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-latest-exec/"
description: "docker-exec – Run a command in a running container"
---

<h2 class="name">NAME</h2>
<p> docker-exec &#8211; Run a command in a running container </p>
<h2>SYNOPSIS</h2>
<p> <code>docker exec</code> [<code>-d</code>|<code>&#8211;detach</code>] [<code>&#8211;detach-keys</code>[=<i>[]</i>]] [<code>&#8211;help</code>] [<code>-i</code>|<code>&#8211;interactive</code>] [<code>&#8211;privileged</code>] [<code>-t</code>|<code>&#8211;tty</code>] [<code>-u</code>|<code>&#8211;user</code>[=<i>USER</i>]] CONTAINER COMMAND [ARG&#8230;] </p>
<h2>DESCRIPTION</h2>
<p> Run a process in a running container. </p>
<p> The command started using docker exec will only run while the container&#8217;s primary process (PID 1) is running, and will not be restarted if the container is restarted. </p>
<p> If the container is paused, then the docker exec command will wait until the container is unpaused, and then run </p>
<h2>OPTIONS</h2>
<p> <code>-d</code>, <code>&#8211;detach</code>=<i>true</i>|<i>false</i><br />
Detached mode: run command in the background. The default is&nbsp;<wbr><i>false</i>. </p>
<p> <code>&#8211;detach-keys</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>Override the key sequence for detaching a container. Format is a single character&nbsp;<wbr>[a-Z]&nbsp;<wbr>or ctrl-&lt;value&gt;&nbsp;<wbr>where&nbsp;<wbr>&lt;value&gt;&nbsp;<wbr>is one of: a-z,&nbsp;<wbr>@,&nbsp;<wbr>^,&nbsp;<wbr>[, , or&nbsp;<wbr>_. </p>
<p> <code>&#8211;help</code><br />
&nbsp;<wbr>&nbsp;<wbr>Print usage statement </p>
<p> <code>-i</code>, <code>&#8211;interactive</code>=<i>true</i>|<i>false</i><br />
Keep STDIN open even if not attached. The default is&nbsp;<wbr><i>false</i>. </p>
<p> <code>&#8211;privileged</code>=<i>true</i>|<i>false</i><br />
Give the process extended&nbsp;<wbr> &lt;<a rel="nofollow" href="http://man7.org/linux/man-pages/man7/capabilities.7.html">http://man7.org/linux/man-pages/man7/capabilities.7.html</a>&gt; when running in a container. The default is <i>false</i>. </p>
<p> Without this flag, the process run by docker exec in a running container has the same capabilities as the container, which may be limited. Set &#8211;privileged to give all capabilities to the process. </p>
<p> <code>-t</code>, <code>&#8211;tty</code>=<i>true</i>|<i>false</i><br />
Allocate a pseudo-TTY. The default is&nbsp;<wbr><i>false</i>. </p>
<p> <code>-u</code>, <code>&#8211;user</code>=&quot;&quot;<br />
Sets the username or UID used and optionally the groupname or GID for the specified command. </p>
<p> The followings examples are all valid:<br />
&#8211;user&nbsp;<wbr>[user | user:group | uid | uid:gid | user:gid | uid:group&nbsp;<wbr>] </p>
<p> Without this argument the command will be run as root in the container. </p>
<p> The <code>-t</code> option is incompatible with a redirection of the docker client standard input. </p>
<h2>HISTORY</h2>
<p> November 2014, updated by Sven Dowideit &lt;SvenDowideit [at] home.org.au&gt; </p>
<h2>Index</h2>
