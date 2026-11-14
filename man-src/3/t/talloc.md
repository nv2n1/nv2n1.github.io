---
title: "talloc(3)"
name: "talloc"
section: "3"
letter: "t"
url: "/docs/linux/man/3-talloc/"
description: "The talloc API – talloc is a hierarchical, reference counted memory pool system with destructors."
---

<p>The talloc API &#8211; talloc is a hierarchical, reference counted memory pool system with destructors.</p>
<h3>Modules</h3>
<p><code>The talloc reference function.</code><br />
 <i>This module contains the definitions around talloc references. </i><br />
 <code>The talloc array functions</code><br />
 <i>Talloc contains some handy helpers for handling Arrays conveniently. </i><br />
 <code>The talloc string functions.</code><br />
 <i>talloc string allocation and manipulation functions. </i><br />
 <code>The talloc debugging support functions</code><br />
 <i>To aid memory debugging, talloc contains routines to inspect the currently allocated memory hierarchy. </i></p>
<h3>Macros</h3>
<pre><code>#define TALLOC_FREE(ctx)      \
    do {                      \
        if (ctx != NULL) {    \
            talloc_free(ctx); \
            ctx = NULL;       \
        }                     \
    } while (0)

Free a talloc chunk and NULL out the pointer.

    Typedefs</code></pre>
<p> typedef void <code>TALLOC_CTX</code><br />
 <i>Define a talloc parent type. </i></p>
<h3>Functions</h3>
<p>void * <code>talloc</code> (const void *ctx,#type)<br />
 <i>Create a new talloc context. </i><br />
 void * <code>talloc_init</code> (const char *fmt,&#8230;)<br />
 <i>Create a new top level talloc context. </i><br />
 int <code>talloc_free</code> (void *ptr)<br />
 <i>Free a chunk of talloc memory. </i><br />
 void <code>talloc_free_children</code> (void *ptr)<br />
 <i>Free a talloc chunk&#8217;s children. </i><br />
 void <code>talloc_set_destructor</code> (const void *ptr, int(*destructor)(void *))<br />
 <i>Assign a destructor function to be called when a chunk is freed. </i><br />
 void * <code>talloc_steal</code> (const void *new_ctx, const void *ptr)<br />
 <i>Change a talloc chunk&#8217;s parent. </i><br />
 const char * <code>talloc_set_name</code> (const void *ptr, const char *fmt,&#8230;)<br />
 <i>Assign a name to a talloc chunk. </i><br />
 void * <code>talloc_move</code> (const void *new_ctx, void **pptr)<br />
 <i>Change a talloc chunk&#8217;s parent. </i><br />
 void <code>talloc_set_name_const</code> (const void *ptr, const char *name)<br />
 <i>Assign a name to a talloc chunk. </i><br />
 void * <code>talloc_named</code> (const void *context, size_t size, const char *fmt,&#8230;)<br />
 <i>Create a named talloc chunk. </i><br />
 void * <code>talloc_named_const</code> (const void *context, size_t size, const char *name)<br />
 <i>Basic routine to allocate a chunk of memory. </i><br />
 void * <code>talloc_size</code> (const void *ctx, size_t size)<br />
 <i>Untyped allocation. </i><br />
 void * <code>talloc_ptrtype</code> (const void *ctx,#type)<br />
 <i>Allocate into a typed pointer. </i><br />
 void * <code>talloc_new</code> (const void *ctx)<br />
 <i>Allocate a new 0-sized talloc chunk. </i><br />
 void * <code>talloc_zero</code> (const void *ctx,#type)<br />
 <i>Allocate a 0-initizialized structure. </i><br />
 void * <code>talloc_zero_size</code> (const void *ctx, size_t size)<br />
 <i>Allocate untyped, 0-initialized memory. </i><br />
 const char * <code>talloc_get_name</code> (const void *ptr)<br />
 <i>Return the name of a talloc chunk. </i><br />
 void * <code>talloc_check_name</code> (const void *ptr, const char *name)<br />
 <i>Verify that a talloc chunk carries a specified name. </i><br />
 void * <code>talloc_parent</code> (const void *ptr)<br />
 <i>Get the parent chunk of a pointer. </i><br />
 const char * <code>talloc_parent_name</code> (const void *ptr)<br />
 <i>Get a talloc chunk&#8217;s parent name. </i><br />
 size_t <code>talloc_total_size</code> (const void *ptr)<br />
 <i>Get the total size of a talloc chunk including its children. </i><br />
 size_t <code>talloc_total_blocks</code> (const void *ptr)<br />
 <i>Get the number of talloc chunks hanging off a chunk. </i><br />
 void * <code>talloc_memdup</code> (const void *t, const void *p, size_t size)<br />
 <i>Duplicate a memory area into a talloc chunk. </i><br />
 void <code>talloc_set_type</code> (const char *ptr,#type)<br />
 <i>Assign a type to a talloc chunk. </i><br />
 type * <code>talloc_get_type</code> (const void *ptr,#type)<br />
 <i>Get a typed pointer out of a talloc pointer. </i><br />
 void * <code>talloc_get_type_abort</code> (const void *ptr,#type)<br />
 <i>Safely turn a void pointer into a typed pointer. </i><br />
 void * <code>talloc_find_parent_byname</code> (const void *ctx, const char *name)<br />
 <i>Find a parent context by name. </i><br />
 void * <code>talloc_find_parent_bytype</code> (const void *ptr,#type)<br />
 <i>Find a parent context by type. </i><br />
 void * <code>talloc_pool</code> (const void *context, size_t size)<br />
 <i>Allocate a talloc pool. </i><br />
 void * <code>talloc_pooled_object</code> (const void *ctx,#type, unsigned num_subobjects, size_t total_subobjects_size)<br />
 <i>Allocate a talloc object as/with an additional pool. </i></p>
<h2>Detailed Description</h2>
<p>talloc is a hierarchical, reference counted memory pool system with destructors. </p>
<p> It is the core memory allocator used in Samba.</p>
<h2>Macro Definition Documentation</h2>
<h3>#define TALLOC_FREE(ctx) do { if (ctx != NULL) { <code>talloc_free</code>(ctx); ctx=NULL; } } while(0)</h3>
<p>Free a talloc chunk and NULL out the pointer. <code>TALLOC_FREE()</code> frees a pointer and sets it to NULL. Use this if you want immediate feedback (i.e. crash) if you use a pointer after having free&#8217;ed it. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>ctx</i> The chunk to be freed.</dl>
<h2>Typedef Documentation</h2>
<h3>typedef void <code>TALLOC_CTX</code></h3>
<p>Define a talloc parent type. As talloc is a hierarchial memory allocator, every talloc chunk is a potential parent to other talloc chunks. So defining a separate type for a talloc chunk is not strictly necessary. TALLOC_CTX is defined nevertheless, as it provides an indicator for function arguments. You will frequently write code like </p>
<pre>* struct foo *foo_create(TALLOC_CTX *mem_ctx)
* {
* struct foo *result;
* result = talloc(mem_ctx, struct foo);
* if (result == NULL) return NULL;
* ... initialize foo ...
* return result;
* }
* </pre>
<p>In this type of allocating functions it is handy to have a general TALLOC_CTX type to indicate which parent to put allocated structures on.</p>
<h2>Function Documentation</h2>
<h3>void* talloc (const void *ctx, #type)</h3>
<p>Create a new talloc context. The <code>talloc()</code> macro is the core of the talloc library. It takes a memory context and a type, and returns a pointer to a new area of memory of the given type. </p>
<p> The returned pointer is itself a talloc context, so you can use it as the context argument to more calls to talloc if you wish. </p>
<p> The returned pointer is a &#8216;child&#8217; of the supplied context. This means that if you <code>talloc_free()</code> the context then the new child disappears as well. Alternatively you can free just the child. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>ctx</i> A talloc context to create a new reference on or NULL to create a new top level context.<br />
 <i>type</i> The type of memory to allocate.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>A type casted talloc context or NULL on error.</dl>
<pre>* unsigned int *a, *b;
*
* a = talloc(NULL, unsigned int);
* b = talloc(a, unsigned int);
* </pre>
<p><code>See Also:</code></p>
<dl>
<dd><code>talloc_zero</code> </p>
<p> <code>talloc_array</code> </p>
<p> <code>talloc_steal</code> </p>
<p> <code>talloc_free</code></dl>
<h3>void* talloc_check_name (const void *ptr, const char *name)</h3>
<p>Verify that a talloc chunk carries a specified name. This function checks if a pointer has the specified name. If it does then the pointer is returned. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>ptr</i> The talloc chunk to check.<br />
 <i>name</i> The name to check against.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The pointer if the name matches, NULL if it doesn&#8217;t.</dl>
<h3>void* talloc_find_parent_byname (const void *ctx, const char *name)</h3>
<p>Find a parent context by name. Find a parent memory context of the current context that has the given name. This can be very useful in complex programs where it may be difficult to pass all information down to the level you need, but you know the structure you want is a parent of another context. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>ctx</i> The talloc chunk to start from.<br />
 <i>name</i> The name of the parent we look for.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The memory context we are looking for, NULL if not found.</dl>
<h3>void* talloc_find_parent_bytype (const void *ptr, #type)</h3>
<p>Find a parent context by type. Find a parent memory context of the current context that has the given name. This can be very useful in complex programs where it may be difficult to pass all information down to the level you need, but you know the structure you want is a parent of another context. </p>
<p> Like <code>talloc_find_parent_byname()</code> but takes a type, making it typesafe. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>ptr</i> The talloc chunk to start from.<br />
 <i>type</i> The type of the parent to look for.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The memory context we are looking for, NULL if not found.</dl>
<h3>int talloc_free (void *ptr)</h3>
<p>Free a chunk of talloc memory. The <code>talloc_free()</code> function frees a piece of talloc memory, and all its children. You can call <code>talloc_free()</code> on any pointer returned by <code>talloc()</code>. </p>
<p> The return value of <code>talloc_free()</code> indicates success or failure, with 0 returned for success and -1 for failure. A possible failure condition is if the pointer had a destructor attached to it and the destructor returned -1. See <code>talloc_set_destructor()</code> for details on destructors. Likewise, if &#8216;ptr&#8217; is NULL, then the function will make no modifications and return -1. </p>
<p> From version 2.0 and onwards, as a special case, <code>talloc_free()</code> is refused on pointers that have more than one parent associated, as talloc would have no way of knowing which parent should be removed. This is different from older versions in the sense that always the reference to the most recently established parent has been destroyed. Hence to free a pointer that has more than one parent please use <code>talloc_unlink()</code>. </p>
<p> To help you find problems in your code caused by this behaviour, if you do try and free a pointer with more than one parent then the talloc logging function will be called to give output like this: </p>
<pre>* ERROR: talloc_free with references at some_dir/source/foo.c:123
* reference at some_dir/source/other.c:325
* reference at some_dir/source/third.c:121
* </pre>
<p>Please see the documentation for <code>talloc_set_log_fn()</code> and <code>talloc_set_log_stderr()</code> for more information on talloc logging functions. </p>
<p> If TALLOC_FREE_FILL environment variable is set, the memory occupied by the context is filled with the value of this variable. The value should be a numeric representation of the character you want to use. </p>
<p> <code>talloc_free()</code> operates recursively on its children. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>ptr</i> The chunk to be freed.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>Returns 0 on success and -1 on error. A possible failure condition is if the pointer had a destructor attached to it and the destructor returned -1. Likewise, if &#8216;ptr&#8217; is NULL, then the function will make no modifications and returns -1.</dl>
<p> Example: </p>
<pre>* unsigned int *a, *b;
* a = talloc(NULL, unsigned int);
* b = talloc(a, unsigned int);
*
* talloc_free(a); // Frees a and b
* </pre>
<p><code>See Also:</code></p>
<dl>
<dd><code>talloc_set_destructor()</code> </p>
<p> <code>talloc_unlink()</code></dl>
<h3>void talloc_free_children (void *ptr)</h3>
<p>Free a talloc chunk&#8217;s children. The function walks along the list of all children of a talloc context and <code>talloc_free()</code>s only the children, not the context itself. </p>
<p> A NULL argument is handled as no-op. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>ptr</i> The chunk that you want to free the children of (NULL is allowed too)</dl>
<h3>const char* talloc_get_name (const void *ptr)</h3>
<p>Return the name of a talloc chunk. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>ptr</i> The talloc chunk.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The current name for the given talloc pointer.</dl>
<p> <code>See Also:</code></p>
<dl>
<dd><code>talloc_set_name()</code></dl>
<h3>type* talloc_get_type (const void *ptr, #type)</h3>
<p>Get a typed pointer out of a talloc pointer. This macro allows you to do type checking on talloc pointers. It is particularly useful for void* private pointers. It is equivalent to this: </p>
<pre>* (type *)talloc_check_name(ptr, #type)
* </pre>
<p><code>Parameters:</code></p>
<dl>
<dd><i>ptr</i> The talloc pointer to check.<br />
 <i>type</i> The type to check against.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The properly casted pointer given by ptr, NULL on error.</dl>
<h3>void* talloc_get_type_abort (const void *ptr, #type)</h3>
<p>Safely turn a void pointer into a typed pointer. This macro is used together with talloc(mem_ctx, struct foo). If you had to assign the talloc chunk pointer to some void pointer variable, <code>talloc_get_type_abort()</code> is the recommended way to get the convert the void pointer back to a typed pointer. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>ptr</i> The void pointer to convert.<br />
 <i>type</i> The type that this chunk contains</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The same value as ptr, type-checked and properly cast.</dl>
<h3>void* talloc_init (const char *fmt, &#8230;)</h3>
<p>Create a new top level talloc context. This function creates a zero length named talloc context as a top level context. It is equivalent to: </p>
<pre>* talloc_named(NULL, 0, fmt, ...);
* </pre>
<p>&nbsp;<wbr> </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>fmt</i> Format string for the name.<br />
 <i>&#8230;</i> Additional printf-style arguments.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The allocated memory chunk, NULL on error.</dl>
<p> <code>See Also:</code></p>
<dl>
<dd><code>talloc_named()</code></dl>
<h3>void* talloc_memdup (const void *t, const void *p, size_tsize)</h3>
<p>Duplicate a memory area into a talloc chunk. The function is equivalent to: </p>
<pre>* ptr = talloc_size(ctx, size);
* if (ptr) memcpy(ptr, p, size);
* </pre>
<p><code>Parameters:</code></p>
<dl>
<dd><i>t</i> The talloc context to hang the result off.<br />
 <i>p</i> The memory chunk you want to duplicate.<br />
 <i>size</i> Number of char&#8217;s that you want copy.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The allocated memory chunk.</dl>
<p> <code>See Also:</code></p>
<dl>
<dd><code>talloc_size()</code></dl>
<h3>void* talloc_move (const void *new_ctx, void **pptr)</h3>
<p>Change a talloc chunk&#8217;s parent. This function has the same effect as <code>talloc_steal()</code>, and additionally sets the source pointer to NULL. You would use it like this: </p>
<pre>* struct foo *X = talloc(tmp_ctx, struct foo);
* struct foo *Y;
* Y = talloc_move(new_ctx, &amp;X);
* </pre>
<p><code>Parameters:</code></p>
<dl>
<dd><i>new_ctx</i> The new parent context.<br />
 <i>pptr</i> Pointer to the talloc chunk to move.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The pointer of the talloc chunk it has been moved to, NULL on error.</dl>
<h3>void* talloc_named (const void *context, size_tsize, const char *fmt, &#8230;)</h3>
<p>Create a named talloc chunk. The <code>talloc_named()</code> function creates a named talloc pointer. It is equivalent to: </p>
<pre>* ptr = talloc_size(context, size);
* talloc_set_name(ptr, fmt, ....);
* </pre>
<p><code>Parameters:</code></p>
<dl>
<dd><i>context</i> The talloc context to hang the result off.<br />
 <i>size</i> Number of char&#8217;s that you want to allocate.<br />
 <i>fmt</i> Format string for the name.<br />
 <i>&#8230;</i> Additional printf-style arguments.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The allocated memory chunk, NULL on error.</dl>
<p> <code>See Also:</code></p>
<dl>
<dd><code>talloc_set_name()</code></dl>
<h3>void* talloc_named_const (const void *context, size_tsize, const char *name)</h3>
<p>Basic routine to allocate a chunk of memory. This is equivalent to: </p>
<pre>* ptr = talloc_size(context, size);
* talloc_set_name_const(ptr, name);
* </pre>
<p><code>Parameters:</code></p>
<dl>
<dd><i>context</i> The parent context.<br />
 <i>size</i> The number of char&#8217;s that we want to allocate.<br />
 <i>name</i> The name the talloc block has.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The allocated memory chunk, NULL on error.</dl>
<h3>void* talloc_new (const void *ctx)</h3>
<p>Allocate a new 0-sized talloc chunk. This is a utility macro that creates a new memory context hanging off an existing context, automatically naming it &#8216;talloc_new: __location__&#8217; where <code>location</code> is the source line it is called from. It is particularly useful for creating a new temporary working context. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>ctx</i> The talloc parent context.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>A new talloc chunk, NULL on error.</dl>
<h3>void* talloc_parent (const void *ptr)</h3>
<p>Get the parent chunk of a pointer. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>ptr</i> The talloc pointer to inspect.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The talloc parent of ptr, NULL on error.</dl>
<h3>const char* talloc_parent_name (const void *ptr)</h3>
<p>Get a talloc chunk&#8217;s parent name. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>ptr</i> The talloc pointer to inspect.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The name of ptr&#8217;s parent chunk.</dl>
<h3>void* talloc_pool (const void *context, size_tsize)</h3>
<p>Allocate a talloc pool. A talloc pool is a pure optimization for specific situations. In the release process for Samba 3.2 we found out that we had become considerably slower than Samba 3.0 was. Profiling showed that <a href="/docs/linux/man/3-malloc/">malloc</a>(3) was a large CPU consumer in benchmarks. For Samba 3.2 we have internally converted many static buffers to dynamically allocated ones, so <a href="/docs/linux/man/3-malloc/">malloc</a>(3) being beaten more was no surprise. But it made us slower. </p>
<p> <code>talloc_pool()</code> is an optimization to call <a href="/docs/linux/man/3-malloc/">malloc</a>(3) a lot less for the use pattern Samba has: The SMB protocol is mainly a request/response protocol where we have to allocate a certain amount of memory per request and free that after the SMB reply is sent to the client. </p>
<p> <code>talloc_pool()</code> creates a talloc chunk that you can use as a talloc parent exactly as you would use any other <code>TALLOC_CTX</code>. The difference is that when you talloc a child of this pool, no <a href="/docs/linux/man/3-malloc/">malloc</a>(3) is done. Instead, talloc just increments a pointer inside the talloc_pool. This also works recursively. If you use the child of the talloc pool as a parent for grand-children, their memory is also taken from the talloc pool. </p>
<p> If there is not enough memory in the pool to allocate the new child, it will create a new talloc chunk as if the parent was a normal talloc context. </p>
<p> If you <code>talloc_free()</code> children of a talloc pool, the memory is not given back to the system. Instead, <a href="/docs/linux/man/3-free/">free</a>(3) is only called if the <code>talloc_pool()</code> itself is released with <code>talloc_free()</code>. </p>
<p> The downside of a talloc pool is that if you <code>talloc_move()</code> a child of a talloc pool to a talloc parent outside the pool, the whole pool memory is not <a href="/docs/linux/man/3-free/">free</a>(3)&#8217;ed until that moved chunk is also <code>talloc_free()</code>ed. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>context</i> The talloc context to hang the result off.<br />
 <i>size</i> Size of the talloc pool.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The allocated talloc pool, NULL on error.</dl>
<h3>void* talloc_pooled_object (const void *ctx, #type, unsignednum_subobjects, size_ttotal_subobjects_size)</h3>
<p>Allocate a talloc object as/with an additional pool. This is like <code>talloc_pool()</code>, but&#8217;s it&#8217;s more flexible and allows an object to be a pool for its children. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>ctx</i> The talloc context to hang the result off.<br />
 <i>type</i> The type that we want to allocate.<br />
 <i>num_subobjects</i> The expected number of subobjects, which will be allocated within the pool. This allocates space for talloc_chunk headers.<br />
 <i>total_subobjects_size</i> The size that all subobjects can use in total.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The allocated talloc object, NULL on error.</dl>
<h3>void* talloc_ptrtype (const void *ctx, #type)</h3>
<p>Allocate into a typed pointer. The <code>talloc_ptrtype()</code> macro should be used when you have a pointer and want to allocate memory to point at with this pointer. When compiling with gcc &gt;= 3 it is typesafe. Note this is a wrapper of <code>talloc_size()</code> and <code>talloc_get_name()</code> will return the current location in the source file and not the type. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>ctx</i> The talloc context to hang the result off.<br />
 <i>type</i> The pointer you want to assign the result to.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The properly casted allocated memory chunk, NULL on error.</dl>
<p> Example: </p>
<pre>* unsigned int *a = talloc_ptrtype(NULL, a);
* </pre>
<p>&nbsp;<wbr></p>
<h3>void talloc_set_destructor (const void *ptr, int(*)(void *)destructor)</h3>
<p>Assign a destructor function to be called when a chunk is freed. The function <code>talloc_set_destructor()</code> sets the &#8216;destructor&#8217; for the pointer &#8216;ptr&#8217;. A destructor is a function that is called when the memory used by a pointer is about to be released. The destructor receives the pointer as an argument, and should return 0 for success and -1 for failure. </p>
<p> The destructor can do anything it wants to, including freeing other pieces of memory. A common use for destructors is to clean up operating system resources (such as open file descriptors) contained in the structure the destructor is placed on. </p>
<p> You can only place one destructor on a pointer. If you need more than one destructor then you can create a zero-length child of the pointer and place an additional destructor on that. </p>
<p> To remove a destructor call <code>talloc_set_destructor()</code> with NULL for the destructor. </p>
<p> If your destructor attempts to <code>talloc_free()</code> the pointer that it is the destructor for then <code>talloc_free()</code> will return -1 and the free will be ignored. This would be a pointless operation anyway, as the destructor is only called when the memory is just about to go away. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>ptr</i> The talloc chunk to add a destructor to.<br />
 <i>destructor</i> The destructor function to be called. NULL to remove it.</dl>
<p> Example: </p>
<pre>* static int destroy_fd(int *fd) {
* close(*fd);
* return 0;
* }
*
* int *open_file(const char *filename) {
* int *fd = talloc(NULL, int);
* *fd = open(filename, O_RDONLY);
* if (*fd &lt; 0) {
* talloc_free(fd);
* return NULL;
* }
* // Whenever they free this, we close the file.
* talloc_set_destructor(fd, destroy_fd);
* return fd;
* }
* </pre>
<p><code>See Also:</code></p>
<dl>
<dd><code>talloc()</code> </p>
<p> <code>talloc_free()</code></dl>
<h3>const char* talloc_set_name (const void *ptr, const char *fmt, &#8230;)</h3>
<p>Assign a name to a talloc chunk. Each talloc pointer has a &#8216;name&#8217;. The name is used principally for debugging purposes, although it is also possible to set and get the name on a pointer in as a way of &#8216;marking&#8217; pointers in your code. </p>
<p> The main use for names on pointer is for &#8216;talloc reports&#8217;. See <code>talloc_report()</code> and <code>talloc_report_full()</code> for details. Also see <code>talloc_enable_leak_report()</code> and <code>talloc_enable_leak_report_full()</code>. </p>
<p> The <code>talloc_set_name()</code> function allocates memory as a child of the pointer. It is logically equivalent to: </p>
<pre>* talloc_set_name_const(ptr, talloc_asprintf(ptr, fmt, ...));
* </pre>
<p><code>Parameters:</code></p>
<dl>
<dd><i>ptr</i> The talloc chunk to assign a name to.<br />
 <i>fmt</i> Format string for the name.<br />
 <i>&#8230;</i> Add printf-style additional arguments.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The assigned name, NULL on error.</dl>
<p> <code>Note:</code></p>
<dl>
<dd>Multiple calls to <code>talloc_set_name()</code> will allocate more memory without releasing the name. All of the memory is released when the ptr is freed using <code>talloc_free()</code>.</dl>
<h3>void talloc_set_name_const (const void *ptr, const char *name)</h3>
<p>Assign a name to a talloc chunk. The function is just like <code>talloc_set_name()</code>, but it takes a string constant, and is much faster. It is extensively used by the &#8216;auto naming&#8217; macros, such as talloc_p(). </p>
<p> This function does not allocate any memory. It just copies the supplied pointer into the internal representation of the talloc ptr. This means you must not pass a name pointer to memory that will disappear before the ptr is freed with <code>talloc_free()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>ptr</i> The talloc chunk to assign a name to.<br />
 <i>name</i> Format string for the name.</dl>
<h3>void talloc_set_type (const char *ptr, #type)</h3>
<p>Assign a type to a talloc chunk. This macro allows you to force the name of a pointer to be of a particular type. This can be used in conjunction with <code>talloc_get_type()</code> to do type checking on void* pointers. </p>
<p> It is equivalent to this: </p>
<pre>* talloc_set_name_const(ptr, #type)
* </pre>
<p><code>Parameters:</code></p>
<dl>
<dd><i>ptr</i> The talloc chunk to assign the type to.<br />
 <i>type</i> The type to assign.</dl>
<h3>void* talloc_size (const void *ctx, size_tsize)</h3>
<p>Untyped allocation. The function should be used when you don&#8217;t have a convenient type to pass to <code>talloc()</code>. Unlike <code>talloc()</code>, it is not type safe (as it returns a void *), so you are on your own for type checking. </p>
<p> Best to use <code>talloc()</code> or <code>talloc_array()</code> instead. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>ctx</i> The talloc context to hang the result off.<br />
 <i>size</i> Number of char&#8217;s that you want to allocate.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The allocated memory chunk, NULL on error.</dl>
<p> Example: </p>
<pre>* void *mem = talloc_size(NULL, 100);
* </pre>
<p>&nbsp;<wbr></p>
<h3>void* talloc_steal (const void *new_ctx, const void *ptr)</h3>
<p>Change a talloc chunk&#8217;s parent. The <code>talloc_steal()</code> function changes the parent context of a talloc pointer. It is typically used when the context that the pointer is currently a child of is going to be freed and you wish to keep the memory for a longer time. </p>
<p> To make the changed hierarchy less error-prone, you might consider to use <code>talloc_move()</code>. </p>
<p> If you try and call <code>talloc_steal()</code> on a pointer that has more than one parent then the result is ambiguous. Talloc will choose to remove the parent that is currently indicated by <code>talloc_parent()</code> and replace it with the chosen parent. You will also get a message like this via the talloc logging functions: </p>
<pre>* WARNING: talloc_steal with references at some_dir/source/foo.c:123
* reference at some_dir/source/other.c:325
* reference at some_dir/source/third.c:121
* </pre>
<p>To unambiguously change the parent of a pointer please see the function <code>talloc_reparent()</code>. See the <code>talloc_set_log_fn()</code> documentation for more information on talloc logging. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>new_ctx</i> The new parent context.<br />
 <i>ptr</i> The talloc chunk to move.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>Returns the pointer that you pass it. It does not have any failure modes.</dl>
<p> <code>Note:</code></p>
<dl>
<dd>It is possible to produce loops in the parent/child relationship if you are not careful with <code>talloc_steal()</code>. No guarantees are provided as to your sanity or the safety of your data if you do this.</dl>
<h3>size_t talloc_total_blocks (const void *ptr)</h3>
<p>Get the number of talloc chunks hanging off a chunk. The <code>talloc_total_blocks()</code> function returns the total memory block count used by this pointer and all child pointers. Mostly useful for debugging. </p>
<p> Passing NULL is allowed, but it will only give a meaningful result if <code>talloc_enable_leak_report()</code> or <code>talloc_enable_leak_report_full()</code> has been called. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>ptr</i> The talloc chunk.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The total size.</dl>
<h3>size_t talloc_total_size (const void *ptr)</h3>
<p>Get the total size of a talloc chunk including its children. The function returns the total size in bytes used by this pointer and all child pointers. Mostly useful for debugging. </p>
<p> Passing NULL is allowed, but it will only give a meaningful result if <code>talloc_enable_leak_report()</code> or <code>talloc_enable_leak_report_full()</code> has been called. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>ptr</i> The talloc chunk.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The total size.</dl>
<h3>void* talloc_zero (const void *ctx, #type)</h3>
<p>Allocate a 0-initizialized structure. The macro is equivalent to: </p>
<pre>* ptr = talloc(ctx, type);
* if (ptr) memset(ptr, 0, sizeof(type));
* </pre>
<p><code>Parameters:</code></p>
<dl>
<dd><i>ctx</i> The talloc context to hang the result off.<br />
 <i>type</i> The type that we want to allocate.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>Pointer to a piece of memory, properly cast to &#8216;type *&#8217;, NULL on error.</dl>
<p> Example: </p>
<pre>* unsigned int *a, *b;
* a = talloc_zero(NULL, unsigned int);
* b = talloc_zero(a, unsigned int);
* </pre>
<p><code>See Also:</code></p>
<dl>
<dd><code>talloc()</code> </p>
<p> <code>talloc_zero_size()</code> </p>
<p> <code>talloc_zero_array()</code></dl>
<h3>void* talloc_zero_size (const void *ctx, size_tsize)</h3>
<p>Allocate untyped, 0-initialized memory. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>ctx</i> The talloc context to hang the result off.<br />
 <i>size</i> Number of char&#8217;s that you want to allocate.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The allocated memory chunk.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for talloc from the source code.</p>
