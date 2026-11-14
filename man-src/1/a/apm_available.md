---
title: "apm_available(1)"
name: "apm_available"
section: "1"
letter: "a"
url: "/docs/linux/man/1-apm_available/"
description: "apm_available – test whether APM subsystem is available"
---

<h2 class="name">NAME</h2>
<p> apm_available &#8211; test whether APM subsystem is available</p>
<h2>SYNOPSIS</h2>
<p> <code>apm_available</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>apm_available</code> checks whether the APM (&quot;Advanced Power Management&quot;) subsystem is available, as evidenced by the presence of the /proc/apm file. </p>
<h2>OPTIONS</h2>
<p> None.</p>
<h2>EXIT STATUS</h2>
<pre>
<code>0</code> (true)        APM subsystem is available
<code>1</code> (false)       APM subsystem is not available
<code>2</code>                       usage error (arguments supplied)
</pre>
<h2>FILES</h2>
<pre>
<i>/proc/apm</i>         APM status information file
</pre>
<h2>AUTHOR</h2>
<p> This manual page was written by Thomas Hood &lt;jdthood [at] yahoo.co.uk&gt;. </p>
<h2>Index</h2>
