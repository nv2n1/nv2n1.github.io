---
title: "ecore_file(3)"
name: "ecore_file"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_file/"
description: "Ecore_File.h – Files utility functions."
---

<p>Ecore_File.h &#8211; Files utility functions. </p>
<h2>Synopsis</h2>
<h3>Functions</h3>
<p>EAPI int <code>ecore_file_init</code> (void)<br />
 <i>Initialize Ecore_File and the services it will use. </i><br />
 EAPI int <code>ecore_file_shutdown</code> (void)<br />
 <i>Shutdown the Ecore_File. </i><br />
 EAPI long long <code>ecore_file_mod_time</code> (const char *file)<br />
 <i>Get the time of the last modification to the give file. </i><br />
 EAPI long long <code>ecore_file_size</code> (const char *file)<br />
 <i>Get the size of the given file. </i><br />
 EAPI int <code>ecore_file_exists</code> (const char *file)<br />
 <i>Check if file exists. </i><br />
 EAPI int <code>ecore_file_is_dir</code> (const char *file)<br />
 <i>Check if file is a directory. </i><br />
 EAPI int <code>ecore_file_mkdir</code> (const char *dir)<br />
 <i>Create a new directory. </i><br />
 EAPI int <code>ecore_file_rmdir</code> (const char *dir)<br />
 <i>Delete the given dir. </i><br />
 EAPI int <code>ecore_file_recursive_rm</code> (const char *dir)<br />
 <i>Delete a directory and all its contents. </i><br />
 EAPI int <code>ecore_file_mkpath</code> (const char *path)<br />
 <i>Create a complete path. </i><br />
 EAPI int <code>ecore_file_cp</code> (const char *src, const char *dst)<br />
 <i>Copy a file. </i><br />
 EAPI int <code>ecore_file_mv</code> (const char *src, const char *dst)<br />
 <i>Move a file. </i><br />
 EAPI int <code>ecore_file_symlink</code> (const char *src, const char *dest)<br />
 <i>Create a symbolic link. </i><br />
 EAPI char * <code>ecore_file_realpath</code> (const char *file)<br />
 <i>Get the canonicalized absolute pathname. </i><br />
 EAPI int <code>ecore_file_unlink</code> (const char *file)<br />
 <i>Delete the given file. </i><br />
 EAPI const char * <code>ecore_file_file_get</code> (const char *path)<br />
 <i>Get the filename from a give path. </i><br />
 EAPI char * <code>ecore_file_dir_get</code> (const char *path)<br />
 <i>Get the directory where file reside. </i><br />
 EAPI int <code>ecore_file_can_read</code> (const char *file)<br />
 <i>Check if file can be read. </i><br />
 EAPI int <code>ecore_file_can_write</code> (const char *file)<br />
 <i>Check if file can be written. </i><br />
 EAPI int <code>ecore_file_can_exec</code> (const char *file)<br />
 <i>Check if file can be executed. </i><br />
 EAPI char * <code>ecore_file_readlink</code> (const char *link)<br />
 <i>Get the path pointed by link. </i><br />
 EAPI Ecore_List * <code>ecore_file_ls</code> (const char *dir)<br />
 <i>Get the list of the files and directories in a given directory. </i><br />
 EAPI char * <code>ecore_file_app_exe_get</code> (const char *app)<br />
 <i>FIXME: To be documented. </i><br />
 EAPI char * <code>ecore_file_escape_name</code> (const char *filename)<br />
 <i>Add the escape sequence (&#8216;\&#8217;) to the given filename. </i><br />
 EAPI char * <code>ecore_file_strip_ext</code> (const char *file)<br />
 <i>Remove the extension from a given path. </i><br />
 EAPI int <code>ecore_file_dir_is_empty</code> (const char *dir)<br />
 <i>Check if the given directory is empty. </i><br />
 EAPI Ecore_File_Monitor * <code>ecore_file_monitor_add</code> (const char *path, void(*func)(void *data, Ecore_File_Monitor *em, Ecore_File_Event event, const char *path), void *data)<br />
 <i>Monitor a path using inotify or polling. </i><br />
 EAPI void <code>ecore_file_monitor_del</code> (Ecore_File_Monitor *ecore_file_monitor)<br />
 <i>Stop monitoring a path. </i><br />
 EAPI const char * <code>ecore_file_monitor_path_get</code> (Ecore_File_Monitor *ecore_file_monitor)<br />
 <i>Get the monitored path. </i><br />
 EAPI int <code>ecore_file_path_dir_exists</code> (const char *in_dir)<br />
 <i>Check if the given directory is in PATH. </i><br />
 EAPI int <code>ecore_file_app_installed</code> (const char *exe)<br />
 <i>Check if the given application is installed. </i><br />
 EAPI Ecore_List * <code>ecore_file_app_list</code> (void)<br />
 <i>Get a list of all the applications installed on the system. </i><br />
 EAPI int <code>ecore_file_download</code> (const char *url, const char *dst, void(*completion_cb)(void *data, const char *file, int status), int(*progress_cb)(void *data, const char *file, long int dltotal, long int dlnow, long int ultotal, long int ulnow), void *data)<br />
 <i>Download </i>url to the given dst.<br />
 EAPI int <code>ecore_file_download_protocol_available</code> (const char *protocol)<br />
 <i>Check if the given protocol is available. </i></p>
<h2>Detailed Description</h2>
<p>Files utility functions. </p>
<h2>Function Documentation</h2>
<h3>EAPI int ecore_file_app_installed (const char * exe)</h3>
<p>Check if the given application is installed. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>exe</i> The name of the application</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 if the exe is in PATH and is executable</dl>
<p> This function check if the given name exist in PATH and is executable </p>
<p> References ecore_file_app_installed(), ecore_list_first_goto(), and ecore_list_next(). </p>
<p> Referenced by ecore_file_app_installed().</p>
<h3>EAPI Ecore_List* ecore_file_app_list (void)</h3>
<p>Get a list of all the applications installed on the system. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>An Ecore_List containing all the executable files in the system</dl>
<p> References ecore_file_app_list(), ecore_list_append(), ecore_list_destroy(), ecore_list_first_goto(), ecore_list_free_cb_set(), ecore_list_new(), and ecore_list_next(). </p>
<p> Referenced by ecore_file_app_list().</p>
<h3>EAPI int ecore_file_can_exec (const char * file)</h3>
<p>Check if file can be executed. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>file</i> The name of the file</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 if the file can be executed, 0 otherwise</dl>
<h3>EAPI int ecore_file_can_read (const char * file)</h3>
<p>Check if file can be read. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>file</i> The name of the file</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 if the file is readable, 0 otherwise</dl>
<h3>EAPI int ecore_file_can_write (const char * file)</h3>
<p>Check if file can be written. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>file</i> The name of the file</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 if the file is writable, 0 otherwise</dl>
<h3>EAPI int ecore_file_cp (const char * src, const char * dst)</h3>
<p>Copy a file. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>src</i> The name of the source file<br />
 <i>dst</i> The name of the destination file</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success, 0 on failure</dl>
<h3>EAPI char* ecore_file_dir_get (const char * file)</h3>
<p>Get the directory where file reside. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>file</i> The name of the file</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The directory name</dl>
<h3>EAPI int ecore_file_dir_is_empty (const char * dir)</h3>
<p>Check if the given directory is empty. </p>
<p> The &#8216;.&#8217; and &#8216;..&#8217; files will be ignored. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>dir</i> The name of the directory to check</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 if directory is empty, 0 if it has at least one file or -1 in case of errors</dl>
<h3>EAPI int ecore_file_download (const char * url, const char * dst, void(*)(void *data, const char *file, int status) completion_cb, int(*)(void *data, const char *file, long int dltotal, long int dlnow, long int ultotal, long int ulnow) progress_cb, void * data)</h3>
<p>Download url to the given dst. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>url</i> The complete url to download<br />
 <i>dst</i> The local file to save the downloaded to<br />
 <i>completion_cb</i> A callback called on download complete<br />
 <i>progress_cb</i> A callback called during the download operation</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 if the download start or 0 on failure</dl>
<p> You must provide the full url, including &#8216;<a rel="nofollow" href="http://',">http://&#8217;,</a> &#8216;<a href="ftp://'">ftp://&#8217;</a> or &#8216;file://&#8217;. </p>
<p>&nbsp;<wbr>If dst already exist it will not be overwritten and the function will fail. </p>
<p>&nbsp;<wbr>Ecore must be compiled with CURL to download using http and ftp protocols.&nbsp;<wbr> </p>
<p> References ecore_file_download(). </p>
<p> Referenced by ecore_file_download().</p>
<h3>EAPI int ecore_file_download_protocol_available (const char * protocol)</h3>
<p>Check if the given protocol is available. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>protocol</i> The protocol to check</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 if protocol is handled or 0 if not</dl>
<p> protocol can be &#8216;<a rel="nofollow" href="http://',">http://&#8217;,</a> &#8216;<a href="ftp://'">ftp://&#8217;</a> or &#8216;file://&#8217;. </p>
<p>&nbsp;<wbr>Ecore must be compiled with CURL to handle http and ftp protocols.&nbsp;<wbr> </p>
<p> References ecore_file_download_protocol_available(). </p>
<p> Referenced by ecore_file_download_protocol_available().</p>
<h3>EAPI char* ecore_file_escape_name (const char * filename)</h3>
<p>Add the escape sequence (&#8216;\&#8217;) to the given filename. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>filename</i> The file name</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The file name with special characters escaped; if the length of the resulting string is longer than PATH_MAX it will return NULL</dl>
<h3>EAPI int ecore_file_exists (const char * file)</h3>
<p>Check if file exists. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>file</i> The name of the file</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 if file exists on local filesystem, 0 otherwise</dl>
<h3>EAPI const char* ecore_file_file_get (const char * path)</h3>
<p>Get the filename from a give path. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>path</i> The complete path</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Only the file name</dl>
<h3>EAPI int ecore_file_init (void)</h3>
<p>Initialize Ecore_File and the services it will use. </p>
<p> Call this function once before you use any of the ecore file functions. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Return the number howoften <code>ecore_file_init()</code> was call succesfully; 0 if it failed.</dl>
<h3>EAPI int ecore_file_is_dir (const char * file)</h3>
<p>Check if file is a directory. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>file</i> The name of the file</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 if file exist and is a directory, 0 otherwise</dl>
<h3>EAPI Ecore_List* ecore_file_ls (const char * dir)</h3>
<p>Get the list of the files and directories in a given directory. </p>
<p> The list will be sorted with strcoll as compare function. That means that you may want to set the current locale for the category LC_COLLATE with setlocale(). For more information see the manual pages of strcoll and setlocale. The list will not contain the directory entries for &#8216;.&#8217; and &#8216;..&#8217;. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>dir</i> The name of the directory to list</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Return an Ecore_List containing all the files in the directory; on failure it returns NULL.</dl>
<p> References ecore_list_append(), ecore_list_first_goto(), ecore_list_free_cb_set(), ecore_list_new(), and ecore_list_sort().</p>
<h3>EAPI int ecore_file_mkdir (const char * dir)</h3>
<p>Create a new directory. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>dir</i> The name of the directory to create</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on successfull creation, 0 on failure</dl>
<p> The directory is created with the mode: S_IRUSR | S_IWUSR | S_IXUSR | S_IRGRP | S_IXGRP | S_IROTH | S_IXOTH</p>
<h3>EAPI int ecore_file_mkpath (const char * path)</h3>
<p>Create a complete path. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>path</i> The path to create</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success, 0 on failure</dl>
<h3>EAPI long long ecore_file_mod_time (const char * file)</h3>
<p>Get the time of the last modification to the give file. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>file</i> The name of the file</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Return the time of the last data modification, if an error should occur it will return 0</dl>
<h3>EAPI Ecore_File_Monitor* ecore_file_monitor_add (const char * path, void(*)(void *data, Ecore_File_Monitor *em, Ecore_File_Event event, const char *path) func, void * data)</h3>
<p>Monitor a path using inotify or polling. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>path</i> The path to monitor<br />
 <i>func</i> The function to call on changes<br />
 <i>data</i> The data passed to func</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>An Ecore_File_Monitor pointer or NULL on failure</dl>
<p> References ecore_file_monitor_add(). </p>
<p> Referenced by ecore_file_monitor_add().</p>
<h3>EAPI void ecore_file_monitor_del (Ecore_File_Monitor * em)</h3>
<p>Stop monitoring a path. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>em</i> The Ecore_File_Monitor to stop</dl>
<p> References ecore_file_monitor_del(). </p>
<p> Referenced by ecore_file_monitor_del().</p>
<h3>EAPI const char* ecore_file_monitor_path_get (Ecore_File_Monitor * em)</h3>
<p>Get the monitored path. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>em</i> The Ecore_File_Monitor to query</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The path that is monitored by em</dl>
<p> References ecore_file_monitor_path_get(). </p>
<p> Referenced by ecore_file_monitor_path_get().</p>
<h3>EAPI int ecore_file_mv (const char * src, const char * dst)</h3>
<p>Move a file. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>src</i> The name of the source file<br />
 <i>dst</i> The name of the destination file</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success, 0 on failure</dl>
<h3>EAPI int ecore_file_path_dir_exists (const char * in_dir)</h3>
<p>Check if the given directory is in PATH. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>The</i> name of the directory to search in PATH</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 if the directory exist in PATH, 0 otherwise</dl>
<p> References ecore_file_path_dir_exists(), ecore_list_first_goto(), and ecore_list_next(). </p>
<p> Referenced by ecore_file_path_dir_exists().</p>
<h3>EAPI char* ecore_file_readlink (const char * link)</h3>
<p>Get the path pointed by link. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>link</i> The name of the link</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The path pointed by link or NULL</dl>
<h3>EAPI char* ecore_file_realpath (const char * file)</h3>
<p>Get the canonicalized absolute pathname. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>file</i> The file path</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The canonicalized absolute pathname; on failure it will return an empty string</dl>
<h3>EAPI int ecore_file_recursive_rm (const char * dir)</h3>
<p>Delete a directory and all its contents. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>dir</i> The name of the directory to delete</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success, 0 on failure</dl>
<p> If dir is a link only the link is removed</p>
<h3>EAPI int ecore_file_rmdir (const char * dir)</h3>
<p>Delete the given dir. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>dir</i> The name of the directory to delete</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success, 0 on failure</dl>
<h3>EAPI int ecore_file_shutdown (void)</h3>
<p>Shutdown the Ecore_File. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>returns the number of libraries that still uses Ecore_File</dl>
<h3>EAPI long long ecore_file_size (const char * file)</h3>
<p>Get the size of the given file. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>file</i> The name of the file</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The size of the file in byte</dl>
<h3>EAPI char* ecore_file_strip_ext (const char * path)</h3>
<p>Remove the extension from a given path. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>path</i> The name of the file</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A newly allocated string with the extension stripped out or NULL on errors</dl>
<h3>EAPI int ecore_file_symlink (const char * src, const char * dest)</h3>
<p>Create a symbolic link. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>src</i> The name of the file to link<br />
 <i>dest</i> The name of link</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success, 0 on failure</dl>
<h3>EAPI int ecore_file_unlink (const char * file)</h3>
<p>Delete the given file. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>file</i> The name of the file to delete</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success, 0 on failure</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
