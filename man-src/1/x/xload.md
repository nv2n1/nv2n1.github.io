---

title: "xload(1)"
name: "xload"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xload/"
description: "xload – system load average display for X"
---

<p> xload &#8211; system load average display for X </p>
<h2>SYNOPSIS</h2>
<p> <code>xload</code><tt>&nbsp;<wbr>&nbsp;</tt>[-<i>toolkitoption</i> &#8230;] [-scale <i>integer</i>] [-update <i>seconds</i>] [-hl <i>color</i>] [-highlight <i>color</i>] [-remote <i>host</i>]</p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[-jumpscroll&nbsp;<i>pixels</i>]&nbsp;[-label&nbsp;<i>string</i>]&nbsp;[-nolabel]&nbsp;[-lights]</p>
<h2>DESCRIPTION</h2>
<p> The <i>xload</i> program displays a periodically updating histogram of the system load average.</p>
<h2>OPTIONS</h2>
<p> <i>Xload</i> accepts all of the standard X Toolkit command line options (see <i><a href="/docs/linux/man/7-x/">X</a>(7)</i>). The order of the options is unimportant. <i>xload also accepts the following additional options: </p>
<dl>
<dt></i><code>-hl </code><i>color</i> or -highlight <i>color</i></dt>
<dd> This option specifies the color of the scale lines.</dd>
<dt><code>-jumpscroll </code>number of pixels</dt>
<dd> The number of pixels to shift the graph to the left when the graph reaches the right edge of the window. The default value is 1/2 the width of the current window. Smooth scrolling can be achieved by setting it to 1.</dd>
<dt><code>-label </code><i>string</i></dt>
<dd> The string to put into the label above the load average.</dd>
<dt><code>-nolabel</code></dt>
<dd> If this command line option is specified then no label will be displayed above the load graph.</dd>
<dt><code>-lights</code></dt>
<dd> When specified, this option causes <i>xload</i> to display the current load average by using the keyboard leds; for a load average of <i>n</i>, xload lights the first <i>n</i> keyboard leds. This option turns off the usual screen display.</dd>
<dt><code>-scale </code><i>integer</i></dt>
<dd> This option specifies the minimum number of tick marks in the histogram, where one division represents one load average point. If the load goes above this number, <i>xload</i> will create more divisions, but it will never use fewer than this number. The default is 1.</dd></dl>
<dl>
<dt><code>-update </code><i>seconds</i></dt>
<dd> This option specifies the interval in seconds at which <i>xload</i> updates its display. The minimum amount of time allowed between updates is 1 second. The default is 10.</dd>
<dt><code>-remote </code><i>host</i></dt>
<dd> This option tells <i>xload</i> to display the load of <i>host</i> instead of <i>localhost</i>. <i>Xload</i> gets the information from the <i>rwhod</i> database and consequently requires <i>rwhod</i> to be executing both on <i>localhost</i> and <i>host</i>.</dd></dl>
<h2>RESOURCES</h2>
<p> In addition to the resources available to each of the widgets used by <i>xload</i> there is one resource defined by the application itself.</p>
<dl>
<dt><code>showLabel (</code>class<code> Boolean)</code></dt>
<dd> If False then no label will be displayed.</dd></dl>
<h2>WIDGETS</h2>
<p> In order to specify resources, it is useful to know the hierarchy of the widgets which compose <i>xload</i>. In the notation below, indentation indicates hierarchical structure. The widget class name is given first, followed by the widget instance name. </p>
<pre>
XLoad  xload
        Paned  paned
                Label  label
                StripChart  load
</pre>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>DISPLAY</code></dt>
<dd> to get the default host and display number.</dd>
<dt><code>XENVIRONMENT</code></dt>
<dd> to get the name of a resource file that overrides the global resources stored in the RESOURCE_MANAGER property.</dd></dl>
<h2>FILES</h2>
<dl>
<dt><i>/etc/X11/app-defaults/XLoad</i></dt>
<dd> specifies required resources</dd></dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-x/">X</a>(7), <a href="/docs/linux/man/1-xrdb/">xrdb</a>(1), <a href="/docs/linux/man/4-mem/">mem</a>(4), Athena StripChart Widget.</p>
<h2>BUGS</h2>
<p> On older platforms, this program may require the ability to open and read the special system file <i>/dev/kmem</i>. Sites that do not allow general access to this file may need to make <i>xload</i> belong to the same group as <i>/dev/kmem</i> and turn on the <i>set group id</i> permission flag. </p>
<p> Reading the load average is inherently non-portable. Therefore, the routine used to read it (get_load.c) must be ported to each new operating system.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; X Consortium<br />
 See <i><a href="/docs/linux/man/7-x/">X</a>(7)</i> for a full statement of rights and permissions.</p>
<h2>AUTHORS</h2>
<p> K. Shane Hartman (MIT-LCS) and Stuart A. Malone (MIT-LCS);<br />
 with features added by Jim Gettys (MIT-Athena), Bob Scheifler (MIT-LCS), Tony Della Fera (MIT-Athena), and Chris Peterson (MIT-LCS). </p>
