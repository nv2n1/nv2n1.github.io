---
title: "libtalloc_context(3)"
name: "libtalloc_context"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libtalloc_context/"
description: "libtalloc_context – Chapter 1: Talloc context"
---

<h2 class="name">NAME</h2>
<p> libtalloc_context &#8211; Chapter 1: Talloc context</p>
<h2>Talloc context</h2>
<p> The talloc context is the most important part of this library and is responsible for every single feature of this memory allocator. It is a logical unit which represents a memory space managed by talloc. </p>
<p> From the programmer&#8217;s point of view, the talloc context is completely equivalent to a pointer that would be returned by the memory routines from the C standard library. This means that every context that is returned from the talloc library can be used directly in functions that do not use talloc internally. For example we can do the following: </p>
<pre><code>
char *str1 = strdup("I am NOT a talloc context");
char *str2 = talloc_strdup(NULL, "I AM a talloc context");
printf("%d, strcmp(str1, str2) == 0);
free(str1);
talloc_free(str2); /* we can not use free() on str2 */
</code></pre>
<p> This is possible because the context is internally handled as a special fixed-length structure called talloc chunk. Each chunk stores context metadata followed by the memory space requested by the programmer. When a talloc function returns a context (pointer), it will in fact return a pointer to the user space portion of the talloc chunk. If we to manipulate this context using talloc functions, the talloc library transforms the user-space pointer back to the starting address of the chunk. This is also the reason why we were unable to use free(str2) in the previous example &#8211; because str2 does not point at the beginning of the allocated block of memory. This is illustrated on the next image: </p>
<p> The type TALLOC_CTX is defined in <code>talloc.h</code> to identify a talloc context in function parameters. However, this type is just an alias for void and exists only for semantical reasons &#8211; thus we can differentiate between void * (arbitrary data) and TALLOC_CTX * (talloc context).</p>
<h3>Context meta data</h3>
<p> Every talloc context carries several pieces of internal information along with the allocated memory: </p>
<dl>
<dt>&bull;</p>
<dd> name &#8211; which is used in reports of context hierarchy and to simulate a dynamic type system,</p>
<dt>&bull;</p>
<dd> size of the requested memory in bytes &#8211; this can be used to determine the number of elements in arrays,</p>
<dt>&bull;</p>
<dd> attached destructor &#8211; which is executed just before the memory block is about to be freed,</p>
<dt>&bull;</p>
<dd> references to the context</p>
<dt>&bull;</p>
<dd> children and parent contexts &#8211; create the hierarchical view on the memory.</dl>
<h2>Hierarchy of talloc context</h2>
<p> Every talloc context contains information about its parent and children. Talloc uses this information to create a hierarchical model of memory or to be more precise, it creates an n-ary tree where each node represents a single talloc context. The root node of the tree is referred to as a top level context &#8211; a context without any parent. </p>
<p> This approach has several advantages: </p>
<dl>
<dt>&bull;</p>
<dd> as a consequence of freeing a talloc context, all of its children will be properly deallocated as well,</p>
<dt>&bull;</p>
<dd> the parent of a context can be changed at any time, which results in moving the whole subtree under another node,</p>
<dt>&bull;</p>
<dd> it creates a more natural way of managing data structures.</dl>
<h3>Example</h3>
<p> We have a structure that stores basic information about a user &#8211; his/her name, identification number and groups he/she is a member of: </p>
<p>struct user {<br />
    uid_t uid;<br />
    char *username;<br />
    size_t num_groups;<br />
    char **groups;<br />
};</p>
<p> We will allocate this structure using talloc. The result will be the following context tree: </p>
<p>/* create new top level context */<br />
struct user *user = talloc(NULL, struct user);<br />
user-&gt;uid = 1000;<br />
user-&gt;num_groups = N;<br />
/* make user the parent of following contexts */<br />
user-&gt;username = talloc_strdup(user, &#8220;Test user&#8221;);<br />
user-&gt;groups = talloc_array(user, char *, user-&gt;num_groups);<br />
for (i = 0; i &lt; user-&gt;num_groups; i++) {<br />
    /* make user-&gt;groups the parent of following context */<br />
    user-&gt;groups[i] = talloc_asprintf(user-&gt;groups,<br />
                                      &#8220;Test group %d&#8221;, i);<br />
}</p>
<p> This way, we have gained a lot of additional capabilities, one of which is very simple deallocation of the structure and all of its elements. </p>
<p> With the C standard library we need first to iterate over the array of groups and free every element separately. Then we must deallocate the array that stores them. Next we deallocate the username and as the last step free the structure itself. But with talloc, the only operation we need to execute is freeing the structure context. Its descendants will be freed automatically. </p>
<pre>
talloc_free(user);
</pre>
<h2>Always keep the hieararchy steady!</h2>
<p> The talloc is a hierarchy memory allocator. The hierarchy nature is what makes the programming more error proof. It makes the memory easier to manage and to free. Therefore, the first thing we should have on our mind is: <code>always project our data structures into the talloc context hierarchy</code>. </p>
<p> That means if we have a structure, we should always use it as a parent context for its elements. This way we will not encounter any troubles when freeing this structure or when changing its parent. The same rule applies for arrays.</p>
<h2>Creating a talloc context</h2>
<p> Here are the most important functions that create a new talloc context.</p>
<h3>Type-safe functions</h3>
<p> It allocates the size that is necessary for the given type and returns a new, properly-casted pointer. This is the preferred way to create a new context as we can rely on the compiler to detect type mismatches. </p>
<p> The name of the context is automatically set to the name of the data type which is used to simulate a dynamic type system. </p>
<p>struct user *user = talloc(ctx, struct user);<br />
/* initialize to default values */<br />
user-&gt;uid = 0;<br />
user-&gt;name = NULL;<br />
user-&gt;num_groups = 0;<br />
user-&gt;groups = NULL;<br />
/* or we can achieve the same result with */<br />
struct user *user_zero = talloc_zero(ctx, struct user);</p>
<h3>Zero-length contexts</h3>
<p> The zero-length context is basically a context without any special semantical meaning. We can use it the same way as any other context. The only difference is that it consists only of the meta data about the context. Therefore, it is strictly of type TALLOC_CTX*. It is often used in cases where we want to aggregate several data structures under one parent (zero-length) context, such as a temporary context to contain memory needed within a single function that is not interesting to the caller. Allocating on a zero-length temporary context will make clean-up of the function simpler. </p>
<pre><code>
TALLOC_CTX *tmp_ctx = NULL;
struct foo *foo = NULL;
struct bar *bar = NULL;
/* new zero-length top level context */
tmp_ctx = talloc_new(NULL);
if (tmp_ctx == NULL) {
    return ENOMEM;
}
foo = talloc(tmp_ctx, struct foo);
bar = talloc(tmp_ctx, struct bar);
/* free everything at once */
talloc_free(tmp_ctx);
</code></pre>
<h3>See also</h3>
<dl>
<dt>&bull;</p>
<dd> <code>talloc_size()</code></p>
<dt>&bull;</p>
<dd> <code>talloc_named()</code></p>
<dt>&bull;</p>
<dd> <code>The talloc array functions</code></p>
<dt>&bull;</p>
<dd> <code>The talloc string functions.</code></dl>
<h2>Index</h2>
