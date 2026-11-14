---
title: "talloc_ref(3)"
name: "talloc_ref"
section: "3"
letter: "t"
url: "/docs/linux/man/3-talloc_ref/"
description: "The talloc reference function. –"
---

<p>The talloc reference function. &#8211; </p>
<p> This module contains the definitions around talloc references.</p>
<h3>Modules</h3>
<p><code>The talloc array functions</code><br />
 <i>Talloc contains some handy helpers for handling Arrays conveniently. </i></p>
<h3>Functions</h3>
<p>int <code>talloc_increase_ref_count</code> (const void *ptr)<br />
 <i>Increase the reference count of a talloc chunk. </i><br />
 size_t <code>talloc_reference_count</code> (const void *ptr)<br />
 <i>Get the number of references to a talloc chunk. </i><br />
 void * <code>talloc_reference</code> (const void *ctx, const void *ptr)<br />
 <i>Create an additional talloc parent to a pointer. </i><br />
 int <code>talloc_unlink</code> (const void *context, void *ptr)<br />
 <i>Remove a specific parent from a talloc chunk. </i><br />
 void * <code>talloc_autofree_context</code> (void)<br />
 <i>Provide a talloc context that is freed at program exit. </i><br />
 size_t <code>talloc_get_size</code> (const void *ctx)<br />
 <i>Get the size of a talloc chunk. </i><br />
 void <code>talloc_show_parents</code> (const void *context, FILE *file)<br />
 <i>Show the parentage of a context. </i><br />
 int <code>talloc_is_parent</code> (const void *context, const void *ptr)<br />
 <i>Check if a context is parent of a talloc chunk. </i><br />
 void * <code>talloc_reparent</code> (const void *old_parent, const void *new_parent, const void *ptr)<br />
 <i>Change the parent context of a talloc pointer. </i></p>
<h2>Detailed Description</h2>
<p>This module contains the definitions around talloc references.</p>
<h2>Function Documentation</h2>
<h3>void* talloc_autofree_context (void)</h3>
<p>Provide a talloc context that is freed at program exit. This is a handy utility function that returns a talloc context which will be automatically freed on program exit. This can be used to reduce the noise in memory leak reports. </p>
<p> Never use this in code that might be used in objects loaded with dlopen and unloaded with dlclose. <code>talloc_autofree_context()</code> internally uses <a href="/docs/linux/man/3-atexit/">atexit</a>(3). Some platforms like modern Linux handles this fine, but for example FreeBSD does not deal well with dlopen() and atexit() used simultaneously: dlclose() does not clean up the list of atexit-handlers, so when the program exits the code that was registered from within <code>talloc_autofree_context()</code> is gone, the program crashes at exit. </p>
<p> <code>Returns:</code></p>
<dl>
<dd>A talloc context, NULL on error.</dl>
<h3>size_t talloc_get_size (const void *ctx)</h3>
<p>Get the size of a talloc chunk. This function lets you know the amount of memory allocated so far by this context. It does NOT account for subcontext memory. This can be used to calculate the size of an array. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>ctx</i> The talloc chunk.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The size of the talloc chunk.</dl>
<h3>int talloc_increase_ref_count (const void *ptr)</h3>
<p>Increase the reference count of a talloc chunk. The talloc_increase_ref_count(ptr) function is exactly equivalent to: </p>
<pre>* talloc_reference(NULL, ptr);
* </pre>
<p>You can use either syntax, depending on which you think is clearer in your code. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>ptr</i> The pointer to increase the reference count.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>0 on success, -1 on error.</dl>
<h3>int talloc_is_parent (const void *context, const void *ptr)</h3>
<p>Check if a context is parent of a talloc chunk. This checks if context is referenced in the talloc hierarchy above ptr. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>context</i> The assumed talloc context.<br />
 <i>ptr</i> The talloc chunk to check.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>Return 1 if this is the case, 0 if not.</dl>
<h3>void* talloc_reference (const void *ctx, const void *ptr)</h3>
<p>Create an additional talloc parent to a pointer. The <code>talloc_reference()</code> function makes &#8216;context&#8217; an additional parent of ptr. Each additional reference consumes around 48 bytes of memory on intel x86 platforms. </p>
<p> If ptr is NULL, then the function is a no-op, and simply returns NULL. </p>
<p> After creating a reference you can free it in one of the following ways: </p>
<dl>
<dt>&bull;</p>
<dd>you can <code>talloc_free()</code> any parent of the original pointer. That will reduce the number of parents of this pointer by 1, and will cause this pointer to be freed if it runs out of parents.</p>
<dt>&bull;</p>
<dd>you can <code>talloc_free()</code> the pointer itself if it has at maximum one parent. This behaviour has been changed since the release of version 2.0. Further informations in the description of &#8216;talloc_free&#8217;.</dl>
<p> For more control on which parent to remove, see <code>talloc_unlink()</code> </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>ctx</i> The additional parent.<br />
 <i>ptr</i> The pointer you want to create an additional parent for.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The original pointer &#8216;ptr&#8217;, NULL if talloc ran out of memory in creating the reference.</dl>
<p> <code>Warning:</code></p>
<dl>
<dd>You should try to avoid using this interface. It turns a beautiful talloc-tree into a graph. It is often really hard to debug if you screw something up by accident.</dl>
<p> Example: </p>
<pre>* unsigned int *a, *b, *c;
* a = talloc(NULL, unsigned int);
* b = talloc(NULL, unsigned int);
* c = talloc(a, unsigned int);
* // b also serves as a parent of c.
* talloc_reference(b, c);
* </pre>
<p><code>See Also:</code></p>
<dl>
<dd><code>talloc_unlink()</code></dl>
<h3>size_t talloc_reference_count (const void *ptr)</h3>
<p>Get the number of references to a talloc chunk. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>ptr</i> The pointer to retrieve the reference count from.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The number of references.</dl>
<h3>void* talloc_reparent (const void *old_parent, const void *new_parent, const void *ptr)</h3>
<p>Change the parent context of a talloc pointer. The function changes the parent context of a talloc pointer. It is typically used when the context that the pointer is currently a child of is going to be freed and you wish to keep the memory for a longer time. </p>
<p> The difference between <code>talloc_reparent()</code> and <code>talloc_steal()</code> is that <code>talloc_reparent()</code> can specify which parent you wish to change. This is useful when a pointer has multiple parents via references. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>old_parent</i><br />
 <i>new_parent</i><br />
 <i>ptr</i></dl>
<p> <code>Returns:</code></p>
<dl>
<dd>Return the pointer you passed. It does not have any failure modes.</dl>
<h3>void talloc_show_parents (const void *context, FILE *file)</h3>
<p>Show the parentage of a context. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>context</i> The talloc context to look at.<br />
 <i>file</i> The output to use, a file, stdout or stderr.</dl>
<h3>int talloc_unlink (const void *context, void *ptr)</h3>
<p>Remove a specific parent from a talloc chunk. The function removes a specific parent from ptr. The context passed must either be a context used in <code>talloc_reference()</code> with this pointer, or must be a direct parent of ptr. </p>
<p> You can just use <code>talloc_free()</code> instead of <code>talloc_unlink()</code> if there is at maximum one parent. This behaviour has been changed since the release of version 2.0. Further informations in the description of &#8216;talloc_free&#8217;. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>context</i> The talloc parent to remove.<br />
 <i>ptr</i> The talloc ptr you want to remove the parent from.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>0 on success, -1 on error.</dl>
<p> <code>Note:</code></p>
<dl>
<dd>If the parent has already been removed using <code>talloc_free()</code> then this function will fail and will return -1. Likewise, if ptr is NULL, then the function will make no modifications and return -1.</dl>
<p> <code>Warning:</code></p>
<dl>
<dd>You should try to avoid using this interface. It turns a beautiful talloc-tree into a graph. It is often really hard to debug if you screw something up by accident.</dl>
<p> Example: </p>
<pre>* unsigned int *a, *b, *c;
* a = talloc(NULL, unsigned int);
* b = talloc(NULL, unsigned int);
* c = talloc(a, unsigned int);
* // b also serves as a parent of c.
* talloc_reference(b, c);
* talloc_unlink(b, c);
* </pre>
<p>&nbsp;<wbr></p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for talloc from the source code.</p>
