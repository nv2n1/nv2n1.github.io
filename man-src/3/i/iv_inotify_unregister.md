---
title: "iv_inotify_unregister(3)"
name: "iv_inotify_unregister"
section: "3"
letter: "i"
url: "/docs/linux/man/3-iv_inotify_unregister/"
description: "IV_INOTIFY_INIT, iv_inotify_register, iv_inotify_unregister, IV_INOTIFY_WATCH_INIT, iv_inotify_watch_register, iv_inotify_watch_unregister – ivykis inotify(7) wrapper"
---

<h2>NAME</h2>
<p> IV_INOTIFY_INIT, iv_inotify_register, iv_inotify_unregister, IV_INOTIFY_WATCH_INIT, iv_inotify_watch_register, iv_inotify_watch_unregister &#8211; ivykis <code><a href="/docs/linux/man/7-inotify/">inotify</a></code>(7) wrapper</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;iv_inotify.h&gt;
struct iv_inotify {
};
</code></pre>
<p> <code>void IV_INOTIFY_INIT(struct iv_inotify *</code><i>inotify</i><code>);</code><br />
 <code>int iv_inotify_register(struct iv_inotify *</code><i>inotify</i><code>);</code><br />
 <code>void iv_inotify_unregister(struct iv_inotify *inotify</code><i>);</i> </p>
<pre><code>
struct iv_inotify_watch {
    struct iv_inotify *inotify;
    const char *pathname;
    uint32_t mask;
    void *cookie;
    void (*handler)(void *, struct inotify_event *);
};
</code></pre>
<p> <code>void IV_INOTIFY_WATCH_INIT(struct iv_inotify_watch *</code><i>watch</i><code>);</code><br />
 <code>int iv_inotify_watch_register(struct iv_inotify_watch *</code><i>watch</i><code>);</code><br />
 <code>int iv_inotify_watch_unregister(struct iv_inotify_watch *</code><i>watch</i><code>);</code> </p>
<h2>DESCRIPTION</h2>
<p> The <code>iv_inotify_register</code> function registers an <code>iv_inotify</code> instance with the <code><a href="/docs/linux/man/3-iv_inotify/">iv_inotify</a></code>(3) module. The <code>inotify</code> parameter is a pointer to the <code>iv_inotify</code> structure to be registered. </p>
<p> The <code>iv_inotify_unregister</code> function unregisters an <code>iv_inotify</code> instance from the <code><a href="/docs/linux/man/3-iv_inotify/">iv_inotify</a></code>(3) module. The <code>inotify</code> parameter is a pointer to the <code>iv_inotify</code> structure to be unregistered. </p>
<p> The <code>iv_inotify_watch_register</code> function adds a watch to the registered <code>iv_inotify</code> instance specified by the <code>-&gt;inotify</code> member. </p>
<p> The <code>iv_inotify_watch_unregister</code> function removes a watch from the <code>iv_inotify</code> instance specified by the <code>-&gt;inotify</code> member. </p>
<p> In the <code>iv_inotify_watch</code> structure used in these functions, the <code>-&gt;pathname</code> and <code>-&gt;mask</code> members correspond to the members of struct inotify_watch as described in <code><a href="/docs/linux/man/7-inotify/">inotify</a></code>(7). <code>-&gt;handler</code> is the event handler called when this watch triggers. The arguments to this handler function are the pointer stored in the <code>-&gt;cookie</code> member of the <code>iv_inotify_watch</code> structure and a pointer to an inotify_event structure as described in <code><a href="/docs/linux/man/7-inotify/">inotify</a></code>(7).</p>
<h2>RETURN VALUE</h2>
<p> <code>iv_inotify_register</code> and <code>iv_inotify_watch_register</code> return zero on success. On error, -1 is returned, and errno is set appropriately.</p>
<h2>ERRORS</h2>
<p> iv_inotify will return errors returned by <code><a href="/docs/linux/man/3-inotify_init/">inotify_init</a></code>(3) and <code><a href="/docs/linux/man/3-inotify_add_watch/">inotify_add_watch</a></code>(3).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ivykis/">ivykis</a></code>(3), <code><a href="/docs/linux/man/7-inotify/">inotify</a></code>(7), <code><a href="/docs/linux/man/3-inotify_init/">inotify_init</a></code>(3), <code><a href="/docs/linux/man/3-inotify_add_watch/">inotify_add_watch</a></code>(3), <code><a href="/docs/linux/man/3-inotify_rm_watch/">inotify_rm_watch</a></code>(3) </p>
<h2>Index</h2>
