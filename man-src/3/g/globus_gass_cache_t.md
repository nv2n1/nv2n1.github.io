---
title: "globus_gass_cache_t(3)"
name: "globus_gass_cache_t"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gass_cache_t/"
description: "Globus GASS Cache –"
---

<h2 class="name">NAME</h2>
<p> Globus GASS Cache &#8211; </p>
<h3>Macros</h3>
<p> #define <code>GLOBUS_GASS_CACHE_MODULE</code> (&amp;globus_i_gass_cache_module)<br />
 <i>module_descriptor </i></p>
<h3>Typedefs</h3>
<p> typedef struct<br />
 globus_i_gass_cache_t * <code>globus_gass_cache_t</code>&quot;<br />
 <i>GASS Cache Handle. </i></p>
<h3>Functions</h3>
<p> int <code>globus_gass_cache_open</code> (const char *cache_directory_path, <code>globus_gass_cache_t</code> *cache_handlep)<br />
 <i>Open a GASS Cache. </i><br />
 int <code>globus_gass_cache_close</code> (<code>globus_gass_cache_t</code> *cache_handlep)<br />
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
 int <code>globus_gass_cache_get_cache_dir</code> (const <code>globus_gass_cache_t</code> cache_handle, char **cache_dir)<br />
 <i>Get the GASS Cache&#8217;s root directory. </i><br />
 int <code>globus_gass_cache_get_dirs</code> (const <code>globus_gass_cache_t</code> cache_handle, const char *url, const char *tag, char **global_root, char **local_root, char **tmp_root, char **log_root, char **global_dir, char **local_dir)<br />
 <i>Get the set of directories used by a GASS Cache. </i><br />
 int <code>globus_gass_cache_get_cache_type_string</code> (const <code>globus_gass_cache_t</code> cache_handle, char **cache_type)<br />
 <i>Get the type of GASS Cache directory layout. </i><br />
 const char * <code>globus_gass_cache_error_string</code> (int error_code)<br />
 <i>Look up the error string corresponding to a GASS Cache error. </i></p>
<h2>Detailed Description</h2>
<p> The GASS cache management API is part of the Globus module called &#8216;GASS&#8217;, (Global Access to Secondary Storage) The GASS cache management API defines calls for manipulating a local file cache. </p>
<p> Each cache entry can be locked during addition and deletion to allow for atomic handling of the cache file contents. </p>
<p> Each cache entry also has an associated timestamp. This timestamp is independent of the local cache file&#8217;s modification time. Rather, the cache entry timestamp is maintained by the user. It can, for example, be used to keep track of the timestamp of a remote file that is associated with the cache entry. </p>
<p> Note: all timestamps are as seconds since the epoch. (01 Jan 1970, 00:00 GMT) </p>
<p> The following functions are part of the API: </p>
<dl>
<dt>&bull;</p>
<dd> <code>globus_gass_cache_open()</code></p>
<dt>&bull;</p>
<dd> <code>globus_gass_cache_close()</code></p>
<dt>&bull;</p>
<dd> <code>globus_gass_cache_add()</code></p>
<dt>&bull;</p>
<dd> <code>globus_gass_cache_add_done()</code></p>
<dt>&bull;</p>
<dd> <code>globus_gass_cache_delete_start()</code></p>
<dt>&bull;</p>
<dd> <code>globus_gass_cache_delete()</code></p>
<dt>&bull;</p>
<dd> <code>globus_gass_cache_cleanup_tag()</code></p>
<dt>&bull;</p>
<dd> <code>globus_gass_cache_cleanup_tag_all()</code></p>
<dt>&bull;</p>
<dd> <code>globus_gass_cache_mangle_url()</code></p>
<dt>&bull;</p>
<dd> <code>globus_gass_cache_mangle_tag()</code></p>
<dt>&bull;</p>
<dd> <code>globus_gass_cache_get_dirs()</code></p>
<dt>&bull;</p>
<dd> <code>globus_gass_cache_get_cache_dir()</code></dl>
<h2>Typedef Documentation</h2>
<h3>typedef struct globus_i_gass_cache_t* <code>globus_gass_cache_t</code></h3>
<p> GASS Cache Handle. Data structure used to store information concerning an open cache directory. This structure MUST NOT be modified directly, but passed to the globus_gass_cache functions</p>
<h2>Function Documentation</h2>
<h3>int globus_gass_cache_add (<code>globus_gass_cache_t</code>cache_handle, const char *url, const char *tag, globus_bool_tcreate, unsigned long *timestamp, char **local_filename)</h3>
<p> Add a tag to an URL in the cache. Create a new cache file or add a tag on it. </p>
<p> If the URL is already in the cache but is locked, then this call will block until the cache entry is unlocked, then will proceed with the subsequent operations. </p>
<p> If the URL is already in the cache and unlocked, then add the tag to the cache entry&#8217;s tag list, return the local cache filename in *local_filename, return the entry&#8217;s current timestamp in *timestamp, lock the cache entry, and return GLOBUS_GASS_CACHE_ADD_EXISTS. </p>
<p> If the URL is not in the cache, and create==GLOBUS_TRUE, then create a new unique empty local cache file, add it to the cache with the specified tag, return the filename in *local_filename, return *timestamp set to GLOBUS_GASS_CACHE_TIMESTAMP_UNKNOWN, lock the cache entry, and return GLOBUS_GASS_CACHE_ADD_NEW. </p>
<p> If the URL is not in the cache, and create==GLOBUS_FALSE, then do not add it to the cache, and return GLOBUS_GASS_CACHE_URL_NOT_FOUND. </p>
<p> If this function returns GLOBUS_GASS_CACHE_ADD_EXISTS or GLOBUS_GASS_CACHE_ADD_NEW, then <code>globus_gass_cache_add_done()</code> or <code>globus_gass_cache_delete()</code> must be subsequently called to unlock the cache entry. </p>
<p> Subsequent calls to <code>globus_gass_cache_add()</code> and <code>globus_gass_cache_delete_start()</code> on the same cache and url, made either from this process or another, will block until the cache entry is unlocked. </p>
<p> If tag==NULL, then a tag with the value &#8216;null&#8217; will be added to the cache entry&#8217;s tag list. </p>
<p> The same tag can be used multiple times, in which case this tag will be added to the entry&#8217;s tag list multiple times. </p>
<p> Note: It is recommended that proglobus_grams started via GLOBUS_GRAM pass a tag value of getenv(&#8216;GLOBUS_GRAM_JOB_CONTACT&#8217;), since upon completion of a job GLOBUS_GRAM will automatically cleanup entries with this tag. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> the local_filename MUST be free by the user in a subsequent operation, using free()</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>cache_handle</i> Handle to the opened cache directory to use.<br />
 <i>url</i> URL of the file to be cached. It is used as the main key to the cache entries.<br />
 <i>tag</i> Tag specifying which job is/are using the cache. This is usually the GLOBUS_GRAM_JOB_CONTACT. Can be NULL or empty; the tag &#8216;null&#8217; is then used. create &#8211; Tells if the cache entry should be created if it is not already existing.<br />
 <i>create</i> Flag to create if it does not already exist.<br />
 <i>timestamp</i> Timestamp of the cached file, set by globus_gass_cache_done(), (or <code>globus_gass_cache_delete()</code> ).<br />
 <i>local_filename</i> Path the the local file caching the file specified by &#8216;url&#8217;. NULL if &#8216;url&#8217; not yet cached and creation not requested (create false).</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> GLOBUS_GASS_CACHE_URL_NOT_FOUND</p>
<dt>&bull;</p>
<dd> GLOBUS_GASS_CACHE_ADD_NEW</p>
<dt>&bull;</p>
<dd> GLOBUS_GASS_CACHE_ADD_EXISTS</p>
<dt>&bull;</p>
<dd> or any of the defined gass error code.</dl>
</dl>
<h3>int globus_gass_cache_add_done (<code>globus_gass_cache_t</code>cache_handle, const char *url, const char *tag, unsigned longtimestamp)</h3>
<p> Complete adding a cache entry and unlock it. <code>globus_gass_cache_add_done()</code> MUST be called after <code>globus_gass_cache_add()</code>, to set the timestamp in the cache entry for the URL, and then unlock the cache entry. (The only case it does not need to be called is if <code>globus_gass_cache_add()</code> has returned GLOBUS_GASS_CACHE_URL_NOT_FOUND, of course. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>cache_handle</i> Handle to the opened cache directory to use.<br />
 <i>url</i> URL of the cached file to set as &#8216;done&#8217; (unlock)<br />
 <i>tag</i> Tag specifying which job has locked the cache and must therefore be unlocked. It is an error to call this function with a tag which does not currently own the cache lock.<br />
 <i>timestamp</i> Timestamp of the cached file.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> <code>globus_gass_cache_add_done()</code> returns GLOBUS_SUCCESS or any of the defined GASS Cache error codes.</dl>
<h3>int globus_gass_cache_cleanup_tag (<code>globus_gass_cache_t</code>cache_handle, const char *url, const char *tag)</h3>
<p> Remove a tag from a cache entry. Remove all instances of the tag from the cache entry&#8217;s tag list. If there are no more tags in the tag list, then remove this cache entry and delete the associated local cache file. If the cache entry is locked with the same tag as is passed to this function, then the entry is unlocked after removing the tags. Otherwise, the cache entry&#8217;s lock is left untouched. </p>
<p> This function does not block on a locked reference. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> The GLOBUS_GRAM job manager will automatically call this function with a tag of getenv(&#8216;GLOBUS_GRAM_JOB_CONTACT&#8217;) upon completion of a job.</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>cache_handle</i> Handle to the opened cache directory to use.<br />
 <i>url</i> URL of the file to be cached. It is used as the main key to the cache entries.<br />
 <i>tag</i> Tag specifying which job is/are using the cache. This is usually the GLOBUS_GRAM_JOB_CONTACT. Can be NULL or empty; the tag &#8216;null&#8217; is then used.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The <code>globus_gass_cache_cleanup_tag()</code> function returns GLOBUS_SUCCESS or any of the defined GASS Cache error codes.</dl>
<h3>int globus_gass_cache_cleanup_tag_all (<code>globus_gass_cache_t</code>cache_handle, char *tag)</h3>
<p> Remove a tag from all cache entries </p>
<p> Remove all instances of the tag from the cache entry&#8217;s tag list. If there are no more tags in the tag list, then remove this cache entry and delete the associated local cache file. If the cache entry is locked with the same tag as is passed to this function, then the entry is unlocked after removing the tags. Otherwise, the cache entry&#8217;s lock is left untouched. This function does not block on a locked reference. This function differs from <code>globus_gass_cache_cleanup_tag()</code> in that this cleans up <code>all</code> URLs related with this tag. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> The GLOBUS_GRAM job manager will automatically call this function with a tag of getenv(&#8216;GLOBUS_GRAM_JOB_CONTACT&#8217;) upon completion of a job.</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>cache_handle</i> Handle to the opened cache directory to use.<br />
 <i>tag</i> Tag specifying which job is/are using the cache. This is usually the GLOBUS_GRAM_JOB_CONTACT. Can be NULL or empty; the tag &#8216;null&#8217; is then used.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The <code>globus_gass_cache_cleanup_tag_all()</code> function returns GLOBUS_SUCCESS or any of the defined GASS Cache error codes.</dl>
<h3>int globus_gass_cache_close (<code>globus_gass_cache_t</code> *cache_handlep)</h3>
<p> Close a cache handle. Close (NOT delete) a previously opened cache:</p>
<dl>
<dt>&bull;</p>
<dd> close the opened files and</p>
<dt>&bull;</p>
<dd> free the memory allocated for the cache_handle.</p>
<dt>&bull;</p>
<dd> mark the handle as &#8216;not initialized&#8217;.</dl>
<p> Parameters: cache_handle: Handle to the opened cache directory to use. </p>
<p> cache_handle-&gt;is_init set to &#8216;not initialized&#8217; and all the files opened bu globus_gass_cache_open are closed . </p>
<p> Returns: GLOBUS_SUCCESS or error code: GLOBUS_GASS_CACHE_ERROR_CACHE_NOT_OPENED</p>
<h3>int globus_gass_cache_delete (<code>globus_gass_cache_t</code>cache_handle, const char *url, const char *tag, unsigned longtimestamp, globus_bool_tis_locked)</h3>
<p> Remove one instance of the tag from the cache entry&#8217;s tag list. If there are no more tags in the tag list, then remove this cache entry and delete the associated local cache file. </p>
<p> Otherwise, update the timestamp to the passed value. </p>
<p> This call will leave the cache entry unlocked. </p>
<p> If is_locked==GLOBUS_TRUE, then this cache entry was locked during a previous call to <code>globus_gass_cache_add()</code> or <code>globus_gass_cache_delete_start()</code>. The cache file should be locked by the corresponding url/tag, or an error is returned. If it is locked by the corresponding url/tag, then the normal operation occur, whithout blocking (remove one instance from the tag update the timestamp and unlock the cache). </p>
<p> If is_locked==GLOBUS_FALSE, eventually wait the cache is not locked any more, and then proceed with the normal operations.(remove one instance from the tag list and update the timestamp). </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>cache_handle</i> Handle to the opened cache directory to use.<br />
 <i>url</i> URL of the file to be cached. It is used as the main key to the cache entries.<br />
 <i>tag</i> Tag specifying which job is/are using the cache. This is usually the GLOBUS_GRAM_JOB_CONTACT. Can be NULL or empty; the tag &#8216;null&#8217; is then used.<br />
 <i>timestamp</i> Timestamp of the cached file.<br />
 <i>is_locked</i> Indicate if this cache entry was locked during a previous call to <code>globus_gass_cache_add()</code> or <code>globus_gass_cache_delete_start()</code>.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The <code>globus_gass_cache_delete()</code> function returns GLOBUS_SUCCESS or any of the defined GASS Cache error codes.</dl>
<h3>int globus_gass_cache_delete_start (<code>globus_gass_cache_t</code>cache_handle, const char *url, const char *tag, unsigned long *timestamp)</h3>
<p> Remove a cache tag. Lock the cache entry for the URL, and return the cache entry&#8217;s current timestamp in *timestamp. This function will block if the data file is already locked, until it is unlocked. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>cache_handle</i> Handle to the opened cache directory to use.<br />
 <i>url</i> URL of the cached file to set as &#8216;done&#8217; (unlock)<br />
 <i>tag</i> Tag specifying which job has locked the cache and must therefore be unlocked. It is an error to call this function with a tag which does not currently own the cache lock.<br />
 <i>timestamp</i> Timestamp of the cached file, set by globus_gass_cache_done(), (or <code>globus_gass_cache_delete()</code> ).</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The <code>globus_gass_cache_delete_start()</code> function returns GLOBUS_SUCCESS or any of the defined GASS Cache error code.</dl>
<h3>const char* globus_gass_cache_error_string (interror_code)</h3>
<p> Look up the error string corresponding to a GASS Cache error. Return a pointer on an error description string. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>error_code</i> error code returned by a previously called globus_gass_cache function.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The <code>globus_gass_cache_error_string()</code> function returns a pointer to an error message, or NULL if error_code is invalid.</dl>
<h3>int globus_gass_cache_get_cache_dir (const <code>globus_gass_cache_t</code>cache_handle, char **cache_dir)</h3>
<p> Get the GASS Cache&#8217;s root directory. Get a the root cache of directory. This is exported for use in the globus_gass_cache program. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>cache_handle</i> Handle to the opened cache directory to use.<br />
 <i>cache_dir</i> Pointer to the cache directory</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Success<br />
 <i>GLOBUS_GASS_CACHE_ERROR_NO_MEMORY</i> No memory</dl>
<h3>int globus_gass_cache_get_cache_type_string (const <code>globus_gass_cache_t</code>cache_handle, char **cache_type)</h3>
<p> Get the type of GASS Cache directory layout. Get a string which describes the cache type (&#8216;normal&#8217; or &#8216;flat&#8217;) </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>cache_handle</i> Handle to the opened cache directory to use.<br />
 <i>cache_type</i> Pointer to the strdup()ed string</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Success<br />
 <i>GLOBUS_GASS_CACHE_ERROR_NO_MEMORY</i> No memory</dl>
<h3>int globus_gass_cache_get_dirs (const <code>globus_gass_cache_t</code>cache_handle, const char *url, const char *tag, char **global_root, char **local_root, char **tmp_root, char **log_root, char **global_dir, char **local_dir)</h3>
<p> Get the set of directories used by a GASS Cache. Gets a bunch of directories. This is exported for use in the globus_gass_cache program. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>cache_handle</i> Handle to the opened cache directory to use.<br />
 <i>url</i> The incoming URL<br />
 <i>tag</i> The incoming tag<br />
 <i>local_root</i> Pointer to the &#8216;local root&#8217; directory<br />
 <i>global_root</i> Pointer to the &#8216;global root&#8217; directory<br />
 <i>tmp_root</i> Pointer to the &#8216;tmp root&#8217; directory<br />
 <i>log_root</i> Pointer to the root log directory<br />
 <i>local_dir</i> Pointer to the related &#8216;local&#8217; directory<br />
 <i>global_dir</i> Pointer to the related &#8216;global&#8217; directory</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Success<br />
 <i>GLOBUS_GASS_CACHE_ERROR_NO_MEMORY</i> No memory</dl>
<h3>int globus_gass_cache_mangle_tag (const <code>globus_gass_cache_t</code>cache_handle, const char *tag, char **mangled_tag, int *length)</h3>
<p> Convert a tag to a string suitable as a file path. Mangles the given tag into a chunk suitable for using as a file / path name. This is exported for use in the globus_gass_cache program. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>cache_handle</i> Handle to the opened cache directory to use.<br />
 <i>tag</i> The incoming tag to mangle (NULL-terminated)<br />
 <i>mangled_tag</i> Pointer to the output string; a buffer for the real string is malloc()ed for the application. If mangled is NULL, then no such buffer is allocated, and no mangled string is created. This can be useful to just get the length of the mangled string.<br />
 <i>length</i> A pointer to the length of the resulting string. If NULL, this is not assigned to.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Success<br />
 <i>GLOBUS_GASS_CACHE_ERROR_NO_MEMORY</i> No memory</dl>
<h3>int globus_gass_cache_mangle_url (const <code>globus_gass_cache_t</code>cache_handle, const char *url, char **mangled_url, int *length)</h3>
<p> Convert a URL to a string suitable as a file path. Mangles the given URL into a chunk suitable for using as a file / path name. This is exported for use in the globus_gass_cache program. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>cache_handle</i> Handle to the opened cache directory to use.<br />
 <i>url</i> The incoming URL to mangle (NULL-terminated)<br />
 <i>mangled_url</i> Pointer to the output string; a buffer for the real string is malloc()ed for the application. If mangled is NULL, then no such buffer is allocated, and no mangled string is created. This can be useful to just get the length of the mangled string.<br />
 <i>length</i> A pointer to the length of the resulting string. If NULL, this is not assigned to.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Success<br />
 <i>GLOBUS_GASS_CACHE_ERROR_NO_MEMORY</i> No memory</dl>
<h3>int globus_gass_cache_open (const char *cache_directory_path, <code>globus_gass_cache_t</code> *cache_handlep)</h3>
<p> Open a GASS Cache. Open the cache specified by the cache_directory_path argument, and return a cache handle that can be used in subsequent cache calls. </p>
<p> If cache_directory_path is NULL, then use the value contained in the GLOBUS_GASS_CACHE_DEFAULT environment variable if it is defined, otherwise use ~/.globus_gass_cache. </p>
<p> The cache_directory_path must be a directory. If it is a file, this call will fail with a non-0 return value. </p>
<p> If the specified directory does not exist, then this call will create the directory. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>cache_directory_path</i> Path to the cache directory to open. Can be NULL (see above)<br />
 <i>cache_handlep</i> Structure containning all the necessary information to access the cache (file names, descriptor,&#8230;) (see globus_gass_gache.h) Some files are also opened: <code>globus_gass_cache_close()</code> must be called subsequently to close those files. This parameter is modified by the <code>globus_gass_cache_open()</code></dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Success<br />
 <i>GLOBUS_GASS_CACHE_ERROR_CACHE_ALREADY_OPENED</i> Handle already opened<br />
 <i>GLOBUS_GASS_CACHE_ERROR_NAME_TOO_LONG</i> Path name too long<br />
 <i>GLOBUS_GASS_CACHE_ERROR_NO_HOME</i> Can&#8217;t find home directory for default cache path</dl>
<h3>int globus_gass_cache_query (<code>globus_gass_cache_t</code>cache_handle, const char *url, const char *tag, globus_bool_twait_for_lock, unsigned long *timestamp, char **local_filename, globus_bool_t *is_locked)</h3>
<p> Query the GASS Cache. Query if an item is in the cache </p>
<p> This call will block only if wait_for_lock is GLOBUS_TRUE </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>cache_handle</i> Handle to the opened cache directory to use.<br />
 <i>url</i> URL of the file to query. It is used as the main key to the cache entries.<br />
 <i>tag</i> Tag specifying which job is/are using the cache. This is usually the GLOBUS_GRAM_JOB_CONTACT. Can be NULL or empty; the tag &#8216;null&#8217; is then used.<br />
 <i>wait_for_lock</i> If GLOBUS_TRUE, wait for any lock existing lock to be released. If GLOBUS_FALSE, doesn&#8217;t wait for a lock to be released.<br />
 <i>timestamp</i> Timestamp of the cached file, set by globus_gass_cache_done(), (or <code>globus_gass_cache_delete()</code> ).<br />
 <i>local_filename</i> Path the the local file caching the file specified by &#8216;url&#8217;. NULL if &#8216;url&#8217; not yet cached and creation not requested (create false).<br />
 <i>is_locked</i> GLOBUS_TRUE if the file is currently (at return time) locked.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The <code>globus_gass_cache_query()</code> function returns GLOBUS_SUCCESS, GLOBUS_GASS_CACHE_URL_NOT_FOUND, or any of the defined gass error code.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_gass_cache from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAI">Function Documentation</a></p>
<dd>
<dt><a href="#lbAY">Author</a></p>
<dd></dl>
