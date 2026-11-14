---
title: "stdfilesystempathempty(3)"
name: "stdfilesystempathempty"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfilesystempathempty/"
---

std::filesystem::path::empty - std::filesystem::path::empty

<h2>Synopsis</h2>

bool empty() const noexcept; <i>(since C++17)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(until C++20)</i> 
[[nodiscard]] bool empty() const noexcept; <i>(since C++20)</i> 
Checks if the path in generic format is empty. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

true if the path is empty, false otherwise. 

<h2>Notes</h2>

An empty path can be obtained by calling clear and by default-constructing a path. It can also be returned by a path decomposition function (such as extension) if the corresponding component is not present in the path. 
An empty path is classified as a relative path. 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a path 
constructor <i>(public member function)</i> 
