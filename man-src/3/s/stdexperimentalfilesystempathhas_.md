---
title: "stdexperimentalfilesystempathhas_(3)"
name: "stdexperimentalfilesystempathhas_"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalfilesystempathhas_/"
description: "std::experimental::filesystem::path::has_… – std::experimental::filesystem::path::has_…"
---

<p>std::experimental::filesystem::path::has_&#8230; &#8211; std::experimental::filesystem::path::has_&#8230;</p>
<h2>Synopsis</h2>
<p>bool has_root_path() const; <code>(1)</code> (filesystem TS)<br />
bool has_root_name() const; <code>(2)</code> (filesystem TS)<br />
bool has_root_directory() const; <code>(3)</code> (filesystem TS)<br />
bool has_relative_path() const; <code>(4)</code> (filesystem TS)<br />
bool has_parent_path() const; <code>(5)</code> (filesystem TS)<br />
bool has_filename() const; <code>(6)</code> (filesystem TS)<br />
bool has_stem() const; <code>(7)</code> (filesystem TS)<br />
bool has_extension() const; <code>(8)</code> (filesystem TS)<br />
Checks whether the path contains the corresponding path element.<br />
1) Checks whether root_path() is empty.<br />
2) Checks whether root_name() is empty.<br />
3) Checks whether root_directory() is empty.<br />
4) Checks whether relative_path() is empty.<br />
5) Checks whether parent_path() is empty.<br />
6) Checks whether filename() is empty.<br />
7) Checks whether stem() is empty.<br />
8) Checks whether extension() is empty. </p>
<h2>Parameters</h2>
<p><i>(none)</i></p>
<h2>Return value</h2>
<p>true if the corresponding path is not empty, false otherwise. </p>
<h2>Exceptions</h2>
<p><i>(none)</i></p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks if the path is empty<br />
empty <i>(public member function)</i> </p>
