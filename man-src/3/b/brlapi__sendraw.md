---
title: "brlapi__sendraw(3)"
name: "brlapi__sendraw"
section: "3"
letter: "b"
url: "/docs/linux/man/3-brlapi__sendraw/"
description: "Driver-Specific modes –"
---

<p>Driver-Specific modes &#8211; </p>
<p> Raw and Suspend Modes mechanism.</p>
<h3>Functions</h3>
<p>int <code>BRLAPI_STDCALL</code> <code>brlapi_enterRawMode</code> (const char *driver) </p>
<p> int <code>BRLAPI_STDCALL</code> <code>brlapi__enterRawMode</code> (<code>brlapi_handle_t</code> *handle, const char *driver) </p>
<p> int <code>BRLAPI_STDCALL</code> <code>brlapi_leaveRawMode</code> (void) </p>
<p> int <code>BRLAPI_STDCALL</code> <code>brlapi__leaveRawMode</code> (<code>brlapi_handle_t</code> *handle) </p>
<p> ssize_t <code>BRLAPI_STDCALL</code> <code>brlapi_sendRaw</code> (const void *buffer, size_t size) </p>
<p> ssize_t <code>BRLAPI_STDCALL</code> <code>brlapi__sendRaw</code> (<code>brlapi_handle_t</code> *handle, const void *buffer, size_t size) </p>
<p> ssize_t <code>BRLAPI_STDCALL</code> <code>brlapi_recvRaw</code> (void *buffer, size_t size) </p>
<p> ssize_t <code>BRLAPI_STDCALL</code> <code>brlapi__recvRaw</code> (<code>brlapi_handle_t</code> *handle, void *buffer, size_t size) </p>
<p> int <code>BRLAPI_STDCALL</code> <code>brlapi_suspendDriver</code> (const char *driver) </p>
<p> int <code>BRLAPI_STDCALL</code> <code>brlapi__suspendDriver</code> (<code>brlapi_handle_t</code> *handle, const char *driver) </p>
<p> int <code>BRLAPI_STDCALL</code> <code>brlapi_resumeDriver</code> (void) </p>
<p> int <code>BRLAPI_STDCALL</code> <code>brlapi__resumeDriver</code> (<code>brlapi_handle_t</code> *handle) </p>
<h2>Detailed Description</h2>
<p>If the application wants to directly talk to the braille terminal, it should use Raw Mode. In this special mode, the driver gives the whole control of the terminal to it: <i>brltty</i> doesn&#8217;t work any more. </p>
<p> For this, it simply has to call <code>brlapi_enterRawMode()</code>, then <code>brlapi_sendRaw()</code> and <code>brlapi_recvRaw()</code>, and finally give control back thanks to <code>brlapi_leaveRawMode()</code>. </p>
<p> Special care of the terminal should be taken, since one might completely trash the terminal&#8217;s data, or even lock it! The application should always check for terminal&#8217;s type thanks to <code>brlapi_getDriverName()</code>. </p>
<p> The client can also make brltty close the driver by using <code>brlapi_suspendDriver()</code>, and resume it again with <code>brlapi_resumeDriver()</code>. This should not be used if possible: raw mode should be sufficient for any use. If not, please ask for features :)</p>
<h2>Function Documentation</h2>
<h3>int <code>BRLAPI_STDCALL</code> brlapi__enterRawMode (<code>brlapi_handle_t</code> *handle, const char *driver)</h3>
<h3>int <code>BRLAPI_STDCALL</code> brlapi__leaveRawMode (<code>brlapi_handle_t</code> *handle)</h3>
<h3>ssize_t <code>BRLAPI_STDCALL</code> brlapi__recvRaw (<code>brlapi_handle_t</code> *handle, void *buffer, size_tsize)</h3>
<h3>int <code>BRLAPI_STDCALL</code> brlapi__resumeDriver (<code>brlapi_handle_t</code> *handle)</h3>
<h3>ssize_t <code>BRLAPI_STDCALL</code> brlapi__sendRaw (<code>brlapi_handle_t</code> *handle, const void *buffer, size_tsize)</h3>
<h3>int <code>BRLAPI_STDCALL</code> brlapi__suspendDriver (<code>brlapi_handle_t</code> *handle, const char *driver)</h3>
<h3>int <code>BRLAPI_STDCALL</code> brlapi_enterRawMode (const char *driver)</h3>
<p>Switch to Raw mode </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>driver</i> Specifies the name of the driver for which the raw communication will be established.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, -1 on error</dl>
<h3>int <code>BRLAPI_STDCALL</code> brlapi_leaveRawMode (void)</h3>
<p>Leave Raw mode </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, -1 on error</dl>
<h3>ssize_t <code>BRLAPI_STDCALL</code> brlapi_recvRaw (void *buffer, size_tsize)</h3>
<p>Get Raw data </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>buffer</i> points on a buffer where the function will store the received data;<br />
 <i>size</i> holds the buffer size.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>its size, -1 on error or signal interruption</dl>
<h3>int <code>BRLAPI_STDCALL</code> brlapi_resumeDriver (void)</h3>
<p>Resume braille driver </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>-1 on error</dl>
<h3>ssize_t <code>BRLAPI_STDCALL</code> brlapi_sendRaw (const void *buffer, size_tsize)</h3>
<p>Send Raw data </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>buffer</i> points on the data;<br />
 <i>size</i> holds the packet size.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>size on success, -1 on error</dl>
<h3>int <code>BRLAPI_STDCALL</code> brlapi_suspendDriver (const char *driver)</h3>
<p>Suspend braille driver </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>driver</i> Specifies the name of the driver which will be suspended.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>-1 on error</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for BrlAPI from the source code.</p>
