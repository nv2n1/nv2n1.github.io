---
title: "xkbvirtualmodstoreal(3)"
name: "xkbvirtualmodstoreal"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbvirtualmodstoreal/"
description: "XkbVirtualModsToReal – Determines the mapping of virtual modifiers to core X protocol modifiers"
---

<p>XkbVirtualModsToReal &#8211; Determines the mapping of virtual modifiers to core X protocol modifiers </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Bool XkbVirtualModsToReal</code> <code>(XkbDescPtr </code><i>xkb</i><code>,</code> <code>unsigned int </code><i>virtual_mask</i><code>,</code> <code>unsigned int *</code><i>mask_rtrn</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; xkb</i></p>
<dd>
<dd>keyboard description for input device</p>
<dt><i>&#8211; virtual_mask</i></p>
<dd>virtual modifier mask to translate</p>
<dt><i>&#8211; mask_rtrn</i></p>
<dd>backfilled with real modifiers</dl>
<h2>Description</h2>
<p>Xkb maintains a <i>virtual modifier mapping, </i> which lists the virtual modifiers associated with, or bound to, each key. The real modifiers bound to a virtual modifier always include all of the modifiers bound to any of the keys that specify that virtual modifier in their virtual modifier mapping. The <i>server.vmodmap </i> array indicates which virtual modifiers are bound to each key; each entry is a bitmask for the virtual modifier bits. The <i>server.vmodmap </i> array is indexed by keycode. </p>
<p> The <i>vmodmap </i> and <i>vmods </i> members of the server map are the &quot;master&quot; virtual modifier definitions. Xkb automatically propagates any changes to these fields to all other fields that use virtual modifier mappings. </p>
<p> For example, if Mod3 is bound to the Num_Lock key by the core protocol modifier mapping, and the NumLock virtual modifier is bound to they Num_Lock key by the virtual modifier mapping, Mod3 is added to the set of modifiers associated with NumLock. </p>
<p> The virtual modifier mapping is normally updated whenever actions are automatically applied to symbols and few applications should need to change the virtual modifier mapping explicitly. </p>
<p> Use <i>XkbGetMap</i> to get the virtual modifiers from the server or use <i>XkbGetVirtualMods </i> to update a local copy of the virtual modifiers bindings from the server. To set the binding of a virtual modifier to a real modifier, use <i>XkbGetVirtualMods</i> </p>
<p> If the keyboard description defined by <i>xkb </i> includes bindings for virtual modifiers, <i>XkbVirtualModsToReal </i> uses those bindings to determine the set of real modifiers that correspond to the set of virtual modifiers specified in <i>virtual_mask. </i> The <i>virtual_mask </i> parameter is a mask specifying the virtual modifiers to translate; the i-th bit (0 relative) of the mask represents the i-th virtual modifier. If <i>mask_rtrn </i> is non-NULL, <i>XkbVirtualModsToReal </i> backfills it with the resulting real modifier mask. If the keyboard description in <i>xkb </i> does not include virtual modifier bindings, <i>XkbVirtualModsToReal </i> returns False; otherwise, it returns True.</p>
<h2>Return Values</h2>
<dl COMPACT>
<dt>True</p>
<dd>The <i>XkbVirtualModsToReal </i> function returns True if the keyboard description in <i>xkb </i> does include virtual modifier bindings.</p>
<dt>False</p>
<dd>The <i>XkbVirtualModsToReal </i> function returns False if the keyboard description in <i>xkb </i> does not include virtual modifier bindings.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkbgetmap/">XkbGetMap</a></code>(3), <code><a href="/docs/linux/man/3-xkbgetvirtualmods/">XkbGetVirtualMods</a></code>(3)</p>
<h2>Notes</h2>
<p>It is possible for a local (client-side) keyboard description (the <i>xkb </i> parameter) to not contain any virtual modifier information (simply because the client has not requested it) while the server&#8217;s corresponding definition may contain virtual modifier information.</p>
