---
title: "iscursorkey(3)"
name: "iscursorkey"
section: "3"
letter: "i"
url: "/docs/linux/man/3-iscursorkey/"
description: "IsCursorKey, IsFunctionKey, IsKeypadKey, IsMiscFunctionKey, IsModifierKey, IsPFKey, IsPrivateKeypadKey – keysym classification macros"
---

<p>IsCursorKey, IsFunctionKey, IsKeypadKey, IsMiscFunctionKey, IsModifierKey, IsPFKey, IsPrivateKeypadKey &#8211; keysym classification macros </p>
<h2>Syntax</h2>
<p>int IsCursorKey(KeySym <i>keysym</i>); </p>
<p> int IsFunctionKey(KeySym <i>keysym</i>); </p>
<p> int IsKeypadKey(KeySym <i>keysym</i>); </p>
<p> int IsMiscFunctionKey(KeySym <i>keysym</i>); </p>
<p> int IsModifierKey(KeySym <i>keysym</i>); </p>
<p> int IsPFKey(KeySym <i>keysym</i>); </p>
<p> int IsPrivateKeypadKey(KeySym <i>keysym</i>);</p>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>keysym</i></p>
<dd>Specifies the KeySym that is to be tested.</dl>
<h2>Description</h2>
<p>The <code>IsCursorKey</code> macro returns <code>True</code> if the specified KeySym is a cursor key. </p>
<p> The <code>IsFunctionKey</code> macro returns <code>True</code> if the KeySym is a function key. </p>
<p> The <code>IsKeypadKey</code> macro returns <code>True</code> if the specified KeySym is a keypad key. </p>
<p> The <code>IsMiscFunctionKey</code> macro returns <code>True</code> if the specified KeySym is a miscellaneous function key. </p>
<p> The <code>IsModifierKey</code> macro returns <code>True</code> if the specified KeySym is a modifier key. </p>
<p> The <code>IsPFKey</code> macro returns <code>True</code> if the specified KeySym is a PF key. </p>
<p> The <code>IsPrivateKeypadKey</code> macro returns <code>True</code> if the specified KeySym is a vendor-private keypad key.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xkbkeytypesforcoresymbols/">XkbKeyTypesForCoreSymbols</a>(3), <a href="/docs/linux/man/3-allplanes/">AllPlanes</a>(3), <a href="/docs/linux/man/3-blackpixelofscreen/">BlackPixelOfScreen</a>(3), <a href="/docs/linux/man/3-imagebyteorder/">ImageByteOrder</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
