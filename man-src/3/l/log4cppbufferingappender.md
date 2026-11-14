---
title: "log4cppbufferingappender(3)"
name: "log4cppbufferingappender"
section: "3"
letter: "l"
url: "/docs/linux/man/3-log4cppbufferingappender/"
description: "log4cpp::BufferingAppender –"
---

<p>log4cpp::BufferingAppender &#8211; </p>
<h2>Synopsis</h2>
<p>#include &lt;BufferingAppender.hh&gt; </p>
<p> Inherits <code>log4cpp::LayoutAppender</code>.</p>
<h3>Public Member Functions</h3>
<p><code>BufferingAppender</code> (const std::string name, unsigned long max_size, std::auto_ptr&lt; <code>Appender</code> &gt; sink, std::auto_ptr&lt; <code>TriggeringEventEvaluator</code> &gt; evaluator) </p>
<p> virtual void <code>close</code> ()<br />
 <i>Release any resources allocated within the appender such as file handles, network connections, etc. </i><br />
 bool <code>getLossy</code> () const </p>
<p> void <code>setLossy</code> (bool lossy) </p>
<h3>Protected Member Functions</h3>
<p>virtual void <code>_append</code> (const <code>LoggingEvent</code> &amp;event)<br />
 <i>Log in </i><code>Appender</code> specific way.</p>
<h3>Additional Inherited Members</h3>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>log4cpp::BufferingAppender::BufferingAppender (const std::stringname, unsigned longmax_size, std::auto_ptr&lt; <code>Appender</code> &gt;sink, std::auto_ptr&lt; <code>TriggeringEventEvaluator</code> &gt;evaluator)</h3>
<h2>Member Function Documentation</h2>
<h3>void log4cpp::BufferingAppender::_append (const <code>LoggingEvent</code> &amp;event) [protected], [virtual]</h3>
<p>Log in <code>Appender</code> specific way. Subclasses of <code>Appender</code> should implement this method to perform actual logging. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>event</i> The <code>LoggingEvent</code> to log.</dl>
<p> Implements <code>log4cpp::AppenderSkeleton</code>.</p>
<h3>virtual void log4cpp::BufferingAppender::close () [inline], [virtual]</h3>
<p>Release any resources allocated within the appender such as file handles, network connections, etc. </p>
<p> Implements <code>log4cpp::AppenderSkeleton</code>.</p>
<h3>bool log4cpp::BufferingAppender::getLossy () const [inline]</h3>
<h3>void log4cpp::BufferingAppender::setLossy (boollossy) [inline]</h3>
<h2>Author</h2>
<p>Generated automatically by Doxygen for log4cpp from the source code.</p>
