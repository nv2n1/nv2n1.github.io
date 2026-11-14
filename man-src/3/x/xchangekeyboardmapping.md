---
title: "xchangekeyboardmapping(3)"
name: "xchangekeyboardmapping"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xchangekeyboardmapping/"
description: "XChangeKeyboardMapping, XGetKeyboardMapping, XDisplayKeycodes, XSetModifierMapping, XGetModifierMapping, XNewModifiermap, XInsertModifiermapEntry, XDeleteModifiermapEntry, XFreeModifiermap, XModifi..."
---

<p>XChangeKeyboardMapping, XGetKeyboardMapping, XDisplayKeycodes, XSetModifierMapping, XGetModifierMapping, XNewModifiermap, XInsertModifiermapEntry, XDeleteModifiermapEntry, XFreeModifiermap, XModifierKeymap &#8211; manipulate keyboard encoding and keyboard encoding structure </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>int XChangeKeyboardMapping(Display *<i>display</i>, int <i>first_keycode</i>, int <i>keysyms_per_keycode</i>, KeySym *<i>keysyms</i>, int <i>num_codes</i>);</p>
<dd>KeySym *XGetKeyboardMapping(Display *<i>display</i>, KeyCode <i>first_keycode</i>, int <i>keycode_count</i>, int *<i>keysyms_per_keycode_return</i>);</p>
<dd>int XDisplayKeycodes(Display *<i>display</i>, int *<i>min_keycodes_return</i>, int *<i>max_keycodes_return</i>);</p>
<dd>int XSetModifierMapping(Display *<i>display</i>, XModifierKeymap *<i>modmap</i>);</p>
<dd>XModifierKeymap *XGetModifierMapping(Display *<i>display</i>);</p>
<dd>XModifierKeymap *XNewModifiermap(int <i>max_keys_per_mod</i>);</p>
<dd>XModifierKeymap *XInsertModifiermapEntry(XModifierKeymap *<i>modmap</i>, KeyCode <i>keycode_entry</i>, int <i>modifier</i>);</p>
<dd>XModifierKeymap *XDeleteModifiermapEntry(XModifierKeymap *<i>modmap</i>, KeyCode <i>keycode_entry</i>, int <i>modifier</i>);</p>
<dd>int XFreeModifiermap(XModifierKeymap *<i>modmap</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>first_keycode</i></p>
<dd>Specifies the first KeyCode that is to be changed or returned.</p>
<dt><i>keycode_count</i></p>
<dd>Specifies the number of KeyCodes that are to be returned.</p>
<dt><i>keycode_entry</i></p>
<dd>Specifies the KeyCode.</p>
<dt><i>keysyms</i></p>
<dd>Specifies an array of KeySyms.</p>
<dt><i>keysyms_per_keycode</i></p>
<dd>Specifies the number of KeySyms per KeyCode.</p>
<dt><i>keysyms_per_keycode_return</i></p>
<dd>Returns the number of KeySyms per KeyCode.</p>
<dt><i>max_keys_per_mod</i></p>
<dd>Specifies the number of KeyCode entries preallocated to the modifiers in the map.</p>
<dt><i>max_keycodes_return</i></p>
<dd>Returns the maximum number of KeyCodes.</p>
<dt><i>min_keycodes_return</i></p>
<dd>Returns the minimum number of KeyCodes.</p>
<dt><i>modifier</i></p>
<dd>Specifies the modifier.</p>
<dt><i>modmap</i></p>
<dd>Specifies the <code>XModifierKeymap</code> structure.</p>
<dt><i>num_codes</i></p>
<dd>Specifies the number of KeyCodes that are to be changed.</dl>
<h2>Description</h2>
<p>The <code>XChangeKeyboardMapping</code> function defines the symbols for the specified number of KeyCodes starting with first_keycode. The symbols for KeyCodes outside this range remain unchanged. The number of elements in keysyms must be: </p>
<p> num_codes * keysyms_per_keycode </p>
<p> The specified first_keycode must be greater than or equal to min_keycode returned by <code>XDisplayKeycodes</code>, or a <code>BadValue</code> error results. In addition, the following expression must be less than or equal to max_keycode as returned by <code>XDisplayKeycodes</code>, or a <code>BadValue</code> error results: </p>
<p> first_keycode + num_codes &#8211; 1 </p>
<p> KeySym number N, counting from zero, for KeyCode K has the following index in keysyms, counting from zero: </p>
<p> (K &#8211; first_keycode) * keysyms_per_keycode + N </p>
<p> The specified keysyms_per_keycode can be chosen arbitrarily by the client to be large enough to hold all desired symbols. A special KeySym value of <code>NoSymbol</code> should be used to fill in unused elements for individual KeyCodes. It is legal for <code>NoSymbol</code> to appear in nontrailing positions of the effective list for a KeyCode. <code>XChangeKeyboardMapping</code> generates a <code>MappingNotify</code> event. </p>
<p> There is no requirement that the X server interpret this mapping. It is merely stored for reading and writing by clients. </p>
<p> <code>XChangeKeyboardMapping</code> can generate <code>BadAlloc</code> and <code>BadValue</code> errors. </p>
<p> The <code>XGetKeyboardMapping</code> function returns the symbols for the specified number of KeyCodes starting with first_keycode. The value specified in first_keycode must be greater than or equal to min_keycode as returned by <code>XDisplayKeycodes</code>, or a <code>BadValue</code> error results. In addition, the following expression must be less than or equal to max_keycode as returned by <code>XDisplayKeycodes</code>: </p>
<p> first_keycode + keycode_count &#8211; 1 </p>
<p> If this is not the case, a <code>BadValue</code> error results. The number of elements in the KeySyms list is: </p>
<p> keycode_count * keysyms_per_keycode_return </p>
<p> KeySym number N, counting from zero, for KeyCode K has the following index in the list, counting from zero: (K &#8211; first_code) * keysyms_per_code_return + N </p>
<p> The X server arbitrarily chooses the keysyms_per_keycode_return value to be large enough to report all requested symbols. A special KeySym value of <code>NoSymbol</code> is used to fill in unused elements for individual KeyCodes. To free the storage returned by <code>XGetKeyboardMapping</code>, use <code>XFree</code>. </p>
<p> <code>XGetKeyboardMapping</code> can generate a <code>BadValue</code> error. </p>
<p> The <code>XDisplayKeycodes</code> function returns the min-keycodes and max-keycodes supported by the specified display. The minimum number of KeyCodes returned is never less than 8, and the maximum number of KeyCodes returned is never greater than 255. Not all KeyCodes in this range are required to have corresponding keys. </p>
<p> The <code>XSetModifierMapping</code> function specifies the KeyCodes of the keys (if any) that are to be used as modifiers. If it succeeds, the X server generates a <code>MappingNotify</code> event, and <code>XSetModifierMapping</code> returns <code>MappingSuccess</code>. X permits at most 8 modifier keys. If more than 8 are specified in the <code>XModifierKeymap</code> structure, a <code>BadLength</code> error results. </p>
<p> The modifiermap member of the <code>XModifierKeymap</code> structure contains 8 sets of max_keypermod KeyCodes, one for each modifier in the order <code>Shift</code>, <code>Lock</code>, <code>Control</code>, <code>Mod1</code>, <code>Mod2</code>, <code>Mod3</code>, <code>Mod4</code>, and <code>Mod5</code>. Only nonzero KeyCodes have meaning in each set, and zero KeyCodes are ignored. In addition, all of the nonzero KeyCodes must be in the range specified by min_keycode and max_keycode in the <code>Display</code> structure, or a <code>BadValue</code> error results. </p>
<p> An X server can impose restrictions on how modifiers can be changed, for example, if certain keys do not generate up transitions in hardware, if auto-repeat cannot be disabled on certain keys, or if multiple modifier keys are not supported. If some such restriction is violated, the status reply is <code>MappingFailed</code>, and none of the modifiers are changed. If the new KeyCodes specified for a modifier differ from those currently defined and any (current or new) keys for that modifier are in the logically down state, <code>XSetModifierMapping</code> returns <code>MappingBusy</code>, and none of the modifiers is changed. </p>
<p> <code>XSetModifierMapping</code> can generate <code>BadAlloc</code> and <code>BadValue</code> errors. </p>
<p> The <code>XGetModifierMapping</code> function returns a pointer to a newly created <code>XModifierKeymap</code> structure that contains the keys being used as modifiers. The structure should be freed after use by calling <code>XFreeModifiermap</code>. If only zero values appear in the set for any modifier, that modifier is disabled. </p>
<p> The <code>XNewModifiermap</code> function returns a pointer to <code>XModifierKeymap</code> structure for later use. </p>
<p> The <code>XInsertModifiermapEntry</code> function adds the specified KeyCode to the set that controls the specified modifier and returns the resulting <code>XModifierKeymap</code> structure (expanded as needed). </p>
<p> The <code>XDeleteModifiermapEntry</code> function deletes the specified KeyCode from the set that controls the specified modifier and returns a pointer to the resulting <code>XModifierKeymap</code> structure. </p>
<p> The <code>XFreeModifiermap</code> function frees the specified <code>XModifierKeymap</code> structure.</p>
<h2>Structures</h2>
<p>The <code>XModifierKeymap</code> structure contains: </p>
<p> typedef struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int max_keypermod;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;This server&#8217;s max number of keys per modifier&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;KeyCode&nbsp;*modifiermap;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;An 8 by max_keypermod array of the modifiers&nbsp;*/ } XModifierKeymap;</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAlloc</code></p>
<dd>The server failed to allocate the requested resource or server memory.</p>
<dt><code>BadValue</code></p>
<dd>Some numeric value falls outside the range of values accepted by the request. Unless a specific range is specified for an argument, the full range defined by the argument&#8217;s type is accepted. Any argument defined as a set of alternatives can generate this error.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xfree/">XFree</a>(3), <a href="/docs/linux/man/3-xkbgetmap/">XkbGetMap</a>(3), <a href="/docs/linux/man/3-xsetpointermapping/">XSetPointerMapping</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
