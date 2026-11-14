---
title: "gammu-smsd-monitor(1)"
name: "gammu-smsd-monitor"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gammu-smsd-monitor/"
description: "gammu-smsd-monitor – Monitor state of SMS daemon for Gammu"
---

<h2>NAME</h2>
<p> gammu-smsd-monitor &#8211; Monitor state of SMS daemon for Gammu</p>
<h2>SYNOPSIS</h2>
<p> <code>gammu-smsd-monitor</code> [<i>OPTION</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>gammu-smsd-monitor</code> command. </p>
<p> <code>gammu-smsd-monitor</code> is a program that monitors state of Gammu SMS daemon. It periodically displays information about phone and number of processed messages. </p>
<p> Program accepts following options (please note that long options might be not accepted on some platforms):</p>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Shows help.</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> Shows version information and compiled in features.</p>
<dt><code>-c</code>, <code>&#8211;config</code>=<i>file</i></p>
<dd> Configuration file to use, default is /etc/gammu-smsdrc, on Windows there is no default and configuration file path has to be always specified.</p>
<dt><code>-l</code>, <code>&#8211;loops</code>=<i>count</i></p>
<dd> Number of loops, by default monitor loops infinitely.</p>
<dt><code>-d</code>, <code>&#8211;delay</code>=<i>seconds</i></p>
<dd> Delay betwen polling SMSD state, default is 20 seconds.</p>
<dt><code>-C</code>, <code>&#8211;csv</code></p>
<dd> Print output in comma separated values format: </p>
<p> client;phone ID;IMEI;sent;received;failed;battery;signal </p>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/5-gammu-smsdrc/">gammu-smsdrc</a>(5), <a href="/docs/linux/man/1-gammu/">gammu</a>(1), <a href="/docs/linux/man/1-gammu-smsd/">gammu-smsd</a>(1)</p>
<h2>AUTHOR</h2>
<p> gammu-smsd and this manual page were written by Michal Cihar &lt;michal [at] cihar.com&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2009 Michal Cihar and other authors. License GPLv2: GNU GPL version 2 &lt;<a rel="nofollow" href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.html">http://www.gnu.org/licenses/old-licenses/gpl-2.0.html</a>&gt;<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>REPORTING BUGS</h2>
<p> Please report bugs to &lt;<a rel="nofollow" href="http://bugs.cihar.com">http://bugs.cihar.com</a>&gt;. </p>
<p> Before reporting a bug, please enable verbose logging in SMSD configuration: </p>
<p>&nbsp;<wbr>[gammu]<br />
&nbsp;<wbr>logformat&nbsp;<wbr>=&nbsp;<wbr>textall </p>
<p> and include this verbose log within bug report. </p>
<h2>Index</h2>
