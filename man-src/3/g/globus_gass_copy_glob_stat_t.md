---
title: "globus_gass_copy_glob_stat_t(3)"
name: "globus_gass_copy_glob_stat_t"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gass_copy_glob_stat_t/"
description: "globus_gass_copy_glob_stat_t –"
---

<h2 class="name">NAME</h2>
<p> globus_gass_copy_glob_stat_t &#8211; </p>
<p> Glob expanded entry information.</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;globus_gass_copy.h&gt;</p>
<h3>Data Fields</h3>
<p> <code>globus_gass_copy_glob_entry_t</code> <code>type</code> </p>
<p> char * <code>unique_id</code> </p>
<p> char * <code>symlink_target</code> </p>
<p> int <code>mode</code> </p>
<p> int <code>mdtm</code> </p>
<p> globus_off_t <code>size</code> </p>
<h2>Detailed Description</h2>
<p> Glob expanded entry information.</p>
<h2>Field Documentation</h2>
<h3>int globus_gass_copy_glob_stat_t::mdtm</h3>
<p> An integer specifying the modification time of the file. It is set to -1 when not available.</p>
<h3>int globus_gass_copy_glob_stat_t::mode</h3>
<p> An integer specifying the mode of the file. It is set to -1 when not available.</p>
<h3>globus_off_t globus_gass_copy_glob_stat_t::size</h3>
<p> A globus_off_t specifying the size of the file. It is set to -1 when not available.</p>
<h3>char* globus_gass_copy_glob_stat_t::symlink_target</h3>
<p> This points to the full path of the target of a symlink. It is NULL for non-symlinks or when not available.</p>
<h3><code>globus_gass_copy_glob_entry_t</code> globus_gass_copy_glob_stat_t::type</h3>
<p> The file type of the entry</p>
<h3>char* globus_gass_copy_glob_stat_t::unique_id</h3>
<p> A string that uniquely identifies the data that the entry refers to. A file and a symlink to that file will have the same unique_id. It is NULL for when not available. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_gass_copy from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAM">Author</a></p>
<dd></dl>
