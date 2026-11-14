---
title: "stdexperimentalfilesystemfilesystem_errorfilesystem_error(3)"
name: "stdexperimentalfilesystemfilesystem_errorfilesystem_error"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalfilesystemfilesystem_errorfilesystem_error/"
description: "std::experimental::filesystem::filesystem_error::filesystem_error – std::experimental::filesystem::filesystem_error::filesystem_error"
---

<p>std::experimental::filesystem::filesystem_error::filesystem_error &#8211; std::experimental::filesystem::filesystem_error::filesystem_error</p>
<h2>Synopsis</h2>
<p>filesystem_error( const string&amp; what_arg, error_code ec ); <code>(1)</code> (filesystem TS)<br />
filesystem_error( const string&amp; what_arg, const path&amp; p1, error_code ec ); <code>(2)</code> (filesystem TS)<br />
filesystem_error( const string&amp; what_arg, const path&amp; p1, const path&amp; p2, error_code ec ); <code>(3)</code> (filesystem TS)<br />
Constructs a new filesystem error object. The explanatory string is set to what_arg, error code is set to ec and optionally, the paths that were involved in the operation that resulted in the error, are set to p1 and p2. </p>
<h2>Parameters</h2>
<p>&nbsp;This section is incomplete</p>
<h2>See also</h2>
<p>&nbsp;This section is incomplete </p>
