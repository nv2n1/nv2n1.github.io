---
title: "docker-exec(1)"
name: "docker-exec"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-exec/"
description: "docker-exec – Run a command in a running container"
---

<h2 class="name">NAME</h2>
<p> docker-exec &#8211; Run a command in a running container </p>
<h2>SYNOPSIS</h2>
<p> <code>docker exec [OPTIONS] CONTAINER COMMAND [ARG&#8230;]</code> </p>
<h2>DESCRIPTION</h2>
<p> Alias for docker container exec. </p>
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
<p> <code><a href="/docs/linux/man/1-docker/">docker</a>(1)</code> </p>
<h2>Index</h2>
