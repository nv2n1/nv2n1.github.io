---
title: "libnutclient_variables(3)"
name: "libnutclient_variables"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libnutclient_variables/"
description: "libnutclient_variables, nutclient_get_device_variables, nutclient_get_device_rw_variables, nutclient_has_device_variable, nutclient_get_device_variable_description, nutclient_get_device_variable_va..."
---

<h2 class="name">NAME</h2>
<p> libnutclient_variables, nutclient_get_device_variables, nutclient_get_device_rw_variables, nutclient_has_device_variable, nutclient_get_device_variable_description, nutclient_get_device_variable_values, nutclient_set_device_variable_value, nutclient_set_device_variable_values &#8211; Variable related functions in Network UPS Tools high-level client access library </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;nutclient.h&gt;
</code></pre>
<pre>
typedef void* NUTCLIENT_t;
</pre>
<pre><code>
strarr nutclient_get_device_variables(NUTCLIENT_t client, const char *dev);
strarr nutclient_get_device_rw_variables(NUTCLIENT_t client, const char *dev);
int nutclient_has_device_variable(NUTCLIENT_t client, const char *dev, const char *var);
char *nutclient_get_device_variable_description(NUTCLIENT_t client, const char *dev, const char *var);
strarr nutclient_get_device_variable_values(NUTCLIENT_t client, const char *dev, const char *var);
void nutclient_set_device_variable_value(NUTCLIENT_t client, const char *dev, const char *var, const char *value);
void nutclient_set_device_variable_values(NUTCLIENT_t client, const char *dev, const char *var, const strarr values);
</code></pre>
<h2>DESCRIPTION</h2>
<p> These functions allow to manage variables of devices. </p>
<p> The <code>nutclient_get_device_variables()</code> function retrieve the list of variables names for a device. The returned strarr must be freed by <i>strarr_free</i>. </p>
<p> The <code>nutclient_get_device_rw_variables</code> function retrieve the list of read-write variables names for a device. The returned strarr must be freed by <i>strarr_free</i>. </p>
<p> The <code>nutclient_has_device_variable</code> function test if the specified variable is supported by the device. Return 1 is supported and 0 if not. </p>
<p> The <code>nutclient_get_device_variable_description</code> function retrieve the variable description, if any. The resturned string must be freed. </p>
<p> The <code>nutclient_get_device_variable_values</code> returns variable values (generally only one). The returned strarr must be freed by <i>strarr_free</i>. </p>
<p> The <code>nutclient_set_device_variable_value</code> intend to set the value of the specified variable. </p>
<p> The <code>nutclient_set_device_variable_values</code> intend to set multiple values of the specified variable. </p>
<p> <i>dev</i> is the device name. </p>
<p> <i>var</i> is the variable name. </p>
<p> <i>value</i> is the variable value. </p>
<p> <i>values</i> is the variable array of values.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libnutclient/">libnutclient</a></code>(3) <code><a href="/docs/linux/man/3-libnutclient_devices/">libnutclient_devices</a></code>(3) <code><a href="/docs/linux/man/3-libnutclient_general/">libnutclient_general</a></code>(3) </p>
<h2>Index</h2>
