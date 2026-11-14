---
title: "globus_common_module(3)"
name: "globus_common_module"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_common_module/"
description: "globus_common.h –"
---

<p>globus_common.h &#8211; </p>
<p> Headers common to all of Globus.</p>
<h2>Synopsis</h2>
<p>#include &#8216;globus_common_include.h&#8217;<br />
 #include &#8216;globus_module.h&#8217;<br />
 #include &#8216;globus_url.h&#8217;<br />
 #include &#8216;globus_list.h&#8217;<br />
 #include &#8216;globus_hashtable.h&#8217;<br />
 #include &#8216;globus_fifo.h&#8217;<br />
 #include &#8216;globus_symboltable.h&#8217;<br />
 #include &#8216;globus_object.h&#8217;<br />
 #include &#8216;globus_object_hierarchy.h&#8217;<br />
 #include &#8216;globus_error.h&#8217;<br />
 #include &#8216;globus_error_hierarchy.h&#8217;<br />
 #include &#8216;globus_thread.h&#8217;<br />
 #include &#8216;globus_time.h&#8217;<br />
 #include &#8216;globus_thread_pool.h&#8217;<br />
 #include &#8216;globus_handle_table.h&#8217;<br />
 #include &#8216;globus_callback.h&#8217;<br />
 #include &#8216;globus_logging.h&#8217;<br />
 #include &#8216;globus_memory.h&#8217;<br />
 #include &#8216;globus_print.h&#8217;<br />
 #include &#8216;globus_tilde_expand.h&#8217;<br />
 #include &#8216;globus_libc.h&#8217;<br />
 #include &#8216;globus_priority_q.h&#8217;<br />
 #include &#8216;globus_range_list.h&#8217;<br />
 #include &#8216;globus_debug.h&#8217;<br />
 #include &#8216;globus_args.h&#8217;<br />
 #include &#8216;globus_strptime.h&#8217;<br />
 #include &#8216;globus_thread_common.h&#8217;<br />
 #include &#8216;globus_thread_rw_mutex.h&#8217;<br />
 #include &#8216;globus_thread_rmutex.h&#8217;<br />
 #include &#8216;globus_error_errno.h&#8217;<br />
 #include &#8216;globus_error_generic.h&#8217;<br />
 #include &#8216;globus_extension.h&#8217;<br />
 #include &#8216;globus_uuid.h&#8217;<br />
 #include &#8216;globus_options.h&#8217;<br />
 #include &#8216;globus_states.h&#8217; </p>
<h3>Macros</h3>
<p>#define <code>GLOBUS_COMMON_MODULE</code> (&amp;globus_i_common_module)<br />
 <i>Globus Common Module Descriptor. </i></p>
<h3>Functions</h3>
<p><code>globus_result_t</code> <code>globus_eval_path</code> (const char *pathstring, char **bufp) </p>
<h2>Detailed Description</h2>
<p>Headers common to all of Globus. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus_common from the source code.</p>
