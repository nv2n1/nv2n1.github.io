---
title: "libtalloc_bestpractices(3)"
name: "libtalloc_bestpractices"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libtalloc_bestpractices/"
description: "libtalloc_bestpractices – Chapter 7: Best practises The following sections contain several best practices and good manners that were found by the Samba and SSSD developers over the years."
---

<h2 class="name">NAME</h2>
<p> libtalloc_bestpractices &#8211; Chapter 7: Best practises The following sections contain several best practices and good manners that were found by the Samba and SSSD developers over the years. </p>
<p> These will help you to write code which is better, easier to debug and with as few (hopefully none) memory leaks as possible. </p>
<h2>Keep the context hierarchy steady</h2>
<p> The talloc is a hierarchy memory allocator. The hierarchy nature is what makes the programming more error proof. It makes the memory easier to manage and to free. Therefore, the first thing we should have on our mind is: always project your data structures into the talloc context hierarchy. </p>
<p> That means if we have a structure, we should always use it as a parent context for its elements. This way we will not encounter any troubles when freeing the structure or when changing its parent. The same rule applies for arrays. </p>
<p> For example, the structure user from section <code>Hierarchy of talloc context</code> should be created with the context hierarchy illustrated on the next image. </p>
<h2>Every function should use its own context</h2>
<p> It is a good practice to create a temporary talloc context at the function beginning and free the context just before the return statement. All the data must be allocated on this context or on its children. This ensures that no memory leaks are created as long as we do not forget to free the temporary context. </p>
<p> This pattern applies to both situations &#8211; when a function does not return any dynamically allocated value and when it does. However, it needs a little extension for the latter case.</p>
<h3>Functions that do not return any dynamically allocated</h3>
<p> value </p>
<p> If the function does not return any value created on the heap, we will just obey the aforementioned pattern. </p>
<pre><code>
int bar()
{
    int ret;
    TALLOC_CTX *tmp_ctx = talloc_new(NULL);
    if (tmp_ctx == NULL) {
        ret = ENOMEM;
        goto done;
    }
    /* allocate data on tmp_ctx or on its descendants */
    ret = EOK;
done:
    talloc_free(tmp_ctx);
    return ret;
}
</code></pre>
<h3>Functions returning dynamically allocated values</h3>
<p> If our function returns any dynamically allocated data, its first parameter should always be the destination talloc context. This context serves as a parent for the output values. But again, we will create the output values as the descendants of the temporary context. If everything goes well, we will change the parent of the output values from the temporary to the destination talloc context. </p>
<p> This pattern ensures that if an error occurs (e.g. I/O error or insufficient amount of the memory), all allocated data is freed and no garbage appears on the destination context. </p>
<p>int struct_foo_init(TALLOC_CTX *mem_ctx, struct foo **_foo)<br />
{<br />
    int ret;<br />
    struct foo *foo = NULL;<br />
    TALLOC_CTX *tmp_ctx = talloc_new(NULL);<br />
    if (tmp_ctx == NULL) {<br />
        ret = ENOMEM;<br />
        goto done;<br />
    }<br />
    foo = talloc_zero(tmp_ctx, struct foo);<br />
    /* &#8230; */<br />
    *_foo = talloc_steal(mem_ctx, foo);<br />
    ret = EOK;<br />
done:<br />
    talloc_free(tmp_ctx);<br />
    return ret;<br />
}</p>
<h2>Allocate temporary contexts on NULL</h2>
<p> As it can be seen on the previous listing, instead of allocating the temporary context directly on mem_ctx, we created a new top level context using NULL as the parameter for <code>talloc_new()</code> function. Take a look at the following example: </p>
<p>char *create_user_filter(TALLOC_CTX *mem_ctx,<br />
                         uid_t uid, const char *username)<br />
{<br />
    char *filter = NULL;<br />
    char *sanitized_username = NULL;<br />
    /* tmp_ctx is a child of mem_ctx */<br />
    TALLOC_CTX *tmp_ctx = talloc_new(mem_ctx);<br />
    if (tmp_ctx == NULL) {<br />
        return NULL;<br />
    }<br />
    sanitized_username = sanitize_string(tmp_ctx, username);<br />
    if (sanitized_username == NULL) {<br />
        talloc_free(tmp_ctx);<br />
        return NULL;<br />
    }<br />
    filter = talloc_aprintf(tmp_ctx, &#8220;(|(uid=%llu)(uname=%s))&#8221;,<br />
                            uid, sanitized_username);<br />
    if (filter == NULL) {<br />
        return NULL; /* tmp_ctx is not freed */ (*@k<br />
    }@*)<br />
}<br />
/* filter becomes a child of mem_ctx */<br />
filter = talloc_steal(mem_ctx, filter);<br />
talloc_free(tmp_ctx);<br />
return filter;<br />
}</p>
<p> We forgot to free tmp_ctx before the return statement in the filter == NULL condition. However, it is created as a child of mem_ctx context and as such it will be freed as soon as the mem_ctx is freed. Therefore, no detectable memory leak is created. </p>
<p> On the other hand, we do not have any way to access the allocated data and for all we know mem_ctx may exist for the lifetime of our application. For these reasons this should be considered as a memory leak. How can we detect if it is unreferenced but still attached to its parent context? The only way is to notice the mistake in the source code. </p>
<p> But if we create the temporary context as a top level context, it will not be freed and memory diagnostic tools (e.g. valgrind) are able to do their job.</p>
<h2>Temporary contexts and the talloc pool</h2>
<p> If we want to take the advantage of the talloc pool but also keep to the pattern introduced in the previous section, we are unable to do it directly. The best thing to do is to create a conditional build where we can decide how do we want to create the temporary context. For example, we can create the following macros: </p>
<p>#ifdef USE_POOL_CONTEXT<br />
#define CREATE_POOL_CTX(ctx, size) talloc_pool(ctx, size)<br />
#define CREATE_TMP_CTX(ctx) talloc_new(ctx)<br />
#else<br />
#define CREATE_POOL_CTX(ctx, size) talloc_new(ctx)<br />
#define CREATE_TMP_CTX(ctx) talloc_new(NULL)<br />
#endif</p>
<p> Now if our application is under development, we will build it with macro USE_POOL_CONTEXT undefined. This way, we can use memory diagnostic utilities to detect memory leaks. </p>
<p> The release version will be compiled with the macro defined. This will enable pool contexts and therefore reduce the malloc() calls, which will end up in a little bit faster processing. </p>
<pre><code>
int struct_foo_init(TALLOC_CTX *mem_ctx, struct foo **_foo)
{
    int ret;
    struct foo *foo = NULL;
    TALLOC_CTX *tmp_ctx = CREATE_TMP_CTX(mem_ctx);
    /* ... */
}
errno_t handle_request(TALLOC_CTX mem_ctx)
{
    int ret;
    struct foo *foo = NULL;
    TALLOC_CTX *pool_ctx = CREATE_POOL_CTX(NULL, 1024);
    ret = struct_foo_init(mem_ctx, &amp;foo);
    /* ... */
}
</code></pre>
<p>&nbsp;<wbr> </p>
<h2>Index</h2>
