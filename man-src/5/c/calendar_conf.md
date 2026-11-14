---
title: "calendar_conf(5)"
name: "calendar_conf"
section: "5"
letter: "c"
url: "/docs/linux/man/5-calendar_conf/"
description: "calendar_conf – xxQS_NAMExx calendar configuration file format"
---

<p>calendar_conf &#8211; xxQS_NAMExx calendar configuration file format</p>
<h2>Description</h2>
<p><i>calendar_conf</i> defines the format of the xxQS_NAMExx calendar configuration. The definition of calendars is used to specify &quot;on duty&quot; and &quot;off duty&quot; time periods for xxQS_NAMExx queues on a time of day, day of week, or day of year basis. Various calendars can be implemented, and the appropriate calendar definition for a certain class of jobs can be attached to a queue. </p>
<p> <i>calendar_conf</i> entries can be added, modified and displayed with the <code>-Acal</code>, <code>-acal</code>, <code>-Mcal</code>, <code>-mcal</code>, <code>-scal</code> and <code>-scall</code> options to or with the calendar configuration dialog of the graphical user interface </p>
<p> Note that jobs may be dispatched incorrectly into calendar windows which are too short unless resource reservation is turned on by setting <code>max_reservation</code> in </p>
<p> Note, xxQS_NAMExx allows backslashes (\) to escape newline characters. The backslash and the newline are replaced with a space (&quot; &quot;) character before any interpretation.</p>
<h2>Format</h2>
<p>A configuration comprises three lines of this form, whose contents are described in the following sections: </p>
<pre> <code>calendar_name</code> <i>calendar_name</i>
 <code>yesr</code> <i>year</i>
 <code>day</code> <i>day</i></pre>
<h3>calendar_name</h3>
<p>The name of the calendar to be used when attaching it to queues, or when administering the calendar definition. See <i>calendar_name</i> in for a precise definition of valid calendar names.</p>
<h3>year</h3>
<p>The queue status definition on a day of the year basis. This field generally will specify on which days of a year (and optionally at which times on those days) a queue, to which the calendar is attached, will change to a certain state. The syntax of the <i>year</i> field is defined as follows: </p>
<pre><i>year</i> :=
 <code>NONE</code>
 | <i>year_day_range_list</i><code>=</code><i>daytime_range_list</i>[<code>=</code><i>state</i>]
 | <i>year_day_range_list</i><code>=</code>[<i>daytime_range_list</i><code>=</code>]<i>state</i>
 | <i>state</i></pre>
<p>Where</p>
<dl>
<dt>&bull;</p>
<dd><code>NONE</code> means no definition is made on the year basis;</p>
<dt>&bull;</p>
<dd>If a definition is made on the year basis, at least one of <i>year_day_range_list</i>, <i>daytime_range_list</i> and <i>state</i> always have to be present;</p>
<dt>&bull;</p>
<dd>All day long is assumed if <i>daytime_range_list</i> is omitted;</p>
<dt>&bull;</p>
<dd>Switching the queue to &quot;off&quot; (i.e. disabling it) is assumed if <i>state</i> is omitted;</p>
<dt>&bull;</p>
<dd>The queue is assumed to be enabled for days neither referenced implicitly (by omitting the <i>year_day_range_list</i>) nor explicitly.</dl>
<p> The syntactical components are defined as follows: </p>
<pre> <i>year_day_range_list</i> := {<i>yearday</i><code>-</code><i>yearday</i> | <i>yearday</i>},...
 <i>daytime_range_list</i> := <i>hour</i>[<code>:</code><i>minute</i>][<code>:</code><i>second</i>]<code>-</code><i>hour</i>[<code>:</code><i>minute</i>][<code>:</code><i>second</i>],...
 <i>state</i> := <code>on</code> | <code>off</code> | <code>suspended</code>
 <i>year_day</i> := <i>month_day</i><code>.</code><i>month</i><code>.</code><i>year</i>
 <i>month_day</i> := <code>1</code> | <code>2</code> | ... | <code>31</code>
 <i>month</i> := <code>jan</code> | <code>feb</code> | ... | <code>dec</code> | <code>1</code> | <code>2</code> | ... | <code>12</code>
 <i>year</i> := <code>1970</code> | <code>1971</code> | ... | <code>2037</code></pre>
<h3>week</h3>
<p>The queue status definition on a day of the week basis. This field generally will specify on which days of the week (and optionally at which times on those days) a queue to which the calendar is attached will change to a certain state. The syntax of the <i>week</i> field is defined as follows: </p>
<pre><i>week</i>:=
 <code>NONE</code> 
 | <i>week_day_range_list</i>[<code>=</code><i>daytime_range_list</i>][<code>=</code><i>state</i>]
 | [<i>week_day_range_list</i><code>=</code>]<i>daytime_range_list</i>[<code>=</code><i>state</i>]
 | [<i>week_day_range_list</i><code>=</code>][<i>daytime_range_list</i><code>=</code>]<i>state</i> ...</pre>
<p>where</p>
<dl>
<dt>&bull;</p>
<dd>NONE means, no definition is made on the week basis;</p>
<dt>&bull;</p>
<dd>If a definition is made on the week basis, at least one of <i>week_day_range_list</i>, <i>daytime_range_list</i> and <i>state</i> always have to be present;</p>
<dt>&bull;</p>
<dd>Every day in the week is assumed if <i>week_day_range_list</i> is omitted;</p>
<dt>&bull;</p>
<dd>Syntax and semantics of <i>daytime_range_list</i> and <i>state</i> are identical to the definition given for the year field above;</p>
<dt>&bull;</p>
<dd>The queue is assumed to be enabled for days neither referenced implicitly (by omitting the <i>week_day_range_list</i>) nor explicitly.</dl>
<p> and where <i>week_day_range_list</i> is defined as </p>
<pre> <i>week_day_range_list</i> := {<i>weekday</i><code>-</code><i>weekday</i> | <i>weekday</i>},...
 <i>week_day</i> := <code>mon</code> | <code>tue</code> | <code>wed</code> | <code>thu</code> | <code>fri</code> | <code>sat</code> | <code>sun</code></pre>
<p>With week_day ranges the <i>week_day</i> identifiers must be different.</p>
<h2>Semantics</h2>
<p>Successive entries to the <i>year</i> and <i>week</i> fields (separated by blanks) are combined in accordance with the following rule:</p>
<dl>
<dt>&bull;</p>
<dd><code>off</code> areas are overridden by overlapping <code>on</code> and <code>suspended</code> areas and <code>suspended</code> areas are overridden by <code>on</code> areas.</dl>
<p> Hence an entry of the form </p>
<pre> week 12-18 tue=13-17=on</pre>
<p>means that queues referencing the corresponding calendar are disabled for the entire week from 12.00-18.00, with the exception of Tuesday between 13.00-17.00, when the queues are available. </p>
<dl>
<dt>&bull;</p>
<dd>Area overriding occurs only within a year/week basis. If a year entry exists for a day, then only the year calendar is taken into account, and no area overriding is done with a possibly conflicting week area. </p>
<dt>&bull;</p>
<dd>The second time specification in a <i>daytime_range_list</i> may be before the first one and treated as expected. Thus an entry of the form </p>
<pre> year 12.03.2004=12-11=off </pre>
<p>causes the queue(s) be disabled on 12.03.2004 from 00:00:00 &#8211; 10:59:59 and 12:00:00 &#8211; 23:59:59.</dl>
<h2>Examples</h2>
<p>(The following examples are contained in the directory <i>$xxQS_NAME_Sxx_ROOT/util/resources/calendars</i>.)</p>
<dl>
<dt>&bull;</p>
<dd>Night, weekend and public holiday calendar: On public holidays &quot;night&quot; queues are explicitly enabled. On working days queues are disabled between 6.00 and 20.00. Saturday and Sunday are implicitly handled as enabled times: </p>
<pre> calendar_name night
 year 1.1.1999,6.1.1999,28.3.1999,30.3.1999-
 31.3.1999,18.5.1999-19.5.1999,3.10.1999,25.12.1999,26
 .12.1999=on
 week mon-fri=6-20</pre>
<dt>&bull;</p>
<dd>Day calendar: On public holidays &quot;day&quot;-queues are disabled. On working days such queues are closed during the night between 20.00 and 6.00, i.e. the queues are also closed on Monday from 0.00 to 6.00 and on Friday from 20.00 to 24.00. On Saturday and Sunday the queues are disabled. </p>
<pre> calendar_name day
 year 1.1.1999,6.1.1999,28.3.1999,30.3.1999-
 31.3.1999,18.5.1999-19.5.1999,3.10.1999,25.12.1999,26
 .12.1999
 week mon-fri=20-6 sat-sun</pre>
<dt>&bull;</p>
<dd>Night, weekend and public holiday calendar with suspension: Essentially the same scenario as the first example but queues are suspended instead of switching them &quot;off&quot;. </p>
<pre> calendar_name night_s
 year 1.1.1999,6.1.1999,28.3.1999,30.3.1999-
 31.3.1999,18.5.1999-19.5.1999,3.10.1999,25.12.1999,26
 .12.1999=on
 week mon-fri=6-20=suspended</pre>
<dt>&bull;</p>
<dd>Day calendar with suspension: Essentially the same scenario as the second example, but queues are suspended instead of switching them &quot;off&quot;. </p>
<pre> calendar_name day_s
 year 1.1.1999,6.1.1999,28.3.1999,30.3.1999-
 31.3.1999,18.5.1999-19.5.1999,3.10.1999,25.12.1999,26
 .12.1999=suspended
 week mon-fri=20-6=suspended sat-sun=suspended</pre>
<dt>&bull;</p>
<dd>Weekend calendar with suspension, ignoring public holidays: Settings are only done on the week basis, with no settings on the year basis (keyword &quot;NONE&quot;). </p>
<pre> calendar_name weekend_s
 year NONE
 week sat-sun=suspended</pre>
<h2>See Also</h2>
<h2>Copyright</h2>
<p>See for a full statement of rights and permissions.</p>
