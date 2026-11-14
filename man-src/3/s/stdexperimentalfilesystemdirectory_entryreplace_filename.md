---
title: "stdexperimentalfilesystemdirectory_entryreplace_filename(3)"
name: "stdexperimentalfilesystemdirectory_entryreplace_filename"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalfilesystemdirectory_entryreplace_filename/"
---

std::experimental::filesystem::directory_entry::replace_filename - std::experimental::filesystem::directory_entry::replace_filename

<h2>Synopsis</h2>

<pre><code>void replace_filename(const path &amp;p);
(filesystem TS)</code></pre> 
Changes the filename of the directory entry. 
Effectively sets path to path().parent_path() / p. 
This function does not commit any changes to the filesystem. 

<h2>Parameters</h2>

p - the path to append to the parent path of the currently stored path

<h2>Return value</h2>

<i>(none)</i> 

<h2>Exceptions</h2>

&nbsp;This section is incomplete

<h2>See also</h2>

&nbsp;This section is incomplete 
