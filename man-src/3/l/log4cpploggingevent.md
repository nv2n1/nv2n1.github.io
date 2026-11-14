---
title: "log4cpploggingevent(3)"
name: "log4cpploggingevent"
section: "3"
letter: "l"
url: "/docs/linux/man/3-log4cpploggingevent/"
description: "log4cpp::LoggingEvent –"
---

<p>log4cpp::LoggingEvent &#8211; </p>
<p> The internal representation of logging events.</p>
<h2>Synopsis</h2>
<p>#include &lt;LoggingEvent.hh&gt;</p>
<h3>Public Member Functions</h3>
<p><code>LoggingEvent</code> (const std::string &amp;category, const std::string &amp;<code>message</code>, const std::string &amp;<code>ndc</code>, <code>Priority::Value</code> <code>priority</code>)<br />
 <i>Instantiate a </i><code>LoggingEvent</code> from the supplied parameters.</p>
<h3>Public Attributes</h3>
<p>const std::string <code>categoryName</code><br />
 <i>The category name. </i><br />
 const std::string <code>message</code><br />
 <i>The application supplied message of logging event. </i><br />
 const std::string <code>ndc</code><br />
 <i>The nested diagnostic context (</i><code>NDC</code>) of logging event.<br />
 <code>Priority::Value</code> <code>priority</code><br />
 <i></i><code>Priority</code> of logging event.<br />
 const std::string <code>threadName</code><br />
 <i>The name of thread in which this logging event was generated, e.g. </i><br />
 <code>TimeStamp</code> <code>timeStamp</code><br />
 <i>The number of seconds elapsed since the epoch (1/1/1970 00:00:00 UTC) until logging event was created. </i></p>
<h2>Detailed Description</h2>
<p>The internal representation of logging events. </p>
<p> When a affirmative logging decision is made a <code>LoggingEvent</code> instance is created. This instance is passed around the different <code>log4cpp</code> components. </p>
<p> This class is of concern to those wishing to extend <code>log4cpp</code>.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>log4cpp::LoggingEvent::LoggingEvent (const std::string &amp;category, const std::string &amp;message, const std::string &amp;ndc, <code>Priority::Value</code>priority)</h3>
<p>Instantiate a <code>LoggingEvent</code> from the supplied parameters. Except timeStamp all the other fields of <code>LoggingEvent</code> are filled when actually needed. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>category</i> The category of this event.<br />
 <i>message</i> The message of this event.<br />
 <i>ndc</i> The nested diagnostic context of this event.<br />
 <i>priority</i> The priority of this event.</dl>
<h2>Member Data Documentation</h2>
<h3>const std::string log4cpp::LoggingEvent::categoryName</h3>
<p>The category name.</p>
<h3>const std::string log4cpp::LoggingEvent::message</h3>
<p>The application supplied message of logging event.</p>
<h3>const std::string log4cpp::LoggingEvent::ndc</h3>
<p>The nested diagnostic context (<code>NDC</code>) of logging event.</p>
<h3><code>Priority::Value</code> log4cpp::LoggingEvent::priority</h3>
<p><code>Priority</code> of logging event.</p>
<h3>const std::string log4cpp::LoggingEvent::threadName</h3>
<p>The name of thread in which this logging event was generated, e.g. the PID.</p>
<h3><code>TimeStamp</code> log4cpp::LoggingEvent::timeStamp</h3>
<p>The number of seconds elapsed since the epoch (1/1/1970 00:00:00 UTC) until logging event was created. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for log4cpp from the source code.</p>
