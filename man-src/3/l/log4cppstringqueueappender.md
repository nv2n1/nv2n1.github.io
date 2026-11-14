---
title: "log4cppstringqueueappender(3)"
name: "log4cppstringqueueappender"
section: "3"
letter: "l"
url: "/docs/linux/man/3-log4cppstringqueueappender/"
description: "log4cpp::StringQueueAppender –"
---

<p>log4cpp::StringQueueAppender &#8211; </p>
<p> This class puts log messages in an in-memory queue.</p>
<h2>Synopsis</h2>
<p>#include &lt;StringQueueAppender.hh&gt; </p>
<p> Inherits <code>log4cpp::LayoutAppender</code>.</p>
<h3>Public Member Functions</h3>
<p><code>StringQueueAppender</code> (const std::string &amp;name) </p>
<p> virtual <code>~StringQueueAppender</code> () </p>
<p> virtual bool <code>reopen</code> ()<br />
 <i>Reopens the output destination of this </i><code>Appender</code>, e.g.<br />
 virtual void <code>close</code> ()<br />
 <i>Release any resources allocated within the appender such as file handles, network connections, etc. </i><br />
 virtual size_t <code>queueSize</code> () const<br />
 <i>Return the current size of the message queue. </i><br />
 virtual std::queue&lt; std::string &gt; &amp; <code>getQueue</code> ()<br />
 <i>Return the queue to which the Appends adds messages. </i><br />
 virtual const std::queue<br />
 &lt; std::string &gt; &amp; <code>getQueue</code> () const &quot;<br />
 <i>Return the queue to which the Appends adds messages. </i><br />
 virtual std::string <code>popMessage</code> ()<br />
 <i>Pop the oldest log message from the front of the queue. </i></p>
<h3>Protected Member Functions</h3>
<p>virtual void <code>_append</code> (const <code>LoggingEvent</code> &amp;event)<br />
 <i>Appends the </i><code>LoggingEvent</code> to the queue.</p>
<h3>Protected Attributes</h3>
<p>std::queue&lt; std::string &gt; <code>_queue</code> </p>
<h3>Additional Inherited Members</h3>
<h2>Detailed Description</h2>
<p>This class puts log messages in an in-memory queue. </p>
<p> Its primary use is in test cases, but it may be useful elsewhere as well. </p>
<p> <code>Since:</code></p>
<dl COMPACT>
<dd>0.2.4</dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>log4cpp::StringQueueAppender::StringQueueAppender (const std::string &amp;name)</h3>
<h3>log4cpp::StringQueueAppender::~StringQueueAppender () [virtual]</h3>
<h2>Member Function Documentation</h2>
<h3>void log4cpp::StringQueueAppender::_append (const <code>LoggingEvent</code> &amp;event) [protected], [virtual]</h3>
<p>Appends the <code>LoggingEvent</code> to the queue. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>event</i> the <code>LoggingEvent</code> to layout and append to the queue.</dl>
<p> Implements <code>log4cpp::AppenderSkeleton</code>.</p>
<h3>void log4cpp::StringQueueAppender::close () [virtual]</h3>
<p>Release any resources allocated within the appender such as file handles, network connections, etc. </p>
<p> Implements <code>log4cpp::AppenderSkeleton</code>.</p>
<h3>std::queue&lt; std::string &gt; &amp; log4cpp::StringQueueAppender::getQueue () [virtual]</h3>
<p>Return the queue to which the Appends adds messages. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the message queue</dl>
<h3>const std::queue&lt; std::string &gt; &amp; log4cpp::StringQueueAppender::getQueue () const [virtual]</h3>
<p>Return the queue to which the Appends adds messages. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the message queue</dl>
<h3>std::string log4cpp::StringQueueAppender::popMessage () [virtual]</h3>
<p>Pop the oldest log message from the front of the queue. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the oldest log message</dl>
<h3>size_t log4cpp::StringQueueAppender::queueSize () const [virtual]</h3>
<p>Return the current size of the message queue. Shorthand for <code>getQueue()</code>.size(). </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the queue size</dl>
<h3>bool log4cpp::StringQueueAppender::reopen () [virtual]</h3>
<p>Reopens the output destination of this <code>Appender</code>, e.g. the logfile or TCP socket. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>false if an error occured during reopening, true otherwise.</dl>
<p> Reimplemented from <code>log4cpp::AppenderSkeleton</code>.</p>
<h2>Member Data Documentation</h2>
<h3>std::queue&lt;std::string&gt; log4cpp::StringQueueAppender::_queue [protected]</h3>
<h2>Author</h2>
<p>Generated automatically by Doxygen for log4cpp from the source code.</p>
