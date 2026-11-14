---
title: "docker-latest-history(1)"
name: "docker-latest-history"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-latest-history/"
description: "docker-history – Show the history of an image"
---

<h2 class="name">NAME</h2>
<p> docker-history &#8211; Show the history of an image </p>
<h2>SYNOPSIS</h2>
<p> <code>docker history</code> [<code>&#8211;help</code>] [<code>-H</code>|<code>&#8211;human</code>[=<i>true</i>]] [<code>&#8211;no-trunc</code>] [<code>-q</code>|<code>&#8211;quiet</code>] IMAGE </p>
<h2>DESCRIPTION</h2>
<p> Show the history of when and how an image was created. </p>
<h2>OPTIONS</h2>
<p> <code>&#8211;help</code><br />
&nbsp;<wbr>&nbsp;<wbr>Print usage statement </p>
<p> <code>-H</code>, <code>&#8211;human</code>=<i>true</i>|<i>false</i><br />
&nbsp;<wbr>Print sizes and dates in human readable format. The default is&nbsp;<wbr><i>true</i>. </p>
<p> <code>&#8211;no-trunc</code>=<i>true</i>|<i>false</i><br />
Don&#8217;t truncate output. The default is&nbsp;<wbr><i>false</i>. </p>
<p> <code>-q</code>, <code>&#8211;quiet</code>=<i>true</i>|<i>false</i><br />
Only show numeric IDs. The default is&nbsp;<wbr><i>false</i>. </p>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd>
<pre>
$ docker history fedora
IMAGE          CREATED          CREATED BY                                      SIZE                COMMENT
105182bb5e8b   5 days ago       /bin/sh -c #(nop) ADD file:71356d2ad59aa3119d   372.7 MB
73bd853d2ea5   13 days ago      /bin/sh -c #(nop) MAINTAINER Lokesh Mandvekar   0 B
511136ea3c5a   10 months ago                                                    0 B                 Imported from -
</pre>
</dl>
<h2>Display comments in the image history</h2>
<p> The docker commit command has a <code>-m</code> flag for adding comments to the image. These comments will be displayed in the image history. </p>
<dl>
<dt>
<dd>
<pre>
$ sudo docker history docker:scm
IMAGE               CREATED             CREATED BY                                      SIZE                COMMENT
2ac9d1098bf1        3 months ago        /bin/bash                                       241.4 MB            Added Apache to Fedora base image
88b42ffd1f7c        5 months ago        /bin/sh -c #(nop) ADD file:1fd8d7f9f6557cafc7   373.7 MB            
c69cab00d6ef        5 months ago        /bin/sh -c #(nop) MAINTAINER Lokesh Mandvekar   0 B                 
511136ea3c5a        19 months ago                                                       0 B                 Imported from -
</pre>
</dl>
<h2>HISTORY</h2>
<p> April 2014, Originally compiled by William Henry (whenry at redhat dot com) based on docker.com source material and internal work. June 2014, updated by Sven Dowideit &lt;SvenDowideit [at] home.org.au&gt; </p>
<h2>Index</h2>
