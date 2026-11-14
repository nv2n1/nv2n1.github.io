---
title: "runscript(1)"
name: "runscript"
section: "1"
letter: "r"
url: "/docs/linux/man/1-runscript/"
description: "runscript – script interpreter for minicom"
---

<h2>NAME</h2>
<p> runscript &#8211; script interpreter for minicom</p>
<h2>SYNOPSIS</h2>
<p> <code>runscript</code> scriptname [logfile [homedir]]</p>
<h2>DESCRIPTION</h2>
<p> <code>runscript</code> is a simple script interpreter that can be called from within the minicom communications program to automate tasks like logging in to a Unix system or your favorite BBS.</p>
<h2>INVOCATION</h2>
<p> The program expects a script name and optionally a filename and the user&#8217;s home directory as arguments, and it expects that it&#8217;s input and output are connected to the &quot;remote end&quot;, the system you are connecting to. All messages from <code>runscript</code> meant for the local screen are directed to the <code>stderr</code> output. All this is automatically taken care of if you run it from <code>minicom</code>. The logfile and home directory parameters are only used to tell the log command the name of the logfile and where to write it. If the homedir is omitted, runscript uses the directory found in the $HOME environment variable. If also the logfile name is omitted, the log commands are ignored.</p>
<h2>KEYWORDS</h2>
<dl>
<dt>Runscript recognizes the following commands:</p>
<dd>
<dl>
<dt>
<dd>
<pre>
expect   send     goto     gosub    return   !
exit     print    set      inc      dec      if
timeout  verbose  sleep    break    call     log
</pre>
</dl>
</dl>
<h2>OVERVIEW OF KEYWORDS</h2>
<dl>
<dt><code>send &lt;string&gt;</code></p>
<dd> &lt;string&gt; is sent to the modem. It is followed by a &#8216;&#8217;. &lt;string&gt; can be:<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211; regular text, e.g.&nbsp;<wbr>&#8216;send hello&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211; text enclosed in quotes, e.g.&nbsp;<wbr>&#8216;send&nbsp;<wbr>&quot;hello world&quot;&#8217;</p>
<dt>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Within&nbsp;<wbr>&lt;string&gt;&nbsp;<wbr>the following sequences are recognized:</p>
<dd>
&nbsp;<wbr>
 &#8211; newline<br />
&nbsp;<wbr> &#8211; carriage return<br />
&nbsp;<wbr> &#8211; bell<br />
&nbsp;<wbr> &#8211; backspace<br />
&nbsp;<wbr>
