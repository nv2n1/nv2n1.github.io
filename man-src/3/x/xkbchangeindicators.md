---
title: "xkbchangeindicators(3)"
name: "xkbchangeindicators"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbchangeindicators/"
description: "XkbChangeIndicators – Changes indicator maps or state without passing the entire keyboard description"
---

<p>XkbChangeIndicators &#8211; Changes indicator maps or state without passing the entire keyboard description </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Bool XkbChangeIndicators</code> <code>(Display *</code><i>dpy</i><code>,</code> <code>XkbDescPtr </code><i>xkb</i><code>,</code> <code>XkbIndicatorChangesPtr </code><i>changes</i><code>,</code> <code>unsigned int </code><i>state</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; dpy</i></p>
<dd>
<dd>connection to the X server</p>
<dt><i>&#8211; xkb</i></p>
<dd>keyboard description from which names are to be taken.</p>
<dt><i>&#8211; changes</i></p>
<dd>indicators to be updated on the server</p>
<dt><i>&#8211; state</i></p>
<dd>new state of indicators listed in changes-&gt;state_changes</dl>
<h2>Description</h2>
<p>The XkbIndicatorChangesRec identifies small modifications to the indicator map. Use it with the function <i>XkbChangeIndicators </i> to reduce the amount of traffic sent to the server (see STRUCTURES).<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp; The <i>state_changes </i> field is a mask that specifies the indicators that have changed state, and <i>map_changes </i> is a mask that specifies the indicators whose maps have changed. </p>
<p> <i>XkbChangeIndicators </i> copies any maps specified by <i>changes </i> from the keyboard description, <i>xkb, </i> to the server specified by <i>dpy. </i> If any bits are set in the <i>state_changes </i> field of <i>changes, XkbChangeIndicators </i> also sets the state of those indicators to the values specified in the <i>state </i> mask. A 1 bit in <i>state </i> turns the corresponding indicator on, a 0 bit turns it off. </p>
<p> In addition, it can also generate XkbIndicatorStateNotify and XkbIndicatorMapNotify events. </p>
<p> Whenever an indicator changes state, the server sends XkbIndicatorStateNotify events to all interested clients. Similarly, whenever an indicator&#8217;s map changes, the server sends XkbIndicatorMapNotify events to all interested clients. </p>
<p> To receive XkbIndicatorStateNotify events, use <i>XkbSelectEvents </i> with both the <i>bits_to_change </i> and <i>values_for_bits </i> parameters containing XkbIndicatorStateNotifyMask. To receive XkbIndicatorMapNotify events, use <i>XkbSelectEvents </i> with XkbIndicatorMapNotifyMask. </p>
<p> To receive events for only specific indicators, use <i>XkbSelectEventDetails. </i> Set the <i>event_type </i> parameter to XkbIndicatorStateNotify or XkbIndicatorMapNotify, and set both the <i>bits_to_change </i> and <i>values_for_bits </i> detail parameters to a mask where each bit specifies one indicator, turning on those bits that specify the indicators for which you want to receive events. </p>
<p> <i>xkb_type </i> is either XkbIndicatorStateNotify or XkbIndicatorMapNotify, depending on whether the event is a kbIndicatorStateNotify event or kbIndicatorMapNotify event. </p>
<p> The <i>changed </i> parameter is a mask that is the bitwise inclusive OR of the indicators that have changed. If the event is of type XkbIndicatorMapNotify, <i>changed </i> reports the maps that changed. If the event is of type XkbIndicatorStateNotify, <i>changed </i> reports the indicators that have changed state. <i>state </i> is a mask that specifies the current state of all indicators, whether they have changed or not, for both XkbIndicatorStateNotify and IndicatorMapNotify events.</p>
<h2>Structures</h2>
<pre> typedef struct _XkbIndicatorChanges {
 unsigned int state_changes;
 unsigned int map_changes;
 }XkbIndicatorChangesRec,*XkbIndicatorChangesPtr;</pre>
<p>Both types of indicator events use the same structure: </p>
<pre> typedef struct _XkbIndicatorNotify {
 int type; /* Xkb extension base event code */
 unsigned long serial; /* X server serial number for event */
 Bool send_event; /* True =&gt; synthetically generated */
 Display * display; /* server connection where event generated */
 Time time; /* server time when event generated */
 int xkb_type; /* specifies state or map notify */
 int device; /* Xkb device ID, will not be XkbUseCoreKbd*/
 unsigned int changed; /* mask of indicators with new state or map */
 unsigned int state; /* current state of all indicators */
 } XkbIndicatorNotifyEvent;</pre>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAtom</code></p>
<dd>A name is neither a valid Atom or None</p>
<dt><code>BadImplementation</code></p>
<dd>Invalid reply from server</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkbindicatormapnotify/">XkbIndicatorMapNotify</a></code>(3), <code><a href="/docs/linux/man/3-xkbindicatorstatenotify/">XkbIndicatorStateNotify</a></code>(3)</p>
