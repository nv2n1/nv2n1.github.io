---
title: "docker-image-tag(1)"
name: "docker-image-tag"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-image-tag/"
description: "docker-image-tag – Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE"
---

<h2 class="name">NAME</h2>
<p> docker-image-tag &#8211; Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE </p>
<h2>SYNOPSIS</h2>
<p> <code>docker image tag SOURCE_IMAGE[:TAG] TARGET_IMAGE[:TAG]</code> </p>
<h2>DESCRIPTION</h2>
<p> Assigns a new alias to an image in a registry. An alias refers to the entire image name including the optional TAG after the &#8216;:&#8217;. </p>
<h2>OPTIONS</h2>
<p> <code>NAME</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;The image name which is made up of slash-separated name components,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;optionally prefixed by a registry hostname. The hostname must comply with<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;standard DNS rules, but may not contain underscores. If a hostname is<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;present, it may optionally be followed by a port number in the format<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;:8080. If not present, the command uses Docker&#8217;s public registry located at<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;registry-1.docker.io by default. Name components may contain lowercase<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;letters, digits and separators. A separator is defined as a period, one or<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;two underscores, or one or more dashes. A name component may not start or end<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;with a separator. </p>
<p> <code>TAG</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;The tag assigned to the image to version and distinguish images with the same<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;name. The tag name must be valid ASCII and may contain lowercase and<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;uppercase letters, digits, underscores, periods and hyphens. A tag name<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;may not start with a period or a hyphen and may contain a maximum of 128<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;characters. </p>
<h2>EXAMPLES</h2>
<h2>Tagging an image referenced by ID</h2>
<p> To tag a local image with ID &quot;0e5574283393&quot; into the &quot;fedora&quot; repository with &quot;version1.0&quot;: </p>
<dl>
<dt>
<dd>
<pre>
docker image tag 0e5574283393 fedora/httpd:version1.0
</pre>
</dl>
<h2>Tagging an image referenced by Name</h2>
<p> To tag a local image with name &quot;httpd&quot; into the &quot;fedora&quot; repository with &quot;version1.0&quot;: </p>
<dl>
<dt>
<dd>
<pre>
docker image tag httpd fedora/httpd:version1.0
</pre>
</dl>
<p> Note that since the tag name is not specified, the alias is created for an existing local version httpd:latest. </p>
<h2>Tagging an image referenced by Name and Tag</h2>
<p> To tag a local image with name &quot;httpd&quot; and tag &quot;test&quot; into the &quot;fedora&quot; repository with &quot;version1.0.test&quot;: </p>
<dl>
<dt>
<dd>
<pre>
docker image tag httpd:test fedora/httpd:version1.0.test
</pre>
</dl>
<h2>Tagging an image for a private repository</h2>
<p> Before pushing an image to a private registry and not the central Docker registry you must tag it with the registry hostname and port (if needed). </p>
<dl>
<dt>
<dd>
<pre>
docker image tag 0e5574283393 myregistryhost:5000/fedora/httpd:version1.0
</pre>
</dl>
<h2>OPTIONS</h2>
<p> <code>-h</code>, <code>&#8211;help</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>help for tag</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-docker-image/">docker-image</a>(1)</code> </p>
<h2>Index</h2>
