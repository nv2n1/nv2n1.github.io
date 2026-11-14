---
title: "xkbkeygroupinfo(3)"
name: "xkbkeygroupinfo"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbkeygroupinfo/"
description: "XkbKeyGroupInfo – Returns the number of groups of symbols bound to the key corresponding to keycode"
---

<p>XkbKeyGroupInfo &#8211; Returns the number of groups of symbols bound to the key corresponding to keycode </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>unsigned char XkbKeyGroupInfo</code> <code>(XkbDescPtr </code><i>xkb</i><code>,</code> <code>KeyCode </code><i>keycode</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; xkb</i></p>
<dd>
<dd>Xkb description of interest</p>
<dt><i>&#8211; keycode</i></p>
<dd>keycode of interest</dl>
<h2>Description</h2>
<p>The <i>group_info </i> field of an XkbSymMapRec is an encoded value containing the number of groups of symbols bound to the key as well as the specification of the treatment of out-of-range groups. It is legal for a key to have zero groups, in which case it also has zero symbols and all events from that key yield NoSymbol. To obtain the number of groups of symbols bound to the key, use <i>XkbKeyNumGroups. </i> To change the number of groups bound to a key, use <i>XkbChangeTypesOfKey. </i> To obtain a mask that determines the treatment of out-of-range groups, use <i>XkbKeyGroupInfo </i> and <i>XkbOutOfRangeGroupInfo.</i> </p>
<p> The keyboard controls contain a <i>groups_wrap </i> field specifying the handling of illegal groups on a global basis. That is, when the user performs an action causing the effective group to go out of the legal range, the <i>groups_wrap </i> field specifies how to normalize the effective keyboard group to a group that is legal for the keyboard as a whole, but there is no guarantee that the normalized group will be within the range of legal groups for any individual key. The per-key <i>group_info </i> field specifies how a key treats a legal effective group if the key does not have a type specified for the group of concern. For example, the Enter key usually has just one group defined. If the user performs an action causing the global keyboard group to change to Group2, the <i>group_info </i> field for the Enter key describes how to handle this situation. </p>
<p> Out-of-range groups for individual keys are mapped to a legal group using the same options as are used for the overall keyboard group. The particular type of mapping used is controlled by the bits set in the <i>group_info </i> flag, as shown in Table 1. </p>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=2>Table 1 group_info Range Normalization
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Bits set in group_info</td>
<td>Normalization method
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XkbRedirectIntoRange</td>
<td>XkbRedirectIntoRange
</td>
</tr>
<tr VALIGN=top>
<td>XkbClampIntoRange</td>
<td>XkbClampIntoRange
</td>
</tr>
<tr VALIGN=top>
<td>none of the above</td>
<td>XkbWrapIntoRange
</td>
</tr>
</table>
<p> <i>XkbKeyGroupInfo </i> returns the group_info field from the XkbSymMapRec structure associated with the key corresponding to <i>keycode.</i></p>
<h2>Structures</h2>
<p>The KeySymMapRec structure is defined as follows: </p>
<pre>#define XkbNumKbdGroups 4
#define XkbMaxKbdGroup (XkbNumKbdGroups-1)
 
typedef struct { /* map to keysyms for a single keycode */
 unsigned char kt_index[XkbNumKbdGroups]; /* key type index for each group */
 unsigned char group_info; /* # of groups and out of range group handling */
 unsigned char width; /* max # of shift levels for key */
 unsigned short offset; /* index to keysym table in syms array */
} XkbSymMapRec, *XkbSymMapPtr;</pre>
<pre>The XkbControlsRec structure is defined as follows:
#define XkbMaxLegalKeyCode 255
#define XkbPerKeyBitArraySize ((XkbMaxLegalKeyCode+1)/8)
 
typedef struct {
 unsigned char mk_dflt_btn; /* default button for keyboard driven mouse */
 unsigned char num_groups; /* number of keyboard groups */
 unsigned char groups_wrap; /* how to wrap out-of-bounds groups */
 XkbModsRec internal; /* defines server internal modifiers */
 XkbModsRec ignore_lock; /* modifiers to ignore when checking for grab */
 unsigned int enabled_ctrls; /* 1 bit =&gt; corresponding boolean control enabled */
 unsigned short repeat_delay; /* ms delay until first repeat */
 unsigned short repeat_interval; /* ms delay between repeats */
 unsigned short slow_keys_delay; /* ms minimum time key must be down to be ok */
 unsigned short debounce_delay; /* ms delay before key reactivated */
 unsigned short mk_delay; /* ms delay to second mouse motion event */
 unsigned short mk_interval; /* ms delay between repeat mouse events */
 unsigned short mk_time_to_max; /* # intervals until constant mouse move */
 unsigned short mk_max_speed; /* multiplier for maximum mouse speed */
 short mk_curve; /* determines mouse move curve type */
 unsigned short ax_options; /* 1 bit =&gt; Access X option enabled */
 unsigned short ax_timeout; /* seconds until Access X disabled */
 unsigned short axt_opts_mask; /* 1 bit =&gt; options to reset on Access X timeout */
 unsigned short axt_opts_values; /* 1 bit =&gt; turn option on, 0=&gt; off */
 unsigned int axt_ctrls_mask; /* which bits in enabled_ctrls to modify */
 unsigned int axt_ctrls_values; /* values for new bits in enabled_ctrls */
 unsigned char per_key_repeat[XkbPerKeyBitArraySize]; /* per key auto repeat */
} XkbControlsRec, *XkbControlsPtr;</pre>
<pre>The XkbControlsRec structure is defined as follows:
#define XkbMaxLegalKeyCode 255
#define XkbPerKeyBitArraySize ((XkbMaxLegalKeyCode+1)/8)
 
typedef struct {
 unsigned char mk_dflt_btn; /* default button for keyboard driven mouse */
 unsigned char num_groups; /* number of keyboard groups */
 unsigned char groups_wrap; /* how to wrap out-of-bounds groups */
 XkbModsRec internal; /* defines server internal modifiers */
 XkbModsRec ignore_lock; /* modifiers to ignore when checking for grab */
 unsigned int enabled_ctrls; /* 1 bit =&gt; corresponding boolean control enabled */
 unsigned short repeat_delay; /* ms delay until first repeat */
 unsigned short repeat_interval; /* ms delay between repeats */
 unsigned short slow_keys_delay; /* ms minimum time key must be down to be ok */
 unsigned short debounce_delay; /* ms delay before key reactivated */
 unsigned short mk_delay; /* ms delay to second mouse motion event */
 unsigned short mk_interval; /* ms delay between repeat mouse events */
 unsigned short mk_time_to_max; /* # intervals until constant mouse move */
 unsigned short mk_max_speed; /* multiplier for maximum mouse speed */
 short mk_curve; /* determines mouse move curve type */
 unsigned short ax_options; /* 1 bit =&gt; Access X option enabled */
 unsigned short ax_timeout; /* seconds until Access X disabled */
 unsigned short axt_opts_mask; /* 1 bit =&gt; options to reset on Access X timeout */
 unsigned short axt_opts_values; /* 1 bit =&gt; turn option on, 0=&gt; off */
 unsigned int axt_ctrls_mask; /* which bits in enabled_ctrls to modify */
 unsigned int axt_ctrls_values; /* values for new bits in enabled_ctrls */
 unsigned char per_key_repeat[XkbPerKeyBitArraySize]; /* per key auto repeat */
} XkbControlsRec, *XkbControlsPtr;</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkbchangetypesofkey/">XkbChangeTypesOfKey</a></code>(3), <code><a href="/docs/linux/man/3-xkbkeygroupinfo/">XkbKeyGroupInfo</a></code>(3), <code><a href="/docs/linux/man/3-xkboutofrangegroupinfo/">XkbOutOfRangeGroupInfo</a></code>(3)</p>
