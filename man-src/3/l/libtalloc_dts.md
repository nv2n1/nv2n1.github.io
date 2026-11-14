---
title: "libtalloc_dts(3)"
name: "libtalloc_dts"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libtalloc_dts/"
description: "libtalloc_dts – Chapter 3: Dynamic type system"
---

<h2 class="name">NAME</h2>
<p> libtalloc_dts &#8211; Chapter 3: Dynamic type system</p>
<h2>Dynamic type system</h2>
<p> Generic programming in the C language is very difficult. There is no inheritance nor templates known from object oriented languages. There is no dynamic type system. Therefore, generic programming in this language is usually done by type-casting a variable to void* and transferring it through a generic function to a specialized callback as illustrated on the next listing. </p>
<pre><code>
void generic_function(callback_fn cb, void *pvt)
{
    /* do some stuff and call the callback */
    cb(pvt);
}
void specific_callback(void *pvt)
{
    struct specific_struct *data;
    data = (struct specific_struct *)pvt;
    /* ... */
}
void specific_function()
{
    struct specific_struct data;
    generic_function(callback, &amp;data);
}
</code></pre>
<p> Unfortunately, the type information is lost as a result of this type cast. The compiler cannot check the type during the compilation nor are we able to do it at runtime. Providing an invalid data type to the callback will result in unexpected behaviour (not necessarily a crash) of the application. This mistake is usually hard to detect because it is not the first thing which comes the mind. </p>
<p> As we already know, every talloc context contains a name. This name is available at any time and it can be used to determine the type of a context even if we lose the type of a variable. </p>
<p> Although the name of the context can be set to any arbitrary string, the best way of using it to simulate the dynamic type system is to set it directly to the type of the variable. </p>
<p> It is recommended to use one of <code>talloc()</code> and <code>talloc_array()</code> (or its variants) to create the context as they set its name to the name of the given type automatically. </p>
<p> If we have a context with such as a name, we can use two similar functions that do both the type check and the type cast for us: </p>
<dl>
<dt>&bull;</p>
<dd> <code>talloc_get_type()</code></p>
<dt>&bull;</p>
<dd> <code>talloc_get_type_abort()</code></dl>
<h2>Examples</h2>
<p> The following example will show how generic programming with talloc is handled &#8211; if we provide invalid data to the callback, the program will be aborted. This is a sufficient reaction for such an error in most applications. </p>
<p>void foo_callback(void *pvt)<br />
{<br />
    struct foo *data = talloc_get_type_abort(pvt, struct foo);<br />
    /* &#8230; */<br />
}<br />
int do_foo()<br />
{<br />
    struct foo *data = talloc_zero(NULL, struct foo);<br />
    /* &#8230; */<br />
    return generic_function(foo_callback, data);<br />
}</p>
<p> But what if we are creating a service application that should be running for the uptime of a server, we may want to abort the application during the development process (to make sure the error is not overlooked) and try to recover from the error in the customer release. This can be achieved by creating a custom abort function with a conditional build. </p>
<p>void my_abort(const char *reason)<br />
{<br />
  fprintf(stderr, &#8220;talloc abort: %s, reason);<br />
#ifdef ABORT_ON_TYPE_MISMATCH<br />
  abort();<br />
#endif<br />
}</p>
<p> The usage of <code>talloc_get_type_abort()</code> would be then: </p>
<pre><code>
talloc_set_abort_fn(my_abort);
TALLOC_CTX *ctx = talloc_new(NULL);
char *str = talloc_get_type_abort(ctx, char);
if (str == NULL) {
    /* recovery code */
}
/* talloc abort: ../src/main.c:25: Type mismatch:
   name[talloc_new: ../src/main.c:24] expected[char] */
</code></pre>
<p>&nbsp;<wbr> </p>
<h2>Index</h2>
