---
title: "libnutclient_devices(3)"
name: "libnutclient_devices"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libnutclient_devices/"
description: "libnutclient_devices, nutclient_get_devices, nutclient_has_device, nutclient_get_device_description – Device related functions in Network UPS Tools high-level client access library"
---

<h2 class="name">NAME</h2>
<p> libnutclient_devices, nutclient_get_devices, nutclient_has_device, nutclient_get_device_description &#8211; Device related functions in Network UPS Tools high-level client access library </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;nutclient.h&gt;
</code></pre>
<pre>
typedef void* NUTCLIENT_t;
</pre>
<pre><code>
strarr nutclient_get_devices(NUTCLIENT_t client);
int nutclient_has_device(NUTCLIENT_t client, const char *dev);
char *nutclient_get_device_description(NUTCLIENT_t client, const char *dev);
</code></pre>
<h2>DESCRIPTION</h2>
<p> These functions allow to manage devices. </p>
<p> The <code>nutclient_get_devices()</code> function retrieve the list of devices monitored by a client. The returned strarr must be freed by <i>strarr_free</i>. </p>
<p> The <code>nutclient_has_device()</code> function test if a device is monitored by a client. </p>
<p> The <code>nutclient_get_device_description()</code> function retrieve the device description. The returned description string must be freed. </p>
<p> <i>dev</i> is the device name.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libnutclient/">libnutclient</a></code>(3) <code><a href="/docs/linux/man/3-libnutclient_commands/">libnutclient_commands</a></code>(3) <code><a href="/docs/linux/man/3-libnutclient_devices/">libnutclient_devices</a></code>(3) <code><a href="/docs/linux/man/3-libnutclient_general/">libnutclient_general</a></code>(3) <code><a href="/docs/linux/man/3-libnutclient_variables/">libnutclient_variables</a></code>(3) </p>
<h2>Index</h2>
