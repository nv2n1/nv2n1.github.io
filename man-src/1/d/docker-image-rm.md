---
title: "docker-image-rm(1)"
name: "docker-image-rm"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-image-rm/"
description: "docker-image-rm – Remove one or more images"
---

<h2 class="name">NAME</h2>
<p> docker-image-rm &#8211; Remove one or more images </p>
<h2>SYNOPSIS</h2>
<p> <code>docker image rm [OPTIONS] IMAGE [IMAGE&#8230;]</code> </p>
<h2>DESCRIPTION</h2>
<p> Removes (and un-tags) one or more images from the host node. If an image has multiple tags, using this command with the tag as a parameter only removes the tag. If the tag is the only one for the image, both the image and the tag are removed. </p>
<p> This does not remove images from a registry. You cannot remove an image of a running container unless you use the <code>-f</code> option. To see all images on a host use the <code>docker image ls</code> command. </p>
<h2>EXAMPLES</h2>
<h2>Removing an image</h2>
<p> Here is an example of removing an image: </p>
<dl>
<dt>
<dd>
<pre>
docker image rm fedora/httpd
</pre>
</dl>
<h2>OPTIONS</h2>
<p> <code>-f</code>, <code>&#8211;force</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Force removal of the image</p>
<p> <code>-h</code>, <code>&#8211;help</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>help for rm</p>
<p> <code>&#8211;no-prune</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Do not delete untagged parents</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-docker-image/">docker-image</a>(1)</code> </p>
<h2>Index</h2>
