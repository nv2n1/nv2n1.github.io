---
title: "sge_calendar_conf(5)"
name: "sge_calendar_conf"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sge_calendar_conf/"
description: "calendar_conf – Grid Engine calendar configuration file format"
---

<p>calendar_conf &#8211; Grid Engine calendar configuration file format</p>
<h2>Description</h2>
<p><i>calendar_conf</i> reflects the format of the Grid Engine calendar configuration. The definition of calendars is used to specify &quot;on duty&quot; and &quot;off duty&quot; time periods for Grid Engine queues on a time of day, day of week or day of year basis. Various calendars can be implemented and the appropriate calendar definition for a certain class of jobs can be attached to a queue. </p>
<p> <i>calendar_conf</i> entries can be added, modified and displayed with the <i>-Acal</i>, <i>-acal</i>, <i>-Mcal</i>, <i>-mcal</i>, <i>-scal</i> and <i>-scall</i> options to or with the calendar configuration dialog of the graphical user interface </p>
<p> Note, Grid Engine allows backslashes (\) be used to escape newline (
ewline) characters. The backslash and the newline are replaced with a space (&quot; &quot;) character before any interpretation.</p>
<h2>Format</h2>
<h3><code>calendar_name</code></h3>
<p>The name of the calendar to be used when attaching it to queues or when administering the calendar definition. See <i>calendar_name</i> in for a precise definition of valid calendar names.</p>
<h3><code>year</code></h3>
<p>The queue status definition on a day of the year basis. This field generally will specify on which days of a year (and optionally at which times on those days) a queue, to which the calendar is attached, will change to a certain state. The syntax of the <code>year</code> field is defined as follows: </p>
<pre><code>year</code>:=
 { NONE
 | <code>year_day_range_list=</code><code>daytime_range_list</code>[<code>=state</code>]
 | <code>year_day_range_list=</code>[<code>daytime_range_list=</code>]<code>state</code>
 | state}</pre>
<p>Where</p>
<dl>
<dt>*</p>
<dd>NONE means, no definition is made on the year basis</p>
<dt>*</p>
<dd>if a definition is made on the year basis, at least one of <code>year_day_range_list</code>, <code>daytime_range_list</code> and <code>state</code> always have to be present,</p>
<dt>*</p>
<dd>all day long is assumed if <code>daytime_range_list</code> is omitted,</p>
<dt>*</p>
<dd>switching the queue to &quot;off&quot; (i.e. disabling it) is assumed if <code>state</code> is omitted,</p>
<dt>*</p>
<dd>the queue is assumed to be enabled for days neither referenced implicitly (by omitting the <code>year_day_range_list</code>) nor explicitly</dl>
<p> and the syntactical components are defined as follows: </p>
<pre> <code>year_day_range_list</code> := {<code>yearday</code>-<code>yearday</code>|<code>yearday</code>},...
 <code>daytime_range_list</code> := hour[:minute][:second]-
 hour[:minute][:second],...
 <code>state</code> := {on|off|suspended}
 <code>year_day</code> := <code>month_day.month.year</code>
 <code>month_day</code> := {1|2|...|31}
 <code>month</code> := {jan|feb|...|dec|1|2|...|12}
 <code>year</code> := {1970|1971|...|2037}</pre>
<h3><code>week</code></h3>
<p>The queue status definition on a day of the week basis. This field generally will specify on which days of a week (and optionally at which times on those days) a queue, to which the calendar is attached, will change to a certain state. The syntax of the <code>week</code> field is defined as follows: </p>
<pre><code>week</code>:=
 { NONE 
 | <code>week_day_range_list</code>[<code>=daytime_range_list</code>][<code>=state</code>]
 | [<code>week_day_range_list=</code>]<code>daytime_range_list</code>[<code>=state</code>]
 | [<code>week_day_range_list=</code>][<code>daytime_range_list=</code>]<code>state</code>} ...</pre>
<p>Where</p>
<dl>
<dt>*</p>
<dd>NONE means, no definition is made on the week basis</p>
<dt>*</p>
<dd>if a definition is made on the week basis, at least one of <code>week_day_range_list</code>, <code>daytime_range_list</code> and <code>state</code> always have to be present,</p>
<dt>*</p>
<dd>every day in the week is assumed if <code>week_day_range_list</code> is omitted,</p>
<dt>*</p>
<dd>syntax and semantics of <code>daytime_range_list</code> and <code>state</code> are identical to the definition given for the year field above,</p>
<dt>*</p>
<dd>the queue is assumed to be enabled for days neither referenced implicitly (by omitting the <code>week_day_range_list</code>) nor explicitly</dl>
<p> and where <code>week_day_range_list</code> is defined as </p>
<pre> <code>week_day_range_list</code> := {<code>weekday</code>-<code>weekday</code>|<code>weekday</code>},...
 <code>week_day</code> := {mon|tue|wed|thu|fri|sat|sun}</pre>
<p>with week_day ranges the week_day identifiers must be different.</p>
<h2>Semantics</h2>
<p>Successive entries to the <code>year</code> and <code>week</code> fields (separated by blanks) are combined in compliance with the following rule:</p>
<dl>
<dt>*</p>
<dd>&quot;off&quot;-areas are overridden by overlapping &quot;on&quot;- and &quot;suspended&quot;-areas and &quot;suspended&quot;-areas are overridden by &quot;on&quot;-areas.</dl>
<p> Hence an entry of the form </p>
<pre> week 12-18 tue=13-17=on</pre>
<p>means that queues referencing the corresponding calendar are disabled the entire week from 12.00-18.00 with the exception of Tuesday between 13.00-17.00 where the queues are available. </p>
<dl>
<dt>*</p>
<dd>Area overriding occurs only within a year/week basis. If a year entry exists for a day then only the year calendar is taken into account and no area overriding is done with a possibly conflicting week area. </p>
<dt>*</p>
<dd>the second time specification in a daytime_range_list may be before the first one and treated as expected. Thus an entry of the form </p>
<pre> year 12.03.2004=12-11=off </pre>
<p>causes the queue(s) be disabled 12.03.2004 from 00:00:00 &#8211; 10:59:59 and 12:00:00 &#8211; 23:59:59.</dl>
<h2>Examples</h2>
<p>(The following examples are contained in the directory $GE_ROOT/util/resources/calendars).</p>
<dl>
<dt>*</p>
<dd>Night, weekend and public holiday calendar: On public holidays &quot;night&quot; queues are explicitly enabled. On working days queues are disabled between 6.00 and 20.00. Saturday and Sunday are implicitly handled as enabled times: </p>
<pre> calendar_name night
 year 1.1.1999,6.1.1999,28.3.1999,30.3.1999-
 31.3.1999,18.5.1999-19.5.1999,3.10.1999,25.12.1999,26
 .12.1999=on
 week mon-fri=6-20</pre>
<dt>*</p>
<dd>Day calendar: On public holidays &quot;day&quot;-queues are disabled. On working days such queues are closed during the night between 20.00 and 6.00, i.e. the queues are also closed on Monday from 0.00 to 6.00 and on Friday from 20.00 to 24.00. On Saturday and Sunday the queues are disabled. </p>
<pre> calendar_name day
 year 1.1.1999,6.1.1999,28.3.1999,30.3.1999-
 31.3.1999,18.5.1999-19.5.1999,3.10.1999,25.12.1999,26
 .12.1999
 week mon-fri=20-6 sat-sun</pre>
<dt>*</p>
<dd>Night, weekend and public holiday calendar with suspension: Essentially the same scenario as the first example but queues are suspended instead of switching them &quot;off&quot;. </p>
<pre> calendar_name night_s
 year 1.1.1999,6.1.1999,28.3.1999,30.3.1999-
 31.3.1999,18.5.1999-19.5.1999,3.10.1999,25.12.1999,26
 .12.1999=on
 week mon-fri=6-20=suspended</pre>
<dt>*</p>
<dd>Day calendar with suspension: Essentially the same scenario as the second example but queues are suspended instead of switching them &quot;off&quot;. </p>
<pre> calendar_name day_s
 year 1.1.1999,6.1.1999,28.3.1999,30.3.1999-
 31.3.1999,18.5.1999-19.5.1999,3.10.1999,25.12.1999,26
 .12.1999=suspended
 week mon-fri=20-6=suspended sat-sun=suspended</pre>
<dt>*</p>
<dd>Weekend calendar with suspension, ignoring public holidays: Settings are only done on the week basis, no settings on the year basis (keyword &quot;NONE&quot;). </p>
<pre> calendar_name weekend_s
 year NONE
 week sat-sun=suspended</pre>
<h2>See Also</h2>
<h2>Copyright</h2>
<p>See for a full statement of rights and permissions.</p>
