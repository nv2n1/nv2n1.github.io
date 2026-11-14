---
title: "xkeysymtokeycode(3)"
name: "xkeysymtokeycode"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkeysymtokeycode/"
description: "XStringToKeysym, XKeysymToString, XKeycodeToKeysym, XKeysymToKeycode, XConvertCase – convert keysyms"
---

<p>XStringToKeysym, XKeysymToString, XKeycodeToKeysym, XKeysymToKeycode, XConvertCase &#8211; convert keysyms </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>KeySym XStringToKeysym(char *<i>string</i>);</p>
<dd>char *XKeysymToString(KeySym <i>keysym</i>);</p>
<dd>KeySym XKeycodeToKeysym(Display *<i>display</i>, KeyCode <i>keycode</i>, int <i>index</i>);</p>
<dd>KeyCode XKeysymToKeycode(Display *<i>display</i>, KeySym <i>keysym</i>);</p>
<dd>void XConvertCase(KeySym <i>keysym</i>, KeySym *<i>lower_return</i>, KeySym *<i>upper_return</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>index</i></p>
<dd>Specifies the element of KeyCode vector.</p>
<dt><i>keycode</i></p>
<dd>Specifies the KeyCode.</p>
<dt><i>keysym</i></p>
<dd>Specifies the KeySym that is to be searched for or converted.</p>
<dt><i>lower_return</i></p>
<dd>Returns the lowercase form of keysym, or keysym.</p>
<dt><i>string</i></p>
<dd>Specifies the name of the KeySym that is to be converted.</p>
<dt><i>upper_return</i></p>
<dd>Returns the uppercase form of keysym, or keysym.</dl>
<h2>Description</h2>
<p>Standard KeySym names are obtained from by removing the XK_ prefix from each name. KeySyms that are not part of the Xlib standard also may be obtained with this function. The set of KeySyms that are available in this manner and the mechanisms by which Xlib obtains them is implementation-dependent. </p>
<p> If the KeySym name is not in the Host Portable Character Encoding, the result is implementation-dependent. If the specified string does not match a valid KeySym, <code>XStringToKeysym</code> returns <code>NoSymbol</code>. </p>
<p> The returned string is in a static area and must not be modified. The returned string is in the Host Portable Character Encoding. If the specified KeySym is not defined, <code>XKeysymToString</code> returns a NULL. </p>
<p> The <code>XKeycodeToKeysym</code> function uses internal Xlib tables and returns the KeySym defined for the specified KeyCode and the element of the KeyCode vector. If no symbol is defined, <code>XKeycodeToKeysym</code> returns <code>NoSymbol</code>. <code>XKeycodeToKeysym</code> predates the XKB extension. If you want to lookup a KeySym while using XKB you have to use <code>XkbKeycodeToKeysym</code>. </p>
<p> If the specified KeySym is not defined for any KeyCode, <code>XKeysymToKeycode</code> returns zero. </p>
<p> The <code>XConvertCase</code> function returns the uppercase and lowercase forms of the specified Keysym, if the KeySym is subject to case conversion; otherwise, the specified KeySym is returned to both lower_return and upper_return. Support for conversion of other than Latin and Cyrillic KeySyms is implementation-dependent.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xkbkeycodetokeysym/">XkbKeycodeToKeysym</a>(3), <a href="/docs/linux/man/3-xlookupkeysym/">XLookupKeysym</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
