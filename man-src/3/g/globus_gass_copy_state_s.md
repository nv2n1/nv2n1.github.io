---
title: "globus_gass_copy_state_s(3)"
name: "globus_gass_copy_state_s"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gass_copy_state_s/"
description: "globus_gass_copy_state_s –"
---

<h2 class="name">NAME</h2>
<p> globus_gass_copy_state_s &#8211; </p>
<p> The state structure contains all that is required to perform a file transfer from a source to a destination.</p>
<h2>SYNOPSIS</h2>
<h3>Data Fields</h3>
<p> <code>globus_i_gass_copy_target_t</code> <code>source</code> </p>
<p> <code>globus_i_gass_copy_target_t</code> <code>dest</code> </p>
<p> <code>globus_i_gass_copy_monitor_t</code> <code>monitor</code> </p>
<p> globus_mutex_t <code>mutex</code> </p>
<p> globus_i_gass_copy_cancel_status_t <code>cancel</code> </p>
<h2>Detailed Description</h2>
<p> The state structure contains all that is required to perform a file transfer from a source to a destination.</p>
<h2>Field Documentation</h2>
<h3><code>globus_i_gass_copy_target_t</code> <code>globus_gass_copy_state_s::source</code></h3>
<p> Source information for the file transfer.</p>
<h3><code>globus_i_gass_copy_target_t</code> <code>globus_gass_copy_state_s::dest</code></h3>
<p> Dest information for the file transfer.</p>
<h3><code>globus_i_gass_copy_monitor_t</code> <code>globus_gass_copy_state_s::monitor</code></h3>
<p> Used for signalling from the various callback functions.</p>
<h3>globus_mutex_t <code>globus_gass_copy_state_s::mutex</code></h3>
<p> coordinates the modifying of the state, aside from the target structures</p>
<h3>globus_i_gass_copy_cancel_status_t <code>globus_gass_copy_state_s::cancel</code></h3>
<p> indicates the status of the cancel operation. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus gass copy from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAL">Author</a></p>
<dd></dl>
