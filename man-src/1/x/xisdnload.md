---
title: "xisdnload(1)"
name: "xisdnload"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xisdnload/"
description: "xisdnload – ISDN load average display for X"
---

<h2>NAME</h2>
<p> xisdnload &#8211; ISDN load average display for X</p>
<h2>SYNOPSIS</h2>
<p> <code>xisdnload</code>[-<i>toolkitoption</i> &#8230;] [-scale <i>integer</i>] [-update <i>seconds</i>] [-hl <i>color</i>] [-highlight <i>color</i>] [-online <i>color</i>] [-active <i>color</i>] [-trying <i>color</i>] [-activate <i>command</i>] [-deactivate <i>command</i>] [-jumpscroll <i>pixels</i>] [-number <i>regexp</i>] [-label <i>string</i>] [-nolabel]</p>
<h2>DESCRIPTION</h2>
<p> The <i>xisdnload </i> program displays a periodically updating histogram of the ISDN load average.</p>
<h2>OPTIONS</h2>
<p> <i>Xisdnload</i> accepts all of the standard X Toolkit command line options (see <i><a href="/docs/linux/man/1-x/">X</a>(1)</i>). The order of the options in unimportant. <i>xisdnload also accepts the following additional options: </p>
<dl>
<dt></i><code>-hl </code><i>color</i> or -highlight <i>color</i></p>
<dd> This option specifies the color of the scale lines.</p>
<dt><code>-online </code><i>color</i></p>
<dd> This option specifies the background color when one or more ISDN channels are online.</p>
<dt><code>-active </code><i>color</i></p>
<dd> This option specifies the background color when any route is found that is directed to an interface named isdn* or ippp*.</p>
<dt><code>-trying </code><i>color</i></p>
<dd> This option specifies the background color when at least one attempt to setup a cennection is pending.</p>
<dt><code>-jumpscroll </code>number of pixels</p>
<dd> The number of pixels to shift the graph to the left when the graph reaches the right edge of the window. The default value is 1/2 the width of the current window. Smooth scrolling can be achieved by setting it to 1.</p>
<dt><code>-label </code><i>string</i></p>
<dd> The string to put into the label above the load average when beeing online. It is interpreted as a standard format string and may contain the dialed number (%s), the minutes (%d) and seconds (%d) being online, the actual cps rate (%f), the amount of kbytes transfered (%d) and a connection history (%s) in this sequence.</p>
<dt><code>-nolabel</code></p>
<dd> If this command line option is specified then no label will be displayed above the load graph.</p>
<dt><code>-scale </code><i>integer</i></p>
<dd> This option specifies the minimum number of tick marks in the histogram, where one division represents one load average point. If the load goes above this number, <i>xisdnload</i> will create more divisions, but it will never use fewer than this number. The default is 1.</dl>
<dl>
<dt><code>-update </code><i>seconds</i></p>
<dd> This option specifies the interval in seconds at which <i>xisdnload</i> updates its display. The minimum amount of time allowed between updates is 1 second. The default is 10.</dl>
<dl>
<dt><code>-activate </code><i>command</i></p>
<dd> This option specifies a command to be executed when dial-on-demand is not active and you clicked on the xisdnload stripchart. A typical command might be something like `sudo /etc/init.d/isdn start&#8217; to start up your connection.</dl>
<dl>
<dt><code>-deactivate </code><i>command</i></p>
<dd> This option specifies a command to be executed when dial-on-demand is active and you clicked on the xisdnload stripchart. A typical command might be something like `sudo /etc/init.d/isdn stop&#8217; to shut down your connection.</dl>
<dl>
<dt><code>-manual</code></p>
<dd> With this option the interface is assumed to be active and in manual dial mode. The activate/deactive commands are selected depending on the connection state. A typical activate command might be `isdnctrl dial ippp0&#8242;, and to deactivate `isdnctrl hangup ippp0&#8242;.</dl>
<dl>
<dt><code>-number </code><i>regexp</i></p>
<dd> The supplied regular expression is used to limit the set numbers to be observed by <i>xisdnload</i>.</dl>
<h2>RESOURCES</h2>
<p> See the resource file for the available resources.</p>
<h2>WIDGETS</h2>
<p> In order to specify resources, it is useful to know the hierarchy of the widgets which compose <i>xisdnload</i>. In the notation below, indentation indicates hierarchical structure. The widget class name is given first, followed by the widget instance name. </p>
<pre>
XISDNLoad  xisdnload
         Paned  paned
              Label  label
              StripChart  load
</pre>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>DISPLAY</code></p>
<dd> to get the default host and display number.</p>
<dt><code>XENVIRONMENT</code></p>
<dd> to get the name of a resource file that overrides the global resources stored in the RESOURCE_MANAGER property.</dl>
<h2>FILES</h2>
<p> &lt;XRoot&gt;/lib/X11/app-defaults/XISDNLoad &#8211; specifies required resources.<br />
 /proc/net/route &#8211; kernel routing table. The proc filesystem is needed by xisdnload to detect wheather a dial-on-demand is active. </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-x/">X</a>(1), <a href="/docs/linux/man/1-xrdb/">xrdb</a>(1), <a href="/docs/linux/man/1-xload/">xload</a>(1), <a href="/docs/linux/man/4-mem/">mem</a>(4), Athena StripChart Widget.</p>
<h2>BUGS</h2>
<p> Certainly a lot.</p>
<h2>COPYRIGHT</h2>
<p> This program is based on <i>xload</i> which is Copyright (1988) X Consortium. See <i><a href="/docs/linux/man/1-x/">X</a>(1)</i> for a full statement of rights and permissions.</p>
<h2>AUTHORS</h2>
<p> Besides the basic xload stuff, the ISDN parts are added by<br />
 Frank Strauss &lt;strauss [at] escape.de&gt; (escape e.V., Braunschweig, Germany). In January 1998 Michael Deindl &lt;olmur [at] dwarf.bb.bawue.de&gt; contributed the `yellow&#8217; patch to make xisdnload recognize the phase of trying to connect and show this by a different background color. Markus Pilzecker &lt;mp [at] timesink.pilzecker.de&gt; detected a bug in the color assignment code resulting in seg faults which has been fixed in January 1998. </p>
<h2>Index</h2>
