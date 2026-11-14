---
title: "cfenvgraph(8)"
name: "cfenvgraph"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cfenvgraph/"
description: "cfengine – network configuration engine"
---

<p>cfengine &#8211; network configuration engine</p>
<h2>Synopsis</h2>
<p>/usr/local/sbin/cfenvgraph [options] </p>
<h2>Command Line Options</h2>
<dl>
<dt>&#8211;help</p>
<dd>
<dt>&#8211;file</p>
<dd><code>Override default input database</code></p>
<dt>&#8211;erasehistory</p>
<dd><code>Erase machine-learned history of named traces. Comma separated list (no spaces)</code></p>
<dt>&#8211;outputdir</p>
<dd><code>override name of output directory</code></p>
<dt>&#8211;titles</p>
<dd><code>Generate titles in output data files for traces</code></p>
<dt>&#8211;timestamps</p>
<dd><code>Add time stamps to output directory</code></p>
<dt>&#8211;resolution</p>
<dd><code>Maximum output resolution (default is smoothed over each hour).</code></p>
<dt>&#8211;separate</p>
<dd><code>Plot separate output files for each trace.</code></p>
<dt>&#8211;no-error-bars</p>
<dd><code>Do not add uncertainty margins to output.</code></p>
<dt>&#8211;no-scaling</p>
<dd><code>Do not renormalize graphs for convenient representation</code></p>
<dt>&#8211;now</p>
<dd><code>Show data for last four hours only in high resolution.</code></p>
<dt>&#8211;verbose</p>
<dd></dl>
<h2>Description</h2>
<p><code>cfengine</code> is a language based system specifically designed for testing and configuring unix-like systems attached to a TCP/IP network. Cfenvd is part of the anomaly detection subsystem for cfagent. <code>cfenvgraph is a research tool for extracting graphs of the</code> learned history of system performance from the learned database. Users are referred to the web page <a rel="nofollow" href="http://www.cfengine.org/confdir/cfenvgraph.html">http://www.cfengine.org/confdir/cfenvgraph.html</a> for an explanation of this graphical tool. </p>
<h2>Author</h2>
<p>Mark Burgess, Oslo University College</p>
<h2>Information</h2>
<p><a rel="nofollow" href="http://www.cfengine.org">http://www.cfengine.org</a></p>
