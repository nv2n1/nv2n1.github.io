---
title: "stdexperimentalfilesystemfile_statustype(3)"
name: "stdexperimentalfilesystemfile_statustype"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalfilesystemfile_statustype/"
description: "std::experimental::filesystem::file_status::type – std::experimental::filesystem::file_status::type"
---

<p>std::experimental::filesystem::file_status::type &#8211; std::experimental::filesystem::file_status::type</p>
<h2>Synopsis</h2>
<p>file_type type() const; <code>(1)</code> (filesystem TS)<br />
void type( file_type type ); <code>(2)</code> (filesystem TS)<br />
Accesses the file type information.<br />
1) Returns file type information.<br />
2) Sets file type to type. </p>
<h2>Parameters</h2>
<p>type &#8211; file type to set to</p>
<h2>Return value</h2>
<p>1) File type information.<br />
2) <i>(none)</i> </p>
<h2>Exceptions</h2>
<p>noexcept specification:<br />
noexcept</p>
