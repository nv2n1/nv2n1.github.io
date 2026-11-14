---
title: "xmonisdn(1)"
name: "xmonisdn"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xmonisdn/"
description: "xmonisdn – monitor for ISDN network"
---

<h2>NAME</h2>
<p> xmonisdn &#8211; monitor for ISDN network</p>
<h2>SYNOPSIS</h2>
<p> <code>xmonisdn</code> [ &#8211;<i>toolkitoption</i> &#8230; ] [ <i>-option</i> &#8230; ]</p>
<h2>DESCRIPTION</h2>
<p> The <i>xmonisdn</i> program displays the status of the ISDN network connection and allows the starting and stopping of the ISDN subsystem. If the ISDN subsystem is not active, a window showing a terminal in the foreground and a dashed terminal in the backgorund is displayed. If the ISDN system is active, but there is no network connection established, two terminals with dashed arrows between them is displayed. If there is a incoming connection or there is dialing in progress, the arrows become more solid. An outgoing network connection is signaled by solid arrows between the terminals and the window is displayed in reverse video. If the ISDN subsystem dials out or hangs up, the program beeps to signal the state change (this can be changed using the <i>volume </i> option). </p>
<p> Pressing button 2 on the window executes the command <i>/sbin/ifup</i> and pressing button 3 executes <i>/sbin/ifdown</i><br />
 <i>/sbin/ifup</i> and <i>/sbin/ifdown</i> should start and stop the ISDN subsystem; if the route command is used, xmonisdn must be run as setuid root for this to work. Alternatively, the scripts can manipulate the isdnctrl dialmode setting, in which case only permission to access /dev/isdnctrl is needed.</p>
<h2>OPTIONS</h2>
<p> <i>xmonisdn</i> accepts all of the standard X Toolkit command line options along with the additional options listed below:</p>
<dl>
<dt><code>-help</code></p>
<dd> This option indicates that a brief summary of the allowed options should be printed on the standard error.</p>
<dt><code>-update </code><i>tenth of a second</i></p>
<dd> This option specifies the frequency in 1/10 of a second at which <i>xmonisdn</i> should update its display. If the window is obscured and then exposed, it will be updated immediately. The default is 0.5 seconds (i.e. -update 5).</p>
<dt><code>-file </code><i>filename</i></p>
<dd> This option specifies the name of the file which should be monitored. By default, it watches /dev/isdninfo.</p>
<dt><code>-volume </code><i>percentage</i></p>
<dd> This option specifies how loud the bell should be rung when there is an important status change.</p>
<dt><code>-shape</code></p>
<dd> This option indicates that the xmonisdn window should be shaped if masks for the images are given.</dl>
<p> The following standard X Toolkit command line arguments are commonly used with <i>xmonisdn:</i></p>
<dl>
<dt><code>-display </code><i>display</i></p>
<dd> This option specifies the X server to contact.</p>
<dt><code>-geometry </code><i>geometry</i></p>
<dd> This option specifies the preferred size and position of the xmonisdn window. The icon is 48 pixels wide and 48 pixels high and will be centered in the window.</p>
<dt><code>-bg </code><i>color</i></p>
<dd> This option specifies the color to use for the background of the window.</p>
<dt><code>-bd </code><i>color</i></p>
<dd> This option specifies the color to use for the border of the window.</p>
<dt><code>-bw </code><i>number</i></p>
<dd> This option specifies the width in pixels of the border surrounding the window.</p>
<dt><code>-fg </code><i>color</i></p>
<dd> This option specifies the color to use for the foreground of the window.</p>
<dt><code>-rv</code></p>
<dd> This option indicates that reverse video should be simulated by swapping the foreground and background colors.</p>
<dt><code>-xrm </code><i>resourcestring</i></p>
<dd> This option specifies a resource string to be used. This is especially useful for setting resources that do not have separate command line options.</dl>
<h2>X DEFAULTS</h2>
<p> The application class name is xmonisdn. This program uses the <i>Netstat</i> widget. It understands all of the core resource names and classes as well as: </p>
<dl>
<dt><code>file (</code>class<code> File)</code></p>
<dd> Specifies the name of the file to monitor. The default is to watch /dev/isdninfo.</p>
<dt><code>width (</code>class<code> Width)</code></p>
<dd> Specifies the width of the icon.</p>
<dt><code>height (</code>class<code> Height)</code></p>
<dd> Specifies the height of the icon.</p>
<dt><code>update (</code>class<code> Interval)</code></p>
<dd> Specifies the frequency in 1/10 of a second at which the isdninfo file should be checked. The default is 5.</p>
<dt><code>volume (</code>class<code> Volume)</code></p>
<dd> Specifies how loud the bell should be rung. The default is 33 percent.</p>
<dt><code>foreground (</code>class<code> Foreground)</code></p>
<dd> Specifies the color for the foreground.</p>
<dt><code>reverseVideo (</code>class<code> ReverseVideo)</code></p>
<dd> Specifies that the foreground and background should be reversed.</p>
<dt><code>flip (</code>class<code> Flip)</code></p>
<dd> Specifies whether or not the image that is shown when there is an outgoing network connection should be inverted. The default is &#8220;true.&#8221;</p>
<dt><code>inactivePixmap (</code>class<code> Pixmap)</code></p>
<dd> Specifies a bitmap to be shown when the ISDN subsystem is inactive. The default is netinactive.</p>
<dt><code>waitingPixmap (</code>class<code> Pixmap)</code></p>
<dd> Specifies a bitmap to be shown when the ISDN subsystem is active, but there is no connection. The default is netwaiting.</p>
<dt><code>activePixmap (</code>class<code> Pixmap)</code></p>
<dd> Specifies a bitmap to be shown when there is a incoming network connection (or dialing is in progress). The default is netactive.</p>
<dt><code>activeoutPixmap (</code>class<code> Pixmap)</code></p>
<dd> Specifies a bitmap to be shown when there is a outgoing network connection. The default is netactiveout.</p>
<dt><code>startPixmap (</code>class<code> Pixmap)</code></p>
<dd> Specifies a bitmap to be shown when the ISDN network is started up. The default is netstart.</p>
<dt><code>stopPixmap (</code>class<code> Pixmap)</code></p>
<dd> Specifies a bitmap to be shown when the ISDN network is stopped. The default is netstop.</p>
<dt><code>shapeWindow (</code>class<code> ShapeWindow)</code></p>
<dd> Specifies whether or not the xmonisdn window should be shaped to the given PixmapMasks. The default is false.</p>
<dt><code>inactivePixmapMask (</code>class<code> PixmapMask) </code></p>
<dd> Specifies a mask for the bitmap to be shown when the ISDN subsystem is inactive. The default is none.</p>
<dt><code>waitingPixmapMask (</code>class<code> PixmapMask)</code></p>
<dd> Specifies a mask for the bitmap to be shown when the ISDN subsystem is active, but there is no connection. The default is none.</p>
<dt><code>activePixmapMask (</code>class<code> PixmapMask)</code></p>
<dd> Specifies a mask for the bitmap to be shown when when there is a incoming network connection (or dialing is in progress). The default is none.</p>
<dt><code>activeoutPixmapMask (</code>class<code> PixmapMask)</code></p>
<dd> Specifies a mask for the bitmap to be shown when there is a outgoing network connection. The default is none.</p>
<dt><code>startPixmapMask (</code>class<code> PixmapMask)</code></p>
<dd> Specifies a mask for the bitmap to be shown when the ISDN network is started up. The default is none.</p>
<dt><code>stopPixmapMask (</code>class<code> PixmapMask)</code></p>
<dd> Specifies a mask for the bitmap to be shown when the ISDN network is stopped. The default is none.</dl>
<h2>ACTIONS</h2>
<p> The <i>Netstat</i> widget provides the following actions for use in event translations:</p>
<dl>
<dt><code>check()</code></p>
<dd> This action causes the widget to check the isdninfo file and display the appropriate icon.</p>
<dt><code>netdown()</code></p>
<dd> This action causes the widget to execute /sbin/ifdown stop.</p>
<dt><code>netup()</code></p>
<dd> This action causes the widget to execute /sbin/ifup start.</dl>
<p> The default translation is </p>
<pre>
        &lt;ButtonPress&gt;Button2:  netup()
        &lt;ButtonPress&gt;Button3:  netdown()
</pre>
<h2>SECURITY ISSUES</h2>
<p> There are a number of reasons why you should not run <i>xmonisdn</i> as a `setuid root&#8217; program. Most importantly, any setuid root program is a potential security hole. The scripts that are executed by <i>xmonisdn</i> may be compromised, or contain non-absolute paths to the commands called (so that by changing the PATH variable the wrong binary is executed!); or the script may in turn call other things that are not secure.<br />
 If you are sure that your scripts are secure and you insist on making <i>xmonisdn</i> setuid root, you can give the <code>-r</code> option as <i>first</i> option. This will turn off xmonisdn&#8217;s setuid detection. However, you are on your own if you do this! </p>
<p> A better alternative is to put the isdn devices in group <code>dialout</code> (if not so already), and add yourself to the <code>dialout</code> group. This way you have permission to manipulate the ISDN devices, e.g. to use <i>isdnctrl</i> to change the dialmode setting to off (to disable dialing) or auto (for autodial). The whole ISDN system may also be turned on and off, see the <i>isdnctrl manpage for more info.</i> This is a more secure way of controlling the dialing than e.g. by manipulating routes. </p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>DISPLAY</code></p>
<dd> to get the default host and display number.</p>
<dt><code>XENVIRONMENT</code></p>
<dd> to get the name of a resource file that overrides the global resources stored in the RESOURCE_MANAGER property.</dl>
<h2>AUTHOR</h2>
<p> Bernhard Nebel</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-isdnctrl/">isdnctrl</a>(8)</code> </p>
<h2>Index</h2>
