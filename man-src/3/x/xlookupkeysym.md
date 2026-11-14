---
title: "xlookupkeysym(3)"
name: "xlookupkeysym"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xlookupkeysym/"
description: "XLookupKeysym, XRefreshKeyboardMapping, XLookupString, XRebindKeysym – handle keyboard input events in Latin-1"
---

<p>XLookupKeysym, XRefreshKeyboardMapping, XLookupString, XRebindKeysym &#8211; handle keyboard input events in Latin-1 </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>KeySym XLookupKeysym(XKeyEvent *<i>key_event</i>, int <i>index</i>);</p>
<dd>int XRefreshKeyboardMapping(XMappingEvent *<i>event_map</i>);</p>
<dd>int XLookupString(XKeyEvent *<i>event_struct</i>, char *<i>buffer_return</i>, int <i>bytes_buffer</i>, KeySym *<i>keysym_return</i>, XComposeStatus *<i>status_in_out</i>);</p>
<dd>int XRebindKeysym(Display *<i>display</i>, KeySym <i>keysym</i>, KeySym <i>list</i>[], int <i>mod_count</i>, unsigned char *<i>string</i>, int <i>num_bytes</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>buffer_return</i></p>
<dd>Returns the translated characters.</p>
<dt><i>bytes_buffer</i></p>
<dd>Specifies the length of the buffer. No more than bytes_buffer of translation are returned.</p>
<dt><i>num_bytes</i></p>
<dd>Specifies the number of bytes in the string argument.</p>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>event_map</i></p>
<dd>Specifies the mapping event that is to be used.</p>
<dt><i>event_struct</i></p>
<dd>Specifies the key event structure to be used. You can pass <code>XKeyPressedEvent</code> or <code>XKeyReleasedEvent</code>.</p>
<dt><i>index</i></p>
<dd>Specifies the index into the KeySyms list for the event&#8217;s KeyCode.</p>
<dt><i>key_event</i></p>
<dd>Specifies the <code>KeyPress</code> or <code>KeyRelease</code> event.</p>
<dt><i>keysym</i></p>
<dd>Specifies the KeySym that is to be returned.</p>
<dt><i>keysym_return</i></p>
<dd>Returns the KeySym computed from the event if this argument is not NULL.</p>
<dt><i>list</i></p>
<dd>Specifies the KeySyms to be used as modifiers.</p>
<dt><i>mod_count</i></p>
<dd>Specifies the number of modifiers in the modifier list.</p>
<dt><i>status_in_out</i></p>
<dd>Specifies or returns the <code>XComposeStatus</code> structure or NULL.</p>
<dt><i>string</i></p>
<dd>Specifies the string that is copied and will be returned by <code>XLookupString</code>.</dl>
<h2>Description</h2>
<p>The <code>XLookupKeysym</code> function uses a given keyboard event and the index you specified to return the KeySym from the list that corresponds to the KeyCode member in the <code>XKeyPressedEvent</code> or <code>XKeyReleasedEvent</code> structure. If no KeySym is defined for the KeyCode of the event, <code>XLookupKeysym</code> returns <code>NoSymbol</code>. </p>
<p> The <code>XRefreshKeyboardMapping</code> function refreshes the stored modifier and keymap information. You usually call this function when a <code>MappingNotify</code> event with a request member of <code>MappingKeyboard</code> or <code>MappingModifier</code> occurs. The result is to update Xlib&#8217;s knowledge of the keyboard. </p>
<p> The <code>XLookupString</code> function translates a key event to a KeySym and a string. The KeySym is obtained by using the standard interpretation of the <code>Shift</code>, <code>Lock</code>, group, and numlock modifiers as defined in the X Protocol specification. If the KeySym has been rebound (see <code>XRebindKeysym</code>), the bound string will be stored in the buffer. Otherwise, the KeySym is mapped, if possible, to an ISO Latin-1 character or (if the Control modifier is on) to an ASCII control character, and that character is stored in the buffer. <code>XLookupString</code> returns the number of characters that are stored in the buffer. </p>
<p> If present (non-NULL), the <code>XComposeStatus</code> structure records the state, which is private to Xlib, that needs preservation across calls to <code>XLookupString</code> to implement compose processing. The creation of <code>XComposeStatus</code> structures is implementation-dependent; a portable program must pass NULL for this argument. </p>
<p> The <code>XRebindKeysym</code> function can be used to rebind the meaning of a KeySym for the client. It does not redefine any key in the X server but merely provides an easy way for long strings to be attached to keys. <code>XLookupString</code> returns this string when the appropriate set of modifier keys are pressed and when the KeySym would have been used for the translation. No text conversions are performed; the client is responsible for supplying appropriately encoded strings. Note that you can rebind a KeySym that may not exist.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xbuttonevent/">XButtonEvent</a>(3), <a href="/docs/linux/man/3-xmapevent/">XMapEvent</a>(3), <a href="/docs/linux/man/3-xstringtokeysym/">XStringToKeysym</a>(3), <a href="/docs/linux/man/3-xkblookupkeysym/">XkbLookupKeySym</a>(3), <a href="/docs/linux/man/3-xkbrefreshkeyboardmapping/">XkbRefreshKeyboardMapping</a>(3), <a href="/docs/linux/man/3-xmblookupstring/">XmbLookupString</a>(3), <a href="/docs/linux/man/3-xwclookupstring/">XwcLookupString</a>(3), <a href="/docs/linux/man/3-xutf8lookupstring/">Xutf8LookupString</a>(3), <a href="/docs/linux/man/5-compose/">Compose</a>(5)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
