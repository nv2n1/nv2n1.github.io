---
title: "faxrunq(1)"
name: "faxrunq"
section: "1"
letter: "f"
url: "/docs/linux/man/1-faxrunq/"
description: "faxrunq – send fax jobs queued by"
---

<h2 class="name">NAME</h2>
<p> faxrunq &#8211; send fax jobs queued by </p>
<p><a href="/docs/linux/man/1-faxspool/">faxspool</a>(1)</p>
<h2>SYNOPSIS</h2>
<p> <code>faxrunq</code></p>
<h2>DESCRIPTION</h2>
<p> Run the fax queue set up by <a href="/docs/linux/man/1-faxspool/">faxspool</a>(1), try to send all faxes, record result, remove job and send notify mails. </p>
<p> <i>faxrunq </i> looks for all the jobs queued by <a href="/docs/linux/man/1-faxspool/">faxspool</a>(1) to /var/spool/fax/outgoing/*. For each job in the queue, faxrunq tries to send it, using <a href="/docs/linux/man/8-sendfax/">sendfax</a>(8). </p>
<p> If the send succeeds, the job is removed from the queue, and a &quot;success&quot; mail is sent to the originator of the spooled job. </p>
<p> If the send fails, it&#8217;s logged, and faxrunq proceeds to the next job. If the job fails five times &quot;fatally&quot;, that is, not with a locked or engaged line, but with &quot;NO CARRIER&quot; (no fax machine, or line noise), the job is suspended, and the requestor gets a mail, telling him so. </p>
<p> <i>faxrunq</i> can be run from the command line (but make sure the user doing this has write access to the modem device and to the fax queue, that is, usually this should be done by &quot;fax&quot; or &quot;root&quot;). In a production environment, it&#8217;s more useful to start <i>faxrunq</i> from <i><a href="/docs/linux/man/8-cron/">cron</a>(8)</i> in regular intervals, like &quot;run it every 5 minutes&quot;. See the <i><a href="/docs/linux/man/8-cron/">cron</a>(8)</i> and/or <i><a href="/docs/linux/man/1-crontab/">crontab</a>(1)</i> man pages for this (which man page exists depends on your system). </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-q</code></p>
<dd> Tells <i>faxrunq</i> to be quiet, that is, suppress all status messages. Error messages will still be printed. </p>
</dl>
<h2>FILES</h2>
<dl>
<dt><code>/var/spool/fax/outgoing/stop</code></p>
<dd> if this file exists, <i>faxrunq </i> (and faxrunqd) will do nothing. You can use this to stop queue processing while testing something, or if you know that the modem(s) are unavailable and do not want to run into oany error messages, etc. </p>
<dt><code>/var/spool/fax/outgoing/faxqueue_done</code></p>
<dd> Every time <i>faxrunq</i> (or faxrunqd) run the fax queue, a time stamp is written into that file. It is used by <i>faxspool</i> to display a warning if the queue hasn&#8217;t been run recently (so faxes may get stuck). </p>
</dl>
<h2>CONFIGURATION FILE</h2>
<p> Some aspects of the behaviour of <i>faxrunq</i> can be controlled by a configuration file, /etc/mgetty+sendfax/faxrunq.config. In this file, you can use the following options:</p>
<dl>
<dt><code>success-send-mail [y/n]</code></p>
<dd> A boolean parameter that controls whether a mail will be sent after successful completition of the fax job. </p>
<dt><code>failure-send-mail [y/n]</code></p>
<dd> A boolean parameter that controls whether a mail will be sent after the fax job has failed more than the maximum number of times. </p>
<dt><code>success-call-program &lt;name&gt;</code></p>
<dd> Here, you can specify a program that will be run when the fax has been successfully sent. It will be passed two command line parameters. The first is the full path to the fax JOB file (see <a href="/docs/linux/man/5-faxq/">faxq</a>(5)), the second is the last exit code from <i>sendfax</i> (for success-call-program, this is always &quot;0&quot;). </p>
<dt><code>failure-call-program &lt;name&gt;</code></p>
<dd> Similar to the &quot;success-call-program&quot;, this program will be run when the fax has been failed too often and <i>faxrunq</i> gives up. This script could, for example, print out the fax on a printer so that it can be sent manually on a paper fax machine. </p>
<dt><code>maxfail-costly &lt;n&gt;</code></p>
<dd> This specifies the number of times that a fax may fail &quot;fatally&quot;, that is, causing telephone costs (explained above). The default value is 5. </p>
<dt><code>maxfail-total &lt;m&gt;</code></p>
<dd> This is the absolute maximum number of times that <i>faxrunq</i> will try to send any given fax. The default value is 10. (Right now, it&#8217;s not yet implemented). </p>
<dt><code>delete-sent-jobs [y/n]</code></p>
<dd> Determines whether <i>faxrunq</i> should delete jobs after sending, or leave them in the fax queue (while moving the &quot;JOB&quot; file to &quot;JOB.done&quot;) so that they can be seen at by &quot;faxq -o&quot;. The default value is &quot;do not delete sent faxes&quot;. </p>
<dt><code>acct-log &lt;path&gt;</code></p>
<dd> Specifies where <i>faxrunq</i> should protocol success and failure of each try to send a fax job. The default location is /var/spool/fax/outgoing/acct.log. </p>
<p> There are some other options that are allowed, but ignored. These are: <i>max-modems,</i> and <i>faxrunqd-log.</i> </p>
<p> They are used by <a href="/docs/linux/man/8-faxrunqd/">faxrunqd</a>(8) (which reads the same config file, but has more options). </p>
</dl>
<h2>BUGS</h2>
<p> <i>faxrunq</i> doesn&#8217;t handle proper time scheduling yet </p>
<p> Don&#8217;t use <i>faxrunq</i> if you have malevolent users with access to the fax spool. It doesn&#8217;t handle all cases of file movement tricks correctly. Use <i><a href="/docs/linux/man/8-faxrunqd/">faxrunqd</a>(8)</i> instead, which does it correctly (this point is mostly moot if the fax queue is set up correctly &#8211; that is, owned by &#8216;fax&#8217;, mode 755, and <a href="/docs/linux/man/1-faxrunq/">faxrunq</a>(1) is also run as user &#8216;fax&#8217;). </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-faxspool/">faxspool</a>(1), <a href="/docs/linux/man/8-sendfax/">sendfax</a>(8), <a href="/docs/linux/man/1-faxq/">faxq</a>(1), <a href="/docs/linux/man/5-faxqueue/">faxqueue</a>(5), <a href="/docs/linux/man/8-faxrunqd/">faxrunqd</a>(8)</p>
<h2>AUTHOR</h2>
<p> <i>faxrunq</i> is Copyright (C) 1993-2002 by Gert Doering, &lt;gert [at] greenie.muc.de&gt;. </p>
<h2>Index</h2>
