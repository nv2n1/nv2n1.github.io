---
title: "get_config_argv(3)"
name: "get_config_argv"
section: "3"
letter: "g"
url: "/docs/linux/man/3-get_config_argv/"
description: "get_config_argv – Reads a token list from the configuration file. Allegro game programming library."
---

<h2>NAME</h2>
<p> get_config_argv &#8211; Reads a token list from the configuration file. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>char **get_config_argv(const char *section, const char *name, int *argc);</code></p>
<h2>DESCRIPTION</h2>
<p> Reads a token list (words separated by spaces) from the current config file. The token list is stored in a temporary buffer that will be clobbered by the next call to get_config_argv(), so the data should not be expected to persist.</p>
<h2>RETURN VALUE</h2>
<p> Returns an argv style argument list and sets `argc&#8217; to the number of retrieved tokens. If the variable is not present, returns NULL and sets argc to zero. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-set_config_file/">set_config_file</a></code>(3), <code><a href="/docs/linux/man/3-get_config_string/">get_config_string</a></code>(3), <code><a href="/docs/linux/man/3-get_config_float/">get_config_float</a></code>(3), <code><a href="/docs/linux/man/3-get_config_hex/">get_config_hex</a></code>(3), <code><a href="/docs/linux/man/3-get_config_int/">get_config_int</a></code>(3), <code><a href="/docs/linux/man/3-get_config_id/">get_config_id</a></code>(3), <code><a href="/docs/linux/man/3-exconfig/">exconfig</a></code>(3) </p>
<h2>Index</h2>
