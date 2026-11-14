---
title: "xreparentevent(3)"
name: "xreparentevent"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xreparentevent/"
description: "XReparentEvent – ReparentNotify event structure"
---

<p>XReparentEvent &#8211; ReparentNotify event structure </p>
<h2>Structures</h2>
<p>The structure for <code>ReparentNotify</code> events contains: </p>
<p> typedef struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int type;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;ReparentNotify&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long serial;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;#&nbsp;of last request processed by server&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Bool send_event;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;true if this came from a SendEvent request&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Display&nbsp;*display;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Display the event was read from&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Window event;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Window window;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Window parent;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int x, y;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Bool override_redirect; } XReparentEvent; </p>
<p> When you receive this event, the structure members are set as follows. </p>
<p> The type member is set to the event type constant name that uniquely identifies it. For example, when the X server reports a <code>GraphicsExpose</code> event to a client application, it sends an <code>XGraphicsExposeEvent</code> structure with the type member set to <code>GraphicsExpose</code>. The display member is set to a pointer to the display the event was read on. The send_event member is set to <code>True</code> if the event came from a <code>SendEvent</code> protocol request. The serial member is set from the serial number reported in the protocol but expanded from the 16-bit least-significant bits to a full 32-bit value. The window member is set to the window that is most useful to toolkit dispatchers. </p>
<p> The event member is set either to the reparented window or to the old or the new parent, depending on whether <code>StructureNotify</code> or <code>SubstructureNotify</code> was selected. The window member is set to the window that was reparented. The parent member is set to the new parent window. The x and y members are set to the reparented window&#8217;s coordinates relative to the new parent window&#8217;s origin and define the upper-left outer corner of the reparented window. The override_redirect member is set to the override-redirect attribute of the window specified by the window member. Window manager clients normally should ignore this window if the override_redirect member is <code>True</code>.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xanyevent/">XAnyEvent</a>(3), <a href="/docs/linux/man/3-xbuttonevent/">XButtonEvent</a>(3), <a href="/docs/linux/man/3-xcreatewindowevent/">XCreateWindowEvent</a>(3), <a href="/docs/linux/man/3-xcirculateevent/">XCirculateEvent</a>(3), <a href="/docs/linux/man/3-xcirculaterequestevent/">XCirculateRequestEvent</a>(3), <a href="/docs/linux/man/3-xcolormapevent/">XColormapEvent</a>(3), <a href="/docs/linux/man/3-xconfigureevent/">XConfigureEvent</a>(3), <a href="/docs/linux/man/3-xconfigurerequestevent/">XConfigureRequestEvent</a>(3), <a href="/docs/linux/man/3-xcrossingevent/">XCrossingEvent</a>(3), <a href="/docs/linux/man/3-xdestroywindowevent/">XDestroyWindowEvent</a>(3), <a href="/docs/linux/man/3-xerrorevent/">XErrorEvent</a>(3), <a href="/docs/linux/man/3-xexposeevent/">XExposeEvent</a>(3), <a href="/docs/linux/man/3-xfocuschangeevent/">XFocusChangeEvent</a>(3), <a href="/docs/linux/man/3-xgraphicsexposeevent/">XGraphicsExposeEvent</a>(3), <a href="/docs/linux/man/3-xgravityevent/">XGravityEvent</a>(3), <a href="/docs/linux/man/3-xkeymapevent/">XKeymapEvent</a>(3), <a href="/docs/linux/man/3-xmapevent/">XMapEvent</a>(3), <a href="/docs/linux/man/3-xmaprequestevent/">XMapRequestEvent</a>(3), <a href="/docs/linux/man/3-xpropertyevent/">XPropertyEvent</a>(3), <a href="/docs/linux/man/3-xresizerequestevent/">XResizeRequestEvent</a>(3), <a href="/docs/linux/man/3-xselectionclearevent/">XSelectionClearEvent</a>(3), <a href="/docs/linux/man/3-xselectionevent/">XSelectionEvent</a>(3), <a href="/docs/linux/man/3-xselectionrequestevent/">XSelectionRequestEvent</a>(3), <a href="/docs/linux/man/3-xunmapevent/">XUnmapEvent</a>(3), <a href="/docs/linux/man/3-xvisibilityevent/">XVisibilityEvent</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
