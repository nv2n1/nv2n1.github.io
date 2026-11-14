---
title: "stdfilesystempathhas_root_pathstdfilesystempathhas_root_name(3)"
name: "stdfilesystempathhas_root_pathstdfilesystempathhas_root_name"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfilesystempathhas_root_pathstdfilesystempathhas_root_name/"
description: "std::filesystem::path::has_root_path,std::filesystem::path::has_root_name, – std::filesystem::path::has_root_path,std::filesystem::path::has_root_name,"
---

<p>std::filesystem::path::has_root_path,std::filesystem::path::has_root_name, &#8211; std::filesystem::path::has_root_path,std::filesystem::path::has_root_name,</p>
<h2>Synopsis</h2>
<p>&nbsp;<wbr>std::filesystem::path::has_parent_path, std::filesystem::path::has_filename,<br />
&nbsp;<wbr>std::filesystem::path::has_stem, std::filesystem::path::has_extension<br />
bool has_root_path()&nbsp;<wbr>const;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>(1)</code>&nbsp;<wbr><i>(since C++17)</i><br />
bool has_root_name()&nbsp;<wbr>const;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>(2)</code>&nbsp;<wbr><i>(since C++17)</i><br />
bool has_root_directory()&nbsp;<wbr>const;&nbsp;<wbr><code>(3)</code>&nbsp;<wbr><i>(since C++17)</i><br />
bool has_relative_path()&nbsp;<wbr>const;&nbsp;<wbr>&nbsp;<wbr><code>(4)</code>&nbsp;<wbr><i>(since C++17)</i><br />
bool has_parent_path()&nbsp;<wbr>const;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>(5)</code>&nbsp;<wbr><i>(since C++17)</i><br />
bool has_filename()&nbsp;<wbr>const;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>(6)</code>&nbsp;<wbr><i>(since C++17)</i><br />
bool has_stem()&nbsp;<wbr>const;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>(7)</code>&nbsp;<wbr><i>(since C++17)</i><br />
bool has_extension()&nbsp;<wbr>const;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>(8)</code>&nbsp;<wbr><i>(since C++17)</i><br />
Checks whether the path contains the corresponding path element.<br />
1)&nbsp;<wbr>Checks whether root_path()&nbsp;<wbr>is empty.<br />
2)&nbsp;<wbr>Checks whether root_name()&nbsp;<wbr>is empty.<br />
3)&nbsp;<wbr>Checks whether root_directory()&nbsp;<wbr>is empty.<br />
4)&nbsp;<wbr>Checks whether relative_path()&nbsp;<wbr>is empty.<br />
5)&nbsp;<wbr>Checks whether parent_path()&nbsp;<wbr>is empty.<br />
6)&nbsp;<wbr>Checks whether filename()&nbsp;<wbr>is empty.<br />
7)&nbsp;<wbr>Checks whether stem()&nbsp;<wbr>is empty.<br />
8)&nbsp;<wbr>Checks whether extension()&nbsp;<wbr>is empty. </p>
<h2>Parameters</h2>
<p><i>(none)</i></p>
<h2>Return value</h2>
<p>true if the corresponding path component is not empty, false otherwise. </p>
<h2>Exceptions</h2>
<p><i>(none)</i></p>
<h2>See also</h2>
<p>empty checks if the path is empty<br />
<i>(public member function)</i> </p>
