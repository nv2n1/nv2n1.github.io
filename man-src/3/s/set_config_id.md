---
title: "set_config_id(3)"
name: "set_config_id"
section: "3"
letter: "s"
url: "/docs/linux/man/3-set_config_id/"
description: "set_config_id – Writes a driver ID in the configuration file. Allegro game programming library."
---

<p>set_config_id &#8211; Writes a driver ID in the configuration file. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void set_config_id(const char *section, const char *name, int val);</code></pre>
<h2>Description</h2>
<p>Writes a 4-letter driver ID variable to the current config file. See the comments about set_config_string(). </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-set_config_file/">set_config_file</a></code>(3), <code><a href="/docs/linux/man/3-get_config_id/">get_config_id</a></code>(3), <code><a href="/docs/linux/man/3-set_config_string/">set_config_string</a></code>(3), <code><a href="/docs/linux/man/3-set_config_float/">set_config_float</a></code>(3), <code><a href="/docs/linux/man/3-set_config_hex/">set_config_hex</a></code>(3), <code><a href="/docs/linux/man/3-set_config_int/">set_config_int</a></code>(3) </p>
