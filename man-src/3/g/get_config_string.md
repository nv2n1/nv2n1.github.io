---
title: "get_config_string(3)"
name: "get_config_string"
section: "3"
letter: "g"
url: "/docs/linux/man/3-get_config_string/"
description: "get_config_string – Retrieves a string from the configuration file. Allegro game programming library."
---

<h2>NAME</h2>
<p> get_config_string &#8211; Retrieves a string from the configuration file. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>const char *get_config_string(const char *section,</code> <code>const char *name, const char *def);</code></p>
<h2>DESCRIPTION</h2>
<p> Retrieves a string variable from the current config file. The section name may be set to NULL to read variables from the root of the file, or used to control which set of parameters (eg. sound or joystick) you are interested in reading. Example: </p>
<pre><code>
const char *lang = get_config_string("system", "language", "EN");
</code></pre>
<h2>RETURN VALUE</h2>
<p> Returns a pointer to the constant string found in the configuration file. If the named variable cannot be found, or its entry in the config file is empty, the value of `def&#8217; is returned. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-set_config_file/">set_config_file</a></code>(3), <code><a href="/docs/linux/man/3-set_config_string/">set_config_string</a></code>(3), <code><a href="/docs/linux/man/3-get_config_argv/">get_config_argv</a></code>(3), <code><a href="/docs/linux/man/3-get_config_float/">get_config_float</a></code>(3), <code><a href="/docs/linux/man/3-get_config_hex/">get_config_hex</a></code>(3), <code><a href="/docs/linux/man/3-get_config_int/">get_config_int</a></code>(3), <code><a href="/docs/linux/man/3-get_config_id/">get_config_id</a></code>(3), <code><a href="/docs/linux/man/3-get_config_text/">get_config_text</a></code>(3), <code><a href="/docs/linux/man/3-exconfig/">exconfig</a></code>(3) </p>
<h2>Index</h2>
