---
title: "docker-container-commit(1)"
name: "docker-container-commit"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-container-commit/"
description: "docker-container-commit – Create a new image from a container’s changes"
---

<h2 class="name">NAME</h2>
<p> docker-container-commit &#8211; Create a new image from a container&#8217;s changes </p>
<h2>SYNOPSIS</h2>
<p> <code>docker container commit [OPTIONS] CONTAINER [REPOSITORY[:TAG]]</code> </p>
<h2>DESCRIPTION</h2>
<p> Create a new image from an existing container specified by name or container ID. The new image will contain the contents of the container filesystem, <i>excluding</i> any data volumes. Refer to <code><a href="/docs/linux/man/1-docker-tag/">docker-tag</a>(1)</code> for more information about valid image and tag names. </p>
<p> While the docker commit command is a convenient way of extending an existing image, you should prefer the use of a Dockerfile and docker build for generating images that you intend to share with other people. </p>
<h2>EXAMPLES</h2>
<h2>Creating a new image from an existing container</h2>
<p> An existing Fedora based container has had Apache installed while running in interactive mode with the bash shell. Apache is also running. To create a new image run docker ps to find the container&#8217;s ID and then run: </p>
<dl>
<dt>
<dd>
<pre>
$ docker commit -m=&quot;Added Apache to Fedora base image&quot; \
  -a=&quot;A D Ministrator&quot; 98bd7fc99854 fedora/fedora_httpd:20
</pre>
</dl>
<p> Note that only a-z0-9-_. are allowed when naming images from an existing container. </p>
<h2>Apply specified Dockerfile instructions while committing the image</h2>
<p> If an existing container was created without the DEBUG environment variable set to &quot;true&quot;, you can create a new image based on that container by first getting the container&#8217;s ID with docker ps and then running: </p>
<dl>
<dt>
<dd>
<pre>
$ docker container commit -c=&quot;ENV DEBUG=true&quot; 98bd7fc99854 debug-image
</pre>
</dl>
<h2>OPTIONS</h2>
<p> <code>-a</code>, <code>&#8211;author</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Author (e.g., &quot;John Hannibal Smith hannibal [at] a-team.com<br />
 &lt;mailto:hannibal [at] a-team.com&gt;&quot;) </p>
<p> <code>-c</code>, <code>&#8211;change</code>= <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Apply Dockerfile instruction to the created image</p>
<p> <code>-h</code>, <code>&#8211;help</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>help for commit</p>
<p> <code>-m</code>, <code>&#8211;message</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Commit message</p>
<p> <code>-p</code>, <code>&#8211;pause</code>[=true] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Pause container during commit</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-docker-container/">docker-container</a>(1)</code> </p>
<h2>Index</h2>
