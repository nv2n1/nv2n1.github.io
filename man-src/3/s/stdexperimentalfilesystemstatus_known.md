---
title: "stdexperimentalfilesystemstatus_known(3)"
name: "stdexperimentalfilesystemstatus_known"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalfilesystemstatus_known/"
description: "std::experimental::filesystem::status_known – std::experimental::filesystem::status_known"
---

<p>std::experimental::filesystem::status_known &#8211; std::experimental::filesystem::status_known</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;experimental/filesystem&gt;<br />
bool status_known( file_status s ); <code>(1)</code> (filesystem TS)<br />
Checks if the given file status is known, Equivalent to s.type() != file_type::none. </p>
<h2>Parameters</h2>
<p>s &#8211; file status to check</p>
<h2>Return value</h2>
<p>true if the given file status is an unknown file status </p>
<h2>Exceptions</h2>
<p>noexcept specification:<br />
noexcept</p>
<h2>Notes</h2>
<p>Despite the name, the function checks for the file status of file_type::none (meaning an error occurred), not file_type::unknown (meaning file exists, but its type cannot be determined). </p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;determines file attributes<br />
status determines file attributes, checking the symlink target<br />
symlink_status <i>(function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;cached status of the file designated by this directory entry<br />
status cached symlink_status of the file designated by this directory entry<br />
symlink_status <i>(public member function of std::experimental::filesystem::directory_entry)</i> </p>
