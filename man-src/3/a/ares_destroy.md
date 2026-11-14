---
title: "ares_destroy(3)"
name: "ares_destroy"
section: "3"
letter: "a"
url: "/docs/linux/man/3-ares_destroy/"
description: "ares_destroy – Destroy a resolver channel"
---

<h2>NAME</h2>
<p> ares_destroy &#8211; Destroy a resolver channel</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ares.h&gt;
void ares_destroy(ares_channel channel)
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>ares_destroy</code> function destroys the name service channel identified by <i>channel</i>, freeing all memory and closing all sockets used by the channel. <code>ares_destroy</code> invokes the callbacks for each pending query on the channel, passing a status of <code>ARES_EDESTRUCTION</code>. These calls give the callbacks a chance to clean up any state which might have been stored in their arguments. A callback must not add new requests to a channel being destroyed.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ares_init/">ares_init</a></code>(3), <code><a href="/docs/linux/man/3-ares_cancel/">ares_cancel</a></code>(3)</p>
<h2>AUTHOR</h2>
<p> Greg Hudson, MIT Information Systems<br />
 Copyright 1998 by the Massachusetts Institute of Technology. </p>
<h2>Index</h2>
