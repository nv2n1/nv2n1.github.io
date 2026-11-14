---
title: "xmparsetable(3)"
name: "xmparsetable"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmparsetable/"
description: "XmParseTable — Data type for a compound string parse table"
---

<p><code>XmParseTable</code> &#8212; Data type for a compound string parse table</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;</pre>
<h2>Description</h2>
<p><code>XmParseTable</code> is the data type for an array of parse mappings (objects of type <code>XmParseMapping</code>). </p>
<p> A parse table is used by some routines that parse and unparse compound strings. The table is an ordered list of parse mappings. A parsing routine that uses a parse table scans the input text and searches the parse mappings, in order, for one containing a pattern that matches the input text. The matching parse mapping supplies a compound string to be included in the compound string under construction. </p>
<p> An unparsing routine that uses a parse table searches the parse mappings, in order, for one containing a compound string that matches the input compound string. The unparsing routine can then include the parse mapping&#8217;s text pattern in the output text under construction.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmparsemapping/">XmParseMapping</a></code>(3), <code><a href="/docs/linux/man/3-xmparsetablefree/">XmParseTableFree</a></code>(3), and <code><a href="/docs/linux/man/3-xmstring/">XmString</a></code>(3).</p>
