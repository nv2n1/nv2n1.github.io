---
title: "stdfilesystemrecursive_directory_iteratoroperatorstdfilesystemrecursive_directory_iteratoroperator(3)"
name: "stdfilesystemrecursive_directory_iteratoroperatorstdfilesystemrecursive_directory_iteratoroperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfilesystemrecursive_directory_iteratoroperatorstdfilesystemrecursive_directory_iteratoroperator/"
---

std::filesystem::recursive_directory_iterator::operator*,std::filesystem::recursive_directory_iterator::operator-&gt; - std::filesystem::recursive_directory_iterator::operator*,std::filesystem::recursive_directory_iterator::operator-&gt;

<h2>Synopsis</h2>

<pre><code>const std::filesystem::directory_entry &amp;operator*() const;
(1)(since C++ 17)

    const std::filesystem::directory_entry *
    operator-&gt;() const;
(2)(since C++ 17)</code></pre> 
Accesses the pointed-to directory_entry 
The result of operator* or operator-&gt; on the end iterator is undefined behavior. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

1) Value of the directory_entry referred to by this iterator 
2) Pointer to the directory_entry referred to by this iterator 

<h2>Exceptions</h2>

<i>(none)</i>

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;accesses the pointed-to entry 
operator* <i>(public member function of std::filesystem::directory_iterator)</i> 
operator-&gt; 
