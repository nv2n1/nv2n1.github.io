---
title: "globus_ftp_client-h(3)"
name: "globus_ftp_client-h"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_ftp_client-h/"
description: "globus_ftp_client.h – GridFTP Client."
---

<p>globus_ftp_client.h &#8211; GridFTP Client.</p>
<h2>Synopsis</h2>
<p>#include &#8216;globus_ftp_control.h&#8217;<br />
 #include &#8216;globus_priority_q.h&#8217; </p>
<h3>Data Structures</h3>
<p>struct <code>globus_ftp_client_restart_stream_t</code><br />
 <i>Stream mode restart marker. </i><br />
 struct <code>globus_ftp_client_restart_extended_block_t</code><br />
 <i>Extended block mode restart marker. </i><br />
 union <code>globus_ftp_client_restart_marker_t</code><br />
 <i>Restart marker.</i> </p>
<p> This structure is may be either a stream mode transfer offset, or an extended block mode byte range. &quot;</p>
<h3>Macros</h3>
<p>#define <code>GLOBUS_FTP_CLIENT_MODULE</code> </p>
<h3>Typedefs</h3>
<p>typedef struct<br />
 <code>globus_i_ftp_client_handle_t</code> * <code>globus_ftp_client_handle_t</code>&quot;<br />
 <i>FTP Client Handle.</i> </p>
<p> An FTP client handle is used to associate state with a group of operations. Handles can have <code>attributes</code> associated with them. All FTP <code>operations </code> take a handle pointer as a parameter. &quot;<br />
 typedef struct<br />
 <code>globus_i_ftp_client_plugin_t</code> * <code>globus_ftp_client_plugin_t</code>&quot;<br />
 <i>FTP Client plugin</i> </p>
<p> An FTP Client plugin is used to add restart, monitoring, and performance tuning operations to the FTP Client library, without modifying the base API. Multiple plugins may be associated with a globus_ftp_client_handle_t. &quot;<br />
 typedef void(* <code>globus_ftp_client_complete_callback_t</code> )(void *user_arg, <code>globus_ftp_client_handle_t</code> *handle, globus_object_t *error) </p>
<p> typedef void(* <code>globus_ftp_client_data_callback_t</code> )(void *user_arg, <code>globus_ftp_client_handle_t</code> *handle, globus_object_t *error, globus_byte_t *buffer, globus_size_t length, globus_off_t offset, globus_bool_t eof) </p>
<p> typedef struct<br />
 <code>globus_i_ftp_client_operationattr_t</code> * <code>globus_ftp_client_operationattr_t</code>&quot;<br />
 <i>Operation Attributes.</i> </p>
<p> FTP Client attributes are used to control the parameters needed to access an URL using the FTP protocol. Attributes are created and manipulated using the functions in the <code>attributes </code> section of the library. &quot;<br />
 typedef struct<br />
 <code>globus_i_ftp_client_handleattr_t</code> * <code>globus_ftp_client_handleattr_t</code>&quot;<br />
 <i>Handle Attributes.</i> </p>
<p> Handle attributes are used to control the caching behavior of the ftp client handle, and to implement the plugin features for reliability and performance tuning. &quot;<br />
 typedef struct<br />
 <code>globus_i_ftp_client_features_s</code> * <code>globus_ftp_client_features_t</code>&quot;<br />
 <i>Feature Handle</i> </p>
<p> Handle used to associate state with feature operations. &quot;</p>
<h3>Enumerations</h3>
<p>enum <code>globus_ftp_client_error_t</code> </p>
<p> enum <code>globus_ftp_client_restart_type_t</code> </p>
<p> enum <code>globus_ftp_client_tristate_t</code> </p>
<p> enum <code>globus_ftp_client_probed_feature_t</code> </p>
<h3>Variables</h3>
<p>globus_module_descriptor_t <code>globus_i_ftp_client_module</code> </p>
<h2>Detailed Description</h2>
<p>GridFTP Client. </p>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>globus_ftp_client_error_t</code></h3>
<p>Error types</p>
<h3>enum <code>globus_ftp_client_restart_type_t</code></h3>
<p>Restart marker types.</p>
<h2>Variable Documentation</h2>
<h3>globus_module_descriptor_t globus_i_ftp_client_module</h3>
<p>Module descriptor static initializer.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus_ftp_client from the source code.</p>
