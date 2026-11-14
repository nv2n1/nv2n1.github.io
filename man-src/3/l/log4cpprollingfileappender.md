---
title: "log4cpprollingfileappender(3)"
name: "log4cpprollingfileappender"
section: "3"
letter: "l"
url: "/docs/linux/man/3-log4cpprollingfileappender/"
description: "log4cpp::RollingFileAppender –"
---

<p>log4cpp::RollingFileAppender &#8211; </p>
<p> <code>RollingFileAppender</code> is a <code>FileAppender</code> that rolls over the logfile once it has reached a certain size limit.</p>
<h2>Synopsis</h2>
<p>#include &lt;RollingFileAppender.hh&gt; </p>
<p> Inherits <code>log4cpp::FileAppender</code>.</p>
<h3>Public Member Functions</h3>
<p><code>RollingFileAppender</code> (const std::string &amp;name, const std::string &amp;fileName, size_t maxFileSize=10 *1024 *1024, unsigned int maxBackupIndex=1, bool append=true, mode_t mode=00644) </p>
<p> virtual void <code>setMaxBackupIndex</code> (unsigned int maxBackups) </p>
<p> virtual unsigned int <code>getMaxBackupIndex</code> () const </p>
<p> virtual void <code>setMaximumFileSize</code> (size_t maxFileSize) </p>
<p> virtual size_t <code>getMaxFileSize</code> () const </p>
<p> virtual void <code>rollOver</code> () </p>
<h3>Protected Member Functions</h3>
<p>virtual void <code>_append</code> (const <code>LoggingEvent</code> &amp;event)<br />
 <i>Log in </i><code>Appender</code> specific way.</p>
<h3>Protected Attributes</h3>
<p>unsigned int <code>_maxBackupIndex</code> </p>
<p> unsigned short int <code>_maxBackupIndexWidth</code> </p>
<p> size_t <code>_maxFileSize</code> </p>
<h3>Additional Inherited Members</h3>
<h2>Detailed Description</h2>
<p><code>RollingFileAppender</code> is a <code>FileAppender</code> that rolls over the logfile once it has reached a certain size limit. </p>
<p> <code>Since:</code></p>
<dl COMPACT>
<dd>0.3.1</dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>log4cpp::RollingFileAppender::RollingFileAppender (const std::string &amp;name, const std::string &amp;fileName, size_tmaxFileSize = 10*1024*1024, unsigned intmaxBackupIndex = 1, boolappend = true, mode_tmode = 00644)</h3>
<h2>Member Function Documentation</h2>
<h3>void log4cpp::RollingFileAppender::_append (const <code>LoggingEvent</code> &amp;event) [protected], [virtual]</h3>
<p>Log in <code>Appender</code> specific way. Subclasses of <code>Appender</code> should implement this method to perform actual logging. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>event</i> The <code>LoggingEvent</code> to log.</dl>
<p> Reimplemented from <code>log4cpp::FileAppender</code>.</p>
<h3>unsigned int log4cpp::RollingFileAppender::getMaxBackupIndex () const [virtual]</h3>
<h3>size_t log4cpp::RollingFileAppender::getMaxFileSize () const [virtual]</h3>
<h3>void log4cpp::RollingFileAppender::rollOver () [virtual]</h3>
<h3>void log4cpp::RollingFileAppender::setMaxBackupIndex (unsigned intmaxBackups) [virtual]</h3>
<h3>void log4cpp::RollingFileAppender::setMaximumFileSize (size_tmaxFileSize) [virtual]</h3>
<h2>Member Data Documentation</h2>
<h3>unsigned int log4cpp::RollingFileAppender::_maxBackupIndex [protected]</h3>
<h3>unsigned short int log4cpp::RollingFileAppender::_maxBackupIndexWidth [protected]</h3>
<h3>size_t log4cpp::RollingFileAppender::_maxFileSize [protected]</h3>
<h2>Author</h2>
<p>Generated automatically by Doxygen for log4cpp from the source code.</p>
