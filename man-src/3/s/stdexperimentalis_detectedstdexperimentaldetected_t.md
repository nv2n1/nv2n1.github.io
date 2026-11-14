---
title: "stdexperimentalis_detectedstdexperimentaldetected_t(3)"
name: "stdexperimentalis_detectedstdexperimentaldetected_t"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalis_detectedstdexperimentaldetected_t/"
---

std::experimental::is_detected,std::experimental::detected_t, - std::experimental::is_detected,std::experimental::detected_t,

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;experimental/type_traits&gt;

template&lt; template&lt;class...&gt; class Op, class... Args &gt;  (library fundamentals TS v2)

using is_detected = /* see below */;

template&lt; template&lt;class...&gt; class Op, class... Args &gt;  (library fundamentals TS v2)

using detected_t = /* see below */;

template&lt; class Default, template&lt;class...&gt; class Op,

class... Args &gt;                                         (library fundamentals TS v2)

using detected_or = /* see below */;</code></pre> 
The alias template detected_or is an alias for an unspecified class type with two 
public member typedefs value_t and type, which are defined as follows: 
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>If the template-id Op&lt;Args...&gt;&nbsp;<wbr>denotes a valid type, then value_t is an alias 
&nbsp;<wbr>for std::true_type, and type is an alias for Op&lt;Args...&gt;; 
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>Otherwise, value_t is an alias for std::false_type and type is an alias for 
&nbsp;<wbr>Default. 
The alias template is_detected is equivalent to typename 
detected_or&lt;std::experimental::nonesuch, Op, Args...&gt;::value_t. It is an alias for 
std::true_type if the template-id Op&lt;Args...&gt;&nbsp;<wbr>denotes a valid type;&nbsp;<wbr>otherwise it is 
an alias for std::false_type. 
The alias template detected_t is equivalent to typename 
detected_or&lt;std::experimental::nonesuch, Op, Args...&gt;::type. It is an alias for 
Op&lt;Args...&gt;&nbsp;<wbr>if that template-id denotes a valid type;&nbsp;<wbr>otherwise it is an alias for 
the class std::experimental::nonesuch. 
&nbsp;<wbr>&nbsp;<wbr>Additional utilities template&lt; template&lt;class...&gt; class Op, class... Args &gt;      (library fundamentals TS

constexpr bool is_detected_v = is_detected&lt;Op,              v2)

Args...&gt;::value;

template&lt; class Default, template&lt;class...&gt; class Op,

class... Args &gt;                                             (library fundamentals TS

using detected_or_t = typename detected_or&lt;Default, Op,     v2)

Args...&gt;::type;

template &lt;class Expected, template&lt;class...&gt; class Op,

class... Args&gt;                                              (library fundamentals TS

using is_detected_exact = std::is_same&lt;Expected,            v2)

detected_t&lt;Op, Args...&gt;&gt;;

template &lt;class Expected, template&lt;class...&gt; class Op,

class... Args&gt;                                              (library fundamentals TS

constexpr bool is_detected_exact_v =                        v2)

is_detected_exact&lt;Expected, Op, Args...&gt;::value;

template &lt;class To, template&lt;class...&gt; class Op, class...

Args&gt;                                                       (library fundamentals TS

using is_detected_convertible =                             v2)

std::is_convertible&lt;detected_t&lt;Op, Args...&gt;, To&gt;;

template &lt;class To, template&lt;class...&gt; class Op, class...

Args&gt;                                                       (library fundamentals TS

constexpr bool is_detected_convertible_v =                  v2)

is_detected_convertible&lt;To, Op, Args...&gt;::value; 
The alias template is_detected_exact checks whether detected_t&lt;Op, Args...&gt;&nbsp;<wbr>is 
Expected. 
The alias template is_detected_convertible checks whether detected_t&lt;Op, Args...&gt;&nbsp;<wbr>is 
convertible to To. 

<h2>Possible implementation</h2>

&nbsp;<wbr>namespace detail&nbsp;<wbr>{ 
&nbsp;<wbr>template&nbsp;<wbr>&lt;class Default, class AlwaysVoid, 
&nbsp;<wbr>&nbsp;<wbr>template&lt;class...&gt;&nbsp;<wbr>class Op, class... Args&gt; 
&nbsp;<wbr>struct detector&nbsp;<wbr>{ 
using value_t&nbsp;<wbr>=&nbsp;<wbr>std::false_type; 
using type&nbsp;<wbr>=&nbsp;<wbr>Default; 
&nbsp;<wbr>}; 

 
&nbsp;<wbr>template&nbsp;<wbr>&lt;class Default, template&lt;class...&gt;&nbsp;<wbr>class Op, class... Args&gt; 
&nbsp;<wbr>struct detector&lt;Default, std::void_t&lt;Op&lt;Args...&gt;&gt;, Op, Args...&gt;&nbsp;<wbr>{ 
//&nbsp;<wbr>Note that std::void_t is a C++17 feature 
using value_t&nbsp;<wbr>=&nbsp;<wbr>std::true_type; 
using type&nbsp;<wbr>=&nbsp;<wbr>Op&lt;Args...&gt;; 
&nbsp;<wbr>}; 

 
&nbsp;<wbr>}&nbsp;<wbr>//&nbsp;<wbr>namespace detail 

 
&nbsp;<wbr>template&nbsp;<wbr>&lt;template&lt;class...&gt;&nbsp;<wbr>class Op, class... Args&gt; 
&nbsp;<wbr>using is_detected&nbsp;<wbr>=&nbsp;<wbr>typename detail::detector&lt;nonesuch, void, Op, Args...&gt;::value_t; 

 
&nbsp;<wbr>template&nbsp;<wbr>&lt;template&lt;class...&gt;&nbsp;<wbr>class Op, class... Args&gt; 
&nbsp;<wbr>using detected_t&nbsp;<wbr>=&nbsp;<wbr>typename detail::detector&lt;nonesuch, void, Op, Args...&gt;::type; 

 
&nbsp;<wbr>template&nbsp;<wbr>&lt;class Default, template&lt;class...&gt;&nbsp;<wbr>class Op, class... Args&gt; 
&nbsp;<wbr>using detected_or&nbsp;<wbr>=&nbsp;<wbr>detail::detector&lt;Default, void, Op, Args...&gt;;

<h2>Example</h2>

// Run this code <pre><code>#include &lt;experimental/type_traits&gt;

#include &lt;cstddef&gt;
template &lt;class T&gt;

using copy_assign_t = decltype(std::declval&lt;T &amp;&gt;() = std::declval&lt;const T &amp;&gt;());
struct Meow {
};

struct Purr {
    void operator=(const Purr &amp;) = delete;
};
static_assert(std::experimental::is_detected&lt;copy_assign_t, Meow&gt;::value,
              &quot;Meow should be copy assignable!&quot;);

static_assert(!std::experimental::is_detected_v&lt;copy_assign_t, Purr&gt;,
              &quot;Purr should not be copy assignable!&quot;);

static_assert(std::experimental::is_detected_exact_v&lt;Meow &amp;, copy_assign_t, Meow&gt;,
              &quot;Copy assignment of Meow should return Meow&amp;!&quot;);
template &lt;class T&gt;

using diff_t = typename T::difference_type;
template &lt;class Ptr&gt;

using difference_type = std::experimental::detected_or_t&lt;std::ptrdiff_t, diff_t, Ptr&gt;;
struct Woof {
    using difference_type = int;
};

struct Bark {
};
static_assert(std::is_same&lt;difference_type&lt;Woof&gt;, int&gt;::value,
              &quot;Woof's difference_type should be int!&quot;);

static_assert(std::is_same&lt;difference_type&lt;Bark&gt;, std::ptrdiff_t&gt;::value,
              &quot;Bark's difference_type should be ptrdiff_t!&quot;);
int main()
{
}
</code></pre>

<h2>See also</h2>


