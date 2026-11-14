---
title: "poll_scroll(3)"
name: "poll_scroll"
section: "3"
letter: "p"
url: "/docs/linux/man/3-poll_scroll/"
description: "poll_scroll – Checks the status of a scroll request with triple buffering. Allegro game programming library."
---

<p>poll_scroll &#8211; Checks the status of a scroll request with triple buffering. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

int poll_scroll();</code></pre>
<h2>Description</h2>
<p>This function is used for triple buffering. It checks the status of a hardware scroll previously initiated by the request_scroll() routine.</p>
<h2>Return Value</h2>
<p>Returns non-zero if it is still waiting to take place, and zero if the requested scroll has already happened. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-request_scroll/">request_scroll</a></code>(3), <code><a href="/docs/linux/man/3-request_video_bitmap/">request_video_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-ex3buf/">ex3buf</a></code>(3), <code><a href="/docs/linux/man/3-exupdate/">exupdate</a></code>(3) </p>
