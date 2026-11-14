---
title: "xkbselecteventdetails(3)"
name: "xkbselecteventdetails"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbselecteventdetails/"
description: "XkbSelectEventDetails – Selects or deselects for a specific Xkb event and optionally places conditions on when events of that type are reported to your client"
---

<p>XkbSelectEventDetails &#8211; Selects or deselects for a specific Xkb event and optionally places conditions on when events of that type are reported to your client </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Bool XkbSelectEventDetails</code> <code>(Display *</code><i>display</i><code>,</code> <code>unsigned int </code><i>device_spec</i><code>,</code> <code>unsigned int </code><i>event_type</i><code>,</code> <code>unsigned long int </code><i>bits_to_change</i><code>,</code> <code>unsigned long int </code><i>values_for_bits</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>
<dd>connection to the X server</p>
<dt><i>device_spec</i></p>
<dd>device ID, or XkbUseCoreKbd</p>
<dt><i>event_type</i></p>
<dd>Xkb event type of interest</p>
<dt><i>bits_to_change</i></p>
<dd>determines events to be selected / deselected</p>
<dt><i>values_for_bits</i></p>
<dd>1=&gt;select, 0-&gt;deselect; for events in bits_to_change</dl>
<h2>Description</h2>
<p>Xkb events are selected using an event mask, much the same as normal core X events are selected. However, unlike selecting core X events, where you must specify the selection status (on or off) for all possible event types whenever you wish to change the selection criteria for any one event, Xkb allows you to restrict the specification to only the event types you wish to change. This means that you do not need to remember the event selection values for all possible types each time you want to change one of them. </p>
<p> Many Xkb event types are generated under several different circumstances. When selecting to receive an Xkb event, you may specify either that you want it delivered under all circumstances, or that you want it delivered only for a subset of the possible circumstances.<br />
&nbsp; You can also deselect an event type that was previously selected for, using the same granularity. </p>
<p> Xkb provides two functions to select and deselect delivery of Xkb events. <i>XkbSelectEvents </i> allows you to select or deselect delivery of more than one Xkb event type at once. Events selected using <i>XkbSelectEvents </i> are delivered to your program under all circumstances that generate the events. To restrict delivery of an event to a subset of the conditions under which it occurs, use <i>XkbSelectEventDetails. XkbSelectEventDetails </i> only allows you to change the selection conditions for a single event at a time, but it provides a means of fine-tuning the conditions under which the event is delivered. </p>
<p> To select or deselect for a specific Xkb event and optionally place conditions on when events of that type are reported to your client, use <i>XkbSelectEventDetails. </i> This allows you to exercise a finer granularity of control over delivery of Xkb events with <i>XkbSelectEvents.</i> </p>
<p> While <i>XkbSelectEvents </i> allows multiple events to be selected, <i>XkbSelectEventDetails </i> changes the selection criteria for a single type of Xkb event. The interpretation of the <i>bits_to_change </i> and <i>values_for_bits </i> masks depends on the event type in question.<br />
&nbsp; <i>XkbSelectEventDetails </i> changes the Xkb event selection mask for the keyboard specified by <i>device_spec </i> and the Xkb event specified by <i>event_type. </i> To turn on event selection for an event detail, set the bit for the detail in the <i>bits_to_change </i> parameter and set the corresponding bit in the <i>values_for_bits </i> parameter. To turn off event detail selection for a detail, set the bit for the detail in the <i>bits_to_change </i> parameter and do not set the corresponding bit in the <i>values_for_bits </i> parameter. </p>
<p> If an invalid event type is specified, a BadValue protocol error results. If a bit is not set in the <i>bits_to_change </i> parameter, but the corresponding bit is set in the <i>values_for_bits </i> parameter, a BadMatch protocol error results. If an undefined bit is set in either the <i>bits_to_change </i> or the <i>values_for_bits </i> parameter, a BadValue protocol error results. </p>
<p> For each type of Xkb event, the legal event details that you can specify in the <i>XkbSelectEventDetails </i> request are listed in the chapters that describe each event in detail.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><font SIZE="-1">BadMatch</font></p>
<dd>A compatible version of Xkb was not available in the server or an argument has correct type and range, but is otherwise invalid</p>
<dt><font SIZE="-1">BadValue</font></p>
<dd>An argument is out of range</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkbselectevents/">XkbSelectEvents</a></code>(3), <code><a href="/docs/linux/man/3-xkbusecorekbd/">XkbUseCoreKbd</a></code>(3)</p>
