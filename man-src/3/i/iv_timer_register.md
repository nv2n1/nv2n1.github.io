---
title: "iv_timer_register(3)"
name: "iv_timer_register"
section: "3"
letter: "i"
url: "/docs/linux/man/3-iv_timer_register/"
description: "iv_timer_register, iv_timer_unregister, iv_timer_registered – deal with ivykis timers"
---

<h2>NAME</h2>
<p> iv_timer_register, iv_timer_unregister, iv_timer_registered &#8211; deal with ivykis timers</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;iv.h&gt;</code> </p>
<pre><code>
struct iv_timer {
    struct timespec expires;
    void *cookie;
    void (*handler)(void *);
};
</code></pre>
<p> <code>void IV_TIMER_INIT(struct iv_timer *</code><i>timer</i><code>);</code><br />
 <code>void iv_timer_register(struct iv_timer *</code><i>timer</i><code>);</code><br />
 <code>void iv_timer_unregister(struct iv_timer *</code><i>timer</i><code>);</code><br />
 <code>int iv_timer_registered(struct iv_timer *</code><i>timer</i><code>);</code> </p>
<h2>DESCRIPTION</h2>
<p> The functions <code>iv_timer_register</code> and <code>iv_timer_unregister</code> register, respectively unregister, a timer with the current thread&#8217;s ivykis event loop. <code>iv_timer_registered</code> on a timer returns true if that timer is currently registered with ivykis. </p>
<p> When a timer that is registered becomes &#8216;ready&#8217;, due to the current system clock value becoming greater than or equal to the timer&#8217;s <code>-&gt;expires</code> member field, the callback function specified by <code>-&gt;handler</code> is called in the thread that the timer was registered in, with <code>-&gt;cookie</code> as its first and sole argument. When this happens, the timer is transparently unregistered. </p>
<p> The application is allowed to change the <code>-&gt;cookie</code> and <code>-&gt;handler</code> members at any time. The application is not allowed to change the <code>-&gt;expires</code> member while the timer is registered. </p>
<p> A given <code>struct iv_timer</code> can only be registered in one thread at a time, and a timer can only be unregistered in the thread that it was registered from. </p>
<p> There is no limit on the number of timers registered at once. </p>
<p> See <code><a href="/docs/linux/man/3-iv_examples/">iv_examples</a></code>(3) for programming examples.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ivykis/">ivykis</a></code>(3), <code><a href="/docs/linux/man/3-iv_examples/">iv_examples</a></code>(3) </p>
<h2>Index</h2>
