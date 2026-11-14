---
title: "iv_event_unregister(3)"
name: "iv_event_unregister"
section: "3"
letter: "i"
url: "/docs/linux/man/3-iv_event_unregister/"
description: "IV_EVENT_INIT, iv_event_register, iv_event_unregister, iv_event_post – manage ivykis objects for event notification"
---

<h2>NAME</h2>
<p> IV_EVENT_INIT, iv_event_register, iv_event_unregister, iv_event_post &#8211; manage ivykis objects for event notification</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;iv_event.h&gt;</code> </p>
<pre><code>
struct iv_event {
    void *cookie;
    void (*handler)(void *);
};
</code></pre>
<p> <code>int IV_EVENT_INIT(struct iv_event *</code><i>this</i><code>);</code><br />
 <code>int iv_event_register(struct iv_event *</code><i>this</i><code>);</code><br />
 <code>void iv_event_unregister(struct iv_event *</code><i>this</i><code>);</code><br />
 <code>void iv_event_post(struct iv_event *</code><i>this</i><code>);</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>iv_event</code> provides a way for delivering events to <code><a href="/docs/linux/man/3-ivykis/">ivykis</a></code>(3) recipients across thread boundaries. </p>
<p> The intended event recipient calls <code>IV_EVENT_INIT</code> on a <code>struct iv_event</code> object, fills in <code>-&gt;cookie</code> and <code>-&gt;handler,</code> and then calls <code>iv_event_register</code> on the object. </p>
<p> To generate an event, call <code>iv_event_post</code> on the previously initialized <code>struct iv_event</code> object. This will cause the callback specified by <code>-&gt;handler</code> to be called in the thread that the <code>struct iv_event</code> object was registered in, with <code>-&gt;cookie</code> as its sole argument. </p>
<p> To deinitialize a <code>struct iv_event</code> object, call <code>iv_event_unregister</code> from the same thread that <code>iv_event_register</code> was called from on that object. </p>
<p> It is permitted to unregister a <code>struct iv_event</code> object from any ivykis callback function in the thread it was registered in, including from a callback function triggered by this object, and it is permitted to free the memory corresponding to an unregistered object from its own callback function. </p>
<p> <code>iv_event_post</code> can be called from the same thread that <code>iv_event_register</code> was called from, or from a different thread within the same process, but can not be called from a different process, and can not be called from signal handlers. If you need this functionality, look at <code><a href="/docs/linux/man/3-iv_event_raw/">iv_event_raw</a></code>(3). </p>
<p> Internally, <code>iv_event</code> is implemented as a wrapper around <code><a href="/docs/linux/man/3-iv_event_raw/">iv_event_raw</a></code>(3), and multiplexes multiple <code>struct iv_event</code> objects over per-thread <code>struct iv_event_raw</code> objects, to save file descriptors and kernel resources. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ivykis/">ivykis</a></code>(3), <code><a href="/docs/linux/man/3-iv_event_raw/">iv_event_raw</a></code>(3) </p>
<h2>Index</h2>
