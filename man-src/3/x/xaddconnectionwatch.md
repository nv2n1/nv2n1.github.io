---
title: "xaddconnectionwatch(3)"
name: "xaddconnectionwatch"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xaddconnectionwatch/"
description: "XAddConnectionWatch, XRemoveConnectionWatch, XProcessInternalConnection, XInternalConnectionNumbers – handle Xlib internal connections"
---

<p>XAddConnectionWatch, XRemoveConnectionWatch, XProcessInternalConnection, XInternalConnectionNumbers &#8211; handle Xlib internal connections </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>typedef void (*XConnectionWatchProc)(Display *<i>display</i>, XPointer <i>client_data</i>, int <i>fd</i>, Bool <i>opening</i>, XPointer *<i>watch_data</i>);</p>
<dd>Status XAddConnectionWatch(Display *<i>display</i>, XWatchProc <i>procedure</i>, XPointer <i>client_data</i>);</p>
<dd>Status XRemoveConnectionWatch(Display *<i>display</i>, XWatchProc <i>procedure</i>, XPointer <i>client_data</i>);</p>
<dd>void XProcessInternalConnection(Display *<i>display</i>, int <i>fd</i>);</p>
<dd>Status XInternalConnectionNumbers(Display *<i>display</i>, int **<i>fd_return</i>, int *<i>count_return</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>client_data</i></p>
<dd>Specifies the additional client data.</p>
<dt><i>count_return</i></p>
<dd>Returns the number of file descriptors.</p>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>fd</i></p>
<dd>Specifies the file descriptor.</p>
<dt><i>fd_return</i></p>
<dd>Returns the file descriptors.</p>
<dt><i>procedure</i></p>
<dd>Specifies the procedure to be called.</dl>
<h2>Description</h2>
<p>The <code>XAddConnectionWatch</code> function registers a procedure to be called each time Xlib opens or closes an internal connection for the specified display. The procedure is passed the display, the specified client_data, the file descriptor for the connection, a Boolean indicating whether the connection is being opened or closed, and a pointer to a location for private watch data. If opening is <code>True</code>, the procedure can store a pointer to private data in the location pointed to by watch_data; when the procedure is later called for this same connection and opening is <code>False</code>, the location pointed to by watch_data will hold this same private data pointer. </p>
<p> This function can be called at any time after a display is opened. If internal connections already exist, the registered procedure will immediately be called for each of them, before <code>XAddConnectionWatch</code> returns. <code>XAddConnectionWatch</code> returns a nonzero status if the procedure is successfully registered; otherwise, it returns zero. </p>
<p> The registered procedure should not call any Xlib functions. If the procedure directly or indirectly causes the state of internal connections or watch procedures to change, the result is not defined. If Xlib has been initialized for threads, the procedure is called with the display locked and the result of a call by the procedure to any Xlib function that locks the display is not defined unless the executing thread has externally locked the display using <code>XLockDisplay</code>. </p>
<p> The <code>XRemoveConnectionWatch</code> function removes a previously registered connection watch procedure. The client_data must match the client_data used when the procedure was initially registered. </p>
<p> The <code>XProcessInternalConnection</code> function processes input available on an internal connection. This function should be called for an internal connection only after an operating system facility (for example, <code>select</code> or <code>poll</code>) has indicated that input is available; otherwise, the effect is not defined. </p>
<p> The <code>XInternalConnectionNumbers</code> function returns a list of the file descriptors for all internal connections currently open for the specified display. When the allocated list is no longer needed, free it by using <code>XFree</code>. This functions returns a nonzero status if the list is successfully allocated; otherwise, it returns zero.</p>
<h2>See Also</h2>
<p><i>Xlib &#8211; C Language X Interface</i></p>
