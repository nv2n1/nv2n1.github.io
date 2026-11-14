---
title: "docker-latest-push(1)"
name: "docker-latest-push"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-latest-push/"
description: "docker-push – Push an image or a repository to a registry"
---

<h2 class="name">NAME</h2>
<p> docker-push &#8211; Push an image or a repository to a registry </p>
<h2>SYNOPSIS</h2>
<p> <code>docker push</code> [<code>&#8211;help</code>] NAME[:TAG] | [REGISTRY_HOST[:REGISTRY_PORT]/]NAME[:TAG] </p>
<h2>DESCRIPTION</h2>
<p> Use docker push to share your images to the &lt;<a rel="nofollow" href="https://hub.docker.com">https://hub.docker.com</a>&gt; registry or to a self-hosted one. </p>
<p> Refer to <code><a href="/docs/linux/man/1-docker-tag/">docker-tag</a>(1)</code> for more information about valid image and tag names. </p>
<p> Killing the <code>docker push</code> process, for example by pressing <code>CTRL-c</code> while it is running in a terminal, terminates the push operation. </p>
<p> Registry credentials are managed by <code><a href="/docs/linux/man/1-docker-login/">docker-login</a>(1)</code>. </p>
<h2>OPTIONS</h2>
<p> <code>&#8211;disable-content-trust</code><br />
&nbsp;<wbr>&nbsp;<wbr>Skip image verification&nbsp;<wbr>(default true) </p>
<p> <code>&#8211;help</code><br />
&nbsp;<wbr>&nbsp;<wbr>Print usage statement </p>
<h2>EXAMPLES</h2>
<h2>Pushing a new image to a registry</h2>
<p> First save the new image by finding the container ID (using <code>docker ps</code>) and then committing it to a new image name. Note that only a-z0-9-_. are allowed when naming images: </p>
<dl>
<dt>
<dd>
<pre>
# docker commit c16378f943fe rhel-httpd
</pre>
</dl>
<p> Now, push the image to the registry using the image ID. In this example the registry is on host named registry-host and listening on port 5000. To do this, tag the image with the host name or IP address, and the port of the registry: </p>
<dl>
<dt>
<dd>
<pre>
# docker tag rhel-httpd registry-host:5000/myadmin/rhel-httpd
# docker push registry-host:5000/myadmin/rhel-httpd
</pre>
</dl>
<p> Check that this worked by running: </p>
<dl>
<dt>
<dd>
<pre>
# docker images
</pre>
</dl>
<p> You should see both rhel-httpd and registry-host:5000/myadmin/rhel-httpd listed. </p>
<h2>HISTORY</h2>
<p> April 2014, Originally compiled by William Henry (whenry at redhat dot com) based on docker.com source material and internal work. June 2014, updated by Sven Dowideit &lt;SvenDowideit [at] home.org.au&gt; April 2015, updated by Mary Anthony for v2 &lt;mary [at] docker.com&gt; June 2015, updated by Sally O&#8217;Malley &lt;somalley [at] redhat.com&gt; </p>
<h2>Index</h2>
