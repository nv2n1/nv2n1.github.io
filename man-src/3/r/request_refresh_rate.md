---
title: "request_refresh_rate(3)"
name: "request_refresh_rate"
section: "3"
letter: "r"
url: "/docs/linux/man/3-request_refresh_rate/"
description: "request_refresh_rate – Requests a specific refresh rate during graphic mode switch. Allegro game programming library."
---

<p>request_refresh_rate &#8211; Requests a specific refresh rate during graphic mode switch. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void request_refresh_rate(int rate);</code></pre>
<h2>Description</h2>
<p>Requests that the next call to set_gfx_mode() try to use the specified refresh rate, if possible. Not all drivers are able to control this at all, and even when they can, not all rates will be possible on all hardware, so the actual settings may differ from what you requested. After you call set_gfx_mode(), you can use get_refresh_rate() to find out what was actually selected. At the moment only the DOS VESA 3.0, X DGA 2.0 and some Windows DirectX drivers support this function. The speed is specified in Hz, eg. 60, 70. To return to the normal default selection, pass a rate value of zero. Example: </p>
<pre><code>request_refresh_rate(60);
if (set_gfx_mode(GFX_AUTODETECT, 640, 480, 0, 0) != 0)
    abort_on_error(&quot;Couldn't set graphic mode!&quot;);
if (get_refresh_rate() != 60)
    abort_on_error(&quot;Couldn't set refresh rate to 60Hz!&quot;);
</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-set_gfx_mode/">set_gfx_mode</a></code>(3), <code><a href="/docs/linux/man/3-get_refresh_rate/">get_refresh_rate</a></code>(3) </p>
