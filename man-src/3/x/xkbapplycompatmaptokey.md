---
title: "xkbapplycompatmaptokey(3)"
name: "xkbapplycompatmaptokey"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbapplycompatmaptokey/"
description: "XkbApplyCompatMapToKey – Apply the new compatibility mapping to an individual key to get its semantics updated"
---

<p>XkbApplyCompatMapToKey &#8211; Apply the new compatibility mapping to an individual key to get its semantics updated </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Bool XkbApplyCompatMapToKey</code> <code>(XkbDescPtr </code><i>xkb</i><code>,</code> <code>KeyCode </code><i>key</i><code>,</code> <code>XkbChangesPtr </code><i>changes</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; xkb</i></p>
<dd>
<dd>keyboard description to be updated</p>
<dt><i>&#8211; key</i></p>
<dd>key to be updated</p>
<dt><i>&#8211; changes</i></p>
<dd>notes changes to the Xkb keyboard description</dl>
<h2>Description</h2>
<p><i>XkbApplyCompatMapToKey </i> essentially performs the operation described in Core Keyboard Mapping to Xkb Keyboard Mapping Transformation to a specific key. This updates the behavior, actions, repeat status, and virtual modifier bindings of the key. </p>
<p> <code>Core Keyboard Mapping to Xkb Keyboard Mapping Transformation</code> </p>
<p> When a core protocol keyboard mapping request is received by the server, the server&#8217;s core keyboard map is updated, and then the Xkb map maintained by the server is updated. Because a client may have explicitly configured some of the Xkb keyboard mapping in the server, this automatic regeneration of the Xkb keyboard mapping from the core protocol keyboard mapping should not modify any components of the Xkb keyboard mapping that were explicitly set by a client. The client must set explicit override controls to prevent this from happening (see Explicit Components-Avoiding Automatic Remapping by the Server). The core-to-Xkb mapping is done as follows: </p>
<p> <code>Explicit Components-Avoiding Automatic Remapping by the Server</code> </p>
<p> Whenever a client remaps the keyboard using core protocol requests, Xkb examines the map to determine likely default values for the components that cannot be specified using the core protocol. </p>
<p> This automatic remapping might replace definitions explicitly requested by an application, so the Xkb keyboard description defines an explicit components mask for each key. Any aspects of the automatic remapping listed in the explicit components mask for a key are not changed by the automatic keyboard mapping. </p>
<p> The explicit components masks are held in the <i>explicit </i> field of the server map, which is an array indexed by keycode. Each entry in this array is a mask that is a bitwise inclusive OR of the values shown in Table 1. </p>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=3>Table 1 Explicit Component Masks
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Bit in Explicit Mask</td>
<td>Value</td>
<td>Protects Against
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>ExplicitKeyType1</td>
<td>(1&lt;&lt;0)</td>
<td> Automatic determination of the key type associated with Group1.
</td>
</tr>
<tr VALIGN=top>
<td>ExplicitKeyType2</td>
<td>(1&lt;&lt;1)</td>
<td> Automatic determination of the key type associated with Group2.
</td>
</tr>
<tr VALIGN=top>
<td>ExplicitKeyType3</td>
<td>(1&lt;&lt;2)</td>
<td> Automatic determination of the key type associated with Group3.
</td>
</tr>
<tr VALIGN=top>
<td>ExplicitKeyType4</td>
<td>(1&lt;&lt;3)</td>
<td> Automatic determination of the key type associated with Group4.
</td>
</tr>
<tr VALIGN=top>
<td>ExplicitInterpret</td>
<td>(1&lt;&lt;4)</td>
<td> Application of any of the fields of a symbol interpretation to the key in question.
</td>
</tr>
<tr VALIGN=top>
<td>ExplicitAutoRepeat</td>
<td>(1&lt;&lt;5)</td>
<td> Automatic determination of auto-repeat status for the key, as specified in a symbol interpretation.
</td>
</tr>
<tr VALIGN=top>
<td>ExplicitBehavior</td>
<td>(1&lt;&lt;6)</td>
<td> Automatic assignment of the XkbKB_Lock behavior to the key, if the XkbSI_LockingKey flag is set in a symbol interpretation.
</td>
</tr>
<tr VALIGN=top>
<td>ExplicitVModMap</td>
<td>(1&lt;&lt;7)</td>
<td> Automatic determination of the virtual modifier map for the key based on the actions assigned to the key and the symbol interpretations that match the key.
</td>
</tr>
</table>
<dl COMPACT>
<dt>1.</p>
<dd>Map the symbols from the keys in the core keyboard map to groups and symbols on keys in the Xkb keyboard map. The core keyboard mapping is of fixed width, so each key in the core mapping has the same number of symbols associated with it. The Xkb mapping allows a different number of symbols to be associated with each key; those symbols may be divided into a different number of groups (1-4) for each key. For each key, this process therefore involves partitioning the fixed number of symbols from the core mapping into a set of variable-length groups with a variable number of symbols in each group. For example, if the core protocol map is of width five, the partition for one key might result in one group with two symbols and another with three symbols. A different key might result in two groups with two symbols plus a third group with one symbol. The core protocol map requires at least two symbols in each of the first two groups.</p>
<dt>1a.</p>
<dd>For each changed key, determine the number of groups represented in the new core keyboard map. This results in a tentative group count for each key in the Xkb map.</p>
<dt>1b.</p>
<dd>For each changed key, determine the number of symbols in each of the groups found in step 1a. There is one explicit override control associated with each of the four possible groups for each Xkb key, ExplicitKeyType1 through ExplicitKeyType4. If no explicit override control is set for a group, the number of symbols used for that group from the core map is two. If the explicit override control is set for a group on the key, the number of symbols used for that Xkb group from the core map is the width of the Xkb group with one exception: because of the core protocol requirement for at least two symbols in each of groups one and two, the number of symbols used for groups one and two is the maximum of 2 or the width of the Xkb group.</p>
<dt>1c.</p>
<dd>For each changed key, assign the symbols in the core map to the appropriate group on the key. If the total number of symbols required by the Xkb map for a particular key needs more symbols than the core protocol map contains, the additional symbols are taken to be NoSymbol keysyms appended to the end of the core set. If the core map contains more symbols than are needed by the Xkb map, trailing symbols in the core map are discarded. In the absence of an explicit override for group one or two, symbols are assigned in order by group; the first symbols in the core map are assigned to group one, in order, followed by group two, and so on. For example, if the core map contained eight symbols per key, and a particular Xkb map contained 2 symbols for G1 and G2 and three for G3, the symbols would be assigned as (G is group, L is shift level): </p>
<pre> G1L1 G1L2 G2L1 G2L2 G3L1 G3L2 G3L3</pre>
<p>If an explicit override control is set for group one or two, the symbols are taken from the core set in a somewhat different order. The first four symbols from the core set are assigned to G1L1, G1L2, G2L1, G2L2, respectively. If group one requires more symbols, they are taken next, and then any additional symbols needed by group two. Group three and four symbols are taken in complete sequence after group two. For example, a key with four groups and three symbols in each group would take symbols from the core set in the following order: </p>
<pre> G1L1 G1L2 G2L1 G2L2 G1L3 G2L3 G3L1 G3L2 G3L3 G4L1 G4L2 G4L3</pre>
<p>As previously noted, the core protocol map requires at lease two symbols in groups one and two. Because of this, if an explicit override control for an Xkb key is set and group one and / or group two is of width one, it is not possible to generate the symbols taken from the core protocol set and assigned to position G1L2 and / or G2L2.</p>
<dt>1d.</p>
<dd>For each group on each changed key, assign a key type appropriate for the symbols in the group.</p>
<dt>1e.</p>
<dd>For each changed key, remove any empty or redundant groups. </p>
<p> At this point, the groups and their associated symbols have been assigned to the corresponding key definitions in the Xkb map.</p>
<dt>2.</p>
<dd>Apply symbol interpretations to modify key operation. This phase is completely skipped if the ExplicitInterpret override control bit is set in the explicit controls mask for the Xkb key (see Explicit Components-Avoiding Automatic Remapping by the Server).</p>
<dt>2a.</p>
<dd>For each symbol on each changed key, attempt to match the symbol and modifiers from the Xkb map to a symbol interpretation describing how to generate the symbol.</p>
<dt>2b.</p>
<dd>When a match is found in step 2a, apply the symbol interpretation to change the semantics associated with the symbol in the Xkb key map. If no match is found, apply a default interpretation.</dl>
<p> The symbol interpretations used in step 2 are configurable and may be specified using XkbSymInterpretRec structures referenced by the sym_interpret field of an XkbCompatMapRec. </p>
<p> <code>Symbol Interpretations &#8211; the XkbSymInterpretRec Structure</code> </p>
<p> Symbol interpretations are used to guide the X server when it modifies the Xkb keymap in step 2. An initial set of symbol interpretations is loaded by the server when it starts. A client may add new ones using XkbSetCompatMap. </p>
<p> Symbol interpretations result in key semantics being set. When a symbol interpretation is applied, the following components of server key event processing may be modified for the particular key involved: </p>
<pre> Virtual modifier map
 Auto repeat
 Key behavior (may be set to XkbKB_Lock)
 Key action</pre>
<p>The XkbSymInterpretRec structure specifies a symbol interpretation: </p>
<pre>typedef struct {
 KeySym sym; /* keysym of interest or NULL */
 unsigned char flags; /* XkbSI_AutoRepeat, XkbSI_LockingKey */
 unsigned char match; /* specifies how mods is interpreted */
 unsigned char mods; /* modifier bits, correspond to eight real modifiers */
 unsigned char virtual_mod; /* 1 modifier to add to key virtual mod map */
 XkbAnyAction act; /* action to bind to symbol position on key */
} XkbSymInterpretRec,*XkbSymInterpretPtr;</pre>
<p>If sym is not NULL, it limits the symbol interpretation to keys on which that particular keysym is selected by the modifiers matching the criteria specified by <i>mods </i> and <i>match. </i> If <i>sym </i> is NULL, the interpretation may be applied to any symbol selected on a key when the modifiers match the criteria specified by <i>mods </i> and <i>match.</i> </p>
<p> <i>match </i> must be one of the values shown in Table 2 and specifies how the real modifiers specified in <i>mods </i> are to be interpreted. </p>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=3>Table 2 Symbol Interpretation Match Criteria
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Match Criteria</td>
<td>Value</td>
<td>Effect
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XkbSI_NoneOf</td>
<td>(0)</td>
<td> None of the bits that are on in mods can be set, but other bits can be.
</td>
</tr>
<tr VALIGN=top>
<td><a href="/docs/linux/man/1-xkbsi_anyofornone/">XkbSI_AnyOfOrNone</a></td>
<td>(1)</td>
<td> Zero or more of the bits that are on in mods can be set, as well as others.
</td>
</tr>
<tr VALIGN=top>
<td><a href="/docs/linux/man/2-xkbsi_anyof/">XkbSI_AnyOf</a></td>
<td>(2)</td>
<td> One or more of the bits that are on in mods can be set, as well as any others.
</td>
</tr>
<tr VALIGN=top>
<td><a href="/docs/linux/man/3-xkbsi_allof/">XkbSI_AllOf</a></td>
<td>(3)</td>
<td> All of the bits that are on in mods must be set, but others may be set as well.
</td>
</tr>
<tr VALIGN=top>
<td><a href="/docs/linux/man/4-xkbsi_exactly/">XkbSI_Exactly</a></td>
<td>(4)</td>
<td> All of the bits that are on in mods must be set, and no other bits may be set.
</td>
</tr>
</table>
<p> In addition to the above bits, <i>match </i> may contain the XkbSI_LevelOneOnly bit, in which case the modifier match criteria specified by <i>mods </i> and <i>match </i> applies only if <i>sym </i> is in level one of its group; otherwise, <i>mods </i> and <i>match </i> are ignored and the symbol matches a condition where no modifiers are set. </p>
<pre>#define XkbSI_LevelOneOnly (0x80) /* use mods + match only if sym is level 1 */</pre>
<p>If no matching symbol interpretation is found, the server uses a default interpretation where: </p>
<pre> sym = 0
 flags = XkbSI_AutoRepeat
 match = XkbSI_AnyOfOrNone
 mods = 0
 virtual_mod = XkbNoModifier
 act = SA_NoAction</pre>
<p>When a matching symbol interpretation is found in step 2a, the interpretation is applied to modify the Xkb map as follows. </p>
<p> The <i>act </i> field specifies a single action to be bound to the symbol position; any key event that selects the symbol causes the action to be taken. Valid actions are defined in Key Actions. </p>
<p> If the Xkb keyboard map for the key does not have its ExplicitVModMap control set, the XkbSI_LevelOneOnly bit and symbol position are examined. If the XkbSI_LevelOneOnly bit is not set in <i>match </i> or the symbol is in position G1L1, the <i>virtual_mod </i> field is examined. If <i>virtual_mod </i> is not XkbNoModifier, <i>virtual_mod </i> specifies a single virtual modifier to be added to the virtual modifier map for the key. <i>virtual_mod </i> is specified as an index in the range [0..15]. </p>
<p> If the matching symbol is in position G1L1 of the key, two bits in the flags field potentially specify additional behavior modifications: </p>
<pre>#define XkbSI_AutoRepeat (1&lt;&lt;0) /* key repeats if sym is in position G1L1 */
#define XkbSI_LockingKey (1&lt;&lt;1) /* set KB_Lock behavior if sym is in psn G1L1 */</pre>
<p>If the Xkb keyboard map for the key does not have its ExplicitAutoRepeat control set, its auto repeat behavior is set based on the value of the XkbSI_AutoRepeat bit. If the XkbSI_AutoRepeat bit is set, the auto-repeat behavior of the key is turned on; otherwise, it is turned off. </p>
<p> If the Xkb keyboard map for the key does not have its ExplicitBehavior control set, its locking behavior is set based on the value of the XkbSI_LockingKey bit. If XkbSI_LockingKey is set, the key behavior is set to KB_Lock; otherwise, it is turned off.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkbkeyaction/">XkbKeyAction</a></code>(3), <code><a href="/docs/linux/man/3-xkbkeyactionentry/">XkbKeyActionEntry</a></code>(3), <code><a href="/docs/linux/man/3-xkbkeyactionsptr/">XkbKeyActionsPtr</a></code>(3), <code><a href="/docs/linux/man/3-xkbkeyhasactions/">XkbKeyHasActions</a></code>(3), <code><a href="/docs/linux/man/3-xkbkeynumactions/">XkbKeyNumActions</a></code>(3)</p>
