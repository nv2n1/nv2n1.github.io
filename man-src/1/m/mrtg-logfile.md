---
title: "mrtg-logfile(1)"
name: "mrtg-logfile"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mrtg-logfile/"
description: "mrtg-logfile – description of the mrtg-2 logfile format"
---

<h2 class="name">NAME</h2>
<p> mrtg-logfile &#8211; description of the mrtg-2 logfile format </p>
<h2>SYNOPSIS</h2>
<p> This document provides a description of the contents of the mrtg-2 logfile.</p>
<h2>OVERVIEW</h2>
<p> The logfile consists of two main sections.</p>
<dl>
<dt>The first Line</p>
<dd> It stores the traffic counters from the most recent run of mrtg.</p>
<dt>The rest of the File</p>
<dd> Stores past traffic rate averates and maxima at increassing intervals.</dl>
<p> The first number on each line is a unix time stamp. It represents the number of seconds since 1970.</p>
<h2>DETAILS</h2>
<h3>The first Line</h3>
<p> The first line has 3 numbers which are:</p>
<dl>
<dt>A (1st column)</p>
<dd> A timestamp of when <font SIZE="-1">MRTG</font> last ran for this interface. The timestamp is the number of non-skip seconds passed since the standard <font SIZE="-1">UNIX</font> &#8220;epoch&#8221; of midnight on 1st of January 1970 <font SIZE="-1">GMT</font>.</p>
<dt>B (2nd column)</p>
<dd> The &#8220;incoming bytes counter&#8221; value.</p>
<dt>C (3rd column)</p>
<dd> The &#8220;outgoing bytes counter&#8221; value.</dl>
<h3>The rest of the File</h3>
<p> The second and remaining lines of the file contains 5 numbers which are:</p>
<dl>
<dt>A (1st column)</p>
<dd> The Unix timestamp for the point in time the data on this line is relevant. Note that the interval between timestamps increases as you progress through the file. At first it is 5 minutes and at the end it is one day between two lines. </p>
<p> This timestamp may be converted in OpenOffice Calc or <font SIZE="-1">MS</font> Excel by using the following formula </p>
<pre>
 =(x+y)/86400+DATE(1970;1;1)
</pre>
<p> (instead of &#8220;;&#8221; it may be that you have to use &#8220;,&#8221; this depends on the context and your locale settings) </p>
<p> you can also ask perl to help by typing </p>
<pre>
 perl -e 'print scalar localtime(x),&quot;
&quot;'
</pre>
<p> <code>x</code> is the unix timestamp and <code>y</code> is the offset in seconds from <font SIZE="-1">UTC</font>. (Perl knows <code>y</code>).</p>
<dt>B (2nd column)</p>
<dd> The average incoming transfer rate in bytes per second. This is valid for the time between the A value of the current line and the A value of the previous line.</p>
<dt>C (3rd column)</p>
<dd> The average outgoing transfer rate in bytes per second since the previous measurement.</p>
<dt>D (4th column)</p>
<dd> The maximum incoming transfer rate in bytes per second for the current interval. This is calculated from all the updates which have occured in the current interval. If the current interval is 1 hour, and updates have occured every 5 minutes, it will be the biggest 5 minute transfer rate seen during the hour.</p>
<dt>E (5th column)</p>
<dd> The maximum outgoing transfer rate in bytes per second for the current interval.</dl>
<h2>AUTHOR</h2>
<p> Butch Kemper &lt;kemper [at] bihs.net&gt; and Tobias Oetiker &lt;tobi [at] oetiker.ch&gt; </p>
<h2>Index</h2>
