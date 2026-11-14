---
title: "tcl_setchannelerror(3)"
name: "tcl_setchannelerror"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_setchannelerror/"
description: "Tcl_SetChannelError, Tcl_SetChannelErrorInterp, Tcl_GetChannelError, Tcl_GetChannelErrorInterp – functions to create/intercept Tcl errors by channel drivers."
---

<p>Tcl_SetChannelError, Tcl_SetChannelErrorInterp, Tcl_GetChannelError, Tcl_GetChannelErrorInterp &#8211; functions to create/intercept Tcl errors by channel drivers. </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
void
<code>Tcl_SetChannelError</code>(<i>chan, msg</i>)
void
<code>Tcl_SetChannelErrorInterp</code>(<i>interp, msg</i>)
void
<code>Tcl_GetChannelError</code>(<i>chan, msgPtr</i>)
void
<code>Tcl_GetChannelErrorInterp</code>(<i>interp, msgPtr</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Channel <i>chan</i> (in) Refers to the Tcl channel whose bypass area is accessed.</p>
<dd>Tcl_Interp* <i>interp</i> (in) Refers to the Tcl interpreter whose bypass area is accessed.</p>
<dd>Tcl_Obj* <i>msg</i> (in) Error message put into a bypass area. A list of return options and values, followed by a string message. Both message and the option/value information are optional.</p>
<dd>Tcl_Obj** <i>msgPtr</i> (out) Reference to a place where the message stored in the accessed bypass area can be stored in.
</dl>
<h2>Description</h2>
<p>The current definition of a Tcl channel driver does not permit the direct return of arbitrary error messages, except for the setting and retrieval of channel options. All other functions are restricted to POSIX error codes. </p>
<p> The functions described here overcome this limitation. Channel drivers are allowed to use <code>Tcl_SetChannelError</code> and <code>Tcl_SetChannelErrorInterp</code> to place arbitrary error messages in <code>bypass areas</code><i> defined for channels and interpreters. And the generic I/O layer uses </i><code>Tcl_GetChannelError</code> and <code>Tcl_GetChannelErrorInterp</code> to look for messages in the bypass areas and arrange for their return as errors. The posix error codes set by a driver are used now if and only if no messages are present. </p>
<p> <code>Tcl_SetChannelError</code> stores error information in the bypass area of the specified channel. The number of references to the <code>msg</code> object goes up by one. Previously stored information will be discarded, by releasing the reference held by the channel. The channel reference must not be NULL. </p>
<p> <code>Tcl_SetChannelErrorInterp</code> stores error information in the bypass area of the specified interpreter. The number of references to the <code>msg</code> object goes up by one. Previously stored information will be discarded, by releasing the reference held by the interpreter. The interpreter reference must not be NULL. </p>
<p> <code>Tcl_GetChannelError</code> places either the error message held in the bypass area of the specified channel into <i>msgPtr</i>, or NULL; and resets the bypass. I.e. after an invocation all following invocations will return NULL, until an intervening invocation of <code>Tcl_SetChannelError</code> with a non-NULL message. The <i>msgPtr</i> must not be NULL. The reference count of the message is not touched. The reference previously held by the channel is now held by the caller of the function and it is its responsibility to release that reference when it is done with the object. </p>
<p> <code>Tcl_GetChannelErrorInterp</code> places either the error message held in the bypass area of the specified interpreter into <i>msgPtr</i>, or NULL; and resets the bypass. I.e. after an invocation all following invocations will return NULL, until an intervening invocation of <code>Tcl_SetChannelErrorInterp</code> with a non-NULL message. The <i>msgPtr</i> must not be NULL. The reference count of the message is not touched. The reference previously held by the interpreter is now held by the caller of the function and it is its responsibility to release that reference when it is done with the object. </p>
<p> Which functions of a channel driver are allowed to use which bypass function is listed below, as is which functions of the public channel API may leave a messages in the bypass areas. </p>
<dl COMPACT>
<dt><code>Tcl_DriverCloseProc</code></p>
<dd>May use <code>Tcl_SetChannelErrorInterp</code>, and only this function.</p>
<dt><code>Tcl_DriverInputProc</code></p>
<dd>May use <code>Tcl_SetChannelError</code>, and only this function.</p>
<dt><code>Tcl_DriverOutputProc</code></p>
<dd>May use <code>Tcl_SetChannelError</code>, and only this function.</p>
<dt><code>Tcl_DriverSeekProc</code></p>
<dd>May use <code>Tcl_SetChannelError</code>, and only this function.</p>
<dt><code>Tcl_DriverWideSeekProc</code></p>
<dd>May use <code>Tcl_SetChannelError</code>, and only this function.</p>
<dt><code>Tcl_DriverSetOptionProc</code></p>
<dd>Has already the ability to pass arbitrary error messages. Must <code>not</code> use any of the new functions.</p>
<dt><code>Tcl_DriverGetOptionProc</code></p>
<dd>Has already the ability to pass arbitrary error messages. Must <code>not</code> use any of the new functions.</p>
<dt><code>Tcl_DriverWatchProc</code></p>
<dd>Must <code>not</code> use any of the new functions. Is internally called and has no ability to return any type of error whatsoever.</p>
<dt><code>Tcl_DriverBlockModeProc</code></p>
<dd>May use <code>Tcl_SetChannelError</code>, and only this function.</p>
<dt><code>Tcl_DriverGetHandleProc</code></p>
<dd>Must <code>not</code> use any of the new functions. It is only a low-level function, and not used by Tcl commands.</p>
<dt><code>Tcl_DriverHandlerProc</code></p>
<dd>Must <code>not</code> use any of the new functions. Is internally called and has no ability to return any type of error whatsoever.</dl>
<p> Given the information above the following public functions of the Tcl C API are affected by these changes. I.e. when these functions are called the channel may now contain a stored arbitrary error message requiring processing by the caller. </p>
<dl COMPACT>
<dt><code>Tcl_StackChannel</code></p>
<dd>
<dt><code>Tcl_Seek</code></p>
<dd>
<dt><code>Tcl_Tell</code></p>
<dd>
<dt><code>Tcl_ReadRaw</code></p>
<dd>
<dt><code>Tcl_Read</code></p>
<dd>
<dt><code>Tcl_ReadChars</code></p>
<dd>
<dt><code>Tcl_Gets</code></p>
<dd>
<dt><code>Tcl_GetsObj</code></p>
<dd>
<dt><code>Tcl_Flush</code></p>
<dd>
<dt><code>Tcl_WriteRaw</code></p>
<dd>
<dt><code>Tcl_WriteObj</code></p>
<dd>
<dt><code>Tcl_Write</code></p>
<dd>
<dt><code>Tcl_WriteChars</code></p>
<dd></dl>
<p> All other API functions are unchanged. Especially the functions below leave all their error information in the interpreter result. </p>
<dl COMPACT>
<dt><code>Tcl_Close</code></p>
<dd>
<dt><code>Tcl_UnregisterChannel</code></p>
<dd>
<dt><code>Tcl_UnstackChannel</code></p>
<dd></dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-tcl_close/">Tcl_Close</a>(3), <a href="/docs/linux/man/3-tcl_openfilechannel/">Tcl_OpenFileChannel</a>(3), <a href="/docs/linux/man/3-tcl_seterrno/">Tcl_SetErrno</a>(3) </p>
<h2>Keywords</h2>
<p>channel driver, error messages, channel type</p>
