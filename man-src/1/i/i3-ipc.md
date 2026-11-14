---
title: "i3-ipc(1)"
name: "i3-ipc"
section: "1"
letter: "i"
url: "/docs/linux/man/1-i3-ipc/"
description: "i3-ipc — inter-process communication with i3"
---

<h2>NAME</h2>
<p> <code>i3-ipc</code> &#8212; inter-process communication with i3</p>
<h2>SYNOPSIS</h2>
<p> <code>i3-ipc</code> [<code>-s</code>] [<code>-t type</code>] [<code>-p</code>] [<code>-j</code>] [<code>-q</code>] [<code>message</code>]</p>
<h2>DESCRIPTION</h2>
<p> <code>i3-ipc</code> can be used to communicate with i3, the improved tiling window manager, through the provided ipc socket. Useful for scripting the window manager. Currently implemented message types of i3 are the following:</p>
<dl>
<dt><code>0 (COMMAND)</code></p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>The payload of the message is a command for i3<br />
&nbsp;<wbr>&nbsp;<wbr>(like the commands you can bind to keys in the configuration file)<br />
&nbsp;<wbr>&nbsp;<wbr>The command will be executed directly after receiving it.<br />
&nbsp;<wbr>&nbsp;<wbr>The reply will be always&nbsp;<wbr>{&quot;succes&quot;:true}&nbsp;<wbr>for now.</p>
<dt><code>1 (GET_WORKSPACES)</code></p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>Gets the current workspaces.<br />
&nbsp;<wbr>&nbsp;<wbr>The reply will be a JSON-encoded list of workspaces.</p>
<dt><code>2 (SUBSCRIBE)</code></p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>Subscribes your connection to the&nbsp;<wbr><code>workspace</code>&nbsp;<wbr>event.</p>
<dt><code>3 (GET_OUTPUTS)</code></p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>Gets the current outputs.<br />
&nbsp;<wbr>&nbsp;<wbr>The reply will be a JSON-encoded list of outputs.</dl>
<h2>OPTIONS</h2>
<p> <code>i3-ipc</code>&#8216;s default mode of operation is to send the command (type 0) specified on the command line. These options can be used to change this behavior:</p>
<dl>
<dt><code>-s</code>, <code>&#8211;socket</code></p>
<dd> Set the socket file, defaults to ~/.i3/ipc.sock</p>
<dt><code>-t</code>, <code>&#8211;type</code></p>
<dd> Set the type. Passing a type of 0 is the default and will send the specified command, type 1 gets the current workspace list, type 2 subscribes to the workspace stream, type 3 gets the current output list.</p>
<dt><code>-p</code>, <code>&#8211;pretty-print</code></p>
<dd> This will pretty print the received reply. Useful for the workspace list.</p>
<dt><code>-j</code>, <code>&#8211;json</code></p>
<dd> This will print the received reply as raw json-encoded data. Useful to pass to another script.</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> Turn off the output. Useful for command mode.</p>
<dt><code>message</code></p>
<dd> This is the actual command to send as defined by i3 You may additionally ask for help:</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Print help.</p>
<dt><code>-m</code>, <code>&#8211;man</code></p>
<dd> Display this man page.</dl>
<h2>EXAMPLES</h2>
<pre>
$ i3-ipc -t 1
$ i3-ipc -t 2 -p
$ i3-ipc -t 3 -j
$ i3-ipc &quot;exec xterm&quot;
</pre>
<h2>BUGS</h2>
<p> <i><a rel="nofollow" href="http://github.com/badboy/i3-ipc/issues">http://github.com/badboy/i3-ipc/issues</a></i></p>
<h2>AUTHOR</h2>
<p> Jan-Erik Rediger:: badboy [at] archlinux.us</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-i3/">i3</a>(1), <a href="/docs/linux/man/1-i3-msg/">i3-msg</a>(1), <i><a rel="nofollow" href="http://i3.zekjur.net/">http://i3.zekjur.net/</a></i>, <i><a href="http://github.com/badboy/i3-ipc">http://github.com/badboy/i3-ipc</a></i> </p>
<h2>Index</h2>
