---
title: "docker-image-save(1)"
name: "docker-image-save"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-image-save/"
description: "docker-image-save – Save one or more images to a tar archive (streamed to STDOUT by default)"
---

<h2 class="name">NAME</h2>
<p> docker-image-save &#8211; Save one or more images to a tar archive (streamed to STDOUT by default) </p>
<h2>SYNOPSIS</h2>
<p> <code>docker image save [OPTIONS] IMAGE [IMAGE&#8230;]</code> </p>
<h2>DESCRIPTION</h2>
<p> Produces a tarred repository to the standard output stream. Contains all parent layers, and all tags + versions, or specified repo:tag. </p>
<p> Stream to a file instead of STDOUT by using <code>-o</code>. </p>
<h2>EXAMPLES</h2>
<p> Save all fedora repository images to a fedora-all.tar and save the latest fedora image to a fedora-latest.tar: </p>
<dl>
<dt>
<dd>
<pre>
$ docker image save fedora &gt; fedora-all.tar
$ docker image save --output=fedora-latest.tar fedora:latest
$ ls -sh fedora-all.tar
721M fedora-all.tar
$ ls -sh fedora-latest.tar
367M fedora-latest.tar
</pre>
</dl>
<h2>See also</h2>
<p> <code><a href="/docs/linux/man/1-docker-image-load/">docker-image-load</a>(1)</code> to load an image from a tar archive on STDIN. </p>
<h2>OPTIONS</h2>
<p> <code>-h</code>, <code>&#8211;help</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>help for save</p>
<p> <code>-o</code>, <code>&#8211;output</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Write to a file, instead of STDOUT</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-docker-image/">docker-image</a>(1)</code> </p>
<h2>Index</h2>
