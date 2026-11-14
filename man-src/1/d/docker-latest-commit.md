---
title: "docker-latest-commit(1)"
name: "docker-latest-commit"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-latest-commit/"
description: "docker-commit – Create a new image from a container’s changes"
---

<h2 class="name">NAME</h2>
<p> docker-commit &#8211; Create a new image from a container&#8217;s changes </p>
<h2>SYNOPSIS</h2>
<p> <code>docker commit</code> [<code>-a</code>|<code>&#8211;author</code>[=<i>AUTHOR</i>]] [<code>-c</code>|<code>&#8211;change</code>[=[<i>DOCKERFILE INSTRUCTIONS</i>]]] [<code>&#8211;help</code>] [<code>-m</code>|<code>&#8211;message</code>[=<i>MESSAGE</i>]] [<code>-p</code>|<code>&#8211;pause</code>[=<i>true</i>]] CONTAINER [REPOSITORY[:TAG]] </p>
<h2>DESCRIPTION</h2>
<p> Create a new image from an existing container specified by name or container ID. The new image will contain the contents of the container filesystem, <i>excluding</i> any data volumes. Refer to <code><a href="/docs/linux/man/1-docker-tag/">docker-tag</a>(1)</code> for more information about valid image and tag names. </p>
<p> While the docker commit command is a convenient way of extending an existing image, you should prefer the use of a Dockerfile and docker build for generating images that you intend to share with other people. </p>
<h2>OPTIONS</h2>
<p> <code>-a</code>, <code>&#8211;author</code>=&quot;&quot;<br />
Author&nbsp;<wbr>(e.g.,&nbsp;<wbr>&quot;John Hannibal Smith&nbsp;<wbr> &lt;hannibal [at] a-team.com&gt;&quot;) </p>
<p> <code>-c</code> , <code>&#8211;change</code>=[]<br />
Apply specified Dockerfile instructions while committing the image<br />
Supported Dockerfile instructions: CMD|ENTRYPOINT|ENV|EXPOSE|LABEL|ONBUILD|USER|VOLUME|WORKDIR </p>
<p> <code>&#8211;help</code><br />
&nbsp;<wbr>&nbsp;<wbr>Print usage statement </p>
<p> <code>-m</code>, <code>&#8211;message</code>=&quot;&quot;<br />
Commit message </p>
<p> <code>-p</code>, <code>&#8211;pause</code>=<i>true</i>|<i>false</i><br />
Pause container during commit. The default is&nbsp;<wbr><i>true</i>. </p>
<h2>EXAMPLES</h2>
<h2>Creating a new image from an existing container</h2>
<p> An existing Fedora based container has had Apache installed while running in interactive mode with the bash shell. Apache is also running. To create a new image run docker ps to find the container&#8217;s ID and then run: </p>
<dl>
<dt>
<dd>
<pre>
# docker commit -m=&quot;Added Apache to Fedora base image&quot; \
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
# docker commit -c=&quot;ENV DEBUG true&quot; 98bd7fc99854 debug-image
</pre>
</dl>
<h2>HISTORY</h2>
<p> April 2014, Originally compiled by William Henry (whenry at redhat dot com) based on docker.com source material and in June 2014, updated by Sven Dowideit &lt;SvenDowideit [at] home.org.au&gt; July 2014, updated by Sven Dowideit &lt;SvenDowideit [at] home.org.au&gt; Oct 2014, updated by Daniel, Dao Quang Minh &lt;daniel at nitrous dot io&gt; June 2015, updated by Sally O&#8217;Malley &lt;somalley [at] redhat.com&gt; </p>
<h2>Index</h2>
