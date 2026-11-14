---
title: "atd(8)"
name: "atd"
section: "8"
letter: "a"
url: "/docs/linux/man/8-atd/"
description: "atd – run jobs queued for later execution"
---

<p>atd &#8211; run jobs queued for later execution</p>
<h2>Synopsis</h2>
<p><code>atd</code> [<code>-l</code> <i>load_avg</i>] [<code>-b</code> <i>batch_interval</i>] [<code>-d</code>] [<code>-f</code>] [<code>-s</code>]</p>
<h2>Description</h2>
<p><code>atd</code> runs jobs queued by <code><a href="/docs/linux/man/1-at/">at</a>(1)</code>. </p>
<h2>Options</h2>
<dl>
<dt><code>-l</code></p>
<dd>Specifies a limiting load factor, over which batch jobs should not be run, instead of the compile-time choice of 0.8. For an SMP system with <i>n</i> CPUs, you will probably want to set this higher than <i>n-1.</i></p>
<dt><code>-b</code></p>
<dd>Specify the minimum interval in seconds between the start of two batch jobs (60 default).</p>
<dt><code>-d</code></p>
<dd>Debug; print error messages to standard error instead of using <code><a href="/docs/linux/man/3-syslog/">syslog</a>(3)</code>. This option also implies <code>-f</code>.</p>
<dt><code>-f</code></p>
<dd>Run <code>atd</code> in the foreground.</p>
<dt><code>-s</code></p>
<dd>Process the at/batch queue only once. This is primarily of use for compatibility with old versions of <code>at</code>; <code>atd -s</code> is equivalent to the old <code>atrun</code> command.</dl>
<h2>Warning</h2>
<p><code>atd</code> won&#8217;t work if its spool directory is mounted via NFS even if <i>no_root_squash</i> is set.</p>
<h2>Files</h2>
<p><i>/var/spool/at</i> The directory for storing jobs; this should be mode 700, owner root. </p>
<p> <i>/var/spool/at/spool</i> The directory for storing output; this should be mode 700, owner root. </p>
<p> <i>/etc/at.allow</i>, <i>/etc/at.deny</i> determine who can use the <code>at</code> system.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-at/">at</a></code>(1), <code><a href="/docs/linux/man/5-at-deny/">at.deny</a></code>(5), <code><a href="/docs/linux/man/5-at-allow/">at.allow</a></code>(5), <code><a href="/docs/linux/man/8-cron/">cron</a></code>(8), <code><a href="/docs/linux/man/1-crontab/">crontab</a></code>(1), <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3).</p>
<h2>Bugs</h2>
<p>The functionality of <code>atd</code> should be merged into <code><a href="/docs/linux/man/8-cron/">cron</a></code>(8)<code>.</code> </p>
