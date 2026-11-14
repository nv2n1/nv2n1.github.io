---
title: "override_config_file(3)"
name: "override_config_file"
section: "3"
letter: "o"
url: "/docs/linux/man/3-override_config_file/"
description: "override_config_file – Specifies a file containing config overrides. Allegro game programming library."
---

<p>override_config_file &#8211; Specifies a file containing config overrides. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void override_config_file(const char *filename);</code></pre>
<h2>Description</h2>
<p>Specifies a file containing config overrides. These settings will be used in addition to the parameters in the main config file, and where a variable is present in both files this version will take priority. This can be used by application programmers to override some of the config settings from their code, while still leaving the main config file free for the end user to customise. For example, you could specify a particular sample frequency and IBK instrument file, but the user could still use an `allegro.cfg&#8217; file to specify the port settings and irq numbers. The override config file will not only take precedence when reading, but will also be used for storing values. When you are done with using the override config file, you can call override_config_file with a NULL parameter, so config data will be directly read from the current config file again. Note: The override file is completely independent from the current configuration. You can e.g. call set_config_file, and the override file will still be active. Also the flush_config_file function will only affect the current config file (which can be changed with set_config_file), never the overriding one specified with this function. The modified override config is written back to disk whenever you call override_config_file. Example:  Note that this function and override_config_data() are mutually exclusive, i.e. calling one will cancel the effects of the other. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-override_config_data/">override_config_data</a></code>(3), <code><a href="/docs/linux/man/3-set_config_file/">set_config_file</a></code>(3) </p>
