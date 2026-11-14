---
title: "stdexperimentalfilesystemis_empty(3)"
name: "stdexperimentalfilesystemis_empty"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalfilesystemis_empty/"
description: "std::experimental::filesystem::is_empty – std::experimental::filesystem::is_empty"
---

<p>std::experimental::filesystem::is_empty &#8211; std::experimental::filesystem::is_empty</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;experimental/filesystem&gt;<br />
bool is_empty( const path&amp; p ); <code>(1)</code> (filesystem TS)<br />
bool is_empty( const path&amp; p, error_code&amp; ec ); <code>(2)</code> (filesystem TS)<br />
Checks whether the given path refers to an empty file or directory.<br />
The second version returns false and sets ec to an appropriate error code if an error occurs. Otherwise, ec is cleared with a call to ec.clear(). </p>
<h2>Parameters</h2>
<p>p &#8211; path to examine<br />
ec &#8211; error code to modify in case of error</p>
<h2>Return value</h2>
<p>true if p refers to an empty file or directory, false otherwise. </p>
<h2>Exceptions</h2>
<p>1) filesystem_error if an error occurs. The exception object is constructed with p as an argument. The error code is set to an appropriate error code for the error that caused the failure.<br />
2)<br />
noexcept specification:<br />
noexcept</p>
<h2>See also</h2>
<p>&nbsp;This section is incomplete </p>
