---
title: "xselectionevent(3)"
name: "xselectionevent"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xselectionevent/"
description: "XSelectionEvent – SelectionNotify event structure"
---

<p>XSelectionEvent &#8211; SelectionNotify event structure </p>
<h2>Structures</h2>
<p>The structure for <code>SelectionNotify</code> events contains: </p>
<p> typedef struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int type;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;SelectionNotify&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long serial;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;#&nbsp;of last request processed by server&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Bool send_event;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;true if this came from a SendEvent request&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Display&nbsp;*display;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Display the event was read from&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Window requestor;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Atom selection;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Atom target;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Atom property;&nbsp;<wbr>&nbsp;/*&nbsp;atom or None&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Time time; } XSelectionEvent; </p>
<p> When you receive this event, the structure members are set as follows. </p>
<p> The type member is set to the event type constant name that uniquely identifies it. For example, when the X server reports a <code>GraphicsExpose</code> event to a client application, it sends an <code>XGraphicsExposeEvent</code> structure with the type member set to <code>GraphicsExpose</code>. The display member is set to a pointer to the display the event was read on. The send_event member is set to <code>True</code> if the event came from a <code>SendEvent</code> protocol request. The serial member is set from the serial number reported in the protocol but expanded from the 16-bit least-significant bits to a full 32-bit value. The window member is set to the window that is most useful to toolkit dispatchers. </p>
<p> The requestor member is set to the window associated with the requestor of the selection. The selection member is set to the atom that indicates the selection. For example, PRIMARY is used for the primary selection. The target member is set to the atom that indicates the converted type. For example, PIXMAP is used for a pixmap. The property member is set to the atom that indicates which property the result was stored on. If the conversion failed, the property member is set to <code>None</code>. The time member is set to the time the conversion took place and can be a timestamp or <code>CurrentTime</code>.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xanyevent/">XAnyEvent</a>(3), <a href="/docs/linux/man/3-xbuttonevent/">XButtonEvent</a>(3), <a href="/docs/linux/man/3-xcreatewindowevent/">XCreateWindowEvent</a>(3), <a href="/docs/linux/man/3-xcirculateevent/">XCirculateEvent</a>(3), <a href="/docs/linux/man/3-xcirculaterequestevent/">XCirculateRequestEvent</a>(3), <a href="/docs/linux/man/3-xcolormapevent/">XColormapEvent</a>(3), <a href="/docs/linux/man/3-xconfigureevent/">XConfigureEvent</a>(3), <a href="/docs/linux/man/3-xconfigurerequestevent/">XConfigureRequestEvent</a>(3), <a href="/docs/linux/man/3-xcrossingevent/">XCrossingEvent</a>(3), <a href="/docs/linux/man/3-xdestroywindowevent/">XDestroyWindowEvent</a>(3), <a href="/docs/linux/man/3-xerrorevent/">XErrorEvent</a>(3), <a href="/docs/linux/man/3-xexposeevent/">XExposeEvent</a>(3), <a href="/docs/linux/man/3-xfocuschangeevent/">XFocusChangeEvent</a>(3), <a href="/docs/linux/man/3-xgraphicsexposeevent/">XGraphicsExposeEvent</a>(3), <a href="/docs/linux/man/3-xgravityevent/">XGravityEvent</a>(3), <a href="/docs/linux/man/3-xkeymapevent/">XKeymapEvent</a>(3), <a href="/docs/linux/man/3-xmapevent/">XMapEvent</a>(3), <a href="/docs/linux/man/3-xmaprequestevent/">XMapRequestEvent</a>(3), <a href="/docs/linux/man/3-xpropertyevent/">XPropertyEvent</a>(3), <a href="/docs/linux/man/3-xreparentevent/">XReparentEvent</a>(3), <a href="/docs/linux/man/3-xresizerequestevent/">XResizeRequestEvent</a>(3), <a href="/docs/linux/man/3-xselectionclearevent/">XSelectionClearEvent</a>(3), <a href="/docs/linux/man/3-xselectionrequestevent/">XSelectionRequestEvent</a>(3), <a href="/docs/linux/man/3-xunmapevent/">XUnmapEvent</a>(3), <a href="/docs/linux/man/3-xvisibilityevent/">XVisibilityEvent</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
