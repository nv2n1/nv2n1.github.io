---
title: "globus_gass_copy_handle_s(3)"
name: "globus_gass_copy_handle_s"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gass_copy_handle_s/"
description: "globus_gass_copy_handle_s –"
---

<h2 class="name">NAME</h2>
<p> globus_gass_copy_handle_s &#8211; </p>
<p> Copy Handle.</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;globus_gass_copy.h&gt;</p>
<h3>Data Fields</h3>
<p> <code>globus_gass_copy_status_t</code> <code>status</code> </p>
<p> globus_gass_copy_state_t * <code>state</code> </p>
<p> void * <code>user_pointer</code> </p>
<p> globus_gass_copy_perf_info_t * <code>performance</code> </p>
<p> globus_bool_t <code>external_third_party</code> </p>
<p> <code>globus_gass_copy_callback_t</code> <code>user_callback</code> </p>
<p> void * <code>callback_arg</code> </p>
<p> <code>globus_gass_copy_callback_t</code> <code>user_cancel_callback</code> </p>
<p> void * <code>cancel_callback_arg</code> </p>
<p> globus_object_t * <code>err</code> </p>
<p> int <code>buffer_length</code> </p>
<p> globus_bool_t <code>no_third_party_transfers</code> </p>
<p> globus_ftp_client_handle_t <code>ftp_handle_2</code> </p>
<p> globus_bool_t <code>send_allo</code> </p>
<p> globus_bool_t <code>always_stat_on_expand</code> </p>
<p> globus_off_t <code>partial_offset</code> </p>
<h2>Detailed Description</h2>
<p> Copy Handle.</p>
<h2>Field Documentation</h2>
<h3>globus_bool_t globus_gass_copy_handle_s::always_stat_on_expand</h3>
<p> Run a stat check on all urls passed to globus_gass_copy_glob_expand_url</p>
<h3>int globus_gass_copy_handle_s::buffer_length</h3>
<p> Size of the buffers to be used in the transfers</p>
<h3>void* globus_gass_copy_handle_s::callback_arg</h3>
<p> pointer to user argument to user callback function</p>
<h3>void* globus_gass_copy_handle_s::cancel_callback_arg</h3>
<p> pointer to user argument to user cancel callback function</p>
<h3>globus_object_t* globus_gass_copy_handle_s::err</h3>
<p> Error object to pass to the callback function</p>
<h3>globus_bool_t globus_gass_copy_handle_s::external_third_party</h3>
<p> Indicates if the 3rd party transfer is done externally to this library.</p>
<h3>globus_ftp_client_handle_t globus_gass_copy_handle_s::ftp_handle_2</h3>
<p> handle only used when no_third_party_transfers is true (for 3pt)</p>
<h3>globus_bool_t globus_gass_copy_handle_s::no_third_party_transfers</h3>
<p> Indicates whether third_party transfers should be used (for ftp to ftp transfers). If set to FALSE, the default, globus_ftp_client_third_party_transfer() will be used. if set to TRUE, gass_copy will manage the transfer</p>
<h3>globus_off_t globus_gass_copy_handle_s::partial_offset</h3>
<p> offsets for partial file transfers</p>
<h3>globus_gass_copy_perf_info_t* globus_gass_copy_handle_s::performance</h3>
<p> Pointer to perf_info structure used to provide the user transfer performance information</p>
<h3>globus_bool_t globus_gass_copy_handle_s::send_allo</h3>
<p> Indicates whether to send ALLO for ftp destinations</p>
<h3>globus_gass_copy_state_t* globus_gass_copy_handle_s::state</h3>
<p> pointer to the state structure which contains internal info related to a transfer</p>
<h3><code>globus_gass_copy_status_t</code> globus_gass_copy_handle_s::status</h3>
<p> the status of the current transfer</p>
<h3><code>globus_gass_copy_callback_t</code> globus_gass_copy_handle_s::user_callback</h3>
<p> Pointer to user callback function</p>
<h3><code>globus_gass_copy_callback_t</code> globus_gass_copy_handle_s::user_cancel_callback</h3>
<p> pointer to user cancel callback function</p>
<h3>void* globus_gass_copy_handle_s::user_pointer</h3>
<p> pointer to user data </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_gass_copy from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAW">Author</a></p>
<dd></dl>
