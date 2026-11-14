---
title: "docker-image-load(1)"
name: "docker-image-load"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-image-load/"
description: "docker-image-load – Load an image from a tar archive or STDIN"
---

<h2 class="name">NAME</h2>
<p> docker-image-load &#8211; Load an image from a tar archive or STDIN </p>
<h2>SYNOPSIS</h2>
<p> <code>docker image load [OPTIONS]</code> </p>
<h2>DESCRIPTION</h2>
<p> Loads a tarred repository from a file or the standard input stream. Restores both images and tags. Write image names or IDs imported it standard output stream. </p>
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
<p> <code><a href="/docs/linux/man/1-docker-image-save/">docker-image-save</a>(1)</code> to save one or more images to a tar archive (streamed to STDOUT by default). </p>
<h2>OPTIONS</h2>
<p> <code>-h</code>, <code>&#8211;help</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>help for load</p>
<p> <code>-i</code>, <code>&#8211;input</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Read from tar archive file, instead of STDIN</p>
<p> <code>-q</code>, <code>&#8211;quiet</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Suppress the load output</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-docker-image/">docker-image</a>(1)</code> </p>
<h2>Index</h2>
