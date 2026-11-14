---
title: "log4cpplayout(3)"
name: "log4cpplayout"
section: "3"
letter: "l"
url: "/docs/linux/man/3-log4cpplayout/"
description: "log4cpp::Layout –"
---

<p>log4cpp::Layout &#8211; </p>
<p> Extend this abstract class to create your own log layout format.</p>
<h2>Synopsis</h2>
<p>#include &lt;Layout.hh&gt; </p>
<p> Inherited by <code>log4cpp::BasicLayout</code>, <code>log4cpp::PassThroughLayout</code>, <code>log4cpp::PatternLayout</code>, and <code>log4cpp::SimpleLayout</code>.</p>
<h3>Public Member Functions</h3>
<p>virtual <code>~Layout</code> ()<br />
 <i>Destructor for </i><code>Layout</code>.<br />
 virtual std::string <code>format</code> (const <code>LoggingEvent</code> &amp;event)=0<br />
 <i>Formats the </i><code>LoggingEvent</code> data to a string that appenders can log.</p>
<h2>Detailed Description</h2>
<p>Extend this abstract class to create your own log layout format.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>virtual log4cpp::Layout::~Layout () [inline], [virtual]</h3>
<p>Destructor for <code>Layout</code>.</p>
<h2>Member Function Documentation</h2>
<h3>virtual std::string log4cpp::Layout::format (const <code>LoggingEvent</code> &amp;event) [pure virtual]</h3>
<p>Formats the <code>LoggingEvent</code> data to a string that appenders can log. Implement this method to create your own layout format. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>event</i> The <code>LoggingEvent</code>.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>an appendable string.</dl>
<p> Implemented in <code>log4cpp::PatternLayout</code>, <code>log4cpp::BasicLayout</code>, <code>log4cpp::SimpleLayout</code>, and <code>log4cpp::PassThroughLayout</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for log4cpp from the source code.</p>
