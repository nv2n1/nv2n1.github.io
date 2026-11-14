---
title: "docker-latest-rmi(1)"
name: "docker-latest-rmi"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-latest-rmi/"
description: "docker-rmi – Remove one or more images"
---

<h2 class="name">NAME</h2>
<p> docker-rmi &#8211; Remove one or more images </p>
<h2>SYNOPSIS</h2>
<p> <code>docker rmi</code> [<code>-f</code>|<code>&#8211;force</code>] [<code>&#8211;help</code>] [<code>&#8211;no-prune</code>] IMAGE [IMAGE&#8230;] </p>
<h2>DESCRIPTION</h2>
<p> Removes one or more images from the host node. This does not remove images from a registry. You cannot remove an image of a running container unless you use the <code>-f</code> option. To see all images on a host use the <code>docker images</code> command. </p>
<h2>OPTIONS</h2>
<p> <code>-f</code>, <code>&#8211;force</code>=<i>true</i>|<i>false</i><br />
Force removal of the image. The default is&nbsp;<wbr><i>false</i>. </p>
<p> <code>&#8211;help</code><br />
&nbsp;<wbr>&nbsp;<wbr>Print usage statement </p>
<p> <code>&#8211;no-prune</code>=<i>true</i>|<i>false</i><br />
Do not delete untagged parents. The default is&nbsp;<wbr><i>false</i>. </p>
<h2>EXAMPLES</h2>
<h2>Removing an image</h2>
<p> Here is an example of removing an image: </p>
<dl>
<dt>
<dd>
<pre>
docker rmi fedora/httpd
</pre>
</dl>
<h2>HISTORY</h2>
<p> April 2014, Originally compiled by William Henry (whenry at redhat dot com) based on docker.com source material and internal work. June 2014, updated by Sven Dowideit &lt;SvenDowideit [at] home.org.au&gt; April 2015, updated by Mary Anthony for v2 &lt;mary [at] docker.com&gt; </p>
<h2>Index</h2>
