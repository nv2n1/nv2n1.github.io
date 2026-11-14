---
title: "docker-image-ls(1)"
name: "docker-image-ls"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-image-ls/"
description: "docker-image-ls – List images"
---

<h2 class="name">NAME</h2>
<p> docker-image-ls &#8211; List images </p>
<h2>SYNOPSIS</h2>
<p> <code>docker image ls [OPTIONS] [REPOSITORY[:TAG]]</code> </p>
<h2>DESCRIPTION</h2>
<p> This command lists the images stored in the local Docker repository. </p>
<p> By default, intermediate images, used during builds, are not listed. Some of the output, e.g., image ID, is truncated, for space reasons. However the truncated image ID, and often the first few characters, are enough to be used in other Docker commands that use the image ID. The output includes repository, tag, image ID, date created and the virtual size. </p>
<p> The title REPOSITORY for the first title may seem confusing. It is essentially the image name. However, because you can tag a specific image, and multiple tags (image instances) can be associated with a single name, the name is really a repository for all tagged images of the same name. For example consider an image called fedora. It may be tagged with 18, 19, or 20, etc. to manage different versions. </p>
<h2>Filters</h2>
<p> Filters the output based on these conditions: </p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> dangling=(true|false) &#8211; find unused images</p>
<dt>&bull;</p>
<dd> label= or label==</p>
<dt>&bull;</p>
<dd> before=([:tag]||image [at] digest &lt;mailto:image [at] digest&gt;)</p>
<dt>&bull;</p>
<dd> since=([:tag]||image [at] digest &lt;mailto:image [at] digest&gt;)</p>
<dt>&bull;</p>
<dd> reference=(pattern of an image reference) </p>
</dl>
</dl>
<h2>Format</h2>
<p> Pretty-print images using a Go template.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Valid placeholders:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.ID &#8211; Image ID<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.Repository &#8211; Image repository<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.Tag &#8211; Image tag<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.Digest &#8211; Image digest<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.CreatedSince &#8211; Elapsed time since the image was created<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.CreatedAt &#8211; Time when the image was created<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.Size &#8211; Image disk size </p>
<h2>EXAMPLES</h2>
<h2>Listing the images</h2>
<p> To list the images in a local repository (not the registry) run: </p>
<dl>
<dt>
<dd>
<pre>
docker image ls
</pre>
</dl>
<p> The list will contain the image repository name, a tag for the image, and an image ID, when it was created and its virtual size. Columns: REPOSITORY, TAG, IMAGE ID, CREATED, and SIZE. </p>
<p> The docker image ls command takes an optional [REPOSITORY[:TAG]] argument that restricts the list to images that match the argument. If you specify REPOSITORY but no TAG, the docker image ls command lists all images in the given repository. </p>
<dl>
<dt>
<dd>
<pre>
docker image ls java
</pre>
</dl>
<p> The [REPOSITORY[:TAG]] value must be an &quot;exact match&quot;. This means that, for example, docker image ls jav does not match the image java. </p>
<p> If both REPOSITORY and TAG are provided, only images matching that repository and tag are listed. To find all local images in the &quot;java&quot; repository with tag &quot;8&quot; you can use: </p>
<dl>
<dt>
<dd>
<pre>
docker image ls java:8
</pre>
</dl>
<p> To get a verbose list of images which contains all the intermediate images used in builds use <code>-a</code>: </p>
<dl>
<dt>
<dd>
<pre>
docker image ls -a
</pre>
</dl>
<p> Previously, the docker image ls command supported the &#8211;tree and &#8211;dot arguments, which displayed different visualizations of the image data. Docker core removed this functionality in the 1.7 version. If you liked this functionality, you can still find it in the third-party dockviz tool: <a rel="nofollow" href="https://github.com/justone/dockviz.">https://github.com/justone/dockviz.</a> </p>
<h2>Listing images in a desired format</h2>
<p> When using the &#8211;format option, the image command will either output the data exactly as the template declares or, when using the table directive, will include column headers as well. You can use special characters like 	 for inserting tab spacing between columns. </p>
<p> The following example uses a template without headers and outputs the ID and Repository entries separated by a colon for all images: </p>
<dl>
<dt>
<dd>
<pre><code>
docker images-- format "&#123;&#123;.ID}}: &#123;&#123;.Repository}}" 77af4d6b9913 : &lt;none&gt;
                                                                     b6fa739cedf5 : committ 78a85c484bad : ipbabble 30557a29d5ab : docker 5ed6274db6ce : &lt;none&gt; 746b819f315e : postgres 746b819f315e : postgres 746b819f315e : postgres 746b819f315e : postgres
</code></pre>
</dl>
<p> To list all images with their repository and tag in a table format you can use: </p>
<dl>
<dt>
<dd>
<pre><code>
docker images-- format "table &#123;&#123;.ID}}	&#123;&#123;.Repository}}	&#123;&#123;.Tag}}" IMAGE ID REPOSITORY TAG 77af4d6b9913 &lt; none &gt; &lt;none&gt;
                                                                                                                    b6fa739cedf5 committ latest 78a85c484bad ipbabble&lt;none&gt; 30557a29d5ab docker latest 5ed6274db6ce &lt; none &gt; &lt;none&gt; 746b819f315e postgres 9 746b819f315e postgres 9.3 746b819f315e postgres 9.3.5 746b819f315e postgres latest
</code></pre>
</dl>
<p> Valid template placeholders are listed above. </p>
<h2>Listing only the shortened image IDs</h2>
<p> Listing just the shortened image IDs. This can be useful for some automated tools. </p>
<dl>
<dt>
<dd>
<pre>
docker image ls -q
</pre>
</dl>
<h2>OPTIONS</h2>
<p> <code>-a</code>, <code>&#8211;all</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Show all images (default hides intermediate images)</p>
<p> <code>&#8211;digests</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Show digests</p>
<p> <code>-f</code>, <code>&#8211;filter</code>= <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Filter output based on conditions provided</p>
<p> <code>&#8211;format</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Pretty-print images using a Go template</p>
<p> <code>-h</code>, <code>&#8211;help</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>help for ls</p>
<p> <code>&#8211;no-trunc</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Don&#8217;t truncate output</p>
<p> <code>-q</code>, <code>&#8211;quiet</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Only show image IDs</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-docker-image/">docker-image</a>(1)</code> </p>
<h2>Index</h2>
