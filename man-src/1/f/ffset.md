---
title: "ffset(1)"
name: "ffset"
section: "1"
letter: "f"
url: "/docs/linux/man/1-ffset/"
description: "ffset – set force-feedback device parameters"
---

<h2>NAME</h2>
<p> ffset &#8211; set force-feedback device parameters</p>
<h2>SYNOPSIS</h2>
<p> <code>ffset</code> &lt;<i>device</i>&gt; [<code>-g</code> &lt;<i>gain</i>&gt;] [<code>-a</code> &lt;<i>autocenter strength</i>&gt;]</p>
<h2>DESCRIPTION</h2>
<p> ffset sets the gain and autocenter strength of a force-feedback device.</p>
<h2>OPTIONS</h2>
<dl>
<dt>&lt;<i>device</i>&gt;</p>
<dd> The device to configure.</p>
<dt><code>-g</code> &lt;<i>gain</i>&gt;</p>
<dd> The gain (0-100).</p>
<dt><code>-a</code> &lt;<i>autocenter strength</i>&gt;</p>
<dd> The autocenter strength (0-100).</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ffcfstress/">ffcfstress</a></code>(1), <code><a href="/docs/linux/man/1-ffmvforce/">ffmvforce</a></code>(1), <code><a href="/docs/linux/man/1-fftest/">fftest</a></code>(1), <code><a href="/docs/linux/man/1-jscal/">jscal</a></code>(1), <code><a href="/docs/linux/man/1-jstest/">jstest</a></code>(1).</p>
<h2>AUTHOR</h2>
<p> <code>ffset</code> was written by Johann Deneux. </p>
<p> This manual page was written by Stephen Kitt &lt;steve [at] sk2.org&gt;, for the Debian GNU/Linux system (but may be used by others). It was last modified for <code>ffmvforce</code> dated May 30, 2001. </p>
<h2>Index</h2>
