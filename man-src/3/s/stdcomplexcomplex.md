---
title: "stdcomplexcomplex(3)"
name: "stdcomplexcomplex"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdcomplexcomplex/"
---

std::complex&lt;T&gt;::complex - std::complex&lt;T&gt;::complex

<h2>Synopsis</h2>

<pre><code>primary template complex&lt;T&gt;

complex(const T &amp;re = T(), const T &amp;im = T());
(1)(until C++ 14)

    constexpr complex(const T &amp;re = T(), const T &amp;im = T());
(1)(since C++ 14)

    complex(const complex &amp;other);
(2)(until C++ 14)

    constexpr complex(const complex &amp;other);
(2)(since C++ 14)

    template &lt;class X&gt;
    (3)(until C++ 14)

        complex(const complex&lt;X&gt; &amp;other);

template &lt;class X&gt;
(3)(since C++ 14)

    constexpr complex(const complex&lt;X&gt; &amp;other);

specialization complex&lt;float&gt;

complex(float re = 0.0f, float im = 0.0f);
(1)(until C++ 11)

    constexpr complex(float re = 0.0f, float im = 0.0f);
(1)(since C++ 11)

    explicit complex(const complex&lt;double&gt; &amp;other);
(3)(until C++ 11)

    explicit complex(const complex&lt;long double&gt; &amp;other);

explicit constexpr complex(const complex&lt;double&gt; &amp;other);
(3)(since C++ 11)

    explicit constexpr complex(const complex&lt;long double&gt; &amp;other);

specialization complex&lt;double&gt;

complex(double re = 0.0, double im = 0.0);
(1)(until C++ 11)

    constexpr complex(double re = 0.0, double im = 0.0);
(1)(since C++ 11)

    complex(const complex&lt;float&gt; &amp;other);
(3)(until C++ 11)

    explicit complex(const complex&lt;long double&gt; &amp;other);

constexpr complex(const complex&lt;float&gt; &amp;other);
(3)(since C++ 11)

    explicit constexpr complex(const complex&lt;long double&gt; &amp;other);

specialization complex&lt;long double&gt;

complex(long double re = 0.0L, long double im = 0.0L);
(1)(until C++ 11)

    constexpr complex(long double re = 0.0L, long double im = 0.0L);
(1)(since C++ 11)

    complex(const complex&lt;float&gt; &amp;other);
(3)(until C++ 11)

    complex(const complex&lt;double&gt; &amp;other);

constexpr complex(const complex&lt;float&gt; &amp;other);
(3)(since C++ 11)

    constexpr complex(const complex&lt;double&gt; &amp;other);</code></pre> 
Constructs the std::complex object. 
1) Constructs the complex number from real and imaginary parts. 
2) Copy constructor. Constructs the object with the copy of the contents of other. The copy constructor is implicit in the standard specializations. 
3) Converting_constructor. Constructs the object from a complex number of a different type. 

<h2>Parameters</h2>

re - the real part 
im - the imaginary part 
other - another complex to use as source

<h2>See also</h2>

<pre><code>assigns the contents

operator=    (public member function)</code></pre> 
operator&quot;&quot;if 
operator&quot;&quot;i A std::complex literal representing pure imaginary number 
operator&quot;&quot;il <i>(function)</i> 
<i>(C++14)</i> 
