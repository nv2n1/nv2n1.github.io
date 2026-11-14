---
title: "stdtype_infooperatorstdtype_infooperator(3)"
name: "stdtype_infooperatorstdtype_infooperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdtype_infooperatorstdtype_infooperator/"
---

std::type_info::operator==,std::type_info::operator!= - std::type_info::operator==,std::type_info::operator!=

<h2>Synopsis</h2>

<pre><code>bool operator==(const type_info &amp;rhs) const;

bool operator!=(const type_info &amp;rhs) const;</code></pre> 
Checks if the objects refer to the same types. 

<h2>Parameters</h2>

rhs - another type information object to compare to

<h2>Return value</h2>

true if the comparison operation holds true, false otherwise 

<h2>Example</h2>

// Run this code employee(std::string &amp;&amp;n, std::string &amp;&amp;p)
    : person(std::move(n)), _profession(std::move(p))
{
}
const std::string &amp;profession() const
{
    return _profession;
} 
&nbsp;<wbr>&nbsp;class person 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;public: std::string _profession;
}
;
void somefunc(const person &amp;p)

{
    if (typeid(employee) == typeid(p)) {
        std::cout &lt;&lt; p.name() &lt;&lt; &quot; is an employee &quot;;
        auto &amp;emp = dynamic_cast&lt;const employee &amp;&gt;(p);
        std::cout &lt;&lt; &quot;who works in &quot; &lt;&lt; emp.profession() &lt;&lt; '\n';
    }
}
int main()

{
    employee paul(&quot;Paul&quot;, &quot;Economics&quot;);
    somefunc(paul);
}
 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;private: std::string _name;

}; 
&nbsp;<wbr>&nbsp;class employee : public person 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;public: employee(std::string &amp;&amp;n, std::string &amp;&amp;p)
    : person(std::move(n)), _profession(std::move(p))
{
}
const std::string &amp;profession() const
{
    return _profession;
} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;private: <pre><code>std::string _profession;
}
;
void somefunc(const person &amp;p)

{
    if (typeid(employee) == typeid(p)) {
        std::cout &lt;&lt; p.name() &lt;&lt; &quot; is an employee &quot;;
        auto &amp;emp = dynamic_cast&lt;const employee &amp;&gt;(p);
        std::cout &lt;&lt; &quot;who works in &quot; &lt;&lt; emp.profession() &lt;&lt; '\n';
    }
}
int main()

{
    employee paul(&quot;Paul&quot;, &quot;Economics&quot;);
    somefunc(paul);
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Paul is an employee who works in Economics

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks whether the referred type precedes referred type of another type_index 
before object in the implementation defined order, i.e. orders the referred types 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function)</i> 
