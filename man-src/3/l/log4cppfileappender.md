---
title: "log4cppfileappender(3)"
name: "log4cppfileappender"
section: "3"
letter: "l"
url: "/docs/linux/man/3-log4cppfileappender/"
description: "log4cpp::FileAppender –"
---

<p>log4cpp::FileAppender &#8211; </p>
<h2>Synopsis</h2>
<p>#include &lt;FileAppender.hh&gt; </p>
<p> Inherits <code>log4cpp::LayoutAppender</code>. </p>
<p> Inherited by <code>log4cpp::RollingFileAppender</code>.</p>
<h3>Public Member Functions</h3>
<p><code>FileAppender</code> (const std::string &amp;name, const std::string &amp;fileName, bool append=true, mode_t mode=00644)<br />
 <i>Constructs a </i><code>FileAppender</code>.<br />
 <code>FileAppender</code> (const std::string &amp;name, int fd)<br />
 <i>Constructs a </i><code>FileAppender</code> to an already open file descriptor.<br />
 virtual <code>~FileAppender</code> () </p>
<p> virtual bool <code>reopen</code> ()<br />
 <i>Reopens the logfile. </i><br />
 virtual void <code>close</code> ()<br />
 <i>Closes the logfile. </i><br />
 virtual void <code>setAppend</code> (bool append)<br />
 <i>Sets the append vs truncate flag. </i><br />
 virtual bool <code>getAppend</code> () const<br />
 <i>Gets the value of the &#8216;append&#8217; option. </i><br />
 virtual void <code>setMode</code> (mode_t mode)<br />
 <i>Sets the file open mode. </i><br />
 virtual mode_t <code>getMode</code> () const<br />
 <i>Gets the file open mode. </i></p>
<h3>Protected Member Functions</h3>
<p>virtual void <code>_append</code> (const <code>LoggingEvent</code> &amp;event)<br />
 <i>Log in </i><code>Appender</code> specific way.</p>
<h3>Protected Attributes</h3>
<p>const std::string <code>_fileName</code> </p>
<p> int <code>_fd</code> </p>
<p> int <code>_flags</code> </p>
<p> mode_t <code>_mode</code> </p>
<h3>Additional Inherited Members</h3>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>log4cpp::FileAppender::FileAppender (const std::string &amp;name, const std::string &amp;fileName, boolappend = true, mode_tmode = 00644)</h3>
<p>Constructs a <code>FileAppender</code>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>name</i> the name of the <code>Appender</code>.<br />
 <i>fileName</i> the name of the file to which the <code>Appender</code> has to log.<br />
 <i>append</i> whether the <code>Appender</code> has to truncate the file or just append to it if it already exists. Defaults to &#8216;true&#8217;.<br />
 <i>mode</i> file mode to open the logfile with. Defaults to 00644.</dl>
<h3>log4cpp::FileAppender::FileAppender (const std::string &amp;name, intfd)</h3>
<p>Constructs a <code>FileAppender</code> to an already open file descriptor. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>name</i> the name of the <code>Appender</code>.<br />
 <i>fd</i> the file descriptor to which the <code>Appender</code> has to log.</dl>
<h3>log4cpp::FileAppender::~FileAppender () [virtual]</h3>
<h2>Member Function Documentation</h2>
<h3>void log4cpp::FileAppender::_append (const <code>LoggingEvent</code> &amp;event) [protected], [virtual]</h3>
<p>Log in <code>Appender</code> specific way. Subclasses of <code>Appender</code> should implement this method to perform actual logging. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>event</i> The <code>LoggingEvent</code> to log.</dl>
<p> Implements <code>log4cpp::AppenderSkeleton</code>. </p>
<p> Reimplemented in <code>log4cpp::RollingFileAppender</code>.</p>
<h3>void log4cpp::FileAppender::close () [virtual]</h3>
<p>Closes the logfile. </p>
<p> Implements <code>log4cpp::AppenderSkeleton</code>.</p>
<h3>bool log4cpp::FileAppender::getAppend () const [virtual]</h3>
<p>Gets the value of the &#8216;append&#8217; option.</p>
<h3>mode_t log4cpp::FileAppender::getMode () const [virtual]</h3>
<p>Gets the file open mode.</p>
<h3>bool log4cpp::FileAppender::reopen () [virtual]</h3>
<p>Reopens the logfile. This can be useful for logfiles that are rotated externally, e.g. by logrotate. This method is a NOOP for FileAppenders that have been constructed with a file descriptor. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>true if the reopen succeeded.</dl>
<p> Reimplemented from <code>log4cpp::AppenderSkeleton</code>.</p>
<h3>void log4cpp::FileAppender::setAppend (boolappend) [virtual]</h3>
<p>Sets the append vs truncate flag. NB. currently the <code>FileAppender</code> opens the logfile in the constructor. Therefore this method is too late to influence the first file opening. We&#8217;ll need something similar to log4j&#8217;s activateOptions(). </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>append</i> false to truncate, true to append</dl>
<h3>void log4cpp::FileAppender::setMode (mode_tmode) [virtual]</h3>
<p>Sets the file open mode.</p>
<h2>Member Data Documentation</h2>
<h3>int log4cpp::FileAppender::_fd [protected]</h3>
<h3>const std::string log4cpp::FileAppender::_fileName [protected]</h3>
<h3>int log4cpp::FileAppender::_flags [protected]</h3>
<h3>mode_t log4cpp::FileAppender::_mode [protected]</h3>
<h2>Author</h2>
<p>Generated automatically by Doxygen for log4cpp from the source code.</p>
