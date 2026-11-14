---
title: "stdexperimentalfilesystemis_directory(3)"
name: "stdexperimentalfilesystemis_directory"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalfilesystemis_directory/"
description: "std::experimental::filesystem::is_directory – std::experimental::filesystem::is_directory"
---

<p>std::experimental::filesystem::is_directory &#8211; std::experimental::filesystem::is_directory</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;experimental/filesystem&gt;<br />
bool is_directory( file_status s ); <code>(1)</code> (filesystem TS)<br />
bool is_directory( const path&amp; p ); <code>(2)</code> (filesystem TS)<br />
bool is_directory( const path&amp; p, error_code&amp; ec ); <code>(3)</code> (filesystem TS)<br />
Checks if the given file status or path corresponds to a directory.<br />
1) Equivalent to s.type() == file_type::directory.<br />
2) Equivalent to is_directory(status(p)).<br />
3) Equivalent to is_directory(status(p, ec)). Returns false if error occurs. </p>
<h2>Parameters</h2>
<p>s &#8211; file status to check<br />
p &#8211; path to query<br />
ec &#8211; error code to modify in case of errors</p>
<h2>Return value</h2>
<p>true if the given path or file status corresponds to a directory, false otherwise. </p>
<h2>Exceptions</h2>
<p>1,3)<br />
noexcept specification:<br />
noexcept<br />
2) Throws filesystem_error if an error occurs. The exception object is constructed with p as an argument.</p>
<h2>See also</h2>
<p>&nbsp;This section is incomplete </p>
