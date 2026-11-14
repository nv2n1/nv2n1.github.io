---
title: "iv_signal_init(3)"
name: "iv_signal_init"
section: "3"
letter: "i"
url: "/docs/linux/man/3-iv_signal_init/"
description: "IV_SIGNAL_INIT, iv_signal_register, iv_signal_unregister – ivykis signal handling"
---

<p>IV_SIGNAL_INIT, iv_signal_register, iv_signal_unregister &#8211; ivykis signal handling</p>
<h2>Synopsis</h2>
<p><code>#include &lt;iv_signal.h&gt;</code> </p>
<pre>struct iv_signal {
 int signum;
 unsigned int flags;
 void *cookie;
 void (*handler)(void *);
};</pre>
<p><code>void IV_SIGNAL_INIT(struct iv_signal *</code><i>this</i><code>);</code><br />
 <code>int iv_signal_register(struct iv_signal *</code><i>this</i><code>);</code><br />
 <code>void iv_signal_unregister(struct iv_signal *</code><i>this</i><code>);</code> </p>
<h2>Description</h2>
<p><code>iv_signal</code> provides a way for <code><a href="/docs/linux/man/3-ivykis/">ivykis</a></code>(3) applications to handle POSIX signals, by integrating them with the ivykis event loop. </p>
<p> An ivykis application desiring signal notification registers a <code>struct iv_signal</code> object by calling <code>iv_signal_register,</code> after having initialised it with <code>IV_SIGNAL_INIT</code> and subsequently having filled in the <code>-&gt;signum,</code> <code>-&gt;cookie</code> and <code>-&gt;handler</code> members. </p>
<p> Once the signal indicated by <code>-&gt;signum</code> is delivered to any thread in the current process, the callback specified by <code>-&gt;handler</code> is scheduled to be called in the thread that the <code>struct iv_signal</code> object was registered in, with <code>-&gt;cookie</code> as its sole argument. </p>
<p> If the same signal arrives again while the callback function is still running, the callback function is guaranteed to be called again after it returns. </p>
<p> It is permitted to register multiple <code>struct iv_signal</code> objects for the same signal number. If all such objects are registered with <code>IV_SIGNAL_FLAG_EXCLUSIVE</code> in <code>-&gt;flags</code> unset, then all objects will have their callback functions called upon arrival of the signal, in no guaranteed order. </p>
<p> Invoking callback functions stops at the first <code>struct iv_signal</code> object with <code>IV_SIGNAL_FLAG_EXCLUSIVE</code> in <code>-&gt;flags</code> set, so that if all objects have <code>IV_SIGNAL_FLAG_EXCLUSIVE</code> set, only one callback function will be invoked. </p>
<p> To deinitialize a <code>struct iv_signal</code> object, call <code>iv_signal_unregister</code> from the same thread that <code>iv_signal_register</code> was called from on that object. </p>
<p> It is permitted to unregister a <code>struct iv_signal</code> object from any ivykis callback function in the thread it was registered in, including from a callback function triggered by this object, and it is permitted to free the memory corresponding to an unregistered object from its own callback function. </p>
<p> It is guaranteed that signals delivered to child processes that were created by <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) but that have not yet called <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) will not cause <code>iv_signal</code> callbacks to be invoked in the parent process. </p>
<p> Internally, <code>iv_signal</code> is implemented using <code><a href="/docs/linux/man/3-iv_event_raw/">iv_event_raw</a></code>(3). </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-ivykis/">ivykis</a></code>(3), <code><a href="/docs/linux/man/3-iv_event_raw/">iv_event_raw</a></code>(3), <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2)</p>
