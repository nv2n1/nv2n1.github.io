---
title: "globus_gass_cache-h(3)"
name: "globus_gass_cache-h"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gass_cache-h/"
description: "globus_gass_cache.h – GASS Cache API."
---

<p>globus_gass_cache.h &#8211; GASS Cache API.</p>
<h2>Synopsis</h2>
<p>#include &#8216;globus_common.h&#8217;<br />
 #include &lt;sys/param.h&gt; </p>
<h3>Macros</h3>
<p>#define <code>GLOBUS_GASS_CACHE_MODULE</code> (&amp;globus_i_gass_cache_module)<br />
 <i>module_descriptor </i></p>
<h3>Typedefs</h3>
<p>typedef struct<br />
 globus_i_gass_cache_t * <code>globus_gass_cache_t</code>&quot;<br />
 <i>GASS Cache Handle. </i></p>
<h3>Functions</h3>
<p>int <code>globus_gass_cache_open</code> (const char *cache_directory_path, <code>globus_gass_cache_t</code> *cache_handle)<br />
 <i>Open a GASS Cache. </i><br />
 int <code>globus_gass_cache_close</code> (<code>globus_gass_cache_t</code> *cache_handle)<br />
 <i>Close a cache handle. </i><br />
 int <code>globus_gass_cache_add</code> (<code>globus_gass_cache_t</code> cache_handle, const char *url, const char *tag, globus_bool_t create, unsigned long *timestamp, char **local_filename)<br />
 <i>Add a tag to an URL in the cache. </i><br />
 int <code>globus_gass_cache_add_done</code> (<code>globus_gass_cache_t</code> cache_handle, const char *url, const char *tag, unsigned long timestamp)<br />
 <i>Complete adding a cache entry and unlock it. </i><br />
 int <code>globus_gass_cache_query</code> (<code>globus_gass_cache_t</code> cache_handle, const char *url, const char *tag, globus_bool_t wait_for_lock, unsigned long *timestamp, char **local_filename, globus_bool_t *is_locked)<br />
 <i>Query the GASS Cache. </i><br />
 int <code>globus_gass_cache_delete_start</code> (<code>globus_gass_cache_t</code> cache_handle, const char *url, const char *tag, unsigned long *timestamp)<br />
 <i>Remove a cache tag. </i><br />
 int <code>globus_gass_cache_delete</code> (<code>globus_gass_cache_t</code> cache_handle, const char *url, const char *tag, unsigned long timestamp, globus_bool_t is_locked)<br />
 <i>Remove one instance of the tag from the cache entry&#8217;s tag list. </i><br />
 int <code>globus_gass_cache_cleanup_tag</code> (<code>globus_gass_cache_t</code> cache_handle, const char *url, const char *tag)<br />
 <i>Remove a tag from a cache entry. </i><br />
 int <code>globus_gass_cache_cleanup_tag_all</code> (<code>globus_gass_cache_t</code> cache_handle, char *tag)<br />
 <i>Remove a tag from all cache entries</i> </p>
<p> Remove all instances of the tag from the cache entry&#8217;s tag list. If there are no more tags in the tag list, then remove this cache entry and delete the associated local cache file. If the cache entry is locked with the same tag as is passed to this function, then the entry is unlocked after removing the tags. Otherwise, the cache entry&#8217;s lock is left untouched. &quot;<br />
 int <code>globus_gass_cache_mangle_url</code> (const <code>globus_gass_cache_t</code> cache_handle, const char *url, char **mangled_url, int *length)<br />
 <i>Convert a URL to a string suitable as a file path. </i><br />
 int <code>globus_gass_cache_mangle_tag</code> (const <code>globus_gass_cache_t</code> cache_handle, const char *tag, char **mangled_tag, int *length)<br />
 <i>Convert a tag to a string suitable as a file path. </i><br />
 int <code>globus_gass_cache_get_dirs</code> (const <code>globus_gass_cache_t</code> cache_handle, const char *url, const char *tag, char **global_root, char **local_root, char **tmp_root, char **log_root, char **global_dir, char **local_dir)<br />
 <i>Get the set of directories used by a GASS Cache. </i><br />
 int <code>globus_gass_cache_get_cache_dir</code> (const <code>globus_gass_cache_t</code> cache_handle, char **cache_dir)<br />
 <i>Get the GASS Cache&#8217;s root directory. </i><br />
 int <code>globus_gass_cache_get_cache_type_string</code> (const <code>globus_gass_cache_t</code> cache_handle, char **cache_type)<br />
 <i>Get the type of GASS Cache directory layout. </i><br />
 const char * <code>globus_gass_cache_error_string</code> (int error_code)<br />
 <i>Look up the error string corresponding to a GASS Cache error. </i></p>
<h2>Detailed Description</h2>
<p>GASS Cache API. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus_gass_cache from the source code.</p>
