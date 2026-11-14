---
title: "stdfilesystemperm_options(3)"
name: "stdfilesystemperm_options"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfilesystemperm_options/"
---

std::filesystem::perm_options - std::filesystem::perm_options

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;filesystem&gt;

enum class perm_options {

    replace = /* unspecified */,

    add = /* unspecified */,        (since C++17)

    remove = /* unspecified */,

    nofollow = /* unspecified */

};</code></pre> 
This type represents available options that control the behavior of the function permissions(). 
perm_options satisfies the requirements of BitmaskType (which means the bitwise operators operator&amp;, operator|, operator^, operator~, operator&amp;=, operator|=, and operator^= are defined for this type) 

<h2>Member constants</h2>

At most one of add, remove, replace may be present, otherwise the behavior of the permissions function is undefined. 

 
Member constant Meaning 
replace Permissions will be completely replaced by the argument to permissions() (default behavior) 
add permissions will be replaced by the bitwise OR of the argument and the current permissions 
remove permissions will be replaced by the bitwise AND of the negated argument and current permissions 
nofollow permissions will be changed on the symlink itself, rather than on the file it resolves to

<h2>Example</h2>

// Run this code <pre><code>#include &lt;fstream&gt;

#include &lt;bitset&gt;

#include &lt;iostream&gt;

#include &lt;filesystem&gt;

namespace fs = std::filesystem;
void demo_perms(fs::perms p)

{
    std::cout &lt;&lt; ((p &amp; fs::perms::owner_read) != fs::perms::none ? &quot;r&quot; : &quot;-&quot;)
              &lt;&lt; ((p &amp; fs::perms::owner_write) != fs::perms::none ? &quot;w&quot; : &quot;-&quot;)
              &lt;&lt; ((p &amp; fs::perms::owner_exec) != fs::perms::none ? &quot;x&quot; : &quot;-&quot;)
              &lt;&lt; ((p &amp; fs::perms::group_read) != fs::perms::none ? &quot;r&quot; : &quot;-&quot;)
              &lt;&lt; ((p &amp; fs::perms::group_write) != fs::perms::none ? &quot;w&quot; : &quot;-&quot;)
              &lt;&lt; ((p &amp; fs::perms::group_exec) != fs::perms::none ? &quot;x&quot; : &quot;-&quot;)
              &lt;&lt; ((p &amp; fs::perms::others_read) != fs::perms::none ? &quot;r&quot; : &quot;-&quot;)
              &lt;&lt; ((p &amp; fs::perms::others_write) != fs::perms::none ? &quot;w&quot; : &quot;-&quot;)
              &lt;&lt; ((p &amp; fs::perms::others_exec) != fs::perms::none ? &quot;x&quot; : &quot;-&quot;)
              &lt;&lt; '\n';
}

int main()

{
    std::ofstream(&quot;test.txt&quot;); // create file
    std::cout &lt;&lt; &quot;Created file with permissions: &quot;;
    demo_perms(fs::status(&quot;test.txt&quot;).permissions());
    fs::permissions(&quot;test.txt&quot;,
                    fs::perms::owner_all | fs::perms::group_all,
                    fs::perm_options::add);
    std::cout &lt;&lt; &quot;After adding o+rwx and g+rwx:  &quot;;
    demo_perms(fs::status(&quot;test.txt&quot;).permissions());
    fs::remove(&quot;test.txt&quot;);
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;Created file with permissions: rw-r--r-- 
&nbsp;<wbr>&nbsp;After adding o+rwx and g+wrx: rwxrwxr--

<h2>See also</h2>

permissions modifies file access permissions 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++17)</i> 
perms identifies file system permissions 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(enum)</i> 
<i>(C++17)</i> 
