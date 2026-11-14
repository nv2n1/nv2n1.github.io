---
title: "stdnumpuncttruenamedo_truenamefalsenamedo_falsename(3)"
name: "stdnumpuncttruenamedo_truenamefalsenamedo_falsename"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdnumpuncttruenamedo_truenamefalsenamedo_falsename/"
---

std::numpunct&lt;CharT&gt;::truename,do_truename,falsename,do_falsename - std::numpunct&lt;CharT&gt;::truename,do_truename,falsename,do_falsename

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;locale&gt;

    public : (1)

                 string_type truename() const;

public:
(2)

    string_type falsename() const;

protected:
(3)

    virtual string_type do_truename() const;

protected:
(4)

    virtual string_type do_falsename() const;</code></pre> 
1-2) Public member function, calls the member function do_truename and do_falsename of the most derived class respectively. 
3) Returns the string to be used as the representation of the boolean value true. 
4) Returns the string to be used as the representation of the boolean value false. 

<h2>Return value</h2>

1,3) The object of type string_type to use as the representation of true. The standard specializations of std::numpunct return &quot;true&quot; and L&quot;true&quot;.

2,4) The object of type string_type to use as the representation of false. The standard specializations of std::numpunct return &quot;false&quot; and L&quot;false&quot;.


<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;locale&gt;

#include &lt;iomanip&gt;
struct custom_tf : std::numpunct&lt;char&gt; {
    std::string do_truename() const
    {
        return &quot;t&quot;;
    }
    std::string do_falsename() const
    {
        return &quot;f&quot;;
    }
};
int main()

{
    std::cout &lt;&lt; std::boolalpha;
    std::cout &lt;&lt; &quot;default locale: &quot; &lt;&lt; true &lt;&lt; true &lt;&lt; false &lt;&lt; false &lt;&lt; '\n';
    std::cout.imbue(std::locale(std::cout.getloc(), new custom_tf));
    std::cout &lt;&lt; &quot;locale with modified numpunct: &quot;
              &lt;&lt; true &lt;&lt; true &lt;&lt; false &lt;&lt; false &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;default locale: truetruefalsefalse 
&nbsp;<wbr>&nbsp;locale with modified numpunct: ttff
