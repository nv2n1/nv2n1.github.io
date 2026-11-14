---
title: "log4cpppassthroughlayout(3)"
name: "log4cpppassthroughlayout"
section: "3"
letter: "l"
url: "/docs/linux/man/3-log4cpppassthroughlayout/"
description: "log4cpp::PassThroughLayout –"
---

<p>log4cpp::PassThroughLayout &#8211; </p>
<h2>Synopsis</h2>
<p>#include &lt;PassThroughLayout.hh&gt; </p>
<p> Inherits <code>log4cpp::Layout</code>.</p>
<h3>Public Member Functions</h3>
<p>virtual std::string <code>format</code> (const <code>LoggingEvent</code> &amp;event)<br />
 <i>Formats the </i><code>LoggingEvent</code> data to a string that appenders can log.</p>
<h2>Member Function Documentation</h2>
<h3>virtual std::string log4cpp::PassThroughLayout::format (const <code>LoggingEvent</code> &amp;event) [inline], [virtual]</h3>
<p>Formats the <code>LoggingEvent</code> data to a string that appenders can log. Implement this method to create your own layout format. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>event</i> The <code>LoggingEvent</code>.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>an appendable string.</dl>
<p> Implements <code>log4cpp::Layout</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for log4cpp from the source code.</p>
