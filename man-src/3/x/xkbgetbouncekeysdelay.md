---
title: "xkbgetbouncekeysdelay(3)"
name: "xkbgetbouncekeysdelay"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbgetbouncekeysdelay/"
description: "XkbGetBounceKeysDelay – Queries the current BounceKeys delay for a keyboard device."
---

<p>XkbGetBounceKeysDelay &#8211; Queries the current BounceKeys delay for a keyboard device. </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Bool XkbGetBounceKeysDelay</code> <code>(Display *</code><i>display</i><code>,</code> <code>unsigned int </code><i>device_spec</i><code>,</code> <code>unsigned int *</code><i>delay_rtrn</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; display</i></p>
<dd>
<dd>connection to X server</p>
<dt><i>&#8211; device_spec</i></p>
<dd>device ID, or XkbUseCoreKbd</p>
<dt><i>&#8211; delay_rtrn</i></p>
<dd>backfilled with bounce keys delay, ms</dl>
<h2>Description</h2>
<p>The server can generate XkbAccessXNotify events for some of the global keyboard controls. The detail field describes what AccessX event just occurred and can be any of the values in Table 1. </p>
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
<p> Some users may accidentally &quot;bounce&quot; on a key when they release it. They press it once, then accidentally press it again after they release it. The BounceKeys control temporarily disables a key after it has been pressed, effectively &quot;debouncing&quot; the keyboard. The period of time the key is disabled after it is released is known as the <i>BounceKeys delay. </i> BounceKeys is a boolean control. </p>
<p> When the BounceKeys control is active, the server reports acceptance or rejection of any key to interested clients by sending an appropriate AccessXNotify event (see STRUCTURES). </p>
<p> <i>XkbGetBounceKeysDelay </i> requests the attributes of the BounceKeys control from the server, waits for a reply, and backfills <i>delay_rtrn </i> with the BounceKeys delay attribute. <i>XkbGetBounceKeysDelay </i> returns True if successful; if a compatible version of the Xkb extension is not available in the server <i>XkbGetSlowKeysDelay </i> returns False.</p>
<h2>Return Values</h2>
<dl COMPACT>
<dt>True</p>
<dd>The <i>XkbGetBounceKeysDelay </i> function returns True when it successfully requests the attributes of the BounceKeys control from the server, waits for a reply, and backfills <i>delay_rtrn </i> with the BounceKeys delay attribute.</p>
<dt>False</p>
<dd>The <i>XkbGetBounceKeysDelay </i> function returns False if a compatible version of the Xkb extension is not available in the server.</dl>
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
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkbgetslowkeysdelay/">XkbGetSlowKeysDelay</a></code>(3)</p>
