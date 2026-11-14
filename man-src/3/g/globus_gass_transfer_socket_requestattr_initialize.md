---
title: "globus_gass_transfer_socket_requestattr_initialize(3)"
name: "globus_gass_transfer_socket_requestattr_initialize"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gass_transfer_socket_requestattr_initialize/"
description: "Implementing Request Attributes –"
---

<h2 class="name">NAME</h2>
<p> Implementing Request Attributes &#8211; </p>
<h3>Functions</h3>
<p> globus_object_t * <code>globus_gass_transfer_requestattr_initialize</code> (globus_object_t *obj, char *proxy_url, globus_size_t block_size, globus_gass_transfer_file_mode_t file_mode, globus_bool_t connection_reuse) </p>
<p> globus_object_t * <code>globus_gass_transfer_socket_requestattr_initialize</code> (globus_object_t *obj, char *proxy_url, globus_size_t block_size, globus_gass_transfer_file_mode_t file_mode, globus_bool_t connection_reuse, int sndbuf, int rcvbuf, globus_bool_t nodelay) </p>
<p> globus_object_t * <code>globus_gass_transfer_secure_requestattr_initialize</code> (globus_object_t *obj, char *proxy_url, globus_size_t block_size, globus_gass_transfer_file_mode_t file_mode, globus_bool_t connection_reuse, int sndbuf, int rcvbuf, globus_bool_t nodelay, globus_gass_transfer_authorization_t authorization, char *subject) </p>
<p> globus_object_t * <code>globus_gass_transfer_listenerattr_initialize</code> (globus_object_t *obj, int backlog, unsigned short port) </p>
<h2>Detailed Description</h2>
<h2>Function Documentation</h2>
<h3>globus_object_t* globus_gass_transfer_listenerattr_initialize (globus_object_t *obj, intbacklog, unsigned shortport)</h3>
<p> Initialize a base listener attribute. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>obj</i><br />
 <i>backlog</i><br />
 <i>port</i></dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returns the <i>obj</i> pointer if the object inherited from the <i>GLOBUS_GASS_OBJECT_TYPE_LISTENERTATTR</i> type and the attribute could be initialized; GLOBUS_NULL otherwise.</dl>
<h3>globus_object_t* globus_gass_transfer_requestattr_initialize (globus_object_t *obj, char *proxy_url, globus_size_tblock_size, globus_gass_transfer_file_mode_tfile_mode, globus_bool_tconnection_reuse)</h3>
<p> Initialize a base request attribute. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>obj</i><br />
 <i>proxy_url</i><br />
 <i>block_size</i><br />
 <i>file_mode</i><br />
 <i>connection_reuse</i></dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returns the <i>obj</i> pointer if the object inherited from the <i>GLOBUS_GASS_OBJECT_TYPE_REQUESTATTR</i> type and the attribute could be initialized; GLOBUS_NULL otherwise.</dl>
<h3>globus_object_t* globus_gass_transfer_secure_requestattr_initialize (globus_object_t *obj, char *proxy_url, globus_size_tblock_size, globus_gass_transfer_file_mode_tfile_mode, globus_bool_tconnection_reuse, intsndbuf, intrcvbuf, globus_bool_tnodelay, globus_gass_transfer_authorization_tauthorization, char *subject)</h3>
<p> Initialize a secure request attribute. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>obj</i><br />
 <i>proxy_url</i><br />
 <i>block_size</i><br />
 <i>file_mode</i><br />
 <i>connection_reuse</i><br />
 <i>sndbuf</i><br />
 <i>rcvbuf</i><br />
 <i>nodelay</i><br />
 <i>authorization</i><br />
 <i>subject</i></dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returns the <i>obj</i> pointer if the object inherited from the <i>GLOBUS_GASS_OBJECT_TYPE_SECURE_REQUESTATTR</i> type and the attribute could be initialized; GLOBUS_NULL otherwise.</dl>
<h3>globus_object_t* globus_gass_transfer_socket_requestattr_initialize (globus_object_t *obj, char *proxy_url, globus_size_tblock_size, globus_gass_transfer_file_mode_tfile_mode, globus_bool_tconnection_reuse, intsndbuf, intrcvbuf, globus_bool_tnodelay)</h3>
<p> Initialize a socket request attribute. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>obj</i><br />
 <i>proxy_url</i><br />
 <i>block_size</i><br />
 <i>file_mode</i><br />
 <i>connection_reuse</i><br />
 <i>sndbuf</i><br />
 <i>rcvbuf</i><br />
 <i>nodelay</i></dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returns the <i>obj</i> pointer if the object inherited from the <i>GLOBUS_GASS_OBJECT_TYPE_SOCKET_REQUESTATTR</i> type and the attribute could be initialized; GLOBUS_NULL otherwise.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_gass_transfer from the source code. </p>
<h2>Index</h2>
