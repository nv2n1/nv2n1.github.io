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
<dt>&#8211;help</dt>
<dd>
</dd><dt>&#8211;file</dt>
<dd><code>Override default input database</code></dd>
<dt>&#8211;erasehistory</dt>
<dd><code>Erase machine-learned history of named traces. Comma separated list (no spaces)</code></dd>
<dt>&#8211;outputdir</dt>
<dd><code>override name of output directory</code></dd>
<dt>&#8211;titles</dt>
<dd><code>Generate titles in output data files for traces</code></dd>
<dt>&#8211;timestamps</dt>
<dd><code>Add time stamps to output directory</code></dd>
<dt>&#8211;resolution</dt>
<dd><code>Maximum output resolution (default is smoothed over each hour).</code></dd>
<dt>&#8211;separate</dt>
<dd><code>Plot separate output files for each trace.</code></dd>
<dt>&#8211;no-error-bars</dt>
<dd><code>Do not add uncertainty margins to output.</code></dd>
<dt>&#8211;no-scaling</dt>
<dd><code>Do not renormalize graphs for convenient representation</code></dd>
<dt>&#8211;now</dt>
<dd><code>Show data for last four hours only in high resolution.</code></dd>
<dt>&#8211;verbose</dt>
<dd></dd></dl>
<h2>Description</h2>
<p><code>cfengine</code> is a language based system specifically designed for testing and configuring unix-like systems attached to a TCP/IP network. Cfenvd is part of the anomaly detection subsystem for cfagent. <code>cfenvgraph is a research tool for extracting graphs of the</code> learned history of system performance from the learned database. Users are referred to the web page <a rel="nofollow" href="http://www.cfengine.org/confdir/cfenvgraph.html">http://www.cfengine.org/confdir/cfenvgraph.html</a> for an explanation of this graphical tool. </p>
<h2>Author</h2>
<p>Mark Burgess, Oslo University College</p>
<h2>Information</h2>
<p><a rel="nofollow" href="http://www.cfengine.org">http://www.cfengine.org</a></p>
