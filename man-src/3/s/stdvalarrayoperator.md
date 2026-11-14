---
title: "stdvalarrayoperator(3)"
name: "stdvalarrayoperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdvalarrayoperator/"
description: "std::valarray<T>::operator[] – std::valarray<T>::operator[]"
---

<p>std::valarray&lt;T&gt;::operator[] &#8211; std::valarray&lt;T&gt;::operator[]</p>
<h2>Synopsis</h2>
<p>T operator[]( std::size_t pos ) const; <i>(until C++11)</i><br />
const T&amp; operator[]( std::size_t pos ) const; <i>(since C++11)</i><br />
T&amp; operator[]( std::size_t pos ); <code>(2)</code><br />
std::valarray&lt;T&gt; operator[]( std::slice slicearr ) const; <code>(3)</code><br />
std::slice_array&lt;T&gt; operator[]( std::slice slicearr ); <code>(4)</code><br />
std::valarray&lt;T&gt; operator[]( const std::gslice&amp; gslicearr ) const; <code>(1)</code> <code>(5)</code><br />
std::gslice_array&lt;T&gt; operator[]( const std::gslice&amp; gslicearr ); <code>(6)</code><br />
std::valarray&lt;T&gt; operator[]( const valarray&lt;bool&gt;&amp; boolarr ) const; <code>(7)</code><br />
std::mask_array&lt;T&gt; operator[]( const valarray&lt;bool&gt;&amp; boolarr ); <code>(8)</code><br />
std::valarray&lt;T&gt; operator[]( const valarray&lt;std::size_t&gt;&amp; indarr ) const; <code>(9)</code><br />
std::indirect_array&lt;T&gt; operator[]( const valarray&lt;std::size_t&gt;&amp; indarr ); <code>(10)</code><br />
Retrieve single elements or portions of the array.<br />
The const overloads that return element sequences create a new std::valarray object. The non-const overloads return classes holding references to the array elements. </p>
<h2>Parameters</h2>
<p>&nbsp;This section is incomplete<br />
&nbsp;Reason: Explain the parameters</p>
<h2>Return value</h2>
<p>1,2) A reference to the corresponding element<br />
3,5,7,9) A std::valarray object containing copies of the selected items<br />
4,6,8,10) The corresponding data structure containing references to the selected items </p>
<h2>Exceptions</h2>
<p><i>(none)</i></p>
<h2>Precondition</h2>
<p>The selected elements must exist.</p>
<h2>Notes</h2>
<p>* For proper values of i and j, the following properties are true: </p>
<pre><code>1) (a[i] = q, a[i]) == q</code></pre>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;For a non-const a.<br />
2) &amp;a[i+j] == &amp;a[i] + j<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;This means that valarray elements are adjacent in memory.<br />
3) &amp;a[i] != &amp;b[j]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;This holds for every objects a and b that are not aliases of one another.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;This means that there are no aliases in the elements and this property can be used to perform some kinds of optimization.<br />
* References become invalid on resize or when the array is destructed.<br />
For overloads (3,5,7,9), The function can be implemented with the return type different from std::valarray. In this case, the replacement type has the following properties:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* All const member functions of std::valarray are provided.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* std::valarray, std::slice_array, std::gslice_array, std::mask_array and std::indirect_array can be constructed from the replacement type.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* All functions accepting an argument of type const std::valarray&amp;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;except begin() and end()<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(since C++11)</i> should also accept the replacement type.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* All functions accepting two arguments of type const std::valarray&amp; should accept every combination of const std::valarray&amp; and the replacement type.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* The return type does not add more than two levels of template nesting over the most deeply-nested argument type. </p>
<h2>Notes</h2>
<p>Slice/mask/indirect index accesses do not chain: v[v==n][std::slice(0,5,2)] = x; is an error because std::mask_array (the type of v[v==n]) does not have operator[].</p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;valarray&gt;
int main()

{
    std::valarray&lt;int&gt; data = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    std::cout &lt;&lt; &quot;Initial valarray: &quot;;
    for (int n : data)
        std::cout &lt;&lt; n &lt;&lt; ' ';
    std::cout &lt;&lt; '
';
    data[data &gt; 5] = -1; // valarray&lt;bool&gt; overload of operator[]
                         // the type of data&gt;5 is std::valarray&lt;bool&gt;
                         // the type of data[data&gt;5] is std::mask_array&lt;int&gt;
    std::cout &lt;&lt; &quot;After v[v&gt;5]=-1:  &quot;;
    for (std::size_t n = 0; n &lt; data.size(); ++n)
        std::cout &lt;&lt; data[n] &lt;&lt; ' '; // regular operator[]
    std::cout &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;Initial valarray: 0 1 2 3 4 5 6 7 8 9<br />
&nbsp;<wbr>&nbsp;After v[v&gt;5]=-1: 0 1 2 3 4 5 -1 -1 -1 -1</p>
