---
title: "stdmake_uniquestdmake_unique_default_init(3)"
name: "stdmake_uniquestdmake_unique_default_init"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdmake_uniquestdmake_unique_default_init/"
description: "std::make_unique,std::make_unique_default_init – std::make_unique,std::make_unique_default_init"
---

<p>std::make_unique,std::make_unique_default_init &#8211; std::make_unique,std::make_unique_default_init</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;memory&gt;

    template &lt;class T, class... Args&gt;
    (1)(since C++ 14)

        unique_ptr&lt;T&gt; make_unique(Args &amp;&amp;...args);                               (only for non-array types)

template&lt; class T &gt;                                                    (2) (since C++14)

unique_ptr&lt;T&gt; make_unique( std::size_t size );                             (only for array types with unknown bound)

template&lt; class T, class... Args &gt;                                     (3) (since C++14)

/* unspecified */ make_unique( Args&amp;&amp;... args ) = delete;                  (only for array types with known bound)

template&lt; class T &gt;                                                    (4) (since C++20)

unique_ptr&lt;T&gt; make_unique_default_init( );                                 (only for non-array types)

template&lt; class T &gt;                                                    (5) (since C++20)

unique_ptr&lt;T&gt; make_unique_default_init( std::size_t size );                (only for array types with unknown bound)

template&lt; class T, class... Args &gt;                                     (6) (since C++20)

/* unspecified */ make_unique_default_init( Args&amp;&amp;... args ) = delete;     (only for array types with known bound)</code></pre>
<p>Constructs an object of type T and wraps it in a std::unique_ptr.<br />
1) Constructs a non-array type T. The arguments args are passed to the constructor of T. This overload only participates in overload resolution if T is not an array type. The function is equivalent to:<br />
&nbsp;<wbr>&nbsp;unique_ptr&lt;T&gt;(new T(std::forward&lt;Args&gt;(args)&#8230;))<br />
2) Constructs an array of unknown bound T. This overload only participates in overload resolution if T is an array of unknown bound. The function is equivalent to:<br />
&nbsp;<wbr>&nbsp;unique_ptr&lt;T&gt;(new typename std::remove_extent&lt;T&gt;::type[size]())<br />
3,6) Construction of arrays of known bound is disallowed.<br />
4) Same as <code>(1)</code>, except that the object is default-initialized. This overload only participates in overload resolution if T is not an array type. The function is equivalent to:<br />
&nbsp;<wbr>&nbsp;unique_ptr&lt;T&gt;(new T)<br />
5) Same as <code>(2)</code>, except that the array is default-initialized. This overload only participates in overload resolution if T is an array of unknown bound. The function is equivalent to:<br />
&nbsp;<wbr>&nbsp;unique_ptr&lt;T&gt;(new typename std::remove_extent&lt;T&gt;::type[size]) </p>
<h2>Parameters</h2>
<p>args &#8211; list of arguments with which an instance of T will be constructed.<br />
size &#8211; the size of the array to construct</p>
<h2>Return value</h2>
<p>std::unique_ptr of an instance of type T. </p>
<h2>Exceptions</h2>
<p>May throw std::bad_alloc or any exception thrown by the constructor of T. If an exception is thrown, this function has no effect. </p>
<p>Possible Implementation </p>
<p>&nbsp;<wbr>&nbsp;// note: this implementation does not disable this overload for array types<br />
&nbsp;<wbr>&nbsp;template&lt;typename T, typename&#8230; Args&gt;<br />
&nbsp;<wbr>&nbsp;std::unique_ptr&lt;T&gt; make_unique(Args&amp;&amp;&#8230; args)<br />
&nbsp;<wbr>&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return std::unique_ptr&lt;T&gt;(new T(std::forward&lt;Args&gt;(args)&#8230;));<br />
&nbsp;<wbr>&nbsp;}</p>
<h2>Notes</h2>
<p>Unlike std::make_shared (which has std::allocate_shared), std::make_unique does not have an allocator-aware counterpart. A hypothetical allocate_unique would be required to invent the deleter type D for the unique_ptr&lt;T,D&gt; it returns which would contain an allocator object and invoke both destroy and deallocate in its operator(). </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;memory&gt;
struct Vec3

{
    int x, y, z;
    Vec3()
        : x(0), y(0), z(0)
    {
    }
    Vec3(int x, int y, int z)
        : x(x), y(y), z(z)
    {
    }
    friend std::ostream &amp;operator&lt;&lt;(std::ostream &amp;os, Vec3 &amp;v)
    {
        return os &lt;&lt; '{' &lt;&lt; &quot;x:&quot; &lt;&lt; v.x &lt;&lt; &quot; y:&quot; &lt;&lt; v.y &lt;&lt; &quot; z:&quot; &lt;&lt; v.z &lt;&lt; '}';
    }
};
int main()

{
    // Use the default constructor.
    std::unique_ptr&lt;Vec3&gt; v1 = std::make_unique&lt;Vec3&gt;();
    // Use the constructor that matches these arguments
    std::unique_ptr&lt;Vec3&gt; v2 = std::make_unique&lt;Vec3&gt;(0, 1, 2);
    // Create a unique_ptr to an array of 5 elements
    std::unique_ptr&lt;Vec3[]&gt; v3 = std::make_unique&lt;Vec3[]&gt;(5);
    std::cout &lt;&lt; &quot;make_unique&lt;Vec3&gt;():      &quot; &lt;&lt; *v1 &lt;&lt; '
'
              &lt;&lt; &quot;make_unique&lt;Vec3&gt;(0,1,2): &quot; &lt;&lt; *v2 &lt;&lt; '
'
              &lt;&lt; &quot;make_unique&lt;Vec3[]&gt;(5):   &quot; &lt;&lt; '
';
    for (int i = 0; i &lt; 5; i++) {
        std::cout &lt;&lt; &quot;     &quot; &lt;&lt; v3[i] &lt;&lt; '
';
    }
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;make_unique&lt;Vec3&gt;(): {x:0 y:0 z:0}<br />
&nbsp;<wbr>&nbsp;make_unique&lt;Vec3&gt;(0,1,2): {x:0 y:1 z:2}<br />
&nbsp;<wbr>&nbsp;make_unique&lt;Vec3[]&gt;<code>(5)</code>:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;{x:0 y:0 z:0}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;{x:0 y:0 z:0}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;{x:0 y:0 z:0}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;{x:0 y:0 z:0}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;{x:0 y:0 z:0}</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a new unique_ptr<br />
constructor <i>(public member function)</i><br />
make_shared<br />
make_shared_default_init creates a shared pointer that manages a new object<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
(C++20) </p>
