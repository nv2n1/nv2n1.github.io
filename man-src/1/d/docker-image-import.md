---
title: "docker-image-import(1)"
name: "docker-image-import"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-image-import/"
description: "docker-image-import – Import the contents from a tarball to create a filesystem image"
---

<h2 class="name">NAME</h2>
<p> docker-image-import &#8211; Import the contents from a tarball to create a filesystem image </p>
<h2>SYNOPSIS</h2>
<p> <code>docker image import [OPTIONS] file|URL|- [REPOSITORY[:TAG]]</code> </p>
<h2>DESCRIPTION</h2>
<p> Create a new filesystem image from the contents of a tarball (.tar, .tar.gz, .tgz, .bzip, .tar.xz, .txz) into it, then optionally tag it. </p>
<h2>EXAMPLES</h2>
<h2>Import from a remote location</h2>
<dl>
<dt>
<dd>
<pre>
# docker image import <a rel="nofollow" href="http://example.com/exampleimage.tgz">http://example.com/exampleimage.tgz</a> example/imagerepo
</pre>
</dl>
<h2>Import from a local file</h2>
<p> Import to docker via pipe and stdin: </p>
<dl>
<dt>
<dd>
<pre>
# cat exampleimage.tgz | docker image import - example/imagelocal
</pre>
</dl>
<p> Import with a commit message. </p>
<dl>
<dt>
<dd>
<pre>
# cat exampleimage.tgz | docker image import --message &quot;New image imported from tarball&quot; - exampleimagelocal:new
</pre>
</dl>
<p> Import to a Docker image from a local file. </p>
<dl>
<dt>
<dd>
<pre>
# docker image import /path/to/exampleimage.tgz 
</pre>
</dl>
<h2>Import from a local file and tag</h2>
<p> Import to docker via pipe and stdin: </p>
<dl>
<dt>
<dd>
<pre>
# cat exampleimageV2.tgz | docker image import - example/imagelocal:V-2.0
</pre>
</dl>
<h2>Import from a local directory</h2>
<dl>
<dt>
<dd>
<pre>
# tar -c . | docker image import - exampleimagedir
</pre>
</dl>
<h2>Apply specified Dockerfile instructions while importing the image</h2>
<p> This example sets the docker image ENV variable DEBUG to true by default. </p>
<dl>
<dt>
<dd>
<pre>
# tar -c . | docker image import -c=&quot;ENV DEBUG=true&quot; - exampleimagedir
</pre>
</dl>
<h2>When the daemon supports multiple operating systems</h2>
<p> If the daemon supports multiple operating systems, and the image being imported does not match the default operating system, it may be necessary to add &#8211;platform. This would be necessary when importing a Linux image into a Windows daemon. </p>
<dl>
<dt>
<dd>
<pre>
# docker image import --platform=linux .\linuximage.tar
</pre>
</dl>
<h2>See also</h2>
<p> <code><a href="/docs/linux/man/1-docker-export/">docker-export</a>(1)</code> to export the contents of a filesystem as a tar archive to STDOUT. </p>
<h2>OPTIONS</h2>
<p> <code>-c</code>, <code>&#8211;change</code>= <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Apply Dockerfile instruction to the created image</p>
<p> <code>-h</code>, <code>&#8211;help</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>help for import</p>
<p> <code>-m</code>, <code>&#8211;message</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Set commit message for imported image</p>
<p> <code>&#8211;platform</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Set platform if server is multi-platform capable</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-docker-image/">docker-image</a>(1)</code> </p>
<h2>Index</h2>
