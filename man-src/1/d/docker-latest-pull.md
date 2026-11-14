---
title: "docker-latest-pull(1)"
name: "docker-latest-pull"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-latest-pull/"
description: "docker-pull – Pull an image or a repository from a registry"
---

<h2 class="name">NAME</h2>
<p> docker-pull &#8211; Pull an image or a repository from a registry </p>
<h2>SYNOPSIS</h2>
<p> <code>docker pull</code> [<code>-a</code>|<code>&#8211;all-tags</code>] [<code>&#8211;help</code>] NAME[:TAG] | [REGISTRY_HOST[:REGISTRY_PORT]/]NAME[:TAG] </p>
<h2>DESCRIPTION</h2>
<p> This command pulls down an image or a repository from a registry. If there is more than one image for a repository (e.g., fedora) then all images for that repository name can be pulled down including any tags (see the option <code>-a</code> or <code>&#8211;all-tags</code>). </p>
<p> If you do not specify a REGISTRY_HOST, the command uses Docker&#8217;s public registry located at registry-1.docker.io by default. </p>
<h2>OPTIONS</h2>
<p> <code>-a</code>, <code>&#8211;all-tags</code>=<i>true</i>|<i>false</i><br />
Download all tagged images in the repository. The default is&nbsp;<wbr><i>false</i>. </p>
<p> <code>&#8211;help</code><br />
&nbsp;<wbr>&nbsp;<wbr>Print usage statement </p>
<h2>EXAMPLES</h2>
<h3>Pull an image from Docker Hub</h3>
<p> To download a particular image, or set of images (i.e., a repository), use docker pull. If no tag is provided, Docker Engine uses the :latest tag as a default. This command pulls the debian:latest image: </p>
<dl>
<dt>
<dd>
<pre>
$ docker pull debian
Using default tag: latest
latest: Pulling from library/debian
fdd5d7827f33: Pull complete
a3ed95caeb02: Pull complete
Digest: sha256:e7d38b3517548a1c71e41bffe9c8ae6d6d29546ce46bf62159837aad072c90aa
Status: Downloaded newer image for debian:latest
</pre>
</dl>
<p> Docker images can consist of multiple layers. In the example above, the image consists of two layers; fdd5d7827f33 and a3ed95caeb02. </p>
<p> Layers can be reused by images. For example, the debian:jessie image shares both layers with debian:latest. Pulling the debian:jessie image therefore only pulls its metadata, but not its layers, because all layers are already present locally: </p>
<dl>
<dt>
<dd>
<pre>
$ docker pull debian:jessie
jessie: Pulling from library/debian
fdd5d7827f33: Already exists
a3ed95caeb02: Already exists
Digest: sha256:a9c958be96d7d40df920e7041608f2f017af81800ca5ad23e327bc402626b58e
Status: Downloaded newer image for debian:jessie
</pre>
</dl>
<p> To see which images are present locally, use the <code><a href="/docs/linux/man/1-docker-images/">docker-images</a>(1)</code> command: </p>
<dl>
<dt>
<dd>
<pre>
$ docker images
REPOSITORY   TAG      IMAGE ID        CREATED      SIZE
debian       jessie   f50f9524513f    5 days ago   125.1 MB
debian       latest   f50f9524513f    5 days ago   125.1 MB
</pre>
</dl>
<p> Docker uses a content-addressable image store, and the image ID is a SHA256 digest covering the image&#8217;s configuration and layers. In the example above, debian:jessie and debian:latest have the same image ID because they are actually the <i>same</i> image tagged with different names. Because they are the same image, their layers are stored only once and do not consume extra disk space. </p>
<p> For more information about images, layers, and the content-addressable store, refer to &lt;<a rel="nofollow" href="https://docs.docker.com/engine/userguide/storagedriver/imagesandcontainers/">https://docs.docker.com/engine/userguide/storagedriver/imagesandcontainers/</a>&gt; in the online documentation. </p>
<h2>Pull an image by digest (immutable identifier)</h2>
<p> So far, you&#8217;ve pulled images by their name (and &quot;tag&quot;). Using names and tags is a convenient way to work with images. When using tags, you can docker pull an image again to make sure you have the most up-to-date version of that image. For example, docker pull ubuntu:14.04 pulls the latest version of the Ubuntu 14.04 image. </p>
<p> In some cases you don&#8217;t want images to be updated to newer versions, but prefer to use a fixed version of an image. Docker enables you to pull an image by its <i>digest</i>. When pulling an image by digest, you specify <i>exactly</i> which version of an image to pull. Doing so, allows you to &quot;pin&quot; an image to that version, and guarantee that the image you&#8217;re using is always the same. </p>
<p> To know the digest of an image, pull the image first. Let&#8217;s pull the latest ubuntu:14.04 image from Docker Hub: </p>
<dl>
<dt>
<dd>
<pre>
$ docker pull ubuntu:14.04
14.04: Pulling from library/ubuntu
5a132a7e7af1: Pull complete
fd2731e4c50c: Pull complete
28a2f68d1120: Pull complete
a3ed95caeb02: Pull complete
Digest: sha256:45b23dee08af5e43a7fea6c4cf9c25ccf269ee113168c19722f87876677c5cb2
Status: Downloaded newer image for ubuntu:14.04
</pre>
</dl>
<p> Docker prints the digest of the image after the pull has finished. In the example above, the digest of the image is: </p>
<dl>
<dt>
<dd>
<pre>
sha256:45b23dee08af5e43a7fea6c4cf9c25ccf269ee113168c19722f87876677c5cb2
</pre>
</dl>
<p> Docker also prints the digest of an image when <i>pushing</i> to a registry. This may be useful if you want to pin to a version of the image you just pushed. </p>
<p> A digest takes the place of the tag when pulling an image, for example, to pull the above image by digest, run the following command: </p>
<dl>
<dt>
<dd>
<pre><code>
$ docker pull ubuntu [at] sha256:45b23dee08af5e43a7fea6c4cf9c25ccf269ee113168c19722f87876677c5cb2
sha256:45b23dee08af5e43a7fea6c4cf9c25ccf269ee113168c19722f87876677c5cb2: Pulling from library/ubuntu
5a132a7e7af1: Already exists
fd2731e4c50c: Already exists
28a2f68d1120: Already exists
a3ed95caeb02: Already exists
Digest: sha256:45b23dee08af5e43a7fea6c4cf9c25ccf269ee113168c19722f87876677c5cb2
Status: Downloaded newer image for ubuntu [at] sha256:45b23dee08af5e43a7fea6c4cf9c25ccf269ee113168c19722f87876677c5cb2
</code></pre>
</dl>
<p> Digest can also be used in the FROM of a Dockerfile, for example: </p>
<dl>
<dt>
<dd>
<pre><code>
FROM ubuntu[at] sha256 : 45b23dee08af5e43a7fea6c4cf9c25ccf269ee113168c19722f87876677c5cb2 MAINTAINER some maintainer&lt;maintainer[at] example.com&gt;
</code></pre>
</dl>
<dl>
<dt>
<dd>
<p> <code>Note</code>: Using this feature &quot;pins&quot; an image to a specific version in time. Docker will therefore not pull updated versions of an image, which may include security updates. If you want to pull an updated image, you need to change the digest accordingly.</dl>
<h2>Pulling from a different registry</h2>
<p> By default, docker pull pulls images from Docker Hub. It is also possible to manually specify the path of a registry to pull from. For example, if you have set up a local registry, you can specify its path to pull from it. A registry path is similar to a URL, but does not contain a protocol specifier (<a rel="nofollow" href="https://">https://</a>). </p>
<p> The following command pulls the testing/test-image image from a local registry listening on port 5000 (myregistry.local:5000): </p>
<dl>
<dt>
<dd>
<pre>
$ docker pull myregistry.local:5000/testing/test-image
</pre>
</dl>
<p> Registry credentials are managed by <code><a href="/docs/linux/man/1-docker-login/">docker-login</a>(1)</code>. </p>
<p> Docker uses the https:// protocol to communicate with a registry, unless the registry is allowed to be accessed over an insecure connection. Refer to the </p>
<p> &lt;<a rel="nofollow" href="https://docs.docker.com/engine/reference/commandline/daemon/#insecure-registries">https://docs.docker.com/engine/reference/commandline/daemon/#insecure-registries</a>&gt; section in the online documentation for more information. </p>
<h2>Pull a repository with multiple images</h2>
<p> By default, docker pull pulls a <i>single</i> image from the registry. A repository can contain multiple images. To pull all images from a repository, provide the -a (or &#8211;all-tags) option when using docker pull. </p>
<p> This command pulls all images from the fedora repository: </p>
<dl>
<dt>
<dd>
<pre>
$ docker pull --all-tags fedora
Pulling repository fedora
ad57ef8d78d7: Download complete
105182bb5e8b: Download complete
511136ea3c5a: Download complete
73bd853d2ea5: Download complete
Status: Downloaded newer image for fedora
</pre>
</dl>
<p> After the pull has completed use the docker images command to see the images that were pulled. The example below shows all the fedora images that are present locally: </p>
<dl>
<dt>
<dd>
<pre>
$ docker images fedora
REPOSITORY   TAG         IMAGE ID        CREATED      SIZE
fedora       rawhide     ad57ef8d78d7    5 days ago   359.3 MB
fedora       20          105182bb5e8b    5 days ago   372.7 MB
fedora       heisenbug   105182bb5e8b    5 days ago   372.7 MB
fedora       latest      105182bb5e8b    5 days ago   372.7 MB
</pre>
</dl>
<h2>Canceling a pull</h2>
<p> Killing the docker pull process, for example by pressing CTRL-c while it is running in a terminal, will terminate the pull operation. </p>
<dl>
<dt>
<dd>
<pre>
$ docker pull fedora
Using default tag: latest
latest: Pulling from library/fedora
a3ed95caeb02: Pulling fs layer
236608c7b546: Pulling fs layer
^C
</pre>
</dl>
<dl>
<dt>
<dd>
<p> <code>Note</code>: Technically, the Engine terminates a pull operation when the connection between the Docker Engine daemon and the Docker Engine client initiating the pull is lost. If the connection with the Engine daemon is lost for other reasons than a manual interaction, the pull is also aborted.</dl>
<h2>HISTORY</h2>
<p> April 2014, Originally compiled by William Henry (whenry at redhat dot com) based on docker.com source material and internal work. June 2014, updated by Sven Dowideit &lt;SvenDowideit [at] home.org.au&gt; August 2014, updated by Sven Dowideit &lt;SvenDowideit [at] home.org.au&gt; April 2015, updated by John Willis &lt;john.willis [at] docker.com&gt; April 2015, updated by Mary Anthony for v2 &lt;mary [at] docker.com&gt; September 2015, updated by Sally O&#8217;Malley &lt;somalley [at] redhat.com&gt; </p>
<h2>Index</h2>
