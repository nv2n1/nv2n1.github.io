---
title: "xkbgetaccessxtimeout(3)"
name: "xkbgetaccessxtimeout"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbgetaccessxtimeout/"
description: "XkbGetAccessXTimeout – Queries the current AccessXTimeout options for a keyboard device"
---

<p>XkbGetAccessXTimeout &#8211; Queries the current AccessXTimeout options for a keyboard device </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Bool XkbGetAccessXTimeout</code> <code>(Display *</code><i>display</i><code>,</code> <code>unsigned int </code><i>device_spec</i><code>,</code> <code>unsigned short *</code><i>timeout_rtrn</i><code>,</code> <code>unsigned int *</code><i>ctrls_mask_rtrn</i><code>,</code> <code>unsigned int *</code><i>ctrls_values_rtrn</i><code>,</code> <code>unsigned short *</code><i>options_mask_rtrn</i><code>,</code> <code>unsigned short *</code><i>options_values_rtrn</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; display</i></p>
<dd>
<dd>unsigned short</p>
<dt><i>&#8211; device_spec</i></p>
<dd>device to query, or XkbUseCoreKbd</p>
<dt><i>&#8211; timeout_rtrn</i></p>
<dd>delay until AccessXTimeout, seconds</p>
<dt><i>&#8211; ctrls_mask_rtrn</i></p>
<dd>backfilled with controls to modify</p>
<dt><i>&#8211; ctrls_values_rtrn</i></p>
<dd>backfilled with on/off status for controls</p>
<dt><i>&#8211; options_mask_rtrn</i></p>
<dd>backfilled with ax_options to modify</p>
<dt><i>&#8211; options_values_rtrn</i></p>
<dd>backfilled with values for ax_options</dl>
<h2>Description</h2>
<p>In environments where computers are shared, features such as SlowKeys present a problem: if SlowKeys is on, the keyboard can appear to be unresponsive because keys are not accepted until they are held for a certain period of time. To help solve this problem, Xkb provides an AccessXTimeout control to automatically change the enabled/disabled state of any boolean controls and to change the value of the AccessXKeys and AccessXFeedback control attributes if the keyboard is idle for a specified period of time. </p>
<p> When a timeout as specified by AccessXTimeout occurs and a control is consequently modified, Xkb generates an XkbControlsNotify event. </p>
<p> <i>XkbGetAccessXTimeout </i> sends a request to the X server to obtain the current values for the AccessXTimeout attributes, waits for a reply, and backfills the values into the appropriate arguments. The parameters <i>options_mask_rtrn </i> and <i>options_values_rtrn </i> are backfilled with the options to modify and the values for <i>ax_options, </i> which is a field in the XkbControlsRec structure. <i>XkbGetAccessXTimeout </i> returns True if successful; if a compatible version of the Xkb extension is not available in the server, <i>XkbGetAccessXTimeout </i> returns False.</p>
<h2>Return Values</h2>
<dl COMPACT>
<dt>True</p>
<dd>The <i>XkbGetAccessXTimeout </i> returns True when it successfully sends a request to the X server to obtain the current values for the AccessXTimeout attributes, waits for a reply, and backfills the values into the appropriate arguments.</p>
<dt>False</p>
<dd>The <i>XkbGetAccessXTimeout </i> funtion returns False if a compatible version of the Xkb extension is not available in the server.</dl>
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
