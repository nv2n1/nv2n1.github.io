---
title: "libnutclient_misc(3)"
name: "libnutclient_misc"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libnutclient_misc/"
description: "libnutclient_misc, nutclient_authenticate, nutclient_logout, nutclient_device_login, nutclient_get_device_num_logins, nutclient_device_master, nutclient_device_forced_shutdown – Miscelaneous functi..."
---

<h2 class="name">NAME</h2>
<p> libnutclient_misc, nutclient_authenticate, nutclient_logout, nutclient_device_login, nutclient_get_device_num_logins, nutclient_device_master, nutclient_device_forced_shutdown &#8211; Miscelaneous functions in Network UPS Tools high-level client access library </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;nutclient.h&gt;
</code></pre>
<pre>
typedef void* NUTCLIENT_t;
</pre>
<pre><code>
void nutclient_authenticate(NUTCLIENT_t client, const char *login, const char *passwd);
void nutclient_logout(NUTCLIENT_t client);
void nutclient_device_login(NUTCLIENT_t client, const char *dev);
int nutclient_get_device_num_logins(NUTCLIENT_t client, const char *dev);
void nutclient_device_master(NUTCLIENT_t client, const char *dev);
void nutclient_device_forced_shutdown(NUTCLIENT_t client, const char *dev);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>nutclient_authenticate()</code> function authenticate the user. </p>
<p> <i>login</i> is the user name. </p>
<p> <i>passwd</i> is the user password. </p>
<p> The <code>nutclient_logout()</code> function disconnect gracefully from the server. </p>
<p> The <code>nutclient_device_login()</code> function log the fact that a system is drawing power from this UPS. </p>
<p> The <code>nutclient_get_device_num_logins()</code> function retrieve the number of clients which have been logged for this device. </p>
<p> The <code>nutclient_device_master()</code> function make sure that master-level functions like FSD are available if necessary. </p>
<p> The <code>nutclient_device_forced_shutdown()</code> function sets the &quot;forced shutdown&quot; flag on the device. </p>
<p> <i>dev</i> is the device name.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libnutclient/">libnutclient</a></code>(3) </p>
<h2>Index</h2>
