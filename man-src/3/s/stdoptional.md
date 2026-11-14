---
title: "stdoptional(3)"
name: "stdoptional"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdoptional/"
---

std::optional - std::optional

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;optional&gt;

template&lt; class T &gt;           (since C++17)

class optional;</code></pre> 
The class template std::optional manages an optional contained value, i.e. a value that may or may not be present. 
A common use case for optional is the return value of a function that may fail. As opposed to other approaches, such as std::pair&lt;T,bool&gt;, optional handles expensive-to-construct objects well and is more readable, as the intent is expressed explicitly. 
Any instance of optional&lt;T&gt; at any given point in time either contains a value or does not contain a value. 
If an optional&lt;T&gt; contains a value, the value is guaranteed to be allocated as part of the optional object footprint, i.e. no dynamic memory allocation ever takes place. Thus, an optional object models an object, not a pointer, even though operator*() and operator-&gt;() are defined. 
When an object of type optional&lt;T&gt; is contextually_converted_to_bool, the conversion returns true if the object contains a value and false if it does not contain a value. 
The optional object contains a value in the following conditions: 
* The object is initialized with/assigned from a value of type T or another optional that contains a value. 
The object does not contain a value in the following conditions: 
* The object is default-initialized. 
* The object is initialized with/assigned from a value of type std::nullopt_t or an optional object that does not contain a value. 
* The member function reset() is called. 
There are no optional references; a program is ill-formed if it instantiates an optional with a reference type. Alternatively, an optional of a std::reference_wrapper of type T may be used to hold a reference. In addition, a program is ill-formed if it instantiates an optional with the tag types std::nullopt_t or std::in_place_t. 

<h2>Template parameters</h2>

T - the type of the value to manage initialization state for. The type must meet the requirements of Destructible

<h2>Member types</h2>

Member type Definition 
value_type T

<h2>Member functions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs the optional object 
constructor <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;destroys the contained value, if there is one 
destructor <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;assigns contents 
operator= <i>(public member function)</i>

<h2>Observers</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;accesses the contained value 
operator-&gt; <i>(public member function)</i> 
operator* 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks whether the object contains a value 
operator_bool <i>(public member function)</i> 
has_value 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the contained value 
value <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the contained value if available, another value otherwise 
value_or <i>(public member function)</i>

<h2>Modifiers</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exchanges the contents 
swap <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;destroys any contained value 
reset <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs the contained value in-place 
emplace <i>(public member function)</i>

<h2>Non-member functions</h2>

operator== 
operator!= 
operator&lt; compares optional objects 
operator&lt;= <i>(function template)</i> 
operator&gt; 
operator&gt;= 

 
<i>(C++17)</i> 

 
make_optional creates an optional object 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++17)</i> 

 
std::swap(std::optional) specializes the std::swap algorithm 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++17)</i>

<h2>Helper classes</h2>

std::hash&lt;std::optional&gt; specializes the std::hash algorithm 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template specialization)</i> 
<i>(C++17)</i> 

 
nullopt_t indicator of optional type with uninitialized state 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class)</i> 
<i>(C++17)</i> 

 
bad_optional_access exception indicating checked access to an optional that doesn't contain a value 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class)</i> 
<i>(C++17)</i> 

 

 
Helpers 

 

 

 
nullopt an object of type nullopt_t 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(constant) 
<i>(C++17)</i> 

 
in_place_ 
in_place_type_ 
in_place_index_ in-place construction tag 
in_place_t_ <i>(class template)</i> 
in_place_type_t_ 
in_place_index_t 

 
<i>(C++17)</i> 

 

 
Deduction_guides

<h2>Example</h2>

// Run this code <pre><code>#include &lt;string&gt;

#include &lt;functional&gt;

#include &lt;iostream&gt;

#include &lt;optional&gt;
// optional can be used as the return type of a factory that may fail

std::optional&lt;std::string&gt; create(bool b)
{
    if (b)
        return &quot;Godzilla&quot;;
    return {};
}
// std::nullopt can be used to create any (empty) std::optional

auto create2(bool b)
{
    return b ? std::optional&lt;std::string&gt;{&quot;Godzilla&quot;} : std::nullopt;
}
// std::reference_wrapper may be used to return a reference

auto create_ref(bool b)
{
    static std::string value = &quot;Godzilla&quot;;
    return b ? std::optional&lt;std::reference_wrapper&lt;std::string&gt;&gt;{value}
             : std::nullopt;
}
int main()

{
    std::cout &lt;&lt; &quot;create(false) returned &quot;
              &lt;&lt; create(false).value_or(&quot;empty&quot;) &lt;&lt; '\n';
    // optional-returning factory functions are usable as conditions of while and if
    if (auto str = create2(true)) {
        std::cout &lt;&lt; &quot;create2(true) returned &quot; &lt;&lt; *str &lt;&lt; '\n';
    }
    if (auto str = create_ref(true)) {
        // using get() to access the reference_wrapper's value
        std::cout &lt;&lt; &quot;create_ref(true) returned &quot; &lt;&lt; str-&gt;get() &lt;&lt; '\n';
        str-&gt;get() = &quot;Mothra&quot;;
        std::cout &lt;&lt; &quot;modifying it changed it to &quot; &lt;&lt; str-&gt;get() &lt;&lt; '\n';
    }
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;create(false) returned empty 
&nbsp;<wbr>&nbsp;create2(true) returned Godzilla 
&nbsp;<wbr>&nbsp;create_ref(true) returned Godzilla 
&nbsp;<wbr>&nbsp;modifying it changed it to Mothra

<h2>See also</h2>

variant a type-safe discriminated union 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++17)</i> 
any Objects that hold instances of any CopyConstructible type. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class)</i> 
<i>(C++17)</i> 
