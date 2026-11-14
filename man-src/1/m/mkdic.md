---
title: "mkdic(1)"
name: "mkdic"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mkdic/"
description: "mkdic – Tool for creating a user dictionary"
---

<h2>NAME</h2>
<p> mkdic &#8211; Tool for creating a user dictionary</p>
<h2>SYNOPSIS</h2>
<p> <code>mkdic [{-cs|-cannaserver} </code><i>canna-server</i>] [-s] [- | -l <i>local-file</i>] <i>remote-dic</i></p>
<h2>DESCRIPTION</h2>
<p> mkdic creates user dictionary named <i>remote-dic</i> in the user dictionary directory of the remote host, on which <i><a href="//www.systutorials.com/docs/linux/man/1M-cannaserver/">cannaserver</a></i>(1M) is in operation. Dictionary file name <i>remote-dic</i> is assigned to this file at this time. </p>
<p> If the &#8211; and -l option isn&#8217;t specified, mkdic creates an empty dictionary. </p>
<p> If the &#8211; option is specified, the standard input will be used as the dictionary file. If the -l option is specified, <i>local-file</i> will be used as the dictionary file. </p>
<p> If the user dictionary directory does not exist, it will be created. </p>
<p> Dictionary directory file &#8212; dics.dir &#8212; is rewritten automatically after the registering. The registered dictionary can thus be used by writing the dictionary name into the customize file.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-cs <i>canna-server</i> (or -cannaserver <i>canna-server</i>)</p>
<dd> Specifies the server machine that contains the dictionary to be created.</p>
<dt>-s</p>
<dd> Indicates that the dictionary to be created is an adjunct dictionary. If this option is omitted, the dictionary will be created as an independent-word one.</p>
<dt>-l <i>local-file</i></p>
<dd> Registers the input data from <i>local-file</i>.</p>
<dt>&#8211;</p>
<dd> The standard input will be used as the dictionary file.</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>(1)</p>
<dd> If you want to creat an empty dictionary file: </p>
<pre>
  % mkdic test
</pre>
<dt>(2)</p>
<dd> If you want to register the input data from the standard input: </p>
<pre>
  % mkdic test -
</pre>
</dl>
<p> Registers the input data from the standard input, in the user dictionary directory under dictionary name &#8220;test&#8221;. The following line is then added to dictionary directory file &#8212; dics.dir &#8212; : </p>
<pre>
          user1.t(.mwd) -test-
</pre>
<dl>
<dt>(3)</p>
<dd> If the dictionary file is specified: </p>
<pre>
  % mkdic test -l test1.t
</pre>
</dl>
<p> Registers independent-word dictionary file &#8220;test1.t&#8221; in the remote host&#8217;s user dictionary directory under dictionary name &#8220;test&#8221;. The following line is then added to dics.dir: </p>
<pre>
         user1.t(.mvd) -test-
</pre>
<p> user1.t is a dictionary file name generated automatically by the system.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-catdic/">catdic</a>(1), <a href="//www.systutorials.com/docs/linux/man/1M-cannaserver/">cannaserver</a>(1M), <a href="/docs/linux/man/1-lsdic/">lsdic</a>(1) </p>
<h2>Index</h2>
