---
title: "stdfilesystemrecursive_directory_iteratorrecursive_directory_iterator(3)"
name: "stdfilesystemrecursive_directory_iteratorrecursive_directory_iterator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfilesystemrecursive_directory_iteratorrecursive_directory_iterator/"
description: "std::filesystem::recursive_directory_iterator::recursive_directory_iterator – std::filesystem::recursive_directory_iterator::recursive_directory_iterator"
---

<p>std::filesystem::recursive_directory_iterator::recursive_directory_iterator &#8211; std::filesystem::recursive_directory_iterator::recursive_directory_iterator</p>
<h2>Synopsis</h2>
<p>recursive_directory_iterator() noexcept; <code>(1)</code> <i>(since C++17)</i><br />
recursive_directory_iterator( const recursive_directory_iterator&amp; rhs ); <code>(2)</code> <i>(since C++17)</i><br />
recursive_directory_iterator( recursive_directory_iterator&amp;&amp; rhs ) noexcept; <code>(3)</code> <i>(since C++17)</i><br />
explicit recursive_directory_iterator( const std::filesystem::path&amp; p ); <code>(4)</code> <i>(since C++17)</i><br />
recursive_directory_iterator(<br />
const std::filesystem::path&amp; p, <code>(4)</code> <i>(since C++17)</i><br />
std::filesystem::directory_options options );<br />
recursive_directory_iterator(<br />
const std::filesystem::path&amp; p, <code>(5)</code> <i>(since C++17)</i><br />
std::filesystem::directory_options options,<br />
std::error_code&amp; ec );<br />
recursive_directory_iterator( const std::filesystem::path&amp; p, std::error_code&amp; ec ); <code>(6)</code> <i>(since C++17)</i><br />
Contructs new recursive directory iterator.<br />
1) Default constructor. Constructs an end iterator.<br />
2) Copy constructor.<br />
3) Move constructor.<br />
4-6) Constructs a iterator that refers to the first entry in the directory that p resolves to.<br />
&nbsp;This section is incomplete<br />
&nbsp;Reason: errors </p>
<h2>Parameters</h2>
<p>&nbsp;This section is incomplete</p>
<h2>Exceptions</h2>
<p>The overload that does not take a std::error_code&amp; parameter throws filesystem_error on underlying OS API errors, constructed with p as the first path argument and the OS error code as the error code argument. The overload taking a std::error_code&amp; parameter sets it to the OS API error code if an OS API call fails, and executes ec.clear() if no errors occur. Any overload not marked noexcept may throw std::bad_alloc if memory allocation fails.</p>
<h2>Notes</h2>
<p>Recursive directory iterators do not follow directory symlinks by default. To enable this behavior, specify directory_options::follow_directory_symlink among the options option set.<br />
Defect reports<br />
The following behavior-changing defect reports were applied retroactively to previously published C++ standards.<br />
DR Applied to Behavior as published Correct behavior<br />
LWG_3013 C++17 error_code overload marked noexcept but can allocate memory noexcept removed </p>
