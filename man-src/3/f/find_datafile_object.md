---
title: "find_datafile_object(3)"
name: "find_datafile_object"
section: "3"
letter: "f"
url: "/docs/linux/man/3-find_datafile_object/"
description: "find_datafile_object – Searches a datafile for an object with a name. Allegro game programming library."
---

<h2>NAME</h2>
<p> find_datafile_object &#8211; Searches a datafile for an object with a name. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>DATAFILE *find_datafile_object(const DATAFILE *dat, const char *objectname);</code></p>
<h2>DESCRIPTION</h2>
<p> Searches an already loaded datafile for an object with the specified name. In the name you can use `/&#8217; and `#&#8217; separators for nested datafile paths. Example: </p>
<pre><code>
char level_name[10];
DATAFILE *dat, *level;
... uszprintf(level_name, sizeof(buffer),
              "LEVEL_%02d", level_number);
level = find_datafile_object(dat, level_name);
if (!level)
    abort_on_error("That level doesn't exist!");
</code></pre>
<h2>RETURN VALUE</h2>
<p> Returns a pointer to a single DATAFILE element whose `dat&#8217; member points to the object, or NULL if the object could not be found. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-load_datafile/">load_datafile</a></code>(3), <code><a href="/docs/linux/man/3-load_datafile_object/">load_datafile_object</a></code>(3) </p>
<h2>Index</h2>
