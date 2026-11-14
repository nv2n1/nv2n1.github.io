---
title: "set_config_data(3)"
name: "set_config_data"
section: "3"
letter: "s"
url: "/docs/linux/man/3-set_config_data/"
description: "set_config_data – Sets a block of configuration data. Allegro game programming library."
---

<p>set_config_data &#8211; Sets a block of configuration data. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void set_config_data(const char *data, int length);</code></pre>
<h2>Description</h2>
<p>Specifies a block of data to be used by all subsequent config functions, which you have already loaded from disk (eg. as part of some more complicated format of your own, or in a grabber datafile). This routine makes a copy of the information, so you can safely free the data after calling it. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-set_config_file/">set_config_file</a></code>(3), <code><a href="/docs/linux/man/3-override_config_data/">override_config_data</a></code>(3), <code><a href="/docs/linux/man/3-push_config_state/">push_config_state</a></code>(3), <code><a href="/docs/linux/man/3-set_config_string/">set_config_string</a></code>(3), <code><a href="/docs/linux/man/3-get_config_string/">get_config_string</a></code>(3) </p>
