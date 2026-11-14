---
title: "mlmmj-maintd(1)"
name: "mlmmj-maintd"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mlmmj-maintd/"
description: "mlmmj-maintd – maintenance for mlmmj maintained lists"
---

<h2>NAME</h2>
<p> mlmmj-maintd &#8211; maintenance for mlmmj maintained lists</p>
<h2>SYNOPSIS</h2>
<p> <code>mlmmj-maintd</code> [<i>-F</i>] <i>[-d</i> | <i>-L</i>] /path/to/dir</p>
<dl>
<dt> <code>-d</code>: Full path to directory with lists</p>
<dt> <code>-L</code>: Full path to list directory</p>
<dt> <code>-F</code>: Don&#8217;t fork, performing one maintenance run only.</dl>
<h2>DESCRIPTION</h2>
<dd>This is the program doing the maintenance for an mlmmj based mailing list. It will unsubscribe people who have bounced for long enough, send out bounce probes, resend mails that couldn&#8217;t be delivered to relayhost, clean out stale requests for e.g. subscription, resend list mails and clean up leftover files etc. </p>
<p> If a directory containing several lists exists, the <code>-d</code> can be used to specify this, making mlmmj-maintd perform a maintenance run in every listdir below the specified one. </p>
<p> Only either <code>-d</code> or <code>-L</code> can be specified at the same time. </p>
<p> It will run as a daemon, unless the <code>-F</code> switch is specified, in which case it just runs once. The <code>-F</code> option should be used when one wants to avoid running another daemon, and use e.g. cron to control it instead. In case cron is used, mlmmj-maintd should be run every 2 hours or so. An example crontab entry: </p>
<p> 0 */2 * * * /usr/bin/mlmmj-maintd -F -L /path/to/list</p>
<h2>AUTHORS</h2>
<p> This manual page was written by the following persons:</p>
<dl>
<dt>
<dd>S&oslash;ren Boll Overgaard &lt;boll [at] debian.org&gt; (based on html2man output)</p>
<dt>
<dd>Mads Martin J&oslash;rgensen &lt;mmj [at] mmj.dk&gt; </p>
</dl>
<h2>Index</h2>
