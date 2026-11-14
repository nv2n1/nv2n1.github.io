---
title: "log4cppabortappender(3)"
name: "log4cppabortappender"
section: "3"
letter: "l"
url: "/docs/linux/man/3-log4cppabortappender/"
description: "log4cpp::AbortAppender –"
---

<p>log4cpp::AbortAppender &#8211; </p>
<p> This <code>Appender</code> causes the application to abort() upon the first append() call.</p>
<h2>Synopsis</h2>
<p>#include &lt;AbortAppender.hh&gt; </p>
<p> Inherits <code>log4cpp::AppenderSkeleton</code>.</p>
<h3>Public Member Functions</h3>
<p><code>AbortAppender</code> (const std::string &amp;name) </p>
<p> virtual <code>~AbortAppender</code> () </p>
<p> virtual bool <code>reopen</code> ()<br />
 <i>Reopens the output destination of this </i><code>Appender</code>, e.g.<br />
 virtual void <code>close</code> ()<br />
 <i>Release any resources allocated within the appender such as file handles, network connections, etc. </i><br />
 virtual bool <code>requiresLayout</code> () const<br />
 <i>The </i><code>AbortAppender</code> does not layout.<br />
 virtual void <code>setLayout</code> (<code>Layout</code> *layout)<br />
 <i>Set the </i><code>Layout</code> for this appender.</p>
<h3>Protected Member Functions</h3>
<p>virtual void <code>_append</code> (const <code>LoggingEvent</code> &amp;event)<br />
 <i>Log in </i><code>Appender</code> specific way.</p>
<h3>Additional Inherited Members</h3>
<h2>Detailed Description</h2>
<p>This <code>Appender</code> causes the application to abort() upon the first append() call. </p>
<p> <code>Since:</code></p>
<dl COMPACT>
<dd>0.3.5</dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>log4cpp::AbortAppender::AbortAppender (const std::string &amp;name)</h3>
<h3>log4cpp::AbortAppender::~AbortAppender () [virtual]</h3>
<h2>Member Function Documentation</h2>
<h3>void log4cpp::AbortAppender::_append (const <code>LoggingEvent</code> &amp;event) [protected], [virtual]</h3>
<p>Log in <code>Appender</code> specific way. Subclasses of <code>Appender</code> should implement this method to perform actual logging. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>event</i> The <code>LoggingEvent</code> to log.</dl>
<p> Implements <code>log4cpp::AppenderSkeleton</code>.</p>
<h3>void log4cpp::AbortAppender::close () [virtual]</h3>
<p>Release any resources allocated within the appender such as file handles, network connections, etc. </p>
<p> Implements <code>log4cpp::AppenderSkeleton</code>.</p>
<h3>bool log4cpp::AbortAppender::reopen () [virtual]</h3>
<p>Reopens the output destination of this <code>Appender</code>, e.g. the logfile or TCP socket. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>false if an error occured during reopening, true otherwise.</dl>
<p> Reimplemented from <code>log4cpp::AppenderSkeleton</code>.</p>
<h3>bool log4cpp::AbortAppender::requiresLayout () const [virtual]</h3>
<p>The <code>AbortAppender</code> does not layout. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>false</dl>
<p> Implements <code>log4cpp::AppenderSkeleton</code>.</p>
<h3>void log4cpp::AbortAppender::setLayout (<code>Layout</code> *layout) [virtual]</h3>
<p>Set the <code>Layout</code> for this appender. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>layout</i> The layout to use.</dl>
<p> Implements <code>log4cpp::AppenderSkeleton</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for log4cpp from the source code.</p>
