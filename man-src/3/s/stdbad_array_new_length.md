---
title: "stdbad_array_new_length(3)"
name: "stdbad_array_new_length"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdbad_array_new_length/"
description: "std::bad_array_new_length – std::bad_array_new_length"
---

<p>std::bad_array_new_length &#8211; std::bad_array_new_length</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;new&gt;<br />
class bad_array_new_length; <i>(since C++11)</i><br />
std::bad_array_new_length is the type of the object thrown as exceptions by the new-expressions to report invalid array lengths if<br />
1) array length is negative<br />
2) total size of the new array would exceed implementation-defined maximum value<br />
3) the number of initializer-clauses exceeds the number of elements to initialize<br />
Only the first array dimension may generate this exception; dimensions other than the first are constant expressions and are checked at compile time.<br />
&nbsp;std-bad array new length-inheritance.svg<br />
Inheritance diagram </p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs the bad_array_new_length object<br />
constructor <i>(public member function)</i> </p>
<p>Inherited from std::bad_alloc </p>
<p>Inherited from std::exception</p>
<h2>Member functions</h2>
<p>destructor destroys the exception object<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual public member function of std::exception)</i><br />
<code>[virtual]</code> </p>
<p>what returns an explanatory string<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual public member function of std::exception)</i><br />
<code>[virtual]</code></p>
<h2>Notes</h2>
<p>The override for the virtual member function what() may by provided, but is not required. </p>
<h2>Example</h2>
<p>Three conditions where std::bad_array_new_length should be thrown:<br />
 // Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;new&gt;

#include &lt;climits&gt;
int main()

{
    int negative = -1;
    int small = 1;
    int large = INT_MAX;
    try {
        new int[negative];       // negative size
        new int[small]{1, 2, 3}; // too many initializers
        new int[large][1000000]; // too large
    } catch (const std::bad_array_new_length &amp;e) {
        std::cout &lt;&lt; e.what() &lt;&lt; '
';
    }
}
</code></pre>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;allocation functions<br />
operator_new <i>(function)</i><br />
operator_new[]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exception thrown when memory allocation fails<br />
bad_alloc <i>(class)</i> </p>
