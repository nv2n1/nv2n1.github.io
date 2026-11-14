---
title: "brlapi_expandkeycode(3)"
name: "brlapi_expandkeycode"
section: "3"
letter: "b"
url: "/docs/linux/man/3-brlapi_expandkeycode/"
description: "Reading key presses –"
---

<p>Reading key presses &#8211; </p>
<p> How to read key presses from the braille terminal.</p>
<h3>Data Structures</h3>
<p>struct <code>brlapi_expandedKeyCode_t</code> </p>
<p> struct <code>brlapi_describedKeyCode_t</code> </p>
<p> struct <code>brlapi_range_t</code> </p>
<h3>Macros</h3>
<p>#define <code>brlapi_ignoreAllKeys</code>() <code>brlapi_ignoreKeys</code>(<code>brlapi_rangeType_all</code>, NULL, 0) </p>
<p> #define <code>brlapi_acceptAllKeys</code>() <code>brlapi_acceptKeys</code>(<code>brlapi_rangeType_all</code>, NULL, 0) </p>
<p> #define <code>BRLAPI_UC_ROW</code> 0x2800UL </p>
<p> #define <code>brlapi__ignoreAllKeys</code>(handle) <code>brlapi__ignoreKeys</code>(handle, <code>brlapi_rangeType_all</code>, NULL, 0) </p>
<p> #define <code>brlapi__acceptAllKeys</code>(handle) <code>brlapi__acceptKeys</code>(handle, <code>brlapi_rangeType_all</code>, NULL, 0) </p>
<h3>Enumerations</h3>
<p>enum <code>brlapi_rangeType_t</code> { <code>brlapi_rangeType_all</code>, <code>brlapi_rangeType_type</code>, <code>brlapi_rangeType_command</code>, <code>brlapi_rangeType_key</code>, <code>brlapi_rangeType_code</code> } </p>
<h3>Functions</h3>
<p>int <code>BRLAPI_STDCALL</code> <code>brlapi_expandKeyCode</code> (<code>brlapi_keyCode_t</code> code, <code>brlapi_expandedKeyCode_t</code> *expansion) </p>
<p> int <code>BRLAPI_STDCALL</code> <code>brlapi_describeKeyCode</code> (<code>brlapi_keyCode_t</code> code, <code>brlapi_describedKeyCode_t</code> *description) </p>
<p> int <code>BRLAPI_STDCALL</code> <code>brlapi_readKey</code> (int wait, <code>brlapi_keyCode_t</code> *code) </p>
<p> int <code>BRLAPI_STDCALL</code> <code>brlapi__readKey</code> (<code>brlapi_handle_t</code> *handle, int wait, <code>brlapi_keyCode_t</code> *code) </p>
<p> int <code>BRLAPI_STDCALL</code> <code>brlapi_ignoreKeys</code> (<code>brlapi_rangeType_t</code> type, const <code>brlapi_keyCode_t</code> keys[], unsigned int count) </p>
<p> int <code>BRLAPI_STDCALL</code> <code>brlapi__ignoreKeys</code> (<code>brlapi_handle_t</code> *handle, <code>brlapi_rangeType_t</code> type, const <code>brlapi_keyCode_t</code> keys[], unsigned int count) </p>
<p> int <code>BRLAPI_STDCALL</code> <code>brlapi_acceptKeys</code> (<code>brlapi_rangeType_t</code> type, const <code>brlapi_keyCode_t</code> keys[], unsigned int count) </p>
<p> int <code>BRLAPI_STDCALL</code> <code>brlapi__acceptKeys</code> (<code>brlapi_handle_t</code> *handle, <code>brlapi_rangeType_t</code> type, const <code>brlapi_keyCode_t</code> keys[], unsigned int count) </p>
<p> int <code>BRLAPI_STDCALL</code> <code>brlapi__ignoreAllKeys</code> (<code>brlapi_handle_t</code> *handle) </p>
<p> int <code>BRLAPI_STDCALL</code> <code>brlapi__acceptAllKeys</code> (<code>brlapi_handle_t</code> *handle) </p>
<p> int <code>BRLAPI_STDCALL</code> <code>brlapi_ignoreKeyRanges</code> (<code>brlapi_range_t</code> ranges[], unsigned int count) </p>
<p> int <code>BRLAPI_STDCALL</code> <code>brlapi__ignoreKeyRanges</code> (<code>brlapi_handle_t</code> *handle, <code>brlapi_range_t</code> ranges[], unsigned int count) </p>
<p> int <code>BRLAPI_STDCALL</code> <code>brlapi_acceptKeyRanges</code> (<code>brlapi_range_t</code> ranges[], unsigned int count) </p>
<p> int <code>BRLAPI_STDCALL</code> <code>brlapi__acceptKeyRanges</code> (<code>brlapi_handle_t</code> *handle, <code>brlapi_range_t</code> ranges[], unsigned int count) </p>
<h2>Detailed Description</h2>
<p>Once <code>brlapi_enterTtyMode()</code> has been called, the application can call <code>brlapi_readKey()</code> to read key presses. Either key codes (see <code>Types and Defines fore BrlAPI Key Codes</code>) or commands will be returned, depending on parameters given to <code>brlapi_enterTtyMode()</code>. </p>
<p> Key presses are buffered, so that calling <code>brlapi_readKey()</code> in non-blocking mode from time to time should suffice.</p>
<h2>Macro Definition Documentation</h2>
<h3>#define brlapi__acceptAllKeys(handle) <code>brlapi__acceptKeys</code>(handle, <code>brlapi_rangeType_all</code>, NULL, 0)</h3>
<h3>#define brlapi__ignoreAllKeys(handle) <code>brlapi__ignoreKeys</code>(handle, <code>brlapi_rangeType_all</code>, NULL, 0)</h3>
<h3>int <code>BRLAPI_STDCALL</code> brlapi_acceptAllKeys(void) <code>brlapi_acceptKeys</code>(<code>brlapi_rangeType_all</code>, NULL, 0)</h3>
<p>Accept all key presses from the braille keyboard </p>
<p> This function asks the server to give all keys to the application, and not give them to <i>brltty</i>. </p>
<p> Warning: after calling this function, make sure to call <code>brlapi_ignoreKeys()</code> for ignoring important keys like BRL_CMD_SWITCHVT_PREV/NEXT and such.</p>
<h3>int <code>BRLAPI_STDCALL</code> brlapi_ignoreAllKeys(void) <code>brlapi_ignoreKeys</code>(<code>brlapi_rangeType_all</code>, NULL, 0)</h3>
<p>Ignore all key presses from the braille keyboard </p>
<p> This function asks the server to give all keys to <i>brltty</i>, rather than returning them to the application via <code>brlapi_readKey()</code>.</p>
<h3>#define BRLAPI_UC_ROW 0x2800UL</h3>
<p>Unicode braille row</p>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>brlapi_rangeType_t</code></h3>
<p>types of key ranges </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>brlapi_rangeType_all </i></p>
<dd>all keys, code must be 0</p>
<dt><i>brlapi_rangeType_type </i></p>
<dd>all keys of a given type</p>
<dt><i>brlapi_rangeType_command </i></p>
<dd>all keys of a given command block, i.e. matching the key type and command parts</p>
<dt><i>brlapi_rangeType_key </i></p>
<dd>a given key with any flags</p>
<dt><i>brlapi_rangeType_code </i></p>
<dd>a given key code</dl>
<h2>Function Documentation</h2>
<h3>int <code>BRLAPI_STDCALL</code> brlapi__acceptAllKeys (<code>brlapi_handle_t</code> *handle)</h3>
<h3>int <code>BRLAPI_STDCALL</code> brlapi__acceptKeyRanges (<code>brlapi_handle_t</code> *handle, <code>brlapi_range_t</code>ranges[], unsigned intcount)</h3>
<h3>int <code>BRLAPI_STDCALL</code> brlapi__acceptKeys (<code>brlapi_handle_t</code> *handle, <code>brlapi_rangeType_t</code>type, const <code>brlapi_keyCode_t</code>keys[], unsigned intcount)</h3>
<h3>int <code>BRLAPI_STDCALL</code> brlapi__ignoreAllKeys (<code>brlapi_handle_t</code> *handle)</h3>
<h3>int <code>BRLAPI_STDCALL</code> brlapi__ignoreKeyRanges (<code>brlapi_handle_t</code> *handle, <code>brlapi_range_t</code>ranges[], unsigned intcount)</h3>
<h3>int <code>BRLAPI_STDCALL</code> brlapi__ignoreKeys (<code>brlapi_handle_t</code> *handle, <code>brlapi_rangeType_t</code>type, const <code>brlapi_keyCode_t</code>keys[], unsigned intcount)</h3>
<h3>int <code>BRLAPI_STDCALL</code> brlapi__readKey (<code>brlapi_handle_t</code> *handle, intwait, <code>brlapi_keyCode_t</code> *code)</h3>
<h3>int <code>BRLAPI_STDCALL</code> brlapi_acceptKeyRanges (<code>brlapi_range_t</code>ranges[], unsigned intcount)</h3>
<p>Accept some key presses from the braille keyboard </p>
<p> This function asks the server to return the provided key ranges (inclusive) to the application, and not give them to <i>brltty</i>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ranges</i> key ranges, which are inclusive<br />
 <i>count</i> number of ranges</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>The given codes should be raw keycodes (i.e. some driver name was given to <code>brlapi_enterTtyMode()</code>)</dl>
<h3>int <code>BRLAPI_STDCALL</code> brlapi_acceptKeys (<code>brlapi_rangeType_t</code>type, const <code>brlapi_keyCode_t</code>keys[], unsigned intcount)</h3>
<p>Accept some key presses from the braille keyboard </p>
<p> This function asks the server to give the provided keys to the application, and not give them to <i>brltty</i>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>type</i> type of keys to be ignored<br />
 <i>keys</i> array of keys to be ignored<br />
 <i>count</i> number of keys</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>The given codes should be <i>brltty</i> commands (NULL or &#8221; was given to <code>brlapi_enterTtyMode()</code>)</dl>
<h3>int <code>BRLAPI_STDCALL</code> brlapi_describeKeyCode (<code>brlapi_keyCode_t</code>code, <code>brlapi_describedKeyCode_t</code> *description)</h3>
<p>Describe the components of a key code. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>code</i> the keycode to be described<br />
 <i>description</i> pointer to the structure that receives the description</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, -1 on error</dl>
<h3>int <code>BRLAPI_STDCALL</code> brlapi_expandKeyCode (<code>brlapi_keyCode_t</code>code, <code>brlapi_expandedKeyCode_t</code> *expansion)</h3>
<p>Expand the components of a key code </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>code</i> the key code to be expanded<br />
 <i>expansion</i> pointer to the structure that receives the components</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, -1 on error</dl>
<h3>int <code>BRLAPI_STDCALL</code> brlapi_ignoreKeyRanges (<code>brlapi_range_t</code>ranges[], unsigned intcount)</h3>
<p>Ignore some key presses from the braille keyboard </p>
<p> This function asks the server to give the provided key ranges to <i>brltty</i>, rather than returning them to the application via <code>brlapi_readKey()</code>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ranges</i> key ranges, which are inclusive<br />
 <i>count</i> number of ranges</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>The given codes should be raw keycodes (i.e. some driver name was given to <code>brlapi_enterTtyMode()</code>)</dl>
<h3>int <code>BRLAPI_STDCALL</code> brlapi_ignoreKeys (<code>brlapi_rangeType_t</code>type, const <code>brlapi_keyCode_t</code>keys[], unsigned intcount)</h3>
<p>Ignore some key presses from the braille keyboard </p>
<p> This function asks the server to give the provided keys to <i>brltty</i>, rather than returning them to the application via <code>brlapi_readKey()</code>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>type</i> type of keys to be ignored<br />
 <i>keys</i> array of keys to be ignored<br />
 <i>count</i> number of keys</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>The given codes should be <i>brltty</i> commands (NULL or &#8221; was given to <code>brlapi_enterTtyMode()</code>)</dl>
<h3>int <code>BRLAPI_STDCALL</code> brlapi_readKey (intwait, <code>brlapi_keyCode_t</code> *code)</h3>
<p>Read a key from the braille keyboard </p>
<p> This function returns one key press&#8217;s code. </p>
<p> If NULL or &#8221; was given to <code>brlapi_enterTtyMode()</code>, a <i>brltty</i> command is returned, as described in the documentation for <code>brlapi_keyCode_t</code> . It is hence pretty driver-independent, and should be used by default when no other option is possible. </p>
<p> By default, all commands but those which restart drivers and switch virtual terminals are returned to the application and not to brltty. If the application doesn&#8217;t want to see some command events, it should call <code>brlapi_ignoreKeys()</code> </p>
<p> If some driver name was given to <code>brlapi_enterTtyMode()</code>, a raw keycode is returned, as specified by the terminal driver, usually in &lt;brltty/brldefs-xy&gt; where xy is the driver&#8217;s code. It generally corresponds to the very code that the terminal tells to the driver. This should only be used by applications which are dedicated to a particular braille terminal. Hence, checking the terminal type thanks to a call to <code>brlapi_getDriverName()</code> before getting tty control is a pretty good idea. </p>
<p> By default, all the keypresses will be passed to the client, none will go through brltty, so the application will have to handle console switching itself for instance. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>wait</i> tells whether the call should block until a key is pressed (1) or should only probe key presses (0);<br />
 <i>code</i> holds the key code if a key press is indeed read.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>-1 on error or signal interrupt and *code is then undefined, 0 if block was 0 and no key was pressed so far, or 1 and *code holds the key code.</dl>
<p> Programming hints: </p>
<p> If your application is only driven by braille command keypresses, you can just call brlapi_readKey(1, &amp;code) so that it keeps blocking, waiting for keypresses. </p>
<p> Else, you&#8217;ll probably want to use the file descriptor returned by <code>brlapi_openConnection()</code> in your &#8216;big polling loop&#8217;. For instance: </p>
<dl COMPACT>
<dt>&bull;</p>
<dd>in a select() loop, just add it to the readfds and exceptfds file descriptor sets;</p>
<dt>&bull;</p>
<dd>in a gtk or atspi application, use g_io_add_watch(fileDescriptor, G_IO_IN|G_IO_ERR|G_IO_HUP, f, data) for adding a callback called f;</p>
<dt>&bull;</p>
<dd>in an Xt/Xaw/motif-based application, use XtAppAddInput(app_context, fileDescriptor, XtInputReadMask|XtInputExceptMask, f, data)</p>
<dt>&bull;</p>
<dd>etc.</dl>
<p> and then, when you detect inbound trafic on the file descriptor, do something like this: </p>
<p> while (brlapi_readKey(0, &amp;code) { // process keycode code // &#8230; } </p>
<p> The while loop is needed for processing <i>all</i> pending key presses, else some of them may be left in libbrlapi&#8217;s internal key buffer and you wouldn&#8217;t get them immediately. </p>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>If the read is interrupted by a signal, <code>brlapi_readKey()</code> will return -1, brlapi_errno will be BRLAPI_ERROR_LIBCERR and errno will be EINTR.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for BrlAPI from the source code.</p>
