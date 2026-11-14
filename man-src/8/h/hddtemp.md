---
title: "hddtemp(8)"
name: "hddtemp"
section: "8"
letter: "h"
url: "/docs/linux/man/8-hddtemp/"
description: "hddtemp – Utility to monitor hard drive temperature"
---

<p>hddtemp &#8211; Utility to monitor hard drive temperature</p>
<h2>Synopsis</h2>
<p><code>hddtemp</code> [<i>options</i>]<i> [type:]disk</i>&#8230;</p>
<h2>Description</h2>
<p><code>hddtemp </code> will give you the temperature of your hard drive by reading Self-Monitoring Analysis and Reporting Technology (S.M.A.R.T.) information on drives that support this feature. Only modern hard drives have a temperature sensor. hddtemp supports reading S.M.A.R.T. information from SCSI drives too. <code>hddtemp</code> can work as simple command line tool or as a daemon. You can specify one or more device drive path, where each path can be prefixed with a <code>type</code> like PATA, SATA or SCSI to force hddtemp too use one of these type (because detection can fail). </p>
<h2>Options</h2>
<p>The program follows the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). A summary of options is included below.</p>
<dl>
<dt><code>-b, &#8211;drivebase</code></p>
<dd>Display the database file that allows hddtemp to recognize a supported drive.</p>
<dt><code>-D, &#8211;debug</code></p>
<dd>Display various S.M.A.R.T. fields and their values. Useful for finding a value that seems to match the temperature and/or to send a report. (done for every drive supplied)</p>
<dt><code>-d, &#8211;daemon</code></p>
<dd>Execute hddtemp in TCP/IP daemon mode (port 7634 by default).</p>
<dt><code>-f, &#8211;file=</code><i>file</i></p>
<dd>Specify the database file to use.</p>
<dt><code>-F, &#8211;foreground</code></p>
<dd>Don&#8217;t fork into the background even in daemon mode. This is useful when running under a process supervisor.</p>
<dt><code>-l, &#8211;listen=</code><i>addr</i></p>
<dd>Listen on a specific address. <i>addr</i> is a string containing a host name or a numeric host address string. The numeric host address string is a dotted-decimal IPv4 address or an IPv6 hex address.</p>
<dt><code>-n, &#8211;numeric</code></p>
<dd>Print only the temperature (without the unit).</p>
<dt><code>-p, &#8211;port=</code><i>#</i></p>
<dd>Port number to listen to (in TCP/IP daemon mode).</p>
<dt><code>-s, &#8211;separator=</code><i>char</i></p>
<dd>Separator to use between fields (in TCP/IP daemon mode). The default separator is `|&#8217;.</p>
<dt><code>-S, &#8211;syslog=</code><i>s</i></p>
<dd>Switch to daemon mode and log temperatures to syslog every <i>s</i> seconds.</p>
<dt><code>-q, &#8211;quiet</code></p>
<dd>Don&#8217;t check if the drive is supported.</p>
<dt><code>-u, &#8211;unit=</code><i>C|F</i></p>
<dd>Force output temperature either in Celsius or Fahrenheit.</p>
<dt><code>-v, &#8211;version</code></p>
<dd>Display hddtemp version number.</p>
<dt><code>-w, &#8211;wake-up</code></p>
<dd>Wake-up the drive if needed (ATA drives only).</p>
<dt><code>-4</code></p>
<dd>Listen on IPv4 sockets only.</p>
<dt><code>-6</code></p>
<dd>Listen on IPv6 sockets only. </p>
</dl>
<h2>Drive Database</h2>
<p>If you know your drive has a temperature sensor but it is being reported unsupported, tell me which model and which manufacturer it is, and/or just add a new entry in /etc/hddtemp.db. Each line of hddtemp.db is either a comment, a blank line or a line containing:</p>
<dl>
<dt>&#8211; a regular expression that allow hddtemp to recognize a drive or a</p>
<dd>set of drives from its model name or from a generic model name,</p>
<dt>&#8211; a value (ATTRIBUTE_ID from S.M.A.R.T.),</p>
<dd>
<dt>&#8211; a C or an F to set the unit to Celsius or Fahrenheit,</p>
<dd>
<dt>&#8211; a description.</p>
<dd></dl>
<p> Feedback is welcome (see the REPORT section below).</p>
<h2>Tcp/Ip Daemon Mode</h2>
<p>Example of type forcing: </p>
<p> # hddtemp SATA:/dev/sda PATA:/dev/hda </p>
<p> To test <code>hddtemp</code> in daemon mode, start it like this: </p>
<p> # hddtemp -d /dev/hd[abcd] </p>
<p> and use <code>telnet</code> or <code>netcat</code> (which is known as <code>nc</code> on some systems) to get a reply: </p>
<p> # netcat localhost 7634 </p>
<p> The drive database is read only once at startup, so <code>hddtemp</code> must be restarted if the database is updated for the changes to take effect.</p>
<h2>Report</h2>
<p>As I receive a lot of reports, things must be clarified. When running hddtemp with debug options, hddtemp will show sort of a dump of S.M.A.R.T. data. Each field corresponds to an information field. The standard field for drive temperature is 194. But this is not always the case (mostly for older drives). Even if your drive has S.M.A.R.T. capabilities, it doesn&#8217;t necessarily mean that it can report its temperature. So, things must be determined through experimentation. </p>
<p> So, you can try to guess which field by is the good one by running hddtemp at regular intervals:</p>
<dl>
<dt>
&nbsp;&#8211; just after starting up your PC/server/station,</p>
<dd>
<dt>
&nbsp;&#8211; after opening a window&nbsp;(a physical window :),</p>
<dd>
<dt>
&nbsp;&#8211; after opening the case,</p>
<dd>
<dt>
&nbsp;&#8211; whatever you can think of&#8230;</p>
<dd></dl>
<p> and looking for a field&#8217;s value that would increase or decrease depending on what effect you want to induce. Be careful, fields 4, 9, and 12 are often reported to match a temperature field but after some investigation they do not. But fields 194 (which is the standard field for temperature) and 231 are good candidates. </p>
<p> Then, you can send me a report with outputs from `hddtemp &#8211;debug &#8230;&#8217;, `smartctl&#8217; or `hdparm -i &#8230;&#8217;, and/or add an entry in hddtemp.db yourself.</p>
<h2>Bugs</h2>
<p>If hddtemp crashes (yes, it might) for some unknown reasons, look for a file named hddtemp.backtrace.&lt;PID&gt;.XXXXXX (where XXXXXX is a random number generated at runtime) in /tmp. Then, you can then send me this file and the hddtemp binary. The backtrace functionality is currently supported on i386 architectures only. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-smartctl/">smartctl</a></code>(8), <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3), <code><a href="/docs/linux/man/8-syslogd/">syslogd</a></code>(8). </p>
<h2>Author</h2>
<p>Emmanuel Varagnat (hddtemp [at] guzu.net). </p>
<p> This manual page was originally written by Aurelien Jarno &lt;aurel32 [at] debian.org&gt;, for the Debian GNU/Linux system (but may be used by others).</p>
