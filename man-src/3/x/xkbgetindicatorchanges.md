---
title: "xkbgetindicatorchanges(3)"
name: "xkbgetindicatorchanges"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbgetindicatorchanges/"
description: "XkbGetIndicatorChanges – Updates a local copy of the keyboard description with the actual values of one or more calls to XkbNoteIndicatorChanges"
---

<p>XkbGetIndicatorChanges &#8211; Updates a local copy of the keyboard description with the actual values of one or more calls to XkbNoteIndicatorChanges </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Status XkbGetIndicatorChanges</code> <code>(Display *</code><i>dpy</i><code>,</code> <code>XkbDescPtr </code><i>xkb</i><code>,</code> <code>XkbIndicatorChangesPtr </code><i>changes</i><code>,</code> <code>unsigned int </code><i>state</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; dpy</i></p>
<dd>
<dd>connection to the X server</p>
<dt><i>&#8211; xkb</i></p>
<dd>keyboard description to hold the new values</p>
<dt><i>&#8211; changes</i></p>
<dd>indicator maps/state to be obtained from the server</p>
<dt><i>&#8211; state</i></p>
<dd>backfilled with the state of the indicators</dl>
<h2>Description</h2>
<p>Whenever an indicator changes state, the server sends XkbIndicatorStateNotify events to all interested clients. Similarly, whenever an indicator&#8217;s map changes, the server sends XkbIndicatorMapNotify events to all interested clients. </p>
<p> To receive XkbIndicatorStateNotify events, use <i>XkbSelectEvents </i> with both the <i>bits_to_change </i> and <i>values_for_bits </i> parameters containing XkbIndicatorStateNotifyMask. To receive XkbIndicatorMapNotify events, use <i>XkbSelectEvents </i> with XkbIndicatorMapNotifyMask. </p>
<p> To receive events for only specific indicators, use <i>XkbSelectEventDetails. </i> Set the <i>event_type </i> parameter to XkbIndicatorStateNotify or XkbIndicatorMapNotify, and set both the <i>bits_to_change </i> and <i>values_for_bits </i> detail parameters to a mask where each bit specifies one indicator, turning on those bits that specify the indicators for which you want to receive events. </p>
<p> Both types of indicator events use the same structure: </p>
<pre>typedef struct _XkbIndicatorNotify {
 int type; /* Xkb extension base event code */
 unsigned long serial; /* X server serial number for event */
 Bool send_event; /* True =&gt; synthetically generated */
 Display * display; /* server connection where event generated */
 Time time; /* server time when event generated */
 int xkb_type; /* specifies state or map notify */
 int device; /* Xkb device ID, will not be XkbUseCoreKbd */
 unsigned int changed; /* mask of indicators with new state or map */
 unsigned int state; /* current state of all indicators */
} XkbIndicatorNotifyEvent;</pre>
<p><i>xkb_type </i> is either XkbIndicatorStateNotify or XkbIndicatorMapNotify, depending on whether the event is a kbIndicatorStateNotify event or kbIndicatorMapNotify event. </p>
<p> The <i>changed </i> parameter is a mask that is the bitwise inclusive OR of the indicators that have changed. If the event is of type XkbIndicatorMapNotify, <i>changed </i> reports the maps that changed. If the event is of type XkbIndicatorStateNotify, <i>changed </i> reports the indicators that have changed state. <i>state </i> is a mask that specifies the current state of all indicators, whether they have changed or not, for both XkbIndicatorStateNotify and IndicatorMapNotify events. </p>
<p> When your client application receives either a XkbIndicatorStateNotify event or XkbIndicatorMapNotify event, you can note the changes in a changes structure by calling <i>XkbNoteIndicatorChanges.</i> </p>
<p> <i>XkbGetIndicatorChanges </i> examines the <i>changes </i> parameter, pulls over the necessary information from the server, and copies the results into the <i>xkb </i> keyboard description. If any bits are set in the <i>state_changes </i> field of <i>changes, XkbGetIndicatorChanges </i> also places the state of those indicators in <i>state. </i> If the <i>indicators </i> field of <i>xkb </i> is NULL, <i>XkbGetIndicatorChanges </i> allocates and initializes it. To free the <i>indicators </i> field, use <i>XkbFreeIndicators.</i></p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAlloc</code></p>
<dd>Unable to allocate storage</p>
<dt><code>BadImplementation</code></p>
<dd>Invalid reply from server</p>
<dt><code>BadMatch</code></p>
<dd>A compatible version of Xkb was not available in the server or an argument has correct type and range, but is otherwise invalid</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkbfreeindicators/">XkbFreeIndicators</a></code>(3), <code><a href="/docs/linux/man/3-xkbgetindicatorchanges/">XkbGetIndicatorChanges</a></code>(3), <code><a href="/docs/linux/man/3-xkbnoteindicatorchanges/">XkbNoteIndicatorChanges</a></code>(3), <code><a href="/docs/linux/man/3-xkbselectevents/">XkbSelectEvents</a></code>(3), <code><a href="/docs/linux/man/3-xkbselecteventdetail/">XkbSelectEventDetail</a></code>(3)</p>
