---
title: "stdkill_dependency(3)"
name: "stdkill_dependency"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdkill_dependency/"
---

std::kill_dependency - std::kill_dependency

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;atomic&gt;

template&lt; class T &gt;                 (since C++11)

T kill_dependency( T y ) noexcept;</code></pre> 
Informs the compiler that the dependency tree started by an std::memory_order_consume atomic load operation does not extend past the return value of std::kill_dependency; that is, the argument does not carry a dependency into the return value. 
This may be used to avoid unnecessary std::memory_order_acquire fences when the dependency chain leaves function scope (and the function does not have the [[carries_dependency]] attribute) 

<h2>Parameters</h2>

y - the expression whose return value is to be removed from a dependency tree

<h2>Return value</h2>

Returns y, no longer a part of a dependency tree. 

<h2>Examples</h2>

<pre><code>// file1.cpp

struct foo {
    int *a;
    int *b;
};

std::atomic&lt;struct foo *&gt; foo_head[10];

int foo_array[10][10];
// consume operation starts a dependency chain, which escapes this function

[[carries_dependency]] struct foo *f(int i)
{
    return foo_head[i].load(memory_order_consume);
}
// the dependency chain enters this function through the right parameter

// and is killed before the function ends (so no extra acquire operation takes place)

int g(int *x, int *y [[carries_dependency]])
{
    return std::kill_dependency(foo_array[*x][*y]);
}

// file2.cpp

[[carries_dependency]] struct foo *f(int i);

int g(int *x, int *y [[carries_dependency]]);
int c = 3;

void h(int i)
{
    struct foo *p;
    p = f(i);                       // dependency chain started inside f continues into p without undue acquire
    do_something_with(g(&amp;c, p-&gt;a)); // p-&gt;b is not brought in from the cache
    do_something_with(g(p-&gt;a, &amp;c)); // left argument does not have the carries_dependency
                                    // attribute: memory acquire fence may be issued
                                    // p-&gt;b becomes visible before g() is entered
}
</code></pre>

<h2>See also</h2>

memory_order defines memory ordering constraints for the given atomic operation 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(enum)</i> 
<i>(C++11)</i> 
