---
title: "cal(1)"
name: "cal"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cal/"
description: "cal ncal – displays a calendar and the date of Easter"
---

<h2 class="name">NAME</h2>
<p> <code>cal</code> <code>ncal</code> &#8211; displays a calendar and the date of Easter </p>
<h2>SYNOPSIS</h2>
<p> [-<code>31jy</code> ] [-<code>A </code><i>number</i> ] [-<code>B </code><i>number</i> ] [-<code>d </code><i>yyyy-mm</i> ] [[<i>month</i> ] <i>year</i> ]<br />
 [-<code>31j</code> ] [-<code>A </code><i>number</i> ] [-<code>B </code><i>number</i> ] [-<code>d </code><i>yyyy-mm</i> ] &#8211;<code>m </code><i>month</i> [<i>year</i> ]<br />
<code>ncal</code> [-<code>C</code> ] [-<code>31jy</code> ] [-<code>A </code><i>number</i> ] [-<code>B </code><i>number</i> ] [-<code>d </code><i>yyyy-mm</i> ] [[<i>month</i> ] <i>year</i> ]<br />
<code>ncal</code> [-<code>C</code> ] [-<code>31j</code> ] [-<code>A </code><i>number</i> ] [-<code>B </code><i>number</i> ] [-<code>d </code><i>yyyy-mm</i> ] &#8211;<code>m </code><i>month</i> [<i>year</i> ]<br />
<code>ncal</code> [-<code>31bhjJpwySM</code> ] [-<code>A </code><i>number</i> ] [-<code>B </code><i>number</i> ] [-<code>H </code><i>yyyy-mm-dd</i> ] [-<code>d </code><i>yyyy-mm</i> ] [-<code>s </code><i>country_code</i> ] [[<i>month</i> ] <i>year</i> ]<br />
<code>ncal</code> [-<code>31bhJeoSM</code> ] [-<code>A </code><i>number</i> ] [-<code>B </code><i>number</i> ] [-<code>d </code><i>yyyy-mm</i> ] [<i>year</i> ]</p>
<h2>DESCRIPTION</h2>
<p> The utility displays a simple calendar in traditional format and <code>ncal</code> offers an alternative layout, more options and the date of Easter. The new format is a little cramped but it makes a year fit on a 25&#215;80 terminal. If arguments are not specified, the current month is displayed. </p>
<p> The options are as follows:</p>
<dl>
<dt><code>-h</code></p>
<dd> Turns off highlighting of today.</p>
<dt><code>-J</code></p>
<dd> Display Julian Calendar, if combined with the &#8211;<code>o</code> option, display date of Orthodox Easter according to the Julian Calendar.</p>
<dt><code>-e</code></p>
<dd> Display date of Easter (for western churches).</p>
<dt><code>-j</code></p>
<dd> Display Julian days (days one-based, numbered from January 1).</p>
<dt><code>-m </code><i>month</i></p>
<dd> Display the specified <i>month</i> If <i>month</i> is specified as a decimal number, appending `f&#8217; or `p&#8217; displays the same month of the following or previous year respectively.</p>
<dt><code>-o</code></p>
<dd> Display date of Orthodox Easter (Greek and Russian Orthodox Churches).</p>
<dt><code>-p</code></p>
<dd> Print the country codes and switching days from Julian to Gregorian Calendar as they are assumed by <code>ncal</code> The country code as determined from the local environment is marked with an asterisk.</p>
<dt><code>-s </code><i>country_code</i></p>
<dd> Assume the switch from Julian to Gregorian Calendar at the date associated with the <i>country_code</i> If not specified, <code>ncal</code> tries to guess the switch date from the local environment or falls back to September 2, 1752. This was when Great Britain and her colonies switched to the Gregorian Calendar.</p>
<dt><code>-w</code></p>
<dd> Print the number of the week below each week column.</p>
<dt><code>-y</code></p>
<dd> Display a calendar for the specified year. This option is implied when a year but no month are specified on the command line.</p>
<dt><code>-3</code></p>
<dd> Display the previous, current and next month surrounding today.</p>
<dt><code>-1</code></p>
<dd> Display only the current month. This is the default.</p>
<dt><code>-A </code><i>number</i></p>
<dd> Months to add after. The specified number of months is added to the end of the display. This is in addition to any date range selected by the &#8211;<code>y</code> &#8211;<code>3</code> or &#8211;<code>1</code> options. For example, &#8220;<code>cal -y -B2 -A2</code> &#8221; shows everything from November of the previous year to February of the following year. Negative numbers are allowed, in which case the specified number of months is subtracted. For example, &#8220;<code>cal -y -B-6 </code> &#8221; shows July to December. And &#8220;<code>cal -A11</code> &#8221; simply shows the next 12 months.</p>
<dt><code>-B </code><i>number</i></p>
<dd> Months to add before. The specified number of months is added to the beginning of the display. See &#8211;<code>A</code> for examples.</p>
<dt><code>-C</code></p>
<dd> Completely switch to <code>cal</code> mode. For <code>cal</code> like output only, use &#8211;<code>b</code> instead.</p>
<dt><code>-N</code></p>
<dd> Switch to <code>ncal</code> mode.</p>
<dt><code>-d </code><i>yyyy-mm</i></p>
<dd> Use <i>yyyy-mm</i> as the current date (for debugging of date selection).</p>
<dt><code>-H </code><i>yyyy-mm-dd</i></p>
<dd> Use <i>yyyy-mm-dd</i> as the current date (for debugging of highlighting).</p>
<dt><code>-M</code></p>
<dd> Weeks start on Monday.</p>
<dt><code>-S</code></p>
<dd> Weeks start on Sunday.</p>
<dt><code>-b</code></p>
<dd> Use oldstyle format for ncal output.</dl>
<p> A single parameter specifies the year (1-9999) to be displayed; note the year must be fully specified: &#8220;<code>cal 89</code> &#8221; will <i>not</i> display a calendar for 1989. Two parameters denote the month and year; the month is either a number between 1 and 12, or a full or abbreviated name as specified by the current locale. Month and year default to those of the current system clock and time zone (so &#8220;<code>cal -m 8</code> &#8221; will display a calendar for the month of August in the current year). </p>
<p> Not all options can be used together. For example, the options &#8211;<code>y , 3 , </code> and &#8211;<code>1 </code> are mutually exclusive. If inconsistent options are given, the later ones take precedence over the earlier ones. </p>
<p> A year starts on January 1. </p>
<p> Highlighting of dates is disabled if stdout is not a tty.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-calendar/">calendar</a>(3), <a href="/docs/linux/man/3-strftime/">strftime</a>(3)</p>
<h2>HISTORY</h2>
<p> A command appeared in AT&amp;T System v5 . The <code>ncal</code> command appeared in Fx 2.2.6 . The output of the <code>cal</code> command is supposed to be bit for bit compatible to the original Unix <code>cal</code> command, because its output is processed by other programs like CGI scripts, that should not be broken. Therefore it will always output 8 lines, even if only 7 contain data. This extra blank line also appears with the original <code>cal</code> command, at least on Solaris 8</p>
<h2>AUTHORS</h2>
<p> The <code>ncal</code> command and manual were written by An Wolfgang Helbig Aq Mt helbig [at] FreeBSD.org .</p>
<h2>BUGS</h2>
<p> The assignment of Julian-Gregorian switching dates to country codes is historically naive for many countries. </p>
<p> Not all options are compatible and using them in different orders will give varying results. </p>
<h2>Index</h2>
