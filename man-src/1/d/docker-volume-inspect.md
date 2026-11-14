---
title: "docker-volume-inspect(1)"
name: "docker-volume-inspect"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-volume-inspect/"
description: "docker-volume-inspect – Display detailed information on one or more volumes"
---

<h2 class="name">NAME</h2>
<p> docker-volume-inspect &#8211; Display detailed information on one or more volumes </p>
<h2>SYNOPSIS</h2>
<p> <code>docker volume inspect [OPTIONS] VOLUME [VOLUME&#8230;]</code> </p>
<h2>DESCRIPTION</h2>
<p> Returns information about one or more volumes. By default, this command renders all results in a JSON array. You can specify an alternate format to execute a given template is executed for each result. Go&#8217;s <a rel="nofollow" href="https://golang.org/pkg/text/template/">https://golang.org/pkg/text/template/</a> package describes all the details of the format. </p>
<h2>OPTIONS</h2>
<p> <code>-f</code>, <code>&#8211;format</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Format the output using the given Go template</p>
<p> <code>-h</code>, <code>&#8211;help</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>help for inspect</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-docker-volume/">docker-volume</a>(1)</code> </p>
<h2>Index</h2>
