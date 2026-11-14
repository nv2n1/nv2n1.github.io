---
title: "stdtuple(3)"
name: "stdtuple"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdtuple/"
---

std::tuple - std::tuple

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;tuple&gt;

template&lt; class... Types &gt;  (since C++11)

class tuple;</code></pre> 
Class template std::tuple is a fixed-size collection of heterogeneous values. It is a generalization of std::pair. 
If (std::is_trivially_destructible_v&lt;Types&gt; &amp;&amp; ...) is true, the destructor of tuple is trivial. <i>(since C++17)</i> 

<h2>Template parameters</h2>

Types... - the types of the elements that the tuple stores. Empty list is supported.

<h2>Member functions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a new tuple 
constructor <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;assigns the contents of one tuple to another 
operator= <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;swaps the contents of two tuples 
swap <i>(public member function)</i>

<h2>Non-member functions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;creates a tuple object of the type defined by the argument types 
make_tuple <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;creates a tuple of lvalue references or unpacks a tuple into individual objects 
tie <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;creates a tuple of rvalue references 
forward_as_tuple <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;creates a tuple by concatenating any number of tuples 
tuple_cat <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tuple accesses specified element 
std::get(std::tuple) <i>(function template)</i> 

 
operator== 
operator!= lexicographically compares the values in the tuple 
operator&lt; <i>(function template)</i> 
operator&lt;= 
operator&gt; 
operator&gt;= 

 
std::swap(std::tuple) specializes the std::swap algorithm 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i>

<h2>Helper classes</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;obtains the size of tuple at compile time 
tuple_size <i>(class template specialization)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;obtains the type of the specified element 
tuple_element <i>(class template specialization)</i> 

 
std::uses_allocator&lt;std::tuple&gt; specializes the std::uses_allocator type trait 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template specialization)</i> 
<i>(C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;placeholder to skip an element when unpacking a tuple using tie 
ignore (constant) 

 

 
Deduction_guides<i>(since C++17)</i>

<h2>Notes</h2>

Until C++17, a function could not return a tuple using list-initialization: std::tuple&lt;int, int&gt; foo_tuple()

{
    return {1, -1};                // Error until C++17
    return std::make_tuple(1, -1); // Always works
}


<h2>Example</h2>

// Run this code <pre><code>#include &lt;tuple&gt;

#include &lt;iostream&gt;

#include &lt;string&gt;

#include &lt;stdexcept&gt;
std::tuple&lt;double, char, std::string&gt; get_student(int id)

{
    if (id == 0)
        return std::make_tuple(3.8, 'A', &quot;Lisa Simpson&quot;);
    if (id == 1)
        return std::make_tuple(2.9, 'C', &quot;Milhouse Van Houten&quot;);
    if (id == 2)
        return std::make_tuple(1.7, 'D', &quot;Ralph Wiggum&quot;);
    throw std::invalid_argument(&quot;id&quot;);
}
int main()

{
    auto student0 = get_student(0);
    std::cout &lt;&lt; &quot;ID: 0, &quot;
              &lt;&lt; &quot;GPA: &quot; &lt;&lt; std::get&lt;0&gt;(student0) &lt;&lt; &quot;, &quot;
              &lt;&lt; &quot;grade: &quot; &lt;&lt; std::get&lt;1&gt;(student0) &lt;&lt; &quot;, &quot;
              &lt;&lt; &quot;name: &quot; &lt;&lt; std::get&lt;2&gt;(student0) &lt;&lt; '\n';
    double gpa1;
    char grade1;
    std::string name1;
    std::tie(gpa1, grade1, name1) = get_student(1);
    std::cout &lt;&lt; &quot;ID: 1, &quot;
              &lt;&lt; &quot;GPA: &quot; &lt;&lt; gpa1 &lt;&lt; &quot;, &quot;
              &lt;&lt; &quot;grade: &quot; &lt;&lt; grade1 &lt;&lt; &quot;, &quot;
              &lt;&lt; &quot;name: &quot; &lt;&lt; name1 &lt;&lt; '\n';
    // C++17 structured binding:
    auto [gpa2, grade2, name2] = get_student(2);
    std::cout &lt;&lt; &quot;ID: 2, &quot;
              &lt;&lt; &quot;GPA: &quot; &lt;&lt; gpa2 &lt;&lt; &quot;, &quot;
              &lt;&lt; &quot;grade: &quot; &lt;&lt; grade2 &lt;&lt; &quot;, &quot;
              &lt;&lt; &quot;name: &quot; &lt;&lt; name2 &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;ID: 0, GPA: 3.8, grade: A, name: Lisa Simpson 
&nbsp;<wbr>&nbsp;ID: 1, GPA: 2.9, grade: C, name: Milhouse Van Houten 
&nbsp;<wbr>&nbsp;ID: 2, GPA: 1.7, grade: D, name: Ralph Wiggum

<h2>References</h2>

* C++11 standard (ISO/IEC 14882:2011): 

 

 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* 20.4 Tuples [tuple]
