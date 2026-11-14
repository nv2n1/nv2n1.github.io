---
title: "override_config_data(3)"
name: "override_config_data"
section: "3"
letter: "o"
url: "/docs/linux/man/3-override_config_data/"
description: "override_config_data – Specifies a block of data containing config overrides. Allegro game programming library."
---

<p>override_config_data &#8211; Specifies a block of data containing config overrides. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void override_config_data(const char *data, int length);</code></pre>
<h2>Description</h2>
<p>Version of override_config_file() which uses a block of data that has already been read into memory. The length of the block has to be specified in bytes. Example:  Note that this function and override_config_file() are mutually exclusive, i.e. calling one will cancel the effects of the other. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-override_config_file/">override_config_file</a></code>(3), <code><a href="/docs/linux/man/3-set_config_data/">set_config_data</a></code>(3) </p>
