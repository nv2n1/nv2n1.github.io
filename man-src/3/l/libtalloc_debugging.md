---
title: "libtalloc_debugging(3)"
name: "libtalloc_debugging"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libtalloc_debugging/"
description: "libtalloc_debugging – Chapter 6: Debugging Although talloc makes memory management significantly easier than the C standard library, developers are still only humans and can make mistakes."
---

<h2 class="name">NAME</h2>
<p> libtalloc_debugging &#8211; Chapter 6: Debugging Although talloc makes memory management significantly easier than the C standard library, developers are still only humans and can make mistakes. </p>
<p> Therefore, it can be handy to know some tools for the inspection of talloc memory usage. </p>
<h2>Talloc log and abort</h2>
<p> We have already encountered the abort function in section <code>Dynamic type system</code>. In that case it was used when a type mismatch was detected. However, talloc calls this abort function in several more situations: </p>
<dl>
<dt>&bull;</p>
<dd> when the provided pointer is not a valid talloc context,</p>
<dt>&bull;</p>
<dd> when the meta data is invalid &#8211; probably due to memory corruption,</p>
<dt>&bull;</p>
<dd> and when an access after free is detected.</dl>
<p> The third one is probably the most interesting. It can help us with detecting an attempt to double-free a context or any other manipulation with it via talloc functions (using it as a parent, stealing it, etc.). </p>
<p> Before the context is freed talloc sets a flag in the meta data. This is then used to detect the access after free. It basically works on the assumption that the memory stays unchanged (at least for a while) even when it is properly deallocated. This will work even if the memory is filled with the value specified in TALLOC_FREE_FILL environment variable, because it fills only the data part and leaves the meta data intact. </p>
<p> Apart from the abort function, talloc uses a log function to provide additional information to the aforementioned violations. To enable logging we shall set the log function with one of: </p>
<dl>
<dt>&bull;</p>
<dd> <code>talloc_set_log_fn()</code></p>
<dt>&bull;</p>
<dd> <code>talloc_set_log_stderr()</code></dl>
<p> The following code is a sample output of accessing a context after it has been freed: </p>
<pre><code>
talloc_set_log_stderr();
TALLOC_CTX *ctx = talloc_new(NULL);
talloc_free(ctx);
talloc_free(ctx);
results in : talloc : access after free error - first free may be at../ src / main.c : 55 Bad talloc magic value - access after free
</code></pre>
<p> Another example is an invalid context: </p>
<p>talloc_set_log_stderr();<br />
TALLOC_CTX *ctx = talloc_new(NULL);<br />
char *str = strdup(&#8220;not a talloc context&#8221;);<br />
talloc_steal(ctx, str);<br />
results in : Bad talloc magic value &#8211; unknown value</p>
<h2>Memory usage reports</h2>
<p> Talloc can print reports of memory usage of a specified talloc context to a file (to stdout or stderr). The report can be simple or full. The simple report provides information only about the context itself and its direct descendants. The full report goes recursively through the entire context tree. See: </p>
<dl>
<dt>&bull;</p>
<dd> <code>talloc_report()</code></p>
<dt>&bull;</p>
<dd> <code>talloc_report_full()</code></dl>
<p> We will use the following code to retrieve the sample report: </p>
<pre><code>
struct foo {
    char *str;
};
TALLOC_CTX *ctx = talloc_new(NULL);
char *str = talloc_strdup(ctx, "my string");
struct foo *foo = talloc_zero(ctx, struct foo);
foo-&gt;str = talloc_strdup(foo, "I am Foo");
char *str2 = talloc_strdup(foo, "Foo is my parent");
/* print full report */
talloc_report_full(ctx, stdout);
</code></pre>
<p> It will print a full report of ctx to the standard output. The message should be similar to: </p>
<pre>
full talloc report on 'talloc_new: ../src/main.c:82' (total 46 bytes in 5 blocks)
  struct foo contains 34 bytes in 3 blocks (ref 0) 0x1495130
    Foo is my parent contains 17 bytes in 1 blocks (ref 0) 0x1495200
    I am Foo contains 9 bytes in 1 blocks (ref 0) 0x1495190
  my string contains 10 bytes in 1 blocks (ref 0) 0x14950c0
</pre>
<p> We can notice in this report that something is wrong with the context containing struct foo. We know that the structure has only one string element. However, we can see in the report that it has two children. This indicates that we have either violated the memory hierarchy or forgotten to free it as temporary data. Looking into the code, we can see that &#8216;Foo is my parent&#8217; should be attached to ctx. </p>
<p> See also: </p>
<dl>
<dt>&bull;</p>
<dd> <code>talloc_enable_null_tracking()</code></p>
<dt>&bull;</p>
<dd> <code>talloc_disable_null_tracking()</code></p>
<dt>&bull;</p>
<dd> <code>talloc_enable_leak_report()</code></p>
<dt>&bull;</p>
<dd> <code>talloc_enable_leak_report_full()</code></dl>
<h2>Index</h2>
