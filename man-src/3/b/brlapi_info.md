---

title: "brlapi_info(3)"
name: "brlapi_info"
section: "3"
letter: "b"
url: "/docs/linux/man/3-brlapi_info/"
description: "Getting Terminal information –"
---

<p> Getting Terminal information &#8211; </p>
<p> How to get information about the connected Terminal.</p>
<h3>Macros</h3>
<p> #define <code>BRLAPI_MAXNAMELENGTH</code> 31 </p>
<h3>Functions</h3>
<p> int <code>BRLAPI_STDCALL</code> <code>brlapi_getDriverName</code> (char *buffer, size_t size) </p>
<p> int <code>BRLAPI_STDCALL</code> <code>brlapi__getDriverName</code> (<code>brlapi_handle_t</code> *handle, char *buffer, size_t size) </p>
<p> int <code>BRLAPI_STDCALL</code> <code>brlapi_getDisplaySize</code> (unsigned int *x, unsigned int *y) </p>
<p> int <code>BRLAPI_STDCALL</code> <code>brlapi__getDisplaySize</code> (<code>brlapi_handle_t</code> *handle, unsigned int *x, unsigned int *y) </p>
<h2>Detailed Description</h2>
<p> Before using Raw mode or key codes, the application should always check the type of the connected terminal, to be sure it is really the one it expects. </p>
<p> One should also check for display size, so as to adjust further displaying on it.</p>
<h2>Macro Definition Documentation</h2>
<h3>#define BRLAPI_MAXNAMELENGTH 31</h3>
<p> Maximum name length for names embeded in BrlAPI packets, not counting any termination \0 character  </p>
<h2>Function Documentation</h2>
<code></code><code></code><h3>int BRLAPI_STDCALL brlapi__getDisplaySize ( brlapi_handle_t *handle, unsigned int *x, unsigned int *y)</h3>
<code></code><code></code><h3>int BRLAPI_STDCALL brlapi__getDriverName ( brlapi_handle_t *handle, char *buffer, size_tsize)</h3>
<code></code><h3>int BRLAPI_STDCALL brlapi_getDisplaySize (unsigned int *x, unsigned int *y)</h3>
<p> Return the size of the braille display  </p>
<code></code><h3>int BRLAPI_STDCALL brlapi_getDriverName (char *buffer, size_tsize)</h3>
<p> Return the complete name of the driver used by <i>brltty</i> </p>
<p> This function fills its argument with the whole name of the braille terminal if available, terminated with a &#8216;\0&#8217;. </p>
<p> <code>Parameters:</code> </p>
<dl>
<dd> <p> <i>buffer</i> is the buffer given by the application; <br />
 <i>size</i> is the maximum size for the name buffer. </p>
 </dd></dl>
<p> <code>Returns:</code> </p>
<dl>
<dd> <p> -1 on error, or a positive value giving the size of the needed buffer, if the supplied one is to small (same as snprintf()). </p>
 </dd></dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for BrlAPI from the source code. </p>
