---
title: "xkbselectevents(3)"
name: "xkbselectevents"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbselectevents/"
description: "XkbSelectEvents – Selects and / or deselects for delivery of one or more Xkb events and has them delivered under all conditions"
---

<p>XkbSelectEvents &#8211; Selects and / or deselects for delivery of one or more Xkb events and has them delivered under all conditions </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Bool XkbSelectEvents</code> <code>(Display *</code><i>display</i><code>,</code> <code>unsigned int </code><i>device_spec</i><code>,</code> <code>unsigned long int </code><i>bits_to_change</i><code>,</code> <code>unsigned long int </code><i>values_for_bits</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>
<dd>connection to the X server</p>
<dt><i>device_spec</i></p>
<dd>device ID, or XkbUseCoreKbd</p>
<dt><i>bits_to_change</i></p>
<dd>determines events to be selected / deselected</p>
<dt><i>values_for_bits</i></p>
<dd>1=&gt;select, 0-&gt;deselect; for events in bits_to_change</dl>
<h2>Description</h2>
<p>Xkb events are selected using an event mask, much the same as normal core X events are selected. However, unlike selecting core X events, where you must specify the selection status (on or off) for all possible event types whenever you wish to change the selection criteria for any one event, Xkb allows you to restrict the specification to only the event types you wish to change. This means that you do not need to remember the event selection values for all possible types each time you want to change one of them. </p>
<p> Many Xkb event types are generated under several different circumstances. When selecting to receive an Xkb event, you may specify either that you want it delivered under all circumstances, or that you want it delivered only for a subset of the possible circumstances. </p>
<p> You can also deselect an event type that was previously selected for, using the same granularity. </p>
<p> Xkb provides two functions to select and deselect delivery of Xkb events. <i>XkbSelectEvents </i> allows you to select or deselect delivery of more than one Xkb event type at once. Events selected using <i>XkbSelectEvents </i> are delivered to your program under all circumstances that generate the events. To restrict delivery of an event to a subset of the conditions under which it occurs, use <i>XkbSelectEventDetails. XkbSelectEventDetails </i> only allows you to change the selection conditions for a single event at a time, but it provides a means of fine-tuning the conditions under which the event is delivered. </p>
<p> This request changes the Xkb event selection mask for the keyboard specified by <i>device_spec.</i> </p>
<p> Each Xkb event that can be selected is represented by a bit in the <i>bits_to_change </i> and <i>values_for_bits </i> masks. Only the event selection bits specified by the <i>bits_to_change </i> parameter are affected; any unspecified bits are left unchanged. To turn on event selection for an event, set the bit for the event in the <i>bits_to_change </i> parameter and set the corresponding bit in the <i>values_for_bits </i> parameter. To turn off event selection for an event, set the bit for the event in the <i>bits_to_change </i> parameter and do not set the corresponding bit in the <i>values_for_bits </i> parameter. The valid values for both of these parameters are an inclusive bitwise OR of the masks shown in Table 1. There is no interface to return your client&#8217;s current event selection mask. Clients cannot set other clients&#8217; event selection masks. </p>
<p> The X server reports the events defined by Xkb to your client application only if you have requested them via a call to <i>XkbSelectEvents </i> or <i>XkbSelectEventDetails. </i> Specify the event types in which you are interested in a mask. </p>
<p> Table 1 lists the event mask constants that can be specified with the <i>XkbSelectEvents </i> request and the circumstances in which the mask should be specified. </p>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=3>Table 1 XkbSelectEvents Mask Constants
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Event Mask</td>
<td>Value</td>
<td>Notification Wanted
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XkbNewKeyboardNotifyMask</td>
<td>(1L&lt;&lt;0)</td>
<td>Keyboard geometry change
</td>
</tr>
<tr VALIGN=top>
<td>XkbMapNotifyMask</td>
<td>(1L&lt;&lt;1)</td>
<td>Keyboard mapping change
</td>
</tr>
<tr VALIGN=top>
<td>XkbStateNotifyMask</td>
<td>(1L&lt;&lt;2)</td>
<td>Keyboard state change
</td>
</tr>
<tr VALIGN=top>
<td>XkbControlsNotifyMask</td>
<td>(1L&lt;&lt;3)</td>
<td>Keyboard control change
</td>
</tr>
<tr VALIGN=top>
<td>XkbIndicatorStateNotifyMask</td>
<td>(1L&lt;&lt;4)</td>
<td>Keyboard indicator state change
</td>
</tr>
<tr VALIGN=top>
<td>XkbIndicatorMapNotifyMask</td>
<td>(1L&lt;&lt;5)</td>
<td>Keyboard indicator map change
</td>
</tr>
<tr VALIGN=top>
<td>XkbNamesNotifyMask</td>
<td>(1L&lt;&lt;6)</td>
<td>Keyboard name change
</td>
</tr>
<tr VALIGN=top>
<td>XkbCompatMapNotifyMask</td>
<td>(1L&lt;&lt;7)</td>
<td>Keyboard compat map change
</td>
</tr>
<tr VALIGN=top>
<td>XkbBellNotifyMask</td>
<td>(1L&lt;&lt;8)</td>
<td>Bell
</td>
</tr>
<tr VALIGN=top>
<td>XkbActionMessageMask</td>
<td>(1L&lt;&lt;9)</td>
<td>Action message
</td>
</tr>
<tr VALIGN=top>
<td>XkbAccessXNotifyMask</td>
<td>(1L&lt;&lt;10)</td>
<td>AccessX features
</td>
</tr>
<tr VALIGN=top>
<td>XkbExtensionDeviceNotifyMask</td>
<td>(1L&lt;&lt;11)</td>
<td>Extension device
</td>
</tr>
<tr VALIGN=top>
<td>XkbAllEventsMask</td>
<td>(0xFFF)</td>
<td>All Xkb events
</td>
</tr>
</table>
<p>&nbsp; If a bit is not set in the <i>bits_to_change </i> parameter, but the corresponding bit is set in the <i>values_for_bits </i> parameter, a BadMatch protocol error results. If an undefined bit is set in either the <i>bits_to_change </i> or the <i>values_for_bits </i> parameter, a BadValue protocol error results. </p>
<p> All event selection bits are initially zero for clients using the Xkb extension. Once you set some bits, they remain set for your client until you clear them via another call to <i>XkbSelectEvents. </i> </p>
<p> <i>XkbSelectEvents </i> returns False if the Xkb extension has not been initilialized and True otherwise.</p>
<h2>Return Values</h2>
<dl COMPACT>
<dt>True</p>
<dd>The <i>XkbSelectEvents </i> function returns True if the Xkb extension has been initilialized.</p>
<dt>False</p>
<dd>The <i>XkbSelectEvents </i> function returns False if the Xkb extension has not been initilialized.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkbselecteventdetails/">XkbSelectEventDetails</a></code>(3), <code><a href="/docs/linux/man/3-xkbusecorekbd/">XkbUseCoreKbd</a></code>(3)</p>
