---
title: "talloc_array(3)"
name: "talloc_array"
section: "3"
letter: "t"
url: "/docs/linux/man/3-talloc_array/"
description: "The talloc array functions – Talloc contains some handy helpers for handling Arrays conveniently."
---

<p>The talloc array functions &#8211; Talloc contains some handy helpers for handling Arrays conveniently.</p>
<h3>Modules</h3>
<p><code>The talloc string functions.</code><br />
 <i>talloc string allocation and manipulation functions. </i></p>
<h3>Functions</h3>
<pre><code>void * talloc_array (const void *ctx,#type, unsigned count)


Allocate an array.


void * talloc_array_size (const void *ctx, size_t size, unsigned count)


Allocate an array.


void * talloc_array_ptrtype (const void *ctx, const void *ptr, unsigned count)


Allocate an array into a typed pointer.


size_t talloc_array_length (const void *ctx)


Get the number of elements in a talloc'ed array.


void * talloc_zero_array (const void *ctx,#type, unsigned count)


Allocate a zero-initialized array.


void * talloc_realloc (const void *ctx, void *ptr,#type, size_t count)


Change the size of a talloc array.


void * talloc_realloc_size (const void *ctx, void *ptr, size_t size)


Untyped realloc to change the size of a talloc array.


void * talloc_realloc_fn (const void *context, void *ptr, size_t size)


Provide a function version of talloc_realloc_size.</code></pre>
<h2>Detailed Description</h2>
<p>Talloc contains some handy helpers for handling Arrays conveniently.</p>
<h2>Function Documentation</h2>
<h3>void* talloc_array (const void *ctx, #type, unsignedcount)</h3>
<p>Allocate an array. The macro is equivalent to: </p>
<pre>* (type *)talloc_size(ctx, sizeof(type) * count);
* </pre>
<p>except that it provides integer overflow protection for the multiply, returning NULL if the multiply overflows. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>ctx</i> The talloc context to hang the result off.<br />
 <i>type</i> The type that we want to allocate.<br />
 <i>count</i> The number of &#8216;type&#8217; elements you want to allocate.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The allocated result, properly cast to &#8216;type *&#8217;, NULL on error.</dl>
<p> Example: </p>
<pre>* unsigned int *a, *b;
* a = talloc_zero(NULL, unsigned int);
* b = talloc_array(a, unsigned int, 100);
* </pre>
<p><code>See Also:</code></p>
<dl>
<dd><code>talloc()</code> </p>
<p> <code>talloc_zero_array()</code></dl>
<h3>size_t talloc_array_length (const void *ctx)</h3>
<p>Get the number of elements in a talloc&#8217;ed array. A talloc chunk carries its own size, so for talloc&#8217;ed arrays it is not necessary to store the number of elements explicitly. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>ctx</i> The allocated array.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The number of elements in ctx.</dl>
<h3>void* talloc_array_ptrtype (const void *ctx, const void *ptr, unsignedcount)</h3>
<p>Allocate an array into a typed pointer. The macro should be used when you have a pointer to an array and want to allocate memory of an array to point at with this pointer. When compiling with gcc &gt;= 3 it is typesafe. Note this is a wrapper of <code>talloc_array_size()</code> and <code>talloc_get_name()</code> will return the current location in the source file and not the type. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>ctx</i> The talloc context to hang the result off.<br />
 <i>ptr</i> The pointer you want to assign the result to.<br />
 <i>count</i> The number of elements you want to allocate.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The allocated memory chunk, properly casted. NULL on error.</dl>
<h3>void* talloc_array_size (const void *ctx, size_tsize, unsignedcount)</h3>
<p>Allocate an array. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>ctx</i> The talloc context to hang the result off.<br />
 <i>size</i> The size of an array element.<br />
 <i>count</i> The number of elements you want to allocate.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The allocated result, NULL on error.</dl>
<h3>void* talloc_realloc (const void *ctx, void *ptr, #type, size_tcount)</h3>
<p>Change the size of a talloc array. The macro changes the size of a talloc pointer. The &#8216;count&#8217; argument is the number of elements of type &#8216;type&#8217; that you want the resulting pointer to hold. </p>
<p> <code>talloc_realloc()</code> has the following equivalences: </p>
<pre>* talloc_realloc(ctx, NULL, type, 1) ==&gt; talloc(ctx, type);
* talloc_realloc(ctx, NULL, type, N) ==&gt; talloc_array(ctx, type, N);
* talloc_realloc(ctx, ptr, type, 0) ==&gt; talloc_free(ptr);
* </pre>
<p>The &#8216;context&#8217; argument is only used if &#8216;ptr&#8217; is NULL, otherwise it is ignored. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>ctx</i> The parent context used if ptr is NULL.<br />
 <i>ptr</i> The chunk to be resized.<br />
 <i>type</i> The type of the array element inside ptr.<br />
 <i>count</i> The intended number of array elements.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The new array, NULL on error. The call will fail either due to a lack of memory, or because the pointer has more than one parent (see <code>talloc_reference()</code>).</dl>
<h3>void* talloc_realloc_fn (const void *context, void *ptr, size_tsize)</h3>
<p>Provide a function version of talloc_realloc_size. This is a non-macro version of <code>talloc_realloc()</code>, which is useful as libraries sometimes want a ralloc function pointer. A realloc() implementation encapsulates the functionality of malloc(), free() and realloc() in one call, which is why it is useful to be able to pass around a single function pointer. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>context</i> The parent context used if ptr is NULL.<br />
 <i>ptr</i> The chunk to be resized.<br />
 <i>size</i> The new chunk size.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The new chunk, NULL on error.</dl>
<h3>void* talloc_realloc_size (const void *ctx, void *ptr, size_tsize)</h3>
<p>Untyped realloc to change the size of a talloc array. The macro is useful when the type is not known so the typesafe <code>talloc_realloc()</code> cannot be used. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>ctx</i> The parent context used if &#8216;ptr&#8217; is NULL.<br />
 <i>ptr</i> The chunk to be resized.<br />
 <i>size</i> The new chunk size.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The new array, NULL on error.</dl>
<h3>void* talloc_zero_array (const void *ctx, #type, unsignedcount)</h3>
<p>Allocate a zero-initialized array. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>ctx</i> The talloc context to hang the result off.<br />
 <i>type</i> The type that we want to allocate.<br />
 <i>count</i> The number of &#8216;type&#8217; elements you want to allocate.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The allocated result casted to &#8216;type *&#8217;, NULL on error.</dl>
<p> The <code>talloc_zero_array()</code> macro is equivalent to: </p>
<pre>* ptr = talloc_array(ctx, type, count);
* if (ptr) memset(ptr, sizeof(type) * count);
* </pre>
<p>&nbsp;<wbr></p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for talloc from the source code.</p>
