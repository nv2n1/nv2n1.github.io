---
title: "set_config_string(3)"
name: "set_config_string"
section: "3"
letter: "s"
url: "/docs/linux/man/3-set_config_string/"
description: "set_config_string – Writes a string in the configuration file. Allegro game programming library."
---

<p>set_config_string &#8211; Writes a string in the configuration file. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void set_config_string(const char *section, const char *name,

                       const char *val);</code></pre>
<h2>Description</h2>
<p>Writes a string variable to the current config file, replacing any existing value it may have, or removes the variable if `val&#8217; is NULL. The section name may be set to NULL to write the variable to the root of the file, or used to control which section the variable is inserted into. The altered file will be cached in memory, and not actually written to disk until you call allegro_exit(). Note that you can only write to files in this way, so the function will have no effect if the current config source was specified with set_config_data() rather than set_config_file(). As a special case, variable or section names that begin with a &#8216;#&#8217; character are treated specially and will not be read from or written to the disk. Addon packages can use this to store version info or other status information into the config module, from where it can be read with the get_config_string() function. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-set_config_file/">set_config_file</a></code>(3), <code><a href="/docs/linux/man/3-get_config_string/">get_config_string</a></code>(3), <code><a href="/docs/linux/man/3-set_config_float/">set_config_float</a></code>(3), <code><a href="/docs/linux/man/3-set_config_hex/">set_config_hex</a></code>(3), <code><a href="/docs/linux/man/3-set_config_int/">set_config_int</a></code>(3), <code><a href="/docs/linux/man/3-set_config_id/">set_config_id</a></code>(3) </p>
