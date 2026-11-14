---
title: "globus_xio_net_manager_cntl_t(3)"
name: "globus_xio_net_manager_cntl_t"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_xio_net_manager_cntl_t/"
description: "Globus XIO Net Manager Driver –"
---

<h2 class="name">NAME</h2>
<p> Globus XIO Net Manager Driver &#8211; </p>
<p> Net Manager XIO Driver.</p>
<h3>Enumerations</h3>
<p> enum <code>globus_xio_net_manager_cntl_t</code> { <code>GLOBUS_XIO_NET_MANAGER_SET_TASK_ID</code>, <code>GLOBUS_XIO_NET_MANAGER_GET_TASK_ID</code> } </p>
<h3>Functions</h3>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_NET_MANAGER_SET_TASK_ID</code>, const char *task_id) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_NET_MANAGER_GET_TASK_ID</code>, const char **task_id) </p>
<h2>Detailed Description</h2>
<p> Net Manager XIO Driver. </p>
<p> The Globus XIO Network Manager Driver interfaces with the globus_net_manager library to integrate network manager functionality within the globus_xio network stack. The list of network managers and their options are configured by calling the GLOBUS_XIO_SET_STRING_OPTIONS attr_cntl with a string of attributes. The attribute names &#8216;task-id&#8217;, &#8216;service&#8217;, and &#8216;manager&#8217; are handled by this driver. Other attributes are interpreted as the attributes to pass on the most recently parsed value of the &#8216;manager&#8217; attribute. For example: </p>
<pre><code>
manager = first;
arg = foo;
another - arg = bar;
manager = second;
yet - another = baz
</code></pre>
<p>&nbsp;<wbr>will create a&nbsp;<wbr><code>context&nbsp;<wbr></code>&nbsp;<wbr>containing the network managers&nbsp;<wbr>&#8216;first&#8217;&nbsp;<wbr>and&nbsp;<wbr>&#8216;second&#8217;. It will synthesize&nbsp;<wbr><code>network manager attributes&nbsp;<wbr></code>&nbsp;<wbr>(scope, name, value)&nbsp;<wbr>containing: </p>
<p> (first, arg, foo) </p>
<p> (first, another-arg, bar) </p>
<p> (second, yet-another, baz) </p>
<p> and pass these, along with transport-specific attributes, to the network managers when their functions are called.</p>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>globus_xio_net_manager_cntl_t</code></h3>
<p> doxygen varargs filter stuff Network driver specific cntls </p>
<p> <code>Enumerator</code></p>
<dl>
<dt><i>GLOBUS_XIO_NET_MANAGER_SET_TASK_ID </i></p>
<dd> See usage for: <code>globus_xio_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_NET_MANAGER_GET_TASK_ID </i></p>
<dd> See usage for: <code>globus_xio_attr_cntl </code></dl>
<h2>Function Documentation</h2>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, <code>GLOBUS_XIO_NET_MANAGER_SET_TASK_ID</code>, const char *task_id)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the task id associated with this XIO handle.</p>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, <code>GLOBUS_XIO_NET_MANAGER_GET_TASK_ID</code>, const char **task_id)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the task id associated with this XIO handle.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_net_manager from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAH">Function Documentation</a></p>
<dd>
<dt><a href="#lbAK">Author</a></p>
<dd></dl>
