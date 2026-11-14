---
title: "log4cpplayoutappender(3)"
name: "log4cpplayoutappender"
section: "3"
letter: "l"
url: "/docs/linux/man/3-log4cpplayoutappender/"
description: "log4cpp::LayoutAppender –"
---

<p>log4cpp::LayoutAppender &#8211; </p>
<p> <code>LayoutAppender</code> is a common superclass for all Appenders that require a <code>Layout</code>.</p>
<h2>Synopsis</h2>
<p>#include &lt;LayoutAppender.hh&gt; </p>
<p> Inherits <code>log4cpp::AppenderSkeleton</code>. </p>
<p> Inherited by <code>log4cpp::BufferingAppender</code>, <code>log4cpp::FileAppender</code>, <code>log4cpp::OstreamAppender</code>, <code>log4cpp::RemoteSyslogAppender</code>, <code>log4cpp::StringQueueAppender</code>, <code>log4cpp::SyslogAppender</code>, and <code>log4cpp::Win32DebugAppender</code>.</p>
<h3>Public Types</h3>
<p>typedef <code>BasicLayout</code> <code>DefaultLayoutType</code> </p>
<h3>Public Member Functions</h3>
<p><code>LayoutAppender</code> (const std::string &amp;name) </p>
<p> virtual <code>~LayoutAppender</code> () </p>
<p> virtual bool <code>requiresLayout</code> () const<br />
 <i>Check if the appender requires a layout. </i><br />
 virtual void <code>setLayout</code> (<code>Layout</code> *layout=NULL)<br />
 <i>Set the </i><code>Layout</code> for this appender.</p>
<h3>Protected Member Functions</h3>
<p><code>Layout</code> &amp; <code>_getLayout</code> ()<br />
 <i>Return the layout of the appender. </i></p>
<h3>Additional Inherited Members</h3>
<h2>Detailed Description</h2>
<p><code>LayoutAppender</code> is a common superclass for all Appenders that require a <code>Layout</code>.</p>
<h2>Member Typedef Documentation</h2>
<h3>typedef <code>BasicLayout</code> <code>log4cpp::LayoutAppender::DefaultLayoutType</code></h3>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>log4cpp::LayoutAppender::LayoutAppender (const std::string &amp;name)</h3>
<h3>log4cpp::LayoutAppender::~LayoutAppender () [virtual]</h3>
<h2>Member Function Documentation</h2>
<h3><code>Layout</code> &amp; log4cpp::LayoutAppender::_getLayout () [protected]</h3>
<p>Return the layout of the appender. This method is the <code>Layout</code> accessor for subclasses of <code>LayoutAppender</code>. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the <code>Layout</code>.</dl>
<h3>bool log4cpp::LayoutAppender::requiresLayout () const [virtual]</h3>
<p>Check if the appender requires a layout. All LayoutAppenders do, therefore this method returns true for all subclasses. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>true.</dl>
<p> Implements <code>log4cpp::AppenderSkeleton</code>.</p>
<h3>void log4cpp::LayoutAppender::setLayout (<code>Layout</code> *layout = NULL) [virtual]</h3>
<p>Set the <code>Layout</code> for this appender. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>layout</i> The layout to use.</dl>
<p> Implements <code>log4cpp::AppenderSkeleton</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for log4cpp from the source code.</p>
