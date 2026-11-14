---
title: "xkbsetdebuggingflags(3)"
name: "xkbsetdebuggingflags"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbsetdebuggingflags/"
description: "XkbSetDebuggingFlags – Change the values of any of the debug controls"
---

<p>XkbSetDebuggingFlags &#8211; Change the values of any of the debug controls </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Bool XkbSetDebuggingFlags</code> <code>(Display *</code><i>display</i><code>,</code> <code>unsigned int </code><i>mask</i><code>,</code> <code>unsigned int </code><i>flags</i><code>,</code> <code>char *</code><i>msg</i><code>,</code> <code>unsigned int </code><i>ctrls_mask</i><code>,</code> <code>unsigned int </code><i>ctrls</i><code>,</code> <code>unsigned int *</code><i>ret_flags</i><code>,</code> <code>unsigned int *</code><i>ret_ctrls</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; display</i></p>
<dd>
<dd>connection to X server</p>
<dt><i>&#8211; mask</i></p>
<dd>mask selecting debug output flags to change</p>
<dt><i>&#8211; flags</i></p>
<dd>values for debug output flags selected by mask</p>
<dt><i>&#8211; msg</i></p>
<dd>message to print right now</p>
<dt><i>&#8211; ctrls_mask</i></p>
<dd>mask selecting debug controls to change</p>
<dt><i>&#8211; ctrls</i></p>
<dd>values for debug controls selected by ctrls_mask</p>
<dt><i>&#8211; ret_flags</i></p>
<dd>resulting state of all debug output flags</p>
<dt><i>&#8211; ret_ctrls</i></p>
<dd>resulting state of all debug controls</dl>
<h2>Description</h2>
<p>The debugging aids are intended for use primarily by Xkb implementors and are optional in any implementation. </p>
<p> There are two bitmasks that may be used to control debugging. One bitmask controls the output of debugging information, and the other controls behavior. Both bitmasks are initially all zeros. </p>
<p> To change the values of any of the debug controls, use <i>XkbSetDebuggingFlags.</i> </p>
<p> <i>XkbSetDebuggingFlags </i> modifies the debug output flags as specified by <i>mask </i> and flags, modifies the debug controls flags as specified by <i>ctrls_mask </i> and ctrls, prints the message <i>msg, </i> and backfills <i>ret_flags </i> and <i>ret_ctrls </i> with the resulting debug output and debug controls flags. </p>
<p> When bits are set in the debug output masks, <i>mask </i> and <i>flags, </i> Xkb prints debug information corresponding to each bit at appropriate points during its processing. The device to which the output is written is implementation-dependent, but is normally the same device to which X server error messages are directed; thus the bits that can be set in <i>mask </i> and <i>flags </i> is implementation-specific. To turn on a debug output selection, set the bit for the output in the <i>mask </i> parameter and set the corresponding bit in the <i>flags </i> parameter. To turn off event selection for an event, set the bit for the output in the <i>mask </i> parameter and do not set the corresponding bit in the <i>flags </i> parameter. </p>
<p> When bits are set in the debug controls masks, <i>ctrls_mask </i> and <i>ctrls, </i> Xkb modifies its behavior according to each controls bit. <i>ctrls_mask </i> and ctrls are related in the same way that <i>mask </i> and <i>flags </i> are. The valid controls bits are defined in Table 1. </p>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=3>Table 1 Debug Control Masks
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Debug Control Mask</td>
<td>Value</td>
<td>Meaning
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XkbDF_DisableLocks</td>
<td>(1 &lt;&lt; 0)</td>
<td>Disable actions that lock modifiers
</td>
</tr>
</table>
<p> <i>XkbSetDebuggingFlags </i> returns True if successful and False otherwise. The only protocol error it may generate is BadAlloc, if for some reason it is unable to allocate storage. </p>
<p> <i>XkbSetDebuggingFlags </i> is intended for developer use and may be disabled in production X servers. If it is disabled, <i>XkbSetDebuggingFlags </i> has no effect and does not generate any protocol errors. </p>
<p> The message in <i>msg </i> is written immediately. The device to which it is written is implementation dependent but is normally the same device where X server error messages are directed.</p>
<h2>Return Values</h2>
<dl COMPACT>
<dt>True</p>
<dd>The <i>XkbSetDebuggingFlags </i> function returns True when successful.</p>
<dt>False</p>
<dd>The <i>XkbSetDebuggingFlags </i> function returns False when not successful.</dl>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAlloc</code></p>
<dd>Unable to allocate storage </p>
</dl>
