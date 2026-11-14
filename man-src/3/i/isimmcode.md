---
title: "isimmcode(3)"
name: "isimmcode"
section: "3"
letter: "i"
url: "/docs/linux/man/3-isimmcode/"
description: "QuantLib::IMM – Main cycle of the International Money Market (a.k.a. IMM) months."
---

<p>QuantLib::IMM &#8211; Main cycle of the International Money Market (a.k.a. IMM) months. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/time/imm.hpp&gt; </p>
<h3>Public Types</h3>
<p>enum <code>Month</code> { <code>F</code> = 1, <code>G</code> = 2, <code>H</code> = 3, <code>J</code> = 4, <code>K</code> = 5, <code>M</code> = 6, <code>N</code> = 7, <code>Q</code> = 8, <code>U</code> = 9, <code>V</code> = 10, <code>X</code> = 11, <code>Z</code> = 12 } </p>
<h3>Static Public Member Functions</h3>
<p>static bool <code>isIMMdate</code> (const <code>Date</code> &amp;d, bool mainCycle=true)<br />
 <i>returns whether or not the given date is an </i><code>IMM</code> date<br />
 static bool <code>isIMMcode</code> (const std::string &amp;in, bool mainCycle=true)<br />
 <i>returns whether or not the given string is an </i><code>IMM</code> code<br />
 static std::string <code>code</code> (const <code>Date</code> &amp;immDate) </p>
<p> static <code>Date</code> <code>date</code> (const std::string &amp;immCode, const <code>Date</code> &amp;referenceDate=<code>Date</code>()) </p>
<p> static <code>Date</code> <code>nextDate</code> (const <code>Date</code> &amp;d=<code>Date</code>(), bool mainCycle=true)<br />
 <i>next </i><code>IMM</code> date following the given date<br />
 static <code>Date</code> <code>nextDate</code> (const std::string &amp;immCode, bool mainCycle=true, const <code>Date</code> &amp;referenceDate=<code>Date</code>())<br />
 <i>next </i><code>IMM</code> date following the given <code>IMM</code> code<br />
 static std::string <code>nextCode</code> (const <code>Date</code> &amp;d=<code>Date</code>(), bool mainCycle=true) </p>
<p> static std::string <code>nextCode</code> (const std::string &amp;immCode, bool mainCycle=true, const <code>Date</code> &amp;referenceDate=<code>Date</code>()) </p>
<h2>Detailed Description</h2>
<p>Main cycle of the International Money Market (a.k.a. IMM) months.</p>
<h2>Member Function Documentation</h2>
<h3>static std::string code (const <code>Date</code> &amp; immDate) [static]</h3>
<p>returns the <code>IMM</code> code for the given date (e.g. H3 for March 20th, 2013). </p>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>It raises an exception if the input date is not an <code>IMM</code> date</dl>
<h3>static <code>Date</code> date (const std::string &amp; immCode, const <code>Date</code> &amp; referenceDate = <code>Date</code>()) [static]</h3>
<p>returns the <code>IMM</code> date for the given <code>IMM</code> code (e.g. March 20th, 2013 for H3). </p>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>It raises an exception if the input string is not an <code>IMM</code> code</dl>
<h3>static <code>Date</code> nextDate (const <code>Date</code> &amp; d = <code>Date</code>(), bool mainCycle = true) [static]</h3>
<p>next <code>IMM</code> date following the given date </p>
<p> returns the 1st delivery date for next contract listed in the International <code>Money</code> Market section of the Chicago Mercantile Exchange.</p>
<h3>static <code>Date</code> nextDate (const std::string &amp; immCode, bool mainCycle = true, const <code>Date</code> &amp; referenceDate = <code>Date</code>()) [static]</h3>
<p>next <code>IMM</code> date following the given <code>IMM</code> code </p>
<p> returns the 1st delivery date for next contract listed in the International <code>Money</code> Market section of the Chicago Mercantile Exchange.</p>
<h3>static std::string nextCode (const <code>Date</code> &amp; d = <code>Date</code>(), bool mainCycle = true) [static]</h3>
<p>returns the <code>IMM</code> code for next contract listed in the International <code>Money</code> Market section of the Chicago Mercantile Exchange.</p>
<h3>static std::string nextCode (const std::string &amp; immCode, bool mainCycle = true, const <code>Date</code> &amp; referenceDate = <code>Date</code>()) [static]</h3>
<p>returns the <code>IMM</code> code for next contract listed in the International <code>Money</code> Market section of the Chicago Mercantile Exchange. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
