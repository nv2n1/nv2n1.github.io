---
title: "docker-latest-save(1)"
name: "docker-latest-save"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-latest-save/"
description: "docker-save – Save one or more images to a tar archive (streamed to STDOUT by default)"
---

<h2 class="name">NAME</h2>
<p> docker-save &#8211; Save one or more images to a tar archive (streamed to STDOUT by default) </p>
<h2>SYNOPSIS</h2>
<p> <code>docker save</code> [<code>&#8211;help</code>] [<code>-o</code>|<code>&#8211;output</code>[=<i>OUTPUT</i>]] IMAGE [IMAGE&#8230;] </p>
<h2>DESCRIPTION</h2>
<p> Produces a tarred repository to the standard output stream. Contains all parent layers, and all tags + versions, or specified repo:tag. </p>
<p> Stream to a file instead of STDOUT by using <code>-o</code>. </p>
<h2>OPTIONS</h2>
<p> <code>&#8211;help</code><br />
&nbsp;<wbr>&nbsp;<wbr>Print usage statement </p>
<p> <code>-o</code>, <code>&#8211;output</code>=&quot;&quot;<br />
Write to a file, instead of STDOUT </p>
<h2>EXAMPLES</h2>
<p> Save all fedora repository images to a fedora-all.tar and save the latest fedora image to a fedora-latest.tar: </p>
<dl>
<dt>
<dd>
<pre>
$ docker save fedora &gt; fedora-all.tar
$ docker save --output=fedora-latest.tar fedora:latest
$ ls -sh fedora-all.tar
721M fedora-all.tar
$ ls -sh fedora-latest.tar
367M fedora-latest.tar
</pre>
</dl>
<h2>See also</h2>
<p> <code><a href="/docs/linux/man/1-docker-load/">docker-load</a>(1)</code> to load an image from a tar archive on STDIN. </p>
<h2>HISTORY</h2>
<p> April 2014, Originally compiled by William Henry (whenry at redhat dot com) based on docker.com source material and internal work. June 2014, updated by Sven Dowideit &lt;SvenDowideit [at] home.org.au&gt; November 2014, updated by Sven Dowideit &lt;SvenDowideit [at] home.org.au&gt; </p>
<h2>Index</h2>
