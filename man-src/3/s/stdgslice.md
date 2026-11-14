---
title: "stdgslice(3)"
name: "stdgslice"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdgslice/"
description: "std::gslice – std::gslice"
---

<p>std::gslice &#8211; std::gslice</p>
<h2>Synopsis</h2>
<pre><code>Defined in header &lt;valarray&gt;

class gslice;</code></pre>
<p>std::gslice is the selector class that identifies a subset of std::valarray indices defined by a multi-level set of strides and sizes. Objects of type std::gslice can be used as indices with valarray&#8217;s operator[] to select, for example, columns of a multidimensional array represented as a valarray.<br />
Given the starting value s, a list of strides i<br />
j and a list of sizes d<br />
j, a std::gslice constructed from these values selects the set of indices k<br />
j=s+Σ<br />
j(i<br />
jd<br />
j).<br />
For example, a gslice with starting index 3, strides {19,4,1} and lengths {2,4,3} generates the following set of indices:<br />
3 + 0*19 + 0*4 + 0*1 = 3,<br />
3 + 0*19 + 0*4 + 1*1 = 4,<br />
3 + 0*19 + 0*4 + 2*1 = 5,<br />
3 + 0*19 + 1*4 + 0*1 = 7,<br />
3 + 0*19 + 1*4 + 1*1 = 8,<br />
&#8230;<br />
3 + 1*19 + 3*4 + 2*1 = 36<br />
It is possible to construct std::gslice objects that select some indices more than once: if the above example used the strides {1,1,1}, the indices would have been {3, 4, 5, 4, 5, 6, &#8230;}. Such gslices may only be used as arguments to the const version of std::valarray::operator[], otherwise the behavior is undefined. </p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a generic slice<br />
constructor <i>(public member function)</i> </p>
<p>start returns the parameters of the slice<br />
size <i>(public member function)</i><br />
stride </p>
<p>&nbsp;std::gslice::gslice </p>
<p>gslice()<br />
gslice( std::size_t start, const std::valarray&lt;std::size_t&gt;&amp; sizes,<br />
const std::valarray&lt;std::size_t&gt;&amp; strides );<br />
gslice( const gslice&amp; other ); </p>
<p>Constructs a new generic slice.<br />
1) Default constructor. Equivalent to gslice(0, std::valarray&lt;std::size_t&gt;(), std::valarray&lt;std::size_t&gt;()). This constructor exists only to allow construction of arrays of slices.<br />
2) Constructs a new slice with parameters start, sizes, strides.<br />
3) Constructs a copy of other.</p>
<h2>Parameters</h2>
<p>start &#8211; the position of the first element<br />
sizes &#8211; an array that defines the number of elements in each dimension<br />
strides &#8211; an array that defines the number of positions between successive elements in each dimension<br />
other &#8211; another slice to copy </p>
<p>&nbsp;std::slice::start, size, stride </p>
<p>std::size_t start() const; <code>(1)</code><br />
std::valarray&lt;std::size_t&gt; size() const; <code>(2)</code><br />
std::valarray&lt;std::size_t&gt; stride() const; <code>(3)</code> </p>
<p>Returns the parameters passed to the slice on construction &#8211; start, sizes and strides respectively.</p>
<h2>Parameters</h2>
<p><i>(none)</i></p>
<h2>Return value</h2>
<p>The parameters of the slice &#8212; start, sizes and strides respectively. </p>
<h2>Complexity</h2>
<p>Constant.</p>
<h2>Example</h2>
<p>demonstrates the use of gslices to address columns of a 3D array<br />
 // Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;valarray&gt;

void test_print(std::valarray&lt;int&gt; &amp;v, int rows, int cols, int planes)

{
    for (int r = 0; r &lt; rows; ++r) {
        for (int c = 0; c &lt; cols; ++c) {
            for (int z = 0; z &lt; planes; ++z)
                std::cout &lt;&lt; v[r * cols * planes + c * planes + z] &lt;&lt; ' ';
            std::cout &lt;&lt; '
';
        }
        std::cout &lt;&lt; '
';
    }
}

int main()

{
    std::valarray&lt;int&gt; v = // 3d array: 2 x 4 x 3 elements
        {111, 112, 113, 121, 122, 123, 131, 132, 133, 141, 142, 143,
         211, 212, 213, 221, 222, 223, 231, 232, 233, 241, 242, 243};
    // int ar3d[2][4][3]
    std::cout &lt;&lt; &quot;Initial 2x4x3 array:
&quot;;
    test_print(v, 2, 4, 3);
    // update every value in the first columns of both planes
    v[std::gslice(0, {2, 4}, {4 * 3, 3})] = 1; // two level one strides of 12 elements
                                               // then four level two strides of 3 elements
                                               // subtract the third column from the second column in the 1st plane
    v[std::gslice(1, {1, 4}, {4 * 3, 3})] -= v[std::gslice(2, {1, 4}, {4 * 3, 3})];
    std::cout &lt;&lt; &quot;After column operations: 
&quot;;
    test_print(v, 2, 4, 3);
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;Initial 2x4x3 array:<br />
&nbsp;<wbr>&nbsp;111 112 113<br />
&nbsp;<wbr>&nbsp;121 122 123<br />
&nbsp;<wbr>&nbsp;131 132 133<br />
&nbsp;<wbr>&nbsp;141 142 143 </p>
<p>&nbsp;<wbr>&nbsp;211 212 213<br />
&nbsp;<wbr>&nbsp;221 222 223<br />
&nbsp;<wbr>&nbsp;231 232 233<br />
&nbsp;<wbr>&nbsp;241 242 243 </p>
<p>&nbsp;<wbr>&nbsp;After column operations:<br />
&nbsp;<wbr>&nbsp;1 -1 113<br />
&nbsp;<wbr>&nbsp;1 -1 123<br />
&nbsp;<wbr>&nbsp;1 -1 133<br />
&nbsp;<wbr>&nbsp;1 -1 143 </p>
<p>&nbsp;<wbr>&nbsp;1 212 213<br />
&nbsp;<wbr>&nbsp;1 222 223<br />
&nbsp;<wbr>&nbsp;1 232 233<br />
&nbsp;<wbr>&nbsp;1 242 243</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;get/set valarray element, slice, or mask<br />
operator[] <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BLAS-like slice of a valarray: starting index, length, stride<br />
slice <i>(class)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;proxy to a subset of a valarray after applying a gslice<br />
gslice_array <i>(class template)</i> </p>
