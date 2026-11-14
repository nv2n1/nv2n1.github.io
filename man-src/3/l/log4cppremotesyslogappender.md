---
title: "log4cppremotesyslogappender(3)"
name: "log4cppremotesyslogappender"
section: "3"
letter: "l"
url: "/docs/linux/man/3-log4cppremotesyslogappender/"
description: "log4cpp::RemoteSyslogAppender –"
---

<p>log4cpp::RemoteSyslogAppender &#8211; </p>
<p> <code>RemoteSyslogAppender</code> sends LoggingEvents to a remote syslog system.</p>
<h2>Synopsis</h2>
<p>#include &lt;RemoteSyslogAppender.hh&gt; </p>
<p> Inherits <code>log4cpp::LayoutAppender</code>.</p>
<h3>Public Member Functions</h3>
<p><code>RemoteSyslogAppender</code> (const std::string &amp;name, const std::string &amp;syslogName, const std::string &amp;relayer, int facility=<code>LOG_USER</code>, int portNumber=514)<br />
 <i>Instantiate a </i><code>RemoteSyslogAppender</code> with given name and name and facility for syslog.<br />
 virtual <code>~RemoteSyslogAppender</code> () </p>
<p> virtual bool <code>reopen</code> ()<br />
 <i>Closes and reopens the socket. </i><br />
 virtual void <code>close</code> ()<br />
 <i>Closes the socket. </i></p>
<h3>Static Public Member Functions</h3>
<p>static int <code>toSyslogPriority</code> (<code>Priority::Value</code> priority)<br />
 <i>Translates a </i><code>log4cpp</code> priority to a syslog priority.</p>
<h3>Protected Member Functions</h3>
<p>virtual void <code>open</code> ()<br />
 <i>Just creates the socket. </i><br />
 virtual void <code>_append</code> (const <code>LoggingEvent</code> &amp;event)<br />
 <i>Sends a </i><code>LoggingEvent</code> to the remote syslog.</p>
<h3>Protected Attributes</h3>
<p>const std::string <code>_syslogName</code> </p>
<p> const std::string <code>_relayer</code> </p>
<p> int <code>_facility</code> </p>
<p> int <code>_portNumber</code> </p>
<p> SOCKET <code>_socket</code> </p>
<p> in_addr_t <code>_ipAddr</code> </p>
<h3>Additional Inherited Members</h3>
<h2>Detailed Description</h2>
<p><code>RemoteSyslogAppender</code> sends LoggingEvents to a remote syslog system. </p>
<p> Also see: draft-ietf-syslog-syslog-12.txt</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>log4cpp::RemoteSyslogAppender::RemoteSyslogAppender (const std::string &amp;name, const std::string &amp;syslogName, const std::string &amp;relayer, intfacility = <code>LOG_USER</code>, intportNumber = 514)</h3>
<p>Instantiate a <code>RemoteSyslogAppender</code> with given name and name and facility for syslog. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>name</i> The name of the <code>Appender</code><br />
 <i>syslogName</i> The ident parameter in the <a href="/docs/linux/man/3-openlog/">openlog</a>(3) call.<br />
 <i>relayer</i> The IP address or hostname of a standard syslog host.<br />
 <i>facility</i> The syslog facility to log to. Defaults to LOG_USER. Value &#8216;-1&#8217; implies to use the default.<br />
 <i>portNumber</i> An alternative port number. Defaults to the standard syslog port number (514). Value &#8216;-1&#8217; implies to use the default.</dl>
<h3>log4cpp::RemoteSyslogAppender::~RemoteSyslogAppender () [virtual]</h3>
<h2>Member Function Documentation</h2>
<h3>void log4cpp::RemoteSyslogAppender::_append (const <code>LoggingEvent</code> &amp;event) [protected], [virtual]</h3>
<p>Sends a <code>LoggingEvent</code> to the remote syslog. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>event</i> the <code>LoggingEvent</code> to log.</dl>
<p> Implements <code>log4cpp::AppenderSkeleton</code>.</p>
<h3>void log4cpp::RemoteSyslogAppender::close () [virtual]</h3>
<p>Closes the socket. </p>
<p> Implements <code>log4cpp::AppenderSkeleton</code>.</p>
<h3>void log4cpp::RemoteSyslogAppender::open () [protected], [virtual]</h3>
<p>Just creates the socket.</p>
<h3>bool log4cpp::RemoteSyslogAppender::reopen () [virtual]</h3>
<p>Closes and reopens the socket. </p>
<p> Reimplemented from <code>log4cpp::AppenderSkeleton</code>.</p>
<h3>int log4cpp::RemoteSyslogAppender::toSyslogPriority (<code>Priority::Value</code>priority) [static]</h3>
<p>Translates a <code>log4cpp</code> priority to a syslog priority. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>priority</i> The <code>log4cpp</code> priority.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the syslog priority.</dl>
<h2>Member Data Documentation</h2>
<h3>int log4cpp::RemoteSyslogAppender::_facility [protected]</h3>
<h3>in_addr_t log4cpp::RemoteSyslogAppender::_ipAddr [protected]</h3>
<h3>int log4cpp::RemoteSyslogAppender::_portNumber [protected]</h3>
<h3>const std::string log4cpp::RemoteSyslogAppender::_relayer [protected]</h3>
<h3>SOCKET log4cpp::RemoteSyslogAppender::_socket [protected]</h3>
<h3>const std::string log4cpp::RemoteSyslogAppender::_syslogName [protected]</h3>
<h2>Author</h2>
<p>Generated automatically by Doxygen for log4cpp from the source code.</p>
