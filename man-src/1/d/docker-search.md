---
title: "docker-search(1)"
name: "docker-search"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-search/"
description: "docker-search – Search the Docker Hub for images"
---

<h2 class="name">NAME</h2>
<p> docker-search &#8211; Search the Docker Hub for images </p>
<h2>SYNOPSIS</h2>
<p> <code>docker search [OPTIONS] TERM</code> </p>
<h2>DESCRIPTION</h2>
<p> Search Docker Hub for images that match the specified TERM. The table of images returned displays the name, description (truncated by default), number of stars awarded, whether the image is official, and whether it is automated. </p>
<p> <i>Note</i> &#8211; Search queries will only return up to 25 results </p>
<h2>Filter</h2>
<p> Filter output based on these conditions:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; stars=<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; is-automated=(true|false)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; is-official=(true|false) </p>
<h2>EXAMPLES</h2>
<h2>Search Docker Hub for ranked images</h2>
<p> Search a registry for the term &#8216;fedora&#8217; and only display those images ranked 3 or higher: </p>
<dl>
<dt>
<dd>
<pre>
$ docker search --filter=stars=3 fedora
NAME                  DESCRIPTION                                    STARS OFFICIAL  AUTOMATED
mattdm/fedora         A basic Fedora image corresponding roughly...  50
fedora                (Semi) Official Fedora base image.             38
mattdm/fedora-small   A small Fedora image on which to build. Co...  8
goldmann/wildfly      A WildFly application server running on a ...  3               [OK]
</pre>
</dl>
<h2>Search Docker Hub for automated images</h2>
<p> Search Docker Hub for the term &#8216;fedora&#8217; and only display automated images ranked 1 or higher: </p>
<dl>
<dt>
<dd>
<pre><code>
$ docker search-- filter = is - automated = true --filter = stars = 1 fedora
                                                                            NAME DESCRIPTION STARS OFFICIAL AUTOMATED
                                                                                goldmann /
                                                                        wildfly A WildFly application server running on a... 3 [OK] tutum / fedora -
                                                                    20 Fedora 20 image with SSH access.For the r... 1 [OK]
</code></pre>
</dl>
<h2>OPTIONS</h2>
<p> <code>-f</code>, <code>&#8211;filter</code>= <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Filter output based on conditions provided</p>
<p> <code>&#8211;format</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Pretty-print search using a Go template</p>
<p> <code>-h</code>, <code>&#8211;help</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>help for search</p>
<p> <code>&#8211;limit</code>=25 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Max number of search results</p>
<p> <code>&#8211;no-trunc</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Don&#8217;t truncate output</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-docker/">docker</a>(1)</code> </p>
<h2>Index</h2>
