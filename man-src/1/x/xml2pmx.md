---
title: "xml2pmx(1)"
name: "xml2pmx"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xml2pmx/"
---

<h2>DESCRIPTION</h2>
<p> xml2pmx translates MusicXML files to input suitable for PMX processing </p>
<h2>SYNOPSIS</h2>
<p> <code>xml2pmx </code> [<code>-v | &#8211;version | -h | &#8211;help</code>] </p>
<p> <code>xml2pmx </code> <i>input</i>.xml <i>output</i>.pmx [ p | d | v | s | l ] .. </p>
<p> The <code>musixtex.lua</code> script from version 0.23 supports <code>xml2pmx</code> as a pre-preprocessor for MusicXML files. </p>
<h2>OPTIONS</h2>
<p> The meanings of the letter options are as follows: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;p&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XML parser output;&nbsp;not recommended unless the terminal window process has enough storage </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;d&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;information on&nbsp;&quot;directions&quot;&nbsp;(dynamical marks etc)&nbsp;<wbr>&nbsp; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;v&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;distribution of voices over instruments and measures&nbsp; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;s&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;statistics of MusicXML tags like&nbsp;&lt;note&gt;,&nbsp;&lt;measure&gt;&nbsp;etc&nbsp; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;l&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for extracting lyrics in a separate file&nbsp;<wbr>&nbsp; </p>
<h2>BUGS</h2>
<p> <code>xml2pmx </code> processes input in UTF-8 encoding only. MusicXML files in UTF-16 encoding should be converted using, for example, <code>recode</code> (in Unix-like systems) or by importing into an editor like <code>notepad</code> and saving in UTF-8 encoding. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pmx/">pmx</a></code>(1) <code><a href="/docs/linux/man/1-obc/">obc</a></code>(1) <code><a href="/docs/linux/man/1-musixtex/">musixtex</a></code>(1) <code><a href="/docs/linux/man/1-recode/">recode</a></code>(1) </p>
<h2>AUTHORS</h2>
<p> This man page was written by Bob Tennent &lt;rdt [at] cs.queensu.ca&gt;. <code>xml2pmx</code> was written by Dieter Gloetzel &lt;d.gloetzel [at] web.de&gt; and adapted for compilation by obc (the Oxford Oberon Compiler) by Mike Spivey &lt;mike [at] cs.ox.ac.uk&gt;. </p>
<h2>Index</h2>
