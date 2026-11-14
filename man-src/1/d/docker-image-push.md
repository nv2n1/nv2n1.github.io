---
title: "docker-image-push(1)"
name: "docker-image-push"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-image-push/"
description: "docker-image-push – Push an image or a repository to a registry"
---

<h2 class="name">NAME</h2>
<p> docker-image-push &#8211; Push an image or a repository to a registry </p>
<h2>SYNOPSIS</h2>
<p> <code>docker image push [OPTIONS] NAME[:TAG]</code> </p>
<h2>DESCRIPTION</h2>
<p> Use docker image push to share your images to the Docker Hub &lt;<a rel="nofollow" href="https://hub.docker.com">https://hub.docker.com</a>&gt; registry or to a self-hosted one. </p>
<p> Refer to <code><a href="/docs/linux/man/1-docker-image-tag/">docker-image-tag</a>(1)</code> for more information about valid image and tag names. </p>
<p> Killing the <code>docker image push</code> process, for example by pressing <code>CTRL-c</code> while it is running in a terminal, terminates the push operation. </p>
<p> Registry credentials are managed by <code><a href="/docs/linux/man/1-docker-login/">docker-login</a>(1)</code>. </p>
<h2>EXAMPLES</h2>
<h2>Pushing a new image to a registry</h2>
<p> First save the new image by finding the container ID (using <code>docker container ls</code>) and then committing it to a new image name. Note that only a-z0-9-_. are allowed when naming images: </p>
<dl>
<dt>
<dd>
<pre>
# docker container commit c16378f943fe rhel-httpd
</pre>
</dl>
<p> Now, push the image to the registry using the image ID. In this example the registry is on host named registry-host and listening on port 5000. To do this, tag the image with the host name or IP address, and the port of the registry: </p>
<dl>
<dt>
<dd>
<pre>
# docker image tag rhel-httpd registry-host:5000/myadmin/rhel-httpd:latest
# docker image push registry-host:5000/myadmin/rhel-httpd:latest
</pre>
</dl>
<p> Check that this worked by running: </p>
<dl>
<dt>
<dd>
<pre>
# docker image ls
</pre>
</dl>
<p> You should see both rhel-httpd and registry-host:5000/myadmin/rhel-httpd listed. </p>
<h3>Push all tags of an image</h3>
<p> Use the -a (or &#8211;all-tags) option to push To push all tags of a local image. </p>
<p> The following example creates multiple tags for an image, and pushes all those tags to Docker Hub. </p>
<dl>
<dt>
<dd>
<pre>
$ docker image tag myimage registry-host:5000/myname/myimage:latest
$ docker image tag myimage registry-host:5000/myname/myimage:v1.0.1
$ docker image tag myimage registry-host:5000/myname/myimage:v1.0
$ docker image tag myimage registry-host:5000/myname/myimage:v1
</pre>
</dl>
<p> The image is now tagged under multiple names: </p>
<dl>
<dt>
<dd>
<pre>
$ docker image ls
REPOSITORY                          TAG        IMAGE ID       CREATED      SIZE
myimage                             latest     6d5fcfe5ff17   2 hours ago  1.22MB
registry-host:5000/myname/myimage   latest     6d5fcfe5ff17   2 hours ago  1.22MB
registry-host:5000/myname/myimage   v1         6d5fcfe5ff17   2 hours ago  1.22MB
registry-host:5000/myname/myimage   v1.0       6d5fcfe5ff17   2 hours ago  1.22MB
registry-host:5000/myname/myimage   v1.0.1     6d5fcfe5ff17   2 hours ago  1.22MB
</pre>
</dl>
<p> When pushing with the &#8211;all-tags option, all tags of the registry-host:5000/myname/myimage image are pushed: </p>
<dl>
<dt>
<dd>
<pre>
$ docker image push --all-tags registry-host:5000/myname/myimage
The push refers to repository [registry-host:5000/myname/myimage]
195be5f8be1d: Pushed
latest: digest: sha256:edafc0a0fb057813850d1ba44014914ca02d671ae247107ca70c94db686e7de6 size: 4527
195be5f8be1d: Layer already exists
v1: digest: sha256:edafc0a0fb057813850d1ba44014914ca02d671ae247107ca70c94db686e7de6 size: 4527
195be5f8be1d: Layer already exists
v1.0: digest: sha256:edafc0a0fb057813850d1ba44014914ca02d671ae247107ca70c94db686e7de6 size: 4527
195be5f8be1d: Layer already exists
v1.0.1: digest: sha256:edafc0a0fb057813850d1ba44014914ca02d671ae247107ca70c94db686e7de6 size: 4527
</pre>
</dl>
<h2>OPTIONS</h2>
<p> <code>-a</code>, <code>&#8211;all-tags</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Push all tagged images in the repository</p>
<p> <code>&#8211;disable-content-trust</code>[=true] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Skip image signing</p>
<p> <code>-h</code>, <code>&#8211;help</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>help for push</p>
<p> <code>-q</code>, <code>&#8211;quiet</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Suppress verbose output</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-docker-image/">docker-image</a>(1)</code> </p>
<h2>Index</h2>
