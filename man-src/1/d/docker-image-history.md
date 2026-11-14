---
title: "docker-image-history(1)"
name: "docker-image-history"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-image-history/"
description: "docker-image-history – Show the history of an image"
---

<h2 class="name">NAME</h2>
<p> docker-image-history &#8211; Show the history of an image </p>
<h2>SYNOPSIS</h2>
<p> <code>docker image history [OPTIONS] IMAGE</code> </p>
<h2>DESCRIPTION</h2>
<p> Show the history of when and how an image was created. </p>
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
<h3>Format the output</h3>
<p> The formatting option (&#8211;format) will pretty-prints history output using a Go template. </p>
<p> Valid placeholders for the Go template are listed below: </p>
<table BORDER>
<tr VALIGN=top>
<td>Placeholder</td>
<td>Description
</td>
</tr>
<tr VALIGN=top>
<td>.ID</td>
<td>Image ID
</td>
</tr>
<tr VALIGN=top>
<td>.CreatedSince</td>
<td> Elapsed time since the image was created if &#8211;human=true, otherwise timestamp of when image was created
</td>
</tr>
<tr VALIGN=top>
<td>.CreatedAt</td>
<td> Timestamp of when image was created
</td>
</tr>
<tr VALIGN=top>
<td>.CreatedBy</td>
<td> Command that was used to create the image
</td>
</tr>
<tr VALIGN=top>
<td>.Size</td>
<td>Image disk size
</td>
</tr>
<tr VALIGN=top>
<td>.Comment</td>
<td>Comment for image
</td>
</tr>
</table>
<p> When using the &#8211;format option, the history command will either output the data exactly as the template declares or, when using the table directive, will include column headers as well. </p>
<p> The following example uses a template without headers and outputs the ID and CreatedSince entries separated by a colon for all images: </p>
<dl>
<dt>
<dd>
<pre><code>
$ docker images-- format "&#123;&#123;.ID}}: &#123;&#123;.CreatedSince}} ago" cc1b61406712 : 2 weeks ago&lt;missing&gt; : 2 weeks ago&lt;missing&gt; : 2 weeks ago&lt;missing&gt; : 2 weeks ago&lt;missing&gt; : 2 weeks ago&lt;missing&gt; : 3 weeks ago&lt;missing&gt; : 3 weeks ago&lt;missing&gt; : 3 weeks ago
</code></pre>
</dl>
<h2>OPTIONS</h2>
<p> <code>&#8211;format</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Pretty-print images using a Go template</p>
<p> <code>-h</code>, <code>&#8211;help</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>help for history</p>
<p> <code>-H</code>, <code>&#8211;human</code>[=true] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Print sizes and dates in human readable format</p>
<p> <code>&#8211;no-trunc</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Don&#8217;t truncate output</p>
<p> <code>-q</code>, <code>&#8211;quiet</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Only show image IDs</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-docker-image/">docker-image</a>(1)</code> </p>
<h2>Index</h2>
