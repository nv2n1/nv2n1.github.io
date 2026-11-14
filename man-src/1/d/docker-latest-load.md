---
title: "docker-latest-load(1)"
name: "docker-latest-load"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-latest-load/"
description: "docker-load – Load an image from a tar archive or STDIN"
---

<h2 class="name">NAME</h2>
<p> docker-load &#8211; Load an image from a tar archive or STDIN </p>
<h2>SYNOPSIS</h2>
<p> <code>docker load</code> [<code>&#8211;help</code>] [<code>-i</code>|<code>&#8211;input</code>[=<i>INPUT</i>]] [<code>-q</code>|<code>&#8211;quiet</code>] </p>
<h2>DESCRIPTION</h2>
<p> Loads a tarred repository from a file or the standard input stream. Restores both images and tags. Write image names or IDs imported it standard output stream. </p>
<h2>OPTIONS</h2>
<p> <code>&#8211;help</code><br />
&nbsp;<wbr>&nbsp;<wbr>Print usage statement </p>
<p> <code>-i</code>, <code>&#8211;input</code>=&quot;&quot;<br />
Read from a tar archive file, instead of STDIN. The tarball may be compressed with gzip, bzip, or xz. </p>
<p> <code>-q</code>, <code>&#8211;quiet</code><br />
Suppress the load progress bar but still outputs the imported images. </p>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd>
<pre><code>
$ docker images
    REPOSITORY TAG IMAGE ID CREATED SIZE
        busybox latest 769b9341d937 7 weeks ago 2.489 MB
            $ docker load-- input fedora.tar
#[…]
                Loaded image : fedora : rawhide
#[…]
                                            Loaded image : fedora : 20
#[…]
                                                           $ docker images
                                                               REPOSITORY TAG IMAGE ID CREATED SIZE
                                                                   busybox latest 769b9341d937 7 weeks ago 2.489 MB
                                                                       fedora rawhide 0d20aec6529d 7 weeks ago 387 MB
                                                                           fedora 20 58394af37342 7 weeks ago 385.5 MB
                                                                               fedora heisenbug 58394af37342 7 weeks ago 385.5 MB
                                                                                   fedora latest 58394af37342 7 weeks ago 385.5 MB
</code></pre>
</dl>
<h2>See also</h2>
<p> <code><a href="/docs/linux/man/1-docker-save/">docker-save</a>(1)</code> to save one or more images to a tar archive (streamed to STDOUT by default). </p>
<h2>HISTORY</h2>
<p> April 2014, Originally compiled by William Henry (whenry at redhat dot com) based on docker.com source material and internal work. June 2014, updated by Sven Dowideit &lt;SvenDowideit [at] home.org.au&gt; July 2015 update by Mary Anthony &lt;mary [at] docker.com&gt; June 2016 update by Vincent Demeester &lt;vincent [at] sbr.pm&gt; </p>
<h2>Index</h2>
