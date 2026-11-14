---
title: "libnutclient_commands(3)"
name: "libnutclient_commands"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libnutclient_commands/"
description: "libnutclient_commands, nutclient_get_device_commands, nutclient_has_device_command, nutclient_get_device_command_description, nutclient_execute_device_command – Instant command related functions in..."
---

<h2 class="name">NAME</h2>
<p> libnutclient_commands, nutclient_get_device_commands, nutclient_has_device_command, nutclient_get_device_command_description, nutclient_execute_device_command &#8211; Instant command related functions in Network UPS Tools high-level client access library </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;nutclient.h&gt;
</code></pre>
<pre>
typedef void* NUTCLIENT_t;
</pre>
<pre><code>
strarr nutclient_get_device_commands(NUTCLIENT_t client, const char *dev);
int nutclient_has_device_command(NUTCLIENT_t client, const char *dev, const char *cmd);
char *nutclient_get_device_command_description(NUTCLIENT_t client, const char *dev, const char *cmd);
void nutclient_execute_device_command(NUTCLIENT_t client, const char *dev, const char *cmd);
</code></pre>
<h2>DESCRIPTION</h2>
<p> These functions allow to manage instant commands of devices. </p>
<p> The <code>nutclient_get_device_commands()</code> function retrieve the list of command names for a device. The returned strarr must be freed by <i>strarr_free</i>. </p>
<p> The <code>nutclient_has_device_command</code> function test if the specified command is supported by the device. Return 1 is supported and 0 if not. </p>
<p> The <code>nutclient_get_device_command_description</code> function retrieve the command description, if any. The resturned string must be freed. </p>
<p> The <code>nutclient_execute_device_command</code> intend to execute the instant command. </p>
<p> <i>dev</i> is the device name. </p>
<p> <i>cmd</i> is the instant command name.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libnutclient/">libnutclient</a></code>(3) <code><a href="/docs/linux/man/3-libnutclient_devices/">libnutclient_devices</a></code>(3) <code><a href="/docs/linux/man/3-libnutclient_general/">libnutclient_general</a></code>(3) </p>
<h2>Index</h2>
