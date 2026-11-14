---
title: "pamphletangler(1)"
name: "pamphletangler"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pamphletangler/"
description: "pamphletangler – Extract code bits from LaTeX pamphlet files."
---

<h2 class="name">NAME</h2>
<p> pamphletangler &#8211; Extract code bits from LaTeX pamphlet files. </p>
<h2>SYNOPSIS</h2>
<p> <code>pamphletangler</code> [<font SIZE="-1">OPTION&#8230;</font>] <i></i><font SIZE="-1"><i>FILE</i></font><i></i> <i></i><font SIZE="-1"><i>CHUNKNAME</i></font><i></i></p>
<h2>DESCRIPTION</h2>
<p> The clojure pamphlet system is a system based on the clojure literate system. In the clojure&#8217;s pamphlet system you have your main LaTeX file, which can be compiled regularly. This file contains documentation and source code (just like in other forms of literate programming). This code snippets are wrapped in the &#8216;chunk&#8217; environment, hence they can be recognized by the tangler in order to extract them. Chunks can be included inside each other by the &#8216;getchunk&#8217; command (which will be typesetted acordingly). Finally, you run your LaTeX file through the tangler and get your desired chunk of code.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-L, &#8211;line=linetext</p>
<dd> If set, this text will be inserted after jumps of lines, changing the string inside &#8220;changetext&#8221; for the line number. This is used so that error report refers to pamphlet line number instead of output line number</p>
<dt>-C, &#8211;change=changetext</p>
<dd> Defaults to &#8220;{}&#8221; this is the text that will be replaced with the line number if the linetext option is specified</p>
<dt>-?, &#8211;help</p>
<dd> Give this help list</p>
<dt>&#8211;usage</p>
<dd> Give a short usage message</p>
<dt>&#8211;man</p>
<dd> Print manual page</p>
<dt>-V, &#8211;version</p>
<dd> Print program version</dl>
<h2>LICENSE</h2>
<p> Copyright (C) 2019 Ernesto Lanchares Sanchez. </p>
<pre>
   The clojure-pamphlet tagler is free software; you can redistribute
   it and/or modify it under the terms of the GNU Lesser General
   Public License as published by the Free Software Foundation;
   either version 3 of the License, or (at your option) any later
   version.
  The clojure-pamphlet tangler is distributed in the hope that it
  will be useful, but WITHOUT ANY WARRANTY; without even the implied
  warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU Lesser General Public License for more details.
  You should have received a copy of the GNU Lesser General Public
  License along with this program; if not, see
  L&lt;<a rel="nofollow" href="http://www.gnu.org/licenses/">http://www.gnu.org/licenses/</a>&gt;.
</pre>
<h2>AUTHOR</h2>
<p> Ernesto Lanchares &lt;e.lancha98 [at] gmail.com&gt;</p>
<h2>BUGS</h2>
<p> Report bugs to e.lancha98 [at] gmail.com </p>
<h2>Index</h2>
