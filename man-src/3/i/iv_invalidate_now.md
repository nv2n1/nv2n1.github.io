---
title: "iv_invalidate_now(3)"
name: "iv_invalidate_now"
section: "3"
letter: "i"
url: "/docs/linux/man/3-iv_invalidate_now/"
description: "iv_now, iv_validate_now, iv_invalidate_now – ivykis time handling"
---

<h2>NAME</h2>
<p> iv_now, iv_validate_now, iv_invalidate_now &#8211; ivykis time handling</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;iv.h&gt;</code> </p>
<p> <code>extern struct timespec </code><i>iv_now</i><code>;</code><br />
 <code>void iv_validate_now(void);</code><br />
 <code>void iv_invalidate_now(void);</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>iv_now</code> is a global variable that reflects the current time-of-day. Applications written to the ivykis API generally require to know the current time-of-day in many places, and therefore effort is done to cache this quantity. </p>
<p> The contents of <code>iv_now</code> might be stale. Calling the function <code>iv_validate_now</code> ensures that the current contents of <code>iv_now</code> are up-to-date. </p>
<p> The function <code>iv_invalidate_now</code> is called to invalidate the currently cached time-of-day. This function should be called after any operation that takes a significant amount of wall clock time.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ivykis/">ivykis</a></code>(3), <code><a href="/docs/linux/man/3-iv_examples/">iv_examples</a></code>(3) </p>
<h2>Index</h2>
