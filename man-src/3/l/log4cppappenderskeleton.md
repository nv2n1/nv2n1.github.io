---
title: "log4cppappenderskeleton(3)"
name: "log4cppappenderskeleton"
section: "3"
letter: "l"
url: "/docs/linux/man/3-log4cppappenderskeleton/"
description: "log4cpp::AppenderSkeleton –"
---

<p>log4cpp::AppenderSkeleton &#8211; </p>
<p> <code>AppenderSkeleton</code> is a helper class, simplifying implementation of Appenders: it already takes care of handling of Thresholds and Filters.</p>
<h2>Synopsis</h2>
<p>#include &lt;AppenderSkeleton.hh&gt; </p>
<p> Inherits <code>log4cpp::Appender</code>. </p>
<p> Inherited by <code>log4cpp::AbortAppender</code>, <code>log4cpp::IdsaAppender</code>, <code>log4cpp::LayoutAppender</code>, and <code>log4cpp::NTEventLogAppender</code>.</p>
<h3>Public Member Functions</h3>
<p>virtual <code>~AppenderSkeleton</code> ()<br />
 <i>Destructor for </i><code>AppenderSkeleton</code>.<br />
 virtual void <code>doAppend</code> (const <code>LoggingEvent</code> &amp;event)<br />
 <i>Log in </i><code>Appender</code> specific way.<br />
 virtual bool <code>reopen</code> ()<br />
 <i>Reopens the output destination of this </i><code>Appender</code>, e.g.<br />
 virtual void <code>close</code> ()=0<br />
 <i>Release any resources allocated within the appender such as file handles, network connections, etc. </i><br />
 virtual bool <code>requiresLayout</code> () const =0<br />
 <i>Check if the appender uses a layout. </i><br />
 virtual void <code>setLayout</code> (<code>Layout</code> *layout)=0<br />
 <i>Set the </i><code>Layout</code> for this appender.<br />
 virtual void <code>setThreshold</code> (<code>Priority::Value</code> priority)<br />
 <i>Set the threshold priority of this </i><code>Appender</code>.<br />
 virtual <code>Priority::Value</code> <code>getThreshold</code> ()<br />
 <i>Get the threshold priority of this </i><code>Appender</code>.<br />
 virtual void <code>setFilter</code> (<code>Filter</code> *filter)<br />
 <i>Set a </i><code>Filter</code> for this appender.<br />
 virtual <code>Filter</code> * <code>getFilter</code> ()<br />
 <i>Get the </i><code>Filter</code> for this appender.</p>
<h3>Protected Member Functions</h3>
<p><code>AppenderSkeleton</code> (const std::string &amp;name)<br />
 <i>Constructor for </i><code>AppenderSkeleton</code>.<br />
 virtual void <code>_append</code> (const <code>LoggingEvent</code> &amp;event)=0<br />
 <i>Log in </i><code>Appender</code> specific way.</p>
<h3>Additional Inherited Members</h3>
<h2>Detailed Description</h2>
<p><code>AppenderSkeleton</code> is a helper class, simplifying implementation of Appenders: it already takes care of handling of Thresholds and Filters.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>log4cpp::AppenderSkeleton::AppenderSkeleton (const std::string &amp;name) [protected]</h3>
<p>Constructor for <code>AppenderSkeleton</code>. Will only be used in <code>getAppender()</code> (and in derived classes of course). </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>name</i> The name of this <code>Appender</code>.</dl>
<h3>log4cpp::AppenderSkeleton::~AppenderSkeleton () [virtual]</h3>
<p>Destructor for <code>AppenderSkeleton</code>.</p>
<h2>Member Function Documentation</h2>
<h3>virtual void log4cpp::AppenderSkeleton::_append (const <code>LoggingEvent</code> &amp;event) [protected], [pure virtual]</h3>
<p>Log in <code>Appender</code> specific way. Subclasses of <code>Appender</code> should implement this method to perform actual logging. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>event</i> The <code>LoggingEvent</code> to log.</dl>
<p> Implemented in <code>log4cpp::RemoteSyslogAppender</code>, <code>log4cpp::NTEventLogAppender</code>, <code>log4cpp::FileAppender</code>, <code>log4cpp::SyslogAppender</code>, <code>log4cpp::IdsaAppender</code>, <code>log4cpp::StringQueueAppender</code>, <code>log4cpp::Win32DebugAppender</code>, <code>log4cpp::AbortAppender</code>, <code>log4cpp::RollingFileAppender</code>, <code>log4cpp::OstreamAppender</code>, and <code>log4cpp::BufferingAppender</code>.</p>
<h3>virtual void log4cpp::AppenderSkeleton::close () [pure virtual]</h3>
<p>Release any resources allocated within the appender such as file handles, network connections, etc. </p>
<p> Implements <code>log4cpp::Appender</code>. </p>
<p> Implemented in <code>log4cpp::RemoteSyslogAppender</code>, <code>log4cpp::NTEventLogAppender</code>, <code>log4cpp::SyslogAppender</code>, <code>log4cpp::FileAppender</code>, <code>log4cpp::IdsaAppender</code>, <code>log4cpp::Win32DebugAppender</code>, <code>log4cpp::StringQueueAppender</code>, <code>log4cpp::AbortAppender</code>, <code>log4cpp::OstreamAppender</code>, and <code>log4cpp::BufferingAppender</code>.</p>
<h3>void log4cpp::AppenderSkeleton::doAppend (const <code>LoggingEvent</code> &amp;event) [virtual]</h3>
<p>Log in <code>Appender</code> specific way. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>event</i> The <code>LoggingEvent</code> to log.</dl>
<p> Implements <code>log4cpp::Appender</code>.</p>
<h3><code>Filter</code> * log4cpp::AppenderSkeleton::getFilter () [virtual]</h3>
<p>Get the <code>Filter</code> for this appender. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the filter, or NULL if no filter has been set.</dl>
<p> Implements <code>log4cpp::Appender</code>.</p>
<h3><code>Priority::Value</code> log4cpp::AppenderSkeleton::getThreshold () [virtual]</h3>
<p>Get the threshold priority of this <code>Appender</code>. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the threshold</dl>
<p> Implements <code>log4cpp::Appender</code>.</p>
<h3>bool log4cpp::AppenderSkeleton::reopen () [virtual]</h3>
<p>Reopens the output destination of this <code>Appender</code>, e.g. the logfile or TCP socket. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>false if an error occured during reopening, true otherwise.</dl>
<p> Implements <code>log4cpp::Appender</code>. </p>
<p> Reimplemented in <code>log4cpp::RemoteSyslogAppender</code>, <code>log4cpp::NTEventLogAppender</code>, <code>log4cpp::SyslogAppender</code>, <code>log4cpp::FileAppender</code>, <code>log4cpp::IdsaAppender</code>, <code>log4cpp::StringQueueAppender</code>, <code>log4cpp::AbortAppender</code>, and <code>log4cpp::OstreamAppender</code>.</p>
<h3>virtual bool log4cpp::AppenderSkeleton::requiresLayout () const [pure virtual]</h3>
<p>Check if the appender uses a layout. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>true if the appender implementation requires a layout.</dl>
<p> Implements <code>log4cpp::Appender</code>. </p>
<p> Implemented in <code>log4cpp::NTEventLogAppender</code>, <code>log4cpp::IdsaAppender</code>, <code>log4cpp::LayoutAppender</code>, and <code>log4cpp::AbortAppender</code>.</p>
<h3>void log4cpp::AppenderSkeleton::setFilter (<code>Filter</code> *filter) [virtual]</h3>
<p>Set a <code>Filter</code> for this appender. </p>
<p> Implements <code>log4cpp::Appender</code>.</p>
<h3>virtual void log4cpp::AppenderSkeleton::setLayout (<code>Layout</code> *layout) [pure virtual]</h3>
<p>Set the <code>Layout</code> for this appender. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>layout</i> The layout to use.</dl>
<p> Implements <code>log4cpp::Appender</code>. </p>
<p> Implemented in <code>log4cpp::NTEventLogAppender</code>, <code>log4cpp::IdsaAppender</code>, <code>log4cpp::AbortAppender</code>, and <code>log4cpp::LayoutAppender</code>.</p>
<h3>void log4cpp::AppenderSkeleton::setThreshold (<code>Priority::Value</code>priority) [virtual]</h3>
<p>Set the threshold priority of this <code>Appender</code>. The <code>Appender</code> will not appender LoggingEvents with a priority lower than the threshold. Use <code>Priority::NOTSET</code> to disable threshold checking. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>priority</i> The priority to set.</dl>
<p> Implements <code>log4cpp::Appender</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for log4cpp from the source code.</p>
