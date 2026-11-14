---
title: "xmlstarlet(1)"
name: "xmlstarlet"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xmlstarlet/"
description: "xmlstarlet – command line XML/XSLT toolkit"
---

<h2 class="name">NAME</h2>
<p> xmlstarlet &#8211; command line XML/XSLT toolkit </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>xml</code> [<i>options</i>&#8230;] {<i>command</i>} [<i>cmd-options</i>&#8230;]</dl>
<h2>INTRODUCTION</h2>
<dd>XMLStarlet is a set of command line utilities (tools) which can be used to transform, query, validate, and edit XML documents and files using simple set of shell commands in similar way it is done for plain text files using UNIX grep, sed, awk, diff, patch, join, etc commands. This set of command line utilities can be used by those who deal with many XML documents on UNIX shell command prompt as well as for automated XML processing with shell scripts.</p>
<h2>OPTIONS</h2>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Display the version of xmlstarlet.</dl>
<p> <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display help.</dl>
<h2>COMMANDS</h2>
<p> <code>xml</code> <i>command</i> <code>&#8211;help</code> for command specific help </p>
<p> Available commands include: </p>
<p> <code>ed (or edit)</code></p>
<dl>
<dt>
<dd> Edit/update XML document(s).</dl>
<p> <code>sel (or select)</code></p>
<dl>
<dt>
<dd> Select data or query XML document(s) (XPATH, etc).</dl>
<p> <code>tr (or transform)</code></p>
<dl>
<dt>
<dd> Transform XML documents(s) using XSLT.</dl>
<p> <code>val (or validate)</code></p>
<dl>
<dt>
<dd> Validate XML document(s) (well-formed/DTD/XSD/RelaxNG).</dl>
<p> <code>fo (or format)</code></p>
<dl>
<dt>
<dd> Format XML document(s).</dl>
<p> <code>el (or elements)</code></p>
<dl>
<dt>
<dd> Display element structure of XML document.</dl>
<p> <code>c14n (or canonic)</code></p>
<dl>
<dt>
<dd> XML canonicalization.</dl>
<p> <code>ls (or list)</code></p>
<dl>
<dt>
<dd> List directory as XML.</dl>
<p> <code>esc (or escape)</code></p>
<dl>
<dt>
<dd> Escape special XML characters.</dl>
<p> <code>unesc (or unescape)</code></p>
<dl>
<dt>
<dd> Unescape special XML characters.</dl>
<p> <code>pyx (or xmln)</code></p>
<dl>
<dt>
<dd> Convert XML into PYX format (based on ESIS &#8211; ISO 8879).</dl>
<p> <code>p2x (or depyx)</code></p>
<dl>
<dt>
<dd> Convert PYX into XML.</dl>
<h2>REFERENCES</h2>
<p> XMLStarlet is a command line toolkit to query/edit/check/transform XML documents (for more information see <a rel="nofollow" href="http://xmlstar.sourceforge.net/">http://xmlstar.sourceforge.net/</a>).</p>
<h2>BUGS</h2>
<p> Report bugs to the mailing list, xmlstar-devel [at] lists.sourceforge.net or the bug tracker: m[blue]<code><a rel="nofollow" href="http://sourceforge.net/tracker/?group_id=66612">http://sourceforge.net/tracker/?group_id=66612</a>&amp;atid=515106</code>m[].</p>
<h2>AUTHOR</h2>
<p> <code>Mikhail Grushinskiy</code></p>
<dl>
<dt>
<dd> XMLStarlet creator.</dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2012 </p>
<h2>Index</h2>
