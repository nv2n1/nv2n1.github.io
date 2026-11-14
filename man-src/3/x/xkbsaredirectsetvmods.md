---
title: "xkbsaredirectsetvmods(3)"
name: "xkbsaredirectsetvmods"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbsaredirectsetvmods/"
description: "XkbSARedirectSetVMods – Sets the vmods0 and vmods1 of act from v"
---

<p>XkbSARedirectSetVMods &#8211; Sets the vmods0 and vmods1 of act from v </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>void XkbSARedirectSetVMods</code> <code>(XkbRedirectKeyAction </code><i>act</i><code>,</code> <code>unsigned int </code><i>v</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; act</i></p>
<dd>
<dd>action in which to set vmods</p>
<dt><i>&#8211; v</i></p>
<dd>new value for virtual modifiers</dl>
<h2>Description</h2>
<p>Actions associated with the XkbRedirectKeyAction structure generate KeyPress and KeyRelease events containing a keycode different from the key that was pressed or released. </p>
<p> The <i>type </i> field for the XkbRedirectKeyAction structure should always be XkbSA_RedirectKey. Key presses cause a KeyPress event for the key specified by the <i>new_key </i> field instead of the actual key. The state reported in this event reports the current effective modifiers changed as follows: any real modifiers selected by the <i>mods_mask </i> field are set to corresponding values from the <i>mods </i> field. Any real modifiers bound to the virtual modifiers specified by the <i>vmods_mask0 </i> and <i>vmods_mask1 </i> fields are either set or cleared, depending on the corresponding values in the <i>vmods0 </i> and <i>vmods1 </i> fields. If the real and virtual modifier definitions specify conflicting values for a single modifier, the real modifier definition has priority. </p>
<p> Key releases cause a KeyRelease event for the key specified by the <i>new_key </i> field instead of the actual key. The state for this event consists of the effective keyboard modifiers at the time of the release, changed as described previously. </p>
<p> The XkbSA_RedirectKey action normally redirects to another key on the same device as the key that caused the event, unless that device does not belong to the input extension KeyClass, in which case this action causes an event on the core keyboard device. (The input extension categorizes devices by breaking them into classes. Keyboards, and other input devices with keys, are classified as KeyClass devices by the input extension.) </p>
<p> The <i>vmods_mask0 </i> and <i>vmods_mask1 </i> fields actually represent one <i>vmods_mask </i> value. Xkb provides macros to convert between the two formats. </p>
<p> <i>XkbSARedirectSetVModsMask </i> sets the <i>vmods0 </i> and <i>vmods1 </i> of <i>act </i> from <i>v.</i></p>
<h2>Structures</h2>
<pre> typedef struct_XkbRedirectKeyAction {
 unsigned char type; /* XkbSA_RedirectKey */
 unsigned char new_key; /* keycode to be put in event */
 unsigned char mods_mask; /* mask of real mods to be reset */
 unsigned char mods; /* mask of real mods to take values from */
 unsigned char vmods_mask0; /* first half of mask of virtual mods to be reset */
 unsigned char vmods_mask1; /* other half of mask of virtual mods to be reset */
 unsigned char vmods0; /* first half of mask of virtual mods to take values from */
 unsigned char vmods1; /* other half of mask of virtual mods to take values from */
 } XkbRedirectKeyAction;</pre>
