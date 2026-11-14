---
title: "innwatch(8)"
name: "innwatch"
section: "8"
letter: "i"
url: "/docs/linux/man/8-innwatch/"
description: "innwatch – Monitor the state of INN and the system"
---

<p>innwatch &#8211; Monitor the state of INN and the system</p>
<h2>Synopsis</h2>
<p><code>innwatch</code> [<code>-f</code> <i>ctlfile</i>] [<code>-i</code> <i>seconds</i>] [<code>-l</code> <i>logfile</i>] [<code>-t</code> <i>seconds</i>]</p>
<h2>Description</h2>
<p><code>innwatch</code> is normally started by <code>rc.news</code>. Every <i>innwatchsleeptime</i> seconds, as set in <i>inn.conf</i>, it examines the load average, and the number of free blocks and inodes on the spool partition, as described by its control file, <i>innwatch.ctl</i> in <i>pathetc</i>. </p>
<p> If the load gets too high, or the disk gets too full, it throttles the server. When the condition restores, it unblocks the server. In addition, on each pass through the loop, it will check the logfile <i>pathlog</i>/news.crit to see if it has been modified, and send mail to the news administrator if so. </p>
<p> Upon receipt of an interrupt signal (<font SIZE="-1">SIGINT</font>), <code>innwatch</code> will report its status in the file <i>innwatch.status</i> in <i>pathrun</i>.</p>
<h2>Options</h2>
<dl>
<dt><code>-f</code> <i>file</i></p>
<dd>Specify the control file to use, other than the default of <i>innwatch.ctl</i> in <i>pathetc</i>.</p>
<dt><code>-i</code> <i>seconds</i></p>
<dd>With this option, <code>innwatch</code> has an initial sleep of <i>seconds</i> seconds at startup. This is useful when <code>innwatch</code> is started at the same time as <font SIZE="-1">INN</font>, so that it can wait a little before beginning performing its checks.</p>
<dt><code>-l</code> <i>logfile</i></p>
<dd>Specify a log file to watch, other than the default of <i>news.crit</i>.</p>
<dt><code>-t</code> <i>seconds</i></p>
<dd>Specify the period in seconds between checks, to override the value set in <i>inn.conf</i>.</dl>
<h2>History</h2>
<p>Written by Mike Cooper &lt;mcooper [at] usc.edu&gt;, with modifications by &lt;kre [at] munnari.oz.au&gt;, Steve Groom &lt;stevo [at] elroy.jpl.nasa.gov&gt; and Christophe Wolfhugel &lt;wolf [at] pasteur.fr&gt;. Converted to <font SIZE="-1">POD</font> by Julien Elie. </p>
<p> <tt>$Id:</tt> innwatch.pod 9726 2014-09-24 18:05:04Z iulius $</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/5-inn-conf/">inn.conf</a></i>(5), <i><a href="/docs/linux/man/5-innwatch-ctl/">innwatch.ctl</a></i>(5), <i><a href="/docs/linux/man/5-newslog/">newslog</a></i>(5), <i><a href="/docs/linux/man/8-rc-news/">rc.news</a></i>(8). </p>
