---
title: "aica_rtc_gettimeofday(9)"
name: "aica_rtc_gettimeofday"
section: "9"
letter: "a"
url: "/docs/linux/man/9-aica_rtc_gettimeofday/"
description: "aica_rtc_gettimeofday – Get the time from the AICA RTC"
---

<p>aica_rtc_gettimeofday &#8211; Get the time from the AICA RTC</p>
<h2>Synopsis</h2>
<pre><code>void aica_rtc_gettimeofday(struct timespec *ts);</code></pre>
<h2>Arguments</h2>
<p><i>ts</i></p>
<dl>
<dd>
<dd>pointer to resulting timespec</dl>
<h2>Description</h2>
<p>Grabs the current RTC seconds counter and adjusts it to the Unix Epoch.</p>
<h2>Author</h2>
<p><code>Paul Mundt</code> &lt;lethal [at] linux-sh.org&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
