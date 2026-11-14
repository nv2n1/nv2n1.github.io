---
title: "xkbkeytypesforcoresymbols(3)"
name: "xkbkeytypesforcoresymbols"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbkeytypesforcoresymbols/"
description: "XkbKeyTypesForCoreSymbols – Determine the Xkb key types appropriate for the symbols bound to a key in a core keyboard mapping"
---

<p>XkbKeyTypesForCoreSymbols &#8211; Determine the Xkb key types appropriate for the symbols bound to a key in a core keyboard mapping </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>int XkbKeyTypesForCoreSymbols</code> <code>(XkbDescPtr </code><i>xkb</i><code>,</code> <code>int </code><i>map_width</i><code>,</code> <code>KeySym *</code><i>core_syms</i><code>,</code> <code>unsigned int </code><i>protected</i><code>,</code> <code>int *</code><i>types_inout</i><code>,</code> <code>KeySym *</code><i>xkb_syms_rtrn</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; xkb</i></p>
<dd>
<dd>keyboard description in which to place symbols</p>
<dt><i>&#8211; map_width</i></p>
<dd>width of core protocol keymap in xkb_syms_rtrn</p>
<dt><i>&#8211; core_syms</i></p>
<dd>core protocol format array of KeySyms</p>
<dt><i>&#8211; protected</i></p>
<dd>explicit key types</p>
<dt><i>&#8211; types_inout</i></p>
<dd>backfilled with the canonical types bound to groups one and two for the key</p>
<dt><i>&#8211; xkb_syms_rtrn</i></p>
<dd>backfilled with symbols bound to the key in the Xkb mapping</dl>
<h2>Description</h2>
<p><i>XkbKeyTypesForCoreSymbols </i> expands the symbols in <i>core_syms </i> and types in <i>types_inout,</i> then chooses canonical key types (canonical key types are defined The Canonical Key Types) for groups 1 and 2 using the rules specified by the Xkb protocol and places them in xkb_syms_rtrn, which will be non-NULL. </p>
<p> <code>The Canonical Key Types</code> </p>
<p> Xkb allows up to XkbMaxKeyTypes (255) key types to be defined, but requires at least XkbNumRequiredTypes (4) predefined types to be in a key map. These predefined key types are referred to as the canonical key types and describe the types of keys available on most keyboards. The definitions for the canonical key types are held in the first XkbNumRequiredTypes entries of the <i>types </i> field of the client map and are indexed using the following constants: </p>
<pre> XkbOneLevelIndex
 XkbTwoLevelIndex
 XkbAlphabeticIndex
 XkbKeypadIndex</pre>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp; ONE_LEVEL </p>
<p> The ONE_LEVEL key type describes groups that have only one symbol. The default ONE_LEVEL key type has no map entries and does not pay attention to any modifiers. A symbolic representation of this key type could look like the following: </p>
<pre> type &quot;ONE_LEVEL&quot; {
 modifiers = None;
 map[None]= Level1;
 level_name[Level1]= &quot;Any&quot;;
 };</pre>
<p>The description of the ONE_LEVEL key type is stored in the types[XkbOneLevelIndex] entry of the client key map. </p>
<p> TWO_LEVEL </p>
<p> The TWO_LEVEL key type describes groups that consist of two symbols but are neither alphabetic nor numeric keypad keys. The default TWO_LEVEL type uses only the Shift modifier. It returns shift level two if Shift is set, and level one if it is not. A symbolic representation of this key type could look like the following: </p>
<pre> type &quot;TWO_LEVEL&quot; {
 modifiers = Shift;
 map[Shift]= Level2;
 level_name[Level1]= &quot;Base&quot;;
 level_name[Level2]= &quot;Shift&quot;;
 };</pre>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp; The description of the TWO_LEVEL key type is stored in the types[XkbTwoLevelIndex] entry of the client key map. </p>
<p> ALPHABETIC </p>
<p> The ALPHABETIC key type describes groups consisting of two symbols: the lowercase form of a symbol followed by the uppercase form of the same symbol. The default ALPHABETIC type implements locale-sensitive &quot;Shift cancels CapsLock&quot; behavior using both the Shift and Lock modifiers as follows: </p>
<dl COMPACT>
<dt>&bull;</p>
<dd>If Shift and Lock are both set, the default ALPHABETIC type yields level one.</p>
<dt>&bull;</p>
<dd>If Shift alone is set, it yields level two.</p>
<dt>&bull;</p>
<dd>If Lock alone is set, it yields level one, but preserves the Lock modifier so Xlib notices and applies the appropriate capitalization rules. The Xlib functions are locale-sensitive and apply different capitalization rules for different locales.</p>
<dt>&bull;</p>
<dd>If neither Shift nor Lock is set, it yields level one. </p>
<p> A symbolic representation of this key type could look like the following: </p>
<pre> type &quot;ALPHABETIC&quot; {
 modifiers = Shift+Lock;
 map[Shift]= Level2;
 preserve[Lock]= Lock;
 level_name[Level1]= &quot;Base&quot;;
 level_name[Level2]= &quot;Caps&quot;;
 };</pre>
<p>The description of the ALPHABETIC key type is stored in the types[XkbAlphabeticIndex] entry of the client key map. </p>
<p> KEYPAD </p>
<p> The KEYPAD key type describes groups that consist of two symbols, at least one of which is a numeric keypad symbol. The numeric keypad symbol is assumed to reside at level two. The default KEYPAD key type implements &quot;Shift cancels NumLock&quot; behavior using the Shift modifier and the real modifier bound to the virtual modifier named &quot;NumLock,&quot; known as the NumLock modifier, as follows: </p>
<dt>&bull;</p>
<dd>If Shift and NumLock are both set, the default KEYPAD type yields level one.</p>
<dt>&bull;</p>
<dd>If Shift alone is set, it yields level two.</p>
<dt>&bull;</p>
<dd>If NumLock alone is set, it yields level two.</p>
<dt>&bull;</p>
<dd>If neither Shift nor NumLock is set, it yields level one. </p>
<p> A symbolic representation of this key type could look like the following: </p>
<pre> type &quot;KEYPAD&quot; {
 modifiers = Shift+NumLock;
 map[None]= Level1;
 map[Shift]= Level2;
 map[NumLock]= Level2;
 map[Shift+NumLock]= Level1;
 level_name[Level1]= &quot;Base&quot;;
 level_name[Level2]= &quot;Caps&quot;;
 };</pre>
<p>The description of the KEYPAD key type is stored in the types[XkbKeypadIndex] entry of the client key map. </p>
<p> A core keymap is a two-dimensional array of keysyms. It has <i>map_width </i> columns and <i>max_key_code </i> rows. <i>XkbKeyTypesForCoreSymbols </i> takes a single row from a core keymap, determines the number of groups associated with it, the type of each group, and the symbols bound to each group. The return value is the number of groups, <i>types_inout </i> has the types for each group, and <i>xkb_syms_rtrn </i> has the symbols in Xkb order (that is, groups are contiguous, regardless of size). </p>
<p> <i>protected </i> contains the explicitly protected key types. There is one explicit override control associated with each of the four possible groups for each Xkb key, ExplicitKeyType1 through ExplicitKeyType4; <i>protected </i> is an inclusive OR of these controls. <i>map_width </i> is the width of the core keymap and is not dependent on any Xkb definitions. <i>types_inout </i> is an array of four type indices. On input, <i>types_inout </i> contains the indices of any types already assigned to the key, in case they are explicitly protected from change. </p>
<p> Upon return, <i>types_inout </i> contains any automatically selected (that is, canonical) types plus any protected types. Canonical types are assigned to all four groups if there are enough symbols to do so. The four entries in <i>types_inout </i> correspond to the four groups for the key in question. </p>
</dl>
