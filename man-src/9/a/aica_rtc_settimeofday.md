---
title: "aica_rtc_settimeofday(9)"
name: "aica_rtc_settimeofday"
section: "9"
letter: "a"
url: "/docs/linux/man/9-aica_rtc_settimeofday/"
description: "aica_rtc_settimeofday – Set the AICA RTC to the current time"
---

<p>aica_rtc_settimeofday &#8211; Set the AICA RTC to the current time</p>
<h2>Synopsis</h2>
<pre><code>int aica_rtc_settimeofday(const time_t secs);</code></pre>
<h2>Arguments</h2>
<p><i>secs</i></p>
<dl>
<dd>
<dd>contains the time_t to set</dl>
<h2>Description</h2>
<p>Adjusts the given <i>tv</i> to the AICA Epoch and sets the RTC seconds counter.</p>
<h2>Author</h2>
<p><code>Paul Mundt</code> &lt;lethal [at] linux-sh.org&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
