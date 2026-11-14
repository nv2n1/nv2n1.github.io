---
title: "docker-volume-ls(1)"
name: "docker-volume-ls"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-volume-ls/"
description: "docker-volume-ls – List volumes"
---

<h2 class="name">NAME</h2>
<p> docker-volume-ls &#8211; List volumes </p>
<h2>SYNOPSIS</h2>
<p> <code>docker volume ls [OPTIONS]</code> </p>
<h2>DESCRIPTION</h2>
<p> Lists all the volumes Docker manages. You can filter using the -f or &#8211;filter flag. The filtering format is a key=value pair. To specify more than one filter, pass multiple flags (for example, &#8211;filter &quot;foo=bar&quot; &#8211;filter &quot;bif=baz&quot;) </p>
<p> The currently supported filters are: </p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> dangling (boolean &#8211; true or false, 1 or 0)</p>
<dt>&bull;</p>
<dd> driver (a volume driver&#8217;s name)</p>
<dt>&bull;</p>
<dd> label (label=&lt;key&gt; or label=&lt;key&gt;=&lt;value&gt;)</p>
<dt>&bull;</p>
<dd> name (a volume&#8217;s name) </p>
</dl>
</dl>
<h2>OPTIONS</h2>
<p> <code>-f</code>, <code>&#8211;filter</code>= <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Provide filter values (e.g. &#8216;dangling=true&#8217;)</p>
<p> <code>&#8211;format</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Pretty-print volumes using a Go template</p>
<p> <code>-h</code>, <code>&#8211;help</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>help for ls</p>
<p> <code>-q</code>, <code>&#8211;quiet</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Only display volume names</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-docker-volume/">docker-volume</a>(1)</code> </p>
<h2>Index</h2>
