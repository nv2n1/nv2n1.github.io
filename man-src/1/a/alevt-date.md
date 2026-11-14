---
title: "alevt-date(1)"
name: "alevt-date"
section: "1"
letter: "a"
url: "/docs/linux/man/1-alevt-date/"
description: "alevt-date – display/set time received via Teletext"
---

<h2>NAME</h2>
<p> alevt-date &#8211; display/set time received via Teletext </p>
<h2>SYNOPSIS</h2>
<p> <code>alevt-date</code> [<i>options</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>alevt-date</code> displays the time received from a Teletext source. It can be used to set the system time. The date is not interpreted (not even transmitted on most channels). So it allows only adjustment of +/-12 hours. The default allowed adjustment is limited to +/-2 hours (use -delta to change). Without the -set option it just displays the date in the format of the <code><a href="/docs/linux/man/1-date/">date</a></code>(1) command. </p>
<h2>OPTIONS</h2>
<p> A summary of options is included below.</p>
<dl>
<dt><code>-set</code></p>
<dd> Set system time from time received via Teletext.</p>
<dt><code>-delta</code><i>&nbsp;<wbr>seconds</i></p>
<dd> Maximum allowed adjustment made to the system time. The default is 7200 seconds (2 hours) and the maximum that may be given is 12 hours.</p>
<dt><code>-format</code><i>&nbsp;<wbr>string</i></p>
<dd> Format string to used to print the time. Look at <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3) for possible control sequences.</p>
<dt><code>-vbi</code><i>&nbsp;<wbr>device</i></p>
<dd> Use the given device name (default: /dev/vbi0).</p>
<dt><code>-timeout</code><i>&nbsp;<wbr>seconds</i></p>
<dd> If the time can&#8217;t be detected in <i>seconds</i>, the program is terminated with a SIGALRM.</p>
<dt><code>&#8211;help</code></p>
<dd> Show summary of options.</p>
<dt><code>&#8211;version</code></p>
<dd> Show version of program.</dl>
<p> Before starting this program, you have to set the TV channel with another program like <code>xawtv</code> of <code>set-tv</code>. </p>
<p> Note: This program does <code>not</code> set the battery backed up clock of your computer. <i>clock -w</i> will do this. </p>
<h2>FILES</h2>
<p> <i>/dev/vbi*</i> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="//www.systutorials.com/docs/linux/man/1x-alevt/">alevt</a></code>(1x), <code><a href="/docs/linux/man/1-alevt-cap/">alevt-cap</a></code>(1), <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3), <code><a href="/docs/linux/man/1-date/">date</a></code>(1), <code><a href="/docs/linux/man/8-clock/">clock</a></code>(8). </p>
<h2>BUGS</h2>
<p> This program is just a toy. The time transmitted by the TV stations is more than inaccurate. Some are within a few seconds of your local time reference but others are more then 15 minutes off. You&#8217;ve been warned. (And don&#8217;t assume the pkt8/30 time is better. It&#8217;s even worse.) </p>
<p> No bug reports to &lt;froese [at] gmx.de&gt; *g*. </p>
<h2>Index</h2>
