---
title: "stdexperimentalfilesystemrecursive_directory_iteratoroptions(3)"
name: "stdexperimentalfilesystemrecursive_directory_iteratoroptions"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalfilesystemrecursive_directory_iteratoroptions/"
---

std::experimental::filesystem::recursive_directory_iterator::options - std::experimental::filesystem::recursive_directory_iterator::options

<h2>Synopsis</h2>

directory_options options() const; (filesystem TS) 
Returns the options that affect the directory iteration. The options can only be supplied when constructing the directory iterator. 
If the options argument was not supplied, returns options::none. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

The effective options that affect the directory iteration. 

<h2>Exceptions</h2>

<i>(none)</i>
