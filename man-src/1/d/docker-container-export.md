---
title: "docker-container-export(1)"
name: "docker-container-export"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-container-export/"
description: "docker-container-export – Export a container’s filesystem as a tar archive"
---

<h2 class="name">NAME</h2>
<p> docker-container-export &#8211; Export a container&#8217;s filesystem as a tar archive </p>
<h2>SYNOPSIS</h2>
<p> <code>docker container export [OPTIONS] CONTAINER</code> </p>
<h2>DESCRIPTION</h2>
<p> Export the contents of a container&#8217;s filesystem using the full or shortened container ID or container name. The output is exported to STDOUT and can be redirected to a tar file. </p>
<p> Stream to a file instead of STDOUT by using <code>-o</code>. </p>
<h2>EXAMPLES</h2>
<p> Export the contents of the container called angry_bell to a tar file called angry_bell.tar: </p>
<dl>
<dt>
<dd>
<pre>
$ docker export angry_bell &gt; angry_bell.tar
$ docker export --output=angry_bell-latest.tar angry_bell
$ ls -sh angry_bell.tar
321M angry_bell.tar
$ ls -sh angry_bell-latest.tar
321M angry_bell-latest.tar
</pre>
</dl>
<h2>See also</h2>
<p> <code><a href="/docs/linux/man/1-docker-import/">docker-import</a>(1)</code> to create an empty filesystem image and import the contents of the tarball into it, then optionally tag it. </p>
<h2>OPTIONS</h2>
<p> <code>-h</code>, <code>&#8211;help</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>help for export</p>
<p> <code>-o</code>, <code>&#8211;output</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Write to a file, instead of STDOUT</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-docker-container/">docker-container</a>(1)</code> </p>
<h2>Index</h2>
