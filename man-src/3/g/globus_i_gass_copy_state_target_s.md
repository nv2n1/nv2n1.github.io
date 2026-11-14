---
title: "globus_i_gass_copy_state_target_s(3)"
name: "globus_i_gass_copy_state_target_s"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_i_gass_copy_state_target_s/"
description: "globus_i_gass_copy_state_target_s –"
---

<h2 class="name">NAME</h2>
<p> globus_i_gass_copy_state_target_s &#8211; </p>
<p> GASS copy target (e.g.</p>
<h2>SYNOPSIS</h2>
<h3>Data Fields</h3>
<p> char * <code>url</code> </p>
<p> globus_gass_copy_attr_t * <code>attr</code> </p>
<p> globus_mutex_t <code>mutex</code> </p>
<p> globus_fifo_t <code>queue</code> </p>
<p> int <code>n_pending</code> </p>
<p> int <code>n_simultaneous</code> </p>
<p> int <code>n_complete</code> </p>
<p> globus_i_gass_copy_target_status_t <code>status</code> </p>
<p> globus_gass_copy_url_mode_t <code>mode</code> </p>
<p> union { </p>
<p> struct { </p>
<p> } <code>ftp</code> </p>
<p> struct { </p>
<p> globus_gass_transfer_request_t <code>request</code> </p>
<p> } <code>gass</code> </p>
<p> struct { </p>
<p> globus_bool_t <code>free_handle</code> </p>
<p> globus_bool_t <code>seekable</code> </p>
<p> } <code>io</code> </p>
<p> } <code>data</code> </p>
<h2>Detailed Description</h2>
<p> GASS copy target (e.g. </p>
<p> source, destination) transfer information.</p>
<h2>Field Documentation</h2>
<h3>char* <code>globus_i_gass_copy_state_target_s::url</code></h3>
<p> url for file transfer</p>
<h3>globus_gass_copy_attr_t* <code>globus_i_gass_copy_state_target_s::attr</code></h3>
<p> attributes to control file transfer</p>
<h3>globus_mutex_t <code>globus_i_gass_copy_state_target_s::mutex</code></h3>
<p> coordinates the modifying of the target structure</p>
<h3>globus_fifo_t <code>globus_i_gass_copy_state_target_s::queue</code></h3>
<p> a queue to manage the reading/writing of data buffers</p>
<h3>int <code>globus_i_gass_copy_state_target_s::n_pending</code></h3>
<p> Used for keeping track of reads/writes in the read/write queue.</p>
<h3>int <code>globus_i_gass_copy_state_target_s::n_simultaneous</code></h3>
<p> Used to limit the number of n_pending.</p>
<h3>int <code>globus_i_gass_copy_state_target_s::n_complete</code></h3>
<p> Used to compute the offset for ftp writes.</p>
<h3>globus_i_gass_copy_target_status_t <code>globus_i_gass_copy_state_target_s::status</code></h3>
<p> signifies the target has been successfully setup</p>
<h3>globus_gass_copy_url_mode_t <code>globus_i_gass_copy_state_target_s::mode</code></h3>
<p> mode used to identify the below target union struct.</p>
<h3>struct { &#8230; } <code>globus_i_gass_copy_state_target_s::ftp</code></h3>
<p> ftp specific data</p>
<h3>globus_gass_transfer_request_t <code>globus_i_gass_copy_state_target_s::request</code></h3>
<p> GASS equivelent of a handle.</p>
<h3>struct { &#8230; } <code>globus_i_gass_copy_state_target_s::gass</code></h3>
<p> GASS specific data.</p>
<h3>globus_bool_t <code>globus_i_gass_copy_state_target_s::free_handle</code></h3>
<p> If the IO handle was passed as an argument then FALSE If the IO handle was created internally then TRUE.</p>
<h3>globus_bool_t <code>globus_i_gass_copy_state_target_s::seekable</code></h3>
<p> Can globus_io_file_seek() be performed on this handle?</p>
<h3>struct { &#8230; } <code>globus_i_gass_copy_state_target_s::io</code></h3>
<p> IO specific data.</p>
<h3>union { &#8230; } <code>globus_i_gass_copy_state_target_s::data</code></h3>
<p> data required to perform each type of transfer </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus gass copy from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAW">Author</a></p>
<dd></dl>
