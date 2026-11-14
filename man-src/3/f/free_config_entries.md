---
title: "free_config_entries(3)"
name: "free_config_entries"
section: "3"
letter: "f"
url: "/docs/linux/man/3-free_config_entries/"
description: "free_config_entries – Frees memory allocated for config entry lists. Allegro game programming library."
---

<h2>NAME</h2>
<p> free_config_entries &#8211; Frees memory allocated for config entry lists. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int free_config_entries(const char ***names);</code></p>
<h2>DESCRIPTION</h2>
<p> Once you are done with the string arrays filled in by list_config_entries and list_config_sections, you can free them again with this function. The passed array pointer will be set to NULL, and you directly can pass the same pointer again to list_config_entries or list_config_sections later &#8211; but you also could pass them again without freeing first, since the memory is re-allocated when the pointer is not NULL. </p>
<p> See list_config_entries for an example of how to use it. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-list_config_entries/">list_config_entries</a></code>(3), <code><a href="/docs/linux/man/3-list_config_sections/">list_config_sections</a></code>(3) </p>
<h2>Index</h2>
