---
title: "packf(1)"
name: "packf"
section: "1"
letter: "p"
url: "/docs/linux/man/1-packf/"
description: "packf – pack messages in nmh folder into a single file"
---

<h2 class="name">NAME</h2>
<p> packf &#8211; pack messages in nmh folder into a single file </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>packf</code> [<i>+folder</i>] [<i>msgs</i>] [<code>-file</code> <i>name</i>] [<code>-mbox</code>] [<code>-mmdf</code>] [<code>-version</code>] [<code>-help</code>]</dl>
<h2>DESCRIPTION</h2>
<p> <code>Packf</code></p>
<dd>will pack copies of messages from a folder, into a single file. </p>
<p> If the <code>-mbox</code> switch is given (the default), then the messages are separated using mbox (uucp) style delimiters. This is the format used by most mail clients (elm, mailx, etc.). </p>
<p> If the <code>-mmdf</code> switch is given, then the messages are separated by mmdf style delimiters. Each message in the file is separated by four CTRL-A&#8217;s and a newline. </p>
<p> You may specify the name of the file in which to use with the <code>-file</code> <i>name</i> switch. If you do not specify the name of the file, it will default to &#8220;<i>msgbox</i>&#8221;. </p>
<p> If the given file name points to an existing file, then the specified messages will be appended to the end of the file, otherwise the file will be created and the messages appended. </p>
<p> <code>packf</code> makes an mbox-style delimiter by examining the first line of the message. If the first line is a &#8220;Return-Path&#8221; field, its address and the current date and time are used. Otherwise, if the first line has an &#8220;X-Envelope-From&#8221; field, its contents (which should already be in the correct format) are used. Otherwise, a dummy address and the current date and time are used. </p>
<p> Messages that are packed by <code>packf</code> can be unpacked using <code>inc</code>.</p>
<h2>FILES</h2>
<pre>
^$HOME/.mh_profile~^The user profile
^.msgbox.map~^A binary index of the file
</pre>
<h2>PROFILE COMPONENTS</h2>
<pre>
^Path:~^To determine the user's nmh directory
^Current-Folder:~^To find the default current folder
^Msg-Protect:~^To set mode when creating a new `file'
</pre>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-inc/">inc</a></i>(1), <i><a href="/docs/linux/man/1-msh/">msh</a></i>(1)</p>
<h2>DEFAULTS</h2>
<pre>
`<code>+folder</code>' defaults to the current folder
`<code>msgs</code>' defaults to all
`<code>-mbox</code>'
`<code>-file ./msgbox</code>'
</pre>
<h2>CONTEXT</h2>
<p> If a folder is given, it will become the current folder. The first message packed will become the current message. </p>
<h2>Index</h2>
