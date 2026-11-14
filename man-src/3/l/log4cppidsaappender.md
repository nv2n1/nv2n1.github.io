---
title: "log4cppidsaappender(3)"
name: "log4cppidsaappender"
section: "3"
letter: "l"
url: "/docs/linux/man/3-log4cppidsaappender/"
description: "log4cpp::IdsaAppender –"
---

<p>log4cpp::IdsaAppender &#8211; </p>
<p> <code>IdsaAppender</code> is an <code>Appender</code> that sends LoggingEvents to the IDS/A logger and reference monitor by Marc Welz.</p>
<h2>Synopsis</h2>
<p>#include &lt;IdsaAppender.hh&gt; </p>
<p> Inherits <code>log4cpp::AppenderSkeleton</code>.</p>
<h3>Public Member Functions</h3>
<p><code>IdsaAppender</code> (const std::string &amp;name, const std::string &amp;idsaName)<br />
 <i>Instantiate an </i><code>IdsaAppender</code> with given name and name.<br />
 virtual <code>~IdsaAppender</code> () </p>
<p> virtual bool <code>reopen</code> ()<br />
 <i>Calls idsa_open() and idsa_close() </i><br />
 virtual void <code>close</code> ()<br />
 <i>Calls idsa_close() </i><br />
 virtual bool <code>requiresLayout</code> () const<br />
 <i>The </i><code>IdsaAppender</code> does its own <code>Layout</code>.<br />
 virtual void <code>setLayout</code> (<code>Layout</code> *layout)<br />
 <i>Set the </i><code>Layout</code> for this appender.</p>
<h3>Protected Member Functions</h3>
<p>virtual void <code>open</code> ()<br />
 <i>Calls idsa_open(). </i><br />
 virtual void <code>_append</code> (const <code>LoggingEvent</code> &amp;event)<br />
 <i>Sends a </i><code>LoggingEvent</code> to idsa.</p>
<h3>Protected Attributes</h3>
<p>const std::string <code>_idsaName</code> </p>
<p> IDSA_CONNECTION * <code>_idsaConnection</code> </p>
<h3>Additional Inherited Members</h3>
<h2>Detailed Description</h2>
<p><code>IdsaAppender</code> is an <code>Appender</code> that sends LoggingEvents to the IDS/A logger and reference monitor by Marc Welz. </p>
<p> See <a rel="nofollow" href="http://jade.cs.uct.ac.za/idsa/">http://jade.cs.uct.ac.za/idsa/</a> for more information on IDS/A.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>log4cpp::IdsaAppender::IdsaAppender (const std::string &amp;name, const std::string &amp;idsaName)</h3>
<p>Instantiate an <code>IdsaAppender</code> with given name and name. Unlike the syslog API, idsa allows multiple connections. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>name</i> The name of the <code>Appender</code><br />
 <i>idsaName</i> The service parameter of idsa</dl>
<h3>virtual log4cpp::IdsaAppender::~IdsaAppender () [virtual]</h3>
<h2>Member Function Documentation</h2>
<h3>virtual void log4cpp::IdsaAppender::_append (const <code>LoggingEvent</code> &amp;event) [protected], [virtual]</h3>
<p>Sends a <code>LoggingEvent</code> to idsa. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>event</i> the <code>LoggingEvent</code> to log.</dl>
<p> Implements <code>log4cpp::AppenderSkeleton</code>.</p>
<h3>virtual void log4cpp::IdsaAppender::close () [virtual]</h3>
<p>Calls idsa_close() </p>
<p> Implements <code>log4cpp::AppenderSkeleton</code>.</p>
<h3>virtual void log4cpp::IdsaAppender::open () [protected], [virtual]</h3>
<p>Calls idsa_open().</p>
<h3>virtual bool log4cpp::IdsaAppender::reopen () [virtual]</h3>
<p>Calls idsa_open() and idsa_close() </p>
<p> Reimplemented from <code>log4cpp::AppenderSkeleton</code>.</p>
<h3>virtual bool log4cpp::IdsaAppender::requiresLayout () const [virtual]</h3>
<p>The <code>IdsaAppender</code> does its own <code>Layout</code>. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>false</dl>
<p> Implements <code>log4cpp::AppenderSkeleton</code>.</p>
<h3>virtual void log4cpp::IdsaAppender::setLayout (<code>Layout</code> *layout) [virtual]</h3>
<p>Set the <code>Layout</code> for this appender. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>layout</i> The layout to use.</dl>
<p> Implements <code>log4cpp::AppenderSkeleton</code>.</p>
<h2>Member Data Documentation</h2>
<h3>IDSA_CONNECTION* log4cpp::IdsaAppender::_idsaConnection [protected]</h3>
<h3>const std::string log4cpp::IdsaAppender::_idsaName [protected]</h3>
<h2>Author</h2>
<p>Generated automatically by Doxygen for log4cpp from the source code.</p>
