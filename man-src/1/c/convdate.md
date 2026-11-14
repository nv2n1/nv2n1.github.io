---
title: "convdate(1)"
name: "convdate"
section: "1"
letter: "c"
url: "/docs/linux/man/1-convdate/"
description: "convdate – Convert to/from RFC 5322 dates and seconds since epoch"
---

<h2 class="name">NAME</h2>
<p> convdate &#8211; Convert to/from RFC 5322 dates and seconds since epoch </p>
<h2>SYNOPSIS</h2>
<p> <code>convdate</code> [<code>-dhl</code>] [<code>-c</code> | <code>-n</code> | <code>-s</code>] [<i>date</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>convdate</code> translates the date/time strings given on the command line, outputting the results one to a line. The input can either be a date in <font SIZE="-1">RFC</font>&nbsp;<wbr>5322 format (accepting the variations on that format that <i><a href="/docs/linux/man/8-innd/">innd</a></i>(8) is willing to accept), or the number of seconds since epoch (if <code>-c</code> is given). The output is either <i><a href="/docs/linux/man/3-ctime/">ctime</a></i>(3) results, the number of seconds since epoch, or a Usenet Date: header, depending on the options given. </p>
<p> If <i>date</i> is not given, <code>convdate</code> outputs the current date.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code></p>
<dd> Each argument is taken to be the number of seconds since epoch (a time_t) rather than a date.</p>
<dt><code>-d</code></p>
<dd> Output a valid Usenet Date: header instead of the results of <i><a href="/docs/linux/man/3-ctime/">ctime</a></i>(3) for each date given on the command line. This is useful for testing the algorithm used to generate Date: headers for local posts. Normally, the date will be in <font SIZE="-1">UTC</font>, but see the <code>-l</code> option.</p>
<dt><code>-h</code></p>
<dd> Print usage information and exit.</p>
<dt><code>-l</code></p>
<dd> Only makes sense in combination with <code>-d</code>. If given, Date: headers generated will use the local time zone instead of <font SIZE="-1">UTC</font>.</p>
<dt><code>-n</code></p>
<dd> Rather than outputting the results of <i><a href="/docs/linux/man/3-ctime/">ctime</a></i>(3) or a Date: header, output each date given as the number of seconds since epoch (a time_t). This option doesn&#8217;t make sense in combination with <code>-d</code>.</p>
<dt><code>-s</code></p>
<dd> Pass each given date to the <font SIZE="-1">RFC</font>&nbsp;<wbr>5322 date parser and print the results of <i><a href="/docs/linux/man/3-ctime/">ctime</a></i>(3) (or a Date: header if <code>-d</code> is given). This is the default behavior.</dl>
<h2>EXAMPLES</h2>
<p> Most of these examples are taken, with modifications from the original man page dating from 1991 and were run in the <font SIZE="-1">EST/EDT</font> time zone. </p>
<pre>
    % convdate '10 Feb 1991 10:00:00 -0500'
    Sun Feb 10 10:00:00 1991
    % convdate '13 Dec 91 12:00 EST' '04 May 1990 0:0:0'
    Fri Dec 13 12:00:00 1991
    Fri May  4 00:00:00 1990
    % convdate -n '10 feb 1991 10:00' '4 May 90 12:00'
    666198000
    641880000
    % convdate -c 666198000
    Sun Feb 10 10:00:00 1991
</pre>
<p> <i><a href="/docs/linux/man/3-ctime/">ctime</a></i>(3) results are in the local time zone. Compare to: </p>
<pre>
    % convdate -dc 666198000
    Sun, 10 Feb 1991 15:00:00 +0000 (UTC)
    % env TZ=PST8PDT convdate -dlc 666198000
    Sun, 10 Feb 1991 07:00:00 -0800 (PST)
    % env TZ=EST5EDT convdate -dlc 666198000
    Sun, 10 Feb 1991 10:00:00 -0500 (EST)
</pre>
<p> The system library functions generally use the environment variable <font SIZE="-1">TZ</font> to determine (or at least override) the local time zone.</p>
<h2>HISTORY</h2>
<p> Written by Rich <tt>$alz</tt> &lt;rsalz [at] uunet.uu.net&gt;, rewritten and updated by Russ Allbery &lt;eagle [at] eyrie.org&gt; for the <code>-d</code> and <code>-l</code> flags. </p>
<p> <tt>$Id:</tt> convdate.pod 9768 2014-12-07 21:22:57Z iulius $</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/5-active-times/">active.times</a></i>(5). </p>
<h2>Index</h2>
