---
title: "stdbind(3)"
name: "stdbind"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdbind/"
---

std::bind - std::bind

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;functional&gt;

template&lt; class F, class... Args &gt;             (1) (since C++11)

/*unspecified*/ bind( F&amp;&amp; f, Args&amp;&amp;... args );

template&lt; class R, class F, class... Args &gt;    (2) (since C++11)

/*unspecified*/ bind( F&amp;&amp; f, Args&amp;&amp;... args );</code></pre> 
The function template bind generates a forwarding call wrapper for f. Calling this wrapper is equivalent to invoking f with some of its arguments bound to args. 

<h2>Parameters</h2>

f - Callable object <i>(function object, pointer to function, reference to function, pointer to member function, or pointer to data member) that will be bound to s</i>ome arguments 
args - list of arguments to bind, with the unbound arguments replaced by the placeholders _1, _2, _3... of namespace std::placeholders

<h2>Return value</h2>

A function object of unspecified type T, for which std::is_bind_expression&lt;T&gt;::value == true. It has the following members: std::bind return type



<h2>Member objects</h2>

The return type of std::bind holds a member object of type std::decay&lt;F&gt;::type constructed from std::forward&lt;F&gt;(f), and one object per each of args..., of type std::decay&lt;Arg_i&gt;::type, similarly constructed from std::forward&lt;Arg_i&gt;(arg_i). 

 
Constructors 

 
The return type of std::bind is CopyConstructible if all of its member objects (specified above) are CopyConstructible, and is MoveConstructible otherwise. The type defines the following members:

<h2>Member type result_type</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(until C++20)</i> 
1) (deprecated in C++17) If F is a pointer to function or a pointer to member function, result_type is the return type of F. If F is a class type with nested typedef result_type, then result_type is F::result_type. Otherwise no result_type is defined. 
2) (deprecated in C++17) result_type is exactly R.

<h2>Member function operator()</h2>

Given an object g obtained from an earlier call to bind, when it is invoked in a function call expression g(u1, u2, ... uM), an invocation of the stored object takes place, as if by std::invoke(fd, std::forward&lt;V1&gt;(v1), std::forward&lt;V2&gt;(v2), ..., std::forward&lt;VN&gt;(vN)), where fd is a value of type std::decay_t&lt;F&gt; the values and types of the bound arguments v1, v2, ..., vN are determined as specified below. 

 
* If the stored argument arg is of type std::reference_wrapper&lt;T&gt; (for example, std::ref or std::cref was used in the initial call to bind), then the argument vn in the std::invoke call above is arg.get() and the type Vn in the same call is T&amp;: the stored argument is passed by reference into the invoked function object. 
* If the stored argument arg is of type T for which std::is_bind_expression&lt;T&gt;::value == true (for example, another bind expression was passed directly into the initial call to bind), then bind performs function composition: instead of passing the function object that the bind subexpression would return, the subexpression is invoked eagerly, and its return value is passed to the outer invokable object. If the bind subexpression has any placeholder arguments, they are shared with the outer bind (picked out of u1, u2, ...). Specifically, the argument vn in the std::invoke call above is arg(std::forward&lt;Uj&gt;(uj)...) and the type Vn in the same call is std::result_of_t&lt;T cv &amp;(Uj&amp;&amp;...)&gt;&amp;&amp; (cv qualification is the same as that of g). 
* If the stored argument arg is of type T, for which std::is_placeholder&lt;T&gt;::value != 0 (meaning, a placeholder such as std::placeholders::_1, _2, _3, ... was used as the argument to the initial call to bind), then the argument indicated by the placeholder (u1 for _1, u2 for _2, etc) is passed to the invokable object: the argument vn in the std::invoke call above is std::forward&lt;Uj&gt;(uj) and the corresponding type Vn in the same call is Uj&amp;&amp;. 
* Otherwise, the ordinary stored argument arg is passed to the invokable object as lvalue argument: the argument vn in the std::invoke call above is simply arg and the corresponding type Vn is T cv &amp;, where cv is the same cv-qualification as that of g. 

 
If some of the arguments that are supplied in the call to g() are not matched by any placeholders stored in g, the unused arguments are evaluated and discarded. 
If g is volatile-qualified (i.e., its cv-qualifiers are either volatile or const volatile), the behavior is undefined.

<h2>Exceptions</h2>

Only throws if construction of std::decay&lt;F&gt;::type from std::forward&lt;F&gt;(f) throws, or any of the constructors for std::decay&lt;Arg_i&gt;::type from the corresponding std::forward&lt;Arg_i&gt;(arg_i) throws where Arg_i is the ith type and arg_i is the ith argument in Args... args.

<h2>Notes</h2>

As described in Callable, when invoking a pointer to non-static member function or pointer to non-static data member, the first argument has to be a reference or pointer (including, possibly, smart pointer such as std::shared_ptr and std::unique_ptr) to an object whose member will be accessed. 
The arguments to bind are copied or moved, and are never passed by reference unless wrapped in std::ref or std::cref. 
Duplicate placeholders in the same bind expression (multiple _1's for example) are allowed, but the results are only well defined if the corresponding argument (u1) is an lvalue or non-movable rvalue. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;random&gt;

#include &lt;iostream&gt;

#include &lt;memory&gt;

#include &lt;functional&gt;
void f(int n1, int n2, int n3, const int &amp;n4, int n5)

{
    std::cout &lt;&lt; n1 &lt;&lt; ' ' &lt;&lt; n2 &lt;&lt; ' ' &lt;&lt; n3 &lt;&lt; ' ' &lt;&lt; n4 &lt;&lt; ' ' &lt;&lt; n5 &lt;&lt; '\n';
}
int g(int n1)

{
    return n1;
}
struct Foo {
    void print_sum(int n1, int n2)
    {
        std::cout &lt;&lt; n1 + n2 &lt;&lt; '\n';
    }
    int data = 10;
};
int main()

{
    using namespace std::placeholders; // for _1, _2, _3...
                                       // demonstrates argument reordering and pass-by-reference
    int n = 7;
    // (_1 and _2 are from std::placeholders, and represent future
    // arguments that will be passed to f1)
    auto f1 = std::bind(f, _2, _1, 42, std::cref(n), n);
    n = 10;
    f1(1, 2, 1001); // 1 is bound by _1, 2 is bound by _2, 1001 is unused
                    // makes a call to f(2, 1, 42, n, 7)
                    // nested bind subexpressions share the placeholders
    auto f2 = std::bind(f, _3, std::bind(g, _3), _3, 4, 5);
    f2(10, 11, 12); // makes a call to f(12, g(12), 12, 4, 5);
                    // common use case: binding a RNG with a distribution
    std::default_random_engine e;
    std::uniform_int_distribution&lt;&gt; d(0, 10);
    auto rnd = std::bind(d, e); // a copy of e is stored in rnd
    for (int n = 0; n &lt; 10; ++n)
        std::cout &lt;&lt; rnd() &lt;&lt; ' ';
    std::cout &lt;&lt; '\n';
    // bind to a pointer to member function
    Foo foo;
    auto f3 = std::bind(&amp;Foo::print_sum, &amp;foo, 95, _1);
    f3(5);
    // bind to a pointer to data member
    auto f4 = std::bind(&amp;Foo::data, _1);
    std::cout &lt;&lt; f4(foo) &lt;&lt; '\n';
    // smart pointers can be used to call members of the referenced objects, too
    std::cout &lt;&lt; f4(std::make_shared&lt;Foo&gt;(foo)) &lt;&lt; '\n'
              &lt;&lt; f4(std::make_unique&lt;Foo&gt;(foo)) &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;2 1 42 10 7 
&nbsp;<wbr>&nbsp;12 12 12 4 5 
&nbsp;<wbr>&nbsp;1 5 0 2 0 8 2 2 10 8 
&nbsp;<wbr>&nbsp;100 
&nbsp;<wbr>&nbsp;10 
&nbsp;<wbr>&nbsp;10 
&nbsp;<wbr>&nbsp;10

<h2>See also</h2>

bind_front binds a variable number of arguments, in order, to a function object 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
(C++20) 
_1,__2,__3,__4,_... placeholders for the unbound arguments in a std::bind expression 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(constant) 
<i>(C++11)</i> 
mem_fn creates a function object out of a pointer to a member 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
