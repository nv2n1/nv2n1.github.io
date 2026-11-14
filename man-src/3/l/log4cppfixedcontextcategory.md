---
title: "log4cppfixedcontextcategory(3)"
name: "log4cppfixedcontextcategory"
section: "3"
letter: "l"
url: "/docs/linux/man/3-log4cppfixedcontextcategory/"
description: "log4cpp::FixedContextCategory –"
---

<p>log4cpp::FixedContextCategory &#8211; </p>
<p> This <code>Category</code> subclass replaces the <code>NDC</code> field in LoggingEvents with a fixed context string.</p>
<h2>Synopsis</h2>
<p>#include &lt;FixedContextCategory.hh&gt; </p>
<p> Inherits <code>log4cpp::Category</code>.</p>
<h3>Public Member Functions</h3>
<p><code>FixedContextCategory</code> (const std::string &amp;name, const std::string &amp;context=&#8221;)<br />
 <i>Constructor. </i><br />
 virtual <code>~FixedContextCategory</code> ()<br />
 <i>Destructor for </i><code>Category</code>.<br />
 virtual void <code>setContext</code> (const std::string &amp;context)<br />
 <i>Set the context string used as </i><code>NDC</code>.<br />
 virtual std::string <code>getContext</code> () const<br />
 <i>Return the context string used as </i><code>NDC</code>.<br />
 virtual <code>Priority::Value</code> <code>getPriority</code> () const throw ()<br />
 <i>Returns the assigned </i><code>Priority</code>, if any, for this <code>Category</code>.<br />
 virtual <code>Priority::Value</code> <code>getChainedPriority</code> () const throw ()<br />
 <i>Starting from this </i><code>Category</code>, search the category hierarchy for a set priority and return it.<br />
 virtual void <code>addAppender</code> (<code>Appender</code> *appender) throw ()<br />
 <i>For the moment this method does nothing. </i><br />
 virtual void <code>addAppender</code> (<code>Appender</code> &amp;appender)<br />
 <i>For the moment this method does nothing. </i><br />
 virtual <code>Appender</code> * <code>getAppender</code> () const<br />
 <i>Returns the </i><code>Appender</code> for this <code>Category</code>, or NULL if no <code>Appender</code> has been set.<br />
 virtual <code>Appender</code> * <code>getAppender</code> (const std::string &amp;name) const<br />
 <i>Returns the specified </i><code>Appender</code> for this <code>Category</code>, or NULL if the <code>Appender</code> is not attached to this <code>Category</code>.<br />
 virtual <code>AppenderSet</code> <code>getAllAppenders</code> () const<br />
 <i>Returns the set of Appenders currently attached to this Catogory. </i><br />
 virtual void <code>removeAllAppenders</code> ()<br />
 <i>Removes all appenders set for this </i><code>Category</code>.<br />
 virtual bool <code>ownsAppender</code> () const throw ()<br />
 <i>FixedContextAppenders cannot own Appenders. </i><br />
 virtual bool <code>ownsAppender</code> (<code>Appender</code> *appender) const throw ()<br />
 <i>FixedContextAppenders cannot own Appenders. </i><br />
 virtual void <code>callAppenders</code> (const <code>LoggingEvent</code> &amp;event) throw ()<br />
 <i>Call the appenders in the hierarchy starting at </i>this.<br />
 virtual void <code>setAdditivity</code> (bool additivity)<br />
 <i>Set the additivity flag for this </i><code>Category</code> instance.<br />
 virtual bool <code>getAdditivity</code> () const throw ()<br />
 <i>Returns the additivity flag for this </i><code>Category</code> instance.</p>
<h3>Protected Member Functions</h3>
<p>virtual void <code>_logUnconditionally2</code> (<code>Priority::Value</code> priority, const std::string &amp;message) throw ()<br />
 <i>Unconditionally log a message with the specified priority. </i></p>
<h3>Additional Inherited Members</h3>
<h2>Detailed Description</h2>
<p>This <code>Category</code> subclass replaces the <code>NDC</code> field in LoggingEvents with a fixed context string. </p>
<p> All handling of Appenders, etc. is delgated to the &#8216;normal&#8217; <code>Category</code> with the same name. Its intended use is for object instances that serve a single client: they contruct a <code>FixedContextCategory</code> with the client identifier as context. Unlike with regular <code>Category</code> instances one has to explicitly create <code>FixedContextCategory</code> instances using the constructor. This also implies one has to take cake of destruction of the instance as well. </p>
<p> <code>Since:</code></p>
<dl COMPACT>
<dd>0.2.4</dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>log4cpp::FixedContextCategory::FixedContextCategory (const std::string &amp;name, const std::string &amp;context = &#8221;)</h3>
<p>Constructor. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>name</i> the fully qualified name of this Categories delegate <code>Category</code>.<br />
 <i>context</i> the context to fill the <code>NDC</code> field of LoggingEvents with.</dl>
<h3>log4cpp::FixedContextCategory::~FixedContextCategory () [virtual]</h3>
<p>Destructor for <code>Category</code>.</p>
<h2>Member Function Documentation</h2>
<h3>void log4cpp::FixedContextCategory::_logUnconditionally2 (<code>Priority::Value</code>priority, const std::string &amp;message) [protected], [virtual]</h3>
<p>Unconditionally log a message with the specified priority. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>priority</i> The priority of this log message.<br />
 <i>message</i> string to write in the log file</dl>
<p> Reimplemented from <code>log4cpp::Category</code>.</p>
<h3>void log4cpp::FixedContextCategory::addAppender (<code>Appender</code> *appender) [virtual]</h3>
<p>For the moment this method does nothing. </p>
<p> Reimplemented from <code>log4cpp::Category</code>.</p>
<h3>void log4cpp::FixedContextCategory::addAppender (<code>Appender</code> &amp;appender) [virtual]</h3>
<p>For the moment this method does nothing. </p>
<p> Reimplemented from <code>log4cpp::Category</code>.</p>
<h3>void log4cpp::FixedContextCategory::callAppenders (const <code>LoggingEvent</code> &amp;event) [virtual]</h3>
<p>Call the appenders in the hierarchy starting at this. If no appenders could be found, emit a warning. </p>
<p> This method always calls all the appenders inherited form the hierracy circumventing any evaluation of whether to log or not to log the particular log request. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>event</i> The <code>LoggingEvent</code> to log.</dl>
<p> Reimplemented from <code>log4cpp::Category</code>.</p>
<h3>bool log4cpp::FixedContextCategory::getAdditivity () const [virtual]</h3>
<p>Returns the additivity flag for this <code>Category</code> instance. </p>
<p> Reimplemented from <code>log4cpp::Category</code>.</p>
<h3><code>AppenderSet</code> log4cpp::FixedContextCategory::getAllAppenders () const [virtual]</h3>
<p>Returns the set of Appenders currently attached to this Catogory. </p>
<p> <code>Since:</code></p>
<dl COMPACT>
<dd>0.3.1</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The set of attached Appenders.</dl>
<p> Reimplemented from <code>log4cpp::Category</code>.</p>
<h3><code>Appender</code> * log4cpp::FixedContextCategory::getAppender () const [virtual]</h3>
<p>Returns the <code>Appender</code> for this <code>Category</code>, or NULL if no <code>Appender</code> has been set. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The <code>Appender</code>.</dl>
<p> Reimplemented from <code>log4cpp::Category</code>.</p>
<h3><code>Appender</code> * log4cpp::FixedContextCategory::getAppender (const std::string &amp;name) const [virtual]</h3>
<p>Returns the specified <code>Appender</code> for this <code>Category</code>, or NULL if the <code>Appender</code> is not attached to this <code>Category</code>. </p>
<p> <code>Since:</code></p>
<dl COMPACT>
<dd>0.2.7</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The <code>Appender</code>.</dl>
<p> Reimplemented from <code>log4cpp::Category</code>.</p>
<h3><code>Priority::Value</code> log4cpp::FixedContextCategory::getChainedPriority () const [virtual]</h3>
<p>Starting from this <code>Category</code>, search the category hierarchy for a set priority and return it. Otherwise, return the priority of the root category. </p>
<p> The <code>Category</code> class is designed so that this method executes as quickly as possible. </p>
<p> Reimplemented from <code>log4cpp::Category</code>.</p>
<h3>std::string log4cpp::FixedContextCategory::getContext () const [virtual]</h3>
<p>Return the context string used as <code>NDC</code>. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the context string.</dl>
<h3><code>Priority::Value</code> log4cpp::FixedContextCategory::getPriority () const [virtual]</h3>
<p>Returns the assigned <code>Priority</code>, if any, for this <code>Category</code>. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd><code>Priority</code> &#8211; the assigned <code>Priority</code>, can be <code>Priority::NOTSET</code></dl>
<p> Reimplemented from <code>log4cpp::Category</code>.</p>
<h3>bool log4cpp::FixedContextCategory::ownsAppender () const [virtual]</h3>
<p>FixedContextAppenders cannot own Appenders. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>false</dl>
<p> Reimplemented from <code>log4cpp::Category</code>.</p>
<h3>bool log4cpp::FixedContextCategory::ownsAppender (<code>Appender</code> *appender) const [virtual]</h3>
<p>FixedContextAppenders cannot own Appenders. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>false</dl>
<p> Reimplemented from <code>log4cpp::Category</code>.</p>
<h3>void log4cpp::FixedContextCategory::removeAllAppenders () [virtual]</h3>
<p>Removes all appenders set for this <code>Category</code>. Currently a <code>Category</code> can have only one appender, but this may change in the future. </p>
<p> Reimplemented from <code>log4cpp::Category</code>.</p>
<h3>void log4cpp::FixedContextCategory::setAdditivity (booladditivity) [virtual]</h3>
<p>Set the additivity flag for this <code>Category</code> instance. </p>
<p> Reimplemented from <code>log4cpp::Category</code>.</p>
<h3>void log4cpp::FixedContextCategory::setContext (const std::string &amp;context) [virtual]</h3>
<p>Set the context string used as <code>NDC</code>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> the context string</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for log4cpp from the source code.</p>
