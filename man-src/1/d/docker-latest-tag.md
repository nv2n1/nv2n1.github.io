---
title: "docker-latest-tag(1)"
name: "docker-latest-tag"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-latest-tag/"
description: "docker-tag – Tag an image into a repository"
---

<h2 class="name">NAME</h2>
<p> docker-tag &#8211; Tag an image into a repository </p>
<h2>SYNOPSIS</h2>
<p> <code>docker tag</code> [<code>&#8211;help</code>] NAME[:TAG] NAME[:TAG] </p>
<h2>DESCRIPTION</h2>
<p> Assigns a new alias to an image in a registry. An alias refers to the entire image name including the optional TAG after the &#8216;:&#8217;. </p>
<h2>OPTIONS</h2>
<p> <code>&#8211;help</code><br />
Print usage statement. </p>
<p> <code>NAME</code><br />
The image name which is made up of slash-separated name components,<br />
optionally prefixed by a registry hostname. The hostname must comply with<br />
standard DNS rules, but may not contain underscores. If a hostname is<br />
present, it may optionally be followed by a port number in the format<br />
:8080. If not present, the command uses Docker&#8217;s public registry located at<br />
registry-1.docker.io by default. Name components may contain lowercase<br />
characters, digits and separators. A separator is defined as a period, one or<br />
two underscores, or one or more dashes. A name component may not start or end<br />
with a separator. </p>
<p> <code>TAG</code><br />
The tag assigned to the image to version and distinguish images with the same<br />
name. The tag name may contain lowercase and uppercase characters, digits,<br />
underscores, periods and dashes. A tag name may not start with a period or a<br />
dash and may contain a maximum of 128 characters. </p>
<h2>EXAMPLES</h2>
<h2>Tagging an image referenced by ID</h2>
<p> To tag a local image with ID &quot;0e5574283393&quot; into the &quot;fedora&quot; repository with &quot;version1.0&quot;: </p>
<dl>
<dt>
<dd>
<pre>
docker tag 0e5574283393 fedora/httpd:version1.0
</pre>
</dl>
<h2>Tagging an image referenced by Name</h2>
<p> To tag a local image with name &quot;httpd&quot; into the &quot;fedora&quot; repository with &quot;version1.0&quot;: </p>
<dl>
<dt>
<dd>
<pre>
docker tag httpd fedora/httpd:version1.0
</pre>
</dl>
<p> Note that since the tag name is not specified, the alias is created for an existing local version httpd:latest. </p>
<h2>Tagging an image referenced by Name and Tag</h2>
<p> To tag a local image with name &quot;httpd&quot; and tag &quot;test&quot; into the &quot;fedora&quot; repository with &quot;version1.0.test&quot;: </p>
<dl>
<dt>
<dd>
<pre>
docker tag httpd:test fedora/httpd:version1.0.test
</pre>
</dl>
<h2>Tagging an image for a private repository</h2>
<p> To push an image to a private registry and not the central Docker registry you must tag it with the registry hostname and port (if needed). </p>
<dl>
<dt>
<dd>
<pre>
docker tag 0e5574283393 myregistryhost:5000/fedora/httpd:version1.0
</pre>
</dl>
<h2>HISTORY</h2>
<p> April 2014, Originally compiled by William Henry (whenry at redhat dot com) based on docker.com source material and internal work. June 2014, updated by Sven Dowideit &lt;SvenDowideit [at] home.org.au&gt; July 2014, updated by Sven Dowideit &lt;SvenDowideit [at] home.org.au&gt; April 2015, updated by Mary Anthony for v2 &lt;mary [at] docker.com&gt; June 2015, updated by Sally O&#8217;Malley &lt;somalley [at] redhat.com&gt; </p>
<h2>Index</h2>
