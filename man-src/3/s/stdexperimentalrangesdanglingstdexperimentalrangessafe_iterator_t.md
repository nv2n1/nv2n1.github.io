---
title: "stdexperimentalrangesdanglingstdexperimentalrangessafe_iterator_t(3)"
name: "stdexperimentalrangesdanglingstdexperimentalrangessafe_iterator_t"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesdanglingstdexperimentalrangessafe_iterator_t/"
description: "std::experimental::ranges::dangling,std::experimental::ranges::safe_iterator_t – std::experimental::ranges::dangling,std::experimental::ranges::safe_iterator_t"
---

<p>std::experimental::ranges::dangling,std::experimental::ranges::safe_iterator_t &#8211; std::experimental::ranges::dangling,std::experimental::ranges::safe_iterator_t</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;experimental / ranges / iterator&gt;

    template &lt;CopyConstructible T&gt;

    class dangling
{

  public:
    dangling() requires DefaultConstructible&lt;T&gt;();
    (ranges TS)

        dangling(T t);

    T get_unsafe() const;
};

template &lt;Range R&gt;

using safe_iterator_t = std::conditional_t &lt; std::is_lvalue_reference&lt;R&gt;::value,
      (ranges TS)

          ranges::iterator_t&lt;R&gt;,

      ranges::dangling&lt;ranges::iterator_t&lt;R&gt;&gt;;</code></pre>
<p>The class template dangling is a simple wrapper around an object to indicate that the wrapped object may be dangling, that is, it refers to another object whose lifetime may have ended.<br />
The alias template safe_iterator_t returns the iterator type of R, wrapped in dangling if the range was an rvalue range (as indicated by R not being an lvalue reference type).<br />
They are used by range algorithms that accept rvalue ranges and return iterators into them. </p>
<h2>Member functions</h2>
<p>&nbsp;std::experimental::ranges::dangling::dangling </p>
<p>dangling() requires DefaultConstructible&lt;T&gt;(); <code>(1)</code><br />
dangling(T t); <code>(2)</code> </p>
<p>1) Default constructor. Value-initializes the wrapped object.<br />
2) Initializes the wrapped object with t. Note that this constructor defines an implicit conversion from T to dangling&lt;T&gt;. </p>
<p>&nbsp;std::experimental::ranges::dangling::get_unsafe </p>
<p>T get_unsafe() const; </p>
<p>Returns a copy of the wrapped object.</p>
