---
title: "list_config_entries(3)"
name: "list_config_entries"
section: "3"
letter: "l"
url: "/docs/linux/man/3-list_config_entries/"
description: "list_config_entries – Lists the names of all entries in a config section Allegro game programming library."
---

<h2>NAME</h2>
<p> list_config_entries &#8211; Lists the names of all entries in a config section Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int list_config_entries(const char *section, const char ***names);</code></p>
<h2>DESCRIPTION</h2>
<p> This function can be used to get a list of all entries in the given config section. The names parameter is a pointer to an array of strings. If it points to a NULL pointer, the list will be allocated, else it will be re-allocated. You should free the list again with free_config_entries if you don&#8217;t need it anymore, or you can pass it again to list_config_entries and the memory will be re-used. See the following example for how you can use it, it will print out the complete contents of the current configuration: </p>
<pre><code>
int i, n;
char const **sections = NULL;
char const **entries = NULL;

/* List all entries not in any section. */
n = list_config_entries(NULL, &amp;entries);
   for (i = 0; i 
      printf(" %s=\"%s\"
", entries[i], get_config_string(
             NULL, entries[i], "-"));
   
   /* List all sections (and entries in them). */
   n = list_config_sections(&amp;sections);
   /* loop through all section names */
   for (i = 0; i 
   {
    int j, m;
    printf("%s
", sections[i]);
    m = list_config_entries(sections[i], &amp;entries);
    /* loop through all entries in the section */
      for (j = 0; j 
      {
        printf(" %s=\"%s\"
", entries[j], get_config_string(sections[i], entries[j], "-"));
      }
   }
   /* It is enough to free the arrays once at the end. */
   free_config_entries(&amp;sections);
   free_config_entries(&amp;entries);
</code></pre>
<h2>RETURN VALUE</h2>
<p> Returns the number of valid strings in the names array. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-set_config_file/">set_config_file</a></code>(3), <code><a href="/docs/linux/man/3-get_config_string/">get_config_string</a></code>(3), <code><a href="/docs/linux/man/3-list_config_sections/">list_config_sections</a></code>(3), <code><a href="/docs/linux/man/3-free_config_entries/">free_config_entries</a></code>(3) </p>
<h2>Index</h2>
