---
title: "docker-container-attach(1)"
name: "docker-container-attach"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-container-attach/"
description: "docker-container-attach – Attach local standard input, output, and error streams to a running container"
---

<h2 class="name">NAME</h2>
<p> docker-container-attach &#8211; Attach local standard input, output, and error streams to a running container </p>
<h2>SYNOPSIS</h2>
<p> <code>docker container attach [OPTIONS] CONTAINER</code> </p>
<h2>DESCRIPTION</h2>
<p> The <code>docker attach</code> command allows you to attach to a running container using the container&#8217;s ID or name, either to view its ongoing output or to control it interactively. You can attach to the same contained process multiple times simultaneously, screen sharing style, or quickly view the progress of your detached process. </p>
<p> To stop a container, use CTRL-c. This key sequence sends SIGKILL to the container. You can detach from the container (and leave it running) using a configurable key sequence. The default sequence is CTRL-p CTRL-q. You configure the key sequence using the <code>&#8211;detach-keys</code> option or a configuration file. See <code><a href="/docs/linux/man/5-config-json/">config-json</a>(5)</code> for documentation on using a configuration file. </p>
<p> It is forbidden to redirect the standard input of a docker attach command while attaching to a tty-enabled container (i.e.: launched with -t). </p>
<h2>Override the detach sequence</h2>
<p> If you want, you can configure an override the Docker key sequence for detach. This is useful if the Docker default sequence conflicts with key sequence you use for other applications. There are two ways to define your own detach key sequence, as a per-container override or as a configuration property on your entire configuration. </p>
<p> To override the sequence for an individual container, use the &#8211;detach-keys=&quot;&lt;sequence&gt;&quot; flag with the docker attach command. The format of the &lt;sequence&gt; is either a letter [a-Z], or the ctrl- combined with any of the following: </p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> a-z (a single lowercase alpha character )</p>
<dt>&bull;</p>
<dd> @ (at sign)</p>
<dt>&bull;</p>
<dd> [ (left bracket)</p>
<dt>&bull;</p>
<dd> \ (two backward slashes)</p>
<dt>&bull;</p>
<dd> _ (underscore)</p>
<dt>&bull;</p>
<dd> ^ (caret) </p>
</dl>
</dl>
<p> These a, ctrl-a, X, or ctrl-\ values are all examples of valid key sequences. To configure a different configuration default key sequence for all containers, see <code><a href="/docs/linux/man/1-docker/">docker</a>(1)</code>. </p>
<h2>EXAMPLES</h2>
<h2>Attaching to a container</h2>
<p> In this example the top command is run inside a container, from an image called fedora, in detached mode. The ID from the container is passed into the <code>docker attach</code> command: </p>
<dl>
<dt>
<dd>
<pre>
$ ID=$(sudo docker run -d fedora /usr/bin/top -b)
$ sudo docker attach $ID
top - 02:05:52 up  3:05,  0 users,  load average: 0.01, 0.02, 0.05
Tasks:   1 total,   1 running,   0 sleeping,   0 stopped,   0 zombie
Cpu(s):  0.1%us,  0.2%sy,  0.0%ni, 99.7%id,  0.0%wa,  0.0%hi,  0.0%si,  0.0%st
Mem:    373572k total,   355560k used,    18012k free,    27872k buffers
Swap:   786428k total,        0k used,   786428k free,   221740k cached
PID USER      PR  NI  VIRT  RES  SHR S %CPU %MEM    TIME+  COMMAND
1 root      20   0 17200 1116  912 R    0  0.3   0:00.03 top
top - 02:05:55 up  3:05,  0 users,  load average: 0.01, 0.02, 0.05
Tasks:   1 total,   1 running,   0 sleeping,   0 stopped,   0 zombie
Cpu(s):  0.0%us,  0.2%sy,  0.0%ni, 99.8%id,  0.0%wa,  0.0%hi,  0.0%si,  0.0%st
Mem:    373572k total,   355244k used,    18328k free,    27872k buffers
Swap:   786428k total,        0k used,   786428k free,   221776k cached
PID USER      PR  NI  VIRT  RES  SHR S %CPU %MEM    TIME+  COMMAND
1 root      20   0 17208 1144  932 R    0  0.3   0:00.03 top
</pre>
</dl>
<h2>OPTIONS</h2>
<p> <code>&#8211;detach-keys</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Override the key sequence for detaching a container</p>
<p> <code>-h</code>, <code>&#8211;help</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>help for attach</p>
<p> <code>&#8211;no-stdin</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Do not attach STDIN</p>
<p> <code>&#8211;sig-proxy</code>[=true] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Proxy all received signals to the process</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-docker-container/">docker-container</a>(1)</code> </p>
<h2>Index</h2>
