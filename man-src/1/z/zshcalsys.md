---
title: "zshcalsys(1)"
name: "zshcalsys"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zshcalsys/"
description: "zshcalsys – zsh calendar system"
---

<h2 class="name">NAME</h2>
<p> zshcalsys &#8211; zsh calendar system </p>
<h2>DESCRIPTION</h2>
<p> The shell is supplied with a series of functions to replace and enhance the traditional Unix <code>calendar</code> programme, which warns the user of imminent or future events, details of which are stored in a text file (typically <code>calendar</code> in the user&#8217;s home directory). The version provided here includes a mechanism for alerting the user when an event is due. </p>
<p> In addition functions <code>age</code>, <code>before</code> and <code>after</code> are provided that can be used in a glob qualifier; they allow files to be selected based on their modification times. </p>
<p> The format of the <code>calendar</code> file and the dates used there in and in the <code>age</code> function are described first, then the functions that can be called to examine and modify the <code>calendar</code> file. </p>
<p> The functions here depend on the availability of the <code>zsh/datetime</code> module which is usually installed with the shell. The library function <code>strptime()</code> must be available; it is present on most recent operating systems. </p>
<h2>FILE AND DATE FORMATS</h2>
<h3>Calendar File Format</h3>
<p> The calendar file is by default <code>~/calendar</code>. This can be configured by the <code>calendar-file</code> style, see the section STYLES below. The basic format consists of a series of separate lines, with no indentation, each including a date and time specification followed by a description of the event. </p>
<p> Various enhancements to this format are supported, based on the syntax of Emacs calendar mode. An indented line indicates a continuation line that continues the description of the event from the preceding line (note the date may not be continued in this way). An initial ampersand (<code>&amp;</code>) is ignored for compatibility. </p>
<p> An indented line on which the first non-whitespace character is <code>#</code> is not displayed with the calendar entry, but is still scanned for information. This can be used to hide information useful to the calendar system but not to the user, such as the unique identifier used by <code>calendar_add</code>. </p>
<p> The Emacs extension that a date with no description may refer to a number of succeeding events at different times is not supported. </p>
<p> Unless the <code>done-file</code> style has been altered, any events which have been processed are appended to the file with the same name as the calendar file with the suffix <code>.done</code>, hence <code>~/calendar.done</code> by default. </p>
<p> An example is shown below. </p>
<h3>Date Format</h3>
<p> The format of the date and time is designed to allow flexibility without admitting ambiguity. (The words `date&#8217; and `time&#8217; are both used in the documentation below; except where specifically noted this implies a string that may include both a date and a time specification.) Note that there is no localization support; month and day names must be in English and separator characters are fixed. Matching is case insensitive, and only the first three letters of the names are significant, although as a special case a form beginning &quot;month&quot; does not match &quot;Monday&quot;. Furthermore, time zones are not handled; all times are assumed to be local. </p>
<p> It is recommended that, rather than exploring the intricacies of the system, users find a date format that is natural to them and stick to it. This will avoid unexpected effects. Various key facts should be noted. </p>
<dl>
<dt>
<dd> &bull; In particular, note the confusion between <i>month</i><code>/</code><i>day</i><code>/</code><i>year</i> and <i>day</i><code>/</code><i>month</i><code>/</code><i>year</i> when the month is numeric; these formats should be avoided if at all possible. Many alternatives are available.</p>
<dt>&bull;</p>
<dd> The year must be given in full to avoid confusion, and only years from 1900 to 2099 inclusive are matched.</dl>
<p> The following give some obvious examples; users finding here a format they like and not subject to vagaries of style may skip the full description. As dates and times are matched separately (even though the time may be embedded in the date), any date format may be mixed with any format for the time of day provide the separators are clear (whitespace, colons, commas). </p>
<dl>
<dt>
<dd>
<pre>
<code>2007/04/03 13:13
2007/04/03:13:13
2007/04/03 1:13 pm
3rd April 2007, 13:13
April 3rd 2007 1:13 p.m.
Apr 3, 2007 13:13
Tue Apr 03 13:13:00 2007
13:13 2007/apr/3</code>
</pre>
</dl>
<p> More detailed rules follow. </p>
<p> Times are parsed and extracted before dates. They must use colons to separate hours and minutes, though a dot is allowed before seconds if they are present. This limits time formats to the following: </p>
<dl>
<dt>
<dd> &bull; <i>HH</i><code>:</code><i>MM</i>[<code>:</code><i>SS</i>[<code>.</code><i>FFFFF</i>]] [<code>am</code>|<code>pm</code>|<code>a.m.</code>|<code>p.m.</code>]</p>
<dt>&bull;</p>
<dd> <i>HH</i><code>:</code><i>MM</i><code>.</code><i>SS</i>[<code>.</code><i>FFFFF</i>] [<code>am</code>|<code>pm</code>|<code>a.m.</code>|<code>p.m.</code>]</dl>
<p> Here, square brackets indicate optional elements, possibly with alternatives. Fractions of a second are recognised but ignored. For absolute times (the normal format require by the <code>calendar</code> file and the <code>age</code>, <code>before</code> and <code>after</code> functions) a date is mandatory but a time of day is not; the time returned is at the start of the date. One variation is allowed: if <code>a.m.</code> or <code>p.m.</code> or one of their variants is present, an hour without a minute is allowed, e.g. <code>3 p.m.</code>. </p>
<p> Time zones are not handled, though if one is matched following a time specification it will be removed to allow a surrounding date to be parsed. This only happens if the format of the timezone is not too unusual. The following are examples of forms that are understood: </p>
<dl>
<dt>
<dd>
<pre>
<code>+0100
GMT
GMT-7
CET+1CDT</code>
</pre>
</dl>
<p> Any part of the timezone that is not numeric must have exactly three capital letters in the name. </p>
<p> Dates suffer from the ambiguity between <i>DD</i><code>/</code><i>MM</i><code>/</code><i>YYYY</i> and <i>MM</i><code>/</code><i>DD</i><code>/</code><i>YYYY</i>. It is recommended this form is avoided with purely numeric dates, but use of ordinals, eg. <code>3rd/04/2007</code>, will resolve the ambiguity as the ordinal is always parsed as the day of the month. Years must be four digits (and the first two must be <code>19</code> or <code>20</code>); <code>03/04/08</code> is not recognised. Other numbers may have leading zeroes, but they are not required. The following are handled: </p>
<dl>
<dt>
<dd> &bull; <i>YYYY</i><code>/</code><i>MM</i><code>/</code><i>DD</i></p>
<dt>&bull;</p>
<dd> <i>YYYY</i><code>&#8211;</code><i>MM</i><code>&#8211;</code><i>DD</i></p>
<dt>&bull;</p>
<dd> <i>YYYY</i><code>/</code><i>MNM</i><code>/</code><i>DD</i></p>
<dt>&bull;</p>
<dd> <i>YYYY</i><code>&#8211;</code><i>MNM</i><code>&#8211;</code><i>DD</i></p>
<dt>&bull;</p>
<dd> <i>DD</i>[<code>th</code>|<code>st</code>|<code>rd</code>] <i>MNM</i>[<code>,</code>] [ <i>YYYY</i> ]</p>
<dt>&bull;</p>
<dd> <i>MNM</i> <i>DD</i>[<code>th</code>|<code>st</code>|<code>rd</code>][<code>,</code>] [ <i>YYYY</i> ]</p>
<dt>&bull;</p>
<dd> <i>DD</i>[<code>th</code>|<code>st</code>|<code>rd</code>]<code>/</code><i>MM</i>[<code>,</code>] <i>YYYY</i></p>
<dt>&bull;</p>
<dd> <i>DD</i>[<code>th</code>|<code>st</code>|<code>rd</code>]<code>/</code><i>MM</i><code>/</code><i>YYYY</i></p>
<dt>&bull;</p>
<dd> <i>MM</i><code>/</code><i>DD</i>[<code>th</code>|<code>st</code>|<code>rd</code>][<code>,</code>] <i>YYYY</i></p>
<dt>&bull;</p>
<dd> <i>MM</i><code>/</code><i>DD</i>[<code>th</code>|<code>st</code>|<code>rd</code>]<code>/</code><i>YYYY</i></dl>
<p> Here, <i>MNM</i> is at least the first three letters of a month name, matched case-insensitively. The remainder of the month name may appear but its contents are irrelevant, so janissary, febrile, martial, apricot, maybe, junta, etc. are happily handled. </p>
<p> Where the year is shown as optional, the current year is assumed. There are only two such cases, the form <code>Jun 20</code> or <code>14 September</code> (the only two commonly occurring forms, apart from a &quot;the&quot; in some forms of English, which isn&#8217;t currently supported). Such dates will of course become ambiguous in the future, so should ideally be avoided. </p>
<p> Times may follow dates with a colon, e.g. <code>1965/07/12:09:45</code>; this is in order to provide a format with no whitespace. A comma and whitespace are allowed, e.g. <code>1965/07/12, 09:45</code>. Currently the order of these separators is not checked, so illogical formats such as <code>1965/07/12, : ,09:45</code> will also be matched. For simplicity such variations are not shown in the list above. Otherwise, a time is only recognised as being associated with a date if there is only whitespace in between, or if the time was embedded in the date. </p>
<p> Days of the week are not normally scanned, but will be ignored if they occur at the start of the date pattern only. However, in contexts where it is useful to specify dates relative to today, days of the week with no other date specification may be given. The day is assumed to be either today or within the past week. Likewise, the words <code>yesterday</code>, <code>today</code> and <code>tomorrow</code> are handled. All matches are case-insensitive. Hence if today is Monday, then <code>Sunday</code> is equivalent to <code>yesterday</code>, <code>Monday</code> is equivalent to <code>today</code>, but <code>Tuesday</code> gives a date six days ago. This is not generally useful within the calendar file. Dates in this format may be combined with a time specification; for example <code>Tomorrow, 8 p.m.</code>. </p>
<p> For example, the standard date format: </p>
<dl>
<dt>
<dd>
<pre>
<code>Fri Aug 18 17:00:48 BST 2006</code>
</pre>
</dl>
<p> is handled by matching <i>HH</i><code>:</code><i>MM</i><code>:</code><i>SS</i> and removing it together with the matched (but unused) time zone. This leaves the following: </p>
<dl>
<dt>
<dd>
<pre>
<code>Fri Aug 18 2006</code>
</pre>
</dl>
<p> <code>Fri</code> is ignored and the rest is matched according to the standard rules. </p>
<h3>Relative Time Format</h3>
<p> In certain places relative times are handled. Here, a date is not allowed; instead a combination of various supported periods are allowed, together with an optional time. The periods must be in order from most to least significant. </p>
<p> In some cases, a more accurate calculation is possible when there is an anchor date: offsets of months or years pick the correct day, rather than being rounded, and it is possible to pick a particular day in a month as `(1st Friday)&#8217;, etc., as described in more detail below. </p>
<p> Anchors are available in the following cases. If one or two times are passed to the function <code>calendar</code>, the start time acts an anchor for the end time when the end time is relative (even if the start time is implicit). When examining calendar files, the scheduled event being examined anchors the warning time when it is given explicitly by means of the <code>WARN</code> keyword; likewise, the scheduled event anchors a repetition period when given by the <code>RPT</code> keyword, so that specifications such as <code>RPT 2 months, 3rd Thursday</code> are handled properly. Finally, the <code>-R</code> argument to <code>calendar_scandate</code> directly provides an anchor for relative calculations. </p>
<p> The periods handled, with possible abbreviations are: </p>
<dl>
<dt>
<dd> Years <code>years</code>, <code>yrs</code>, <code>ys</code>, <code>year</code>, <code>yr</code>, <code>y</code>, <code>yearly</code>. A year is 365.25 days unless there is an anchor.</p>
<dt>Months</p>
<dd> <code>months</code>, <code>mons</code>, <code>mnths</code>, <code>mths</code>, <code>month</code>, <code>mon</code>, <code>mnth</code>, <code>mth</code>, <code>monthly</code>. Note that <code>m</code>, <code>ms</code>, <code>mn</code>, <code>mns</code> are ambiguous and are <i>not</i> handled. A month is a period of 30 days rather than a calendar month unless there is an anchor.</p>
<dt>Weeks</p>
<dd> <code>weeks</code>, <code>wks</code>, <code>ws</code>, <code>week</code>, <code>wk</code>, <code>w</code>, <code>weekly</code></p>
<dt>Days</p>
<dd> <code>days</code>, <code>dys</code>, <code>ds</code>, <code>day</code>, <code>dy</code>, <code>d</code>, <code>daily</code></p>
<dt>Hours</p>
<dd> <code>hours</code>, <code>hrs</code>, <code>hs</code>, <code>hour</code>, <code>hr</code>, <code>h</code>, <code>hourly</code></p>
<dt>Minutes</p>
<dd> <code>minutes</code>, <code>mins</code>, <code>minute</code>, <code>min</code>, but <i>not</i> <code>m</code>, <code>ms</code>, <code>mn</code> or <code>mns</code></p>
<dt>Seconds</p>
<dd> <code>seconds</code>, <code>secs</code>, <code>ss</code>, <code>second</code>, <code>sec</code>, <code>s</code></dl>
<p> Spaces between the numbers are optional, but are required between items, although a comma may be used (with or without spaces). </p>
<p> The forms <code>yearly</code> to <code>hourly</code> allow the number to be omitted; it is assumed to be 1. For example, <code>1 d</code> and <code>daily</code> are equivalent. Note that using those forms with plurals is confusing; <code>2 yearly</code> is the same as <code>2 years</code>, <i>not</i> twice yearly, so it is recommended they only be used without numbers. </p>
<p> When an anchor time is present, there is an extension to handle regular events in the form of the <i>n</i>th <i>some</i>day of the month. Such a specification must occur immediately after any year and month specification, but before any time of day, and must be in the form <i>n</i>(<code>th</code>|<code>st</code>|<code>rd</code>) <i>day</i>, for example <code>1st Tuesday</code> or <code>3rd Monday</code>. As in other places, days are matched case insensitively, must be in English, and only the first three letters are significant except that a form beginning `month&#8217; does not match `Monday&#8217;. No attempt is made to sanitize the resulting date; attempts to squeeze too many occurrences into a month will push the day into the next month (but in the obvious fashion, retaining the correct day of the week). </p>
<p> Here are some examples: </p>
<dl>
<dt>
<dd>
<pre>
<code>30 years 3 months 4 days 3:42:41
14 days 5 hours
Monthly, 3rd Thursday
4d,10hr</code>
</pre>
</dl>
<h3>Example</h3>
<p> Here is an example calendar file. It uses a consistent date format, as recommended above. </p>
<dl>
<dt>
<dd>
<pre>
<code>Feb 1, 2006 14:30 Pointless bureaucratic meeting
Mar 27, 2006 11:00 Mutual recrimination and finger pointing
  Bring water pistol and waterproofs
Mar 31, 2006 14:00 Very serious managerial pontification
  # UID 12C7878A9A50
Apr 10, 2006 13:30 Even more pointless blame assignment exercise WARN 30 mins
May 18, 2006 16:00 Regular moaning session RPT monthly, 3rd Thursday</code>
</pre>
</dl>
<p> The second entry has a continuation line. The third entry has a continuation line that will not be shown when the entry is displayed, but the unique identifier will be used by the <code>calendar_add</code> function when updating the event. The fourth entry will produce a warning 30 minutes before the event (to allow you to equip yourself appropriately). The fifth entry repeats after a month on the 3rd Thursday, i.e. June 15, 2006, at the same time. </p>
<h2>USER FUNCTIONS</h2>
<p> This section describes functions that are designed to be called directly by the user. The first part describes those functions associated with the user&#8217;s calendar; the second part describes the use in glob qualifiers. </p>
<h3>Calendar system functions</h3>
<dl>
<dt>
<dd> <code>calendar </code>[ <code>-abdDsv</code> ] [ <code>-C</code> <i>calfile</i> ] [ <code>-n</code> <i>num</i> ] [ <code>-S</code> <i>showprog</i> ]</p>
<dt>
<dd> [ [ <i>start</i> ] <i>end</i> ]</p>
<dt>
<dd> <code>calendar -r</code> [ <code>-abdDrsv</code> ] [ <code>-C</code> <i>calfile</i> ] [ <code>-n</code> <i>num</i> ] [ <code>-S</code> <i>showprog</i> ]</p>
<dt>
<dd> [ <i>start</i> ] Show events in the calendar.</p>
<dl>
<dt>
<dd>
<p> With no arguments, show events from the start of today until the end of the next working day after today. In other words, if today is Friday, Saturday, or Sunday, show up to the end of the following Monday, otherwise show today and tomorrow. </p>
<p> If <i>end</i> is given, show events from the start of today up to the time and date given, which is in the format described in the previous section. Note that if this is a date the time is assumed to be midnight at the start of the date, so that effectively this shows all events before the given date. </p>
<p> <i>end</i> may start with a <code>+</code>, in which case the remainder of the specification is a relative time format as described in the previous section indicating the range of time from the start time that is to be included. </p>
<p> If <i>start</i> is also given, show events starting from that time and date. The word <code>now</code> can be used to indicate the current time. </p>
<p> To implement an alert when events are due, include <code>calendar -s</code> in your <code>~/.zshrc</code> file. </p>
<p> Options: </p>
<dl>
<dt>
<dd> <code>-a</code> Show all items in the calendar, regardless of the <code>start</code> and <code>end</code>.</p>
<dt><code>-b</code></p>
<dd> Brief: don&#8217;t display continuation lines (i.e. indented lines following the line with the date/time), just the first line.</p>
<dt><code>-B</code> <i>lines</i></p>
<dd> Brief: display at most the first <i>lines</i> lines of the calendar entry. `<code>-B 1</code>&#8216; is equivalent to `<code>-b</code>&#8216;.</p>
<dt><code>-C</code> <i>calfile</i></p>
<dd> Explicitly specify a calendar file instead of the value of the <code>calendar-file</code> style or the default <code>~/calendar</code>.</p>
<dt><code>-d</code></p>
<dd> Move any events that have passed from the calendar file to the &quot;done&quot; file, as given by the <code>done-file</code> style or the default which is the calendar file with <code>.done</code> appended. This option is implied by the <code>-s</code> option.</p>
<dt><code>-D</code></p>
<dd> Turns off the option <code>-d</code>, even if the <code>-s</code> option is also present.</p>
<dt><code>-n</code> <i>num</i>, <code>&#8211;</code><i>num</i></p>
<dd> Show at least <i>num</i> events, if present in the calendar file, regardless of the <code>start</code> and <code>end</code>.</p>
<dt><code>-r</code></p>
<dd> Show all the remaining options in the calendar, ignoring the given <i>end</i> time. The <i>start</i> time is respected; any argument given is treated as a <i>start</i> time.</p>
<dt><code>-s</code></p>
<dd> Use the shell&#8217;s <code>sched</code> command to schedule a timed event that will warn the user when an event is due. Note that the <code>sched</code> command only runs if the shell is at an interactive prompt; a foreground task blocks the scheduled task from running until it is finished.</p>
<dl>
<dt>
<dd>
<p> The timed event usually runs the programme <code>calendar_show</code> to show the event, as described in the section UTILITY FUNCTIONS below. </p>
<p> By default, a warning of the event is shown five minutes before it is due. The warning period can be configured by the style <code>warn-time</code> or for a single calendar entry by including <code>WARN</code> <i>reltime</i> in the first line of the entry, where <i>reltime</i> is one of the usual relative time formats. </p>
<p> A repeated event may be indicated by including <code>RPT</code> <i>reldate</i> in the first line of the entry. After the scheduled event has been displayed it will be re-entered into the calendar file at a time <i>reldate</i> after the existing event. Note that this is currently the only use made of the repeat count, so that it is not possible to query the schedule for a recurrence of an event in the calendar until the previous event has passed. </p>
<p> If <code>RPT</code> is used, it is also possible to specify that certain recurrences of an event are rescheduled or cancelled. This is done with the <code>OCCURRENCE</code> keyword, followed by whitespace and the date and time of the occurrence in the regular sequence, followed by whitespace and either the date and time of the rescheduled event or the exact string <code>CANCELLED</code>. In this case the date and time must be in exactly the &quot;date with local time&quot; format used by the <code>text/calendar</code> MIME type (RFC 2445), <i>&lt;YYYY&gt;&lt;MM&gt;&lt;DD&gt;</i><code>T</code><i>&lt;hh&gt;&lt;mm&gt;&lt;ss&gt;</i> (note the presence of the literal character <code>T</code>). The first word (the regular recurrence) may be something other than a proper date/time to indicate that the event is additional to the normal sequence; a convention that retains the formatting appearance is <code>XXXXXXXXTXXXXXX</code>. </p>
<p> Furthermore, it is useful to record the next regular recurrence (as then the displayed date may be for a rescheduled event so cannot be used for calculating the regular sequence). This is specified by <code>RECURRENCE</code> and a time or date in the same format. <code>calendar_add</code> adds such an indication when it encounters a recurring event that does not include one, based on the headline date/time. </p>
<p> If <code>calendar_add</code> is used to update occurrences the <code>UID</code> keyword described there should be present in both the existing entry and the added occurrence in order to identify recurring event sequences. </p>
<p> For example, </p>
<dl>
<dt>
<dd>
<pre>
<code>Thu May 6, 2010 11:00 Informal chat RPT 1 week
  # RECURRENCE 20100506T110000
  # OCCURRENCE 20100513T110000 20100513T120000
  # OCCURRENCE 20100520T110000 CANCELLED</code>
</pre>
</dl>
<p> The event that occurs at 11:00 on 13th May 2010 is rescheduled an hour later. The event that occurs a week later is cancelled. The occurrences are given on a continuation line starting with a <code>#</code> character so will not usually be displayed as part of the event. As elsewhere, no account of time zones is taken with the times. After the next event occurs the headline date/time will be `<code>Thu May 13, 2010 12:00</code>&#8216; while the <code>RECURRENCE</code> date/time will be `<code>20100513T110000</code>&#8216; (note that cancelled and moved events are not taken account of in the <code>RECURRENCE</code>, which records what the next regular recurrence is, but they are accounted for in the headline date/time). </p>
<p> It is safe to run <code>calendar -s</code> to reschedule an existing event (if the calendar file has changed, for example), and also to have it running in multiples instances of the shell since the calendar file is locked when in use. </p>
<p> By default, expired events are moved to the &quot;done&quot; file; see the <code>-d</code> option. Use <code>-D</code> to prevent this.</dl>
<dt><code>-S</code> <i>showprog</i></p>
<dd> Explicitly specify a programme to be used for showing events instead of the value of the <code>show-prog</code> style or the default <code>calendar_show</code>.</p>
<dt><code>-v</code></p>
<dd> Verbose: show more information about stages of processing. This is useful for confirming that the function has successfully parsed the dates in the calendar file.</dl>
</dl>
<dt><code>calendar_add</code> [ <code>-BL</code> ] <i>event</i> &#8230;</p>
<dd> Adds a single event to the calendar in the appropriate location. The event can contain multiple lines, as described in the section Calendar File Format above. Using this function ensures that the calendar file is sorted in date and time order. It also makes special arrangements for locking the file while it is altered. The old calendar is left in a file with the suffix <code>.old</code>.</p>
<dl>
<dt>
<dd>
<p> The option <code>-B</code> indicates that backing up the calendar file will be handled by the caller and should not be performed by <code>calendar_add</code>. The option <code>-L</code> indicates that <code>calendar_add</code> does not need to lock the calendar file as it is already locked. These options will not usually be needed by users. </p>
<p> If the style <code>reformat-date</code> is true, the date and time of the new entry will be rewritten into the standard date format: see the descriptions of this style and the style <code>date-format</code>. </p>
<p> The function can use a unique identifier stored with each event to ensure that updates to existing events are treated correctly. The entry should contain the word <code>UID</code>, followed by whitespace, followed by a word consisting entirely of hexadecimal digits of arbitrary length (all digits are significant, including leading zeroes). As the UID is not directly useful to the user, it is convenient to hide it on an indented continuation line starting with a <code>#</code>, for example: </p>
<dl>
<dt>
<dd>
<pre>
<code>Aug 31, 2007 09:30  Celebrate the end of the holidays
  # UID 045B78A0</code>
</pre>
</dl>
<p> The second line will not be shown by the <code>calendar</code> function. </p>
<p> It is possible to specify the <code>RPT</code> keyword followed by <code>CANCELLED</code> instead of a relative time. This causes any matched event or series of events to be cancelled (the original event does not have to be marked as recurring in order to be cancelled by this method). A <code>UID</code> is required in order to match an existing event in the calendar. </p>
<p> <code>calendar_add</code> will attempt to manage recurrences and occurrences of repeating events as described for event scheduling by <code>calendar -s</code> above. To reschedule or cancel a single event <code>calendar_add</code> should be called with an entry that includes the correct <code>UID</code> but does <i>not</i> include the <code>RPT</code> keyword as this is taken to mean the entry applies to a series of repeating events and hence replaces all existing information. Each rescheduled or cancelled occurrence must have an <code>OCCURRENCE</code> keyword in the entry passed to <code>calendar_add</code> which will be merged into the calendar file. Any existing reference to the occurrence is replaced. An occurrence that does not refer to a valid existing event is added as a one-off occurrence to the same calendar entry.</dl>
<dt><code>calendar_edit</code></p>
<dd> This calls the user&#8217;s editor to edit the calendar file. If there are arguments, they are taken as the editor to use (the file name is appended to the commands); otherwise, the editor is given by the variable <code>VISUAL</code>, if set, else the variable <code>EDITOR</code>.</p>
<dl>
<dt>
<dd>
<p> If the calendar scheduler was running, then after editing the file <code>calendar -s</code> is called to update it. </p>
<p> This function locks out the calendar system during the edit. Hence it should be used to edit the calendar file if there is any possibility of a calendar event occurring meanwhile. Note this can lead to another shell with calendar functions enabled hanging waiting for a lock, so it is necessary to quit the editor as soon as possible.</dl>
<dt><code>calendar_parse</code> <i>calendar-entry</i></p>
<dd> This is the internal function that analyses the parts of a calendar entry, which is passed as the only argument. The function returns status 1 if the argument could not be parsed as a calendar entry and status 2 if the wrong number of arguments were passed; it also sets the parameter <code>reply</code> to an empty associative array. Otherwise, it returns status 0 and sets elements of the associative array <code>reply</code> as follows:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>time</code></p>
<dd> The time as a string of digits in the same units as <code>$EPOCHSECONDS</code></p>
<dt><code>schedtime</code></p>
<dd> The regularly scheduled time. This may differ from the actual event time <code>time</code> if this is a recurring event and the next occurrence has been rescheduled. Then <code>time</code> gives the actual time and <code>schedtime</code> the time of the regular recurrence before modification.</p>
<dt><code>text1</code></p>
<dd> The text from the line not including the date and time of the event, but including any <code>WARN</code> or <code>RPT</code> keywords and values.</p>
<dt><code>warntime</code></p>
<dd> Any warning time given by the <code>WARN</code> keyword as a string of digits containing the time at which to warn in the same units as <code>$EPOCHSECONDS</code>. (Note this is an absolute time, not the relative time passed down.) Not set no <code>WARN</code> keyword and value were matched.</p>
<dt><code>warnstr</code></p>
<dd> The raw string matched after the <code>WARN</code> keyword, else unset.</p>
<dt><code>rpttime</code></p>
<dd> Any recurrence time given by the <code>RPT</code> keyword as a string of digits containing the time of the recurrence in the same units as <code>$EPOCHSECONDS</code>. (Note this is an absolute time.) Not set if no <code>RPT</code> keyword and value were matched.</p>
<dt><code>schedrpttime</code></p>
<dd> The next regularly scheduled occurrence of a recurring event before modification. This may differ from <code>rpttime</code>, which is the actual time of the event that may have been rescheduled from the regular time.</p>
<dt><code>rptstr</code></p>
<dd> The raw string matched after the <code>RPT</code> keyword, else unset.</p>
<dt><code>text2</code></p>
<dd> The text from the line after removal of the date and any keywords and values.</dl>
</dl>
</dl>
<dl>
<dt><code>calendar_showdate</code> [ <code>-r</code> ] [ <code>-f</code> <i>fmt</i> ] <i>date-spec</i> &#8230;</p>
<dd> The given <i>date-spec</i> is interpreted and the corresponding date and time printed. If the initial <i>date-spec</i> begins with a <code>+</code> or <code>&#8211;</code> it is treated as relative to the current time; <i>date-spec</i>s after the first are treated as relative to the date calculated so far and a leading <code>+</code> is optional in that case. This allows one to use the system as a date calculator. For example, <code>calendar_showdate &#8216;+1 month, 1st Friday&#8217;</code> shows the date of the first Friday of next month.</p>
<dl>
<dt>
<dd>
<p> With the option <code>-r</code> nothing is printed but the value of the date and time in seconds since the epoch is stored in the parameter <code>REPLY</code>. </p>
<p> With the option <code>-f</code> <i>fmt</i> the given date/time conversion format is passed to <code>strftime</code>; see notes on the <code>date-format</code> style below. </p>
<p> In order to avoid ambiguity with negative relative date specifications, options must occur in separate words; in other words, <code>-r</code> and <code>-f</code> should not be combined in the same word.</dl>
<dt><code>calendar_sort</code></p>
<dd> Sorts the calendar file into date and time order. The old calendar is left in a file with the suffix <code>.old</code>.</dl>
<h3>Glob qualifiers</h3>
<dl>
<dt>
<dd> <code>age</code> The function <code>age</code> can be autoloaded and use separately from the calendar system, although it uses the function <code>calendar_scandate</code> for date formatting. It requires the <code>zsh/stat</code> builtin, but uses only the builtin <code>zstat</code>.</p>
<dl>
<dt>
<dd>
<p> <code>age</code> selects files having a given modification time for use as a glob qualifier. The format of the date is the same as that understood by the calendar system, described in the section FILE AND DATE FORMATS above. </p>
<p> The function can take one or two arguments, which can be supplied either directly as command or arguments, or separately as shell parameters. </p>
<dl>
<dt>
<dd>
<pre>
<code>print *(e:age 2006/10/04 2006/10/09:)</code>
</pre>
</dl>
<p> The example above matches all files modified between the start of those dates. The second argument may alternatively be a relative time introduced by a <code>+</code>: </p>
<dl>
<dt>
<dd>
<pre>
<code>print *(e:age 2006/10/04 +5d:)</code>
</pre>
</dl>
<p> The example above is equivalent to the previous example. </p>
<p> In addition to the special use of days of the week, <code>today</code> and <code>yesterday</code>, times with no date may be specified; these apply to today. Obviously such uses become problematic around midnight. </p>
<dl>
<dt>
<dd>
<pre>
<code>print *(e-age 12:00 13:30-)</code>
</pre>
</dl>
<p> The example above shows files modified between 12:00 and 13:00 today. </p>
<dl>
<dt>
<dd>
<pre>
<code>print *(e:age 2006/10/04:)</code>
</pre>
</dl>
<p> The example above matches all files modified on that date. If the second argument is omitted it is taken to be exactly 24 hours after the first argument (even if the first argument contains a time). </p>
<dl>
<dt>
<dd>
<pre>
<code>print *(e-age 2006/10/04:10:15 2006/10/04:10:45-)</code>
</pre>
</dl>
<p> The example above supplies times. Note that whitespace within the time and date specification must be quoted to ensure <code>age</code> receives the correct arguments, hence the use of the additional colon to separate the date and time. </p>
<dl>
<dt>
<dd>
<pre>
<code>AGEREF=2006/10/04:10:15
AGEREF2=2006/10/04:10:45
print *(+age)</code>
</pre>
</dl>
<p> This shows the same example before using another form of argument passing. The dates and times in the parameters <code>AGEREF</code> and <code>AGEREF2</code> stay in effect until unset, but will be overridden if any argument is passed as an explicit argument to age. Any explicit argument causes both parameters to be ignored. </p>
<p> Instead of an explicit date and time, it&#8217;s possible to use the modification time of a file as the date and time for either argument by introducing the file name with a colon: </p>
<dl>
<dt>
<dd>
<pre>
<code>print *(e-age :file1-)</code>
</pre>
</dl>
<p> matches all files created on the same day (24 hours starting from midnight) as <code>file1</code>. </p>
<dl>
<dt>
<dd>
<pre>
<code>print *(e-age :file1 :file2-)</code>
</pre>
</dl>
<p> matches all files modified no earlier than <code>file1</code> and no later than <code>file2</code>; precision here is to the nearest second.</dl>
<dt>
<dd> <code>after</code></p>
<dt>
<dd> <code>before</code> The functions <code>after</code> and <code>before</code> are simpler versions of <code>age</code> that take just one argument. The argument is parsed similarly to an argument of <code>age</code>; if it is not given the variable <code>AGEREF</code> is consulted. As the names of the functions suggest, a file matches if its modification time is after or before the time and date specified. If a time only is given the date is today.</p>
<dl>
<dt>
<dd>
<p> The two following examples are therefore equivalent:</p>
<dl>
<dt>
<dd>
<pre>
<code>print *(e-after 12:00-)
print *(e-after today:12:00-)</code>
</pre>
</dl>
</dl>
</dl>
<h2>STYLES</h2>
<p> The zsh style mechanism using the <code>zstyle</code> command is describe in <i><a href="/docs/linux/man/1-zshmodules/">zshmodules</a></i>(1). This is the same mechanism used in the completion system. </p>
<p> The styles below are all examined in the context <code>:datetime:</code><i>function</i><code>:</code>, for example <code>:datetime:calendar:</code>. </p>
<dl>
<dt>
<dd> <code>calendar-file</code> The location of the main calendar. The default is <code>~/calendar</code>.</p>
<dt><code>date-format</code></p>
<dd> A <code>strftime</code> format string (see <i><a href="/docs/linux/man/3-strftime/">strftime</a></i>(3)) with the zsh extensions providing various numbers with no leading zero or space if the number is a single digit as described for the <code>%D{</code><i>string</i><code>}</code> prompt format in the section EXPANSION OF PROMPT SEQUENCES in <i><a href="/docs/linux/man/1-zshmisc/">zshmisc</a></i>(1).</p>
<dl>
<dt>
<dd>
<p> This is used for outputting dates in <code>calendar</code>, both to support the <code>-v</code> option and when adding recurring events back to the calendar file, and in <code>calendar_showdate</code> as the final output format. </p>
<p> If the style is not set, the default used is similar the standard system format as output by the <code>date</code> command (also known as `ctime format&#8217;): `<code>%a %b %d %H:%M:%S %Z %Y</code>&#8216;.</dl>
<dt><code>done-file</code></p>
<dd> The location of the file to which events which have passed are appended. The default is the calendar file location with the suffix <code>.done</code>. The style may be set to an empty string in which case a &quot;done&quot; file will not be maintained.</p>
<dt><code>reformat-date</code></p>
<dd> Boolean, used by <code>calendar_add</code>. If it is true, the date and time of new entries added to the calendar will be reformatted to the format given by the style <code>date-format</code> or its default. Only the date and time of the event itself is reformatted; any subsidiary dates and times such as those associated with repeat and warning times are left alone.</p>
<dt><code>show-prog</code></p>
<dd> The programme run by <code>calendar</code> for showing events. It will be passed the start time and stop time of the events requested in seconds since the epoch followed by the event text. Note that <code>calendar -s</code> uses a start time and stop time equal to one another to indicate alerts for specific events.</p>
<dl>
<dt>
<dd>
<p> The default is the function <code>calendar_show</code>.</dl>
<dt><code>warn-time</code></p>
<dd> The time before an event at which a warning will be displayed, if the first line of the event does not include the text <code>EVENT</code> <i>reltime</i>. The default is 5 minutes.</dl>
<h2>UTILITY FUNCTIONS</h2>
<dl>
<dt>
<dd> <code>calendar_lockfiles</code> Attempt to lock the files given in the argument. To prevent problems with network file locking this is done in an ad hoc fashion by attempting to create a symbolic link to the file with the name <i>file</i><code>.lockfile</code>. No other system level functions are used for locking, i.e. the file can be accessed and modified by any utility that does not use this mechanism. In particular, the user is not prevented from editing the calendar file at the same time unless <code>calendar_edit</code> is used.</p>
<dl>
<dt>
<dd>
<p> Three attempts are made to lock the file before giving up. If the module <code>zsh/zselect</code> is available, the times of the attempts are jittered so that multiple instances of the calling function are unlikely to retry at the same time. </p>
<p> The files locked are appended to the array <code>lockfiles</code>, which should be local to the caller. </p>
<p> If all files were successfully locked, status zero is returned, else status one. </p>
<p> This function may be used as a general file locking function, although this will only work if only this mechanism is used to lock files.</dl>
<dt><code>calendar_read</code></p>
<dd> This is a backend used by various other functions to parse the calendar file, which is passed as the only argument. The array <code>calendar_entries</code> is set to the list of events in the file; no pruning is done except that ampersands are removed from the start of the line. Each entry may contain multiple lines.</p>
<dt><code>calendar_scandate</code></p>
<dd> This is a generic function to parse dates and times that may be used separately from the calendar system. The argument is a date or time specification as described in the section FILE AND DATE FORMATS above. The parameter <code>REPLY</code> is set to the number of seconds since the epoch corresponding to that date or time. By default, the date and time may occur anywhere within the given argument.</p>
<dl>
<dt>
<dd>
<p> Returns status zero if the date and time were successfully parsed, else one. </p>
<p> Options:</p>
<dl>
<dt>
<dd> <code>-a</code> The date and time are anchored to the start of the argument; they will not be matched if there is preceding text.</p>
<dt><code>-A</code></p>
<dd> The date and time are anchored to both the start and end of the argument; they will not be matched if the is any other text in the argument.</p>
<dt><code>-d</code></p>
<dd> Enable additional debugging output.</p>
<dt><code>-m</code></p>
<dd> Minus. When <code>-R</code> <i>anchor_time</i> is also given the relative time is calculated backwards from <i>anchor_time</i>.</p>
<dt><code>-r</code></p>
<dd> The argument passed is to be parsed as a relative time.</p>
<dt><code>-R</code> <i>anchor_time</i></p>
<dd> The argument passed is to be parsed as a relative time. The time is relative to <i>anchor_time</i>, a time in seconds since the epoch, and the returned value is the absolute time corresponding to advancing <i>anchor_time</i> by the relative time given. This allows lengths of months to be correctly taken into account. If the final day does not exist in the given month, the last day of the final month is given. For example, if the anchor time is during 31st January 2007 and the relative time is 1 month, the final time is the same time of day during 28th February 2007.</p>
<dt><code>-s</code></p>
<dd> In addition to setting <code>REPLY</code>, set <code>REPLY2</code> to the remainder of the argument after the date and time have been stripped. This is empty if the option <code>-A</code> was given.</p>
<dt><code>-t</code></p>
<dd> Allow a time with no date specification. The date is assumed to be today. The behaviour is unspecified if the iron tongue of midnight is tolling twelve.</dl>
</dl>
<dt><code>calendar_show</code></p>
<dd> The function used by default to display events. It accepts a start time and end time for events, both in epoch seconds, and an event description.</p>
<dl>
<dt>
<dd>
<p> The event is always printed to standard output. If the command line editor is active (which will usually be the case) the command line will be redisplayed after the output. </p>
<p> If the parameter <code>DISPLAY</code> is set and the start and end times are the same (indicating a scheduled event), the function uses the command <code>xmessage</code> to display a window with the event details.</dl>
</dl>
<h2>BUGS</h2>
<p> As the system is based entirely on shell functions (with a little support from the <code>zsh/datetime</code> module) the mechanisms used are not as robust as those provided by a dedicated calendar utility. Consequently the user should not rely on the shell for vital alerts. </p>
<p> There is no <code>calendar_delete</code> function. </p>
<p> There is no localization support for dates and times, nor any support for the use of time zones. </p>
<p> Relative periods of months and years do not take into account the variable number of days. </p>
<p> The <code>calendar_show</code> function is currently hardwired to use <code>xmessage</code> for displaying alerts on X Window System displays. This should be configurable and ideally integrate better with the desktop. </p>
<p> <code>calendar_lockfiles</code> hangs the shell while waiting for a lock on a file. If called from a scheduled task, it should instead reschedule the event that caused it. </p>
<h2>Index</h2>
