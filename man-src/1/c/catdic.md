---
title: "catdic(1)"
name: "catdic"
section: "1"
letter: "c"
url: "/docs/linux/man/1-catdic/"
description: "catdic – Download a dictionary"
---

<h2>NAME</h2>
<p> catdic &#8211; Download a dictionary</p>
<h2>SYNOPSIS</h2>
<p> <code>catdic [{-cs|-cannaserver} </code><i>canna-server</i>] [-i|-u <i>user-name</i>] <i>remote-dic</i> [-l <i>local-file</i>]</p>
<h2>DESCRIPTION</h2>
<p> catdic downloads a dictionary file to the current directory. The file downloaded is a dictionary file the dictionary name of which is <i>remote-dic</i>. It is in the user dictionary directory of the machine on which <i><a href="//www.systutorials.com/docs/linux/man/1M-cannaserver/">cannaserver</a></i>(1M) is in operation. (Hereafter, this machine is called the remote host.)</p>
<h2>OPTIONS</h2>
<dl>
<dt>-cs <i>canna-server</i> (or -cannaserver <i>canna-server</i>)</p>
<dd> Specifies the name of the server machine that contains a dictionary to be downloaded.</p>
<dt>-i</p>
<dd> Downloads the system dictionary.</p>
<dt>-u <i>user-name</i></p>
<dd> Specifies the user name. Another user&#8217;s dictionary can be referenced by this user name.</p>
<dt>-l <i>local-file</i></p>
<dd> <i>local-file</i> is the dictionary file name. If it is omitted, the standard output will be assumed.</dl>
<h2>EXAMPLES</h2>
<pre>
  % catdic test
</pre>
<p> Outputs the contents of dictionary file &#8220;test&#8221; on the remote host, to the standard output. </p>
<pre>
  % catdic test -l test2.t
</pre>
<p> Downloads dictionary file &#8220;test&#8221; on the remote host to current directory file &#8220;test2.t&#8221;.</p>
<h2>SEE ALSO</h2>
<p> <a href="//www.systutorials.com/docs/linux/man/1M-cannaserver/">cannaserver</a>(1M), <a href="/docs/linux/man/1-lsdic/">lsdic</a>(1), <a href="/docs/linux/man/1-mkdic/">mkdic</a>(1) </p>
<h2>Index</h2>
