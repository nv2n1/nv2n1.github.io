---
title: "ecore_con_url_group(3)"
name: "ecore_con_url_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_con_url_group/"
description: "Ecore URL Connection Functions – Utility functions that set up, use and shut down the Ecore URL Connection library."
---

<p>Ecore URL Connection Functions &#8211; Utility functions that set up, use and shut down the Ecore URL Connection library. </p>
<h3>Functions</h3>
<p>EAPI int <code>ecore_con_url_init</code> (void)<br />
 <i>Initialises the Ecore_Con_Url library. </i><br />
 EAPI int <code>ecore_con_url_shutdown</code> (void)<br />
 <i>Shuts down the Ecore_Con_Url library. </i><br />
 EAPI Ecore_Con_Url * <code>ecore_con_url_new</code> (const char *url)<br />
 <i>Creates and initializes a new Ecore_Con_Url. </i><br />
 EAPI void <code>ecore_con_url_destroy</code> (Ecore_Con_Url *url_con)<br />
 <i>Frees the Ecore_Con_Url. </i><br />
 EAPI int <code>ecore_con_url_url_set</code> (Ecore_Con_Url *url_con, const char *url)<br />
 <i>FIXME: To be documented. </i><br />
 EAPI void <code>ecore_con_url_data_set</code> (Ecore_Con_Url *url_con, void *data)<br />
 <i>FIXME: To be documented. </i><br />
 EAPI void * <code>ecore_con_url_data_get</code> (Ecore_Con_Url *url_con)<br />
 <i>FIXME: To be documented. </i><br />
 EAPI void <code>ecore_con_url_time</code> (Ecore_Con_Url *url_con, Ecore_Con_Url_Time condition, time_t tm)<br />
 <i>FIXME: To be documented. </i><br />
 EAPI void <code>ecore_con_url_fd_set</code> (Ecore_Con_Url *url_con, int fd)<br />
 <i>FIXME: To be documented. </i><br />
 EAPI int <code>ecore_con_url_received_bytes_get</code> (Ecore_Con_Url *url_con)<br />
 <i>FIXME: To be documented. </i><br />
 EAPI int <code>ecore_con_url_send</code> (Ecore_Con_Url *url_con, void *data, size_t length, char *content_type)<br />
 <i>FIXME: To be documented. </i><br />
 EAPI int <code>ecore_con_url_ftp_upload</code> (Ecore_Con_Url *url_con, char *filename, char *user, char *pass, char *upload_dir)<br />
 <i>Makes a FTP upload. </i><br />
 EAPI void <code>ecore_con_url_verbose_set</code> (Ecore_Con_Url *url_con, int verbose)<br />
 <i>Enable or disable libcurl verbose output, useful for debug. </i><br />
 EAPI void <code>ecore_con_url_ftp_use_epsv_set</code> (Ecore_Con_Url *url_con, int use_epsv)<br />
 <i>Enable or disable EPSV extension. </i></p>
<h2>Detailed Description</h2>
<p>Utility functions that set up, use and shut down the Ecore URL Connection library. </p>
<p> FIXME: write detailed description</p>
<h2>Function Documentation</h2>
<h3>EAPI void* ecore_con_url_data_get (Ecore_Con_Url * url_con)</h3>
<p>FIXME: To be documented. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>FIXME: To be documented.</dl>
<h3>EAPI void ecore_con_url_data_set (Ecore_Con_Url * url_con, void * data)</h3>
<p>FIXME: To be documented. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>FIXME: To be documented.</dl>
<h3>EAPI void ecore_con_url_destroy (Ecore_Con_Url * url_con)</h3>
<p>Frees the Ecore_Con_Url. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>FIXME: To be documented.</dl>
<p> References ecore_direct_compare(), ecore_list_find(), ecore_list_remove(), and ecore_main_fd_handler_del(). </p>
<p> Referenced by ecore_con_url_shutdown().</p>
<h3>EAPI void ecore_con_url_fd_set (Ecore_Con_Url * url_con, int fd)</h3>
<p>FIXME: To be documented. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>FIXME: To be documented.</dl>
<h3>EAPI int ecore_con_url_ftp_upload (Ecore_Con_Url * url_con, char * filename, char * user, char * pass, char * upload_dir)</h3>
<p>Makes a FTP upload. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>FIXME: To be more documented.</dl>
<p> References ecore_con_url_url_set().</p>
<h3>EAPI void ecore_con_url_ftp_use_epsv_set (Ecore_Con_Url * url_con, int use_epsv)</h3>
<p>Enable or disable EPSV extension. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>FIXME: To be more documented.</dl>
<h3>EAPI int ecore_con_url_init (void)</h3>
<p>Initialises the Ecore_Con_Url library. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Number of times the library has been initialised without being shut down.</dl>
<p> References ecore_event_type_new(), ecore_list_destroy(), and ecore_list_new().</p>
<h3>EAPI Ecore_Con_Url* ecore_con_url_new (const char * url)</h3>
<p>Creates and initializes a new Ecore_Con_Url. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>NULL on error, a new Ecore_Con_Url on success.</dl>
<p> References ecore_con_url_url_set().</p>
<h3>EAPI int ecore_con_url_received_bytes_get (Ecore_Con_Url * url_con)</h3>
<p>FIXME: To be documented. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>FIXME: To be documented.</dl>
<h3>EAPI int ecore_con_url_send (Ecore_Con_Url * url_con, void * data, size_t length, char * content_type)</h3>
<p>FIXME: To be documented. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>FIXME: To be documented.</dl>
<h3>EAPI int ecore_con_url_shutdown (void)</h3>
<p>Shuts down the Ecore_Con_Url library. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Number of calls that still uses Ecore_Con_Url</dl>
<p> References ecore_con_url_destroy(), ecore_list_destroy(), ecore_list_empty_is(), and ecore_list_first().</p>
<h3>EAPI void ecore_con_url_time (Ecore_Con_Url * url_con, Ecore_Con_Url_Time condition, time_t tm)</h3>
<p>FIXME: To be documented. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>FIXME: To be documented.</dl>
<h3>EAPI int ecore_con_url_url_set (Ecore_Con_Url * url_con, const char * url)</h3>
<p>FIXME: To be documented. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>FIXME: To be documented.</dl>
<p> Referenced by ecore_con_url_ftp_upload(), and ecore_con_url_new().</p>
<h3>EAPI void ecore_con_url_verbose_set (Ecore_Con_Url * url_con, int verbose)</h3>
<p>Enable or disable libcurl verbose output, useful for debug. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>FIXME: To be more documented.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
