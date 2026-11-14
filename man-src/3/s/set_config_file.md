---
title: "set_config_file(3)"
name: "set_config_file"
section: "3"
letter: "s"
url: "/docs/linux/man/3-set_config_file/"
description: "set_config_file – Sets the configuration file. Allegro game programming library."
---

<p>set_config_file &#8211; Sets the configuration file. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void set_config_file(const char *filename);</code></pre>
<h2>Description</h2>
<p>Sets the configuration file to be used by all subsequent config functions. If you don&#8217;t call this function, Allegro will use the default `allegro.cfg&#8217; file, looking first in the same directory as your program and then in the directory pointed to by the ALLEGRO environment variable and the usual platform-specific paths for configuration files. For example it will look for `/etc/allegro.cfg&#8217; under Unix. All pointers returned by previous calls to get_config_string() and other related functions are invalidated when you call this function! You can call this function before install_allegro() to change the configuration file, but after set_uformat() if you want to use a text encoding format other than the default. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-set_config_data/">set_config_data</a></code>(3), <code><a href="/docs/linux/man/3-override_config_file/">override_config_file</a></code>(3), <code><a href="/docs/linux/man/3-push_config_state/">push_config_state</a></code>(3), <code><a href="/docs/linux/man/3-set_uformat/">set_uformat</a></code>(3), <code><a href="/docs/linux/man/3-set_config_string/">set_config_string</a></code>(3), <code><a href="/docs/linux/man/3-get_config_string/">get_config_string</a></code>(3), <code><a href="/docs/linux/man/3-exconfig/">exconfig</a></code>(3) </p>
