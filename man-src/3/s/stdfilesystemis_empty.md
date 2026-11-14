---
title: "stdfilesystemis_empty(3)"
name: "stdfilesystemis_empty"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfilesystemis_empty/"
---

std::filesystem::is_empty - std::filesystem::is_empty

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;filesystem&gt;

    bool is_empty(const std::filesystem::path &amp;p);
(since C++ 17)

    bool is_empty(const std::filesystem::path &amp;p, std::error_code &amp;ec);</code></pre> 
Checks whether the given path refers to an empty file or directory. 

<h2>Parameters</h2>

p - path to examine 
ec - error code to modify in case of error

<h2>Return value</h2>

true if the file indicated by p or if the type indicated s refers to an empty file or directory, false otherwise. The non-throwing overload returns false if an error occurs. 

<h2>Exceptions</h2>

The overload that does not take a std::error_code&amp; parameter throws filesystem_error on underlying OS API errors, constructed with p as the first path argument and the OS error code as the error code argument. The overload taking a std::error_code&amp; parameter sets it to the OS API error code if an OS API call fails, and executes ec.clear() if no errors occur. Any overload not marked noexcept may throw std::bad_alloc if memory allocation fails. 

 
Defect reports 

 
The following behavior-changing defect reports were applied retroactively to previously published C++ standards. 

 
DR Applied to Behavior as published Correct behavior 
LWG_3013 C++17 error_code overload marked noexcept but can allocate memory noexcept removed

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

status determines file attributes 
symlink_status determines file attributes, checking the symlink target 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++17)</i> 
<i>(C++17)</i> 
exists checks whether path refers to existing file system object 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++17)</i> 
