---
title: "get_datafile_property(3)"
name: "get_datafile_property"
section: "3"
letter: "g"
url: "/docs/linux/man/3-get_datafile_property/"
description: "get_datafile_property – Returns the property string for the object. Allegro game programming library."
---

<h2>NAME</h2>
<p> get_datafile_property &#8211; Returns the property string for the object. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>const char *get_datafile_property(const DATAFILE *dat, int type);</code></p>
<h2>DESCRIPTION</h2>
<p> Finds the property type of a DATAFILE object. The type parameter must be a value created with the DAT_ID() macro. Example: </p>
<pre><code>
const char *name;
... name = get_datafile_property(game_data,
                                 DAT_ID('N', 'A', 'M', 'E'));
if (name == empty_string)
    abort_on_error("Object doesn't have a name!");
</code></pre>
<h2>RETURN VALUE</h2>
<p> Returns a pointer to the text string for the object, or a pointer to the variable empty_string if the property isn&#8217;t present. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-dat_id/">DAT_ID</a></code>(3), <code><a href="/docs/linux/man/3-empty_string/">empty_string</a></code>(3) </p>
<h2>Index</h2>
