---
title: "lprm(1)"
name: "lprm"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lprm/"
description: "lprm – cancel print jobs"
---

<h2 class="name">NAME</h2>
<p> lprm &#8211; cancel print jobs </p>
<h2>SYNOPSIS</h2>
<p> <code>lprm</code> [ <code>-E</code> ] [ <code>-U</code> <i>username</i> ] [ <code>-h</code> <i>server</i>[<i>:port</i>] ] [ <code>-P</code> <i>destination</i>[<i>/instance</i>] ] [ <code>&#8211;</code> ] [ <i>job-id(s)</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>lprm</code> cancels print jobs that have been queued for printing. If no arguments are supplied, the current job on the default destination is canceled. You can specify one or more job ID numbers to cancel those jobs or use the <i>&#8211;</i> option to cancel all jobs.</p>
<h2>OPTIONS</h2>
<p> The <code>lprm</code> command supports the following options:</p>
<dl>
<dt><code>-E</code></p>
<dd> Forces encryption when connecting to the server.</p>
<dt><code>-P </code><i>destination</i>[<i>/instance</i>]</p>
<dd> Specifies the destination printer or class.</p>
<dt><code>-U </code><i>username</i></p>
<dd> Specifies an alternate username.</p>
<dt><code>-h </code><i>server</i>[<i>:port</i>]</p>
<dd> Specifies an alternate server.</dl>
<h2>CONFORMING TO</h2>
<p> The CUPS version of <code>lprm</code> is compatible with the standard Berkeley command of the same name.</p>
<h2>EXAMPLES</h2>
<p> Cancel the current job on the default printer: </p>
<pre>
    lprm
</pre>
<p> Cancel job 1234: </p>
<pre>
    lprm 1234
</pre>
<p> Cancel all jobs: </p>
<pre>
    lprm -
</pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-cancel/">cancel</a></code>(1), <code><a href="/docs/linux/man/1-lp/">lp</a></code>(1), <code><a href="/docs/linux/man/1-lpq/">lpq</a></code>(1), <code><a href="/docs/linux/man/1-lpr/">lpr</a></code>(1), <code><a href="/docs/linux/man/1-lpstat/">lpstat</a></code>(1), CUPS Online Help (<a rel="nofollow" href="http://localhost:631/help)">http://localhost:631/help)</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2021-2022 by OpenPrinting. </p>
<h2>Index</h2>
