---
title: "get_executable_name(3)"
name: "get_executable_name"
section: "3"
letter: "g"
url: "/docs/linux/man/3-get_executable_name/"
description: "get_executable_name – Obtains the full path to the current executable. Allegro game programming library."
---

<h2>NAME</h2>
<p> get_executable_name &#8211; Obtains the full path to the current executable. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void get_executable_name(char *buf, int size);</code></p>
<h2>DESCRIPTION</h2>
<p> Fills `buf&#8217; with the full path to the current executable, writing at most `size&#8217; bytes. This generally comes from `argv[0]&#8217; but on Unix systems it tries to get the information from the `/proc&#8217; filesystem first, searching the directories specified in `$PATH&#8217; if necessary. If this fails too, it tries to find the executable name from the output of the `ps&#8217; command, using `argv[0]&#8217; only as a last resort if all other options fail. Example: </p>
<pre><code>
char name[200];
... get_executable_name(name, sizeof(name));
allegro_message("Running `%s'
", name);
</code></pre>
<h2>Index</h2>
