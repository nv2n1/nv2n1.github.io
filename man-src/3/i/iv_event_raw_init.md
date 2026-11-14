---
title: "iv_event_raw_init(3)"
name: "iv_event_raw_init"
section: "3"
letter: "i"
url: "/docs/linux/man/3-iv_event_raw_init/"
description: "IV_EVENT_RAW_INIT, iv_event_raw_register, iv_event_raw_unregister, iv_event_raw_post – manage ivykis objects for event notification"
---

<p>IV_EVENT_RAW_INIT, iv_event_raw_register, iv_event_raw_unregister, iv_event_raw_post &#8211; manage ivykis objects for event notification</p>
<h2>Synopsis</h2>
<p><code>#include &lt;iv_event_raw.h&gt;</code> </p>
<pre>struct iv_event_raw {
 void *cookie;
 void (*handler)(void *);
};</pre>
<p><code>void IV_EVENT_RAW_INIT(struct iv_event_raw *</code><i>this</i><code>);</code><br />
 <code>int iv_event_raw_register(struct iv_event_raw *</code><i>this</i><code>);</code><br />
 <code>void iv_event_raw_unregister(struct iv_event_raw *</code><i>this</i><code>);</code><br />
 <code>void iv_event_raw_post(struct iv_event_raw *</code><i>this</i><code>);</code> </p>
<h2>Description</h2>
<p><code>iv_event_raw</code> provides a way for delivering events to <code><a href="/docs/linux/man/3-ivykis/">ivykis</a></code>(3) recipients across thread and process boundaries. </p>
<p> The intended event recipient calls <code>IV_EVENT_RAW_INIT</code> on a <code>struct iv_event_raw</code> object, fills in <code>-&gt;cookie</code> and <code>-&gt;handler,</code> and then calls <code>iv_event_raw_register</code> on the object. </p>
<p> To generate an event, call <code>iv_event_raw_post</code> on the previously initialized <code>struct iv_event_raw</code> object. This will cause the callback specified by <code>-&gt;handler</code> to be called in the thread that the <code>struct iv_event_raw</code> object was registered in, with <code>-&gt;cookie</code> as its sole argument. </p>
<p> To deinitialize a <code>struct iv_event_raw</code> object, call <code>iv_event_raw_unregister</code> from the same thread that <code>iv_event_raw_register</code> was called from on that object. </p>
<p> It is permitted to unregister a <code>struct iv_event_raw</code> object from any ivykis callback function in the thread it was registered in, including from a callback function triggered by this object, and it is permitted to free the memory corresponding to an unregistered object from its own callback function. </p>
<p> <code>iv_event_raw_post</code> can be called from the same thread that <code>iv_event_raw_register</code> was called from, from a different thread in the same process, or even from a different process, and can safely be called from signal handlers. </p>
<p> If posting an event only ever needs to be done from within the same process, see <code><a href="/docs/linux/man/3-iv_event/">iv_event</a></code>(3) for a lighter-weight alternative to <code>iv_event_raw.</code> </p>
<p> Internally, <code>iv_event_raw</code> is implemented by registering a file descriptor (a struct <code><a href="/docs/linux/man/3-iv_fd/">iv_fd</a></code>(3)) with the recipient thread&#8217;s ivykis event loop, and by causing that file descriptor to become readable upon a call to <code>iv_event_raw_post.</code> </p>
<p> If <code><a href="/docs/linux/man/2-eventfd/">eventfd</a></code>(2) is available, it will be used to procure the abovementioned file descriptor. If not, <code>iv_event_raw</code> will fall back to <code><a href="/docs/linux/man/2-pipe/">pipe</a></code>(2) as the source of its file descriptors. <code><a href="/docs/linux/man/2-eventfd/">eventfd</a></code>(2) is preferred as it requires only one file descriptor table entry (while <code><a href="/docs/linux/man/2-pipe/">pipe</a></code>(2) requires two), and has much less kernel overhead than <code><a href="/docs/linux/man/2-pipe/">pipe</a></code>(2) has.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-ivykis/">ivykis</a></code>(3), <code><a href="/docs/linux/man/3-iv_event/">iv_event</a></code>(3), <code><a href="/docs/linux/man/2-eventfd/">eventfd</a></code>(2), <code><a href="/docs/linux/man/2-pipe/">pipe</a></code>(2)</p>
