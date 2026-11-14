---
title: "talloc_debug(3)"
name: "talloc_debug"
section: "3"
letter: "t"
url: "/docs/linux/man/3-talloc_debug/"
description: "The talloc debugging support functions –"
---

<p>The talloc debugging support functions &#8211; </p>
<p> To aid memory debugging, talloc contains routines to inspect the currently allocated memory hierarchy.</p>
<h3>Functions</h3>
<p>void <code>talloc_report_depth_cb</code> (const void *ptr, int depth, int max_depth, void(*callback)(const void *ptr, int depth, int max_depth, int is_ref, void *private_data), void *private_data)<br />
 <i>Walk a complete talloc hierarchy. </i><br />
 void <code>talloc_report_depth_file</code> (const void *ptr, int depth, int max_depth, FILE *f)<br />
 <i>Print a talloc hierarchy. </i><br />
 void <code>talloc_report_full</code> (const void *ptr, FILE *f)<br />
 <i>Print a summary report of all memory used by ptr. </i><br />
 void <code>talloc_report</code> (const void *ptr, FILE *f)<br />
 <i>Print a summary report of all memory used by ptr. </i><br />
 void <code>talloc_enable_null_tracking</code> (void)<br />
 <i>Enable tracking the use of NULL memory contexts. </i><br />
 void <code>talloc_enable_null_tracking_no_autofree</code> (void)<br />
 <i>Enable tracking the use of NULL memory contexts. </i><br />
 void <code>talloc_disable_null_tracking</code> (void)<br />
 <i>Disable tracking of the NULL memory context. </i><br />
 void <code>talloc_enable_leak_report</code> (void)<br />
 <i>Enable leak report when a program exits. </i><br />
 void <code>talloc_enable_leak_report_full</code> (void)<br />
 <i>Enable full leak report when a program exits. </i><br />
 void <code>talloc_set_abort_fn</code> (void(*abort_fn)(const char *reason))<br />
 <i>Set a custom &#8216;abort&#8217; function that is called on serious error. </i><br />
 void <code>talloc_set_log_fn</code> (void(*log_fn)(const char *message))<br />
 <i>Set a logging function. </i><br />
 void <code>talloc_set_log_stderr</code> (void)<br />
 <i>Set stderr as the output for logs. </i><br />
 int <code>talloc_set_memlimit</code> (const void *ctx, size_t max_size)<br />
 <i>Set a max memory limit for the current context hierarchy This affects all children of this context and constrain any allocation in the hierarchy to never exceed the limit set. </i></p>
<h2>Detailed Description</h2>
<p>To aid memory debugging, talloc contains routines to inspect the currently allocated memory hierarchy.</p>
<h2>Function Documentation</h2>
<h3>void talloc_disable_null_tracking (void)</h3>
<p>Disable tracking of the NULL memory context. This disables tracking of the NULL memory context.</p>
<h3>void talloc_enable_leak_report (void)</h3>
<p>Enable leak report when a program exits. This enables calling of talloc_report(NULL, stderr) when the program exits. In Samba4 this is enabled by using the &#8211;leak-report command line option. </p>
<p> For it to be useful, this function must be called before any other talloc function as it establishes a &#8216;null context&#8217; that acts as the top of the tree. If you don&#8217;t call this function first then passing NULL to <code>talloc_report()</code> or <code>talloc_report_full()</code> won&#8217;t give you the full tree printout. </p>
<p> Here is a typical talloc report: </p>
<pre>* talloc report on 'null_context' (total 267 bytes in 15 blocks)
* libcli/auth/spnego_parse.c:55 contains 31 bytes in 2 blocks
* libcli/auth/spnego_parse.c:55 contains 31 bytes in 2 blocks
* iconv(UTF8,CP850) contains 42 bytes in 2 blocks
* libcli/auth/spnego_parse.c:55 contains 31 bytes in 2 blocks
* iconv(CP850,UTF8) contains 42 bytes in 2 blocks
* iconv(UTF8,UTF-16LE) contains 45 bytes in 2 blocks
* iconv(UTF-16LE,UTF8) contains 45 bytes in 2 blocks
* </pre>
<p>&nbsp;<wbr></p>
<h3>void talloc_enable_leak_report_full (void)</h3>
<p>Enable full leak report when a program exits. This enables calling of talloc_report_full(NULL, stderr) when the program exits. In Samba4 this is enabled by using the &#8211;leak-report-full command line option. </p>
<p> For it to be useful, this function must be called before any other talloc function as it establishes a &#8216;null context&#8217; that acts as the top of the tree. If you don&#8217;t call this function first then passing NULL to <code>talloc_report()</code> or <code>talloc_report_full()</code> won&#8217;t give you the full tree printout. </p>
<p> Here is a typical full report: </p>
<pre>* full talloc report on 'root' (total 18 bytes in 8 blocks)
* p1 contains 18 bytes in 7 blocks (ref 0)
* r1 contains 13 bytes in 2 blocks (ref 0)
* reference to: p2
* p2 contains 1 bytes in 1 blocks (ref 1)
* x3 contains 1 bytes in 1 blocks (ref 0)
* x2 contains 1 bytes in 1 blocks (ref 0)
* x1 contains 1 bytes in 1 blocks (ref 0)
* </pre>
<p>&nbsp;<wbr></p>
<h3>void talloc_enable_null_tracking (void)</h3>
<p>Enable tracking the use of NULL memory contexts. This enables tracking of the NULL memory context without enabling leak reporting on exit. Useful for when you want to do your own leak reporting call via talloc_report_null_full();</p>
<h3>void talloc_enable_null_tracking_no_autofree (void)</h3>
<p>Enable tracking the use of NULL memory contexts. This enables tracking of the NULL memory context without enabling leak reporting on exit. Useful for when you want to do your own leak reporting call via talloc_report_null_full();</p>
<h3>void talloc_report (const void *ptr, FILE *f)</h3>
<p>Print a summary report of all memory used by ptr. This function prints a summary report of all memory used by ptr. One line of report is printed for each immediate child of ptr, showing the total memory and number of blocks used by that child. </p>
<p> You can pass NULL for the pointer, in which case a report is printed for the top level memory context, but only if <code>talloc_enable_leak_report()</code> or <code>talloc_enable_leak_report_full()</code> has been called. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>ptr</i> The talloc chunk.<br />
 <i>f</i> The file handle to print to.</dl>
<p> Example: </p>
<pre>* unsigned int *a, *b;
* a = talloc(NULL, unsigned int);
* b = talloc(a, unsigned int);
* fprintf(stderr, &quot;Summary of memory tree for a:);
* talloc_report(a, stderr);
* </pre>
<p><code>See Also:</code></p>
<dl>
<dd><code>talloc_report_full()</code></dl>
<h3>void talloc_report_depth_cb (const void *ptr, intdepth, intmax_depth, void(*)(const void *ptr, int depth, int max_depth, int is_ref, void *private_data)callback, void *private_data)</h3>
<p>Walk a complete talloc hierarchy. This provides a more flexible reports than <code>talloc_report()</code>. It will recursively call the callback for the entire tree of memory referenced by the pointer. References in the tree are passed with is_ref = 1 and the pointer that is referenced. </p>
<p> You can pass NULL for the pointer, in which case a report is printed for the top level memory context, but only if <code>talloc_enable_leak_report()</code> or <code>talloc_enable_leak_report_full()</code> has been called. </p>
<p> The recursion is stopped when depth &gt;= max_depth. max_depth = -1 means only stop at leaf nodes. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>ptr</i> The talloc chunk.<br />
 <i>depth</i> Internal parameter to control recursion. Call with 0.<br />
 <i>max_depth</i> Maximum recursion level.<br />
 <i>callback</i> Function to be called on every chunk.<br />
 <i>private_data</i> Private pointer passed to callback.</dl>
<h3>void talloc_report_depth_file (const void *ptr, intdepth, intmax_depth, FILE *f)</h3>
<p>Print a talloc hierarchy. This provides a more flexible reports than <code>talloc_report()</code>. It will let you specify the depth and max_depth. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>ptr</i> The talloc chunk.<br />
 <i>depth</i> Internal parameter to control recursion. Call with 0.<br />
 <i>max_depth</i> Maximum recursion level.<br />
 <i>f</i> The file handle to print to.</dl>
<h3>void talloc_report_full (const void *ptr, FILE *f)</h3>
<p>Print a summary report of all memory used by ptr. This provides a more detailed report than <code>talloc_report()</code>. It will recursively print the entire tree of memory referenced by the pointer. References in the tree are shown by giving the name of the pointer that is referenced. </p>
<p> You can pass NULL for the pointer, in which case a report is printed for the top level memory context, but only if <code>talloc_enable_leak_report()</code> or <code>talloc_enable_leak_report_full()</code> has been called. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>ptr</i> The talloc chunk.<br />
 <i>f</i> The file handle to print to.</dl>
<p> Example: </p>
<pre>* unsigned int *a, *b;
* a = talloc(NULL, unsigned int);
* b = talloc(a, unsigned int);
* fprintf(stderr, &quot;Dumping memory tree for a:);
* talloc_report_full(a, stderr);
* </pre>
<p><code>See Also:</code></p>
<dl>
<dd><code>talloc_report()</code></dl>
<h3>void talloc_set_abort_fn (void(*)(const char *reason)abort_fn)</h3>
<p>Set a custom &#8216;abort&#8217; function that is called on serious error. The default &#8216;abort&#8217; function is abort(). </p>
<p> The &#8216;abort&#8217; function is called when: </p>
<dl>
<dt>&bull;</p>
<dd><code>talloc_get_type_abort()</code> fails</p>
<dt>&bull;</p>
<dd>the provided pointer is not a valid talloc context</p>
<dt>&bull;</p>
<dd>when the context meta data are invalid</p>
<dt>&bull;</p>
<dd>when access after free is detected</dl>
<p> Example: </p>
<pre>* void my_abort(const char *reason)
* {
* fprintf(stderr, &quot;talloc abort: %s, reason);
* abort();
* }
*
* talloc_set_abort_fn(my_abort);
* </pre>
<p><code>Parameters:</code></p>
<dl>
<dd><i>abort_fn</i> The new &#8216;abort&#8217; function.</dl>
<p> <code>See Also:</code></p>
<dl>
<dd><code>talloc_set_log_fn()</code> </p>
<p> <code>talloc_get_type()</code></dl>
<h3>void talloc_set_log_fn (void(*)(const char *message)log_fn)</h3>
<p>Set a logging function. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>log_fn</i> The logging function.</dl>
<p> <code>See Also:</code></p>
<dl>
<dd><code>talloc_set_log_stderr()</code> </p>
<p> <code>talloc_set_abort_fn()</code></dl>
<h3>void talloc_set_log_stderr (void)</h3>
<p>Set stderr as the output for logs. </p>
<p> <code>See Also:</code></p>
<dl>
<dd><code>talloc_set_log_fn()</code> </p>
<p> <code>talloc_set_abort_fn()</code></dl>
<h3>int talloc_set_memlimit (const void *ctx, size_tmax_size)</h3>
<p>Set a max memory limit for the current context hierarchy This affects all children of this context and constrain any allocation in the hierarchy to never exceed the limit set. </p>
<pre> The limit can be removed by setting 0 (unlimited) as the
 max_size by calling the funciton again on the sam context.
 Memory limits can also be nested, meaning a hild can have
 a stricter memory limit than a parent.
 Memory limits are enforced only at memory allocation time.
 Stealing a context into a 'limited' hierarchy properly
 updates memory usage but does *not* cause failure if the
 move causes the new parent to exceed its limits. However
 any further allocation on that hierarchy will then fail.</pre>
<p><code>Parameters:</code></p>
<dl>
<dd><i>ctx</i> The talloc context to set the limit on<br />
 <i>max_size</i> The (new) max_size</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for talloc from the source code.</p>
