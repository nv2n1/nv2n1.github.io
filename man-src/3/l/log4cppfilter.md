---
title: "log4cppfilter(3)"
name: "log4cppfilter"
section: "3"
letter: "l"
url: "/docs/linux/man/3-log4cppfilter/"
description: "log4cpp::Filter –"
---

<p>log4cpp::Filter &#8211; </p>
<p> Users should extend this class to implement customized logging event filtering.</p>
<h2>Synopsis</h2>
<p>#include &lt;Filter.hh&gt;</p>
<h3>Public Types</h3>
<p>enum <code>Decision</code> { <code>DENY</code> = -1, <code>NEUTRAL</code> = 0, <code>ACCEPT</code> = 1 } </p>
<h3>Public Member Functions</h3>
<p><code>Filter</code> ()<br />
 <i>Default Constructor for </i><code>Filter</code>.<br />
 virtual <code>~Filter</code> ()<br />
 <i>Destructor for </i><code>Filter</code>.<br />
 virtual void <code>setChainedFilter</code> (<code>Filter</code> *filter)<br />
 <i>Set the next </i><code>Filter</code> in the <code>Filter</code> chain.<br />
 virtual <code>Filter</code> * <code>getChainedFilter</code> ()<br />
 <i>Get the next </i><code>Filter</code> in the <code>Filter</code> chain.<br />
 virtual <code>Filter</code> * <code>getEndOfChain</code> ()<br />
 <i>Get the last </i><code>Filter</code> in the <code>Filter</code> chain.<br />
 virtual void <code>appendChainedFilter</code> (<code>Filter</code> *filter)<br />
 <i>Add a </i><code>Filter</code> to the end of the <code>Filter</code> chain.<br />
 virtual <code>Decision</code> <code>decide</code> (const <code>LoggingEvent</code> &amp;event)<br />
 <i>Decide whether to accept or deny a </i><code>LoggingEvent</code>.</p>
<h3>Protected Member Functions</h3>
<p>virtual <code>Decision</code> <code>_decide</code> (const <code>LoggingEvent</code> &amp;event)=0<br />
 <i>Decide whether </i><code>this</code> <code>Filter</code> accepts or denies the given <code>LoggingEvent</code>.</p>
<h2>Detailed Description</h2>
<p>Users should extend this class to implement customized logging event filtering. </p>
<p> Note that <code>log4cpp::Category</code> and lof4cpp::Appender have built-in filtering rules. It is suggested that you first use and understand the built-in rules before rushing to write your own custom filters. </p>
<p> This abstract class assumes and also imposes that filters be organized in a linear chain. The decide(LoggingEvent) method of each filter is called sequentially, in the order of their addition to the chain. </p>
<p> The decide(LoggingEvent) method must return a Decision value, either DENY, NEUTRAL or ACCCEPT. </p>
<p> If the value DENY is returned, then the log event is dropped immediately without consulting with the remaining filters. </p>
<p> If the value NEUTRAL is returned, then the next filter in the chain is consulted. If there are no more filters in the chain, then the log event is logged. Thus, in the presence of no filters, the default behaviour is to log all logging events. </p>
<p> If the value ACCEPT is returned, then the log event is logged without consulting the remaining filters. </p>
<p> The philosophy of <code>log4cpp</code> filters is largely inspired from the Linux ipchains.</p>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>log4cpp::Filter::Decision</code></h3>
<p><code>Enumerator</code></p>
<dl COMPACT>
<dt><i>DENY </i></p>
<dd>
<dt><i>NEUTRAL </i></p>
<dd>
<dt><i>ACCEPT </i></p>
<dd></dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>log4cpp::Filter::Filter ()</h3>
<p>Default Constructor for <code>Filter</code>.</p>
<h3>log4cpp::Filter::~Filter () [virtual]</h3>
<p>Destructor for <code>Filter</code>.</p>
<h2>Member Function Documentation</h2>
<h3>virtual <code>Decision</code> log4cpp::Filter::_decide (const <code>LoggingEvent</code> &amp;event) [protected], [pure virtual]</h3>
<p>Decide whether <code>this</code> <code>Filter</code> accepts or denies the given <code>LoggingEvent</code>. Actual implementation of <code>Filter</code> should override this method and not decide(LoggingEvent&amp;). </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>event</i> The <code>LoggingEvent</code> to decide on.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The Decision</dl>
<h3>void log4cpp::Filter::appendChainedFilter (<code>Filter</code> *filter) [virtual]</h3>
<p>Add a <code>Filter</code> to the end of the <code>Filter</code> chain. Convience method for <code>getEndOfChain()</code>-&gt;setChainedFilter(filter). </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>filter</i> The filter to add to the end of the chain.</dl>
<h3><code>Filter::Decision</code> log4cpp::Filter::decide (const <code>LoggingEvent</code> &amp;event) [virtual]</h3>
<p>Decide whether to accept or deny a <code>LoggingEvent</code>. This method will walk the entire chain until a non neutral decision has been made or the end of the chain has been reached. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>event</i> The <code>LoggingEvent</code> to decide on.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The Decision</dl>
<h3><code>Filter</code> * log4cpp::Filter::getChainedFilter () [virtual]</h3>
<p>Get the next <code>Filter</code> in the <code>Filter</code> chain. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The next <code>Filter</code> or NULL if the current filter is the last in the chain</dl>
<h3><code>Filter</code> * log4cpp::Filter::getEndOfChain () [virtual]</h3>
<p>Get the last <code>Filter</code> in the <code>Filter</code> chain. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The last <code>Filter</code> in the <code>Filter</code> chain</dl>
<h3>void log4cpp::Filter::setChainedFilter (<code>Filter</code> *filter) [virtual]</h3>
<p>Set the next <code>Filter</code> in the <code>Filter</code> chain. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>filter</i> The filter to chain</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for log4cpp from the source code.</p>
