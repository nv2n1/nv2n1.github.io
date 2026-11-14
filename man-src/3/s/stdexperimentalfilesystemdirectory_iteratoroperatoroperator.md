---
title: "stdexperimentalfilesystemdirectory_iteratoroperatoroperator(3)"
name: "stdexperimentalfilesystemdirectory_iteratoroperatoroperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalfilesystemdirectory_iteratoroperatoroperator/"
---

std::experimental::filesystem::directory_iterator::operator*,operator-&gt; - std::experimental::filesystem::directory_iterator::operator*,operator-&gt;

<h2>Synopsis</h2>

<pre><code>const directory_entry &amp;operator*() const;
(filesystem TS)

    const directory_entry *
    operator-&gt;() const;</code></pre> 
Accesses the pointed-to directory_entry. 
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
operator* <i>(public member function of std::experimental::filesystem::recursive_directory_iterator)</i> 
operator-&gt; 
