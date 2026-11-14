---
title: "wl_display_connect(3)"
name: "wl_display_connect"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wl_display_connect/"
description: "wl_display_connect, wl_display_connect_to_fd – Connect to a Wayland socket"
---

<p>wl_display_connect, wl_display_connect_to_fd &#8211; Connect to a Wayland socket</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;wayland-client.h&gt;

struct wl_display *wl_display_connect(const char *name);

struct wl_display *wl_display_connect_to_fd(int fd);</code></pre>
<h2>Description</h2>
<p><code>wl_display_connect</code></p>
<dd>connects to a Wayland socket that was previously opened by a Wayland server. The server socket must be placed in <code>XDG_RUNTIME_DIR</code> for this function to find it. The <i>name</i> argument specifies the name of the socket or <code>NULL</code> to use the default (which is <code>&quot;wayland-0&quot;</code>). The environment variable <code>WAYLAND_DISPLAY</code> replaces the default value. If <code>WAYLAND_SOCKET</code> is set, this function behaves like <code>wl_display_connect_to_fd</code> with the file-descriptor number taken from the environment variable. </p>
<p> <code>wl_display_connect_to_fd</code> connects to a Wayland socket with an explicit file-descriptor. The file-descriptor is passed as argument <i>fd</i>.</p>
<h2>Return Value</h2>
<p><code>wl_display_connect</code> and <code>wl_display_connect_to_fd</code> return a new display context object or NULL on failure. <i>errno</i> is set correspondingly.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-wayland-client/">wayland-client</a></code>(7), <code><a href="/docs/linux/man/3-wl_display_disconnect/">wl_display_disconnect</a></code>(3), <code><a href="/docs/linux/man/3-wl_display_iterate/">wl_display_iterate</a></code>(3) </p>
