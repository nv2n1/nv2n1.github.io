---
title: "stdexperimentalfilesystemrecursive_directory_iteratorrecursive_directory_iterator(3)"
name: "stdexperimentalfilesystemrecursive_directory_iteratorrecursive_directory_iterator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalfilesystemrecursive_directory_iteratorrecursive_directory_iterator/"
---

std::experimental::filesystem::recursive_directory_iterator::recursive_directory_iterator - std::experimental::filesystem::recursive_directory_iterator::recursive_directory_iterator

<h2>Synopsis</h2>

<pre><code>recursive_directory_iterator();
(1)(filesystem TS)

    recursive_directory_iterator(const recursive_directory_iterator &amp;) = default;
(2)(filesystem TS)

    recursive_directory_iterator(recursive_directory_iterator &amp;&amp;) = default;
(3)(filesystem TS)

    explicit recursive_directory_iterator(const path &amp;p, (4)(filesystem TS)

                                                             directory_options options = directory_options::none);

recursive_directory_iterator(const path &amp;p, (5)(filesystem TS)

                                                directory_options options,
                             error_code &amp;ec);

recursive_directory_iterator(const path &amp;p, error_code &amp;ec);
(6)(filesystem TS)</code></pre> 
Contructs new recursive directory iterator. 
1) Default constructor. Constructs an end iterator. 
2-3) Default copy and move constructors. 
4-6) Constructs a iterator that refers to the first entry in the directory that p resolves to. 
&nbsp;This section is incomplete 
&nbsp;Reason: errors 

<h2>Parameters</h2>

&nbsp;This section is incomplete

<h2>Exceptions</h2>

1,5,6) 
noexcept specification: 
noexcept 

 
&nbsp;This section is incomplete

<h2>Notes</h2>

Recursive directory iterators do not follow directory symlinks by default. To enable this behavior, specify directory_options::follow_directory_symlink among the options option set. 
