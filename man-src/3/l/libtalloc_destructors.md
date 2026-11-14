---
title: "libtalloc_destructors(3)"
name: "libtalloc_destructors"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libtalloc_destructors/"
description: "libtalloc_destructors – Chapter 4: Using destructors"
---

<h2 class="name">NAME</h2>
<p> libtalloc_destructors &#8211; Chapter 4: Using destructors</p>
<h2>Using destructors</h2>
<p> Destructors are well known methods in the world of object oriented programming. A destructor is a method of an object that is automatically run when the object is destroyed. It is usually used to return resources taken by the object back to the system (e.g. closing file descriptors, terminating connection to a database, deallocating memory). </p>
<p> With talloc we can take the advantage of destructors even in C. We can easily attach our own destructor to a talloc context. When the context is freed, the destructor will run automatically. </p>
<p> To attach/detach a destructor to a talloc context use: <code>talloc_set_destructor()</code>.</p>
<h2>Example</h2>
<p> Imagine that we have a dynamically created linked list. Before we deallocate an element of the list, we need to make sure that we have successfully removed it from the list. Normally, this would be done by two commands in the exact order: remove it from the list and then free the element. With talloc, we can do this at once by setting a destructor on the element which will remove it from the list and <code>talloc_free()</code> will do the rest. </p>
<p> The destructor would be: </p>
<pre><code>
int list_remove(void *ctx)
{
    struct list_el *el = NULL;
    el = talloc_get_type_abort(ctx, struct list_el);
    /* remove element from the list */
}
</code></pre>
<p> GCC version 3 and newer can check for the types during the compilation. So if it is our major compiler, we can use a more advanced destructor: </p>
<p>int list_remove(struct list_el *el)<br />
{<br />
    /* remove element from the list */<br />
}</p>
<p> Now we will assign the destructor to the list element. We can do this directly in the function that inserts it. </p>
<p>struct list_el *list_insert(TALLOC_CTX *mem_ctx,<br />
                            struct list_el *where,<br />
                            void *ptr)<br />
{<br />
    struct list_el *el = talloc(mem_ctx, struct list_el);<br />
    el-&gt;data = ptr;<br />
    /* insert into list */<br />
    talloc_set_destructor(el, list_remove);<br />
    return el;<br />
}</p>
<p> Because talloc is a hierarchical memory allocator, we can go a step further and free the data with the element as well: </p>
<pre><code>
struct list_el *list_insert_free(TALLOC_CTX *mem_ctx,
                                 struct list_el *where,
                                 void *ptr)
{
    struct list_el *el = NULL;
    el = list_insert(mem_ctx, where, ptr);
    talloc_steal(el, ptr);
    return el;
}
</code></pre>
<p>&nbsp;<wbr> </p>
<h2>Index</h2>
