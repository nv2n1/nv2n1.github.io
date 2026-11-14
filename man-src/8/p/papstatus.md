---
title: "papstatus(8)"
name: "papstatus"
section: "8"
letter: "p"
url: "/docs/linux/man/8-papstatus/"
description: "papstatus – get the status of an AppleTalk-connected printer"
---

<p>papstatus &#8211; get the status of an AppleTalk-connected printer</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>/usr/sbin/papstatus</code> [-d] [-p&nbsp;<wbr><i>printer</i>] [<i>retrytime</i>]</dl>
<h2>Description</h2>
<p><code>papstatus</code></p>
<dd>is used to obtain the current status message from an AppleTalk connected printer. It uses the Printer Access Protocol (PAP) to obtain the status information. </p>
<p> If no printer is specified on the command line, <code>papstatus</code> looks for a file called <code>.paprc</code> in the current directory and reads it to obtain the name of a printer. The <code>.paprc</code> file should contain a single line of the form <i>object</i><code>:</code><i>type</i><code>@</code><i>zone</i> where each of <i>object</i>, <code>:</code><i>type</i><code>,</code> and <code>@</code><i>zone</i> are optional. <i>type</i> and <i>zone</i> must be proceeded by `<code>:</code>&#8216; and `<code>@</code>&#8216; respectively. Blank lines and lines the begin with a `<code>#</code>&#8216; are ignored. <i>type</i> and <i>zone</i> default to <code>LaserWriter</code> and the zone of the local host, respectively.</p>
<h2>Options</h2>
<p><code>-d</code></p>
<dl>
<dd>Turns on a debugging mode that prints some extra information to standard error.</dl>
<p> <code>-p</code> <i>printer</i></p>
<dl>
<dd>Get status from <i>printer</i> (do not consult any <code>.paprc</code> files to find a printer name). The syntax for <i>printer</i> is the same as discussed above for the <code>.paprc</code> file.</dl>
<p> <i>retrytime</i></p>
<dl>
<dd>Normally, <code>papstatus</code> only gets the status from the printer once. If <i>retrytime</i> is specified, the status is obtained repeatedly, with a sleep of <i>retrytime</i> seconds between inquiring the printer.</dl>
<h2>Files</h2>
<p><code>.paprc</code></p>
<dl>
<dd>file that contains printer name</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-nbp/">nbp</a></code>(1), <code><a href="/docs/linux/man/1-pap/">pap</a></code>(1) </p>
