---
title: "tk_createclientmessagehandler(3)"
name: "tk_createclientmessagehandler"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_createclientmessagehandler/"
description: "Tk_CreateClientMessageHandler, Tk_DeleteClientMessageHandler – associate procedure callback with ClientMessage type X events"
---

<p>Tk_CreateClientMessageHandler, Tk_DeleteClientMessageHandler &#8211; associate procedure callback with ClientMessage type X events </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
<code>Tk_CreateClientMessageHandler</code>(<i>proc</i>)
<code>Tk_DeleteClientMessageHandler</code>(<i>proc</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tk_ClientMessageProc <i>*proc</i> (in) Procedure to invoke whenever a ClientMessage X event occurs on any display. </p>
</dl>
<h2>Description</h2>
<p><code>Tk_CreateClientMessageHandler</code> arranges for <i>proc</i> to be invoked in the future whenever a ClientMessage X event occurs that is not handled by <code>WM_PROTOCOL</code>. <code>Tk_CreateClientMessageHandler</code> is intended for use by applications which need to watch X ClientMessage events, such as drag and drop applications. </p>
<p> The callback to <i>proc</i> will be made by <code>Tk_HandleEvent</code>; this mechanism only works in programs that dispatch events through <code>Tk_HandleEvent</code> (or through other Tk procedures that call <code>Tk_HandleEvent</code>, such as <code>Tk_DoOneEvent</code> or <code>Tk_MainLoop</code>). </p>
<p> <i>Proc</i> should have arguments and result that match the type <code>Tk_ClientMessageProc</code>:</p>
<dl COMPACT>
<dd>
<pre>typedef int Tk_ClientMessageProc(
 Tk_Window <i>tkwin</i>,
 XEvent *<i>eventPtr</i>);</pre>
</dl>
<p> The <i>tkwin</i> parameter to <i>proc</i> is the Tk window which is associated with this event. <i>EventPtr</i> is a pointer to the X event. </p>
<p> Whenever an X ClientMessage event is processed by <code>Tk_HandleEvent</code>, the <i>proc</i> is called if it was not handled as a <code>WM_PROTOCOL</code>. The return value from <i>proc</i> is normally 0. A non-zero return value indicates that the event is not to be handled further; that is, <i>proc</i> has done all processing that is to be allowed for the event. </p>
<p> If there are multiple ClientMessage event handlers, each one is called for each event, in the order in which they were established. </p>
<p> <code>Tk_DeleteClientMessageHandler</code> may be called to delete a previously-created ClientMessage event handler: it deletes each handler it finds that matches the <i>proc</i> argument. If no such handler exists, then <code>Tk_DeleteClientMessageHandler</code> returns without doing anything. Although Tk supports it, it&#8217;s probably a bad idea to have more than one callback with the same <i>proc</i> argument. </p>
<h2>Keywords</h2>
<p>bind, callback, event, handler</p>
