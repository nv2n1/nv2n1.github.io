---
title: "log4cppcategory(3)"
name: "log4cppcategory"
section: "3"
letter: "l"
url: "/docs/linux/man/3-log4cppcategory/"
description: "log4cpp::Category –"
---

<p>log4cpp::Category &#8211; </p>
<p> This is the central class in the log4j package.</p>
<h2>Synopsis</h2>
<p>#include &lt;Category.hh&gt; </p>
<p> Inherited by <code>log4cpp::FixedContextCategory</code>.</p>
<h3>Public Member Functions</h3>
<p>virtual <code>~Category</code> ()<br />
 <i>Destructor for </i><code>Category</code>.<br />
 virtual const std::string &amp; <code>getName</code> () const throw ()<br />
 <i>Return the category name. </i><br />
 virtual void <code>setPriority</code> (<code>Priority::Value</code> priority) throw (std::invalid_argument)<br />
 <i>Set the priority of this </i><code>Category</code>.<br />
 virtual <code>Priority::Value</code> <code>getPriority</code> () const throw ()<br />
 <i>Returns the assigned </i><code>Priority</code>, if any, for this <code>Category</code>.<br />
 virtual <code>Priority::Value</code> <code>getChainedPriority</code> () const throw ()<br />
 <i>Starting from this </i><code>Category</code>, search the category hierarchy for a set priority and return it.<br />
 virtual bool <code>isPriorityEnabled</code> (<code>Priority::Value</code> priority) const throw ()<br />
 <i>Returns true if the chained priority of the </i><code>Category</code> is equal to or higher than given priority.<br />
 virtual void <code>addAppender</code> (<code>Appender</code> *appender) throw (std::invalid_argument)<br />
 <i>Adds an </i><code>Appender</code> to this <code>Category</code>.<br />
 virtual void <code>addAppender</code> (<code>Appender</code> &amp;appender)<br />
 <i>Adds an </i><code>Appender</code> for this <code>Category</code>.<br />
 void <code>setAppender</code> (<code>Appender</code> *appender)<br />
 <i>Adds an </i><code>Appender</code> to this <code>Category</code>.<br />
 void <code>setAppender</code> (<code>Appender</code> &amp;appender)<br />
 <i>Adds an </i><code>Appender</code> for this <code>Category</code>.<br />
 virtual <code>Appender</code> * <code>getAppender</code> () const<br />
 <i>Returns the first </i><code>Appender</code> for this <code>Category</code>, or NULL if no <code>Appender</code> has been set.<br />
 virtual <code>Appender</code> * <code>getAppender</code> (const std::string &amp;name) const<br />
 <i>Returns the specified </i><code>Appender</code> for this <code>Category</code>, or NULL if the <code>Appender</code> is not attached to this <code>Category</code>.<br />
 virtual <code>AppenderSet</code> <code>getAllAppenders</code> () const<br />
 <i>Returns the set of Appenders currently attached to this Catogory. </i><br />
 virtual void <code>removeAllAppenders</code> ()<br />
 <i>Removes all appenders for this </i><code>Category</code>.<br />
 virtual void <code>removeAppender</code> (<code>Appender</code> *appender)<br />
 <i>Removes specified appender for this </i><code>Category</code>.<br />
 virtual bool <code>ownsAppender</code> () const throw ()<br />
 <i>Returns true if the </i><code>Category</code> owns the first <code>Appender</code> in its <code>Appender</code> set.<br />
 virtual bool <code>ownsAppender</code> (<code>Appender</code> *appender) const throw ()<br />
 <i>Returns true if the </i><code>Category</code> owns the <code>Appender</code>.<br />
 virtual void <code>callAppenders</code> (const <code>LoggingEvent</code> &amp;event) throw ()<br />
 <i>Call the appenders in the hierarchy starting at </i>this.<br />
 virtual void <code>setAdditivity</code> (bool additivity)<br />
 <i>Set the additivity flag for this </i><code>Category</code> instance.<br />
 virtual bool <code>getAdditivity</code> () const throw ()<br />
 <i>Returns the additivity flag for this </i><code>Category</code> instance.<br />
 virtual <code>Category</code> * <code>getParent</code> () throw ()<br />
 <i>Returns the parent category of this category, or NULL if the category is the root category. </i><br />
 virtual const <code>Category</code> * <code>getParent</code> () const throw ()<br />
 <i>Returns the parent category of this category, or NULL if the category is the root category. </i><br />
 virtual void <code>log</code> (<code>Priority::Value</code> priority, const char *stringFormat,&#8230;) throw ()<br />
 <i>Log a message with the specified priority. </i><br />
 virtual void <code>log</code> (<code>Priority::Value</code> priority, const std::string &amp;message) throw ()<br />
 <i>Log a message with the specified priority. </i><br />
 virtual void <code>logva</code> (<code>Priority::Value</code> priority, const char *stringFormat, va_list va) throw ()<br />
 <i>Log a message with the specified priority. </i><br />
 void <code>debug</code> (const char *stringFormat,&#8230;) throw ()<br />
 <i>Log a message with debug priority. </i><br />
 void <code>debug</code> (const std::string &amp;message) throw ()<br />
 <i>Log a message with debug priority. </i><br />
 bool <code>isDebugEnabled</code> () const throw ()<br />
 <i>Return true if the </i><code>Category</code> will log messages with priority DEBUG.<br />
 <code>CategoryStream</code> <code>debugStream</code> ()<br />
 <i>Return a </i><code>CategoryStream</code> with priority DEBUG.<br />
 void <code>info</code> (const char *stringFormat,&#8230;) throw ()<br />
 <i>Log a message with info priority. </i><br />
 void <code>info</code> (const std::string &amp;message) throw ()<br />
 <i>Log a message with info priority. </i><br />
 bool <code>isInfoEnabled</code> () const throw ()<br />
 <i>Return true if the </i><code>Category</code> will log messages with priority INFO.<br />
 <code>CategoryStream</code> <code>infoStream</code> ()<br />
 <i>Return a </i><code>CategoryStream</code> with priority INFO.<br />
 void <code>notice</code> (const char *stringFormat,&#8230;) throw ()<br />
 <i>Log a message with notice priority. </i><br />
 void <code>notice</code> (const std::string &amp;message) throw ()<br />
 <i>Log a message with notice priority. </i><br />
 bool <code>isNoticeEnabled</code> () const throw ()<br />
 <i>Return true if the </i><code>Category</code> will log messages with priority NOTICE.<br />
 <code>CategoryStream</code> <code>noticeStream</code> ()<br />
 <i>Return a </i><code>CategoryStream</code> with priority NOTICE.<br />
 void <code>warn</code> (const char *stringFormat,&#8230;) throw ()<br />
 <i>Log a message with warn priority. </i><br />
 void <code>warn</code> (const std::string &amp;message) throw ()<br />
 <i>Log a message with warn priority. </i><br />
 bool <code>isWarnEnabled</code> () const throw ()<br />
 <i>Return true if the </i><code>Category</code> will log messages with priority WARN.<br />
 <code>CategoryStream</code> <code>warnStream</code> ()<br />
 <i>Return a </i><code>CategoryStream</code> with priority WARN.<br />
 void <code>error</code> (const char *stringFormat,&#8230;) throw ()<br />
 <i>Log a message with error priority. </i><br />
 void <code>error</code> (const std::string &amp;message) throw ()<br />
 <i>Log a message with error priority. </i><br />
 bool <code>isErrorEnabled</code> () const throw ()<br />
 <i>Return true if the </i><code>Category</code> will log messages with priority ERROR.<br />
 <code>CategoryStream</code> <code>errorStream</code> ()<br />
 <i>Return a </i><code>CategoryStream</code> with priority ERROR.<br />
 void <code>crit</code> (const char *stringFormat,&#8230;) throw ()<br />
 <i>Log a message with crit priority. </i><br />
 void <code>crit</code> (const std::string &amp;message) throw ()<br />
 <i>Log a message with crit priority. </i><br />
 bool <code>isCritEnabled</code> () const throw ()<br />
 <i>Return true if the </i><code>Category</code> will log messages with priority CRIT.<br />
 <code>CategoryStream</code> <code>critStream</code> ()<br />
 <i>Return a </i><code>CategoryStream</code> with priority CRIT.<br />
 void <code>alert</code> (const char *stringFormat,&#8230;) throw ()<br />
 <i>Log a message with alert priority. </i><br />
 void <code>alert</code> (const std::string &amp;message) throw ()<br />
 <i>Log a message with alert priority. </i><br />
 bool <code>isAlertEnabled</code> () const throw ()<br />
 <i>Return true if the </i><code>Category</code> will log messages with priority ALERT.<br />
 <code>CategoryStream</code> <code>alertStream</code> () throw ()<br />
 <i>Return a </i><code>CategoryStream</code> with priority ALERT.<br />
 void <code>emerg</code> (const char *stringFormat,&#8230;) throw ()<br />
 <i>Log a message with emerg priority. </i><br />
 void <code>emerg</code> (const std::string &amp;message) throw ()<br />
 <i>Log a message with emerg priority. </i><br />
 bool <code>isEmergEnabled</code> () const throw ()<br />
 <i>Return true if the </i><code>Category</code> will log messages with priority EMERG.<br />
 <code>CategoryStream</code> <code>emergStream</code> ()<br />
 <i>Return a </i><code>CategoryStream</code> with priority EMERG.<br />
 void <code>fatal</code> (const char *stringFormat,&#8230;) throw ()<br />
 <i>Log a message with fatal priority. </i><br />
 void <code>fatal</code> (const std::string &amp;message) throw ()<br />
 <i>Log a message with fatal priority. </i><br />
 bool <code>isFatalEnabled</code> () const throw ()<br />
 <i>Return true if the </i><code>Category</code> will log messages with priority FATAL.<br />
 <code>CategoryStream</code> <code>fatalStream</code> ()<br />
 <i>Return a </i><code>CategoryStream</code> with priority FATAL.<br />
 virtual <code>CategoryStream</code> <code>getStream</code> (<code>Priority::Value</code> priority)<br />
 <i>Return a </i><code>CategoryStream</code> with given <code>Priority</code>.<br />
 virtual <code>CategoryStream</code> <code>operator&lt;&lt;</code> (<code>Priority::Value</code> priority)<br />
 <i>Return a </i><code>CategoryStream</code> with given <code>Priority</code>.</p>
<h3>Static Public Member Functions</h3>
<p>static <code>Category</code> &amp; <code>getRoot</code> ()<br />
 <i>Return the root of the </i><code>Category</code> hierarchy.<br />
 static void <code>setRootPriority</code> (<code>Priority::Value</code> priority)<br />
 <i>Set the priority of the root </i><code>Category</code>.<br />
 static <code>Priority::Value</code> <code>getRootPriority</code> () throw ()<br />
 <i>Get the priority of the </i>root <code>Category</code>.<br />
 static <code>Category</code> &amp; <code>getInstance</code> (const std::string &amp;name)<br />
 <i>Instantiate a </i><code>Category</code> with name name.<br />
 static <code>Category</code> * <code>exists</code> (const std::string &amp;name)<br />
 <i>If the named category exists (in the default hierarchy) then it returns a reference to the category, otherwise it returns NULL. </i><br />
 static std::vector&lt; <code>Category</code> * &gt; * <code>getCurrentCategories</code> ()<br />
 <i>Returns all the currently defined categories as a vector of </i><code>Category</code> pointers.<br />
 static void <code>shutdown</code> ()<br />
 <i>This method will remove all Appenders from Categories.XXX. </i></p>
<h3>Protected Member Functions</h3>
<p><code>Category</code> (const std::string &amp;name, <code>Category</code> *parent, <code>Priority::Value</code> priority=<code>Priority::NOTSET</code>)<br />
 <i>Constructor. </i><br />
 virtual void <code>_logUnconditionally</code> (<code>Priority::Value</code> priority, const char *format, va_list arguments) throw () </p>
<p> virtual void <code>_logUnconditionally2</code> (<code>Priority::Value</code> priority, const std::string &amp;message) throw ()<br />
 <i>Unconditionally log a message with the specified priority. </i></p>
<h3>Friends</h3>
<p>class <code>HierarchyMaintainer</code> </p>
<h2>Detailed Description</h2>
<p>This is the central class in the log4j package. </p>
<p> One of the distintive features of log4j (and hence <code>log4cpp</code>) are hierarchal categories and their evaluation.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>log4cpp::Category::~Category () [virtual]</h3>
<p>Destructor for <code>Category</code>.</p>
<h3>log4cpp::Category::Category (const std::string &amp;name, <code>Category</code> *parent, <code>Priority::Value</code>priority = <code>Priority::NOTSET</code>) [protected]</h3>
<p>Constructor. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>name</i> the fully qualified name of this <code>Category</code><br />
 <i>parent</i> the parent of this parent, or NULL for the root <code>Category</code><br />
 <i>priority</i> the priority for this <code>Category</code>. Defaults to <code>Priority::NOTSET</code></dl>
<h2>Member Function Documentation</h2>
<h3>void log4cpp::Category::_logUnconditionally (<code>Priority::Value</code>priority, const char *format, va_listarguments) [protected], [virtual]</h3>
<h3>void log4cpp::Category::_logUnconditionally2 (<code>Priority::Value</code>priority, const std::string &amp;message) [protected], [virtual]</h3>
<p>Unconditionally log a message with the specified priority. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>priority</i> The priority of this log message.<br />
 <i>message</i> string to write in the log file</dl>
<p> Reimplemented in <code>log4cpp::FixedContextCategory</code>.</p>
<h3>void log4cpp::Category::addAppender (<code>Appender</code> *appender)std::invalid_argument [virtual]</h3>
<p>Adds an <code>Appender</code> to this <code>Category</code>. This method passes ownership from the caller to the <code>Category</code>. </p>
<p> <code>Since:</code></p>
<dl COMPACT>
<dd>0.2.7</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>appender</i> The <code>Appender</code> to wich this category has to log.</dl>
<p> <code>Exceptions:</code></p>
<dl COMPACT>
<dd><i>std::invalid_argument</i> if the appender is NULL.</dl>
<p> Reimplemented in <code>log4cpp::FixedContextCategory</code>.</p>
<h3>void log4cpp::Category::addAppender (<code>Appender</code> &amp;appender) [virtual]</h3>
<p>Adds an <code>Appender</code> for this <code>Category</code>. This method does not pass ownership from the caller to the <code>Category</code>. </p>
<p> <code>Since:</code></p>
<dl COMPACT>
<dd>0.2.7</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>appender</i> The <code>Appender</code> this category has to log to.</dl>
<p> Reimplemented in <code>log4cpp::FixedContextCategory</code>.</p>
<h3>void log4cpp::Category::alert (const char *stringFormat, &#8230;)</h3>
<p>Log a message with alert priority. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>stringFormat</i> Format specifier for the string to write in the log file.<br />
 <i>&#8230;</i> The arguments for stringFormat</dl>
<h3>void log4cpp::Category::alert (const std::string &amp;message)</h3>
<p>Log a message with alert priority. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>message</i> string to write in the log file</dl>
<h3><code>CategoryStream</code> log4cpp::Category::alertStream () [inline]</h3>
<p>Return a <code>CategoryStream</code> with priority ALERT. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The <code>CategoryStream</code>.</dl>
<h3>void log4cpp::Category::callAppenders (const <code>LoggingEvent</code> &amp;event) [virtual]</h3>
<p>Call the appenders in the hierarchy starting at this. If no appenders could be found, emit a warning. </p>
<p> This method always calls all the appenders inherited form the hierracy circumventing any evaluation of whether to log or not to log the particular log request. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>event</i> the LogginEvent to log.</dl>
<p> Reimplemented in <code>log4cpp::FixedContextCategory</code>.</p>
<h3>void log4cpp::Category::crit (const char *stringFormat, &#8230;)</h3>
<p>Log a message with crit priority. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>stringFormat</i> Format specifier for the string to write in the log file.<br />
 <i>&#8230;</i> The arguments for stringFormat</dl>
<h3>void log4cpp::Category::crit (const std::string &amp;message)</h3>
<p>Log a message with crit priority. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>message</i> string to write in the log file</dl>
<h3><code>CategoryStream</code> log4cpp::Category::critStream () [inline]</h3>
<p>Return a <code>CategoryStream</code> with priority CRIT. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The <code>CategoryStream</code>.</dl>
<h3>void log4cpp::Category::debug (const char *stringFormat, &#8230;)</h3>
<p>Log a message with debug priority. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>stringFormat</i> Format specifier for the string to write in the log file.<br />
 <i>&#8230;</i> The arguments for stringFormat</dl>
<h3>void log4cpp::Category::debug (const std::string &amp;message)</h3>
<p>Log a message with debug priority. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>message</i> string to write in the log file</dl>
<h3><code>CategoryStream</code> log4cpp::Category::debugStream () [inline]</h3>
<p>Return a <code>CategoryStream</code> with priority DEBUG. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The <code>CategoryStream</code>.</dl>
<h3>void log4cpp::Category::emerg (const char *stringFormat, &#8230;)</h3>
<p>Log a message with emerg priority. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>stringFormat</i> Format specifier for the string to write in the log file.<br />
 <i>&#8230;</i> The arguments for stringFormat</dl>
<h3>void log4cpp::Category::emerg (const std::string &amp;message)</h3>
<p>Log a message with emerg priority. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>message</i> string to write in the log file</dl>
<h3><code>CategoryStream</code> log4cpp::Category::emergStream () [inline]</h3>
<p>Return a <code>CategoryStream</code> with priority EMERG. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The <code>CategoryStream</code>.</dl>
<h3>void log4cpp::Category::error (const char *stringFormat, &#8230;)</h3>
<p>Log a message with error priority. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>stringFormat</i> Format specifier for the string to write in the log file.<br />
 <i>&#8230;</i> The arguments for stringFormat</dl>
<h3>void log4cpp::Category::error (const std::string &amp;message)</h3>
<p>Log a message with error priority. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>message</i> string to write in the log file</dl>
<h3><code>CategoryStream</code> log4cpp::Category::errorStream () [inline]</h3>
<p>Return a <code>CategoryStream</code> with priority ERROR. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The <code>CategoryStream</code>.</dl>
<h3><code>Category</code> * log4cpp::Category::exists (const std::string &amp;name) [static]</h3>
<p>If the named category exists (in the default hierarchy) then it returns a reference to the category, otherwise it returns NULL. </p>
<p> <code>Since:</code></p>
<dl COMPACT>
<dd>0.2.7</dl>
<h3>void log4cpp::Category::fatal (const char *stringFormat, &#8230;)</h3>
<p>Log a message with fatal priority. NB. priority &#8216;fatal&#8217; is equivalent to &#8217;emerg&#8217;. </p>
<p> <code>Since:</code></p>
<dl COMPACT>
<dd>0.2.7</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>stringFormat</i> Format specifier for the string to write in the log file.<br />
 <i>&#8230;</i> The arguments for stringFormat</dl>
<h3>void log4cpp::Category::fatal (const std::string &amp;message)</h3>
<p>Log a message with fatal priority. NB. priority &#8216;fatal&#8217; is equivalent to &#8217;emerg&#8217;. </p>
<p> <code>Since:</code></p>
<dl COMPACT>
<dd>0.2.7</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>message</i> string to write in the log file</dl>
<h3><code>CategoryStream</code> log4cpp::Category::fatalStream () [inline]</h3>
<p>Return a <code>CategoryStream</code> with priority FATAL. NB. priority &#8216;fatal&#8217; is equivalent to &#8217;emerg&#8217;. </p>
<p> <code>Since:</code></p>
<dl COMPACT>
<dd>0.2.7</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The <code>CategoryStream</code>.</dl>
<h3>bool log4cpp::Category::getAdditivity () const [virtual]</h3>
<p>Returns the additivity flag for this <code>Category</code> instance. </p>
<p> Reimplemented in <code>log4cpp::FixedContextCategory</code>.</p>
<h3><code>AppenderSet</code> log4cpp::Category::getAllAppenders () const [virtual]</h3>
<p>Returns the set of Appenders currently attached to this Catogory. </p>
<p> <code>Since:</code></p>
<dl COMPACT>
<dd>0.3.1</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The set of attached Appenders.</dl>
<p> Reimplemented in <code>log4cpp::FixedContextCategory</code>.</p>
<h3><code>Appender</code> * log4cpp::Category::getAppender () const [virtual]</h3>
<p>Returns the first <code>Appender</code> for this <code>Category</code>, or NULL if no <code>Appender</code> has been set. </p>
<p> <code>Deprecated</code></p>
<dl COMPACT>
<dd>use getAppender(const std::string&amp;)</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The <code>Appender</code>.</dl>
<p> Reimplemented in <code>log4cpp::FixedContextCategory</code>.</p>
<h3><code>Appender</code> * log4cpp::Category::getAppender (const std::string &amp;name) const [virtual]</h3>
<p>Returns the specified <code>Appender</code> for this <code>Category</code>, or NULL if the <code>Appender</code> is not attached to this <code>Category</code>. </p>
<p> <code>Since:</code></p>
<dl COMPACT>
<dd>0.2.7</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The <code>Appender</code>.</dl>
<p> Reimplemented in <code>log4cpp::FixedContextCategory</code>.</p>
<h3><code>Priority::Value</code> log4cpp::Category::getChainedPriority () const [virtual]</h3>
<p>Starting from this <code>Category</code>, search the category hierarchy for a set priority and return it. Otherwise, return the priority of the root category. </p>
<p> The <code>Category</code> class is designed so that this method executes as quickly as possible. </p>
<p> Reimplemented in <code>log4cpp::FixedContextCategory</code>.</p>
<h3>std::vector&lt; <code>Category</code> * &gt; * log4cpp::Category::getCurrentCategories () [static]</h3>
<p>Returns all the currently defined categories as a vector of <code>Category</code> pointers. Note: this function does not pass ownership of the categories in the vector to the caller, only the ownership of the vector. However vector&lt;Category&amp;&gt;* is not legal C++, so we can&#8217;t follow the default ownership conventions. </p>
<p> Unlike in log4j, the root category <i>is</i> included in the returned set. </p>
<p> <code>Since:</code></p>
<dl COMPACT>
<dd>0.3.2. Before 0.3.2 this method returned a std::set</dl>
<h3><code>Category</code> &amp; log4cpp::Category::getInstance (const std::string &amp;name) [static]</h3>
<p>Instantiate a <code>Category</code> with name name. This method does not set priority of the category which is by default <code>Priority::NOTSET</code>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>name</i> The name of the category to retrieve.</dl>
<h3>const std::string &amp; log4cpp::Category::getName () const [virtual]</h3>
<p>Return the category name. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The category name.</dl>
<h3><code>Category</code> * log4cpp::Category::getParent () [virtual]</h3>
<p>Returns the parent category of this category, or NULL if the category is the root category. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the parent category.</dl>
<h3>const <code>Category</code> * log4cpp::Category::getParent () const [virtual]</h3>
<p>Returns the parent category of this category, or NULL if the category is the root category. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the parent category.</dl>
<h3><code>Priority::Value</code> log4cpp::Category::getPriority () const [virtual]</h3>
<p>Returns the assigned <code>Priority</code>, if any, for this <code>Category</code>. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd><code>Priority</code> &#8211; the assigned <code>Priority</code>, can be <code>Priority::NOTSET</code></dl>
<p> Reimplemented in <code>log4cpp::FixedContextCategory</code>.</p>
<h3><code>Category</code> &amp; log4cpp::Category::getRoot () [static]</h3>
<p>Return the root of the <code>Category</code> hierarchy. The root category is always instantiated and available. It&#8217;s name is the empty string. </p>
<p> Unlike in log4j, calling <code>Category.getInstance</code>(&#8221;) <i>does</i> retrieve the root category and not a category just under root named &#8221;. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The root category</dl>
<h3><code>Priority::Value</code> log4cpp::Category::getRootPriority () [static]</h3>
<p>Get the priority of the root <code>Category</code>. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the priority of the root category</dl>
<h3><code>CategoryStream</code> log4cpp::Category::getStream (<code>Priority::Value</code>priority) [virtual]</h3>
<p>Return a <code>CategoryStream</code> with given <code>Priority</code>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>priority</i> The <code>Priority</code> of the <code>CategoryStream</code>.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The requested <code>CategoryStream</code>.</dl>
<h3>void log4cpp::Category::info (const char *stringFormat, &#8230;)</h3>
<p>Log a message with info priority. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>stringFormat</i> Format specifier for the string to write in the log file.<br />
 <i>&#8230;</i> The arguments for stringFormat</dl>
<h3>void log4cpp::Category::info (const std::string &amp;message)</h3>
<p>Log a message with info priority. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>message</i> string to write in the log file</dl>
<h3><code>CategoryStream</code> log4cpp::Category::infoStream () [inline]</h3>
<p>Return a <code>CategoryStream</code> with priority INFO. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The <code>CategoryStream</code>.</dl>
<h3>bool log4cpp::Category::isAlertEnabled () const [inline]</h3>
<p>Return true if the <code>Category</code> will log messages with priority ALERT. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Whether the <code>Category</code> will log.</dl>
<h3>bool log4cpp::Category::isCritEnabled () const [inline]</h3>
<p>Return true if the <code>Category</code> will log messages with priority CRIT. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Whether the <code>Category</code> will log.</dl>
<h3>bool log4cpp::Category::isDebugEnabled () const [inline]</h3>
<p>Return true if the <code>Category</code> will log messages with priority DEBUG. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Whether the <code>Category</code> will log.</dl>
<h3>bool log4cpp::Category::isEmergEnabled () const [inline]</h3>
<p>Return true if the <code>Category</code> will log messages with priority EMERG. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Whether the <code>Category</code> will log.</dl>
<h3>bool log4cpp::Category::isErrorEnabled () const [inline]</h3>
<p>Return true if the <code>Category</code> will log messages with priority ERROR. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Whether the <code>Category</code> will log.</dl>
<h3>bool log4cpp::Category::isFatalEnabled () const [inline]</h3>
<p>Return true if the <code>Category</code> will log messages with priority FATAL. NB. priority &#8216;fatal&#8217; is equivalent to &#8217;emerg&#8217;. </p>
<p> <code>Since:</code></p>
<dl COMPACT>
<dd>0.2.7</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Whether the <code>Category</code> will log.</dl>
<h3>bool log4cpp::Category::isInfoEnabled () const [inline]</h3>
<p>Return true if the <code>Category</code> will log messages with priority INFO. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Whether the <code>Category</code> will log.</dl>
<h3>bool log4cpp::Category::isNoticeEnabled () const [inline]</h3>
<p>Return true if the <code>Category</code> will log messages with priority NOTICE. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Whether the <code>Category</code> will log.</dl>
<h3>bool log4cpp::Category::isPriorityEnabled (<code>Priority::Value</code>priority) const [virtual]</h3>
<p>Returns true if the chained priority of the <code>Category</code> is equal to or higher than given priority. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>priority</i> The priority to compare with.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>whether logging is enable for this priority.</dl>
<h3>bool log4cpp::Category::isWarnEnabled () const [inline]</h3>
<p>Return true if the <code>Category</code> will log messages with priority WARN. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Whether the <code>Category</code> will log.</dl>
<h3>void log4cpp::Category::log (<code>Priority::Value</code>priority, const char *stringFormat, &#8230;) [virtual]</h3>
<p>Log a message with the specified priority. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>priority</i> The priority of this log message.<br />
 <i>stringFormat</i> Format specifier for the string to write in the log file.<br />
 <i>&#8230;</i> The arguments for stringFormat</dl>
<h3>void log4cpp::Category::log (<code>Priority::Value</code>priority, const std::string &amp;message) [virtual]</h3>
<p>Log a message with the specified priority. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>priority</i> The priority of this log message.<br />
 <i>message</i> string to write in the log file</dl>
<h3>void log4cpp::Category::logva (<code>Priority::Value</code>priority, const char *stringFormat, va_listva) [virtual]</h3>
<p>Log a message with the specified priority. </p>
<p> <code>Since:</code></p>
<dl COMPACT>
<dd>0.2.7</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>priority</i> The priority of this log message.<br />
 <i>stringFormat</i> Format specifier for the string to write in the log file.<br />
 <i>va</i> The arguments for stringFormat.</dl>
<h3>void log4cpp::Category::notice (const char *stringFormat, &#8230;)</h3>
<p>Log a message with notice priority. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>stringFormat</i> Format specifier for the string to write in the log file.<br />
 <i>&#8230;</i> The arguments for stringFormat</dl>
<h3>void log4cpp::Category::notice (const std::string &amp;message)</h3>
<p>Log a message with notice priority. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>message</i> string to write in the log file</dl>
<h3><code>CategoryStream</code> log4cpp::Category::noticeStream () [inline]</h3>
<p>Return a <code>CategoryStream</code> with priority NOTICE. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The <code>CategoryStream</code>.</dl>
<h3><code>CategoryStream</code> log4cpp::Category::operator&lt;&lt; (<code>Priority::Value</code>priority) [virtual]</h3>
<p>Return a <code>CategoryStream</code> with given <code>Priority</code>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>priority</i> The <code>Priority</code> of the <code>CategoryStream</code>.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The requested <code>CategoryStream</code>.</dl>
<h3>virtual bool log4cpp::Category::ownsAppender () const [inline], [virtual]</h3>
<p>Returns true if the <code>Category</code> owns the first <code>Appender</code> in its <code>Appender</code> set. In that case the <code>Category</code> destructor will delete the <code>Appender</code>. </p>
<p> <code>Deprecated</code></p>
<dl COMPACT>
<dd>use ownsAppender(Appender*)</dl>
<p> Reimplemented in <code>log4cpp::FixedContextCategory</code>.</p>
<h3>bool log4cpp::Category::ownsAppender (<code>Appender</code> *appender) const [virtual]</h3>
<p>Returns true if the <code>Category</code> owns the <code>Appender</code>. In that case the <code>Category</code> destructor will delete the <code>Appender</code>. </p>
<p> <code>Since:</code></p>
<dl COMPACT>
<dd>0.2.7</dl>
<p> Reimplemented in <code>log4cpp::FixedContextCategory</code>.</p>
<h3>void log4cpp::Category::removeAllAppenders () [virtual]</h3>
<p>Removes all appenders for this <code>Category</code>. </p>
<p> Reimplemented in <code>log4cpp::FixedContextCategory</code>.</p>
<h3>void log4cpp::Category::removeAppender (<code>Appender</code> *appender) [virtual]</h3>
<p>Removes specified appender for this <code>Category</code>. </p>
<p> <code>Since:</code></p>
<dl COMPACT>
<dd>0.2.7</dl>
<h3>void log4cpp::Category::setAdditivity (booladditivity) [virtual]</h3>
<p>Set the additivity flag for this <code>Category</code> instance. </p>
<p> Reimplemented in <code>log4cpp::FixedContextCategory</code>.</p>
<h3>void log4cpp::Category::setAppender (<code>Appender</code> *appender) [inline]</h3>
<p>Adds an <code>Appender</code> to this <code>Category</code>. This method passes ownership from the caller to the <code>Category</code>. </p>
<p> <code>Deprecated</code></p>
<dl COMPACT>
<dd>use <code>addAppender(Appender*)</code> or <code>removeAllAppenders()</code> instead.</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>appender</i> The <code>Appender</code> this category has to log to or NULL to remove the current Appenders.</dl>
<h3>void log4cpp::Category::setAppender (<code>Appender</code> &amp;appender) [inline]</h3>
<p>Adds an <code>Appender</code> for this <code>Category</code>. This method does not pass ownership from the caller to the <code>Category</code>. </p>
<p> <code>Deprecated</code></p>
<dl COMPACT>
<dd>use <code>addAppender(Appender&amp;)</code> instead.</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>appender</i> The <code>Appender</code> this category has to log to.</dl>
<h3>void log4cpp::Category::setPriority (<code>Priority::Value</code>priority)std::invalid_argument [virtual]</h3>
<p>Set the priority of this <code>Category</code>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>priority</i> The priority to set. Use <code>Priority::NOTSET</code> to let the category use its parents priority as effective priority.</dl>
<p> <code>Exceptions:</code></p>
<dl COMPACT>
<dd><i>std::invalid_argument</i> if the caller tries to set <code>Priority::NOTSET</code> on the Root <code>Category</code>.</dl>
<h3>void log4cpp::Category::setRootPriority (<code>Priority::Value</code>priority) [static]</h3>
<p>Set the priority of the root <code>Category</code>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>priority</i> The new priority for the root <code>Category</code></dl>
<h3>void log4cpp::Category::shutdown () [static]</h3>
<p>This method will remove all Appenders from Categories.XXX.</p>
<h3>void log4cpp::Category::warn (const char *stringFormat, &#8230;)</h3>
<p>Log a message with warn priority. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>stringFormat</i> Format specifier for the string to write in the log file.<br />
 <i>&#8230;</i> The arguments for stringFormat</dl>
<h3>void log4cpp::Category::warn (const std::string &amp;message)</h3>
<p>Log a message with warn priority. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>message</i> string to write in the log file</dl>
<h3><code>CategoryStream</code> log4cpp::Category::warnStream () [inline]</h3>
<p>Return a <code>CategoryStream</code> with priority WARN. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The <code>CategoryStream</code>.</dl>
<h2>Friends And Related Function Documentation</h2>
<h3>friend class <code>HierarchyMaintainer</code> [friend]</h3>
<h2>Author</h2>
<p>Generated automatically by Doxygen for log4cpp from the source code.</p>
