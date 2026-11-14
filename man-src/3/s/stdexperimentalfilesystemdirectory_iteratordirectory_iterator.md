---
title: "stdexperimentalfilesystemdirectory_iteratordirectory_iterator(3)"
name: "stdexperimentalfilesystemdirectory_iteratordirectory_iterator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalfilesystemdirectory_iteratordirectory_iterator/"
---

std::experimental::filesystem::directory_iterator::directory_iterator - std::experimental::filesystem::directory_iterator::directory_iterator

<h2>Synopsis</h2>

<pre><code>directory_iterator();
(1)(filesystem TS)

    explicit directory_iterator(const path &amp;p);
(2)(filesystem TS)

    directory_iterator(const path &amp;p, error_code &amp;ec);
(3)(filesystem TS)

    directory_iterator(const directory_iterator &amp;) = default;
(4)(filesystem TS)

    directory_iterator(directory_iterator &amp;&amp;) = default;
(5)(filesystem TS)</code></pre> 
Constructs a new directory iterator. 
1) Constructs the end iterator. 
2) Constructs a directory iterator that refers to the first directory entry of a directory identified by p. If p refers to an non-existing file or not a directory, returns the end iterator. 

<h2>Parameters</h2>

&nbsp;This section is incomplete

<h2>Exceptions</h2>

1) 
noexcept specification: 
noexcept 
2) filesystem_error if an error occurs. The exception object is constructed with p as an argument. 
3) 
noexcept specification: 
noexcept

<h2>Notes</h2>

To iterate over the current directory, construct the iterator as directory_iterator(&quot;.&quot;) instead of directory_iterator(&quot;&quot;). 
