---
title: "rrdfetch(1)"
name: "rrdfetch"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rrdfetch/"
description: "rrdfetch – Fetch data from an RRD."
---

<h2 class="name">NAME</h2>
<p> rrdfetch &#8211; Fetch data from an RRD. </p>
<h2>SYNOPSIS</h2>
<p> <code>rrdtool</code> <code>fetch</code> <i>filename</i> <i></i><font SIZE="-1"><i>CF</i></font><i></i> [<code>&#8211;resolution</code>|<code>-r</code>&nbsp;<wbr><i>resolution</i>] [<code>&#8211;start</code>|<code>-s</code>&nbsp;<wbr><i>start</i>] [<code>&#8211;end</code>|<code>-e</code>&nbsp;<wbr><i>end</i>] [<code>&#8211;daemon</code>&nbsp;<wbr><i>address</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <code>fetch</code> function is normally used internally by the graph function to get data from <font SIZE="-1"><code>RRD</code></font>s. <code>fetch</code> will analyze the <font SIZE="-1"><code>RRD</code></font> and try to retrieve the data in the resolution requested. The data fetched is printed to stdout. <i>*UNKNOWN*</i> data is often represented by the string &#8220;NaN&#8221; depending on your <font SIZE="-1">OS</font>&#8216;s printf function.</p>
<dl>
<dt><i>filename</i></p>
<dd> the name of the <font SIZE="-1"><code>RRD</code></font> you want to fetch the data from.</p>
<dt><i></i><font SIZE="-1"><i>CF</i></font><i></i></p>
<dd> the consolidation function that is applied to the data you want to fetch (<font SIZE="-1">AVERAGE</font>,MIN,MAX,LAST)</p>
<dt><code>&#8211;resolution</code>|<code>-r</code> <i>resolution</i> (default is the highest resolution)</p>
<dd> the interval you want the values to have (seconds per value). <code>rrdfetch</code> will try to match your request, but it will return data even if no absolute match is possible. <font SIZE="-1"><code>NB</code></font><code>.</code> See note below.</p>
<dt><code>&#8211;start</code>|<code>-s</code> <i>start</i> (default end-1day)</p>
<dd> start of the time series. A time in seconds since epoch (1970-01-01) is required. Negative numbers are relative to the current time. By default, one day worth of data will be fetched. See also AT-STYLE <font SIZE="-1">TIME</font> <font SIZE="-1">SPECIFICATION</font> section for a detailed explanation on ways to specify the start time.</p>
<dt><code>&#8211;end</code>|<code>-e</code> <i>end</i> (default now)</p>
<dd> the end of the time series in seconds since epoch. See also AT-STYLE <font SIZE="-1">TIME</font> <font SIZE="-1">SPECIFICATION</font> section for a detailed explanation of how to specify the end time.</p>
<dt><code>&#8211;daemon</code> <i>address</i></p>
<dd> Address of the rrdcached daemon. If specified, a <tt>&quot;flush&quot;</tt> command is sent to the server before reading the <font SIZE="-1">RRD</font> files. This allows <code>rrdtool</code> to return fresh data even if the daemon is configured to cache values for a long time. For a list of accepted formats, see the <code>-l</code> option in the rrdcached manual. </p>
<pre>
 rrdtool fetch --daemon unix:/var/run/rrdcached.sock /var/lib/rrd/foo.rrd AVERAGE
</pre>
</dl>
<h3><font SIZE="-1">RESOLUTION</font> <font SIZE="-1">INTERVAL</font></h3>
<p> In order to get RRDtool to fetch anything other than the finest resolution <font SIZE="-1">RRA</font> <code>both</code> the start and end time must be specified on boundaries that are multiples of the desired resolution. Consider the following example: </p>
<pre>
 rrdtool create subdata.rrd -s 10 DS:ds0:GAUGE:300:0:U \
  RRA:AVERAGE:0.5:30:3600 \
  RRA:AVERAGE:0.5:90:1200 \
  RRA:AVERAGE:0.5:360:1200 \
  RRA:MAX:0.5:360:1200 \
  RRA:AVERAGE:0.5:8640:600 \
  RRA:MAX:0.5:8640:600
</pre>
<p> This <font SIZE="-1">RRD</font> collects data every 10 seconds and stores its averages over 5 minutes, 15 minutes, 1 hour, and 1 day, as well as the maxima for 1 hour and 1 day. </p>
<p> Consider now that you want to fetch the 15 minute average data for the last hour. You might try </p>
<pre>
 rrdtool fetch subdata.rrd AVERAGE -r 900 -s -1h
</pre>
<p> However, this will almost always result in a time series that is <font SIZE="-1"><code>NOT</code></font> in the 15 minute <font SIZE="-1">RRA</font>. Therefore, the highest resolution <font SIZE="-1">RRA</font>, i.e. 5 minute averages, will be chosen which in this case is not what you want. </p>
<p> Hence, make sure that</p>
<dl>
<dt>1.</p>
<dd> both start and end time are a multiple of 900</p>
<dt>2.</p>
<dd> both start and end time are within the desired <font SIZE="-1">RRA</font></dl>
<p> So, if time now is called &#8220;t&#8221;, do </p>
<pre><code>
end time == int(t / 900) * 900,
    start time == end time - 1hour,
    resolution == 900.
</code></pre>
<p> Using the bash shell, this could look be: </p>
<pre>
 TIME=$(date +%s)
 RRDRES=900
 rrdtool fetch subdata.rrd AVERAGE -r $RRDRES \
    -e $(($TIME/$RRDRES*$RRDRES)) -s e-1h
</pre>
<p> Or in Perl: </p>
<pre><code>
perl - e '$ctime = time; $rrdres = 900; \
          system "rrdtool fetch subdata.rrd AVERAGE \
                  -r $rrdres -e @{[int($ctime/$rrdres)*$rrdres]} -s e-1h"'
</code></pre>
<h3>AT-STYLE <font SIZE="-1">TIME</font> <font SIZE="-1">SPECIFICATION</font></h3>
<p> Apart from the traditional <i>Seconds since epoch</i>, RRDtool does also understand at-style time specification. The specification is called &#8220;at-style&#8221; after the Unix command <i><a href="/docs/linux/man/1-at/">at</a></i>(1) that has moderately complex ways to specify time to run your job at a certain date and time. The at-style specification consists of two parts: the <font SIZE="-1"><code>TIME</code></font><font SIZE="-1"><code>REFERENCE</code></font> specification and the <font SIZE="-1"><code>TIME</code></font><font SIZE="-1"><code>OFFSET</code></font> specification.</p>
<h3><font SIZE="-1">TIME</font> <font SIZE="-1">REFERENCE</font> <font SIZE="-1">SPECIFICATION</font></h3>
<p> The time reference specification is used, well, to establish a reference moment in time (to which the time offset is then applied to). When present, it should come first, when omitted, it defaults to <code>now</code>. On its own part, time reference consists of a <i>time-of-day</i> reference (which should come first, if present) and a <i>day</i> reference. </p>
<p> The <i>time-of-day</i> can be specified as <font SIZE="-1"><code>HH:MM</code></font>, <font SIZE="-1"><code>HH</code></font><code>.MM</code>, or just <font SIZE="-1"><code>HH</code></font>. You can suffix it with <code>am</code> or <code>pm</code> or use 24-hours clock. Some special times of day are understood as well, including <code>midnight</code> (00:00), <code>noon</code> (12:00) and British <code>teatime</code> (16:00). </p>
<p> The <i>day</i> can be specified as <i>month-name</i> <i>day-of-the-month</i> and optional a 2- or 4-digit <i>year</i> number (e.g. March 8 1999). Alternatively, you can use <i>day-of-week-name</i> (e.g. Monday), or one of the words: <code>yesterday</code>, <code>today</code>, <code>tomorrow</code>. You can also specify the <i>day</i> as a full date in several numerical formats, including <code>MM/DD/[</code><font SIZE="-1"><code>YY</code></font><code>]YY</code>, <font SIZE="-1"><code>DD</code></font><code>.MM.[</code><font SIZE="-1"><code>YY</code></font><code>]YY</code>, or <font SIZE="-1"><code>YYYYMMDD</code></font>. </p>
<p> <i></i><font SIZE="-1"><i>NOTE1</i></font><i></i>: this is different from the original <i><a href="/docs/linux/man/1-at/">at</a></i>(1) behavior, where a single-number date is interpreted as MMDD[<font SIZE="-1">YY</font>]YY. </p>
<p> <i></i><font SIZE="-1"><i>NOTE2</i></font><i></i>: if you specify the <i>day</i> in this way, the <i>time-of-day</i> is <font SIZE="-1">REQUIRED</font> as well. </p>
<p> Finally, you can use the words <code>now</code>, <code>start</code>, <code>end</code> or <code>epoch</code> as your time reference. <code>Now</code> refers to the current moment (and is also the default time reference). <code>Start</code> (<code>end</code>) can be used to specify a time relative to the start (end) time for those tools that use these categories (<code>rrdfetch</code>, rrdgraph) and <code>epoch</code> indicates the *IX epoch (*IX timestamp 0 = 1970-01-01 00:00:00 <font SIZE="-1">UTC</font>). <code>epoch</code> is useful to disambiguate between a timestamp value and some forms of abbreviated date/time specifications, because it allows to use time offset specifications using units, eg. <code>epoch</code>+19711205s unambiguously denotes timestamp 19711205 and not 1971-12-05 00:00:00 <font SIZE="-1">UTC</font>. </p>
<p> Month and day of the week names can be used in their naturally abbreviated form (e.g., Dec for December, Sun for Sunday, etc.). The words <code>now</code>, <code>start</code>, <code>end</code> can be abbreviated as <code>n</code>, <code>s</code>, <code>e</code>.</p>
<h3><font SIZE="-1">TIME</font> <font SIZE="-1">OFFSET</font> <font SIZE="-1">SPECIFICATION</font></h3>
<p> The time offset specification is used to add/subtract certain time intervals to/from the time reference moment. It consists of a <i>sign</i> (<code>+</code>&nbsp;<wbr>or&nbsp;<wbr><code>&#8211;</code>) and an <i>amount</i>. The following time units can be used to specify the <i>amount</i>: <code>years</code>, <code>months</code>, <code>weeks</code>, <code>days</code>, <code>hours</code>, <code>minutes</code>, or <code>seconds</code>. These units can be used in singular or plural form, and abbreviated naturally or to a single letter (e.g. +3days, -1wk, -3y). Several time units can be combined (e.g., -5mon1w2d) or concatenated (e.g., -5h45min = -5h-45min = -6h+15min = -7h+1h30m-15min, etc.) </p>
<p> <i></i><font SIZE="-1"><i>NOTE3</i></font><i></i>: If you specify time offset in days, weeks, months, or years, you will end with the time offset that may vary depending on your time reference, because all those time units have no single well defined time interval value (1 year contains either 365 or 366 days, 1 month is 28 to 31 days long, and even 1 day may be not equal to 24 hours twice a year, when DST-related clock adjustments take place). To cope with this, when you use days, weeks, months, or years as your time offset units your time reference date is adjusted accordingly without too much further effort to ensure anything about it (in the hope that <i><a href="/docs/linux/man/3-mktime/">mktime</a></i>(3) will take care of this later). This may lead to some surprising (or even invalid!) results, e.g. &#8216;May 31 -1month&#8217; = &#8216;Apr 31&#8217; (meaningless) = &#8216;May 1&#8217; (after <i><a href="/docs/linux/man/3-mktime/">mktime</a></i>(3) normalization); in the <font SIZE="-1">EET</font> timezone &#8216;3:30am Mar 29 1999 -1 day&#8217; yields &#8216;3:30am Mar 28 1999&#8217; (Sunday) which is an invalid time/date combination (because of 3am -&gt; 4am <font SIZE="-1">DST</font> forward clock adjustment, see the below example). </p>
<p> In contrast, hours, minutes, and seconds are well defined time intervals, and these are guaranteed to always produce time offsets exactly as specified (e.g. for <font SIZE="-1">EET</font> timezone, &#8216;8:00 Mar 27 1999&nbsp;<wbr>+2 days&#8217; = &#8216;8:00 Mar 29 1999&#8217;, but since there is 1-hour <font SIZE="-1">DST</font> forward clock adjustment that occurs around 3:00 Mar 28 1999, the actual time interval between 8:00 Mar 27 1999 and 8:00 Mar 29 1999 equals 47 hours; on the other hand, &#8216;8:00 Mar 27 1999&nbsp;<wbr>+48 hours&#8217; = &#8216;9:00 Mar 29 1999&#8217;, as expected) </p>
<p> <i></i><font SIZE="-1"><i>NOTE4</i></font><i></i>: The single-letter abbreviation for both <code>months</code> and <code>minutes</code> is <code>m</code>. To disambiguate them, the parser tries to read your mind :) by applying the following two heuristics:</p>
<dl>
<dt>1.</p>
<dd> If <code>m</code> is used in context of (i.e. right after the) years, months, weeks, or days it is assumed to mean <code>months</code>, while in the context of hours, minutes, and seconds it means minutes. (e.g., in -1y6m or +3w1m <code>m</code> is interpreted as <code>months</code>, while in -3h20m or +5s2m <code>m</code> the parser decides for <code>minutes</code>).</p>
<dt>2.</p>
<dd> Out of context (i.e. right after the <code>+</code> or <code>&#8211;</code> sign) the meaning of <code>m</code> is guessed from the number it directly follows. Currently, if the number&#8217;s absolute value is below 25 it is assumed that <code>m</code> means <code>months</code>, otherwise it is treated as <code>minutes</code>. (e.g., -25m == -25 minutes, while +24m == +24 months)</dl>
<p> <i>Final </i><font SIZE="-1"><i>NOTES</i></font><i></i>: Time specification is case-insensitive. Whitespace can be inserted freely or omitted altogether. There are, however, cases when whitespace is required (e.g., &#8216;midnight Thu&#8217;). In this case you should either quote the whole phrase to prevent it from being taken apart by your shell or use &#8216;_&#8217; (underscore) or &#8216;,&#8217; (comma) which also count as whitespace (e.g., midnight_Thu or midnight,Thu).</p>
<h3><font SIZE="-1">TIME</font> <font SIZE="-1">SPECIFICATION</font> <font SIZE="-1">EXAMPLES</font></h3>
<p> <i>Oct 12</i> &#8212; October 12 this year </p>
<p> <i>-1month</i> or <i>-1m</i> &#8212; current time of day, only a month before (may yield surprises, see <font SIZE="-1">NOTE3</font> above). </p>
<p> <i>noon yesterday -3hours</i> &#8212; yesterday morning; can also be specified as <i>9am-1day</i>. </p>
<p> <i>23:59 31.12.1999</i> &#8212; 1 minute to the year 2000. </p>
<p> <i>12/31/99 11:59pm</i> &#8212; 1 minute to the year 2000 for imperialists. </p>
<p> <i>12am 01/01/01</i> &#8212; start of the new millennium </p>
<p> <i>end-3weeks</i> or <i>e-3w</i> &#8212; 3 weeks before end time (may be used as start time specification). </p>
<p> <i>start+6hours</i> or <i>s+6h</i> &#8212; 6 hours after start time (may be used as end time specification). </p>
<p> <i>931225537</i> &#8212; 18:45 July 5th, 1999 (yes, seconds since 1970 are valid as well). </p>
<p> <i>19970703 12:45</i> &#8212; 12:45 July 3th, 1997 (my favorite, and its even got an <font SIZE="-1">ISO</font> number (8601)).</p>
<h2>ENVIRONMENT VARIABLES</h2>
<p> The following environment variables may be used to change the behavior of <tt>&quot;rrdtool fetch&quot;</tt>:</p>
<dl>
<dt><font SIZE="-1"><code>RRDCACHED_ADDRESS</code></font></p>
<dd> If this environment variable is set it will have the same effect as specifying the <tt>&quot;--daemon&quot;</tt> option on the command line. If both are present, the command line argument takes precedence.</dl>
<h2>AUTHOR</h2>
<p> Tobias Oetiker &lt;tobi [at] oetiker.ch&gt; </p>
<h2>Index</h2>
<dt><a href="#lbAJ">ENVIRONMENT VARIABLES</a></p>
<dd>
<dt><a href="#lbAK">AUTHOR</a></p>
<dd></dl>
