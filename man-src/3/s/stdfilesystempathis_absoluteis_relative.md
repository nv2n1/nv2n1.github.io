---
title: "stdfilesystempathis_absoluteis_relative(3)"
name: "stdfilesystempathis_absoluteis_relative"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfilesystempathis_absoluteis_relative/"
description: "std::filesystem::path::is_absolute,is_relative – std::filesystem::path::is_absolute,is_relative"
---

<p>std::filesystem::path::is_absolute,is_relative &#8211; std::filesystem::path::is_absolute,is_relative</p>
<h2>Synopsis</h2>
<p>bool is_absolute() const; <code>(1)</code> <i>(since C++17)</i><br />
bool is_relative() const; <code>(2)</code> <i>(since C++17)</i><br />
Checks whether the path is absolute or relative. An absolute path is a path that unambiguously identifies the location of a file without reference to an additional starting location. The first version returns true if the path, in native format, is absolute, false otherwise; the second version the other way round. </p>
<h2>Parameters</h2>
<p><i>(none)</i></p>
<h2>Return value</h2>
<p>1) true if the path is absolute, false otherwise.<br />
2) false if the path is absolute, true otherwise. </p>
<h2>Exceptions</h2>
<p><i>(none)</i></p>
<h2>Notes</h2>
<p>The path &quot;/&quot; is absolute on a POSIX OS, but is relative on Windows. </p>
<h2>See also</h2>
<p>absolute composes an absolute path<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++17)</i> </p>
