---
title: "ares_set_socket_callback(3)"
name: "ares_set_socket_callback"
section: "3"
letter: "a"
url: "/docs/linux/man/3-ares_set_socket_callback/"
description: "ares_set_socket_callback – Set a socket creation callback"
---

<h2>NAME</h2>
<p> ares_set_socket_callback &#8211; Set a socket creation callback</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ares.h&gt;
void ares_set_socket_callback(ares_channel channel,
                              ares_sock_create_callback callback,
                              void *userdata)
        cc file.c
    - lcares
</code></pre>
<h2>DESCRIPTION</h2>
<p> This function sets a <i>callback</i> in the given ares channel handle. This callback function will be invoked after the socket has been created, and connected to the remote server. The callback must return ARES_SUCCESS if things are fine, or use the standard ares error codes to signal errors back. Returned errors will abort the ares operation.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ares_init_options/">ares_init_options</a></code>(3)</p>
<h2>AVAILABILITY</h2>
<p> <a href="/docs/linux/man/3-ares_set_socket_callback/">ares_set_socket_callback</a>(3) was added in c-ares 1.6.0</p>
<h2>AUTHOR</h2>
<p> Gregor Jasny </p>
<h2>Index</h2>
