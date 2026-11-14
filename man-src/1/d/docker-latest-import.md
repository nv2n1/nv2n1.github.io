---
title: "docker-latest-import(1)"
name: "docker-latest-import"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-latest-import/"
description: "docker-import – Create an empty filesystem image and import the contents of the tarball (.tar, .tar.gz, .tgz, .bzip, .tar.xz, .txz) into it, then optionally tag it."
---

<h2 class="name">NAME</h2>
<p> docker-import &#8211; Create an empty filesystem image and import the contents of the tarball (.tar, .tar.gz, .tgz, .bzip, .tar.xz, .txz) into it, then optionally tag it. </p>
<h2>SYNOPSIS</h2>
<p> <code>docker import</code> [<code>-c</code>|<code>&#8211;change</code>[=<i>[]</i>]] [<code>-m</code>|<code>&#8211;message</code>[=<i>MESSAGE</i>]] [<code>&#8211;help</code>] file|URL|<code>&#8211;</code>[REPOSITORY[:TAG]] </p>
<h2>OPTIONS</h2>
<p> <code>-c</code>, <code>&#8211;change</code>=[]<br />
Apply specified Dockerfile instructions while importing the image<br />
Supported Dockerfile instructions: CMD|ENTRYPOINT|ENV|EXPOSE|ONBUILD|USER|VOLUME|WORKDIR </p>
<p> <code>&#8211;help</code><br />
&nbsp;<wbr>&nbsp;<wbr>Print usage statement </p>
<p> <code>-m</code>, <code>&#8211;message</code>=&quot;&quot;<br />
Set commit message for imported image </p>
<h2>DESCRIPTION</h2>
<p> Create a new filesystem image from the contents of a tarball (.tar, .tar.gz, .tgz, .bzip, .tar.xz, .txz) into it, then optionally tag it. </p>
<h2>EXAMPLES</h2>
<h2>Import from a remote location</h2>
<dl>
<dt>
<dd>
<pre>
# docker import <a rel="nofollow" href="http://example.com/exampleimage.tgz">http://example.com/exampleimage.tgz</a> example/imagerepo
</pre>
</dl>
<h2>Import from a local file</h2>
<p> Import to docker via pipe and stdin: </p>
<dl>
<dt>
<dd>
<pre>
# cat exampleimage.tgz | docker import - example/imagelocal
</pre>
</dl>
<p> Import with a commit message. </p>
<dl>
<dt>
<dd>
<pre>
# cat exampleimage.tgz | docker import --message &quot;New image imported from tarball&quot; - exampleimagelocal:new
</pre>
</dl>
<p> Import to a Docker image from a local file. </p>
<dl>
<dt>
<dd>
<pre>
# docker import /path/to/exampleimage.tgz 
</pre>
</dl>
<h2>Import from a local file and tag</h2>
<p> Import to docker via pipe and stdin: </p>
<dl>
<dt>
<dd>
<pre>
# cat exampleimageV2.tgz | docker import - example/imagelocal:V-2.0
</pre>
</dl>
<h2>Import from a local directory</h2>
<dl>
<dt>
<dd>
<pre>
# tar -c . | docker import - exampleimagedir
</pre>
</dl>
<h2>Apply specified Dockerfile instructions while importing the image</h2>
<p> This example sets the docker image ENV variable DEBUG to true by default. </p>
<dl>
<dt>
<dd>
<pre>
# tar -c . | docker import -c=&quot;ENV DEBUG true&quot; - exampleimagedir
</pre>
</dl>
<h2>See also</h2>
<p> <code><a href="/docs/linux/man/1-docker-export/">docker-export</a>(1)</code> to export the contents of a filesystem as a tar archive to STDOUT. </p>
<h2>HISTORY</h2>
<p> April 2014, Originally compiled by William Henry (whenry at redhat dot com) based on docker.com source material and internal work. June 2014, updated by Sven Dowideit &lt;SvenDowideit [at] home.org.au&gt; </p>
<h2>Index</h2>
