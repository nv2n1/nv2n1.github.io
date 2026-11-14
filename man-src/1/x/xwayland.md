---
title: "xwayland(1)"
name: "xwayland"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xwayland/"
description: "Xwayland – an X server for running X clients under Wayland."
---

<p>Xwayland &#8211; an X server for running X clients under Wayland. </p>
<h2>Synopsis</h2>
<p><code>Xwayland</code> [option &#8230;]</p>
<h2>Description</h2>
<p><i>Xwayland</i> is an X server and a Wayland client. It plays the role of a proxy between legacy X clients which do not support the Wayland protocols and the Wayland server. </p>
<p> Usually, <i>Xwayland</i> is spawned automatically by the Wayland server and runs rootless so that X clients integrate seamlessly with the rest of the Wayland desktop. It is however possible for a user to launch Xwayland non-rootless, mainly for testing purposes. </p>
<p> Like all of the X servers, <i>Xwayland</i> accepts the command line options described in the <i><a href="/docs/linux/man/7-xserver/">Xserver</a></i>(7) manual page. The following additional arguments are supported as well.</p>
<dl>
<dt><code>-eglstream</code></p>
<dd>Use EGLStream backend for NVidia GPUs. If <i>Xwayland</i> was compiled with EGLStream support, this option will instruct <i>Xwayland</i> to try that backend first, then fallback to the GBM backend if EGLStream is not supported by the Wayland server. Without this option, <i>Xwayland</i> tries the GBM backend first, and fallback to EGLStream if GBM is not usable.</p>
<dt><code>-initfd </code><i>fd</i></p>
<dd>Add the given <i>fd</i> as a listen socket for initialization of X clients. This options is aimed at <i>Wayland</i> servers which run <i>Xwayland</i> on-demand, to be able to spawn specific X clients which need to complete before other regular X clients can connect to <i>Xwayland</i>, like <i>xrdb</i>.</p>
<dt><code>-listen </code><i>fd</i></p>
<dd>deprecated, use <i>-listenfd</i> instead.</p>
<dt><code>-listenfd </code><i>fdP</i></p>
<dd>Add given fd as a listen socket. This option is used by the <i>Wayland</i> server to pass <i>Xwayland</i> the socket where X clients connect.</p>
<dt><code>-noTouchPointerEmulation</code></p>
<dd>Disable touch pointer emulation. This allows the Wayland compositor to implement its own pointer emulation mechanism for X11 clients that don&#8217;t support touch input.</p>
<dt><code>-rootless</code></p>
<dd>Run <i>Xwayland</i> rootless, so that X clients integrate seamlessly with Wayland clients in a Wayland desktop. That requires the Wayland server to be an X window manager as well.</p>
<dt><code>-shm</code></p>
<dd>Force the shared memory backend instead of glamor (if available) for passing buffers to the Wayland server.</p>
<dt><code>-verbose</code> [<i>n</i>]</p>
<dd>Sets the verbosity level for information printed on stderr. If the <i>n</i> value isn&#8217;t supplied, each occurrence of this option increments the verbosity level. When the <i>n</i> value is supplied, the verbosity level is set to that value. The default verbosity level is 0.</p>
<dt><code>-version</code></p>
<dd>Show the server version and exit.</p>
<dt><code>-wm </code><i>fd</i></p>
<dd>This option is used by the <i>Wayland</i> server to pass <i>Xwayland</i> the socket where the X window manager client connects, when <i>Xwayland</i> is running with <i>-rootless</i>.</dl>
<h2>Environment</h2>
<dl>
<dt><code>WAYLAND_DISPLAY</code></p>
<dd>the name of the display of the Wayland server.</p>
<dt><code>XWAYLAND_NO_GLAMOR</code></p>
<dd>disable glamor and DRI3 support in <i>Xwayland</i>, for testing purposes.</dl>
<h2>See Also</h2>
<p>General information: <i><a href="/docs/linux/man/7-x/">X</a></i>(7)</p>
