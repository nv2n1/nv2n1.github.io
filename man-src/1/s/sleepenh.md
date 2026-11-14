---
title: "sleepenh(1)"
name: "sleepenh"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sleepenh/"
description: "sleepenh – an enhanced sleep program."
---

<h2 class="name">NAME</h2>
<p> sleepenh &#8211; an enhanced sleep program. </p>
<h2>SYNOPSIS</h2>
<p> <code>sleepenh</code> [<i>initial-time</i>] sleep-time</p>
<h2>DESCRIPTION</h2>
<p> <code>sleepenh</code> is a program that can be used when there is a need to execute some functions periodically in a shell script. It was not designed to be accurate for a single sleep, but to be accurate in a sequence of consecutive sleeps.<br />
 After a successful execution, it returns to stdout the timestamp it finished running, that can be used as <code>initial-time</code> to a successive execution of <code>sleepenh</code>.</p>
<h2>OPTIONS</h2>
<p> There are no command line options. Run it without any option to get a brief help and version.</p>
<h2>ARGUMENTS</h2>
<p> <code>sleep-time</code> is a real number in seconds, with microseconds resolution (1 minute, 20 seconds and 123456 microseconds would be 80.123456).<br />
 <code>initial-time</code> is a real number in seconds, with microseconds resolution. This number is system dependent. In GNU/Linux systems, it is the number of seconds since midnight 1970-01-01 GMT. Do not try to get a good value of <code>initial-time</code>. Use the value supplied by a previous execution of <code>sleepenh</code>.<br />
 If you don&#8217;t specify <code>initial-time</code>, it is assumed the current-time.</p>
<h2>EXIT STATUS</h2>
<p> An exit status greater or equal to 10 means failure. Known exit status:</p>
<dl>
<dt><code>0</code></p>
<dd> Success.</p>
<dt><code>1</code></p>
<dd> Success. There was no need to sleep. (means that initial-time + sleep-time was greater than current-time).</p>
<dt><code>10</code></p>
<dd> Failure. Missing command line arguments.</p>
<dt><code>11</code></p>
<dd> Failure. Did not receive SIGALRM.</p>
<dt><code>12</code></p>
<dd> Failure. Argument is not a number.</p>
<dt><code>13</code></p>
<dd> Failure. System error, could not get current time.</dl>
<h2>USAGE EXAMPLE</h2>
<p> Suppose you need to send the char &#8216;A&#8217; to the serial port ttyS0 every 4 seconds. This will do that:</p>
<dl>
<dt>
<dd>
&nbsp;<wbr>#!/bin/sh<br />
&nbsp;<wbr>TIMESTAMP=`sleepenh 0`<br />
&nbsp;<wbr>while true;&nbsp;<wbr>do<br />
#&nbsp;<wbr>send the byte to ttyS0<br />
echo -n&nbsp;<wbr>&quot;A&quot;&nbsp;<wbr>&gt;&nbsp;<wbr>/dev/ttyS0;<br />
&nbsp;<wbr>&nbsp;<wbr><br />
#&nbsp;<wbr>just print a nice message on screen<br />
echo -n&nbsp;<wbr>&quot;I sent&nbsp;<wbr>&#8216;A&#8217;&nbsp;<wbr>to ttyS0, time now is&nbsp;<wbr>&quot;;<br />
sleepenh 0; </p>
<p>#&nbsp;<wbr>wait the required time&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><br />
TIMESTAMP=`sleepenh&nbsp;<wbr>$TIMESTAMP 4.0`;<br />
&nbsp;<wbr>done</dl>
<h2>HINT</h2>
<p> This program can be used to get the current time. Just execute:</p>
<dl>
<dt>sleepenh 0</p>
<dd></dl>
<h2>BUGS</h2>
<p> It is not accurate for a single sleep. Short sleep-times will also not be accurate.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-date/">date</a></code>(1), <code><a href="/docs/linux/man/1-sleep/">sleep</a></code>(1). </p>
<h2>AUTHOR</h2>
<p> This manual page was written by Pedro Zorzenon Neto. </p>
<h2>Index</h2>
