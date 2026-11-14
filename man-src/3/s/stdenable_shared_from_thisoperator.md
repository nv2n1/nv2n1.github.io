---
title: "stdenable_shared_from_thisoperator(3)"
name: "stdenable_shared_from_thisoperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdenable_shared_from_thisoperator/"
---

std::enable_shared_from_this&lt;T&gt;::operator= - std::enable_shared_from_this&lt;T&gt;::operator=

<h2>Synopsis</h2>

<pre><code>enable_shared_from_this&lt;T&gt; &amp;operator=(const enable_shared_from_this&lt;T&gt; &amp;obj) noexcept;
(since C++ 11)</code></pre> 
Does nothing; returns *this. 

<h2>Parameters</h2>

obj - an enable_shared_from_this to assign to *this

<h2>Return value</h2>

*this 

<h2>Notes</h2>

The private std::weak_ptr&lt;T&gt; member is not affected by this assignment operator. 

<h2>Example</h2>

Note: enable_shared_from_this::operator= is defined as protected in order to prevent accidental slicing but allow derived classes to have default assignment operators. 
 // Run this code <pre><code>#include &lt;memory&gt;

#include &lt;iostream&gt;
class SharedInt : public std::enable_shared_from_this&lt;SharedInt&gt;

{

  public:
    explicit SharedInt(int n)
        : mNumber(n)
    {
    }
    SharedInt(const SharedInt &amp;) = default;
    SharedInt(SharedInt &amp;&amp;) = default;
    ~SharedInt() = default;
    // Both assignment operators use enable_shared_from_this::operator=
    SharedInt &amp;operator=(const SharedInt &amp;) = default;
    SharedInt &amp;operator=(SharedInt &amp;&amp;) = default;
    int number() const
    {
        return mNumber;
    }

  private:
    int mNumber;
};
int main()
{
    std::shared_ptr&lt;SharedInt&gt; a = std::make_shared&lt;SharedInt&gt;(2);
    std::shared_ptr&lt;SharedInt&gt; b = std::make_shared&lt;SharedInt&gt;(4);
    *a = *b;
    std::cout &lt;&lt; a-&gt;number() &lt;&lt; std::endl;
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;4

<h2>See also</h2>

shared_ptr smart pointer with shared object ownership semantics 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
