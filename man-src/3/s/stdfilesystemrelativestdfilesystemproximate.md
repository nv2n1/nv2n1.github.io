---
title: "stdfilesystemrelativestdfilesystemproximate(3)"
name: "stdfilesystemrelativestdfilesystemproximate"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfilesystemrelativestdfilesystemproximate/"
---

std::filesystem::relative,std::filesystem::proximate - std::filesystem::relative,std::filesystem::proximate

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;filesystem&gt;

    path relative(const std::filesystem::path &amp;p, (1)(since C++ 17)

                                                      std::error_code &amp;ec);

path relative(const std::filesystem::path &amp;p,

              const std::filesystem::path &amp;base = std::filesystem::current_path());

path relative(const std::filesystem::path &amp;p, (2)(since C++ 17)

                                                  const std::filesystem::path &amp;base,

              std::error_code &amp;ec);

path proximate(const std::filesystem::path &amp;p, (3)(since C++ 17)

                                                   std::error_code &amp;ec);

path proximate(const std::filesystem::path &amp;p,

               const std::filesystem::path &amp;base = std::filesystem::current_path());

path proximate(const std::filesystem::path &amp;p, (4)(since C++ 17)

                                                   const std::filesystem::path &amp;base,

               std::error_code &amp;ec);</code></pre> 
1) Returns relative(p, current_path(), ec) 
2) Returns p made relative to base. Resolves symlinks and normalizes both p and base before other processing. Effectively returns weakly_canonical(p).lexically_relative(weakly_canonical(base)) or weakly_canonical(p, ec).lexically_relative(weakly_canonical(base, ec)), except the error code form returns path() at the first error occurrence, if any. 
3) Returns proximate(p, current_path(), ec) 
4) Effectively returns weakly_canonical(p).lexically_proximate(weakly_canonical(base)) or weakly_canonical(p, ec).lexically_proximate(weakly_canonical(base, ec)), except the error code form returns path() at the first error occurrence, if any. 

<h2>Parameters</h2>

p - an existing path 
base - base path, against which p will be made relative/proximate 
ec - error code to store error status to

<h2>Return value</h2>

1) p made relative against base. 
2) p made proximate against base 

<h2>Exceptions</h2>

The overload that does not take a std::error_code&amp; parameter throws filesystem_error on underlying OS API errors, constructed with p as the first path argument, base as the second path argument, and the OS error code as the error code argument. The overload taking a std::error_code&amp; parameter sets it to the OS API error code if an OS API call fails, and executes ec.clear() if no errors occur. Any overload not marked noexcept may throw std::bad_alloc if memory allocation fails.

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

path represents a path 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class)</i> 
<i>(C++17)</i> 
absolute composes an absolute path 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++17)</i> 
canonical composes a canonical path 
weakly_canonical <i>(function)</i> 
<i>(C++17)</i> 
