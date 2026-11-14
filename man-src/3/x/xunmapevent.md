---
title: "xunmapevent(3)"
name: "xunmapevent"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xunmapevent/"
description: "XUnmapEvent – UnmapNotify event structure"
---

<p>XUnmapEvent &#8211; UnmapNotify event structure </p>
<h2>Structures</h2>
<p>The structure for <code>UnmapNotify</code> events contains: </p>
<p> typedef struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int type;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;UnmapNotify&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long serial;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;#&nbsp;of last request processed by server&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Bool send_event;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;true if this came from a SendEvent request&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Display&nbsp;*display;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Display the event was read from&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Window event;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Window window;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Bool from_configure; } XUnmapEvent; </p>
<p> When you receive this event, the structure members are set as follows. </p>
<p> The type member is set to the event type constant name that uniquely identifies it. For example, when the X server reports a <code>GraphicsExpose</code> event to a client application, it sends an <code>XGraphicsExposeEvent</code> structure with the type member set to <code>GraphicsExpose</code>. The display member is set to a pointer to the display the event was read on. The send_event member is set to <code>True</code> if the event came from a <code>SendEvent</code> protocol request. The serial member is set from the serial number reported in the protocol but expanded from the 16-bit least-significant bits to a full 32-bit value. The window member is set to the window that is most useful to toolkit dispatchers. </p>
<p> The event member is set either to the unmapped window or to its parent, depending on whether <code>StructureNotify</code> or <code>SubstructureNotify</code> was selected. This is the window used by the X server to report the event. The window member is set to the window that was unmapped. The from_configure member is set to <code>True</code> if the event was generated as a result of a resizing of the window&#8217;s parent when the window itself had a win_gravity of <code>UnmapGravity</code>.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xanyevent/">XAnyEvent</a>(3), <a href="/docs/linux/man/3-xbuttonevent/">XButtonEvent</a>(3), <a href="/docs/linux/man/3-xcreatewindowevent/">XCreateWindowEvent</a>(3), <a href="/docs/linux/man/3-xcirculateevent/">XCirculateEvent</a>(3), <a href="/docs/linux/man/3-xcirculaterequestevent/">XCirculateRequestEvent</a>(3), <a href="/docs/linux/man/3-xcolormapevent/">XColormapEvent</a>(3), <a href="/docs/linux/man/3-xconfigureevent/">XConfigureEvent</a>(3), <a href="/docs/linux/man/3-xconfigurerequestevent/">XConfigureRequestEvent</a>(3), <a href="/docs/linux/man/3-xcrossingevent/">XCrossingEvent</a>(3), <a href="/docs/linux/man/3-xdestroywindowevent/">XDestroyWindowEvent</a>(3), <a href="/docs/linux/man/3-xerrorevent/">XErrorEvent</a>(3), <a href="/docs/linux/man/3-xexposeevent/">XExposeEvent</a>(3), <a href="/docs/linux/man/3-xfocuschangeevent/">XFocusChangeEvent</a>(3), <a href="/docs/linux/man/3-xgraphicsexposeevent/">XGraphicsExposeEvent</a>(3), <a href="/docs/linux/man/3-xgravityevent/">XGravityEvent</a>(3), <a href="/docs/linux/man/3-xkeymapevent/">XKeymapEvent</a>(3), <a href="/docs/linux/man/3-xmapevent/">XMapEvent</a>(3), <a href="/docs/linux/man/3-xmaprequestevent/">XMapRequestEvent</a>(3), <a href="/docs/linux/man/3-xpropertyevent/">XPropertyEvent</a>(3), <a href="/docs/linux/man/3-xreparentevent/">XReparentEvent</a>(3), <a href="/docs/linux/man/3-xresizerequestevent/">XResizeRequestEvent</a>(3), <a href="/docs/linux/man/3-xselectionclearevent/">XSelectionClearEvent</a>(3), <a href="/docs/linux/man/3-xselectionevent/">XSelectionEvent</a>(3), <a href="/docs/linux/man/3-xselectionrequestevent/">XSelectionRequestEvent</a>(3), <a href="/docs/linux/man/3-xvisibilityevent/">XVisibilityEvent</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
