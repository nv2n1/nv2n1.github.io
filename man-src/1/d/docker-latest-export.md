---
title: "docker-latest-export(1)"
name: "docker-latest-export"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-latest-export/"
description: "docker-export – Export the contents of a container’s filesystem as a tar archive"
---

<h2 class="name">NAME</h2>
<p> docker-export &#8211; Export the contents of a container&#8217;s filesystem as a tar archive </p>
<h2>SYNOPSIS</h2>
<p> <code>docker export</code> [<code>&#8211;help</code>] [<code>-o</code>|<code>&#8211;output</code>[=<i>&quot;&quot;</i>]] CONTAINER </p>
<h2>DESCRIPTION</h2>
<p> Export the contents of a container&#8217;s filesystem using the full or shortened container ID or container name. The output is exported to STDOUT and can be redirected to a tar file. </p>
<p> Stream to a file instead of STDOUT by using <code>-o</code>. </p>
<h2>OPTIONS</h2>
<p> <code>&#8211;help</code><br />
&nbsp;<wbr>&nbsp;<wbr>Print usage statement </p>
<p> <code>-o</code>, <code>&#8211;output</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>Write to a file, instead of STDOUT </p>
<h2>EXAMPLES</h2>
<p> Export the contents of the container called angry_bell to a tar file called angry_bell.tar: </p>
<dl>
<dt>
<dd>
<pre>
# docker export angry_bell &gt; angry_bell.tar
# docker export --output=angry_bell-latest.tar angry_bell
# ls -sh angry_bell.tar
321M angry_bell.tar
# ls -sh angry_bell-latest.tar
321M angry_bell-latest.tar
</pre>
</dl>
<h2>See also</h2>
<p> <code><a href="/docs/linux/man/1-docker-import/">docker-import</a>(1)</code> to create an empty filesystem image and import the contents of the tarball into it, then optionally tag it. </p>
<h2>HISTORY</h2>
<p> April 2014, Originally compiled by William Henry (whenry at redhat dot com) based on docker.com source material and internal work. June 2014, updated by Sven Dowideit &lt;SvenDowideit [at] home.org.au&gt; January 2015, updated by Joseph Kern (josephakern at gmail dot com) </p>
<h2>Index</h2>
