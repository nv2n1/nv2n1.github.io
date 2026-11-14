---
title: "find_allegro_resource(3)"
name: "find_allegro_resource"
section: "3"
letter: "f"
url: "/docs/linux/man/3-find_allegro_resource/"
description: "find_allegro_resource – Searches for a support file in many places. Allegro game programming library."
---

<h2>NAME</h2>
<p> find_allegro_resource &#8211; Searches for a support file in many places. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int find_allegro_resource(char *dest, const char *resource, </code> <code>const char *ext, const char *datafile, </code> <code>const char *objectname, const char *envvar, </code> <code>const char *subdir, int size);</code></p>
<h2>DESCRIPTION</h2>
<p> Searches for a support file, eg. `allegro.cfg&#8217; or `language.dat&#8217;. Passed a resource string describing what you are looking for, along with extra optional information such as the default extension, what datafile to look inside, what the datafile object name is likely to be, any special environment variable to check, and any subdirectory that you would like to check as well as the default location, this function looks in a hell of a lot of different places :-). Pass NULL for the parameters you are not using. </p>
<p> Check the documentation chapter specific to your platform for information on additional paths this function might search for. Also, don&#8217;t forget about set_allegro_resource_path() to extend the searches. Example: </p>
<pre><code>
char path[256];
int ret;
ret = find_allegro_resource(path, "scores.cfg", NULL, NULL,
                            NULL, NULL, NULL, sizeof(path));
if (ret == 0) {
    /* Found system wide scores file. */
} else {
    /* No previous scores, create our own file. */
}
</code></pre>
<h2>RETURN VALUE</h2>
<p> Returns zero on success, and stores a full path to the file (at most size bytes) into the dest buffer. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-set_allegro_resource_path/">set_allegro_resource_path</a></code>(3) </p>
<h2>Index</h2>
