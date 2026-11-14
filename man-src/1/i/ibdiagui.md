---
title: "ibdiagui(1)"
name: "ibdiagui"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ibdiagui/"
description: "ibdiagui – IB Diagnostic GUI"
---

<h2>NAME</h2>
<p> <code>ibdiagui &#8211; IB Diagnostic GUI</code></p>
<h2>SYNOPSYS</h2>
<p> ibdiagui [-c &lt;count&gt;] [-v] [-r] [-o &lt;out-dir&gt;]<br />
&nbsp;<wbr>&nbsp;<wbr>[-t&nbsp;<wbr>&lt;topo-file&gt;]&nbsp;<wbr>[-s&nbsp;<wbr>&lt;sys-name&gt;]&nbsp;<wbr>[-i&nbsp;<wbr>&lt;dev-index&gt;]&nbsp;<wbr>[-p&nbsp;<wbr>&lt;port-num&gt;]<br />
&nbsp;<wbr>&nbsp;<wbr>[-pm]&nbsp;<wbr>[-pc]&nbsp;<wbr>[-P&nbsp;<wbr>&lt;<font SIZE="-1">PM</font>&nbsp;<wbr>counter&gt;=&lt;Trash Limit&gt;]<br />
&nbsp;<wbr>&nbsp;<wbr>[-lw&nbsp;<wbr>&lt;1x|4x|12x&gt;]&nbsp;<wbr>[-ls&nbsp;<wbr>&lt;2.5|5|10&gt;]</p>
<h2>DESCRIPTION</h2>
<pre>
  ibdiagui is a GUI wrapper for ibdiagnet.
  Its main features:
</pre>
<dl>
<dt>1. Display a graph of the discovered fabric (with optional names annotattion)</p>
<dd>
<dt>2. Hyperlink the ibdiagnet log to the graph objects</p>
<dd>
<dt>3. Show each object properties and object type specific actions on a properties pannel.</p>
<dd></dl>
<h2>OPTIONS</h2>
<dl>
<dt>ibdiagui simply passes its options to ibdiagnet. Please see ibdiagnet man page for the complete list.</p>
<dd>
</dl>
<h2>Index</h2>
