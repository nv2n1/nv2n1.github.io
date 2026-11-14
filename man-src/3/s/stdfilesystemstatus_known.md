---
title: "stdfilesystemstatus_known(3)"
name: "stdfilesystemstatus_known"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfilesystemstatus_known/"
description: "std::filesystem::status_known – std::filesystem::status_known"
---

<p>std::filesystem::status_known &#8211; std::filesystem::status_known</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;filesystem&gt;<br />
bool status_known( std::filesystem::file_status s ) noexcept; <code>(1)</code> <i>(since C++17)</i><br />
Checks if the given file status is known, Equivalent to s.type() != file_type::none. </p>
<h2>Parameters</h2>
<p>s &#8211; file status to check</p>
<h2>Return value</h2>
<p>true if the given file status is a known file status. </p>
<h2>Notes</h2>
<p>Despite the name, the function checks for the file status of file_type::none (meaning an error occurred), not file_type::unknown (meaning file exists, but its type cannot be determined). </p>
<h2>See also</h2>
<p>status determines file attributes<br />
symlink_status determines file attributes, checking the symlink target<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++17)</i><br />
<i>(C++17)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;status of the file designated by this directory entry<br />
status symlink_status of the file designated by this directory entry<br />
symlink_status <i>(public member function of std::filesystem::directory_entry)</i> </p>
