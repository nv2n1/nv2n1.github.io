---
title: "log4cppostreamappender(3)"
name: "log4cppostreamappender"
section: "3"
letter: "l"
url: "/docs/linux/man/3-log4cppostreamappender/"
description: "log4cpp::OstreamAppender –"
---

<p>log4cpp::OstreamAppender &#8211; </p>
<p> <code>OstreamAppender</code> appends LoggingEvents to ostreams.</p>
<h2>Synopsis</h2>
<p>#include &lt;OstreamAppender.hh&gt; </p>
<p> Inherits <code>log4cpp::LayoutAppender</code>.</p>
<h3>Public Member Functions</h3>
<p><code>OstreamAppender</code> (const std::string &amp;name, std::ostream *stream) </p>
<p> virtual <code>~OstreamAppender</code> () </p>
<p> virtual bool <code>reopen</code> ()<br />
 <i>Reopens the output destination of this </i><code>Appender</code>, e.g.<br />
 virtual void <code>close</code> ()<br />
 <i>Release any resources allocated within the appender such as file handles, network connections, etc. </i></p>
<h3>Protected Member Functions</h3>
<p>virtual void <code>_append</code> (const <code>LoggingEvent</code> &amp;event)<br />
 <i>Log in </i><code>Appender</code> specific way.</p>
<h3>Protected Attributes</h3>
<p>std::ostream * <code>_stream</code> </p>
<h3>Additional Inherited Members</h3>
<h2>Detailed Description</h2>
<p><code>OstreamAppender</code> appends LoggingEvents to ostreams.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>log4cpp::OstreamAppender::OstreamAppender (const std::string &amp;name, std::ostream *stream)</h3>
<h3>log4cpp::OstreamAppender::~OstreamAppender () [virtual]</h3>
<h2>Member Function Documentation</h2>
<h3>void log4cpp::OstreamAppender::_append (const <code>LoggingEvent</code> &amp;event) [protected], [virtual]</h3>
<p>Log in <code>Appender</code> specific way. Subclasses of <code>Appender</code> should implement this method to perform actual logging. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>event</i> The <code>LoggingEvent</code> to log.</dl>
<p> Implements <code>log4cpp::AppenderSkeleton</code>.</p>
<h3>void log4cpp::OstreamAppender::close () [virtual]</h3>
<p>Release any resources allocated within the appender such as file handles, network connections, etc. </p>
<p> Implements <code>log4cpp::AppenderSkeleton</code>.</p>
<h3>bool log4cpp::OstreamAppender::reopen () [virtual]</h3>
<p>Reopens the output destination of this <code>Appender</code>, e.g. the logfile or TCP socket. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>false if an error occured during reopening, true otherwise.</dl>
<p> Reimplemented from <code>log4cpp::AppenderSkeleton</code>.</p>
<h2>Member Data Documentation</h2>
<h3>std::ostream* log4cpp::OstreamAppender::_stream [protected]</h3>
<h2>Author</h2>
<p>Generated automatically by Doxygen for log4cpp from the source code.</p>
