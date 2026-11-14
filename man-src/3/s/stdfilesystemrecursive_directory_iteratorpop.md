---
title: "stdfilesystemrecursive_directory_iteratorpop(3)"
name: "stdfilesystemrecursive_directory_iteratorpop"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfilesystemrecursive_directory_iteratorpop/"
---

std::filesystem::recursive_directory_iterator::pop - std::filesystem::recursive_directory_iterator::pop

<h2>Synopsis</h2>

<pre><code>void pop();
(1)(since C++ 17)

    void pop(std::error_code &amp;ec);
(2)(since C++ 17)</code></pre> 
Moves the iterator one level up in the directory hierarchy. Invalidates all copies of the previous value of *this. 
If the parent directory is outside directory hierarchy that is iterated on (i.e. depth() == 0), sets *this to an end directory iterator. 

<h2>Parameters</h2>

ec - error code to store the error status to

<h2>Return value</h2>

<i>(none)</i> 

<h2>Exceptions</h2>

The overload that does not take a std::error_code&amp; parameter throws filesystem_error on underlying OS API errors, constructed with the OS error code as the error code argument. The overload taking a std::error_code&amp; parameter sets it to the OS API error code if an OS API call fails, and executes ec.clear() if no errors occur. Any overload not marked noexcept may throw std::bad_alloc if memory allocation fails.
