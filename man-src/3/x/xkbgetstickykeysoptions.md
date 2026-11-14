---
title: "xkbgetstickykeysoptions(3)"
name: "xkbgetstickykeysoptions"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbgetstickykeysoptions/"
description: "XkbGetStickyKeysOptions – Queries the current StickyKeys attributes for a keyboard device"
---

<p>XkbGetStickyKeysOptions &#8211; Queries the current StickyKeys attributes for a keyboard device </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Bool XkbGetStickyKeysOptions</code> <code>(Display *</code><i>display</i><code>,</code> <code>unsigned int </code><i>device_spec</i><code>,</code> <code>unsigned int *</code><i>options_rtrn</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; display</i></p>
<dd>
<dd>connection to X server</p>
<dt><i>&#8211; device_spec</i></p>
<dd>device ID, or XkbUseCoreKbd</p>
<dt><i>&#8211; options_rtrn</i></p>
<dd>backfilled with StickyKeys option mask</dl>
<h2>Description</h2>
<p>The StickyKeys control has two options that can be accessed via the <i>ax_options </i> of an XkbControlsRec structure. The first option, TwoKeys, specifies whether StickyKeys should automatically turn off when two keys are pressed at the same time. This feature is useful for shared computers so people who do not want them do not need to turn StickyKeys off if a previous user left StickyKeys on. The second option, LatchToLock, specifies whether or not StickyKeys locks a modifier when pressed twice in a row. </p>
<p> <i>XkbGetStickyKeysOptions </i> requests the attributes of the StickyKeys control from the server, waits for a reply, and backfills <i>options_rtrn </i> with a mask indicating whether the individual StickyKeys options are on or off. Valid bits in <i>options_rtrn </i> are: </p>
<pre> XkbAX_TwoKeysMask
 XkbAX_LatchToLockMask</pre>
<p><i>XkbGetStickyKeysOptions </i> returns True if successful; if a compatible version of the Xkb extension is not available in the server <i>XkbGetStickyKeysOptions </i> returns False.</p>
<h2>Return Values</h2>
<dl COMPACT>
<dt>True</p>
<dd>The <i>XkbGetStickyKeysOptions </i> function returns True if the request for the attributes of the StickyKeys control from the server was successful.</p>
<dt>False</p>
<dd>The <i>XkbGetStickyKeysOptions </i> function returns False if a compatible version of the Xkb extension is not available in the server.</dl>
<h2>Structures</h2>
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
