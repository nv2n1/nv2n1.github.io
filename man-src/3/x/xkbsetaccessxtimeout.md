---
title: "xkbsetaccessxtimeout(3)"
name: "xkbsetaccessxtimeout"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbsetaccessxtimeout/"
description: "XkbSetAccessXTimeout – Configures the AccessXTimeout options for a keyboard device"
---

<p>XkbSetAccessXTimeout &#8211; Configures the AccessXTimeout options for a keyboard device </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Bool XkbSetAccessXTimeout</code> <code>(Display *</code><i>display</i><code>,</code> <code>unsigned int </code><i>device_spec</i><code>,</code> <code>unsigned short </code><i>timeout</i><code>,</code> <code>unsigned int </code><i>ctrls_mask</i><code>,</code> <code>unsigned int </code><i>ctrls_values</i><code>,</code> <code>unsigned short </code><i>opts_mask</i><code>,</code> <code>unsigned short </code><i>opts_values</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; display</i></p>
<dd>
<dd>connection to X server</p>
<dt><i>&#8211; device_spec</i></p>
<dd>device to configure, or XkbUseCoreKbd</p>
<dt><i>&#8211; timeout</i></p>
<dd>seconds idle until AccessXTimeout occurs</p>
<dt><i>&#8211; ctrls_mask</i></p>
<dd>boolean controls to modify</p>
<dt><i>&#8211; ctrls_values</i></p>
<dd>new bits for controls selected by ctrls_mask</p>
<dt><i>&#8211; opts_mask</i></p>
<dd>ax_options to change</p>
<dt><i>&#8211; opts_values</i></p>
<dd>new bits for ax_options selected by opts_mask</dl>
<h2>Description</h2>
<p>In environments where computers are shared, features such as SlowKeys present a problem: if SlowKeys is on, the keyboard can appear to be unresponsive because keys are not accepted until they are held for a certain period of time. To help solve this problem, Xkb provides an AccessXTimeout control to automatically change the enabled/disabled state of any boolean controls and to change the value of the AccessXKeys and AccessXFeedback control attributes if the keyboard is idle for a specified period of time. </p>
<p> When a timeout as specified by AccessXTimeout occurs and a control is consequently modified, Xkb generates an XkbControlsNotify event. For more information on XkbControlsNotify events. </p>
<p> <i>timeout </i> specifies the number of seconds the keyboard must be idle before the controls are modified. <i>ctrls_mask </i> specifies what controls are to be enabled or disabled, and <i>ctrls_values </i> specifies whether those controls are to be enabled or disabled. The bit values correspond to those for enabling and disabling boolean controls using <i>XkbChangeEnabledControls.</i><br />
&nbsp;The&nbsp; <i>opts_mask </i> field specifies which attributes of the AccessXKeys and AccessXFeedback controls are to be changed, and <i>opts_values </i> specifies the new values for those options. The bit values correspond to those for the <i>ax_options </i> field of an XkbDescRec. </p>
<p> <i>XkbSetAccessXTimeout </i> sends a request to configure the AccessXTimeout control to the server. It does not wait for a reply, and normally returns True. If a compatible version of the Xkb extension is not available in the server, <i>XkbSetAccessXTimeout </i> returns False.</p>
<h2>Return Values</h2>
<dl COMPACT>
<dt>True</p>
<dd>The <i>XkbSetAccessXTimeout</i> function returns True when a compatible version of the Xkb extension is available in the server.</p>
<dt>False</p>
<dd>The <i>XkbSetAccessXTimeout</i> function returns False when a compatible version of the Xkb extension is not available in the server.</dl>
<h2>Structures</h2>
<p>The complete description of an Xkb keyboard is given by an XkbDescRec. The component structures in the XkbDescRec represent the major Xkb components. </p>
<pre>typedef struct {
 struct _XDisplay * display; /* connection to X server */
 unsigned short flags; /* private to Xkb, do not modify */
 unsigned short device_spec; /* device of interest */
 KeyCode min_key_code; /* minimum keycode for device */
 KeyCode max_key_code; /* maximum keycode for device */
 XkbControlsPtr ctrls; /* controls */
 XkbServerMapPtr server; /* server keymap */
 XkbClientMapPtr map; /* client keymap */
 XkbIndicatorPtr indicators; /* indicator map */
 XkbNamesPtr names; /* names for all components */
 XkbCompatMapPtr compat; /* compatibility map */
 XkbGeometryPtr geom; /* physical geometry of keyboard */
} XkbDescRec, *XkbDescPtr;</pre>
<p>The <i>display </i> field points to an X display structure. The <i>flags field is private to the library: modifying </i> <i>flags </i> may yield unpredictable results. The <i>device_spec </i> field specifies the device identifier of the keyboard input device, or XkbUseCoreKeyboard, which specifies the core keyboard device. The <i>min_key_code</i> and <i>max_key_code </i> fields specify the least and greatest keycode that can be returned by the keyboard. </p>
<p> Each structure component has a corresponding mask bit that is used in function calls to indicate that the structure should be manipulated in some manner, such as allocating it or freeing it. These masks and their relationships to the fields in the XkbDescRec are shown in Table 1. </p>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=3>Table 1 Mask Bits for XkbDescRec
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Mask Bit</td>
<td>XkbDescRec Field</td>
<td>Value
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XkbControlsMask</td>
<td>ctrls</td>
<td>(1L&lt;&lt;0)
</td>
</tr>
<tr VALIGN=top>
<td>XkbServerMapMask</td>
<td>server</td>
<td>(1L&lt;&lt;1)
</td>
</tr>
<tr VALIGN=top>
<td>XkbIClientMapMask</td>
<td>map</td>
<td>(1L&lt;&lt;2)
</td>
</tr>
<tr VALIGN=top>
<td>XkbIndicatorMapMask</td>
<td>indicators</td>
<td>(1L&lt;&lt;3)
</td>
</tr>
<tr VALIGN=top>
<td>XkbNamesMask</td>
<td>names</td>
<td>(1L&lt;&lt;4)
</td>
</tr>
<tr VALIGN=top>
<td>XkbCompatMapMask</td>
<td>compat</td>
<td>(1L&lt;&lt;5)
</td>
</tr>
<tr VALIGN=top>
<td>XkbGeometryMask</td>
<td>geom</td>
<td>(1L&lt;&lt;6)
</td>
</tr>
<tr VALIGN=top>
<td>XkbAllComponentsMask</td>
<td>All Fields</td>
<td>(0x7f)
</td>
</tr>
</table>
<p> The structure for the XkbControlsNotify event is defined as follows: </p>
<pre> typedef struct {
 int type; /* Xkb extension base event code */
 unsigned long serial; /* X server serial number for event */
 Bool send_event; /* True =&gt; synthetically generated */
 Display * display; /* server connection where event generated */
 Time time; /* server time when event generated */
 int xkb_type; /* XkbCompatMapNotify */
 int device; /* Xkb device ID, will not be XkbUseCoreKbd */
 unsigned int changed_ctrls; /* bits indicating which controls data have changed*/
 unsigned int enabled_ctrls; /* controls currently enabled in server */
 unsigned int enabled_ctrl_changes; /* bits indicating enabled/disabled controls */
 int num_groups; /* current number of keyboard groups */
 KeyCode keycode; /* != 0 =&gt; keycode of key causing change */
 char event_type; /* Type of event causing change */
 char req_major; /* major event code of event causing change */
 char req_minor; /* minor event code of event causing change */
 } XkbControlsNotifyEvent;</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkbchangeenabledcontrols/">XkbChangeEnabledControls</a></code>(3)</p>
