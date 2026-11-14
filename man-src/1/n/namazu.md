---
title: "namazu(1)"
name: "namazu"
section: "1"
letter: "n"
url: "/docs/linux/man/1-namazu/"
description: "namazu – a search program of Namazu"
---

<h2>NAME</h2>
<p> namazu &#8211; a search program of Namazu</p>
<h2>SYNOPSIS</h2>
<p> <code>namazu</code> [<i>options</i>] <i>&lt;query&gt; </i>[<i>index</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> namazu 2.0.19, a search program of Namazu.</p>
<dl>
<dt><code>-n</code>, <code>&#8211;max</code>=<i>NUM</i></p>
<dd> set the number of documents shown to NUM.</p>
<dt><code>-w</code>, <code>&#8211;whence</code>=<i>NUM</i></p>
<dd> set the first number of documents shown to NUM.</p>
<dt><code>-l</code>, <code>&#8211;list</code></p>
<dd> print the results by listing the format.</p>
<dt><code>-s</code>, <code>&#8211;short</code></p>
<dd> print the results in a short format.</p>
<dt><code>&#8211;result</code>=<i>EXT</i></p>
<dd> set NMZ.result.EXT for printing the results.</p>
<dt><code>&#8211;late</code></p>
<dd> sort the documents in late order.</p>
<dt><code>&#8211;early</code></p>
<dd> sort the documents in early order.</p>
<dt><code>&#8211;sort</code>=<i>METHOD</i></p>
<dd> set a sort METHOD (score, date, field:name)</p>
<dt><code>&#8211;ascending</code></p>
<dd> sort in ascending order (default: descending)</p>
<dt><code>-a</code>, <code>&#8211;all</code></p>
<dd> print all results.</p>
<dt><code>-c</code>, <code>&#8211;count</code></p>
<dd> print only the number of hits.</p>
<dt><code>-h</code>, <code>&#8211;html</code></p>
<dd> print in HTML format.</p>
<dt><code>-r</code>, <code>&#8211;no-references</code></p>
<dd> do not display the reference hit counts.</p>
<dt><code>-H</code>, <code>&#8211;page</code></p>
<dd> print the links of further results. (This is nearly meaningless)</p>
<dt><code>-F</code>, <code>&#8211;form</code></p>
<dd> force to print the &lt;form&gt; &#8230; &lt;/form&gt; region.</p>
<dt><code>-R</code>, <code>&#8211;no-replace</code></p>
<dd> do not replace the URI string.</p>
<dt><code>-U</code>, <code>&#8211;no-decode-uri</code></p>
<dd> do not decode the URI when printing in a plain format.</p>
<dt><code>-o</code>, <code>&#8211;output</code>=<i>FILE</i></p>
<dd> set the output file name to FILE.</p>
<dt><code>-f</code>, <code>&#8211;config</code>=<i>FILE</i></p>
<dd> set the config file name to FILE.</p>
<dt><code>-C</code>, <code>&#8211;show-config</code></p>
<dd> print the current configuration.</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> do not display extra messages except search results.</p>
<dt><code>-d</code>, <code>&#8211;debug</code></p>
<dd> be in debug mode.</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> show the namazu version and exit.</p>
<dt><code>&#8211;help</code></p>
<dd> show this help and exit.</p>
<dt><code>&#8211;norc</code></p>
<dd> do not read the personal initialization files.</p>
<dt><code>&#8212;</code></p>
<dd> Terminate option list.</dl>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;<a rel="nofollow" href="http://www.namazu.org/trac-namazu/trac.cgi">http://www.namazu.org/trac-namazu/trac.cgi</a>&gt; or &lt;bug-namazu [at] namazu.org&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1997-1999 Satoru Takabayashi All rights reserved.<br />
 Copyright &#169; 2000-2009 Namazu Project All rights reserved.<br />
 This is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<h2>Index</h2>
