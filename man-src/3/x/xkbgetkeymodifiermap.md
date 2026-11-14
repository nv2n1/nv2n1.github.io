---
title: "xkbgetkeymodifiermap(3)"
name: "xkbgetkeymodifiermap"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbgetkeymodifiermap/"
description: "XkbGetKeyModifierMap – Update the modifier map for one or more of the keys in a keyboard description"
---

<p>XkbGetKeyModifierMap &#8211; Update the modifier map for one or more of the keys in a keyboard description </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Status XkbGetKeyModifierMap</code> <code>(Display *</code><i>dpy</i><code>,</code> <code>unsigned int </code><i>first</i><code>,</code> <code>unsigned int </code><i>num</i><code>,</code> <code>XkbDescPtr </code><i>xkb</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; dpy</i></p>
<dd>
<dd>connection to X server</p>
<dt><i>&#8211; first</i></p>
<dd>keycode of first key to get</p>
<dt><i>&#8211; num</i></p>
<dd>number of keys for which information is desired</p>
<dt><i>&#8211; xkb</i></p>
<dd>keyboard description to update</dl>
<h2>Description</h2>
<p>The <i>modmap </i> entry of the client map is an array, indexed by keycode, specifying the real modifiers bound to a key. Each entry is a mask composed of a bitwise inclusive OR of the legal real modifiers: ShiftMask, LockMask, ControlMask, Mod1Mask, Mod2Mask, Mod3Mask, Mod4Mask, and Mod5Mask. If a bit is set in a <i>modmap </i> entry, the corresponding key is bound to that modifier. </p>
<p> Pressing or releasing the key bound to a modifier changes the modifier set and unset state. The particular manner in which the modifier set and unset state changes is determined by the behavior and actions assigned to the key. </p>
<p> <i>XkbGetKeyModifierMap </i> sends a request to the server for the modifier mappings for <i>num </i> keys starting with the key whose keycode is <i>first. </i> It waits for a reply and places the results in the <i>xkb-&gt;map-&gt;modmap </i> array. If successful, <i>XkbGetKeyModifier </i> returns Success.<br />
&nbsp; If the map component of the <i>xkb </i> parameter has not been allocated, <i>XkbGetKeyModifierMap </i> allocates and initializes it. </p>
<p> If a compatible version of Xkb is not available in the server or the Xkb extension has not been properly initialized, <i>XkbGetKeySyms </i> returns BadAccess. If any allocation errors occur while obtaining the modifier map, <i>XkbGetKeyModifierMap </i> returns BadAlloc.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAccess</code></p>
<dd>The Xkb extension has not been properly initialized</p>
<dt><code>BadAlloc</code></p>
<dd>Unable to allocate storage </p>
</dl>
