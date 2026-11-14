---
title: "gammu-smsd(1)"
name: "gammu-smsd"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gammu-smsd/"
description: "gammu-smsd – SMS daemon for Gammu"
---

<h2>NAME</h2>
<p> gammu-smsd &#8211; SMS daemon for Gammu</p>
<h2>SYNOPSIS</h2>
<p> <code>gammu-smsd</code> [<i>OPTION</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>gammu-smsd</code> command. </p>
<p> <code>gammu-smsd</code> is a program that periodically scans GSM modem for received messages, stores them in defined storage and also sends messages enqueued in this storage. </p>
<p> The daemon can reload configuration file after sending hangup signal (SIGHUP) and properly terminates itself on SIGINT and SIGTERM. </p>
<p> Program accepts following options (please note that long options might be not accepted on some platforms):</p>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Shows help.</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> Shows version information and compiled in features.</p>
<dt><code>-c</code>, <code>&#8211;config</code>=<i>file</i></p>
<dd> Configuration file to use, default is /etc/gammu-smsdrc, on Windows there is no default and configuration file path has to be always specified.</p>
<dt><code>-p</code>, <code>&#8211;pid</code>=<i>file</i></p>
<dd> Lock file for storing pid, empty for no locking. Not supported on Windows.</p>
<dt><code>-U</code>, <code>&#8211;user</code>=<i>user</i></p>
<dd> Drop daemon privileges to chosed user after starting.</p>
<dt><code>-G</code>, <code>&#8211;group</code>=<i>group</i></p>
<dd> Drop daemon privileges to chosen group after starting.</p>
<dt><code>-d</code>, <code>&#8211;daemon</code></p>
<dd> Daemonize program on startup. Not supported on Windows.</p>
<dt><code>-i</code>, <code>&#8211;install-service</code></p>
<dd> Installs SMSD as a Windows service.</p>
<dt><code>-u</code>, <code>&#8211;uninstall-service</code></p>
<dd> Uninstalls SMSD as a Windows service.</p>
<dt><code>-s</code>, <code>&#8211;start-service</code></p>
<dd> Starts SMSD Windows service.</p>
<dt><code>-k</code>, <code>&#8211;stop-service</code></p>
<dd> Stops SMSD Windows service.</p>
<dt><code>-X</code>, <code>&#8211;suicide</code>=<i>seconds</i></p>
<dd> Kills itself after number of seconds.</p>
<dt><code>-S</code>, <code>&#8211;run-service</code></p>
<dd> Runs pogram as SMSD Windows service. This should not be used manually, but only Windows Service manager should use this command.</p>
<dt><code>-n</code>, <code>&#8211;service-name</code>=<i>name</i></p>
<dd> Defines name of a Windows service. Each service requires an unique name, so if you want to run several SMSD instances, you have to name each service differently. Default is &quot;GammuSMSD&quot;. </p>
</dl>
<h2>EXAMPLE</h2>
<h3>Linux/Unix Examples</h3>
<dl>
<dt>Start SMSD as a deamon on Linux:</p>
<dd>
<p> gammu-smsd &#8211;config /etc/gammu-smsdrc &#8211;pid /var/run/gammu-smsd.pid &#8211;daemon </p>
<dt>Start SMSD as a deamon on Linux with reduced privileges:</p>
<dd>
<p> gammu-smsd &#8211;config /etc/gammu-smsdrc &#8211;pid /var/run/gammu-smsd.pid &#8211;daemon &#8211;user gammu &#8211;group gammu </p>
</dl>
<h3>Windows Service Examples</h3>
<dl>
<dt>Install Gammu SMSD Windows service:</p>
<dd>
<p> gammu-smsd.exe -c c:\Gammu\smsdrc -i </p>
<dt>Install two instances of SMSD Windows service:</p>
<dd>
<p> gammu-smsd.exe -c c:\Gammu\smsdrc-1 -n Gammu-first-phone -i </p>
<p> gammu-smsd.exe -c c:\Gammu\smsdrc-2 -n Gammu-second-phone -i </p>
<dt>To uninstall a Windows service:</p>
<dd>
<p> gammu-smsd.exe -u </p>
</dl>
<h3>Troubleshooting Windows Service</h3>
<p> If Gammu fails to start as a Windows service (you will usually get &quot;Error 1053: The service did not respond to the start or control request in a timely fashion&quot;), first check your SMSD logs. If they do not contain any useful hint, try starting SMSD manually with exactly same parameters as you installed the service (without -i), for example: </p>
<p>&nbsp;<wbr>gammu-smsd.exe -c smsdrc </p>
<p> You now should be able to get errors from SMSD even if it fails to start as a service. </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/5-gammu-smsdrc/">gammu-smsdrc</a>(5), <a href="/docs/linux/man/1-gammu/">gammu</a>(1), <a href="/docs/linux/man/1-gammu-smsd-inject/">gammu-smsd-inject</a>(1), <a href="/docs/linux/man/1-gammu-smsd-monitor/">gammu-smsd-monitor</a>(1) </p>
<p> <a href="/docs/linux/man/7-gammu-smsd-files/">gammu-smsd-files</a>(7), <a href="/docs/linux/man/7-gammu-smsd-mysql/">gammu-smsd-mysql</a>(7), <a href="/docs/linux/man/7-gammu-smsd-pgsql/">gammu-smsd-pgsql</a>(7), <a href="/docs/linux/man/7-gammu-smsd-dbi/">gammu-smsd-dbi</a>(7), <a href="/docs/linux/man/7-gammu-smsd-tables/">gammu-smsd-tables</a>(7)</p>
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
<p>&nbsp;<wbr>[smsd]<br />
&nbsp;<wbr>debuglevel&nbsp;<wbr>=&nbsp;<wbr>255<br />
&nbsp;<wbr>logfile&nbsp;<wbr>=&nbsp;<wbr>smsd.log </p>
<p> and include this verbose log within bug report. </p>
<h2>Index</h2>
