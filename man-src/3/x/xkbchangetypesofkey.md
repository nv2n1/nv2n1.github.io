---
title: "xkbchangetypesofkey(3)"
name: "xkbchangetypesofkey"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbchangetypesofkey/"
description: "XkbChangeTypesOfKey – Change the number of groups and the types bound to a key"
---

<p>XkbChangeTypesOfKey &#8211; Change the number of groups and the types bound to a key </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Status XkbChangeTypesOfKey</code> <code>(XkbDescPtr </code><i>xkb</i><code>,</code> <code>int </code><i>key</i><code>,</code> <code>int </code><i>n_groups</i><code>,</code> <code>unsigned int </code><i>groups</i><code>,</code> <code>int *</code><i>new_types_in</i><code>,</code> <code>XkbMapChangesPtr </code><i>p_changes</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; xkb</i></p>
<dd>
<dd>keyboard description to be changed</p>
<dt><i>&#8211; key</i></p>
<dd>keycode for key of interest</p>
<dt><i>&#8211; n_groups</i></p>
<dd>new number of groups for key</p>
<dt><i>&#8211; groups</i></p>
<dd>mask indicating groups to change</p>
<dt><i>&#8211; new_types_in</i></p>
<dd>indices for new groups specified in groups</p>
<dt><i>&#8211; p_changes</i></p>
<dd>notes changes made to xkb</dl>
<h2>Description</h2>
<p><i>XkbChangeTypesOfKey </i> reallocates the symbols and actions bound to the key, if necessary, and initializes any new symbols or actions to NoSymbol or NoAction, as appropriate. If the p_changes parameter is not NULL, <i>XkbChangeTypesOfKey </i> adds the XkbKeySymsMask to the changes field of <i>p_changes </i> and modifies the <i>first_key_sym </i> and <i>num_key_syms </i> fields of <i>p_changes </i> to include the <i>key </i> that was changed. See STRUCTURE for more information on the XkbMapChangesPtr structure. If successful, <i>XkbChangeTypesOfKey </i> returns Success. </p>
<p> The <i>n_groups </i> parameter specifies the new number of groups for the key. The <i>groups </i> parameter is a mask specifying the groups for which new types are supplied and is a bitwise inclusive OR of the following masks: XkbGroup1Mask, XkbGroup2Mask, XkbGroup3Mask, and XkbGroup4Mask. </p>
<p> The <i>new_types_in </i> parameter is an integer array of length <i>n_groups. </i> Each entry represents the type to use for the associated group and is an index into <i>xkb-&gt;map-&gt;types. </i> The <i>new_types_in </i> array is indexed by group index; if <i>n_groups </i> is four and <i>groups </i> only has Group1Mask and Group3Mask set, <i>new_types_in </i> looks like this: </p>
<pre> new_types_in[0] = type for Group1
 new_types_in[1] = ignored
 new_types_in[2] = type for Group3
 new_types_in[3] = ignored</pre>
<p>For convenience, Xkb provides the following constants to use as indices to the groups: </p>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=2>Table 1 Group Index Constants
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Constant Name</td>
<td>Value
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XkbGroup1Index</td>
<td>0
</td>
</tr>
<tr VALIGN=top>
<td>XkbGroup2Index</td>
<td>1
</td>
</tr>
<tr VALIGN=top>
<td>XkbGroup3Index</td>
<td>2
</td>
</tr>
<tr VALIGN=top>
<td>XkbGroup4Index</td>
<td>3
</td>
</tr>
</table>
<p> If the Xkb extension has not been properly initialized, <i>XkbChangeTypesOfKey </i> returns BadAccess. If the <i>xkb </i> parameter it not valid (that is, it is NULL or it does not contain a valid client map), <i>XkbChangeTypesOfKey </i> returns BadMatch. If the <i>key </i> is not a valid keycode, <i>n_groups </i> is greater than XkbNumKbdGroups, or the <i>groups </i> mask does not contain any of the valid group mask bits, <i>XkbChangeTypesOfKey </i> returns BadValue. If it is necessary to resize the key symbols or key actions arrays and any allocation errors occur, <i>XkbChangeTypesOfKey </i> returns BadAlloc.</p>
<h2>Structures</h2>
<p>Use the XkbMapChangesRec structure to identify and track partial modifications to the mapping components and to reduce the amount of traffic between the server and clients. </p>
<pre>typedef struct _XkbMapChanges {
 unsigned short changed; /* identifies valid components in 
structure */
 KeyCode min_key_code; /* lowest numbered keycode for device 
*/
 KeyCode max_key_code; /* highest numbered keycode for device 
*/
 unsigned char first_type; /* index of first key type modified */
 unsigned char num_types; /* # types modified */
 KeyCode first_key_sym; /* first key whose key_sym_map changed 
*/
 unsigned char num_key_syms; /* # key_sym_map entries changed */
 KeyCode first_key_act; /* first key whose key_acts entry 
changed */
 unsigned char num_key_acts; /* # key_acts entries changed */
 KeyCode first_key_behavior; /* first key whose behaviors changed */
 unsigned char num_key_behaviors; /* # behaviors entries changed */
 KeyCode first_key_explicit; /* first key whose explicit entry 
changed */
 unsigned char num_key_explicit; /* # explicit entries changed */
 KeyCode first_modmap_key; /* first key whose modmap entry changed 
*/
 unsigned char num_modmap_keys; /* # modmap entries changed */
 KeyCode first_vmodmap_key; /* first key whose vmodmap changed */
 unsigned char num_vmodmap_keys; /* # vmodmap entries changed */
 unsigned char pad1; /* reserved */
 unsigned short vmods; /* mask indicating which vmods changed 
*/
} XkbMapChangesRec,*XkbMapChangesPtr;</pre>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAccess</code></p>
<dd>The Xkb extension has not been properly initialized</p>
<dt><code>BadAlloc</code></p>
<dd>Unable to allocate storage</p>
<dt><code>BadMatch</code></p>
<dd>A compatible version of Xkb was not available in the server or an argument has correct type and range, but is otherwise invalid</p>
<dt><code>BadValue</code></p>
<dd>An argument is out of range </p>
</dl>
