---
title: "log4cppwin32debugappender(3)"
name: "log4cppwin32debugappender"
section: "3"
letter: "l"
url: "/docs/linux/man/3-log4cppwin32debugappender/"
description: "log4cpp::Win32DebugAppender –"
---

<p>log4cpp::Win32DebugAppender &#8211; </p>
<p> <code>Win32DebugAppender</code> simply sends the log message to the default system debugger on Win32 systems.</p>
<h2>Synopsis</h2>
<p>#include &lt;Win32DebugAppender.hh&gt; </p>
<p> Inherits <code>log4cpp::LayoutAppender</code>.</p>
<h3>Public Member Functions</h3>
<p><code>Win32DebugAppender</code> (const std::string &amp;name)<br />
 <i>Constructor. </i><br />
 virtual <code>~Win32DebugAppender</code> ()<br />
 <i>Destructor. </i><br />
 virtual void <code>close</code> ()<br />
 <i>Close method. </i></p>
<h3>Protected Member Functions</h3>
<p>virtual void <code>_append</code> (const <code>LoggingEvent</code> &amp;event)<br />
 <i>Method that does the actual work. </i></p>
<h3>Additional Inherited Members</h3>
<h2>Detailed Description</h2>
<p><code>Win32DebugAppender</code> simply sends the log message to the default system debugger on Win32 systems. </p>
<p> This is useful for users of MSVC and Borland because the log messages will show up in the debugger window. </p>
<p>&nbsp;<wbr><code>NB:</code>&nbsp;<wbr>This class is only available on Win32 platforms.&nbsp;<wbr></p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>log4cpp::Win32DebugAppender::Win32DebugAppender (const std::string &amp;name)</h3>
<p>Constructor. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>name</i> Name used by the base classes only.</dl>
<h3>log4cpp::Win32DebugAppender::~Win32DebugAppender () [virtual]</h3>
<p>Destructor.</p>
<h2>Member Function Documentation</h2>
<h3>void log4cpp::Win32DebugAppender::_append (const <code>LoggingEvent</code> &amp;event) [protected], [virtual]</h3>
<p>Method that does the actual work. In this case, it simply sets up the layout and calls the OutputDebugString API. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>event</i> Event for which we are logging.</dl>
<p> Implements <code>log4cpp::AppenderSkeleton</code>.</p>
<h3>void log4cpp::Win32DebugAppender::close () [virtual]</h3>
<p>Close method. This is called by the framework, but there is nothing to do for the OutputDebugString API, so it simply returns. </p>
<p> Implements <code>log4cpp::AppenderSkeleton</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for log4cpp from the source code.</p>
