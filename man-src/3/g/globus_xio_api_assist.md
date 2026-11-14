---
title: "globus_xio_api_assist(3)"
name: "globus_xio_api_assist"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_xio_api_assist/"
description: "XIO Examples – Help understanding the globus_xio api."
---

<p>XIO Examples &#8211; Help understanding the globus_xio api. </p>
<h2>Stack Construction</h2>
<p>The driver stack that is used for a given XIO handle is constructed using a globus_xio_stack_t. Each driver is loaded by name and pushed onto a stack. </p>
<p> Stack setup example: </p>
<pre>// First load the drivers
globus_xio_driver_load(&quot;tcp&quot;, &amp;tcp_driver);
globus_xio_driver_load(&quot;gsi&quot;, &amp;gsi_driver);
//build the stack
globus_xio_stack_init(&amp;stack);
globus_xio_stack_push_driver(stack, tcp_driver, NULL);
globus_xio_stack_push_driver(stack, gsi_driver, NULL);</pre>
<h2>Servers</h2>
<p>A server data structure provides functionality for passive opens. A server is initialized and bound to a protocol stack and set of attributes with the function <code>globus_xio_server_create()</code>. Once a server is created many &#8216;connections&#8217; can be accepted. Each connection will result in an intialized handle which can later be opened. </p>
<pre>globus_xio_server_t server;
globus_xio_attr_t attr;
globus_xio_attr_init(&amp;attr);
globus_xio_server_create(&amp;server_handle, attr, stack); 
globus_xio_server_accept(&amp;handle, server);</pre>
<h2>Handle Construction</h2>
<p>There are two ways to create a handle. The first is for use as a client (one that is doing an active open). The function: <code>globus_xio_handle_create()</code> is used to create such a handle and bind that handle to a protocol stack. </p>
<pre>globus_xio_handle_create(&amp;handle, stack);</pre>
<p>The second means of creating a handle is for use as a server (one that is doing a passive open). This is created by accepting a connection on a server_handle with the function <code>globus_xio_server_accept()</code> or <code>globus_xio_server_register_accept()</code>. </p>
<p> Mutable attrs can be altered via a call to <code>globus_xio_handle_cntl()</code> described later. </p>
<pre>globus_xio_server_accept(&amp;xio_handle, server_handle);</pre>
<p>once a handle is initialized the user can call <code>globus_xio_open()</code> to begin the open process.</p>
<h2>Timeouts</h2>
<p>A user can set a timeout value for any I/O operation. Each I/O operation (open close read write) can have its own timeout value. If no timeout is set the operation will be allowed to infinitely block. </p>
<p> When time expires the outstanding operation is canceled. If the timeout callback for the given operation is not NULL it is called first to notify the user that the operation timed out and give the user a chance to ignore that timeout. If canceled, the user will get the callback they registered for the operation as well, but it will come with an error indicating that it has been canceled. </p>
<p> It is possible that part of an I/O operation will complete before the timeout expires. In this case the operation can still be canceled. The user will receive there IO callback with and error set and the length value appropriately set to indicate how much of the operation completed. </p>
<p> Timeouts are registered by using the following handle_cntl values: </p>
<dl COMPACT>
<dt>&bull;</p>
<dd>GLOBUS_XIO_ATTR_SET_TIMEOUT_ALL</p>
<dt>&bull;</p>
<dd>GLOBUS_XIO_ATTR_SET_TIMEOUT_OPEN</p>
<dt>&bull;</p>
<dd>GLOBUS_XIO_ATTR_SET_TIMEOUT_CLOSE</p>
<dt>&bull;</p>
<dd>GLOBUS_XIO_ATTR_SET_TIMEOUT_READ</p>
<dt>&bull;</p>
<dd>GLOBUS_XIO_ATTR_SET_TIMEOUT_WRITE</p>
<dt>&bull;</p>
<dd>GLOBUS_XIO_ATTR_SET_TIMEOUT_ACCEPT</dl>
<p> Each of these cntls expect three parameters: </p>
<dl COMPACT>
<dt>&bull;</p>
<dd>globus_xio_timeout_callback_t callback_function</p>
<dt>&bull;</p>
<dd>globus_reltime_t * delay_time</p>
<dt>&bull;</p>
<dd>void * callback_arg</dl>
<h2>Data Descriptor</h2>
<p>The data descriptor ADT gives the user a means of attaching/extracting meta data to a read or write operation. </p>
<p>&nbsp;<wbr>Things like offset, out of band message, and other driver specific meta data are contained in the data descriptor. </p>
<p>&nbsp;<wbr>Data descriptors are passed to globus_xio in&nbsp;<wbr><code>globus_xio_read()</code>&nbsp;<wbr>and&nbsp;<wbr><code>globus_xio_write()</code>. Within the globus_xio framework it is acceptable to pass NULL instead of a valid data_descriptor, </p>
<p> Example: </p>
<pre>globus_xio_data_descriptor_init(&amp;desc);
globus_xio_data_descriptor_cntl(desc, 
 tcp_driver,
 GLOBUS_XIO_TCP_SET_SEND_FLAGS,
 GLOBUS_XIO_TCP_SEND_OOB);</pre>
<h2>User Attributes</h2>
<p>Globus XIO uses a single attribute object for all of its functions. Attributes give the user an extensible mechanism to alter default values which control parameters in an operation. </p>
<p> In most of the Globus XIO user API functions a user passes an attribute as a parameter. In many cases the user may ignore the attribute parameter and just pass in NULL. However at times the user will wish to tweak the operation. The attribute structure is used for this tweaking. </p>
<p> There are only three attribute functions. <code>globus_xio_attr_init</code> <code>globus_xio_attr_cntl</code> and <code>globus_xio_attr_destroy</code>. The init and destroy functions are very simple and require little explanation. Before an attribute can be used it must be initialized, and to clean up all memory associated with it the user must call destroy on it. </p>
<p> The function <code>globus_xio_attr_cntl</code> manipulates values in the attribute. For more info on it see <code>globus_xio_attr_cntl</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus_xio from the source code.</p>
