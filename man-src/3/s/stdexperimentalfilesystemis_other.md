---
title: "stdexperimentalfilesystemis_other(3)"
name: "stdexperimentalfilesystemis_other"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalfilesystemis_other/"
description: "std::experimental::filesystem::is_other – std::experimental::filesystem::is_other"
---

<p>std::experimental::filesystem::is_other &#8211; std::experimental::filesystem::is_other</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;experimental/filesystem&gt;<br />
bool is_other( file_status s ); <code>(1)</code> (filesystem TS)<br />
bool is_other( const path&amp; p ); <code>(2)</code> (filesystem TS)<br />
bool is_other( const path&amp; p, error_code&amp; ec ); <code>(3)</code> (filesystem TS)<br />
Checks if the given file status or path corresponds to a file of type other type. That is, the file exists, but is neither regular file, nor directory nor a symlink.<br />
1) Equivalent to exists(s) &amp;&amp; !is_regular_file(s) &amp;&amp; !is_directory(s) &amp;&amp; !is_symlink(s).<br />
2) Equivalent to is_other(status(p)).<br />
3) Equivalent to is_other(status(p, ec)). Returns false and sets ec to an appropriate error code if an error occurs. Otherwise, ec is cleared with a call to ec.clear(). </p>
<h2>Parameters</h2>
<p>s &#8211; file status to check<br />
p &#8211; path to examine<br />
ec &#8211; error code to store the error status to</p>
<h2>Return value</h2>
<p>true if the given path or file status corresponds to a other file, false otherwise. </p>
<h2>Exceptions</h2>
<p>1,3)<br />
noexcept specification:<br />
noexcept<br />
2) Throws filesystem_error if an error occurs. The error is constructed with p as an argument. The error code is set to an appropriate error code for the error that caused the failure.</p>
<h2>See also</h2>
<p>&nbsp;This section is incomplete </p>
