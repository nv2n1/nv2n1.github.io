---
title: "list_config_sections(3)"
name: "list_config_sections"
section: "3"
letter: "l"
url: "/docs/linux/man/3-list_config_sections/"
description: "list_config_sections – Lists the names of all sections available in the current configuration. Allegro game programming library."
---

<h2>NAME</h2>
<p> list_config_sections &#8211; Lists the names of all sections available in the current configuration. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int list_config_sections(const char ***names);</code></p>
<h2>DESCRIPTION</h2>
<p> The names parameter is a pointer to an array of strings. If it points to a NULL pointer, the list will be allocated, else it will be re-allocated. After the function returns, it will contain the names of all sections in the current configuration. Use free_config_entries to free the allocated memory again. See list_config_entries for more information and an example how to use it.</p>
<h2>RETURN VALUE</h2>
<p> Returns the number of valid strings in the names array. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-list_config_entries/">list_config_entries</a></code>(3), <code><a href="/docs/linux/man/3-set_config_file/">set_config_file</a></code>(3), <code><a href="/docs/linux/man/3-get_config_string/">get_config_string</a></code>(3), <code><a href="/docs/linux/man/3-free_config_entries/">free_config_entries</a></code>(3) </p>
<h2>Index</h2>
