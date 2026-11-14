---
title: "ddate(1)"
name: "ddate"
section: "1"
letter: "d"
url: "/docs/linux/man/1-ddate/"
description: "ddate – convert Gregorian dates to Discordian dates"
---

<h2 class="name">NAME</h2>
<p> ddate &#8211; convert Gregorian dates to Discordian dates </p>
<h2>SYNOPSIS</h2>
<p> <code>ddate</code> [<i></i><code>+</code>format] [<i>date</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>ddate</code> prints the date in Discordian date format. </p>
<p> If called with no arguments, <code>ddate</code> will get the current system date, convert this to the Discordian date format and print this on the standard output. Alternatively, a Gregorian date may be specified on the command line, in the form of a numerical day, month and year. </p>
<p> If a format string is specified, the Discordian date will be printed in a format specified by the string. This mechanism works similarly to the format string mechanism of <code><a href="/docs/linux/man/1-date/">date</a>(1),</code> only almost completely differently. The fields are:</p>
<dl>
<dt>%A</p>
<dd> Full name of the day of the week (i.e., Sweetmorn)</p>
<dt>%a</p>
<dd> Abbreviated name of the day of the week (i.e., SM)</p>
<dt>%B</p>
<dd> Full name of the season (i.e., Chaos)</p>
<dt>%b</p>
<dd> Abbreviated name of the season (i.e., Chs)</p>
<dt>%d</p>
<dd> Ordinal number of day in season (i.e., 23)</p>
<dt>%e</p>
<dd> Cardinal number of day in season (i.e., 23rd)</p>
<dt>%H</p>
<dd> Name of current Holyday, if any</p>
<dt>%N</p>
<dd> Magic code to prevent rest of format from being printed unless today is a Holyday.</p>
<dt>%n</p>
<dd> Newline</p>
<dt>%t</p>
<dd> Tab</p>
<dt>%X</p>
<dd> Number of days remaining until X-Day. (Not valid if the SubGenius options are not compiled in.)</p>
<dt>%{</p>
<dd>
<dt>%}</p>
<dd> Used to enclose the part of the string which is to be replaced with the words &quot;St. Tib&#8217;s Day&quot; if the current day is St. Tib&#8217;s Day.</p>
<dt>%.</p>
<dd> Try it and see.</dl>
<h2>EXAMPLES</h2>
<pre><code>
% ddate

        Sweetmorn,
    Bureaucracy 42, 3161 YOLD % ddate + 'Today is %{%A, the %e of %B%}, %Y. %N%nCelebrate %H'

                        Today is Sweetmorn,
    the 42nd of Bureaucracy, 3161. % ddate + "It's %{%A, the %e of %B%}, %Y. %N%nCelebrate %H" 26 9 1995

                                                 It's Prickle-Prickle, the 50th of Bureaucracy, 3161.

                                                 Celebrate Bureflux %
                                                 ddate +
                                 "Today's %{%A, the %e of %B%}, %Y. %N%nCelebrate %H" 29 2 1996

                                 Today 's St. Tib' s Day,
    3162.
</code></pre>
<h2>BUGS</h2>
<p> <code><a href="/docs/linux/man/1-ddate/">ddate</a>(1)</code> will produce undefined behavior if asked to produce the date for St. Tib&#8217;s day and its format string does not contain the St. Tib&#8217;s Day delimiters %{ and %}. </p>
<h2>NOTE</h2>
<p> After `X-Day&#8217; passed without incident, the Church of the SubGenius declared that it had got the year upside down &#8211; X-Day is actually in 8661 AD rather than 1998 AD. Thus, the True X-Day is Cfn 40, 9827. </p>
<h2>AUTHOR</h2>
<p> Original program by Druel the Chaotic aka Jeremy Johnson (mpython [at] gnu.ai.mit.edu)<br />
 Major rewrite by Lee H:. O:. Smith, KYTP, aka Andrew Bulhak (acb [at] dev.null.org)<br />
 Five tons of flax. </p>
<h2>DISTRIBUTION POLICY</h2>
<p> Public domain. All rites reversed. </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-date/">date</a>(1),<br />
 <a rel="nofollow" href="http://www.subgenius.com/">http://www.subgenius.com/</a><br />
 Malaclypse the Younger, <i>Principia Discordia, Or How I Found Goddess And What I Did To Her When I Found Her</i> </p>
<h2>AVAILABILITY</h2>
<p> The ddate command is part of the util-linux package and is available from <a href="ftp://ftp.kernel.org/pub/linux/utils/util-linux/.">ftp://ftp.kernel.org/pub/linux/utils/util-linux/.</a> </p>
<h2>Index</h2>
