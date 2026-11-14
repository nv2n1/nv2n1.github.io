---
title: "calendar(1)"
name: "calendar"
section: "1"
letter: "c"
url: "/docs/linux/man/1-calendar/"
description: "calendar – reminder service"
---

<h2 class="name">NAME</h2>
<p> <code>calendar</code> &#8211; reminder service </p>
<h2>SYNOPSIS</h2>
<p> <code>calendar</code> [-<code>abw</code> ] [-<code>A </code><i>num</i> ] [-<code>B </code><i>num</i> ] [-<code>l </code><i>num</i> ] [-<code>e </code><i>num</i> ] [-<code>f </code><i>calendarfile</i> ] [-<code>t </code>[[[<i>cc </i><i>yy </i><i>mm </i><i>dd</i> ] ] ] ]</p>
<h2>DESCRIPTION</h2>
<p> The <code>calendar</code> utility checks the current directory or the directory specified by the <code>CALENDAR_DIR</code> environment variable for a file named calendar and displays lines that begin with either today&#8217;s date or tomorrow&#8217;s. On Fridays, events on Friday through Monday are displayed. </p>
<p> The options are as follows:</p>
<dl>
<dt><code>-A </code><i>num</i></p>
<dd> Print lines from today and next <i>num</i> days (forward, future). Defaults to one. (same as -l)</p>
<dt><code>-a</code></p>
<dd> Process the &#8220;calendar&#8221; files of all users and mail the results to them. This requires superuser privileges.</p>
<dt><code>-B </code><i>num</i></p>
<dd> Print lines from today and previous <i>num</i> days (backward, past).</p>
<dt><code>-b</code></p>
<dd> Enforce special date calculation mode for Cyrillic calendars.</p>
<dt><code>-l </code><i>num</i></p>
<dd> Print lines from today and next <i>num</i> days (forward, future). Defaults to one. (same as -A)</p>
<dt><code>-e </code><i>num</i></p>
<dd> Print lines from today and next <i>num</i> days, only if today is Friday (forward, future). Defaults to two, which causes <code>calendar</code> to print entries through the weekend on Fridays.</p>
<dt><code>-f </code><i>calendarfile</i></p>
<dd> Use <i>calendarfile</i> as the default calendar file. If this file is not accessible, the system-wide default is used.</p>
<dt><code>-t </code>[[[<i>cc </i><i>yy </i><i>mm </i><i>dd</i> ] ] ]</p>
<dd> Act like the specified value is &#8220;today&#8221; instead of using the current date. If yy is specified, but cc is not, a value for yy between 69 and 99 results in a cc value of 19. Otherwise, a cc value of 20 is used.</p>
<dt><code>-w</code></p>
<dd> Print day of the week name in front of each event.</dl>
<p> To handle calendars in your national code table you can specify &#8220;LANG=&lt;locale_name&gt;&#8221; in the calendar file as early as possible. To handle national Easter names in the calendars, &#8220;Easter=&lt;national_name&gt;&#8221; (for Catholic Easter) or &#8220;Paskha=&lt;national_name&gt;&#8221; (for Orthodox Easter) can be used. </p>
<p> A special locale name exists: `utf-8&#8242; Specifying &#8220;LANG=utf-8&#8221; indicates that the dates will be read using the C locale, and the descriptions will be encoded in UTF-8. This is usually used for the distributed calendar files. The &#8220;CALENDAR&#8221; variable can be used to specify the style. Only `Julian&#8217; and `Gregorian&#8217; styles are currently supported. Use &#8220;CALENDAR=&#8221; to return to the default (Gregorian). </p>
<p> To enforce special date calculation mode for Cyrillic calendars you should specify &#8220;LANG=&lt;local_name&gt;&#8221; and &#8220;BODUN=&lt;bodun_prefix&gt;&#8221; where &lt;local_name&gt; can be ru_RU.UTF-8, uk_UA.UTF-8 or by_BY.UTF-8. </p>
<p> Note that the locale is reset to the user&#8217;s default for each new file that is read. This is so that locales from one file do not accidentally carry over into another file. </p>
<p> Other lines should begin with a month and day. They may be entered in almost any format, either numeric or as character strings. If proper locale is set, national months and weekdays names can be used. A single asterisk (`*&#8217;) matches every month. A day without a month matches that day of every week. A month without a day matches the first of that month. Two numbers default to the month followed by the day. Lines with leading tabs default to the last entered date, allowing multiple line specifications for a single date. &#8220;Easter&#8221; (may be followed by a positive or negative integer) is Easter for this year. &#8220;Paskha&#8221; (may be followed by a positive or negative integer) is Orthodox Easter for this year. Weekdays may be followed by &#8220;-4&#8221; <code>&#8230;</code> &#8220;+5&#8221; (aliases last, first, second, third, fourth) for moving events like &#8220;the last Monday in April&#8221; </p>
<p> By convention, dates followed by an asterisk (`*&#8217; ) are not fixed, i.e., change from year to year. </p>
<p> Day descriptions start after the first &lt;tab&gt; character in the line; if the line does not contain a &lt;tab&gt; character, it isn&#8217;t printed out. If the first character in the line is a &lt;tab&gt; character, it is treated as the continuation of the previous description. </p>
<p> The calendar file is preprocessed by <a href="/docs/linux/man/1-cpp/">cpp</a>(1), allowing the inclusion of shared files such as company holidays or meetings. If the shared file is not referenced by a full pathname, <a href="/docs/linux/man/1-cpp/">cpp</a>(1) searches in the current (or home) directory first, and then in the directory /etc/calendar and finally in /usr/share/calendar Empty lines and lines protected by the C commenting syntax (<code>/* &#8230; */</code> ) are ignored. </p>
<p> Some possible calendar entries (a <code>	</code> sequence denotes a &lt;tab&gt; character): </p>
<blockquote>
<pre><code>
LANG = C
    Easter = Ostern
#include &lt;calendar.birthday&gt;
#include &lt;calendar.usholiday&gt;
                 6 /
                 15	June 15(if ambiguous, will default to month / day).Jun.15	June 15. 15 June	June 15. Thursday	Every Thursday.June	Every June 1st. 15 *	15th of every month.May Sun +
             2	second Sunday in May(Muttertag) 04 / SunLast	last Sunday in April,
	summer time in Europe
         Easter	Easter
             Ostern -
     2	Good Friday(2 days before Easter)
         Paskha	Orthodox Easter
</code></pre>
</blockquote>
<h2>FILES</h2>
<dl>
<dt><code>calendar </code></p>
<dd> File in current directory.</p>
<dt><code>~/.calendar </code></p>
<dd> Directory in the user&#8217;s home directory (which <code>calendar</code> changes into, if it exists).</p>
<dt><code>~/.calendar/calendar </code></p>
<dd> File to use if no calendar file exists in the current directory.</p>
<dt><code>~/.calendar/nomail </code></p>
<dd> <code>calendar</code> will not send mail if this file exists.</p>
<dt><code>calendar.all </code></p>
<dd> International and national calendar files.</p>
<dt><code>calendar.birthday </code></p>
<dd> Births and deaths of famous (and not-so-famous) people.</p>
<dt><code>calendar.canada </code></p>
<dd> Canadian holidays.</p>
<dt><code>calendar.christian </code></p>
<dd> Christian holidays (should be updated yearly by the local system administrator so that roving holidays are set correctly for the current year).</p>
<dt><code>calendar.computer </code></p>
<dd> Days of special significance to computer people.</p>
<dt><code>calendar.croatian </code></p>
<dd> Croatian calendar.</p>
<dt><code>calendar.discord </code></p>
<dd> Discordian calendar (all rites reversed).</p>
<dt><code>calendar.fictional </code></p>
<dd> Fantasy and fiction dates (mostly LOTR).</p>
<dt><code>calendar.french </code></p>
<dd> French calendar.</p>
<dt><code>calendar.german </code></p>
<dd> German calendar.</p>
<dt><code>calendar.history </code></p>
<dd> Miscellaneous history.</p>
<dt><code>calendar.holiday </code></p>
<dd> Other holidays (including the not-well-known, obscure, and <i>really</i> obscure).</p>
<dt><code>calendar.judaic </code></p>
<dd> Jewish holidays (should be updated yearly by the local system administrator so that roving holidays are set correctly for the current year).</p>
<dt><code>calendar.music </code></p>
<dd> Musical events, births, and deaths (strongly oriented toward rock n&#8217; roll).</p>
<dt><code>calendar.nz </code></p>
<dd> New Zealand calendar.</p>
<dt><code>calendar.openbsd </code></p>
<dd> Ox related events.</p>
<dt><code>calendar.pagan </code></p>
<dd> Pagan holidays, celebrations and festivals.</p>
<dt><code>calendar.russian </code></p>
<dd> Russian calendar.</p>
<dt><code>calendar.space </code></p>
<dd> Cosmic history.</p>
<dt><code>calendar.uk </code></p>
<dd> UK calendar.</p>
<dt><code>calendar.ushistory </code></p>
<dd> U.S. history.</p>
<dt><code>calendar.usholiday </code></p>
<dd> U.S. holidays.</p>
<dt><code>calendar.world </code></p>
<dd> World wide calendar.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-at/">at</a>(1), <a href="/docs/linux/man/1-cal/">cal</a>(1), <a href="/docs/linux/man/1-cpp/">cpp</a>(1), <a href="/docs/linux/man/1-mail/">mail</a>(1), <a href="/docs/linux/man/8-cron/">cron</a>(8)</p>
<h2>STANDARDS</h2>
<p> The <code>calendar</code> program previously selected lines which had the correct date anywhere in the line. This is no longer true: the date is only recognized when it occurs at the beginning of a line.</p>
<h2>COMPATIBILITY</h2>
<p> The <code>calendar</code> command will only display lines that use a &lt;tab&gt; character to separate the date and description, or that begin with a &lt;tab&gt;. This is different than in previous releases. </p>
<p> The Fl t flag argument syntax is from the original FreeBSD <code>calendar</code> program. </p>
<p> The &#8211;<code>l</code> and &#8211;<code>e</code> flags are Debian-specific enhancements. Option &#8211;<code>e</code> used to be called in Debian, but this option is now used differently by upstream. Also, the original <code>calendar</code> program did not accept <code>0</code> as an argument to the &#8211;<code>A</code> flag. </p>
<p> Using `utf-8&#8242; as a locale name is a Debian-specific enhancement.</p>
<h2>HISTORY</h2>
<p> A <code>calendar</code> command appeared in AT&amp;T System v7 .</p>
<h2>BUGS</h2>
<p> <code>calendar</code> doesn&#8217;t handle all Jewish holidays or moon phases. </p>
<h2>Index</h2>
