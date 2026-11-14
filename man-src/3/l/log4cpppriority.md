---
title: "log4cpppriority(3)"
name: "log4cpppriority"
section: "3"
letter: "l"
url: "/docs/linux/man/3-log4cpppriority/"
description: "log4cpp::Priority –"
---

<p>log4cpp::Priority &#8211; </p>
<p> The <code>Priority</code> class provides importance levels with which one can categorize log messages.</p>
<h2>Synopsis</h2>
<p>#include &lt;Priority.hh&gt;</p>
<h3>Public Types</h3>
<p>enum <code>PriorityLevel</code> { <code>EMERG</code> = 0, <code>FATAL</code> = 0, <code>ALERT</code> = 100, <code>CRIT</code> = 200, <code>ERROR</code> = 300, <code>WARN</code> = 400, <code>NOTICE</code> = 500, <code>INFO</code> = 600, <code>DEBUG</code> = 700, <code>NOTSET</code> = 800 }<br />
 <i>Predefined Levels of Priorities. </i><br />
 typedef int <code>Value</code><br />
 <i>The type of </i><code>Priority</code> Values.</p>
<h3>Static Public Member Functions</h3>
<p>static const std::string &amp; <code>getPriorityName</code> (int priority) throw ()<br />
 <i>Returns the name of the given priority value. </i><br />
 static <code>Value</code> <code>getPriorityValue</code> (const std::string &amp;priorityName) throw (std::invalid_argument)<br />
 <i>Returns the value of the given priority name. </i></p>
<h3>Static Public Attributes</h3>
<p>static const int <code>MESSAGE_SIZE</code> = 8 </p>
<h2>Detailed Description</h2>
<p>The <code>Priority</code> class provides importance levels with which one can categorize log messages.</p>
<h2>Member Typedef Documentation</h2>
<h3>typedef int <code>log4cpp::Priority::Value</code></h3>
<p>The type of <code>Priority</code> Values.</p>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>log4cpp::Priority::PriorityLevel</code></h3>
<p>Predefined Levels of Priorities. These correspond to the priority levels used by <a href="/docs/linux/man/3-syslog/">syslog</a>(3). </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>EMERG </i></p>
<dd>
<dt><i>FATAL </i></p>
<dd>
<dt><i>ALERT </i></p>
<dd>
<dt><i>CRIT </i></p>
<dd>
<dt><i>ERROR </i></p>
<dd>
<dt><i>WARN </i></p>
<dd>
<dt><i>NOTICE </i></p>
<dd>
<dt><i>INFO </i></p>
<dd>
<dt><i>DEBUG </i></p>
<dd>
<dt><i>NOTSET </i></p>
<dd></dl>
<h2>Member Function Documentation</h2>
<h3>const std::string &amp; log4cpp::Priority::getPriorityName (intpriority) [static]</h3>
<p>Returns the name of the given priority value. Currently, if the value is not one of the PriorityLevel values, the method returns the name of the largest priority smaller the given value. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>priority</i> the numeric value of the priority.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>a string representing the name of the priority.</dl>
<h3><code>Priority::Value</code> log4cpp::Priority::getPriorityValue (const std::string &amp;priorityName)std::invalid_argument [static]</h3>
<p>Returns the value of the given priority name. This can be either one of EMERG &#8230; NOTSET or a decimal string representation of the value, e.g. &#8216;700&#8217; for DEBUG. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>priorityName</i> the string containing the the of the priority</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the value corresponding with the priority name</dl>
<p> <code>Exceptions:</code></p>
<dl COMPACT>
<dd><i>std::invalid_argument</i> if the priorityName does not correspond with a known <code>Priority</code> name or a number</dl>
<h2>Member Data Documentation</h2>
<h3>const int log4cpp::Priority::MESSAGE_SIZE = 8 [static]</h3>
<h2>Author</h2>
<p>Generated automatically by Doxygen for log4cpp from the source code.</p>
