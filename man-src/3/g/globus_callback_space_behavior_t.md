---
title: "globus_callback_space_behavior_t(3)"
name: "globus_callback_space_behavior_t"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_callback_space_behavior_t/"
description: "Globus Callback Spaces –"
---

<h2 class="name">NAME</h2>
<p> Globus Callback Spaces &#8211; </p>
<h3>Macros</h3>
<p> #define <code>GLOBUS_CALLBACK_GLOBAL_SPACE</code><br />
 <i>Global callback space. </i></p>
<h3>Enumerations</h3>
<p> enum <code>globus_callback_space_behavior_t</code> { <code>GLOBUS_CALLBACK_SPACE_BEHAVIOR_SINGLE</code>, <code>GLOBUS_CALLBACK_SPACE_BEHAVIOR_SERIALIZED</code>, <code>GLOBUS_CALLBACK_SPACE_BEHAVIOR_THREADED</code> }<br />
 <i>Callback space behaviors describe how a space behaves. </i></p>
<h3>Functions</h3>
<p> <code>globus_result_t</code> <code>globus_callback_space_init</code> (<code>globus_callback_space_t</code> *space, <code>globus_callback_space_attr_t</code> attr)<br />
 <i>Initialize a user space. </i><br />
 <code>globus_result_t</code> <code>globus_callback_space_reference</code> (<code>globus_callback_space_t</code> space)<br />
 <i>Take a reference to a space. </i><br />
 <code>globus_result_t</code> <code>globus_callback_space_destroy</code> (<code>globus_callback_space_t</code> space)<br />
 <i>Destroy a reference to a user space. </i><br />
 <code>globus_result_t</code> <code>globus_callback_space_attr_init</code> (<code>globus_callback_space_attr_t</code> *attr)<br />
 <i>Initialize a space attr. </i><br />
 <code>globus_result_t</code> <code>globus_callback_space_attr_destroy</code> (<code>globus_callback_space_attr_t</code> attr)<br />
 <i>Destroy a space attr. </i><br />
 <code>globus_result_t</code> <code>globus_callback_space_attr_set_behavior</code> (<code>globus_callback_space_attr_t</code> attr, <code>globus_callback_space_behavior_t</code> behavior)<br />
 <i>Set the behavior of a space. </i><br />
 <code>globus_result_t</code> <code>globus_callback_space_attr_get_behavior</code> (<code>globus_callback_space_attr_t</code> attr, <code>globus_callback_space_behavior_t</code> *behavior)<br />
 <i>Get the behavior associated with an attr. </i><br />
 <code>globus_result_t</code> <code>globus_callback_space_get</code> (<code>globus_callback_space_t</code> *space)<br />
 <i>Retrieve the space of a currently running callback. </i><br />
 int <code>globus_callback_space_get_depth</code> (<code>globus_callback_space_t</code> space)<br />
 <i>Retrieve the current nesting level of a space. </i><br />
 <code>globus_bool_t</code> <code>globus_callback_space_is_single</code> (<code>globus_callback_space_t</code> space)<br />
 <i>See if the specified space is a single threaded behavior space. </i></p>
<h2>Detailed Description</h2>
<h2>Macro Definition Documentation</h2>
<h3>#define GLOBUS_CALLBACK_GLOBAL_SPACE</h3>
<p> Global callback space. The &#8216;global&#8217; space handle. </p>
<p> This is the default space handle implied if no spaces are explicitly created.</p>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>globus_callback_space_behavior_t</code></h3>
<p> Callback space behaviors describe how a space behaves. In a non-threaded build all spaces exhibit a behavior == _BEHAVIOR_SINGLE. Setting a specific behavior in this case is ignored. </p>
<p> In a threaded build, _BEHAVIOR_SINGLE retains all the rules and behaviors of a non-threaded build while _BEHAVIOR_THREADED makes the space act as the global space. </p>
<p> Setting a space&#8217;s behavior to _BEHAVIOR_SINGLE guarantees that the poll protection will always be there and all callbacks are serialized and only kicked out when polled for. In a threaded build, it is still necessary to poll for callbacks in a _BEHAVIOR_SINGLE space. (<code>globus_cond_wait()</code> will take care of this for you also) </p>
<p> Setting a space&#8217;s behavior to _BEHAVIOR_SERIALIZED guarantees that the poll protection will always be there and all callbacks are serialized. In a threaded build, it is NOT necessary to poll for callbacks in a _BEHAVIOR_SERIALIZED space. Callbacks in this space will be delivered as soon as possible, but only one outstanding (and unblocked) callback will be allowed at any time. </p>
<p> Setting a space&#8217;s behavior to _BEHAVIOR_THREADED allows the user to have the poll protection provided by spaces when built non-threaded, yet, be fully threaded when built threaded (where poll protection is not needed) </p>
<p> <code>Enumerator</code></p>
<dl>
<dt><i>GLOBUS_CALLBACK_SPACE_BEHAVIOR_SINGLE </i></p>
<dd> The default behavior. Indicates that you always want poll protection and single threaded behavior (callbacks need to be explicitly polled for</p>
<dt><i>GLOBUS_CALLBACK_SPACE_BEHAVIOR_SERIALIZED </i></p>
<dd> Indicates that you want poll protection and all callbacks to be serialized (but they do not need to be polled for in a threaded build)</p>
<dt><i>GLOBUS_CALLBACK_SPACE_BEHAVIOR_THREADED </i></p>
<dd> Indicates that you only want poll protection</dl>
<h2>Function Documentation</h2>
<h3><code>globus_result_t</code> globus_callback_space_attr_destroy (<code>globus_callback_space_attr_t</code>attr)</h3>
<p> Destroy a space attr. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> attr to destroy, previously initialized with <code>globus_callback_space_attr_init()</code></dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> GLOBUS_CALLBACK_ERROR_INVALID_ARGUMENT on NULL attr</p>
<dt>&bull;</p>
<dd> GLOBUS_SUCCESS</dl>
</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_callback_space_attr_init()</code></dl>
<h3><code>globus_result_t</code> globus_callback_space_attr_get_behavior (<code>globus_callback_space_attr_t</code>attr, <code>globus_callback_space_behavior_t</code> *behavior)</h3>
<p> Get the behavior associated with an attr. Note: for a non-threaded build, this will always pass back a behavior == GLOBUS_CALLBACK_SPACE_BEHAVIOR_SINGLE. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> attr on which to query behavior<br />
 <i>behavior</i> storage for the behavior</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> GLOBUS_CALLBACK_ERROR_INVALID_ARGUMENT</p>
<dt>&bull;</p>
<dd> GLOBUS_SUCCESS</dl>
</dl>
<h3><code>globus_result_t</code> globus_callback_space_attr_init (<code>globus_callback_space_attr_t</code> *attr)</h3>
<p> Initialize a space attr. Currently, the only attr to set is the behavior. The default behavior associated with this attr is GLOBUS_CALLBACK_SPACE_BEHAVIOR_SINGLE </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> storage for the intialized attr. Must be destroyed with <code>globus_callback_space_attr_destroy()</code></dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> GLOBUS_CALLBACK_ERROR_INVALID_ARGUMENT on NULL attr</p>
<dt>&bull;</p>
<dd> GLOBUS_CALLBACK_ERROR_MEMORY_ALLOC</p>
<dt>&bull;</p>
<dd> GLOBUS_SUCCESS</dl>
</dl>
<h3><code>globus_result_t</code> globus_callback_space_attr_set_behavior (<code>globus_callback_space_attr_t</code>attr, <code>globus_callback_space_behavior_t</code>behavior)</h3>
<p> Set the behavior of a space. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> attr to associate behavior with<br />
 <i>behavior</i> desired behavior</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> GLOBUS_CALLBACK_ERROR_INVALID_ARGUMENT</p>
<dt>&bull;</p>
<dd> GLOBUS_SUCCESS</dl>
</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_callback_space_behavior_t</code></dl>
<h3><code>globus_result_t</code> globus_callback_space_destroy (<code>globus_callback_space_t</code>space)</h3>
<p> Destroy a reference to a user space. This will destroy a reference to a previously initialized space. Space will not actually be destroyed until all callbacks registered with this space have been run and unregistered (if the user has a handle to that callback) AND all references (from <code>globus_callback_space_reference()</code>) have been destroyed. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>space</i> space to destroy, previously initialized by <code>globus_callback_space_init()</code> or referenced with <code>globus_callback_space_reference()</code></dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> GLOBUS_CALLBACK_ERROR_INVALID_SPACE</p>
<dt>&bull;</p>
<dd> GLOBUS_SUCCESS</dl>
</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_callback_space_init()</code> </p>
<p> <code>globus_callback_space_reference()</code></dl>
<h3><code>globus_result_t</code> globus_callback_space_get (<code>globus_callback_space_t</code> *space)</h3>
<p> Retrieve the space of a currently running callback. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>space</i> storage for the handle to the space currently running</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> GLOBUS_CALLBACK_ERROR_INVALID_ARGUMENT on NULL space</p>
<dt>&bull;</p>
<dd> GLOBUS_CALLBACK_ERROR_NO_ACTIVE_CALLBACK</p>
<dt>&bull;</p>
<dd> GLOBUS_SUCCESS</dl>
</dl>
<h3>int globus_callback_space_get_depth (<code>globus_callback_space_t</code>space)</h3>
<p> Retrieve the current nesting level of a space. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>space</i> The space to query.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> the current nesting level</p>
<dt>&bull;</p>
<dd> -1 on invalid space</dl>
</dl>
<h3><code>globus_result_t</code> globus_callback_space_init (<code>globus_callback_space_t</code> *space, <code>globus_callback_space_attr_t</code>attr)</h3>
<p> Initialize a user space. This creates a user space. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>space</i> storage for the initialized space handle. This must be destroyed with <code>globus_callback_space_destroy()</code><br />
 <i>attr</i> a space attr descibing desired behaviors. If GLOBUS_NULL, the default behavior of GLOBUS_CALLBACK_SPACE_BEHAVIOR_SINGLE is assumed. This attr is copied into the space, so it is acceptable to destroy the attr as soon as it is no longer needed</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> GLOBUS_CALLBACK_ERROR_INVALID_ARGUMENT on NULL space</p>
<dt>&bull;</p>
<dd> GLOBUS_CALLBACK_ERROR_MEMORY_ALLOC</p>
<dt>&bull;</p>
<dd> GLOBUS_SUCCESS</dl>
</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_condattr_setspace()</code> </p>
<p> globus_io_attr_set_callback_space()</dl>
<h3><code>globus_bool_t</code> globus_callback_space_is_single (<code>globus_callback_space_t</code>space)</h3>
<p> See if the specified space is a single threaded behavior space. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>space</i> the space to query</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> GLOBUS_TRUE if space&#8217;s behavior is _BEHAVIOR_SINGLE</p>
<dt>&bull;</p>
<dd> GLOBUS_FALSE otherwise</dl>
</dl>
<h3><code>globus_result_t</code> globus_callback_space_reference (<code>globus_callback_space_t</code>space)</h3>
<p> Take a reference to a space. A library which has been &#8216;given&#8217; a space to provide callbacks on would use this to take a reference on the user&#8217;s space. This prevents mayhem should a user destroy a space before the library is done with it. This reference should be destroyed with <code>globus_callback_space_destroy()</code> (think dup()) </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>space</i> space to reference</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> GLOBUS_CALLBACK_ERROR_INVALID_SPACE</p>
<dt>&bull;</p>
<dd> GLOBUS_SUCCESS</dl>
</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_common from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAK">Function Documentation</a></p>
<dd>
<dt><a href="#lbAV">Author</a></p>
<dd></dl>
