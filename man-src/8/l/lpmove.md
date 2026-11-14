---
title: "lpmove(8)"
name: "lpmove"
section: "8"
letter: "l"
url: "/docs/linux/man/8-lpmove/"
description: "lpmove – move a job or all jobs to a new destination"
---

<p>lpmove &#8211; move a job or all jobs to a new destination</p>
<h2>Synopsis</h2>
<p><code>lpmove</code> [ <code>-E</code> ] [ <code>-h </code><i>server</i>[<code>:</code><i>port</i>] ] [ <code>-U</code> <i>username</i> ] <i>job</i> <i>destination</i><br />
 <code>lpmove</code> [ <code>-E</code> ] [ <code>-h </code><i>server</i>[<code>:</code><i>port</i>] ] [ <code>-U</code> <i>username</i> ] <i>source</i> <i>destination</i></p>
<h2>Description</h2>
<p><code>lpmove</code> moves the specified <i>job</i> or all jobs from <i>source</i> to <i>destination</i>. <i>job</i> can be the job ID number or the old destination and job ID.</p>
<h2>Options</h2>
<p>The <code>lpmove</code> command supports the following options:</p>
<dl>
<dt><code>-E</code></p>
<dd>Forces encryption when connecting to the server.</p>
<dt><code>-U </code><i>username</i></p>
<dd>Specifies an alternate username.</p>
<dt><code>-h </code><i>server</i>[<code>:</code><i>port</i>]</p>
<dd>Specifies an alternate server.</dl>
<h2>Examples</h2>
<p>Move job 123 from &quot;oldprinter&quot; to &quot;newprinter&quot;: </p>
<pre> lpmove 123 newprinter
 <i>or</i>
 lpmove oldprinter-123 newprinter</pre>
<p>Move all jobs from &quot;oldprinter&quot; to &quot;newprinter&quot;: </p>
<pre> lpmove oldprinter newprinter</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-cancel/">cancel</a></code>(1), <code><a href="/docs/linux/man/1-lp/">lp</a></code>(1), <code><a href="/docs/linux/man/1-lpr/">lpr</a></code>(1), <code><a href="/docs/linux/man/1-lprm/">lprm</a></code>(1),<br />
 CUPS Online Help (<a rel="nofollow" href="http://localhost:631/help)">http://localhost:631/help)</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2021-2022 by OpenPrinting.</p>
