---
title: "brlapi_openconnection(3)"
name: "brlapi_openconnection"
section: "3"
letter: "b"
url: "/docs/linux/man/3-brlapi_openconnection/"
description: "Connecting to BrlAPI –"
---

<p>Connecting to BrlAPI &#8211; </p>
<h3>Data Structures</h3>
<p>struct <code>brlapi_connectionSettings_t</code><br />
 <i>Settings structure for BrlAPI</i> connection.</p>
<h3>Macros</h3>
<p>#define <code>BRLAPI_SOCKETPORTNUM</code> 4101 </p>
<p> #define <code>BRLAPI_SOCKETPORT</code> &#8216;4101&#8217; </p>
<p> #define <code>BRLAPI_SOCKETPATH</code> &#8216;/var/lib/BrlAPI&#8217; </p>
<p> #define <code>BRLAPI_ETCDIR</code> &#8216;/etc&#8217; </p>
<p> #define <code>BRLAPI_AUTHKEYFILE</code> &#8216;brlapi.key&#8217; </p>
<p> #define <code>BRLAPI_DEFAUTH</code> <code>BRLAPI_ETCDIR</code> &#8216;/&#8217; <code>BRLAPI_AUTHKEYFILE</code> </p>
<p> #define <code>BRLAPI_SETTINGS_INITIALIZER</code> { NULL, NULL } </p>
<h3>Typedefs</h3>
<p>typedef int <code>brlapi_fileDescriptor</code> </p>
<h3>Functions</h3>
<p><code>brlapi_fileDescriptor</code><br />
 <code>BRLAPI_STDCALL</code> <code>brlapi_openConnection</code> (const <code>brlapi_connectionSettings_t</code> *desiredSettings, <code>brlapi_connectionSettings_t</code> *actualSettings)&quot; </p>
<p> <code>brlapi_fileDescriptor</code><br />
 <code>BRLAPI_STDCALL</code> <code>brlapi__openConnection</code> (<code>brlapi_handle_t</code> *handle, const <code>brlapi_connectionSettings_t</code> *desiredSettings, <code>brlapi_connectionSettings_t</code> *actualSettings)&quot; </p>
<p> void <code>BRLAPI_STDCALL</code> <code>brlapi_closeConnection</code> (void) </p>
<p> void <code>BRLAPI_STDCALL</code> <code>brlapi__closeConnection</code> (<code>brlapi_handle_t</code> *handle) </p>
<h2>Detailed Description</h2>
<p>Before calling any other function of the library, calling <code>brlapi_openConnection()</code> is needed to establish a connection to <i>BrlAPI</i> &#8216;s server. When the connection is not needed any more, <code>brlapi_closeConnection()</code> must be called to close the connection.</p>
<h2>Macro Definition Documentation</h2>
<h3>#define BRLAPI_AUTHKEYFILE &#8216;brlapi.key&#8217;</h3>
<p>Default name of the file containing <i>BrlAPI</i> &#8216;s authorization key </p>
<p> This name is relative to BRLAPI_ETCDIR</p>
<h3>#define BRLAPI_DEFAUTH <code>BRLAPI_ETCDIR</code> &#8216;/&#8217; <code>BRLAPI_AUTHKEYFILE</code></h3>
<p>Default authorization setting</p>
<h3>#define BRLAPI_ETCDIR &#8216;/etc&#8217;</h3>
<p><i>brltty</i> &#8216;s settings directory </p>
<p> This is where authorization key and driver-dependent key names are found for instance.</p>
<h3>#define BRLAPI_SETTINGS_INITIALIZER { NULL, NULL }</h3>
<p>Allows to initialize a structure of type <i></i><code>brlapi_connectionSettings_t</code> * with default values.</p>
<h3>#define BRLAPI_SOCKETPATH &#8216;/var/lib/BrlAPI&#8217;</h3>
<p>Default unix path on which connections to <i>BrlAPI</i> can be established</p>
<h3>#define BRLAPI_SOCKETPORT &#8216;4101&#8217;</h3>
<h3>#define BRLAPI_SOCKETPORTNUM 4101</h3>
<p>Default port number on which connections to <i>BrlAPI</i> can be established</p>
<h2>Typedef Documentation</h2>
<h3>typedef int <code>brlapi_fileDescriptor</code></h3>
<h2>Function Documentation</h2>
<h3>void <code>BRLAPI_STDCALL</code> brlapi__closeConnection (<code>brlapi_handle_t</code> *handle)</h3>
<h3><code>brlapi_fileDescriptor</code> <code>BRLAPI_STDCALL</code> brlapi__openConnection (<code>brlapi_handle_t</code> *handle, const <code>brlapi_connectionSettings_t</code> *desiredSettings, <code>brlapi_connectionSettings_t</code> *actualSettings)</h3>
<h3>void <code>BRLAPI_STDCALL</code> brlapi_closeConnection (void)</h3>
<p>Cleanly close the socket </p>
<p> This function locks until a closing acknowledgement is received from the server. The socket is then freed, so the file descriptor <code>brlapi_openConnection()</code> gave has no meaning any more</p>
<h3><code>brlapi_fileDescriptor</code> <code>BRLAPI_STDCALL</code> brlapi_openConnection (const <code>brlapi_connectionSettings_t</code> *desiredSettings, <code>brlapi_connectionSettings_t</code> *actualSettings)</h3>
<p>Open a socket and connect it to <i>BrlAPI</i> &#8216;s server </p>
<p> This function first loads an authorization key as specified in settings. It then creates a TCP socket and connects it to the specified machine, on the specified port. It writes the authorization key on the socket and waits for acknowledgement. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the file descriptor, or -1 on error</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>The file descriptor is returned in case the client wants to communicate with the server without using <i>libbrlapi</i> functions. If it uses them however, it won&#8217;t have to pass the file descriptor later, since the library keeps a copy of it. But that also means that <code>brlapi_openConnection()</code> may be called several times, but <i>libbrlapi</i> functions will always work with the last call&#8217;s descriptor</dl>
<p> <code>Example:</code></p>
<dl COMPACT>
<dd>
<pre>if (brlapi_openConnection(&amp;settings,&amp;settings)&lt;0) {
 fprintf(stderr,'couldn't connect to BrlAPI at %s: %s,
 settings.host, brlapi_strerror(&amp;brlapi_error));
 <a href="//www.systutorials.com/docs/linux/man/1-exit/">exit</a>(1);
}</pre>
</dl>
<p> <code>Errors:</code></p>
<dl COMPACT>
<dd><i>BrlAPI</i> might not be on this TCP port, the host name might not be resolvable, the authorization may fail,&#8230;</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>desiredSettings</i> this gives the desired connection parameters, as described in <code>brlapi_connectionSettings_t</code>. If NULL, defaults values are used, so that it is generally a good idea to give NULL as default, and only fill a <code>brlapi_connectionSettings_t</code> structure when the user gave parameters to the program for instance;<br />
 <i>actualSettings</i> if not NULL, parameters which were actually used are stored here, if the application ever needs them.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>brlapi_connectionSettings_t</code> <code>brlapi_writePacket()</code> <code>brlapi_readPacketHeader()</code> <code>brlapi_readPacketContent()</code> <code>brlapi_readPacket()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for BrlAPI from the source code.</p>
