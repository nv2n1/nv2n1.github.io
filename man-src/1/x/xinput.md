---
title: "xinput(1)"
name: "xinput"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xinput/"
description: "xinput – utility to configure and test X input devices"
---

<h2 class="name">NAME</h2>
<p> xinput &#8211; utility to configure and test X input devices</p>
<h2>SYNOPSIS</h2>
<p> <code>xinput [OPTIONS] [DEVICE]</code> </p>
<h2>DESCRIPTION</h2>
<p> xinput is a utility to list available input devices, query information about a device and change input device settings.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></p>
<dd> Test if the X Input extension is available and return the version number of the program and the version supported by the server. This option does not require a device name.</dl>
<dl>
<dt><code>&#8211;list [&#8211;short || &#8211;long || &#8211;name-only || &#8211;id-only] [</code><i>device</i>]</p>
<dd> If no argument is given list all the input devices. If an argument is given, show all the features of <i>device</i>. If &#8211;long is provided, the output includes detailed information about the capabilities of each devices. Otherwise, or if &#8211;short is provided, only the device names and some minimal information is listed. If &#8211;name-only is provided, the output is limited to the device names. One device name is listed per line. Note that the order the devices are listed is undefined. If &#8211;id-only is provided, the output is limited to the device IDs. One device ID is listed per line. Note that the order the devices are listed is undefined.</dl>
<dl>
<dt><code>&#8211;get-feedbacks </code><i>device</i></p>
<dd> Display the feedbacks of <i>device</i>.</dl>
<dl>
<dt><code>&#8211;set-pointer </code><i>device</i></p>
<dd> Switch <i>device</i> in core pointer. This option does nothing on X servers 1.5 and later.</dl>
<dl>
<dt><code>&#8211;set-mode </code><i>device</i> <i>ABSOLUTE|RELATIVE</i></p>
<dd> Change the mode of <i>device</i>.</dl>
<dl>
<dt><code>&#8211;set-ptr-feedback </code><i>device</i> <i>threshold</i> <i>num</i> <i>denom</i></p>
<dd> Change the pointer acceleration (or feedback) parameters of <i>device</i>. The <a href="/docs/linux/man/1-xset/">xset</a>(1) man page has more details. For X.Org Server 1.7 and above, there are additional device properties pertaining to pointer acceleration. These do not replace, but complement the pointer feedback setting.</dl>
<dl>
<dt><code>&#8211;set-integer-feedback </code><i>device</i> <i>index</i> <i>value</i></p>
<dd> Change the value of an integer feedback of <i>device</i>.</dl>
<dl>
<dt><code>&#8211;set-button-map </code><i>device</i> <i>map_button_1</i> [<i>map_button_2</i> [<i>&#8230;</i>]]</p>
<dd> Change the button mapping of <i>device</i>. The buttons are specified in physical order (starting with button 1) and are mapped to the logical button provided. 0 disables a button. The default button mapping for a device is 1 2 3 4 5 6 etc.</dl>
<dl>
<dt><code>&#8211;query-state </code><i>device</i></p>
<dd> Query the device state.</dl>
<dl>
<dt><code>&#8211;list-props </code><i>device</i> [<i>device</i> [<i>&#8230;</i>]]</p>
<dd> Lists properties that can be set for the given device(s).</dl>
<dl>
<dt><code>&#8211;set-int-prop </code><i>device</i> <i>property</i> <i>format</i> <i>value</i></p>
<dd> Sets an integer property for the device. Appropriate values for <i>format</i> are 8, 16, or 32, depending on the property. Deprecated, use <code>&#8211;set-prop</code> instead.</dl>
<dl>
<dt><code>&#8211;set-float-prop </code><i>device</i> <i>property</i> <i>value</i></p>
<dd> Sets a float property for the device. Deprecated, use <code>&#8211;set-prop</code> instead.</dl>
<dl>
<dt><code>&#8211;set-prop [&#8211;type=</code><i>atom|float|int</i>] [&#8211;format=<i>8|16|32</i>] <i>device</i> <i>property</i> <i>value</i> [&#8230;]</p>
<dd> Set the property to the given value(s). If not specified, the format and type of the property are left as-is. The arguments are interpreted according to the property type. See Section <i>CHANGING PROPERTIES</i>.</dl>
<dl>
<dt><code>&#8211;watch-props </code><i>device</i></p>
<dd> Prints to standard out when property changes occur.</dl>
<dl>
<dt><code>&#8211;delete-prop </code><i>device</i> <i>property</i></p>
<dd> Delete the property from the device.</dl>
<dl>
<dt><code>&#8211;test [-proximity] </code><i>device</i></p>
<dd> Register all extended events from <i>device</i> and enter an endless loop displaying events received. If the -proximity is given, ProximityIn and ProximityOut are registered.</dl>
<dl>
<dt><code>&#8211;test-xi2 [&#8211;root] [</code><i>device</i>]</p>
<dd> Register for a number of XI2 events and display them. If a device is given, only events on this device are displayed. If &#8211;root is given, events are selected on the root window only. Otherwise, a new client window is created (similar to xev).</dl>
<dl>
<dt><code>&#8211;create-master </code><i>prefix</i> [sendCore] [enable]</p>
<dd> Create a new pair of master devices on an XI2-enabled server with the given <i>prefix</i>. The server will create one master pointer named &quot;<i>prefix</i> pointer&quot; and one master keyboard named &quot;<i>prefix</i> keyboard&quot;. If <i>sendCore</i> is 1, this pair of master devices is set to send core events (default). If <i>enable</i> is 1, this master device pair will be enabled immediately (default).</dl>
<dl>
<dt><code>&#8211;remove-master </code><i>master</i> [Floating|AttachToMaster] [returnPointer] [returnKeyboard]</p>
<dd> Remove <i>master</i> and its paired master device. Attached slave devices are set floating if <i>Floating</i> is specified or the argument is omitted. If the second argument is <i>AttachToMaster</i>, <i>returnPointer</i> specifies the master pointer to attach all slave pointers to and <i>returnKeyboard</i> specifies the master keyboard to attach all slave keyboards to.</dl>
<dl>
<dt><code>&#8211;reattach </code><i>slave</i> <i>master</i></p>
<dd> Reattach <i>slave</i> to <i>master</i>.</dl>
<dl>
<dt><code>&#8211;float </code><i>slave</i></p>
<dd> Remove <i>slave</i> from its current master device.</dl>
<dl>
<dt><code>&#8211;set-cp </code><i>window</i> <i>master</i></p>
<dd> Set the ClientPointer for the client owning <i>window</i> to <i>master</i>. <i>master</i> must specify a master pointer.</dl>
<dl>
<dt><code>&#8211;map-to-output </code><i>device</i> <i>crtc</i></p>
<dd> Restricts the movements of the absolute <i>device</i> to the RandR <i>crtc</i>. The output name must match a currently connected output (see <i><a href="/docs/linux/man/1-xrandr/">xrandr</a>(1)</i>). If the NVIDIA binary driver is detected or RandR 1.2 or later is not available, a Xinerama output may be specified as &quot;HEAD-N&quot;, with N being the Xinerama screen number. This option has no effect on relative devices.</dl>
<dl>
<dt><code>&#8211;enable </code><i>device</i></p>
<dd> Enable the <i>device</i>. This call is equivalent to <code>xinput &#8211;set-prop device </code><i>Device Enabled</i> 1</dl>
<dl>
<dt><code>&#8211;disable </code><i>device</i></p>
<dd> Disable the <i>device</i>. This call is equivalent to <code>xinput &#8211;set-prop device </code><i>Device Enabled</i> 0</dl>
<p> <i>device</i> can be the device name as a string or the XID of the device. </p>
<p> <i>slave</i> can be the device name as a string or the XID of a slave device. </p>
<p> <i>master</i> can be the device name as a string or the XID of a master device. </p>
<p> <i>property</i> can be the property as a string or the Atom value. </p>
<h2>CHANGING PROPERTIES</h2>
<p> When xinput should modify an existing driver property value, it is sufficient to provide the device name and property name as string, followed by the new value(s) of the property. For example:</p>
<dl>
<dt>
<dd> <code>xinput set-prop &quot;my device&quot; &quot;my prop&quot; 1 2 3 </p>
</dl>
<p> </code></p>
<h2>XWAYLAND</h2>
<p> Xwayland is an X server that uses a Wayland Compositor as backend. Xwayland acts as translation layer between the X protocol and the Wayland protocol but does not have direct access to the hardware. The X Input Extension devices created by Xwayland (&quot;xwayland-pointer&quot;, &quot;xwayland-keyboard&quot;, etc.) map to the Wayland protocol devices, not to physical devices. </p>
<p> These X Input Extension devices are only visible to other X clients connected to the same Xwayland process. Changing properties on Xwayland devices only affects the behavior of those clients. For example, disabling an Xwayland device with xinput does not disable the device in Wayland-native applications. Other changes may not have any effect at all. </p>
<p> In most instances, using xinput with an Xwayland device is indicative of a bug in a shell script and xinput will print a warning. Use the Wayland Compositor&#8217;s native device configuration methods instead. </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-x/">X</a>(7), <a href="/docs/linux/man/1-xset/">xset</a>(1), <a href="/docs/linux/man/1-xrandr/">xrandr</a>(1)</p>
<h2>COPYRIGHT</h2>
<p> Copyright 1996,1997, Frederic Lepied. </p>
<p> Copyright 2007, Peter Hutterer. </p>
<p> Copyright 2008, Philip Langdale. </p>
<p> Copyright 2009-2011, Red Hat, Inc. </p>
<h2>AUTHORS</h2>
<pre><code>
Peter Hutterer&lt;peter.hutterer[at] who - t.net&gt;
    Philip Langdale, &lt;philipl[at] alumni.utexas.net&gt; Frederic Lepied, France&lt;Frederic.Lepied[at] sugix.frmug.org&gt; Julien Cristau&lt;jcristau[at] debian.org&gt; Thomas Jaeger&lt;ThJaeger[at] gmail.com&gt; and more.
</code></pre>
<h2>Index</h2>
