---
title: "brlapi_leavettymode(3)"
name: "brlapi_leavettymode"
section: "3"
letter: "b"
url: "/docs/linux/man/3-brlapi_leavettymode/"
description: "Entering & leaving tty mode –"
---

<p>Entering &amp; leaving tty mode &#8211; </p>
<p> How to take control of ttys for direct braille display / read.</p>
<h3>Macros</h3>
<p>#define <code>BRLAPI_TTY_DEFAULT</code> -1 </p>
<h3>Functions</h3>
<p>int <code>BRLAPI_STDCALL</code> <code>brlapi_enterTtyMode</code> (int tty, const char *driver) </p>
<p> int <code>BRLAPI_STDCALL</code> <code>brlapi__enterTtyMode</code> (<code>brlapi_handle_t</code> *handle, int tty, const char *driver) </p>
<p> int <code>BRLAPI_STDCALL</code> <code>brlapi_enterTtyModeWithPath</code> (int *ttys, int count, const char *driver) </p>
<p> int <code>BRLAPI_STDCALL</code> <code>brlapi__enterTtyModeWithPath</code> (<code>brlapi_handle_t</code> *handle, int *ttys, int count, const char *driver) </p>
<p> int <code>BRLAPI_STDCALL</code> <code>brlapi_leaveTtyMode</code> (void) </p>
<p> int <code>BRLAPI_STDCALL</code> <code>brlapi__leaveTtyMode</code> (<code>brlapi_handle_t</code> *handle) </p>
<p> int <code>BRLAPI_STDCALL</code> <code>brlapi_setFocus</code> (int tty) </p>
<p> int <code>BRLAPI_STDCALL</code> <code>brlapi__setFocus</code> (<code>brlapi_handle_t</code> *handle, int tty) </p>
<h2>Detailed Description</h2>
<p>Before being able to write on the braille display, the application must tell the server which tty it will handle. </p>
<p> The application must also specify how braille keys will be delivered to it. Two ways are possible: key codes and commands: </p>
<dl COMPACT>
<dt>&bull;</p>
<dd>key codes are specific to each braille driver, since the raw key code, as defined in the driver will be given for each key press. Using them leads to building highly driver-dependent applications, which can yet sometimes be useful to mimic existing proprietary applications for instance.</p>
<dt>&bull;</p>
<dd>commands means that applications will get exactly the same values as <i>brltty</i>. This allows driver-independent clients, which will hopefully be nice to use with a lot of different terminals.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>brlapi_readKey()</code></dl>
<h2>Macro Definition Documentation</h2>
<h3>#define BRLAPI_TTY_DEFAULT -1</h3>
<p>Select the default tty. </p>
<p> The library takes the following steps:</p>
<dl COMPACT>
<dt>1.</p>
<dd>Try to get the tty number from the WINDOWID environment variable (for the xterm case).</p>
<dt>2.</p>
<dd>Try to get the tty number from the CONTROLVT environment variable.</p>
<dt>3.</p>
<dd>Read /proc/self/stat (on Linux).</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>brlapi_enterTtyMode()</code></dl>
<h2>Function Documentation</h2>
<h3>int <code>BRLAPI_STDCALL</code> brlapi__enterTtyMode (<code>brlapi_handle_t</code> *handle, inttty, const char *driver)</h3>
<h3>int <code>BRLAPI_STDCALL</code> brlapi__enterTtyModeWithPath (<code>brlapi_handle_t</code> *handle, int *ttys, intcount, const char *driver)</h3>
<h3>int <code>BRLAPI_STDCALL</code> brlapi__leaveTtyMode (<code>brlapi_handle_t</code> *handle)</h3>
<h3>int <code>BRLAPI_STDCALL</code> brlapi__setFocus (<code>brlapi_handle_t</code> *handle, inttty)</h3>
<h3>int <code>BRLAPI_STDCALL</code> brlapi_enterTtyMode (inttty, const char *driver)</h3>
<p>Ask for some tty, with some key mechanism </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>tty</i></p>
<dl COMPACT>
<dt>&bull;</p>
<dd>If tty&gt;=0 then take control of the specified tty.</p>
<dt>&bull;</p>
<dd>If tty==<code>BRLAPI_TTY_DEFAULT</code> then take control of the default tty.</dl>
<p> <i>driver</i> tells how the application wants <code>brlapi_readKey()</code> to return key presses. NULL or &#8221; means BRLTTY commands are required, whereas a driver name means that raw key codes returned by this driver are expected.</dl>
<p> WINDOWPATH and WINDOWID should be propagated when running remote applications via ssh, for instance, along with BRLAPI_HOST and the authorization key (see SendEnv in <a href="/docs/linux/man/5-ssh_config/">ssh_config</a>(5) and AcceptEnv in <a href="/docs/linux/man/5-sshd_config/">sshd_config</a>(5)) </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the used tty number on success, -1 on error</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>brlapi_leaveTtyMode()</code> <code>brlapi_readKey()</code></dl>
<h3>int <code>BRLAPI_STDCALL</code> brlapi_enterTtyModeWithPath (int *ttys, intcount, const char *driver)</h3>
<p>Ask for some tty specified by its path in the tty tree, with some key mechanism </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ttys</i> points on the array of ttys representing the tty path to be got. Can be NULL if nttys is 0.<br />
 <i>count</i> gives the number of elements in ttys.<br />
 <i>driver</i> has the same meaning as in <code>brlapi_enterTtyMode()</code></dl>
<p> Providing nttys == 0 means to get the root. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>brlapi_enterTtyMode()</code></dl>
<h3>int <code>BRLAPI_STDCALL</code> brlapi_leaveTtyMode (void)</h3>
<p>Stop controlling the tty </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, -1 on error.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>brlapi_enterTtyMode()</code></dl>
<h3>int <code>BRLAPI_STDCALL</code> brlapi_setFocus (inttty)</h3>
<p>Tell the current tty to brltty </p>
<p> This is intended for focus tellers, such as brltty, xbrlapi, screen, &#8230; <code>brlapi_enterTtyMode()</code> must have been called beforehand to tell where this focus applies in the tty tree. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, -1 on error.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>brlapi_enterTtyMode()</code> <code>brlapi_leaveTtyMode()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for BrlAPI from the source code.</p>
