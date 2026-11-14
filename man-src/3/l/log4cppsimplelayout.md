---
title: "log4cppsimplelayout(3)"
name: "log4cppsimplelayout"
section: "3"
letter: "l"
url: "/docs/linux/man/3-log4cppsimplelayout/"
description: "log4cpp::SimpleLayout –"
---

<p>log4cpp::SimpleLayout &#8211; </p>
<p> <code>BasicLayout</code> is a simple fixed format <code>Layout</code> implementation.</p>
<h2>Synopsis</h2>
<p>#include &lt;SimpleLayout.hh&gt; </p>
<p> Inherits <code>log4cpp::Layout</code>.</p>
<h3>Public Member Functions</h3>
<p><code>SimpleLayout</code> () </p>
<p> virtual <code>~SimpleLayout</code> () </p>
<p> virtual std::string <code>format</code> (const <code>LoggingEvent</code> &amp;event)<br />
 <i>Formats the </i><code>LoggingEvent</code> in <code>SimpleLayout</code> style: </p>
<p>&nbsp;<wbr>&#8216;priority &#8211; message&#8217;.&nbsp;<wbr>&quot;</p>
<h2>Detailed Description</h2>
<p><code>BasicLayout</code> is a simple fixed format <code>Layout</code> implementation.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>log4cpp::SimpleLayout::SimpleLayout ()</h3>
<h3>log4cpp::SimpleLayout::~SimpleLayout () [virtual]</h3>
<h2>Member Function Documentation</h2>
<h3>std::string log4cpp::SimpleLayout::format (const <code>LoggingEvent</code> &amp;event) [virtual]</h3>
<p>Formats the <code>LoggingEvent</code> in <code>SimpleLayout</code> style: </p>
<p>&nbsp;<wbr>&#8216;priority &#8211; message&#8217;.&nbsp;<wbr> </p>
<p> Implements <code>log4cpp::Layout</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for log4cpp from the source code.</p>
