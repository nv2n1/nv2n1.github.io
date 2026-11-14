---
title: "xkbgetslowkeysdelay(3)"
name: "xkbgetslowkeysdelay"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbgetslowkeysdelay/"
description: "XkbGetSlowKeysDelay – Gets the SlowKeys acceptance delay for a keyboard device"
---

<p>XkbGetSlowKeysDelay &#8211; Gets the SlowKeys acceptance delay for a keyboard device </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Bool XkbGetSlowKeysDelay</code> <code>(Display *</code><i>display</i><code>,</code> <code>unsigned int </code><i>device_spec</i><code>,</code> <code>unsigned int *</code><i>delay_rtrn</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; display</i></p>
<dd>
<dd>connection to X server</p>
<dt><i>&#8211; device_spec</i></p>
<dd>device ID, or XkbUseCoreKbd</p>
<dt><i>&#8211; delay_rtrn</i></p>
<dd>backfilled with SlowKeys delay, ms</dl>
<h2>Description</h2>
<p>Some users may accidentally bump keys while moving a hand or typing stick toward the key they want. Usually, the keys that are accidentally bumped are just hit for a very short period of time. The SlowKeys control helps filter these accidental bumps by telling the server to wait a specified period, called the <i>SlowKeys acceptance delay, </i> before delivering key events. If the key is released before this period elapses, no key events are generated. Users can then bump any number of keys on their way to the one they want without accidentally getting those characters. Once they have reached the key they want, they can then hold the desired key long enough for the computer to accept it. SlowKeys is a boolean control with one configurable attribute. </p>
<p> When the SlowKeys control is active, the server reports the initial key press, subsequent acceptance or rejection, and release of any key to interested clients by sending an appropriate AccessXNotify event (see section 10.6.4). </p>
<p> The server can generate XkbAccessXNotify events for some of the global keyboard controls. The detail field describes what AccessX event just occurred and can be any of the values in Table 1. The server can generate XkbAccessXNotify events for some of the global keyboard controls. The detail field describes what AccessX event just occurred and can be any of the values in Table 1. </p>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=2>Table 1 AccessXNotify Events
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>detail</td>
<td>Reason
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XkbAXN_SKPress</td>
<td> A key was pressed when SlowKeys was enabled.
</td>
</tr>
<tr VALIGN=top>
<td>XkbAXN_SKAccept</td>
<td> A key was accepted (held longer than the SlowKeys delay).
</td>
</tr>
<tr VALIGN=top>
<td>XkbAXN_SKRelease</td>
<td> An accepted SlowKeys key was released.
</td>
</tr>
<tr VALIGN=top>
<td>XkbAXN_SKReject</td>
<td> A key was rejected (released before the SlowKeys delay expired).
</td>
</tr>
<tr VALIGN=top>
<td>XkbAXN_BKAccept</td>
<td> A key was accepted by BounceKeys.
</td>
</tr>
<tr VALIGN=top>
<td>XkbAXN_BKReject</td>
<td> A key was rejected (pressed before the BounceKeys delay expired).
</td>
</tr>
<tr VALIGN=top>
<td>XkbAXN_AXKWarning</td>
<td> AccessXKeys is about to turn on/off StickyKeys or BounceKeys.
</td>
</tr>
</table>
<p> The <i>keycode </i> field reports the keycode of the key for which the event occurred. If the action is related to <i>SlowKeys, </i> the <i>slowKeysDelay </i> field contains the current SlowKeys acceptance delay. If the action is related to BounceKeys, the <i>debounceDelay </i> field contains the current BounceKeys debounce delay. </p>
<p> Selecting for AccessX Events </p>
<p> To receive XkbAccessXNotify events under all possible conditions, use <i>XkbSelectEvents</i> and pass XkbAccesXNotifyMask in both <i>bits_to_change </i> and <i>values_for_bits.</i> </p>
<p> To receive XkbStateNotify events only under certain conditions, use <i>XkbSelectEventDetails </i> using XkbAccessXNotify as the <i>event_type </i> and specifying the desired state changes in <i>bits_to_change </i> and <i>values_for_bits </i> using mask bits from Table 2. </p>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=3>Table 2 AccessXNotify Event Details
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XkbAccessXNotify Event Details</td>
<td>Value</td>
<td>Circumstances
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XkbAXN_SKPressMask</td>
<td>(1&lt;&lt;0)</td>
<td> Slow key press notification wanted
</td>
</tr>
<tr VALIGN=top>
<td>XkbAXN_SKAcceptMask</td>
<td>(1&lt;&lt;1)</td>
<td> Slow key accept notification wanted
</td>
</tr>
<tr VALIGN=top>
<td>XkbAXN_SKRejectMask</td>
<td>(1&lt;&lt;2)</td>
<td> Slow key reject notification wanted
</td>
</tr>
<tr VALIGN=top>
<td>XkbAXN_SKReleaseMask</td>
<td>(1&lt;&lt;3)</td>
<td> Slow key release notification wanted
</td>
</tr>
<tr VALIGN=top>
<td>XkbAXN_BKAcceptMask</td>
<td>(1&lt;&lt;4)</td>
<td> Bounce key accept notification wanted
</td>
</tr>
<tr VALIGN=top>
<td>XkbAXN_BKRejectMask</td>
<td>(1&lt;&lt;5)</td>
<td> Bounce key reject notification wanted
</td>
</tr>
<tr VALIGN=top>
<td>XkbAXN_AXKWarningMask</td>
<td>(1&lt;&lt;6)</td>
<td> AccessX warning notification wanted
</td>
</tr>
<tr VALIGN=top>
<td>XkbAllAccessXEventsMask</td>
<td>(0x7f)</td>
<td> All AccessX features notifications wanted
</td>
</tr>
</table>
<p> <i>XkbGetSlowKeysDelay </i> requests the attributes of the SlowKeys control from the server, waits for a reply and backfills <i>delay_rtrn </i> with the SlowKeys delay attribute. <i>XkbGetSlowKeysDelay </i> returns True if successful; , <i>XkbGetSlowKeysDelay </i> returns False.</p>
<h2>Return Values</h2>
<dl COMPACT>
<dt>True</p>
<dd>The <i>XkbGetSlowKeysDelay </i> function returns True if the request of the Slowkeys control from the server was successful. <i></p>
<dt>False</p>
<dd></i> The <i>XkbGetSlowKeysDelay </i> function returns False if a compatible version of the Xkb extension is not available in the server.</dl>
<h2>Structures</h2>
<p>The structure for the XkbAccessXNotify event type is as follows: </p>
<pre>typedef struct {
 int type; /* Xkb extension base event code */
 unsigned long serial; /* X server serial number for event */
 Bool send_event; /* True =&gt; synthetically generated */
 Display * display; /* server connection where event generated */
 Time time; /* server time when event generated */
 int xkb_type; /* XkbAccessXNotify */
 int device; /* Xkb device ID, will not be XkbUseCoreKbd 
*/
 int detail; /* XkbAXN_* */
 KeyCode keycode; /* key of event */
 int slowKeysDelay; /* current SlowKeys delay */
 int debounceDelay; /* current debounce delay */
} XkbAccessXNotifyEvent;</pre>
