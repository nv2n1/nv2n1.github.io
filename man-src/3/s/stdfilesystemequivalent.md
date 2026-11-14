---
title: "stdfilesystemequivalent(3)"
name: "stdfilesystemequivalent"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfilesystemequivalent/"
---

std::filesystem::equivalent - std::filesystem::equivalent

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;filesystem&gt;

    bool equivalent(const std::filesystem::path &amp;p1,

                    const std::filesystem::path &amp;p2);

bool equivalent(const std::filesystem::path &amp;p1, (1)(since C++ 17)

                                                     const std::filesystem::path &amp;p2,

                std::error_code &amp;ec) noexcept;</code></pre> 
Checks whether the paths p1 and p2 resolve to the same file system entity. 
If either p1 or p2 does not exist, an error is reported. 
The non-throwing overload returns false on errors. 

<h2>Parameters</h2>

p1, p2 - paths to check for equivalence 
ec - out-parameter for error reporting in the non-throwing overload

<h2>Return value</h2>

true if the p1 and p2 refer to the same file or directory and their file status is the same. false otherwise. 

<h2>Exceptions</h2>

The overload that does not take a std::error_code&amp; parameter throws filesystem_error on underlying OS API errors, constructed with p1 as the first path argument, p2 as the second path argument, and the OS error code as the error code argument. The overload taking a std::error_code&amp; parameter sets it to the OS API error code if an OS API call fails, and executes ec.clear() if no errors occur. Any overload not marked noexcept may throw std::bad_alloc if memory allocation fails.

<h2>Notes</h2>

Two paths are considered to resolve to the same file system entity if the two candidate entities the paths resolve to are located on the same device at the same location. For POSIX, this means that the st_dev and st_ino members of their POSIX stat_structure, obtained as if by POSIX stat, are equal. 
In particular, all hard links for the same file or directory are equivalent, and a symlink and its target on the same file system are equivalent. 
Defect reports 
The following behavior-changing defect reports were applied retroactively to previously published C++ standards. 
DR Applied to Behavior as published Correct behavior 
LWG_2937 C++17 error condition specified incorrectly corrected 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;cstdint&gt;

#include &lt;filesystem&gt;

namespace fs = std::filesystem;

int main()

{
    // hard link equivalency
    fs::path p1 = &quot;.&quot;;
    fs::path p2 = fs::current_path();
    if (fs::equivalent(p1, p2))
        std::cout &lt;&lt; p1 &lt;&lt; &quot; is equivalent to &quot; &lt;&lt; p2 &lt;&lt; '\n';
    // symlink equivalency
    fs::path p3 = &quot;/lib/libc.so.6&quot;;
    fs::path p4 = p3.parent_path() / fs::read_symlink(p3);
    if (fs::equivalent(p3, p4))
        std::cout &lt;&lt; p3 &lt;&lt; &quot; is equivalent to &quot; &lt;&lt; p4 &lt;&lt; '\n';
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;&quot;.&quot; is equivalent to &quot;/var/tmp/test&quot; 
&nbsp;<wbr>&nbsp;&quot;/lib/libc.so.6&quot; is equivalent to &quot;/lib/libc-2.12.so&quot;

<h2>See also</h2>

status determines file attributes 
symlink_status determines file attributes, checking the symlink target 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++17)</i> 
<i>(C++17)</i> 
