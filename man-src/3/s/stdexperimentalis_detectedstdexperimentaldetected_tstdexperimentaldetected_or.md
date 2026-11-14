---
title: "stdexperimentalis_detectedstdexperimentaldetected_tstdexperimentaldetected_or(3)"
name: "stdexperimentalis_detectedstdexperimentaldetected_tstdexperimentaldetected_or"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalis_detectedstdexperimentaldetected_tstdexperimentaldetected_or/"
---

std::experimental::is_detected,std::experimental::detected_t,std::experimental::detected_or - std::experimental::is_detected,std::experimental::detected_t,std::experimental::detected_or

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;experimental/type_traits&gt;

template&lt; template&lt;class...&gt; class Op, class... Args &gt;                 (library fundamentals TS v2)

using is_detected = /* see below */;

template&lt; template&lt;class...&gt; class Op, class... Args &gt;                 (library fundamentals TS v2)

using detected_t = /* see below */;

template&lt; class Default, template&lt;class...&gt; class Op, class... Args &gt;  (library fundamentals TS v2)

using detected_or = /* see below */;</code></pre> 
The alias template detected_or is an alias for an unspecified class type with two public member typedefs value_t and type, which are defined as follows: 
* If the template-id Op&lt;Args...&gt; denotes a valid type, then value_t is an alias for std::true_type, and type is an alias for Op&lt;Args...&gt;; 
* Otherwise, value_t is an alias for std::false_type and type is an alias for Default. 
The alias template is_detected is equivalent to typename detected_or&lt;std::experimental::nonesuch, Op, Args...&gt;::value_t. It is an alias for std::true_type if the template-id Op&lt;Args...&gt; denotes a valid type; otherwise it is an alias for std::false_type. 
The alias template detected_t is equivalent to typename detected_or&lt;std::experimental::nonesuch, Op, Args...&gt;::type. It is an alias for Op&lt;Args...&gt; if that template-id denotes a valid type; otherwise it is an alias for the class std::experimental::nonesuch. 
Additional utilities template&lt; template&lt;class...&gt; class Op, class... Args &gt;                                       (library fundamentals TS v2)

constexpr bool is_detected_v = is_detected&lt;Op, Args...&gt;::value;

template&lt; class Default, template&lt;class...&gt; class Op, class... Args &gt;                        (library fundamentals TS v2)

using detected_or_t = typename detected_or&lt;Default, Op, Args...&gt;::type;

template &lt;class Expected, template&lt;class...&gt; class Op, class... Args&gt;                        (library fundamentals TS v2)

using is_detected_exact = std::is_same&lt;Expected, detected_t&lt;Op, Args...&gt;&gt;;

template &lt;class Expected, template&lt;class...&gt; class Op, class... Args&gt;                        (library fundamentals TS v2)

constexpr bool is_detected_exact_v = is_detected_exact&lt;Expected, Op, Args...&gt;::value;

template &lt;class To, template&lt;class...&gt; class Op, class... Args&gt;                              (library fundamentals TS v2)

using is_detected_convertible = std::is_convertible&lt;detected_t&lt;Op, Args...&gt;, To&gt;;

template &lt;class To, template&lt;class...&gt; class Op, class... Args&gt;                              (library fundamentals TS v2)

constexpr bool is_detected_convertible_v = is_detected_convertible&lt;To, Op, Args...&gt;::value; 
The alias template is_detected_exact checks whether detected_t&lt;Op, Args...&gt; is Expected. 
The alias template is_detected_convertible checks whether detected_t&lt;Op, Args...&gt; is convertible to To. 

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;namespace detail { 
&nbsp;<wbr>&nbsp;template &lt;class Default, class AlwaysVoid, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;template&lt;class...&gt; class Op, class... Args&gt; 
&nbsp;<wbr>&nbsp;struct detector { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;using value_t = std::false_type; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;using type = Default; 
&nbsp;<wbr>&nbsp;}; 

 
&nbsp;<wbr>&nbsp;template &lt;class Default, template&lt;class...&gt; class Op, class... Args&gt; 
&nbsp;<wbr>&nbsp;struct detector&lt;Default, std::void_t&lt;Op&lt;Args...&gt;&gt;, Op, Args...&gt; { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;// Note that std::void_t is a C++17 feature 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;using value_t = std::true_type; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;using type = Op&lt;Args...&gt;; 
&nbsp;<wbr>&nbsp;}; 

 
&nbsp;<wbr>&nbsp;} // namespace detail 

 
&nbsp;<wbr>&nbsp;template &lt;template&lt;class...&gt; class Op, class... Args&gt; 
&nbsp;<wbr>&nbsp;using is_detected = typename detail::detector&lt;nonesuch, void, Op, Args...&gt;::value_t; 

 
&nbsp;<wbr>&nbsp;template &lt;template&lt;class...&gt; class Op, class... Args&gt; 
&nbsp;<wbr>&nbsp;using detected_t = typename detail::detector&lt;nonesuch, void, Op, Args...&gt;::type; 

 
&nbsp;<wbr>&nbsp;template &lt;class Default, template&lt;class...&gt; class Op, class... Args&gt; 
&nbsp;<wbr>&nbsp;using detected_or = detail::detector&lt;Default, void, Op, Args...&gt;;

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


