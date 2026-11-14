---
title: "pserver(1)"
name: "pserver"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pserver/"
description: "pserver – NetWare print server"
---

<h2>NAME</h2>
<p> pserver &#8211; NetWare print server</p>
<h2>SYNOPSIS</h2>
<p> <code>pserver</code> [ <code>-S</code> <i>server</i> ] [ <code>-h</code> ] [ <code>-U</code> <i>user name</i> ] [ <code>-P</code> <i>password</i> | <code>-n</code> ] [ <code>-C</code> ] [ <code>-q</code> <i>queue name</i> ] [ <code>-c</code> <i>command</i> ] [ <code>-j</code> <i>job type</i> ] [ <code>-t</code> <i>timeout</i> ] [ <code>-d</code> ] </p>
<h2>DESCRIPTION</h2>
<p> <code>pserver</code> is a program that connects to print queues on NetWare servers and feeds incoming print jobs to the Linux printing system. </p>
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
<dd> When a job is received from the print queue, pserver forks off a new process, and feeds the job file to stdin. <i>command</i> is the printing command that is executed for each job. The default command is &#8216;lpr&#8217;. </p>
<p> You can insert several flags into the command, preceded by %. These are replaced with values retrieved from the queue structure for the print job. </p>
<p> %u: This field will be replaced by the name of the user who posted this print job. </p>
<p> %d: This field will be replaced by the job description field of this print job.</dl>
<p> <code>-j</code> <i>job type</i></p>
<dl>
<dt>
<dd> Each job in a NetWare print queue has a job type. For print jobs, this corresponds to the number of the form the job should be printed on. You can tell pserver that it should only receive jobs for one specific form from the queue. The default is -1, which means that everything is received.</dl>
<p> <code>-t </code> <i>timeout</i></p>
<dl>
<dt>
<dd> Pserver is not informed by NetWare servers when new jobs arrive. So a polling scheme has to be used. When there are no jobs to service, <i>timeout</i> tells pserver how long to wait between two requests. The default is 30 seconds. When a job is finished, pserver asks the NetWare server immediately for a new job, and does not wait <i>timeout</i> seconds.</dl>
<p> <code>-d</code></p>
<dl>
<dt>
<dd> Normally, pserver daemonizes itself. <code>-d</code> tells it not to do so. This is useful if you want to see the diagnostic messages that are printed when a error occurs.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-nwclient/">nwclient</a>(5), <a href="/docs/linux/man/1-slist/">slist</a>(1), <a href="/docs/linux/man/1-pqlist/">pqlist</a>(1), <a href="/docs/linux/man/8-ncpmount/">ncpmount</a>(8), <a href="/docs/linux/man/8-ncpumount/">ncpumount</a>(8)</code> </p>
<h2>CREDITS</h2>
<p> pserver was written by Volker Lendecke (lendecke [at] math.uni-goettingen.de) </p>
<h2>Index</h2>
