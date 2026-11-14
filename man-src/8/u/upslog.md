---
title: "upslog(8)"
name: "upslog"
section: "8"
letter: "u"
url: "/docs/linux/man/8-upslog/"
description: "upslog – UPS status logger"
---

<p>upslog &#8211; UPS status logger</p>
<h2>Synopsis</h2>
<p><code>upslog -h</code> </p>
<p> <code>upslog</code> [<i>OPTIONS</i>]</p>
<h2>Description</h2>
<p><code>upslog</code> is a daemon that will poll a UPS at periodic intervals, fetch the variables that interest you, format them, and write them to a file. </p>
<p> The default format string includes variables that are supported by many common UPS models. See the description below to make your own.</p>
<h2>Options</h2>
<p><code>-h</code></p>
<dl>
<dd>Display the help message.</dl>
<p> <code>-f</code> <i>format</i></p>
<dl>
<dd>Monitor the UPS using this format string. Be sure to enclose <i>format</i> in quotes so your shell doesn&#8217;t split it up. Valid escapes within this string are: </p>
<p> %%</p>
<dl>
<dd>Insert a single &quot;%&quot;</dl>
<p> %TIME format%</p>
<dl>
<dd>Insert the time with strftime formatting</dl>
<p> %ETIME%</p>
<dl>
<dd>Insert the number of seconds, ala time_t. This is now a 10 digit number.</dl>
<p> %HOST%</p>
<dl>
<dd>insert the local hostname</dl>
<p> %UPSHOST%</p>
<dl>
<dd>insert the host of the UPS being monitored</dl>
<p> %PID%</p>
<dl>
<dd>insert the pid of upslog</dl>
<p> %VAR varname%</p>
<dl>
<dd>insert the value of variable varname</dl>
</dl>
<p> The default format string is: </p>
<dl>
<dd>
<pre>%TIME @Y@m@d @H@M@S% %VAR battery.charge% %VAR input.voltage%
%VAR ups.load% [%VAR ups.status%] %VAR ups.temperature%
%VAR input.frequency%</pre>
</dl>
<p> <code>-i</code> <i>interval</i></p>
<dl>
<dd>Wait this many seconds between polls. This defaults to 30 seconds. </p>
<p> If you require tighter timing, you should write your own logger using the <code><a href="/docs/linux/man/3-upsclient/">upsclient</a></code>(3) library.</dl>
<p> <code>-l</code> <i>logfile</i></p>
<dl>
<dd>Store the results in this file. </p>
<p> You can use &quot;-&quot; for stdout, but upslog will remain in the foreground.</dl>
<p> <code>-s</code> <i>ups</i></p>
<dl>
<dd>Monitor this UPS. The format for this option is upsname[@hostname[:port]]. The default hostname is &quot;localhost&quot;.</dl>
<p> <code>-u</code> <i>username</i></p>
<dl>
<dd>If started as root, upsmon will <code><a href="/docs/linux/man/2-setuid/">setuid</a></code>(2) to the user id associated with <i>username</i> for security. </p>
<p> If <i>username</i> is not defined, it will use the value that was compiled into the program. This defaults to &quot;nobody&quot;, which is less than ideal.</dl>
<h2>Service Delays</h2>
<p>The interval value is merely the number given to <code><a href="/docs/linux/man/3-sleep/">sleep</a></code>(3) after running through the format string. Therefore, a query will actually take slightly longer than the interval, depending on the speed of your system.</p>
<h2>Log Rotation</h2>
<p><code>upslog</code> writes its PID to upslog.pid, and will reopen the log file if you send it a SIGHUP. This allows it to keep running when the log is rotated by an external program.</p>
<h2>See Also</h2>
<h3>Server:</h3>
<p><code><a href="/docs/linux/man/8-upsd/">upsd</a></code>(8)</p>
<h3>Clients:</h3>
<p><code><a href="/docs/linux/man/8-upsc/">upsc</a></code>(8), <code><a href="/docs/linux/man/8-upscmd/">upscmd</a></code>(8), <code><a href="/docs/linux/man/8-upsrw/">upsrw</a></code>(8), <code><a href="/docs/linux/man/8-upsmon/">upsmon</a></code>(8)</p>
<h3>Internet resources:</h3>
<p>The NUT (Network UPS Tools) home page: <a rel="nofollow" href="http://www.networkupstools.org/">http://www.networkupstools.org/</a> </p>
