---
title: "log4cppappender(3)"
name: "log4cppappender"
section: "3"
letter: "l"
url: "/docs/linux/man/3-log4cppappender/"
description: "log4cpp::Appender –"
---

<p>log4cpp::Appender &#8211; </p>
<p> Implement this interface for your own strategies for printing log statements.</p>
<h2>Synopsis</h2>
<p>#include &lt;Appender.hh&gt; </p>
<p> Inherited by <code>log4cpp::AppenderSkeleton</code>.</p>
<h3>Public Member Functions</h3>
<p>virtual <code>~Appender</code> ()<br />
 <i>Destructor for </i><code>Appender</code>.<br />
 virtual void <code>doAppend</code> (const <code>LoggingEvent</code> &amp;event)=0<br />
 <i>Log in </i><code>Appender</code> specific way.<br />
 virtual bool <code>reopen</code> ()=0<br />
 <i>Reopens the output destination of this </i><code>Appender</code>, e.g.<br />
 virtual void <code>close</code> ()=0<br />
 <i>Release any resources allocated within the appender such as file handles, network connections, etc. </i><br />
 virtual bool <code>requiresLayout</code> () const =0<br />
 <i>Check if the appender uses a layout. </i><br />
 virtual void <code>setLayout</code> (<code>Layout</code> *layout)=0<br />
 <i>Set the </i><code>Layout</code> for this appender.<br />
 const std::string &amp; <code>getName</code> () const<br />
 <i>Get the name of this appender. </i><br />
 virtual void <code>setThreshold</code> (<code>Priority::Value</code> priority)=0<br />
 <i>Set the threshold priority of this </i><code>Appender</code>.<br />
 virtual <code>Priority::Value</code> <code>getThreshold</code> ()=0<br />
 <i>Get the threshold priority of this </i><code>Appender</code>.<br />
 virtual void <code>setFilter</code> (<code>Filter</code> *filter)=0<br />
 <i>Set a </i><code>Filter</code> for this appender.<br />
 virtual <code>Filter</code> * <code>getFilter</code> ()=0<br />
 <i>Get the </i><code>Filter</code> for this appender.</p>
<h3>Static Public Member Functions</h3>
<p>static <code>Appender</code> * <code>getAppender</code> (const std::string &amp;name)<br />
 <i>Get a pointer to an exitsing </i><code>Appender</code>.<br />
 static bool <code>reopenAll</code> ()<br />
 <i>Call </i><code>reopen()</code> on all existing Appenders.<br />
 static void <code>closeAll</code> ()<br />
 <i>Call </i><code>reopen()</code> on all existing Appenders.</p>
<h3>Protected Member Functions</h3>
<p><code>Appender</code> (const std::string &amp;name)<br />
 <i>Constructor for </i><code>Appender</code>.</p>
<h2>Detailed Description</h2>
<p>Implement this interface for your own strategies for printing log statements.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>log4cpp::Appender::Appender (const std::string &amp;name) [protected]</h3>
<p>Constructor for <code>Appender</code>. Will only be used in <code>getAppender()</code> (and in derived classes of course). </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>name</i> The name of this <code>Appender</code>.</dl>
<h3>log4cpp::Appender::~Appender () [virtual]</h3>
<p>Destructor for <code>Appender</code>.</p>
<h2>Member Function Documentation</h2>
<h3>virtual void log4cpp::Appender::close () [pure virtual]</h3>
<p>Release any resources allocated within the appender such as file handles, network connections, etc. </p>
<p> Implemented in <code>log4cpp::RemoteSyslogAppender</code>, <code>log4cpp::NTEventLogAppender</code>, <code>log4cpp::AppenderSkeleton</code>, <code>log4cpp::SyslogAppender</code>, <code>log4cpp::FileAppender</code>, <code>log4cpp::IdsaAppender</code>, <code>log4cpp::Win32DebugAppender</code>, <code>log4cpp::StringQueueAppender</code>, <code>log4cpp::AbortAppender</code>, <code>log4cpp::OstreamAppender</code>, and <code>log4cpp::BufferingAppender</code>.</p>
<h3>void log4cpp::Appender::closeAll () [static]</h3>
<p>Call <code>reopen()</code> on all existing Appenders. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>true if all Appenders returned true on their <code>reopen()</code> call.</dl>
<h3>virtual void log4cpp::Appender::doAppend (const <code>LoggingEvent</code> &amp;event) [pure virtual]</h3>
<p>Log in <code>Appender</code> specific way. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>event</i> The <code>LoggingEvent</code> to log.</dl>
<p> Implemented in <code>log4cpp::AppenderSkeleton</code>.</p>
<h3><code>Appender</code> * log4cpp::Appender::getAppender (const std::string &amp;name) [static]</h3>
<p>Get a pointer to an exitsing <code>Appender</code>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>name</i> The name of the <code>Appender</code> to return.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>a pointer to an existing <code>Appender</code>, or NULL if no appender with the specfied name exists.</dl>
<h3>virtual <code>Filter</code>* log4cpp::Appender::getFilter () [pure virtual]</h3>
<p>Get the <code>Filter</code> for this appender. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the filter, or NULL if no filter has been set.</dl>
<p> Implemented in <code>log4cpp::AppenderSkeleton</code>.</p>
<h3>const std::string&amp; log4cpp::Appender::getName () const [inline]</h3>
<p>Get the name of this appender. The name identifies the appender. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the name of the appender.</dl>
<h3>virtual <code>Priority::Value</code> log4cpp::Appender::getThreshold () [pure virtual]</h3>
<p>Get the threshold priority of this <code>Appender</code>. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the threshold</dl>
<p> Implemented in <code>log4cpp::AppenderSkeleton</code>.</p>
<h3>virtual bool log4cpp::Appender::reopen () [pure virtual]</h3>
<p>Reopens the output destination of this <code>Appender</code>, e.g. the logfile or TCP socket. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>false if an error occured during reopening, true otherwise.</dl>
<p> Implemented in <code>log4cpp::RemoteSyslogAppender</code>, <code>log4cpp::NTEventLogAppender</code>, <code>log4cpp::SyslogAppender</code>, <code>log4cpp::AppenderSkeleton</code>, <code>log4cpp::FileAppender</code>, <code>log4cpp::IdsaAppender</code>, <code>log4cpp::StringQueueAppender</code>, <code>log4cpp::AbortAppender</code>, and <code>log4cpp::OstreamAppender</code>.</p>
<h3>bool log4cpp::Appender::reopenAll () [static]</h3>
<p>Call <code>reopen()</code> on all existing Appenders. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>true if all Appenders returned true on their <code>reopen()</code> call.</dl>
<h3>virtual bool log4cpp::Appender::requiresLayout () const [pure virtual]</h3>
<p>Check if the appender uses a layout. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>true if the appender implementation requires a layout.</dl>
<p> Implemented in <code>log4cpp::NTEventLogAppender</code>, <code>log4cpp::AppenderSkeleton</code>, <code>log4cpp::IdsaAppender</code>, <code>log4cpp::LayoutAppender</code>, and <code>log4cpp::AbortAppender</code>.</p>
<h3>virtual void log4cpp::Appender::setFilter (<code>Filter</code> *filter) [pure virtual]</h3>
<p>Set a <code>Filter</code> for this appender. </p>
<p> Implemented in <code>log4cpp::AppenderSkeleton</code>.</p>
<h3>virtual void log4cpp::Appender::setLayout (<code>Layout</code> *layout) [pure virtual]</h3>
<p>Set the <code>Layout</code> for this appender. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>layout</i> The layout to use.</dl>
<p> Implemented in <code>log4cpp::NTEventLogAppender</code>, <code>log4cpp::AppenderSkeleton</code>, <code>log4cpp::IdsaAppender</code>, <code>log4cpp::AbortAppender</code>, and <code>log4cpp::LayoutAppender</code>.</p>
<h3>virtual void log4cpp::Appender::setThreshold (<code>Priority::Value</code>priority) [pure virtual]</h3>
<p>Set the threshold priority of this <code>Appender</code>. The <code>Appender</code> will not appender LoggingEvents with a priority lower than the threshold. Use <code>Priority::NOTSET</code> to disable threshold checking. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>priority</i> The priority to set.</dl>
<p> Implemented in <code>log4cpp::AppenderSkeleton</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for log4cpp from the source code.</p>
