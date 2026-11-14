---
title: "dmxgetinputattributes(3)"
name: "dmxgetinputattributes"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dmxgetinputattributes/"
description: "DMXGetInputAttributes – determine input device attributes"
---

<p>DMXGetInputAttributes &#8211; determine input device attributes</p>
<h2>Synopsis</h2>
<p><code>#include &lt;<a href="file:/usr/include/X11/extensions/dmxext.h">X11/extensions/dmxext.h</a>&gt;</code> </p>
<pre><code>Bool DMXGetInputAttributes(Display </code><i>*dpy</i><code>,</code>
<code> int </code><i>id</i><code>,</code>
<code> DMXInputAttributes </code><i>*attr</i><code>);</code></pre>
<h2>Description</h2>
<p><code>DMXGetInputAttributes()</code> returns information about the input device specified with <i>id</i>. This information cannot be obtained from the <code><a href="/docs/linux/man/3-xlistinputdeivices/">XListInputDeivices</a></code>(3) call. <i>id</i> is the same as that used by the <code><a href="/docs/linux/man/3-xlistinputdevices/">XListInputDevices</a></code>(3) call, and must be in the range 0 to one less than the value returned by <code><a href="/docs/linux/man/3-dmxgetinputcount/">DMXGetInputCount</a>(3)</code>, inclusive. </p>
<p> The <code>DMXInputAttributes</code> structure is: </p>
<pre>typedef struct {
 DMXInputEnum inputType;
 int physicalScreen;
 int physicalId;
 Bool isCore;
 Bool sendsCore;
 const char *name;
 Bool detached;
} DMXInputAttributes;</pre>
<p>The value of <i>inputType</i> will always be valid, and will have one of the following values, depending on the type of input: <code>DMXLocalInputType , DMXConsoleInputType , or DMXBackendInputType .</code> </p>
<p> For local devices, all other fields returned, except <i>isCore and sendsCore ,</i> are invalid. </p>
<p> For console devices, <i>physicalScreen and physicalID</i> will be invalid, and <i>name</i> will return the name of the X server on which the console window is displayed. </p>
<p> For back-end devices, <i>physicalScreen</i> will identify the back-end display and can be used as an argument to <code><a href="/docs/linux/man/3-dmxgetscreenattributes/">DMXGetScreenAttributes</a></code>(3) to obtain more information; <i>physicalId</i> will be the XInput device id on the back-end X server; and <i>name</i> will be invalid (since it does not provide any additional information that cannot be obtained with <code><a href="/docs/linux/man/3-dmxgetscreenattributes/">DMXGetScreenAttributes</a></code>(3)). </p>
<p> If <i>isCore</i> is <code>True</code>, then this device is active as a true core input device and will send core events. If <code>sendsCore</code> is True, then this device is an XInput extension device, but sends core events <i>instead</i> of extension events. This behavior is different from that of XFree86 or Xorg, where XInput extension devices may send <i>both</i> extension events and core events. </p>
<p> If <i>detached</i> is True, then this device has been detached and is no longer producing input events. The device may be reattached using <code><a href="/docs/linux/man/3-dmxaddinput/">DMXAddInput</a></code>(3).</p>
<h2>Return Value</h2>
<p><code>DMXGetInputAttributes()</code> returns <code>True</code> unless there is a protocol error. </p>
<p> <code>DMXGetInputAttributes()</code> can generate <code>BadValue</code> (if the value of <i>id</i> is out of range).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-dmxgetinputcount/">DMXGetInputCount</a></code>(3), <code><a href="/docs/linux/man/3-xlistinputdevices/">XListInputDevices</a></code>(3), <code><a href="/docs/linux/man/3-dmxgetscreenattributes/">DMXGetScreenAttributes</a></code>(3), <code><a href="/docs/linux/man/3-dmxaddinput/">DMXAddInput</a></code>(3), <code><a href="/docs/linux/man/3-dmx/">DMX</a></code>(3), <code><a href="/docs/linux/man/1-xdmx/">Xdmx</a></code>(1)</p>
