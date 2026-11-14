---
title: "dmxaddinput(3)"
name: "dmxaddinput"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dmxaddinput/"
description: "DMXAddInput, DMXAddBackendInput, DMXAddConsoleInput – attach a new input"
---

<p>DMXAddInput, DMXAddBackendInput, DMXAddConsoleInput &#8211; attach a new input</p>
<h2>Synopsis</h2>
<p><code>#include &lt;<a href="file:/usr/include/X11/extensions/dmxext.h">X11/extensions/dmxext.h</a>&gt;</code> </p>
<pre><code>Bool DMXAddInput(Display </code><i>*dpy</i><code>,</code>
<code> unsigned int </code><i>mask</i><code>,</code>
<code> DMXInputAttributes </code><i>*attr</i><code>,</code>
<code> int </code><i>*id</i><code>);</code>
<br>
<code>Bool DMXAddBackendInput(Display </code><i>*dpy</i><code>,</code>
<code> int </code><i>screen</i><code>,</code>
<code> int </code><i>sendsCore</i><code>,</code>
<code> int </code><i>*newId</i><code>);</code>
<br>
<code>Bool DMXAddConsoleInput(Display </code><i>*dpy</i><code>,</code>
<code> const char </code><i>*name</i><code>,</code>
<code> int </code><i>sendsCore</i><code>,</code>
<code> int </code><i>*newId</i><code>);</code></pre>
<h2>Description</h2>
<p><code>DMXAddInput()</code> is used to attach a new input (or a previously detached input) to the <code><a href="/docs/linux/man/1-xdmx/">Xdmx</a></code>(1) server. <i>mask</i> specifies the fields in <i>attr</i> that are active, and <i>id</i> returns the device if of the first device in the series that is added. </p>
<p> The value of <i>mask</i> is computed from the following values: </p>
<pre>DMXInputType
DMXInputPhysicalScreen
DMXInputSendsCore</pre>
<p>The <code>DMXInputAttributes</code> structure is: </p>
<pre>typedef struct {
 DMXInputEnum inputType;
 int physicalScreen;
 int physicalId;
 Bool isCore;
 Bool sendsCore;
 const char *name;
 Bool detached;
} DMXInputAttributes;</pre>
<p><i>inputType</i> may bave the value <code>DmxConsoleInputType or DmxBackendInputType .</code> </p>
<p> For console devices, <i>name</i> will specify the display to be used. </p>
<p> For back-end devices, <i>physicalScreen</i> will specify the <code><a href="/docs/linux/man/1-xdmx/">Xdmx</a></code>(1) screen number. </p>
<p> If <i>sendsCore</i> is <code>True</code>, the new device will be added as a true core device. </p>
<p> If a device was removed with <code><a href="/docs/linux/man/3-dmxremoveinput/">DMXRemoveInput</a></code>(3) an attempt will be made to reconnect the previous devices (<i>sendsCore</i> is ignored in this case). </p>
<p> <code>DMXAddBackendInput()</code> is a helper function that is used to add input from a back-end server. With this function, <i>screen</i> refers to the back-end screen, <i>sendsCore</i> is <code>True</code> if the new input should send core events (and it ignored if the input has been detached), and <i>newId</i> will hold the device id of the first device in the series added. </p>
<p> <code>DMXAddConsoleInput()</code> is a helper function that is used to add input from a console. With this function, <i>name</i> is the name of the console display, <i>sendsCore</i> is <code>True</code> if the new input should send core events (and it ignored if the input has been detached), and <i>newId</i> will hold the device id of the first device in the series added.</p>
<h2>Return Value</h2>
<p><code>DMXAddInput()</code> returns <code>True</code> on success and <code>False</code> otherwise. </p>
<p> <code>DMXAddInput()</code> can generate <code>BadValue</code> (if <i>inputType</i> is invalid or <i>physicalScreen</i> is out of range), <code>BadAccess</code> (if the input has already been attached or if the backend screen is currently detached).</p>
<h2>Notes</h2>
<p>Local devices cannot be attached or detached. </p>
<p> Attributes that are not specified will default to 0. This may lead to unintended results.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-dmxremoveinput/">DMXRemoveInput</a></code>(3), <code><a href="/docs/linux/man/3-dmx/">DMX</a></code>(3), <code><a href="/docs/linux/man/1-xdmx/">Xdmx</a></code>(1)</p>
