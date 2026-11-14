---
title: "brlapi_errlist(3)"
name: "brlapi_errlist"
section: "3"
letter: "b"
url: "/docs/linux/man/3-brlapi_errlist/"
description: "Error handling –"
---

<h2 class="name">NAME</h2>
<p> Error handling &#8211; </p>
<p> How to handle errors.</p>
<h3>Data Structures</h3>
<p> struct <code>brlapi_error_t</code> </p>
<h3>Macros</h3>
<p> #define <code>BRLAPI_ERROR_SUCCESS</code> 0 </p>
<p> #define <code>BRLAPI_ERROR_NOMEM</code> 1 </p>
<p> #define <code>BRLAPI_ERROR_TTYBUSY</code> 2 </p>
<p> #define <code>BRLAPI_ERROR_DEVICEBUSY</code> 3 </p>
<p> #define <code>BRLAPI_ERROR_UNKNOWN_INSTRUCTION</code> 4 </p>
<p> #define <code>BRLAPI_ERROR_ILLEGAL_INSTRUCTION</code> 5 </p>
<p> #define <code>BRLAPI_ERROR_INVALID_PARAMETER</code> 6 </p>
<p> #define <code>BRLAPI_ERROR_INVALID_PACKET</code> 7 </p>
<p> #define <code>BRLAPI_ERROR_CONNREFUSED</code> 8 </p>
<p> #define <code>BRLAPI_ERROR_OPNOTSUPP</code> 9 </p>
<p> #define <code>BRLAPI_ERROR_GAIERR</code> 10 </p>
<p> #define <code>BRLAPI_ERROR_LIBCERR</code> 11 </p>
<p> #define <code>BRLAPI_ERROR_UNKNOWNTTY</code> 12 </p>
<p> #define <code>BRLAPI_ERROR_PROTOCOL_VERSION</code> 13 </p>
<p> #define <code>BRLAPI_ERROR_EOF</code> 14 </p>
<p> #define <code>BRLAPI_ERROR_EMPTYKEY</code> 15 </p>
<p> #define <code>BRLAPI_ERROR_DRIVERERROR</code> 16 </p>
<p> #define <code>BRLAPI_ERROR_AUTHENTICATION</code> 17 </p>
<p> #define <code>brlapi_error</code> (*<code>brlapi_error_location</code>()) </p>
<p> #define <code>brlapi_errno</code> (brlapi_error.brlerrno) </p>
<p> #define <code>brlapi_libcerrno</code> (brlapi_error.libcerrno) </p>
<p> #define <code>brlapi_gaierrno</code> (brlapi_error.gaierrno) </p>
<p> #define <code>brlapi_errfun</code> (brlapi_error.errfun) </p>
<h3>Typedefs</h3>
<p> typedef uint32_t <code>brlapi_packetType_t</code> </p>
<p> typedef void(<code>BRLAPI_STDCALL</code> * <code>brlapi_exceptionHandler_t</code> )(int error, <code>brlapi_packetType_t</code> type, const void *packet, size_t size) </p>
<p> typedef void(<code>BRLAPI_STDCALL</code> * <code>brlapi__exceptionHandler_t</code> )(<code>brlapi_handle_t</code> *handle, int error, <code>brlapi_packetType_t</code> type, const void *packet, size_t size) </p>
<h3>Functions</h3>
<p> void <code>BRLAPI_STDCALL</code> <code>brlapi_perror</code> (const char *s) </p>
<p> <code>brlapi_error_t</code> *<code>BRLAPI_STDCALL</code> <code>brlapi_error_location</code> (void) </p>
<p> const char *<code>BRLAPI_STDCALL</code> <code>brlapi_strerror</code> (const <code>brlapi_error_t</code> *error) </p>
<p> const char *<code>BRLAPI_STDCALL</code> <code>brlapi_getPacketTypeName</code> (<code>brlapi_packetType_t</code> type) </p>
<p> int <code>BRLAPI_STDCALL</code> <code>brlapi_strexception</code> (char *buffer, size_t bufferSize, int error, <code>brlapi_packetType_t</code> type, const void *packet, size_t packetSize) </p>
<p> int <code>BRLAPI_STDCALL</code> <code>brlapi__strexception</code> (<code>brlapi_handle_t</code> *handle, char *buffer, size_t bufferSize, int error, <code>brlapi_packetType_t</code> type, const void *packet, size_t packetSize) </p>
<p> <code>brlapi_exceptionHandler_t</code><br />
 <code>BRLAPI_STDCALL</code> <code>brlapi_setExceptionHandler</code> (<code>brlapi_exceptionHandler_t</code> handler)&quot; </p>
<p> <code>brlapi__exceptionHandler_t</code><br />
 <code>BRLAPI_STDCALL</code> <code>brlapi__setExceptionHandler</code> (<code>brlapi_handle_t</code> *handle, <code>brlapi__exceptionHandler_t</code> handler)&quot; </p>
<p> void <code>BRLAPI_STDCALL</code> <code>brlapi_defaultExceptionHandler</code> (int error, <code>brlapi_packetType_t</code> type, const void *packet, size_t size) </p>
<p> void <code>BRLAPI_STDCALL</code> <code>brlapi__defaultExceptionHandler</code> (<code>brlapi_handle_t</code> *handle, int error, <code>brlapi_packetType_t</code> type, const void *packet, size_t size) </p>
<h3>Variables</h3>
<p> const char * <code>brlapi_errlist</code> [] </p>
<p> const int <code>brlapi_nerr</code> </p>
<p> <code>brlapi_error_t</code> <code>brlapi_error</code> </p>
<p> int <code>brlapi_errno</code> </p>
<p> int <code>brlapi_libcerrno</code> </p>
<p> int <code>brlapi_gaierrno</code> </p>
<p> const char * <code>brlapi_errfun</code> </p>
<h2>Detailed Description</h2>
<p> When a function fails, <code>brlapi_errno</code> will hold an error code to explain why it failed. It should always be reported somehow. </p>
<p> Although most errors are reported that way, some (called exceptions) are reported asynchronously for efficiency reasons, because they always just report a programming error. The affected functions are: brlapi_setFocus, brlapi_write* and brlapi_sendRaw. When they happen, the next call to brlapi_something will close the connection and call the <i>exception</i> handler. If the exception handler returns, the brlapi_something function will return an end-of-file error. </p>
<p> The default exception handler (<code>brlapi_defaultExceptionHandler()</code>) dumps the guilty packet before abort()ing. It can be replaced by calling <code>brlapi_setExceptionHandler()</code>. For instance, the Java and Python bindings use this for raising a Java or Python exception that may be caught.</p>
<h2>Macro Definition Documentation</h2>
<h3>#define brlapi_errfun (brlapi_error.errfun)</h3>
<p> Cheat about the brlapi_errfun C token</p>
<h3>#define brlapi_errno (brlapi_error.brlerrno)</h3>
<p> Cheat about the brlapi_errno C token</p>
<h3>#define brlapi_error (*<code>brlapi_error_location</code>())</h3>
<p> Cheat about the brlapi_error C token</p>
<h3>#define BRLAPI_ERROR_AUTHENTICATION 17</h3>
<p> Authentication failed</p>
<h3>#define BRLAPI_ERROR_CONNREFUSED 8</h3>
<p> Connection refused</p>
<h3>#define BRLAPI_ERROR_DEVICEBUSY 3</h3>
<p> A connection is already using RAW or suspend mode</p>
<h3>#define BRLAPI_ERROR_DRIVERERROR 16</h3>
<p> Packet returned by driver too large</p>
<h3>#define BRLAPI_ERROR_EMPTYKEY 15</h3>
<p> Key file empty</p>
<h3>#define BRLAPI_ERROR_EOF 14</h3>
<p> Unexpected end of file</p>
<h3>#define BRLAPI_ERROR_GAIERR 10</h3>
<p> Getaddrinfo error</p>
<h3>#define BRLAPI_ERROR_ILLEGAL_INSTRUCTION 5</h3>
<p> Forbiden in current mode</p>
<h3>#define BRLAPI_ERROR_INVALID_PACKET 7</h3>
<p> Invalid size</p>
<h3>#define BRLAPI_ERROR_INVALID_PARAMETER 6</h3>
<p> Out of range or have no sense</p>
<h3>#define BRLAPI_ERROR_LIBCERR 11</h3>
<p> Libc error</p>
<h3>#define BRLAPI_ERROR_NOMEM 1</h3>
<p> Not enough memory</p>
<h3>#define BRLAPI_ERROR_OPNOTSUPP 9</h3>
<p> Operation not supported</p>
<h3>#define BRLAPI_ERROR_PROTOCOL_VERSION 13</h3>
<p> Bad protocol version</p>
<h3>#define BRLAPI_ERROR_SUCCESS 0</h3>
<p> Success</p>
<h3>#define BRLAPI_ERROR_TTYBUSY 2</h3>
<p> A connection is already running in this tty</p>
<h3>#define BRLAPI_ERROR_UNKNOWN_INSTRUCTION 4</h3>
<p> Not implemented in protocol</p>
<h3>#define BRLAPI_ERROR_UNKNOWNTTY 12</h3>
<p> Couldn&#8217;t find out the tty number</p>
<h3>#define brlapi_gaierrno (brlapi_error.gaierrno)</h3>
<p> Cheat about the brlapi_gaierrno C token</p>
<h3>#define brlapi_libcerrno (brlapi_error.libcerrno)</h3>
<p> Cheat about the brlapi_libcerrno C token</p>
<h2>Typedef Documentation</h2>
<h3>typedef void(<code>BRLAPI_STDCALL</code> * brlapi__exceptionHandler_t)(<code>brlapi_handle_t</code> *handle, int error, <code>brlapi_packetType_t</code> type, const void *packet, size_t size)</h3>
<h3>typedef void(<code>BRLAPI_STDCALL</code> * brlapi_exceptionHandler_t)(int error, <code>brlapi_packetType_t</code> type, const void *packet, size_t size)</h3>
<p> Types for exception handlers </p>
<p> Types of exception handlers which are to be given to <code>brlapi_setExceptionHandler()</code> and <code>brlapi__setExceptionHandler()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> is the handle corresponding to the guilty connection;<br />
 <i>error</i> is a BRLAPI_ERROR_ error code;<br />
 <i>type</i> is the type of the guilty packet;<br />
 <i>packet</i> points to the content of the guilty packet (might be a little bit truncated);<br />
 <i>size</i> gives the guilty packet&#8217;s size.</dl>
<h3>typedef uint32_t <code>brlapi_packetType_t</code></h3>
<p> Type for packet type. Only unsigned can cross networks, 32bits</p>
<h2>Function Documentation</h2>
<h3>void <code>BRLAPI_STDCALL</code> brlapi__defaultExceptionHandler (<code>brlapi_handle_t</code> *handle, interror, <code>brlapi_packetType_t</code>type, const void *packet, size_tsize)</h3>
<h3><code>brlapi__exceptionHandler_t</code> <code>BRLAPI_STDCALL</code> brlapi__setExceptionHandler (<code>brlapi_handle_t</code> *handle, <code>brlapi__exceptionHandler_t</code>handler)</h3>
<h3>int <code>BRLAPI_STDCALL</code> brlapi__strexception (<code>brlapi_handle_t</code> *handle, char *buffer, size_tbufferSize, interror, <code>brlapi_packetType_t</code>type, const void *packet, size_tpacketSize)</h3>
<h3>void <code>BRLAPI_STDCALL</code> brlapi_defaultExceptionHandler (interror, <code>brlapi_packetType_t</code>type, const void *packet, size_tsize)</h3>
<h3><code>brlapi_error_t</code>* <code>BRLAPI_STDCALL</code> brlapi_error_location (void)</h3>
<p> Get per-thread error location </p>
<p> In multithreaded software, <code>brlapi_error</code> is thread-specific, so api.h cheats about the brlapi_error token and actually calls <code>brlapi_error_location()</code>. </p>
<p> This gets the thread specific location of global variable <code>brlapi_error</code></p>
<h3>const char* <code>BRLAPI_STDCALL</code> brlapi_getPacketTypeName (<code>brlapi_packetType_t</code>type)</h3>
<p> Get plain packet type </p>
<p> <code>brlapi_getPacketTypeName()</code> returns the plain packet type name corresponding to its argument.</p>
<h3>void <code>BRLAPI_STDCALL</code> brlapi_perror (const char *s)</h3>
<p> Print a BrlAPI error message </p>
<p> <code>brlapi_perror()</code> reads <code>brlapi_error</code>, and acts just like perror().</p>
<h3><code>brlapi_exceptionHandler_t</code> <code>BRLAPI_STDCALL</code> brlapi_setExceptionHandler (<code>brlapi_exceptionHandler_t</code>handler)</h3>
<p> Set a new exception handler </p>
<p> <code>brlapi_setExceptionHandler()</code> replaces the previous exception handler with the handler parameter. The previous exception handler is returned to make chaining error handlers possible. </p>
<p> The default handler just prints the exception and abort()s.</p>
<h3>const char* <code>BRLAPI_STDCALL</code> brlapi_strerror (const <code>brlapi_error_t</code> *error)</h3>
<p> Get plain error message </p>
<p> <code>brlapi_strerror()</code> returns the plain error message corresponding to its argument.</p>
<h3>int <code>BRLAPI_STDCALL</code> brlapi_strexception (char *buffer, size_tbufferSize, interror, <code>brlapi_packetType_t</code>type, const void *packet, size_tpacketSize)</h3>
<p> Describes an exception </p>
<p> <code>brlapi_strexception()</code> puts a text describing the given exception in buffer. </p>
<p> The beginning of the guilty packet is dumped as a sequence of hex bytes. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> the size of the text describing the exception, following snprintf()&#8217;s semantics.</dl>
<h2>Variable Documentation</h2>
<h3>const char* brlapi_errfun</h3>
<p> Shorthand for brlapi_error.errfun</p>
<h3>const char* brlapi_errlist[]</h3>
<p> Error message list </p>
<p> These are the string constants used by <code>brlapi_perror()</code>.</p>
<h3>int brlapi_errno</h3>
<p> Shorthand for brlapi_error.errno</p>
<h3><code>brlapi_error_t</code> brlapi_error</h3>
<p> Global variable brlapi_error </p>
<p> <code>brlapi_error</code> is a global left-value containing the last error information. Its errno field is not reset to BRLAPI_ERROR_SUCCESS on success. </p>
<p> This information may be copied in <code>brlapi_error_t</code> variables for later use with the brlapi_strerror function.</p>
<h3>int brlapi_gaierrno</h3>
<p> Shorthand for brlapi_error.gaierrno</p>
<h3>int brlapi_libcerrno</h3>
<p> Shorthand for brlapi_error.libcerrno</p>
<h3>const int brlapi_nerr</h3>
<p> Number of error messages</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for BrlAPI from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbBG">Typedef Documentation</a></p>
<dd>
<dt><a href="#lbBK">Function Documentation</a></p>
<dd>
<dt><a href="#lbBV">Variable Documentation</a></p>
<dd>
<dt><a href="#lbCD">Author</a></p>
<dd></dl>
