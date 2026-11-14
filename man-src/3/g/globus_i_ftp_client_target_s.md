---
title: "globus_i_ftp_client_target_s(3)"
name: "globus_i_ftp_client_target_s"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_i_ftp_client_target_s/"
description: "globus_i_ftp_client_target_s –"
---

<h2 class="name">NAME</h2>
<p> globus_i_ftp_client_target_s &#8211; </p>
<p> FTP Connection State.</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;globus_i_ftp_client.h&gt;</p>
<h3>Data Fields</h3>
<p> globus_ftp_client_target_state_t <code>state</code> </p>
<p> globus_ftp_control_handle_t * <code>control_handle</code> </p>
<p> char * <code>url_string</code> </p>
<p> globus_url_t <code>url</code> </p>
<p> globus_ftp_control_auth_info_t <code>auth_info</code> </p>
<p> <code>globus_i_ftp_client_features_t</code> * <code>features</code> </p>
<p> globus_ftp_control_dcau_t <code>dcau</code> </p>
<p> <code>globus_i_ftp_client_operationattr_t</code> * <code>attr</code> </p>
<p> <code>globus_i_ftp_client_handle_t</code> * <code>owner</code> </p>
<p> <code>globus_i_ftp_client_data_target_t</code> <code>cached_data_conn</code> </p>
<p> <code>globus_ftp_client_plugin_command_mask_t</code> <code>mask</code> </p>
<h2>Detailed Description</h2>
<p> FTP Connection State. </p>
<p> This type is used to store information about an active FTP control connection. This information includes the FTP control handle, the extensions which the server supports, and the current session settings which have been set on the control handle.</p>
<h2>Field Documentation</h2>
<h3><code>globus_i_ftp_client_operationattr_t</code>* globus_i_ftp_client_target_s::attr</h3>
<p> Requested settings</p>
<h3>globus_ftp_control_auth_info_t globus_i_ftp_client_target_s::auth_info</h3>
<p> Information about server authentication.</p>
<h3><code>globus_i_ftp_client_data_target_t</code> globus_i_ftp_client_target_s::cached_data_conn</h3>
<p> Data connection caching information</p>
<h3>globus_ftp_control_handle_t* globus_i_ftp_client_target_s::control_handle</h3>
<p> Handle to an FTP control connection.</p>
<h3>globus_ftp_control_dcau_t globus_i_ftp_client_target_s::dcau</h3>
<p> Current settings</p>
<h3><code>globus_i_ftp_client_features_t</code>* globus_i_ftp_client_target_s::features</h3>
<p> Features we&#8217;ve discovered about this target so far.</p>
<h3><code>globus_ftp_client_plugin_command_mask_t</code> globus_i_ftp_client_target_s::mask</h3>
<p> Plugin mask associated with the currently pending command.</p>
<h3><code>globus_i_ftp_client_handle_t</code>* globus_i_ftp_client_target_s::owner</h3>
<p> The client that this target is associated with</p>
<h3>globus_ftp_client_target_state_t globus_i_ftp_client_target_s::state</h3>
<p> Current connection/activity state of this target</p>
<h3>globus_url_t globus_i_ftp_client_target_s::url</h3>
<p> Host/port we are connected to.</p>
<h3>char* globus_i_ftp_client_target_s::url_string</h3>
<p> URL we are currently processing. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_ftp_client from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAR">Author</a></p>
<dd></dl>
