---
title: "stdslice(3)"
name: "stdslice"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdslice/"
description: "std::slice – std::slice"
---

<p>std::slice &#8211; std::slice</p>
<h2>Synopsis</h2>
<pre><code>Defined in header &lt;valarray&gt;

class slice;</code></pre>
<p>std::slice is the selector class that identifies a subset of std::valarray similar to BLAS slice. An object of type std::slice holds three values: the starting index, the stride, and the total number of values in the subset. Objects of type std::slice can be used as indexes with valarray&#8217;s operator[]. </p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a slice<br />
constructor <i>(public member function)</i> </p>
<p>start returns the parameters of the slice<br />
size <i>(public member function)</i><br />
stride </p>
<p>&nbsp;std::slice::slice </p>
<p>slice()<br />
slice( std::size_t start, std::size_t size, std::size_t stride );<br />
slice( const slice&amp; other ); </p>
<p>Constructs a new slice.<br />
1) Default constructor. Equivalent to slice(0, 0, 0). This constructor exists only to allow construction of arrays of slices.<br />
2) Constructs a new slice with parameters start, size, stride. This slice will refer to size number of elements, each with the position:<br />
start + 0*stride<br />
start + 1*stride<br />
&#8230;<br />
start + (size-1)*stride<br />
3) Constructs a copy of other.</p>
<h2>Parameters</h2>
<p>start &#8211; the position of the first element<br />
size &#8211; the number of elements in the slice<br />
stride &#8211; the number of positions between successive elements in the slice<br />
other &#8211; another slice to copy </p>
<p>&nbsp;std::slice::start, size, stride </p>
<p>std::size_t start() const; <code>(1)</code><br />
std::size_t size() const; <code>(2)</code><br />
std::size_t stride() const; <code>(3)</code> </p>
<p>Returns the parameters passed to the slice on construction &#8211; start, size and stride respectively.</p>
<h2>Parameters</h2>
<p><i>(none)</i></p>
<h2>Return value</h2>
<p>The parameters of the slice &#8212; start, size and stride respectively. </p>
<h2>Complexity</h2>
<p>Constant.</p>
<h2>Example</h2>
<p>Barebones valarray-backed Matrix class with a trace calculating function.<br />
 // Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;valarray&gt;

class Matrix
{
    std::valarray&lt;int&gt; data;
    int dim;

  public:
    Matrix(int r, int c)
        : data(r * c), dim(c)
    {
    }
    int &amp;operator()(int r, int c)
    {
        return data[r * dim + c];
    }
    int trace() const
    {
        return data[std::slice(0, dim, dim + 1)].sum();
    }
};

int main()

{
    Matrix m(3, 3);
    int n = 0;
    for (int r = 0; r &lt; 3; ++r)
        for (int c = 0; c &lt; 3; ++c)
            m(r, c) = ++n;
    std::cout &lt;&lt; &quot;Trace of the matrix (1,2,3) (4,5,6) (7,8,9) is &quot; &lt;&lt; m.trace() &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;Trace of the matrix (1,2,3) (4,5,6) (7,8,9) is 15</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;get/set valarray element, slice, or mask<br />
operator[] <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;generalized slice of a valarray: starting index, set of lengths, set of strides<br />
gslice <i>(class)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;proxy to a subset of a valarray after applying a slice<br />
slice_array <i>(class template)</i> </p>
