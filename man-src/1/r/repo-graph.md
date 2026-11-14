---
title: "repo-graph(1)"
name: "repo-graph"
section: "1"
letter: "r"
url: "/docs/linux/man/1-repo-graph/"
description: "repo-graph – output a full package dependency graph in dot format"
---

<h2>NAME</h2>
<p> repo-graph &#8211; output a full package dependency graph in dot format</p>
<h2>SYNOPSIS</h2>
<p> <code>repo-graph</code> [options]</p>
<h2>DESCRIPTION</h2>
<p> <code>repo-graph</code> is a program that generates a full package dependency list from a yum repository and outputs it in dot format. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Display a help message, and then quit.</p>
<dt><code>&#8211;repoid=REPOID</code></p>
<dd> Specify repo ids to query, can be specified multiple times (default is all enabled).</p>
<dt><code>-c CONFIG</code></p>
<dd> Config file to use (defaults to /etc/yum.conf). </p>
</dl>
<h2>SEE ALSO</h2>
<pre>
<i>yum.conf (5)</i>
<a rel="nofollow" href="http://yum.baseurl.org/">http://yum.baseurl.org/</a>
</pre>
<h2>AUTHORS</h2>
<pre>
See the Authors file included with this program.
</pre>
<h2>Index</h2>
