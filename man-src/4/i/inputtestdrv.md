---
title: "inputtestdrv(4)"
name: "inputtestdrv"
section: "4"
letter: "i"
url: "/docs/linux/man/4-inputtestdrv/"
description: "inputtest – An X.Org input driver for testing"
---

<p>inputtest &#8211; An X.Org input driver for testing</p>
<h2>Synopsis</h2>
<pre><code>Section &#34;InputDevice&#34;</code>
<code> Identifier &#34;</code><i>devname</i><code>&#34;</code>
<code> Driver &#34;inputtest&#34;</code>
<code> Option &#34;SocketPath&#34; &#34;</code><i>path</i><code>&#34;</code>
&nbsp;<wbr>&nbsp;...
<code>EndSection</code></pre>
<h2>Description</h2>
<p><code>inputtest</code> is an Xorg input driver that passes events received over a socket on to the server as input events. It supports the full set of the xf86 driver APIs exposed by Xorg. The primary use cases of this input driver are various integration tests that need to interface with the input subsystem. </p>
<h2>Configuration Details</h2>
<p>Please refer to <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5) for general configuration details and for options that can be used with all input drivers. This section only covers configuration details specific to this driver. </p>
<p> External process can communicate with the input driver via a named socket that is created after the driver is initialized. The paths to the socket is passed via input driver options. </p>
<p> The following driver <code>Options</code> are supported:</p>
<dl>
<dt><code>Option &#34;SocketPath&#34; &#34;</code><i>string</i><code>&#34;</code></p>
<dd>Sets the path where the driver will create a named socket. Any existing file at that location will be removed.</p>
<dt><code>Option &#34;DeviceType&#34; &#34;</code><i>string</i><code>&#34;</code></p>
<dd>Sets the type of the device to be emulated.</p>
<dd><code>Keyboard</code> Initializes a keyboard device.</p>
<dd><code>Pointer</code> Initializes a relative-mode pointer device. It will have four valuators &#8211; a &quot;Rel X&quot; valuator at axis 0 and a &quot;Rel Y&quot; valuator at axis 1. A horizontal scroll valuator will be set up at axis 2. A vertical scroll valuator will be set up at axis 3.</p>
<dd><code>PointerAbsolute</code> Initializes an absolute-mode pointer device. It will have four valuators &#8211; an &quot;Abs X&quot; valuator at axis 0 and an &quot;Abs Y&quot; valuator at axis 1. A horizontal scroll valuator will be set up at axis 2. A vertical scroll valuator will be set up at axis 3.</p>
<dd><code>PointerAbsoluteProximity</code> Initializes an absolute-mode pointer device with proximity support. The valuators are initialized in the same way as for <code>PointerAbsolute</code> type.</p>
<dd><code>Touch</code> Initializes a touch device. It will have 5 valuators: an &quot;Abs MT Position X&quot; at axis 0, an &quot;Abs MT Position Y&quot; valuator at axis 1, a horizontal scroll valuator on axis 2, a vertical scroll valuator on axis 3 and an &quot;Abs MT Pressure&quot; valuator at axis 4.</p>
<dt><code>Option &#34;TouchCount&#34; &#34;</code><i>int</i><code>&#34;</code></p>
<dd>Sets the maximum number of simultaneous touches for touch devices.</p>
<dt><code>Option &#34;PointerButtonCount&#34; &#34;</code><i>int</i><code>&#34;</code></p>
<dd>Sets the maximum number of buttons in pointer devices.</p>
<dt><code>Option &#34;PointerHasPressure&#34; &#34;</code><i>bool</i><code>&#34;</code></p>
<dd>Selects whether &quot;Abs Pressure&quot; is available at the axis 4 in pointer devices. </p>
</dl>
<h2>Interface With The Driver</h2>
<p>The communication with the driver is a binary protocol defined in include/xf86-input-inputtest-protocol.h </p>
<p> At the beginning, the client process that communicates with the driver must connect to the socket that is created by the driver at SocketPath. Once the connection is established, it must write a xf86ITEventClientVersion event and read a xf86ITResponseServerVersion response where the driver specifies the protocol version supported by it. If this version is lower than requested by the client, then the driver will disconnect. </p>
<p> After receiving xf86ITResponseServerVersion message the client may send events to the driver. Each event is an instance of one of the <code>xf86ITEvent*</code> structs. The length field defines the full length of the struct in bytes and the event field defines the type of the struct. </p>
<p> The responses from the server follow the same structure. Each response is an instance of one of the <code>xf86ITResponse*</code> structs. The length field defines the full length of the struct in bytes and the event field defines the type of the struct. </p>
<p> The synchronization with Xorg is performed via <code>xf86ITEventWaitForSync</code> event. After sending such event, the client must read of a <code>xf86ITResponseSyncFinished</code><i>event</i><code>from</code><i>the</i><code>socket</code><i>without</i><code>sending</code><i>additional</i> events. The completion of the read operation indicates that Xorg has fully processed all input events sent to it so far.</p>
<h2>Authors</h2>
<p>Povilas Kanapickas &lt;povilas [at] radix.lt&gt;</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-xorg/">Xorg</a>(1), <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5), <a href="/docs/linux/man/1-xserver/">Xserver</a>(1), <a href="/docs/linux/man/7-x/">X</a>(7) </p>
