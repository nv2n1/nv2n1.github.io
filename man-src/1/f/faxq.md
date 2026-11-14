---
title: "faxq(1)"
name: "faxq"
section: "1"
letter: "f"
url: "/docs/linux/man/1-faxq/"
description: "faxq – display fax jobs queued by"
---

<h2 class="name">NAME</h2>
<p> faxq &#8211; display fax jobs queued by </p>
<p><a href="/docs/linux/man/1-faxspool/">faxspool</a>(1)</p>
<h2>SYNOPSIS</h2>
<p> <code>faxq</code> [<code>&lt;command&gt;</code>] [<code>-osa</code>] [<code>-v</code>] [<code>-r</code>] [<code>-P</code>&lt;job&gt;<code>&lt;prio&gt;</code>]</p>
<h2>DESCRIPTION</h2>
<p> Display the fax queue set up by <a href="/docs/linux/man/1-faxspool/">faxspool</a>(1). </p>
<p> <i>faxq </i> looks for all the jobs queued by <a href="/docs/linux/man/1-faxspool/">faxspool</a>(1) to /var/spool/fax/outgoing/*. For each job in the queue, <i>faxq</i> displays some status informations about it. If no options are specified, one line per queued fax job is printed, displaying the job number, sender, number of pages and target fax number. </p>
<h2>COMMANDS</h2>
<p> <code>faxq stop</code> stops the fax queue processing by creating the file /var/spool/fax/outgoing/stop. This command works only if you have write access to the spool directory. Depending on local setup, this means &#8220;root only&#8221; or &#8220;fax administrator group&#8221;. If you don&#8217;t have write access, an error message is printed. </p>
<p> <code>faxq start</code> re-starts a previously stopped fax queue, by removing the &#8220;stop&#8221; file. As for <i>faxq stop</i> this only works if you have write access. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-v</code></p>
<dd> Tells <i>faxq</i> to print a more verbose report for each job (multiple lines).</p>
<dt><code>-o</code></p>
<dd> Show old jobs, already sent but still in the queue directory, too.</p>
<dt><code>-s</code></p>
<dd> Show suspended jobs (stopped because of too many fatal errors during sending). You can restart those jobs with <i>faxq -r</i></p>
<dt><code>-a</code></p>
<dd> Show all jobs (active, old, suspended).</p>
<dt><code>-r</code></p>
<dd> Restart suspended jobs. Every suspended job in the queue (that you have write permissions for) will be requeued. Use <i>faxrm</i> to delete jobs that you do not want to be sent!</p>
<dt><code>-P &lt;job&gt; &lt;prio&gt;</code></p>
<dd> Change the priority of fax job &lt;job&gt; to &lt;prio&gt;. Example: &quot;faxq -P F000247 3&quot;. </p>
</dl>
<h2>BUGS</h2>
<p> <i>faxq</i> doesn&#8217;t handle time scheduling yet. </p>
<p> <i>faxq -P</i> is currently broken (needs re-implementing with faxq-helper). </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-faxrunq/">faxrunq</a>(1), <a href="/docs/linux/man/1-faxspool/">faxspool</a>(1), <a href="/docs/linux/man/1-faxrm/">faxrm</a>(1), <a href="/docs/linux/man/5-faxqueue/">faxqueue</a>(5)</p>
<h2>AUTHOR</h2>
<p> <i>faxq</i> is Copyright (C) 1993 by Gert Doering, &lt;gert [at] greenie.muc.de&gt;. </p>
<h2>Index</h2>
