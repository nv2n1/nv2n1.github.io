---
title: "xkbtranslatekeycode(3)"
name: "xkbtranslatekeycode"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbtranslatekeycode/"
description: "XkbTranslateKeyCode – Translate a keycode to a key symbol and modifiers"
---

<p>XkbTranslateKeyCode &#8211; Translate a keycode to a key symbol and modifiers </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Bool XkbTranslateKeyCode</code> <code>(XkbDescPtr </code><i>xkb</i><code>,</code> <code>KeyCode </code><i>key</i><code>,</code> <code>unsigned int </code><i>mods</i><code>,</code> <code>unsigned int *</code><i>mods_rtrn</i><code>,</code> <code>KeySym *</code><i>keysym_rtrn</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; xkb</i></p>
<dd>
<dd>keyboard description to use for translation</p>
<dt><i>&#8211; key</i></p>
<dd>keycode to translate</p>
<dt><i>&#8211; mods</i></p>
<dd>modifiers to apply when translating key</p>
<dt><i>&#8211; mods_rtrn</i></p>
<dd>backfilled with consumed modifiers</p>
<dt><i>&#8211; keysym_rtrn</i></p>
<dd>keysym resulting from translation</dl>
<h2>Description</h2>
<p><i>mods_rtrn </i> is backfilled with the modifiers consumed by the translation process. <i>mods </i> is a bitwise inclusive OR of the legal modifier masks: ShiftMask, LockMask, ControlMask, Mod1Mask, Mod2Mask, Mod3Mask, Mod4Mask, Mod5Mask.The AlwaysConsumeShiftAndLock library control (see below), if enabled, causes <i>XkbTranslateKeyCode </i> to consume shift and lock. <i>XkbTranslateKeyCode </i> returns True if the translation resulted in a keysym, and False if it resulted in NoSymbol. </p>
<p> The AlwaysConsumeShiftAndLock control, if enabled, forces <i>XLookupString </i> to consume the Shift and Lock modifiers when processing all keys, even if the definition for the key type does not specify these modifiers. The AlwaysConsumeShiftAndLock control is unset by default.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xlookupstring/">XLookupString</a></code>(3)</p>
