---
title: "log4cppnteventlogappender(3)"
name: "log4cppnteventlogappender"
section: "3"
letter: "l"
url: "/docs/linux/man/3-log4cppnteventlogappender/"
description: "log4cpp::NTEventLogAppender –"
---

<p>log4cpp::NTEventLogAppender &#8211; </p>
<p> <code>NTEventLogAppender</code> is an <code>Appender</code> that sends LoggingEvents to the Windows event log.</p>
<h2>Synopsis</h2>
<p>#include &lt;NTEventLogAppender.hh&gt; </p>
<p> Inherits <code>log4cpp::AppenderSkeleton</code>.</p>
<h3>Public Member Functions</h3>
<p><code>NTEventLogAppender</code> (const std::string &amp;name, const std::string &amp;sourceName)<br />
 <i>Instantiate an </i><code>NTEventLogAppender</code> with given name and source.<br />
 virtual <code>~NTEventLogAppender</code> () </p>
<p> virtual bool <code>reopen</code> ()<br />
 <i>Calls </i><code>open()</code> and <code>close()</code><br />
 virtual void <code>close</code> ()<br />
 <i>Release any resources allocated within the appender such as file handles, network connections, etc. </i><br />
 virtual bool <code>requiresLayout</code> () const<br />
 <i>The </i><code>NTEventLogAppender</code> does its own <code>Layout</code>.<br />
 virtual void <code>setLayout</code> (<code>Layout</code> *layout)<br />
 <i>Set the </i><code>Layout</code> for this appender.</p>
<h3>Protected Member Functions</h3>
<p>WORD <code>getCategory</code> (<code>Priority::Value</code> priority)<br />
 <i>Convert </i><code>log4cpp</code> <code>Priority</code> to an EventLog category.<br />
 WORD <code>getType</code> (<code>Priority::Value</code> priority)<br />
 <i>Convert </i><code>log4cpp</code> <code>Priority</code> to an EventLog type.<br />
 HKEY <code>regGetKey</code> (TCHAR *subkey, DWORD *disposition) </p>
<p> void <code>regSetString</code> (HKEY hkey, TCHAR *name, TCHAR *value) </p>
<p> void <code>regSetDword</code> (HKEY hkey, TCHAR *name, DWORD value) </p>
<p> void <code>addRegistryInfo</code> (const char *source) </p>
<p> virtual void <code>open</code> () </p>
<p> virtual void <code>_append</code> (const <code>LoggingEvent</code> &amp;event)<br />
 <i>Sends a </i><code>LoggingEvent</code> to NT Event log.</p>
<h3>Protected Attributes</h3>
<p>HANDLE <code>_hEventSource</code> </p>
<p> std::string <code>_strSourceName</code> </p>
<h3>Additional Inherited Members</h3>
<h2>Detailed Description</h2>
<p><code>NTEventLogAppender</code> is an <code>Appender</code> that sends LoggingEvents to the Windows event log. </p>
<p> Building log4cpp.dsp/log4cppDLL.dsp creates the resource DLL NTEventLogAppender.dll. Do not forget to place this DLL in a directory that is on the PATH of the Windows system. Otherwise, the category and message will not display correctly in Event Viewer. </p>
<p>&nbsp;<wbr><code>NB:</code>&nbsp;<wbr>This class is only available on Win32 platforms.&nbsp;<wbr></p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>log4cpp::NTEventLogAppender::NTEventLogAppender (const std::string &amp;name, const std::string &amp;sourceName)</h3>
<p>Instantiate an <code>NTEventLogAppender</code> with given name and source. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>name</i> The name of the <code>Appender</code><br />
 <i>sourceName</i> The source name to log</dl>
<h3>log4cpp::NTEventLogAppender::~NTEventLogAppender () [virtual]</h3>
<h2>Member Function Documentation</h2>
<h3>void log4cpp::NTEventLogAppender::_append (const <code>LoggingEvent</code> &amp;event) [protected], [virtual]</h3>
<p>Sends a <code>LoggingEvent</code> to NT Event log. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>event</i> the <code>LoggingEvent</code> to log.</dl>
<p> Implements <code>log4cpp::AppenderSkeleton</code>.</p>
<h3>void log4cpp::NTEventLogAppender::addRegistryInfo (const char *source) [protected]</h3>
<h3>void log4cpp::NTEventLogAppender::close () [virtual]</h3>
<p>Release any resources allocated within the appender such as file handles, network connections, etc. </p>
<p> Implements <code>log4cpp::AppenderSkeleton</code>.</p>
<h3>WORD log4cpp::NTEventLogAppender::getCategory (<code>Priority::Value</code>priority) [protected]</h3>
<p>Convert <code>log4cpp</code> <code>Priority</code> to an EventLog category. Each category is backed by a message resource so that proper category names will be displayed in the NT Event Viewer.</p>
<h3>WORD log4cpp::NTEventLogAppender::getType (<code>Priority::Value</code>priority) [protected]</h3>
<p>Convert <code>log4cpp</code> <code>Priority</code> to an EventLog type. The <code>log4cpp</code> package supports 8 defined priorites, but the NT EventLog only knows 3 event types of interest to us: ERROR, WARNING, and INFO.</p>
<h3>void log4cpp::NTEventLogAppender::open () [protected], [virtual]</h3>
<h3>HKEY log4cpp::NTEventLogAppender::regGetKey (TCHAR *subkey, DWORD *disposition) [protected]</h3>
<h3>void log4cpp::NTEventLogAppender::regSetDword (HKEYhkey, TCHAR *name, DWORDvalue) [protected]</h3>
<h3>void log4cpp::NTEventLogAppender::regSetString (HKEYhkey, TCHAR *name, TCHAR *value) [protected]</h3>
<h3>bool log4cpp::NTEventLogAppender::reopen () [virtual]</h3>
<p>Calls <code>open()</code> and <code>close()</code> </p>
<p> Reimplemented from <code>log4cpp::AppenderSkeleton</code>.</p>
<h3>bool log4cpp::NTEventLogAppender::requiresLayout () const [virtual]</h3>
<p>The <code>NTEventLogAppender</code> does its own <code>Layout</code>. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>false</dl>
<p> Implements <code>log4cpp::AppenderSkeleton</code>.</p>
<h3>void log4cpp::NTEventLogAppender::setLayout (<code>Layout</code> *layout) [virtual]</h3>
<p>Set the <code>Layout</code> for this appender. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>layout</i> The layout to use.</dl>
<p> Implements <code>log4cpp::AppenderSkeleton</code>.</p>
<h2>Member Data Documentation</h2>
<h3>HANDLE log4cpp::NTEventLogAppender::_hEventSource [protected]</h3>
<h3>std::string log4cpp::NTEventLogAppender::_strSourceName [protected]</h3>
<h2>Author</h2>
<p>Generated automatically by Doxygen for log4cpp from the source code.</p>
