---
title: "stdexperimentalfilesystemrecursive_directory_iteratorpop(3)"
name: "stdexperimentalfilesystemrecursive_directory_iteratorpop"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalfilesystemrecursive_directory_iteratorpop/"
---

std::experimental::filesystem::recursive_directory_iterator::pop - std::experimental::filesystem::recursive_directory_iterator::pop

<h2>Synopsis</h2>

<pre><code>void pop();
(filesystem TS)</code></pre> 
Moves the iterator one level up in the directory hierarchy. 
If the parent directory is outside directory hierarchy that is iterated on (i.e. depth() == 0), sets *this to an end directory iterator. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

<i>(none)</i> 

<h2>Exceptions</h2>

&nbsp;This section is incomplete
