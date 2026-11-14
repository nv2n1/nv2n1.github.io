---
title: "xkbupdatemapfromcore(3)"
name: "xkbupdatemapfromcore"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbupdatemapfromcore/"
description: "XkbUpdateMapFromCore – Update a local Xkb keyboard map to reflect the mapping expressed by a core format mapping"
---

<p>XkbUpdateMapFromCore &#8211; Update a local Xkb keyboard map to reflect the mapping expressed by a core format mapping </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Bool XkbUpdateMapFromCore</code> <code>(XkbDescPtr </code><i>xkb</i><code>,</code> <code>KeyCode </code><i>first_key</i><code>,</code> <code>int </code><i>num_keys</i><code>,</code> <code>int </code><i>map_width</i><code>,</code> <code>KeySym *</code><i>core_keysyms</i><code>,</code> <code>XkbChangesPtr </code><i>changes</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; xkb</i></p>
<dd>
<dd>keyboard description to update</p>
<dt><i>&#8211; first_key</i></p>
<dd>keycode of first key description to update</p>
<dt><i>&#8211; num_keys</i></p>
<dd>number of key descriptions to update</p>
<dt><i>&#8211; map_width</i></p>
<dd>width of core protocol keymap</p>
<dt><i>&#8211; core_keysyms</i></p>
<dd>symbols in core protocol keymap</p>
<dt><i>&#8211; changes</i></p>
<dd>backfilled with changes made to Xkb</dl>
<h2>Description</h2>
<p>Xkb provides several functions that make it easier to apply the compatibility map to configure a client-side Xkb keyboard mapping, given a core protocol representation of part or all of a keyboard mapping. Obtain a core protocol representation of a keyboard mapping from an actual server (by using <i>XGetKeyboardMapping, </i> for example), a data file, or some other source. </p>
<p> <i>XkbUpdateMapFromCore </i> interprets input argument information representing a keyboard map in core format to update the Xkb keyboard description passed in <i>xkb. </i> Only a portion of the Xkb map is updated &#8211; the portion corresponding to keys with keycodes in the range <i>first_key </i> through <i>first_key + num_keys &#8211; 1. </i> If <i>XkbUpdateMapFromCore </i> is being called in response to a MappingNotify event, <i>first_key </i> and <i>num_keys </i> are reported in the MappingNotify event. <i>core_keysyms </i> contains the keysyms corresponding to the keycode range being updated, in core keyboard description order. <i>map_width </i> is the number of keysyms per key in <i>core_keysyms. </i> Thus, the first <i>map_width </i> entries in <i>core_keysyms </i> are for the key with keycode <i>first_key, </i> the next <i>map_width </i> entries are for key <i>first_key + 1, </i> and so on. </p>
<p> In addition to modifying the Xkb keyboard mapping in <i>xkb, XkbUpdateMapFromCore </i> backfills the changes structure whose address is passed in <i>changes </i> to indicate the modifications that were made. You may then use <i>changes </i> in subsequent calls such as <i>XkbSetMap, </i> to propagate the local modifications to a server.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkbsetmap/">XkbSetMap</a></code>(3)</p>
