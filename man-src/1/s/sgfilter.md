---
title: "sgfilter(1)"
name: "sgfilter"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sgfilter/"
description: "sgfilter – scan something for viruses/spams over sagator’s filterd() service"
---

<h2>NAME</h2>
<p> sgfilter &#8211; scan something for viruses/spams over sagator&#8217;s filterd() service</p>
<h2>SYNOPSIS</h2>
<p> <code>sgfilter</code> [&#8211;help] [&#8211;host hostname] [&#8211;port number] [&#8211;codes|-c] [&#8211;non-safe|-x] [filename]</p>
<h2>DESCRIPTION</h2>
<p> This command is a part of sagator. It can be used to scan emails for viruses/spams. It is usable for example for courier smtpd, but can be used also for procmail or other configurations.</p>
<h2>OPTIONS</h2>
<dl>
<dt>&#8211;help</dt>
<dd> Display a short help text.</dd>
<dt>&#8211;host hostname</dt>
<dd> Define a hostname of sagator&#8217;s filterd() service.</dd>
<dt>&#8211;port number</dt>
<dd> Define a port of sagator&#8217;s filterd() service.</dd>
<dt>&#8211;codes -c</dt>
<dd> Just check if the message is spam or not. Set exit code to 1, if message is a spam, 0 if not a spam or processing failure.</dd>
<dt>&#8211;non-safe -x</dt>
<dd> Turn off &quot;safe fallback&quot; error recovery, which passes through if an error occurs. Non safe processing returns an error code described in &quot;RETURN CODES&quot; section.</dd>
<dt>filename</dt>
<dd> Name of the file to open. If it is not defined, standard input is used.</dd></dl>
<h2>RETURN CODES</h2>
<dl>
<dt>0</dt>
<dd> Scanned email is clean (no virus and no spam has been found)</dd>
<dt>1</dt>
<dd> Scanned email is infected (virus or spam has been detected). Just error codes (&#8211;codes) option must be turned on to return this status.</dd>
<dt>64</dt>
<dd> An internal error occurred during scanning. Non safe processing must be turned on to return this status.</dd>
<dt>65</dt>
<dd> An error with communication to sgfilterd() service (service is not running?) Non safe processing must be turned on to return this status.</dd></dl>
<h2>EXAMPLES</h2>
<dl>
<dt>An procmailrc filter:</dt>
<dd>
<pre>
# filter through sagator
:0fw
|sgfilter
# move identified emails to quarantine
:0
* ^X-Sagator-Status: .
$HOME/mail/quarantine
</pre>
</dd><dt>An courier filter:</dt>
<dd> xfilter &quot;/usr/bin/sgfilter &#8211;host localhost &#8211;port 27&quot;</dd></dl>
<h2>AUTHOR</h2>
<p> Jan ONDREJ (SAL) &lt;ondrejj (at) salstar.sk&gt;</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-sgscan/">sgscan</a>(1), <a href="/docs/linux/man/8-sagator/">sagator</a>(8), <a href="/docs/linux/man/8-sqback/">sqback</a>(8) </p>
<h2>Index</h2>
