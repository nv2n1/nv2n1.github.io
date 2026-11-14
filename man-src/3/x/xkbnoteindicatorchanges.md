---
title: "xkbnoteindicatorchanges(3)"
name: "xkbnoteindicatorchanges"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbnoteindicatorchanges/"
description: "XkbNoteIndicatorChanges – Notes the changes in a changes structure"
---

<p>XkbNoteIndicatorChanges &#8211; Notes the changes in a changes structure </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>void XkbNoteIndicatorChanges</code> <code>(XkbIndicatorChangesPtr </code><i>old</i><code>,</code> <code>XkbIndicatorNotifyEvent *</code><i>new</i><code>,</code> <code>unsigned int </code><i>wanted</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; old</i></p>
<dd>
<dd>XkbIndicatorChanges structure to be updated</p>
<dt><i>&#8211; new</i></p>
<dd>event from which changes are to be copied</p>
<dt><i>&#8211; wanted</i></p>
<dd>which changes are to be noted</dl>
<h2>Description</h2>
<p>Whenever an indicator changes state, the server sends XkbIndicatorStateNotify events to all interested clients. Similarly, whenever an indicator&#8217;s map changes, the server sends XkbIndicatorMapNotify events to all interested clients. </p>
<p> To receive XkbIndicatorStateNotify events, use <i>XkbSelectEvents </i> with both the <i>bits_to_change </i> and <i>values_for_bits </i> parameters containing XkbIndicatorStateNotifyMask. To receive XkbIndicatorMapNotify events, use <i>XkbSelectEvents </i> with XkbIndicatorMapNotifyMask. </p>
<p> To receive events for only specific indicators, use <i>XkbSelectEventDetails. </i> Set the <i>event_type </i> parameter to XkbIndicatorStateNotify or XkbIndicatorMapNotify, and set both the <i>bits_to_change </i> and <i>values_for_bits </i> detail parameters to a mask where each bit specifies one indicator, turning on those bits that specify the indicators for which you want to receive events. </p>
<p> The <i>changed </i> parameter is a mask that is the bitwise inclusive OR of the indicators that have changed. If the event is of type XkbIndicatorMapNotify, <i>changed </i> reports the maps that changed. If the event is of type XkbIndicatorStateNotify, <i>changed </i> reports the indicators that have changed state. <i>state </i> is a mask that specifies the current state of all indicators, whether they have changed or not, for both XkbIndicatorStateNotify and IndicatorMapNotify events. </p>
<p> When your client application receives either a XkbIndicatorStateNotify event or XkbIndicatorMapNotify event, you can note the changes in a changes structure by calling <i>XkbNoteIndicatorChanges.</i> </p>
<p> The <i>wanted </i> parameter is the bitwise inclusive OR of XkbIndicatorMapMask and XkbIndicatorStateMask. <i>XkbNoteIndicatorChanges </i> copies any changes reported in <i>new </i> and specified in <i>wanted </i> into the changes record specified by <i>old.</i></p>
<h2>Structures</h2>
<p>Both types of indicator events use the same structure: </p>
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
<p><i>xkb_type </i> is either XkbIndicatorStateNotify or XkbIndicatorMapNotify, depending on whether the event is a kbIndicatorStateNotify event or kbIndicatorMapNotify event.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkbindicatormapmask/">XkbIndicatorMapMask</a></code>(3), <code><a href="/docs/linux/man/3-xkbindicatorstatemask/">XkbIndicatorStateMask</a></code>(3), <code><a href="/docs/linux/man/3-xkbselecteventdetails/">XkbSelectEventDetails</a></code>(3), <code><a href="/docs/linux/man/3-xkbselectevents/">XkbSelectEvents</a></code>(3)</p>
