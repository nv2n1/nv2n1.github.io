---
title: "log4cpp(3)"
name: "log4cpp"
section: "3"
letter: "l"
url: "/docs/linux/man/3-log4cpp/"
description: "log4cpp –"
---

<h2 class="name">NAME</h2>
<p> log4cpp &#8211; </p>
<p> The top level namespace for all &#8216;Log for C++&#8217; types and classes.</p>
<h2>SYNOPSIS</h2>
<h3>Namespaces</h3>
<p> <code>details</code> </p>
<p> <code>threading</code> </p>
<h3>Classes</h3>
<p> class <code>AbortAppender</code><br />
 <i>This </i><code>Appender</code> causes the application to abort() upon the first append() call.<br />
 class <code>Appender</code><br />
 <i>Implement this interface for your own strategies for printing log statements. </i><br />
 class <code>AppendersFactory</code> </p>
<p> class <code>AppenderSkeleton</code><br />
 <i></i><code>AppenderSkeleton</code> is a helper class, simplifying implementation of Appenders: it already takes care of handling of Thresholds and Filters.<br />
 class <code>BasicConfigurator</code><br />
 <i>This class implements a trivial default configuration for </i><code>log4cpp</code>: it adds a <code>FileAppender</code> that logs to stdout and uses a <code>BasicLayout</code> to the root <code>Category</code>.<br />
 class <code>BasicLayout</code><br />
 <i></i><code>BasicLayout</code> is a simple fixed format <code>Layout</code> implementation.<br />
 class <code>BufferingAppender</code> </p>
<p> class <code>Category</code><br />
 <i>This is the central class in the log4j package. </i><br />
 class <code>CategoryStream</code><br />
 <i>This class enables streaming simple types and objects to a category. </i><br />
 class <code>ConfigureFailure</code><br />
 <i>Exception class for configuration. </i><br />
 class <code>FactoryParams</code> </p>
<p> class <code>FileAppender</code> </p>
<p> class <code>Filter</code><br />
 <i>Users should extend this class to implement customized logging event filtering. </i><br />
 class <code>FixedContextCategory</code><br />
 <i>This </i><code>Category</code> subclass replaces the <code>NDC</code> field in LoggingEvents with a fixed context string.<br />
 class <code>HierarchyMaintainer</code><br />
 <i></i><code>HierarchyMaintainer</code> is an internal <code>log4cpp</code> class.<br />
 class <code>IdsaAppender</code><br />
 <i></i><code>IdsaAppender</code> is an <code>Appender</code> that sends LoggingEvents to the IDS/A logger and reference monitor by Marc Welz.<br />
 class <code>Layout</code><br />
 <i>Extend this abstract class to create your own log layout format. </i><br />
 class <code>LayoutAppender</code><br />
 <i></i><code>LayoutAppender</code> is a common superclass for all Appenders that require a <code>Layout</code>.<br />
 class <code>LayoutsFactory</code> </p>
<p> class <code>LevelEvaluator</code> </p>
<p> struct <code>LoggingEvent</code><br />
 <i>The internal representation of logging events. </i><br />
 class <code>width</code> </p>
<p> class <code>tab</code> </p>
<p> class <code>NDC</code><br />
 <i>The </i><code>NDC</code> class implements <i>nested diagnostic contexts</i> as defined by Neil Harrison in the article &#8216;Patterns for Logging Diagnostic Messages&#8217; part of the book &#8216;&lt;i&gt;Pattern Languages of Program Design 3&lt;/i&gt;&#8217; edited by Martin et al. &quot;<br />
 class <code>NTEventLogAppender</code><br />
 <i></i><code>NTEventLogAppender</code> is an <code>Appender</code> that sends LoggingEvents to the Windows event log.<br />
 class <code>OstreamAppender</code><br />
 <i></i><code>OstreamAppender</code> appends LoggingEvents to ostreams.<br />
 class <code>PassThroughLayout</code> </p>
<p> class <code>PatternLayout</code><br />
 <i></i><code>PatternLayout</code> is a simple fixed format <code>Layout</code> implementation.<br />
 class <code>Priority</code><br />
 <i>The </i><code>Priority</code> class provides importance levels with which one can categorize log messages.<br />
 class <code>PropertyConfigurator</code><br />
 <i>Property configurator will read a config file using the same (or similar) format to the config file used by log4j. </i><br />
 class <code>RemoteSyslogAppender</code><br />
 <i></i><code>RemoteSyslogAppender</code> sends LoggingEvents to a remote syslog system.<br />
 class <code>RollingFileAppender</code><br />
 <i></i><code>RollingFileAppender</code> is a <code>FileAppender</code> that rolls over the logfile once it has reached a certain size limit.<br />
 class <code>SimpleConfigurator</code><br />
 <i>This class implements a simple Configurator for </i><code>log4cpp</code>.<br />
 class <code>SimpleLayout</code><br />
 <i></i><code>BasicLayout</code> is a simple fixed format <code>Layout</code> implementation.<br />
 class <code>StringQueueAppender</code><br />
 <i>This class puts log messages in an in-memory queue. </i><br />
 class <code>SyslogAppender</code><br />
 <i></i><code>SyslogAppender</code> sends LoggingEvents to the local syslog system.<br />
 class <code>TimeStamp</code><br />
 <i>A simple </i><code>TimeStamp</code> abstraction.<br />
 class <code>TriggeringEventEvaluator</code> </p>
<p> class <code>TriggeringEventEvaluatorFactory</code> </p>
<p> class <code>Win32DebugAppender</code><br />
 <i></i><code>Win32DebugAppender</code> simply sends the log message to the default system debugger on Win32 systems.<br />
 struct <code>StringLiteralComponent</code> </p>
<p> struct <code>CategoryNameComponent</code> </p>
<p> struct <code>MessageComponent</code> </p>
<p> struct <code>NDCComponent</code> </p>
<p> struct <code>PriorityComponent</code> </p>
<p> struct <code>ThreadNameComponent</code> </p>
<p> struct <code>ProcessorTimeComponent</code> </p>
<p> struct <code>TimeStampComponent</code> </p>
<p> struct <code>SecondsSinceEpochComponent</code> </p>
<p> struct <code>MillisSinceEpochComponent</code> </p>
<p> struct <code>FormatModifierComponent</code> </p>
<p> class <code>Properties</code> </p>
<p> class <code>PropertyConfiguratorImpl</code> </p>
<p> class <code>StringUtil</code> </p>
<h3>Typedefs</h3>
<p> typedef std::set&lt; <code>Appender</code> * &gt; <code>AppenderSet</code> </p>
<h3>Functions</h3>
<p> <code>LOG4CPP_EXPORT</code> <code>CategoryStream</code> &amp; <code>eol</code> (<code>CategoryStream</code> &amp;os)<br />
 <i>eol manipulator </i><br />
 <code>LOG4CPP_EXPORT</code> <code>CategoryStream</code> &amp; <code>left</code> (<code>CategoryStream</code> &amp;os)<br />
 <i>left manipulator </i><br />
 std::auto_ptr&lt; <code>Appender</code> &gt; <code>create_abort_appender</code> (const <code>FactoryParams</code> &amp;params) </p>
<p> std::auto_ptr&lt; <code>Appender</code> &gt; <code>create_file_appender</code> (const <code>FactoryParams</code> &amp;) </p>
<p> std::auto_ptr&lt; <code>Appender</code> &gt; <code>create_roll_file_appender</code> (const <code>FactoryParams</code> &amp;) </p>
<p> std::auto_ptr&lt; <code>Appender</code> &gt; <code>create_idsa_appender</code> (const <code>FactoryParams</code> &amp;) </p>
<p> std::auto_ptr&lt; <code>Appender</code> &gt; <code>create_nt_event_log_appender</code> (const <code>FactoryParams</code> &amp;) </p>
<p> std::auto_ptr&lt; <code>Appender</code> &gt; <code>create_remote_syslog_appender</code> (const <code>FactoryParams</code> &amp;) </p>
<p> std::auto_ptr&lt; <code>Appender</code> &gt; <code>create_syslog_appender</code> (const <code>FactoryParams</code> &amp;) </p>
<p> std::auto_ptr&lt; <code>Appender</code> &gt; <code>create_win32_debug_appender</code> (const <code>FactoryParams</code> &amp;) </p>
<p> std::auto_ptr&lt; <code>Appender</code> &gt; <code>create_smtp_appender</code> (const <code>FactoryParams</code> &amp;) </p>
<p> std::auto_ptr&lt; <code>Layout</code> &gt; <code>create_basic_layout</code> (const <code>FactoryParams</code> &amp;params) </p>
<p> std::auto_ptr&lt; <code>Layout</code> &gt; <code>create_simple_layout</code> (const <code>FactoryParams</code> &amp;params) </p>
<p> std::auto_ptr&lt; <code>Layout</code> &gt; <code>create_pattern_layout</code> (const <code>FactoryParams</code> &amp;params) </p>
<p> std::auto_ptr&lt; <code>Layout</code> &gt; <code>create_pass_through_layout</code> (const <code>FactoryParams</code> &amp;params) </p>
<p> std::auto_ptr<br />
 &lt; <code>TriggeringEventEvaluator</code> &gt; <code>create_level_evaluator</code> (const <code>FactoryParams</code> &amp;params)&quot; </p>
<p> void <code>localtime</code> (const ::time_t *time,::tm *t) </p>
<p> ostream &amp; <code>operator&lt;&lt;</code> (ostream &amp;os, const <code>width</code> &amp;w) </p>
<p> ostream &amp; <code>operator&lt;&lt;</code> (ostream &amp;os, const <code>tab</code> &amp;t) </p>
<p> template&lt;typename T &gt; const T &amp; <code>min</code> (const T &amp;a, const T &amp;b) </p>
<p> template&lt;typename T &gt; const T &amp; <code>max</code> (const T &amp;a, const T &amp;b) </p>
<h3>Variables</h3>
<p> class <code>LOG4CPP_EXPORT</code> <code>Filter</code> </p>
<p> class <code>LOG4CPP_EXPORT</code> <code>Category</code> </p>
<p> class <code>LOG4CPP_EXPORT</code> <code>CategoryStream</code> </p>
<p> static <code>AppendersFactory</code> * <code>appenders_factory_</code> = 0 </p>
<p> static const std::string <code>EMPTY</code> </p>
<p> static <code>LayoutsFactory</code> * <code>layouts_factory_</code> = 0 </p>
<p> static<br />
 <code>TriggeringEventEvaluatorFactory</code> * <code>evaluators_factory_</code> = 0&quot; </p>
<h2>Detailed Description</h2>
<p> The top level namespace for all &#8216;Log for C++&#8217; types and classes.</p>
<h2>Typedef Documentation</h2>
<h3>typedef std::set&lt;<code>Appender</code> *&gt; <code>log4cpp::AppenderSet</code></h3>
<h2>Function Documentation</h2>
<h3>std::auto_ptr&lt; <code>Appender</code> &gt; log4cpp::create_abort_appender (const FactoryParams &amp;params)</h3>
<h3>std::auto_ptr&lt; <code>Layout</code> &gt; log4cpp::create_basic_layout (const FactoryParams &amp;params)</h3>
<h3>std::auto_ptr&lt; <code>Appender</code> &gt; log4cpp::create_file_appender (const FactoryParams &amp;params)</h3>
<h3>std::auto_ptr&lt;<code>Appender</code>&gt; log4cpp::create_idsa_appender (const FactoryParams &amp;)</h3>
<h3>std::auto_ptr&lt; <code>TriggeringEventEvaluator</code> &gt; log4cpp::create_level_evaluator (const FactoryParams &amp;params)</h3>
<h3>std::auto_ptr&lt; <code>Appender</code> &gt; log4cpp::create_nt_event_log_appender (const FactoryParams &amp;params)</h3>
<h3>std::auto_ptr&lt; <code>Layout</code> &gt; log4cpp::create_pass_through_layout (const FactoryParams &amp;params)</h3>
<h3>std::auto_ptr&lt; <code>Layout</code> &gt; log4cpp::create_pattern_layout (const FactoryParams &amp;params)</h3>
<h3>std::auto_ptr&lt; <code>Appender</code> &gt; log4cpp::create_remote_syslog_appender (const FactoryParams &amp;params)</h3>
<h3>std::auto_ptr&lt; <code>Appender</code> &gt; log4cpp::create_roll_file_appender (const FactoryParams &amp;params)</h3>
<h3>std::auto_ptr&lt; <code>Layout</code> &gt; log4cpp::create_simple_layout (const FactoryParams &amp;params)</h3>
<h3>std::auto_ptr&lt;<code>Appender</code>&gt; log4cpp::create_smtp_appender (const FactoryParams &amp;)</h3>
<h3>std::auto_ptr&lt;<code>Appender</code>&gt; log4cpp::create_syslog_appender (const FactoryParams &amp;)</h3>
<h3>std::auto_ptr&lt; <code>Appender</code> &gt; log4cpp::create_win32_debug_appender (const FactoryParams &amp;params)</h3>
<h3><code>CategoryStream</code> &amp; log4cpp::eol (CategoryStream &amp;os)</h3>
<p> eol manipulator</p>
<h3><code>CategoryStream</code> &amp; log4cpp::left (CategoryStream &amp;os)</h3>
<p> left manipulator</p>
<h3>void log4cpp::localtime (const ::time_t *time, ::tm *t)</h3>
<h3>template&lt;typename T &gt; const T&amp; log4cpp::max (const T &amp;a, const T &amp;b)</h3>
<h3>template&lt;typename T &gt; const T&amp; log4cpp::min (const T &amp;a, const T &amp;b)</h3>
<h3>ostream&amp; log4cpp::operator&lt;&lt; (ostream &amp;os, const width &amp;w)</h3>
<h3>ostream&amp; log4cpp::operator&lt;&lt; (ostream &amp;os, const tab &amp;t)</h3>
<h2>Variable Documentation</h2>
<h3><code>AppendersFactory</code>* log4cpp::appenders_factory_ = 0 [static]</h3>
<h3>class <code>LOG4CPP_EXPORT</code> <code>log4cpp::Category</code></h3>
<h3>class <code>LOG4CPP_EXPORT</code> <code>log4cpp::CategoryStream</code></h3>
<h3>const std::string log4cpp::EMPTY [static]</h3>
<h3><code>TriggeringEventEvaluatorFactory</code>* log4cpp::evaluators_factory_ = 0 [static]</h3>
<h3>class <code>LOG4CPP_EXPORT</code> <code>log4cpp::Filter</code></h3>
<h3><code>LayoutsFactory</code>* log4cpp::layouts_factory_ = 0 [static]</h3>
<h2>Author</h2>
<p> Generated automatically by Doxygen for log4cpp from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAL">Function Documentation</a></p>
<dd>
<dt><a href="#lbBH">Variable Documentation</a></p>
<dd>
<dt><a href="#lbBP">Author</a></p>
<dd></dl>
