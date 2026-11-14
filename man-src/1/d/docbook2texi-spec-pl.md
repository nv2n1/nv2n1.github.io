---
title: "docbook2texi-spec-pl(1)"
name: "docbook2texi-spec-pl"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docbook2texi-spec-pl/"
description: "docbook2texi-spec.pl – convert DocBook Booksto Texinfo documents"
---

<p>docbook2texi-spec.pl &#8211; convert DocBook Booksto Texinfo documents </p>
<h2>Synopsis</h2>
<p><code>sgmlspl</code> <code>docbook2man-spec.pl</code> </p>
<p> <code>nsgmls</code> [ <i>sgml document</i> ]<code>| sgmlspl</code> <code>docbook2texi-spec.pl</code> [ <i>basename</i> ] </p>
<h2>Description</h2>
<p><code>docbook2texi</code> is a sgmlspl spec file that produces GNU Texinfo documents from DocBook documents. </p>
<p> The program reads ESIS produced by nsgmls (or other SGML parsers) from standard input. Currently the document element must be Book, otherwise the results are undefined. </p>
<p> Its output, the converted Texinfo document, is written to standard output. </p>
<p> The file <i>basename.refs</i> will also be created, which contains all the nodes in the document and their immediate &#8216;child&#8217; nodes. As node processing always require forward references, <code>docbook2texi</code> must be run twice for each document: the first time to build the references, and the second to actually generate a valid document.</p>
<h2>Requirements</h2>
<p>The SGMLSpm package from CPAN. This package includes the sgmlspl script that is also needed.</p>
<h2>Limitations</h2>
<p>Trying <code>docbook2man</code> on non-DocBook or non-conformant SGML results in undefined behavior. :-) </p>
<p> This program is a slow, dodgy Perl script. </p>
<p> This program does not come close to supporting all the possible markup in DocBook, and may produce wrong output in some cases with supported markup.</p>
<h2>To Do</h2>
<dl>
<dt>&bull;</p>
<dd>How the hell do you represent a backslash (\) in Texinfo!!@? I&#8217;ve tried \ but TeX complains about it.</p>
<dt>&bull;</p>
<dd>Fix breakages found in the test documents.</p>
<dt>&bull;</p>
<dd>Add new element handling and fix existing handling. Be robust.</p>
<dt>&bull;</p>
<dd>Make it faster. I think most of the speed problems so far is with parsing ESIS. Rewrite <i>SGMLS.pm</i> with C and/or get input directly from <code>SP</code>.</p>
<dt>&bull;</p>
<dd>There are some dependencies on elements occurring when they are actually optional (according to the DTD). We need to fix that (preferably) or prominently state the requirements.</p>
<dt>&bull;</p>
<dd>Allow other more common document elements.</p>
<dt>&bull;</p>
<dd>Separate out node referencing to a separate script. Not only would it make it faster/easier to maintain because it&#8217;s separate from the main code, but also I would like it to evolve into an automatic DocBook ToC generator.</dl>
<h2>Copyright</h2>
<p>Copyright (C) 1998-1999 Steve Cheng &lt;steve [at] ggi-project.org&gt; </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2, or (at your option) any later version. </p>
<p> You should have received a copy of the GNU General Public License along with this program; see the file <i>COPYING</i>. If not, please write to the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.</p>
