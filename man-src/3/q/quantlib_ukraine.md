---
title: "quantlib_ukraine(3)"
name: "quantlib_ukraine"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_ukraine/"
description: "QuantLib::Ukraine – Ukrainian calendars."
---

<p>QuantLib::Ukraine &#8211; Ukrainian calendars. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/time/calendars/ukraine.hpp&gt; </p>
<p> Inherits <code>QuantLib::Calendar</code>. </p>
<h3>Public Types</h3>
<p>enum <code>Market</code> { <code>USE</code> } </p>
<h3>Public Member Functions</h3>
<p><code>Ukraine</code> (<code>Market</code> m=USE) </p>
<h2>Detailed Description</h2>
<p>Ukrainian calendars. </p>
<p> Holidays for the Ukrainian stock exchange (data from &lt;<a rel="nofollow" href="http://www.ukrse.kiev.ua/eng/">http://www.ukrse.kiev.ua/eng/</a>&gt;): </p>
<dl COMPACT>
<dt>*</dt>
<dd>Saturdays</dd>
<dt>*</dt>
<dd>Sundays</dd>
<dt>*</dt>
<dd>New Year&#8217;s Day, January 1st</dd>
<dt>*</dt>
<dd>Orthodox Christmas, January 7th</dd>
<dt>*</dt>
<dd>International Women&#8217;s Day, March 8th</dd>
<dt>*</dt>
<dd>Easter Monday</dd>
<dt>*</dt>
<dd>Holy Trinity Day, 50 days after Easter</dd>
<dt>*</dt>
<dd>International Workers&#8217; Solidarity Days, May 1st and 2nd</dd>
<dt>*</dt>
<dd>Victory Day, May 9th</dd>
<dt>*</dt>
<dd>Constitution Day, June 28th</dd>
<dt>*</dt>
<dd>Independence Day, August 24th</dd></dl>
<p> Holidays falling on a Saturday or Sunday are moved to the following Monday.</p>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>Market</code></h3>
<p><code>Enumerator: </code></p>
<dl COMPACT>
<dt><i>USE </i></dt>
<dd>Ukrainian stock exchange. </dd>
</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
