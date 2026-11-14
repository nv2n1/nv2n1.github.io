---
title: "stdplaceholders_1stdplaceholders_2-stdplaceholders_n(3)"
name: "stdplaceholders_1stdplaceholders_2-stdplaceholders_n"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdplaceholders_1stdplaceholders_2-stdplaceholders_n/"
---

std::placeholders::_1,std::placeholders::_2,...,std::placeholders::_N - std::placeholders::_1,std::placeholders::_2,...,std::placeholders::_N

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;functional&gt;

/*see below*/ _1;

/*see below*/ _2;

.

.

/*see below*/ _N;</code></pre> 
The std::placeholders namespace contains the placeholder objects [_1, . . . _N] where N is an implementation defined maximum number. 
When used as an argument in a std::bind expression, the placeholder objects are stored in the generated function object, and when that function object is invoked with unbound arguments, each placeholder _N is replaced by the corresponding Nth unbound argument. 
Each placeholder is declared as if by extern /*unspecified*/ _1; <i>(until C++17)</i> 
Implementations are encouraged to declare the placeholders as if by inline constexpr /*unspecified*/ _1;, although declaring them by extern /*unspecified*/ _1; is still allowed by the standard. <i>(since C++17)</i> 
The types of the placeholder objects are DefaultConstructible and CopyConstructible, their default copy/move constructors do not throw exceptions, and for any placeholder _N, the type std::is_placeholder&lt;decltype(_N)&gt; is defined and is derived from std::integral_constant&lt;int, N&gt;. 

<h2>Example</h2>

The following code shows the creation of function objects with a placeholder argument. 
 // Run this code <pre><code>#include &lt;functional&gt;

#include &lt;string&gt;

#include &lt;iostream&gt;
void goodbye(const std::string &amp;s)

{
    std::cout &lt;&lt; &quot;Goodbye &quot; &lt;&lt; s &lt;&lt; '\n';
}
class Object
{

  public:
    void hello(const std::string &amp;s)
    {
        std::cout &lt;&lt; &quot;Hello &quot; &lt;&lt; s &lt;&lt; '\n';
    }
};
int main()

{
    typedef std::function&lt;void(const std::string &amp;)&gt; ExampleFunction;
    Object instance;
    std::string str(&quot;World&quot;);
    ExampleFunction f = std::bind(&amp;Object::hello, &amp;instance,
                                  std::placeholders::_1);
    // equivalent to instance.hello(str)
    f(str);
    f = std::bind(&amp;goodbye, std::placeholders::_1);
    // equivalent to goodbye(str)
    f(str);
    return 0;
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Hello World 
&nbsp;<wbr>&nbsp;Goodbye World

<h2>See also</h2>

bind binds one or more arguments to a function object 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
is_placeholder indicates that an object is a standard placeholder or can be used as one 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;placeholder to skip an element when unpacking a tuple using tie 
ignore (constant) 
