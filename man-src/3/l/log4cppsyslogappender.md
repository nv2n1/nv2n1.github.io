---
title: "log4cppsyslogappender(3)"
name: "log4cppsyslogappender"
section: "3"
letter: "l"
url: "/docs/linux/man/3-log4cppsyslogappender/"
description: "log4cpp::SyslogAppender –"
---

<p>log4cpp::SyslogAppender &#8211; </p>
<p> <code>SyslogAppender</code> sends LoggingEvents to the local syslog system.</p>
<h2>Synopsis</h2>
<p>#include &lt;SyslogAppender.hh&gt; </p>
<p> Inherits <code>log4cpp::LayoutAppender</code>.</p>
<h3>Public Member Functions</h3>
<p><code>SyslogAppender</code> (const std::string &amp;name, const std::string &amp;syslogName, int facility=<code>LOG_USER</code>)<br />
 <i>Instantiate a </i><code>SyslogAppender</code> with given name and name and facility for syslog.<br />
 virtual <code>~SyslogAppender</code> () </p>
<p> virtual bool <code>reopen</code> ()<br />
 <i>Calls <a href="/docs/linux/man/3-closelog/">closelog</a>(3) and <a href="/docs/linux/man/3-openlog/">openlog</a>(3). </i><br />
 virtual void <code>close</code> ()<br />
 <i>Calls <a href="/docs/linux/man/3-closelog/">closelog</a>(3) to close the syslog file descriptor. </i></p>
<h3>Static Public Member Functions</h3>
<p>static int <code>toSyslogPriority</code> (<code>Priority::Value</code> priority)<br />
 <i>Translates a </i><code>log4cpp</code> priority to a syslog priority.</p>
<h3>Protected Member Functions</h3>
<p>virtual void <code>open</code> ()<br />
 <i>Calls <a href="/docs/linux/man/3-openlog/">openlog</a>(3). </i><br />
 virtual void <code>_append</code> (const <code>LoggingEvent</code> &amp;event)<br />
 <i>Sends a </i><code>LoggingEvent</code> to syslog.</p>
<h3>Protected Attributes</h3>
<p>const std::string <code>_syslogName</code> </p>
<p> int <code>_facility</code> </p>
<h3>Additional Inherited Members</h3>
<h2>Detailed Description</h2>
<p><code>SyslogAppender</code> sends LoggingEvents to the local syslog system.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>log4cpp::SyslogAppender::SyslogAppender (const std::string &amp;name, const std::string &amp;syslogName, intfacility = <code>LOG_USER</code>)</h3>
<p>Instantiate a <code>SyslogAppender</code> with given name and name and facility for syslog. Note that the C syslog API is process global, so instantion of a second <code>SyslogAppender</code> will &#8216;overwrite&#8217; the syslog name of the first. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>name</i> The name of the <code>Appender</code><br />
 <i>syslogName</i> The ident parameter in the <a href="/docs/linux/man/3-openlog/">openlog</a>(3) call.<br />
 <i>facility</i> The syslog facility to log to. Defaults to LOG_USER.</dl>
<h3>virtual log4cpp::SyslogAppender::~SyslogAppender () [virtual]</h3>
<h2>Member Function Documentation</h2>
<h3>virtual void log4cpp::SyslogAppender::_append (const <code>LoggingEvent</code> &amp;event) [protected], [virtual]</h3>
<p>Sends a <code>LoggingEvent</code> to syslog. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>event</i> the <code>LoggingEvent</code> to log.</dl>
<p> Implements <code>log4cpp::AppenderSkeleton</code>.</p>
<h3>virtual void log4cpp::SyslogAppender::close () [virtual]</h3>
<p>Calls <a href="/docs/linux/man/3-closelog/">closelog</a>(3) to close the syslog file descriptor. </p>
<p> Implements <code>log4cpp::AppenderSkeleton</code>.</p>
<h3>virtual void log4cpp::SyslogAppender::open () [protected], [virtual]</h3>
<p>Calls <a href="/docs/linux/man/3-openlog/">openlog</a>(3).</p>
<h3>virtual bool log4cpp::SyslogAppender::reopen () [virtual]</h3>
<p>Calls <a href="/docs/linux/man/3-closelog/">closelog</a>(3) and <a href="/docs/linux/man/3-openlog/">openlog</a>(3). </p>
<p> Reimplemented from <code>log4cpp::AppenderSkeleton</code>.</p>
<h3>static int log4cpp::SyslogAppender::toSyslogPriority (<code>Priority::Value</code>priority) [static]</h3>
<p>Translates a <code>log4cpp</code> priority to a syslog priority. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>priority</i> The <code>log4cpp</code> priority.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the syslog priority.</dl>
<h2>Member Data Documentation</h2>
<h3>int log4cpp::SyslogAppender::_facility [protected]</h3>
<h3>const std::string log4cpp::SyslogAppender::_syslogName [protected]</h3>
<h2>Author</h2>
<p>Generated automatically by Doxygen for log4cpp from the source code.</p>
