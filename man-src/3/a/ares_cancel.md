---
title: "ares_cancel(3)"
name: "ares_cancel"
section: "3"
letter: "a"
url: "/docs/linux/man/3-ares_cancel/"
description: "ares_cancel – Cancel a resolve"
---

<h2>NAME</h2>
<p> ares_cancel &#8211; Cancel a resolve</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ares.h&gt;
void ares_cancel(ares_channel channel)
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>ares_cancel</code> function cancels all lookups/requests made on the the name service channel identified by <i>channel</i>. <code>ares_cancel</code> invokes the callbacks for each pending query on the channel, passing a status of <code>ARES_ECANCELLED</code>. These calls give the callbacks a chance to clean up any state which might have been stored in their arguments. If such a callback invocation adds a new request to the channel, that request will <i>not</i> be cancelled by the current invocation of <code>ares_cancel</code>.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ares_init/">ares_init</a></code>(3) <code><a href="/docs/linux/man/3-ares_destroy/">ares_destroy</a></code>(3)</p>
<h2>NOTES</h2>
<p> This function was added in c-ares 1.2.0 </p>
<p> c-ares 1.6.0 and earlier pass a status of <code>ARES_ETIMEOUT</code> instead of <code>ARES_ECANCELLED</code>.</p>
<h2>AUTHOR</h2>
<p> Dirk Manske </p>
<h2>Index</h2>
