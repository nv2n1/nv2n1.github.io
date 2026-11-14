---
title: "stdexperimentalfilesystempathis_absoluteis_relative(3)"
name: "stdexperimentalfilesystempathis_absoluteis_relative"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalfilesystempathis_absoluteis_relative/"
description: "std::experimental::filesystem::path::is_absolute,is_relative – std::experimental::filesystem::path::is_absolute,is_relative"
---

<p>std::experimental::filesystem::path::is_absolute,is_relative &#8211; std::experimental::filesystem::path::is_absolute,is_relative</p>
<h2>Synopsis</h2>
<p>bool is_absolute() const; <code>(1)</code> (filesystem TS)<br />
bool is_relative() const; <code>(2)</code> (filesystem TS)<br />
Checks whether the path is absolute or relative. An absolute path is such that the elements of root_path() uniquely identify a file system location. The first version returns true if the path is absolute, false otherwise; the second version the other way round. </p>
<h2>Parameters</h2>
<p><i>(none)</i></p>
<h2>Return value</h2>
<p>1) true if the path is absolute, false otherwise.<br />
2) false if the path is absolute, true otherwise. </p>
<h2>Exceptions</h2>
<p><i>(none)</i></p>
<h2>See also</h2>
<p>has_root_path<br />
has_root_name<br />
has_root_directory checks if the corresponding path element is not empty<br />
has_relative_path <i>(public member function)</i><br />
has_parent_path<br />
has_filename<br />
has_stem<br />
has_extension </p>
