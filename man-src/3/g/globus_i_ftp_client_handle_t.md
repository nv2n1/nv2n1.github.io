---
title: "globus_i_ftp_client_handle_t(3)"
name: "globus_i_ftp_client_handle_t"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_i_ftp_client_handle_t/"
description: "globus_i_ftp_client_handle_t –"
---

<h2 class="name">NAME</h2>
<p> globus_i_ftp_client_handle_t &#8211; </p>
<p> FTP Client handle implementation.</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;globus_i_ftp_client.h&gt;</p>
<h3>Data Fields</h3>
<p> char <code>magic</code> [24] </p>
<p> <code>globus_ftp_client_handle_t</code> * <code>handle</code> </p>
<p> struct<br />
 <code>globus_i_ftp_client_target_s</code> * <code>source</code>&quot; </p>
<p> char * <code>source_url</code> </p>
<p> struct<br />
 <code>globus_i_ftp_client_target_s</code> * <code>dest</code>&quot; </p>
<p> char * <code>dest_url</code> </p>
<p> globus_i_ftp_client_operation_t <code>op</code> </p>
<p> <code>globus_ftp_client_complete_callback_t</code> <code>callback</code> </p>
<p> void * <code>callback_arg</code> </p>
<p> globus_ftp_client_handle_state_t <code>state</code> </p>
<p> globus_priority_q_t <code>stalled_blocks</code> </p>
<p> globus_hashtable_t <code>active_blocks</code> </p>
<p> int <code>num_active_blocks</code> </p>
<p> globus_ftp_control_host_port_t * <code>pasv_address</code> </p>
<p> int <code>num_pasv_addresses</code> </p>
<p> globus_object_t * <code>err</code> </p>
<p> struct<br />
 <code>globus_i_ftp_client_restart_s</code> * <code>restart_info</code>&quot; </p>
<p> int <code>notify_in_progress</code> </p>
<p> globus_off_t <code>source_size</code> </p>
<p> <code>globus_ftp_client_restart_marker_t</code> <code>restart_marker</code> </p>
<p> globus_off_t <code>partial_offset</code> </p>
<p> globus_off_t <code>partial_end_offset</code> </p>
<p> globus_off_t <code>base_offset</code> </p>
<p> globus_off_t <code>read_all_biggest_offset</code> </p>
<p> globus_abstime_t * <code>modification_time_pointer</code> </p>
<p> globus_off_t * <code>size_pointer</code> </p>
<p> <code>globus_i_ftp_client_features_t</code> * <code>features_pointer</code> </p>
<p> globus_byte_t ** <code>mlst_buffer_pointer</code> </p>
<p> int <code>chmod_file_mode</code> </p>
<p> char * <code>chgrp_group</code> </p>
<p> struct tm <code>utime_time</code> </p>
<p> globus_mutex_t <code>mutex</code> </p>
<p> char * <code>checksum</code> </p>
<p> globus_off_t <code>checksum_offset</code> </p>
<p> globus_fifo_t <code>src_op_queue</code> </p>
<p> void * <code>user_pointer</code> </p>
<h2>Detailed Description</h2>
<p> FTP Client handle implementation. </p>
<p> <code>Examples: </code> <code>globus_ftp_client_debug_plugin.example</code>, and <code>globus_ftp_client_restart_plugin.example</code>.</p>
<h2>Field Documentation</h2>
<h3>globus_hashtable_t globus_i_ftp_client_handle_t::active_blocks</h3>
<p> Hash of data blocks which are currently being processed by the control handle.</p>
<h3>globus_off_t globus_i_ftp_client_handle_t::base_offset</h3>
<p> Base offset for a transfer, to be added to all offsets in stream mode</p>
<h3><code>globus_ftp_client_complete_callback_t</code> globus_i_ftp_client_handle_t::callback</h3>
<p> Callback to be called once this operation is completed.</p>
<h3>void* globus_i_ftp_client_handle_t::callback_arg</h3>
<p> User-supplied parameter to this callback</p>
<h3>char* globus_i_ftp_client_handle_t::checksum</h3>
<p> cksm pointer</p>
<h3>globus_off_t globus_i_ftp_client_handle_t::checksum_offset</h3>
<p> checksum parameters</p>
<h3>char* globus_i_ftp_client_handle_t::chgrp_group</h3>
<p> group name or ID for CHGRP</p>
<h3>int globus_i_ftp_client_handle_t::chmod_file_mode</h3>
<p> file mode for CHMOD</p>
<h3>struct <code>globus_i_ftp_client_target_s</code>* globus_i_ftp_client_handle_t::dest</h3>
<p> Information about the connection to the destination URL for a put or third-party transfer.</p>
<h3>char* globus_i_ftp_client_handle_t::dest_url</h3>
<p> destination URL</p>
<h3>globus_object_t* globus_i_ftp_client_handle_t::err</h3>
<p> Error object to pass to the completion callback</p>
<h3><code>globus_i_ftp_client_features_t</code>* globus_i_ftp_client_handle_t::features_pointer</h3>
<p> Pointer to user&#8217;s features buffer</p>
<h3><code>globus_ftp_client_handle_t</code>* globus_i_ftp_client_handle_t::handle</h3>
<p> The user&#8217;s handle pointer used to initialize this structure</p>
<h3>char globus_i_ftp_client_handle_t::magic[24]</h3>
<p> client handle magic number</p>
<h3>globus_byte_t** globus_i_ftp_client_handle_t::mlst_buffer_pointer</h3>
<p> Pointer to user&#8217;s MLST/STAT string buffer</p>
<h3>globus_abstime_t* globus_i_ftp_client_handle_t::modification_time_pointer</h3>
<p> Pointer to user&#8217;s modification time buffer</p>
<h3>globus_mutex_t globus_i_ftp_client_handle_t::mutex</h3>
<p> Thread safety</p>
<h3>int globus_i_ftp_client_handle_t::notify_in_progress</h3>
<p> Delayed notification information.</p>
<h3>int globus_i_ftp_client_handle_t::num_active_blocks</h3>
<p> Number of blocks in the active_blocks hash.</p>
<h3>int globus_i_ftp_client_handle_t::num_pasv_addresses</h3>
<p> Number of passive addresses we know about.</p>
<h3>globus_i_ftp_client_operation_t globus_i_ftp_client_handle_t::op</h3>
<p> Current operation on this handle</p>
<h3>globus_off_t globus_i_ftp_client_handle_t::partial_end_offset</h3>
<p> Partial file transfer ending offset.</p>
<h3>globus_off_t globus_i_ftp_client_handle_t::partial_offset</h3>
<p> Partial file transfer starting offset.</p>
<h3>globus_ftp_control_host_port_t* globus_i_ftp_client_handle_t::pasv_address</h3>
<p> Address of PASV side of a transfer.</p>
<h3>globus_off_t globus_i_ftp_client_handle_t::read_all_biggest_offset</h3>
<p> Offset used to determine what length to return in a read callback in when the read_all attribute is set.</p>
<h3>struct <code>globus_i_ftp_client_restart_s</code>* globus_i_ftp_client_handle_t::restart_info</h3>
<p> Restart information.</p>
<h3><code>globus_ftp_client_restart_marker_t</code> globus_i_ftp_client_handle_t::restart_marker</h3>
<p> Current information about what has been transferred so far.</p>
<h3>globus_off_t* globus_i_ftp_client_handle_t::size_pointer</h3>
<p> Pointer to user&#8217;s size buffer</p>
<h3>struct <code>globus_i_ftp_client_target_s</code>* globus_i_ftp_client_handle_t::source</h3>
<p> Information about the connection to the source URL for a get or third-party transfer.</p>
<h3>globus_off_t globus_i_ftp_client_handle_t::source_size</h3>
<p> Size of the file to be downloaded, if known.</p>
<h3>char* globus_i_ftp_client_handle_t::source_url</h3>
<p> source URL</p>
<h3>globus_fifo_t globus_i_ftp_client_handle_t::src_op_queue</h3>
<p> piplining operation queue</p>
<h3>globus_priority_q_t globus_i_ftp_client_handle_t::stalled_blocks</h3>
<p> Priority queue of data blocks which haven&#8217;t yet been sent to the FTP control library</p>
<h3>globus_ftp_client_handle_state_t globus_i_ftp_client_handle_t::state</h3>
<p> Current state of the operation we are processing</p>
<h3>void* globus_i_ftp_client_handle_t::user_pointer</h3>
<p> User pointer </p>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_ftp_client_handle_set_user_pointer()</code>, globus_ftp_client_handle_get_user_pointer()</dl>
<h3>struct tm globus_i_ftp_client_handle_t::utime_time</h3>
<p> modification time for UTIME </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_ftp_client from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbBQ">Author</a></p>
<dd></dl>
