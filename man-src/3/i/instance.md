---
title: "instance(3)"
name: "instance"
section: "3"
letter: "i"
url: "/docs/linux/man/3-instance/"
description: "QuantLib::Singleton – Basic support for the singleton pattern."
---

<h2 class="name">NAME</h2>
<p> QuantLib::Singleton &#8211; Basic support for the singleton pattern. </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;ql/patterns/singleton.hpp&gt; </p>
<p> Inherits boost::noncopyable. </p>
<h3>Static Public Member Functions</h3>
<p> static T &amp; <code>instance</code> ()<br />
 <i>access to the unique instance </i></p>
<h2>Detailed Description</h2>
<h3>template&lt;class T&gt; class QuantLib::Singleton&lt; T &gt;</h3>
<p> Basic support for the singleton pattern. </p>
<p> The typical use of this class is: </p>
<pre><code>
class Foo : public Singleton&lt;Foo&gt;
{
    friend class Singleton&lt;Foo&gt;;

  private:
    Foo()
    {
    }

  public:
    ...
};
</code></pre>
<p>&nbsp;<wbr>which, albeit sub-optimal, frees one from the concerns of creating and managing the unique instance and can serve later as a single implemementation point should synchronization features be added.&nbsp;<wbr> </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for QuantLib from the source code. </p>
<h2>Index</h2>
