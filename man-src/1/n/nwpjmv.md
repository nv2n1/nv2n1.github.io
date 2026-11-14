---
title: "nwpjmv(1)"
name: "nwpjmv"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nwpjmv/"
description: "nwpjvm – Move print job to Unix queue"
---

<h2>NAME</h2>
<p> nwpjvm &#8211; Move print job to Unix queue</p>
<h2>SYNOPSIS</h2>
<p> <code>nwpjmv</code> [ <code>-S</code> <i>server</i> ] [ <code>-h</code> ] [ <code>-U</code> <i>user name</i> ] [ <code>-P</code> <i>password</i> | <code>-n</code> ] [ <code>-C</code> ] [ <code>-q</code> <i>queue name</i> ] [ <code>-c</code> <i>command</i> ] [ <code>-j</code> <i>job number</i> ] [ <code>-d</code> ] </p>
<h2>DESCRIPTION</h2>
<p> <code>nwpjmv</code> is a program that connects to print queues on NetWare servers and moves a designated print job to a Unix queue. </p>
<h2>OPTIONS</h2>
<p> <code>-h</code></p>
<dl>
<dt>
<dd> <code>-h</code> is used to print out a short help text.</dl>
<p> <code>-S</code> <i>server</i></p>
<dl>
<dt>
<dd> <code>server</code> is the name of the server you want to use.</dl>
<p> <code>-U</code> <i>user</i></p>
<dl>
<dt>
<dd> <code>user</code> is the print server name at the server.</dl>
<p> <code>-P</code> <i>password</i></p>
<dl>
<dt>
<dd> <code>password</code> is the password to use for the print server at the server. If neither <code>-n</code> nor <code>-P</code> are given, and the user has no open connection to the server, pserver prompts for a password.</dl>
<p> <code>-n</code></p>
<dl>
<dt>
<dd> <code>-n</code> should be given if the print server does not require a password.</dl>
<p> <code>-C</code></p>
<dl>
<dt>
<dd> By default, passwords are converted to uppercase before they are sent to the server, because most servers require this. You can turn off this conversion by <code>-C.</code></dl>
<p> <code>-q</code> <i>queue name</i></p>
<dl>
<dt>
<dd> <code>queue name </code> is the name of the print queue you want to service.</dl>
<p> <code>-c</code> <i>command</i></p>
<dl>
<dt>
<dd> nwpjmv removes the designated job from the Novell queue and feeds the job file to stdin. <i>command</i> is the printing command that is executed for each job. The default command is &#8216;lpr&#8217;. </p>
<p> You can insert several flags into the command, preceded by %. These are replaced with values retrieved from the queue structure for the print job. </p>
<p> %u: This field will be replaced by the name of the user who posted this print job. </p>
<p> %d: This field will be replaced by the job description field of this print job.</dl>
<p> <code>-j</code> <i>job number</i></p>
<dl>
<dt>
<dd> This designates the ID number of the print job to be moved.</dl>
<p> <code>-d</code> causes extra error messages to be logged. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-nwclient/">nwclient</a>(5), <a href="/docs/linux/man/1-slist/">slist</a>(1), <a href="/docs/linux/man/1-pqlist/">pqlist</a>(1), <a href="/docs/linux/man/8-ncpmount/">ncpmount</a>(8), <a href="/docs/linux/man/8-ncpumount/">ncpumount</a>(8), <a href="/docs/linux/man/1-pserver/">pserver</a>(1)</code> </p>
<h2>CREDITS</h2>
<p> nwpjmv was written by Bruno Browning (bruno [at] lss.wisc.edu) based on pserver by Volker Lendecke (lendecke [at] math.uni-goettingen.de) </p>
<h2>Index</h2>
