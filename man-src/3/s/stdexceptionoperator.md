---
title: "stdexceptionoperator(3)"
name: "stdexceptionoperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexceptionoperator/"
---

std::exception::operator= - std::exception::operator=

<h2>Synopsis</h2>

<pre><code>exception &amp;operator=(const exception &amp;other) throw();
(until C++ 11)

    exception &amp;
    operator=(const exception &amp;other) noexcept;
(since C++ 11)</code></pre> 
Copy assignment operator. Assigns the contents of other 
The effects of calling what() after assignment are implementation-defined. <i>(until C++11)</i> 
If *this and other both have dynamic type std::exception then std::strcmp(what(), other.what()) == 0. <i>(since C++11)</i> 

<h2>Parameters</h2>

other - another exception to assign the contents of
