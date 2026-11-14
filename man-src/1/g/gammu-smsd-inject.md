---
title: "gammu-smsd-inject(1)"
name: "gammu-smsd-inject"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gammu-smsd-inject/"
description: "gammu-smsd-inject – Inject messages into queue of SMS daemon for Gammu"
---

<h2>NAME</h2>
<p> gammu-smsd-inject &#8211; Inject messages into queue of SMS daemon for Gammu</p>
<h2>SYNOPSIS</h2>
<p> <code>gammu-smsd-inject</code> [<i>OPTION</i>]&#8230; MESSAGETYPE RECIPIENT [<i>MESSAGE_PARAMETER</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>gammu-smsd-inject</code> command. </p>
<p> <code>gammu-smsd-inject</code> is a program that enqueues message in Gammu SMS daemon, which will be later sent by the deamon using connected GSM modem. </p>
<p> Support for this program depends on features available in currently used SMSD service backend, currently only files (<a href="/docs/linux/man/7-gammu-smsd-files/">gammu-smsd-files</a>(7)) does not support this feature. </p>
<p> Program accepts following options (please note that long options might be not accepted on some platforms):</p>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Shows help.</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> Shows version information and compiled in features.</p>
<dt><code>-c</code>, <code>&#8211;config</code>=<i>file</i></p>
<dd> Configuration file to use, default is /etc/gammu-smsdrc, on Windows there is no default and configuration file path has to be always specified.</dl>
<p> For description of message types and their parameters, please check <a href="/docs/linux/man/1-gammu/">gammu</a>(1). The options are identical to ones you can use for gammu sendsms. </p>
<h2>EXAMPLE</h2>
<p> To check it out, you need to have configuration file for SMSD, see <a href="/docs/linux/man/5-gammu-smsdrc/">gammu-smsdrc</a>(5) for more details about it. </p>
<dl>
<dt>Inject text message up to standard 160 chars:</p>
<dd>
<p> echo &quot;All your base are belong to us&quot; | gammu-smsd-inject TEXT 123456 </p>
<p> or </p>
<p> gammu-smsd-inject TEXT 123456 -text &quot;All your base are belong to us&quot; </p>
<dt>Inject long text message:</p>
<dd>
<p> echo &quot;All your base are belong to us&quot; | gammu-smsd-inject TEXT 123456 -len 400 </p>
<p> or </p>
<p> gammu-smsd-inject TEXT 123456 -len 400 -text &quot;All your base are belong to us&quot; </p>
<p> or </p>
<p> gammu-smsd-inject EMS 123456 -text &quot;All your base are belong to us&quot; </p>
<dt>Inject some funky message with predefined sound and animation from 2 bitmaps:</p>
<dd>
<p> gammu-smsd-inject EMS 123456 -text &quot;Greetings&quot; -defsound 1 -text &quot;from Gammu&quot; -tone10 axelf.txt -animation 2 file1.bmp file2.bmp </p>
<dt>Inject protected message with ringtone:</p>
<dd>
<p> gammu-smsd-inject EMS 123456 -protected 2 -variablebitmaplong ala.bmp -toneSElong axelf.txt -toneSE ring.txt </p>
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
<p>&nbsp;<wbr>[smsd]<br />
&nbsp;<wbr>debuglevel&nbsp;<wbr>=&nbsp;<wbr>255<br />
&nbsp;<wbr>logfile&nbsp;<wbr>=&nbsp;<wbr>smsd.log </p>
<p> and include this verbose log within bug report. </p>
<h2>Index</h2>
