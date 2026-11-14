---
title: "papstatus(1)"
name: "papstatus"
section: "1"
letter: "p"
url: "/docs/linux/man/1-papstatus/"
description: "pap – client interface to remote printers using Printer Access Protocol"
---

<h2 class="name">NAME</h2>
<p> pap &#8211; client interface to remote printers using Printer Access Protocol </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>pap</code> [-A&nbsp;<wbr><i>address</i>] [-c] [-d] [-e] [-E] [-p&nbsp;<wbr><i>nbpname</i>] [-s&nbsp;<wbr><i>statusfile</i>] [-w] [-W] [<i>FILES</i>]</dl>
<h2>DESCRIPTION</h2>
<p> <code>pap</code></p>
<dd>is used to connect and send files to an AppleTalk connected printer using the Apple Printer Access Protocol (PAP). When <code>pap</code> starts execution, it tries to open a session with the printer using PAP, and then downloads the <i>files</i> to the printer. </p>
<p> If no <i>files</i> are given on the command line, <code>pap</code> begins reading from standard input. </p>
<p> If no printer is specified on the command line, <code>pap</code> looks for a file called <code>.paprc</code> in the current working directory and reads it to obtain the <i>nbpname</i> of a printer. Blank lines and lines that begin with a `<code>#</code>&#8216; are ignored. <i>type</i> and <i>zone</i> default to <code>LaserWriter</code> and the zone of the local host, respectively. </p>
<p> Note that <code>pap</code> is designed to be useful as a communication filter for sending <code><a href="/docs/linux/man/8-lpd/">lpd</a></code>(8) spooled print jobs to AppleTalk connected printers. See <code><a href="/docs/linux/man/8-psf/">psf</a></code>(8) for hints on how to use it this way.</p>
<h2>OPTIONS</h2>
<p> <code>-A </code><i>address</i></p>
<dl>
<dt>
<dd> Connect to the printer with Appletalk address <i>address</i> and do not consult the <code>.paprc</code> file to find a printer name. See <code><a href="/docs/linux/man/3-atalk_aton/">atalk_aton</a></code>(3) for the syntax of <i>address</i>.</dl>
<p> <code>-c</code></p>
<dl>
<dt>
<dd> Take cuts. The PAP protocol specified a simple queuing procedure, such that the clients tell the printer how long they have been waiting to print. This option causes <code>pap</code> to lie about how long it has been waiting.</dl>
<p> <code>-d</code></p>
<dl>
<dt>
<dd> Enable debug output.</dl>
<p> <code>-e</code></p>
<dl>
<dt>
<dd> Send any message from the printer to stderr instead of stdout. <code><a href="/docs/linux/man/8-psf/">psf</a></code>(8) invokes <code>pap</code> with this option.</dl>
<p> <code>-E</code></p>
<dl>
<dt>
<dd> Don&#8217;t wait for EOF from the printer. This option is useful for printers which don&#8217;t implement PAP correctly. In a correct implementation, the client side should wait for the printer to return EOF before closing the connection. Some clients don&#8217;t wait, and hence some printers have related bugs in their implementation.</dl>
<p> <code>-p</code> <i>nbpname</i></p>
<dl>
<dt>
<dd> Connect to the printer named <i>nbpname</i> and do not consult the <code>.paprc</code> file to find a printer name. See <code><a href="/docs/linux/man/3-nbp_name/">nbp_name</a></code>(3) for the syntax of <i>nbpname</i>.</dl>
<p> <code>-s</code> <i>statusfile</i></p>
<dl>
<dt>
<dd> Update the file called <i>statusfile</i> to contain the most recent status message from the printer. <code>pap</code> gets the status from the printer when it is waiting for the printer to process input. The <i>statusfile</i> will contain a single line terminated with a newline. This is useful when <code>pap</code> is invoked by <code><a href="/docs/linux/man/8-psf/">psf</a></code>(8) within <code>lpd</code>&#8216;s spool directory.</dl>
<p> <code>-w</code></p>
<dl>
<dt>
<dd> Wait for the printer status to contain the word &quot;waiting&quot; before sending the job. This is to defeat printer-side spool available on HP IV and V printers.</dl>
<p> <code>-W</code></p>
<dl>
<dt>
<dd> Wait for the printer status to contain the word &quot;idle&quot; before sending the job. This is to defeat printer-side spool available on HP IV and V printers.</dl>
<h2>FILES</h2>
<p> <code>.paprc</code></p>
<dl>
<dt>
<dd> file read to obtain printer name if not specified on command line</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-nbp_name/">nbp_name</a></code>(3), <code><a href="/docs/linux/man/3-atalk_aton/">atalk_aton</a></code>(3), <code><a href="/docs/linux/man/8-lpd/">lpd</a></code>(8), <code><a href="/docs/linux/man/8-psf/">psf</a></code>(8). </p>
<h2>Index</h2>
