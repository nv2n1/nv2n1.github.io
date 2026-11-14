---
title: "docker-latest-search(1)"
name: "docker-latest-search"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-latest-search/"
description: "docker-search – Search the Docker Hub for images"
---

<h2 class="name">NAME</h2>
<p> docker-search &#8211; Search the Docker Hub for images </p>
<h2>SYNOPSIS</h2>
<p> <code>docker search</code> [<code>-f</code>|<code>&#8211;filter</code>[=<i>[]</i>]] [<code>&#8211;help</code>] [<code>&#8211;limit</code>[=<i>LIMIT</i>]] [<code>&#8211;no-index</code>] [<code>&#8211;no-trunc</code>] TERM </p>
<h2>DESCRIPTION</h2>
<p> Search Docker Hub for images that match the specified TERM. The table of images returned displays the name, description (truncated by default), number of stars awarded, whether the image is official, and whether it is automated. </p>
<p> <i>Note</i> &#8211; Search queries will only return up to 25 results </p>
<h2>OPTIONS</h2>
<p> <code>-f</code>, <code>&#8211;filter</code>=[]<br />
Filter output based on these conditions:<br />
&#8211; stars=&lt;numberOfStar&gt;<br />
&#8211; is-automated=(true|false)<br />
&#8211; is-official=(true|false) </p>
<p> <code>&#8211;help</code><br />
Print usage statement </p>
<p> <code>&#8211;no-index</code>=<i>true</i>|<i>false</i><br />
Do not include index name in output. Sort results primarily by registry<br />
name. </p>
<p> <code>&#8211;limit</code>=<i>LIMIT</i><br />
&nbsp;<wbr>&nbsp;<wbr>Maximum returned search results. The default is 25. </p>
<p> <code>&#8211;no-trunc</code>=<i>true</i>|<i>false</i><br />
Don&#8217;t truncate output. The default is&nbsp;<wbr><i>false</i>. </p>
<h2>EXAMPLES</h2>
<h2>Search Docker Hub for ranked images</h2>
<p> Search a registry for the term &#8216;fedora&#8217; and only display those images ranked 3 or higher: </p>
<dl>
<dt>
<dd>
<pre>
$ docker search --filter=starts=3 fedora
INDEX      NAME                            DESCRIPTION                                    STARS OFFICIAL  AUTOMATED
docker.io  docker.io/mattdm/fedora         A basic Fedora image corresponding roughly...  50
docker.io  docker.io/fedora                (Semi) Official Fedora base image.             38
docker.io  docker.io/mattdm/fedora-small   A small Fedora image on which to build. Co...  8
docker.io  docker.io/goldmann/wildfly      A WildFly application server running on a ...  3               [OK]
</pre>
</dl>
<h2>Search Docker Hub for automated images</h2>
<p> Search Docker Hub for the term &#8216;fedora&#8217; and only display automated images ranked 1 or higher: </p>
<dl>
<dt>
<dd>
<pre><code>
$ docker search-- filter = is - automated = true --filter = starts = 1 fedora
                                                                             INDEX NAME DESCRIPTION STARS OFFICIAL AUTOMATED
                                                                                 docker.io docker.io /
                                                                         goldmann / wildfly A WildFly application server running on a... 3 [OK] docker.io docker.io / tutum / fedora -
                                                                     20 Fedora 20 image with SSH access.For the r... 1 [OK]
</code></pre>
</dl>
<h2>HISTORY</h2>
<p> April 2014, Originally compiled by William Henry (whenry at redhat dot com) based on docker.com source material and internal work. June 2014, updated by Sven Dowideit &lt;SvenDowideit [at] home.org.au&gt; April 2015, updated by Mary Anthony for v2 &lt;mary [at] docker.com&gt; April 2016, updated by Vincent Demeester &lt;vincent [at] sbr.pm&gt; </p>
<h2>Index</h2>
