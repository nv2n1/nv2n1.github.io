---
title: "stdin_placestdin_place_typestdin_place_indexstdin_place_t(3)"
name: "stdin_placestdin_place_typestdin_place_indexstdin_place_t"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdin_placestdin_place_typestdin_place_indexstdin_place_t/"
---

std::in_place,std::in_place_type,std::in_place_index,std::in_place_t, - std::in_place,std::in_place_type,std::in_place_index,std::in_place_t,

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;utility&gt;

    struct in_place_t {
    explicit in_place_t() = default;
    (since C++ 17)
};
inline constexpr in_place_t in_place{};

template &lt;class T&gt;
struct in_place_type_t {
    explicit in_place_type_t() = default;
};
(since C++ 17)

    template &lt;class T&gt;
    inline constexpr in_place_type_t&lt;T&gt; in_place_type{};

template &lt;std::size_t I&gt;
struct in_place_index_t {
    explicit in_place_index_t() = default;
};
(since C++ 17)

    template &lt;std::size_t I&gt;
    inline constexpr in_place_index_t&lt;I&gt; in_place_index{};</code></pre> 
std::in_place, std::in_place_type, and std::in_place_index are disambiguation tags 
that can be passed to the constructors of std::optional, std::variant, and std::any 
to indicate that the contained object should be constructed in-place, and&nbsp;<wbr>(for the 
latter two)&nbsp;<wbr>the type of the object to be constructed. 
The corresponding type/type templates std::in_place_t, std::in_place_type_t and 
std::in_place_index_t can be used in the constructor's parameter list to match the 
intended tag. 

<h2>See also</h2>

optional a wrapper that may or may not hold an object 
<i>(C++17)</i>&nbsp;<wbr>&nbsp;<wbr><i>(class template)</i> 
variant&nbsp;<wbr>&nbsp;<wbr>a type-safe discriminated union 
<i>(C++17)</i>&nbsp;<wbr>&nbsp;<wbr><i>(class template)</i> 
any&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Objects that hold instances of any CopyConstructible type. 
<i>(C++17)</i>&nbsp;<wbr>&nbsp;<wbr><i>(class)</i> 
