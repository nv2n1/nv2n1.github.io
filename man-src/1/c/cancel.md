---
title: "cancel(1)"
name: "cancel"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cancel/"
description: "cancel – cancel jobs"
---

<h2 class="name">NAME</h2>
<p> cancel &#8211; cancel jobs </p>
<h2>SYNOPSIS</h2>
<p> <code>cancel</code> [ <code>-E</code> ] [ <code>-U</code> <i>username</i> ] [ <code>-a</code> ] [ <code>-h</code> <i>hostname[:port]</i> ] [ <code>-u</code> <i>username</i> ] [ <code>-x</code> ] [ <i>id</i> ] [ <i>destination</i> ] [ <i>destination-id</i> ]</p>
<h2>DESCRIPTION</h2>
<p> The <code>cancel</code> command cancels print jobs. If no <i>destination</i> or <i>id</i> is specified, the currently printing job on the default destination is canceled.</p>
<h2>OPTIONS</h2>
<p> The following options are recognized by <code>cancel</code>:</p>
<dl>
<dt><code>-a</code></p>
<dd> Cancel all jobs on the named destination, or all jobs on all destinations if none is provided.</p>
<dt><code>-E</code></p>
<dd> Forces encryption when connecting to the server.</p>
<dt><code>-h </code><i>hostname</i>[<i>:port</i>]</p>
<dd> Specifies an alternate server.</p>
<dt><code>-U </code><i>username</i></p>
<dd> Specifies the username to use when connecting to the server.</p>
<dt><code>-u </code><i>username</i></p>
<dd> Cancels jobs owned by <i>username</i>.</p>
<dt><code>-x</code></p>
<dd> Deletes job data files in addition to canceling.</dl>
<h2>CONFORMING TO</h2>
<p> Unlike the System V printing system, CUPS allows printer names to contain any printable character except SPACE, TAB, &quot;/&quot;, or &quot;#&quot;. Also, printer and class names are <i>not</i> case-sensitive.</p>
<h2>EXAMPLES</h2>
<p> Cancel the current print job: </p>
<pre>
    cancel
</pre>
<p> Cancel job &quot;myprinter-42&quot;: </p>
<pre>
    cancel myprinter-42
</pre>
<p> Cancel all jobs: </p>
<pre>
    cancel -a
</pre>
<h2>NOTES</h2>
<p> Administrators wishing to prevent unauthorized cancellation of jobs via the <i>-u</i> option should require authentication for Cancel-Jobs operations in <code><a href="/docs/linux/man/5-cupsd-conf/">cupsd.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-cupsd-conf/">cupsd.conf</a></code>(5), <code><a href="/docs/linux/man/1-lp/">lp</a></code>(1), <code><a href="/docs/linux/man/8-lpmove/">lpmove</a></code>(8), <code><a href="/docs/linux/man/1-lpstat/">lpstat</a></code>(1), CUPS Online Help (<a rel="nofollow" href="http://localhost:631/help)">http://localhost:631/help)</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2021-2022 by OpenPrinting. </p>
<h2>Index</h2>
