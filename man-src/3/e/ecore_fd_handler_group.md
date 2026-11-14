---
title: "ecore_fd_handler_group(3)"
name: "ecore_fd_handler_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_fd_handler_group/"
description: "File Event Handling Functions – Functions that deal with file descriptor handlers."
---

<p>File Event Handling Functions &#8211; Functions that deal with file descriptor handlers. </p>
<h3>Functions</h3>
<p>EAPI <code>Ecore_Fd_Handler</code> * <code>ecore_main_fd_handler_add</code> (int fd, Ecore_Fd_Handler_Flags flags, int(*func)(void *data, <code>Ecore_Fd_Handler</code> *fd_handler), const void *data, int(*buf_func)(void *buf_data, <code>Ecore_Fd_Handler</code> *fd_handler), const void *buf_data)<br />
 <i>Adds a callback for activity on the given file descriptor. </i><br />
 EAPI void * <code>ecore_main_fd_handler_del</code> (<code>Ecore_Fd_Handler</code> *fd_handler)<br />
 <i>Deletes the given FD handler. </i><br />
 EAPI int <code>ecore_main_fd_handler_fd_get</code> (<code>Ecore_Fd_Handler</code> *fd_handler)<br />
 <i>Retrieves the file descriptor that the given handler is handling. </i><br />
 EAPI int <code>ecore_main_fd_handler_active_get</code> (<code>Ecore_Fd_Handler</code> *fd_handler, Ecore_Fd_Handler_Flags flags)<br />
 <i>Return if read, write or error, or a combination thereof, is active on the file descriptor of the given FD handler. </i><br />
 EAPI void <code>ecore_main_fd_handler_active_set</code> (<code>Ecore_Fd_Handler</code> *fd_handler, Ecore_Fd_Handler_Flags flags)<br />
 <i>Set what active streams the given FD handler should be monitoring. </i></p>
<h2>Detailed Description</h2>
<p>Functions that deal with file descriptor handlers.</p>
<h2>Function Documentation</h2>
<h3>EAPI int ecore_main_fd_handler_active_get (<code>Ecore_Fd_Handler</code> * fd_handler, Ecore_Fd_Handler_Flags flags)</h3>
<p>Return if read, write or error, or a combination thereof, is active on the file descriptor of the given FD handler. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>fd_handler</i> The given FD handler.<br />
 <i>flags</i> The flags, ECORE_FD_READ, ECORE_FD_WRITE or ECORE_FD_ERROR to query.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 if any of the given flags are active. 0 otherwise.</dl>
<p> References ECORE_FD_ERROR, ECORE_FD_READ, and ECORE_FD_WRITE.</p>
<h3>EAPI void ecore_main_fd_handler_active_set (<code>Ecore_Fd_Handler</code> * fd_handler, Ecore_Fd_Handler_Flags flags)</h3>
<p>Set what active streams the given FD handler should be monitoring. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>fd_handler</i> The given FD handler.<br />
 <i>flags</i> The flags to be watching.</dl>
<p> Referenced by ecore_con_client_send(), ecore_con_server_send(), ecore_exe_pipe_run(), and ecore_exe_send().</p>
<h3>EAPI <code>Ecore_Fd_Handler</code>* ecore_main_fd_handler_add (int fd, Ecore_Fd_Handler_Flags flags, int(*)(void *data, <code>Ecore_Fd_Handler</code> *fd_handler) func, const void * data, int(*)(void *buf_data, <code>Ecore_Fd_Handler</code> *fd_handler) buf_func, const void * buf_data)</h3>
<p>Adds a callback for activity on the given file descriptor. </p>
<p> func will be called during the execution of <code>ecore_main_loop_begin</code> when the file descriptor is available for reading, or writing, or both. </p>
<p> Normally the return value from the func is &#8216;zero means this handler is finished and can be deleted&#8217; as is usual for handler callbacks. However, if the buf_func is supplied, then the return value from the func is &#8216;non zero means the handler should be called again in a tight loop&#8217;. </p>
<p> buf_func is called during event loop handling to check if data that has been read from the file descriptor is in a buffer and is available to read. Some systems (notably xlib) handle their own buffering, and would otherwise not work with select(). These systems should use a buf_func. This is a most annoying hack, only ecore_x uses it, so refer to that for an example. NOTE &#8211; func should probably return &#8216;one&#8217; always if buf_func is used, to avoid confusion with the other return value semantics. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>fd</i> The file descriptor to watch.<br />
 <i>flags</i> To watch it for read (ECORE_FD_READ) and/or (ECORE_FD_WRITE) write ability. ECORE_FD_ERROR<br />
 <i>func</i> The callback function.<br />
 <i>data</i> The data to pass to the callback.<br />
 <i>buf_func</i> The function to call to check if any data has been buffered and already read from the fd. Can be NULL.<br />
 <i>buf_data</i> The data to pass to the buf_func function.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A fd handler handle if successful. NULL otherwise.</dl>
<p> Referenced by ecore_con_server_add(), ecore_con_server_connect(), ecore_evas_init(), ecore_exe_pipe_run(), and ecore_x_init().</p>
<h3>EAPI void* ecore_main_fd_handler_del (<code>Ecore_Fd_Handler</code> * fd_handler)</h3>
<p>Deletes the given FD handler. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>fd_handler</i> The given FD handler.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The data pointer set using <code>ecore_main_fd_handler_add</code>, for fd_handler on success. NULL otherwise.</dl>
<p> Referenced by ecore_con_client_del(), ecore_con_server_add(), ecore_con_server_connect(), ecore_con_server_del(), ecore_con_url_destroy(), ecore_evas_shutdown(), and ecore_exe_free().</p>
<h3>EAPI int ecore_main_fd_handler_fd_get (<code>Ecore_Fd_Handler</code> * fd_handler)</h3>
<p>Retrieves the file descriptor that the given handler is handling. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>fd_handler</i> The given FD handler.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The file descriptor the handler is watching.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
