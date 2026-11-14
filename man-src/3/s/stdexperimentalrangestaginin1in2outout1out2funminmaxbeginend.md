---
title: "stdexperimentalrangestaginin1in2outout1out2funminmaxbeginend(3)"
name: "stdexperimentalrangestaginin1in2outout1out2funminmaxbeginend"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangestaginin1in2outout1out2funminmaxbeginend/"
---

std::experimental::ranges::tag::in,in1,in2,out,out1,out2,fun,min,max,begin,end - std::experimental::ranges::tag::in,in1,in2,out,out1,out2,fun,min,max,begin,end

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;experimental / ranges / algorithm&gt;

    struct in { /* implementation-defined */
};

struct in1 { /* implementation-defined */
};

struct in2 { /* implementation-defined */
};

struct out { /* implementation-defined */
};

struct out1 { /* implementation-defined */
};

struct out2 { /* implementation-defined */
};
(ranges TS)

    struct fun { /* implementation-defined */
};

struct min { /* implementation-defined */
};

struct max { /* implementation-defined */
};

struct begin { /* implementation-defined */
};

struct end { /* implementation-defined */
};</code></pre> 
These classes are TagSpecifiers for use with ranges::tagged. 
The name of a specifier is also the element name it corresponds to. For instance, ranges::tagged&lt;std::pair&lt;int, int&gt;, tag::min, tag::max&gt; provides a set of named accessors named min and a set of named accessors named max. 
