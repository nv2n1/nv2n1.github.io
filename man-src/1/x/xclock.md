---
title: "xclock(1)"
name: "xclock"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xclock/"
description: "xclock – analog / digital clock for X"
---

<h2 class="name">NAME</h2>
<p> xclock &#8211; analog / digital clock for X </p>
<h2>SYNOPSIS</h2>
<p> <code>xclock</code> [ <code>-help</code> ] [ <code>-analog</code> | <code>-digital</code> ] [ <code>-brief</code> ] [ <code>-chime</code> ] [ <code>-hd</code> <i>color</i> ] [ <code>-hl</code> <i>color</i> ] [ <code>-update</code> <i>seconds</i> ] [ <code>-strftime</code> <i>format</i> ] [ <code>-twelve</code> | <code>-twentyfour</code> | <code>-utime</code> ] [ <code>-padding</code> <i>number</i> ] [ <code>-norender</code> ] [ <code>-render</code> ] [ <code>-sharp</code> ] [ <code>-face</code> <i>pattern</i> ]</p>
<h2>DESCRIPTION</h2>
<p> The <i>xclock</i> program displays the time in analog or digital form. The time is continuously updated at a frequency which may be specified by the user.</p>
<h2>OPTIONS</h2>
<p> <i>Xclock</i> accepts all of the standard X Toolkit command line options along with the additional options listed below:</p>
<dl>
<dt><code>-help</code></p>
<dd> This option indicates that a brief summary of the allowed options should be printed on the standard error.</p>
<dt><code>-analog</code></p>
<dd> This option indicates that a conventional 12 hour clock face with tick marks and hands should be used. This is the default.</p>
<dt><code>-digital</code> or <code>-d</code></p>
<dd> This option indicates that a 24 hour digital clock should be used.</p>
<dt><code>-brief</code></p>
<dd> This option indicates that the digital clock should only display the hours and minutes fields. The default is to show the full time and date information.</p>
<dt><code>-utime</code></p>
<dd> This option indicates that a digital clock should display seconds since the Epoch (in format &#8216;970012340 seconds since Epoch&#8217; instead of a standard 24-hour time.</p>
<dt><code>-strftime </code><i>format</i></p>
<dd> This option allows an <a href="/docs/linux/man/3-strftime/">strftime</a>(3) format string to be specified for the digital clock&#8217;s display.</p>
<dt><code>-twelve</code></p>
<dd> This option indicates that a digital clock should display the time in twelve hour format.</p>
<dt><code>-twentyfour</code></p>
<dd> This option indicates that a digital clock should display the time in twenty-four hour format. This is the default when a digital clock is used.</p>
<dt><code>-chime</code></p>
<dd> This option indicates that the clock should chime once on the half hour and twice on the hour.</p>
<dt><code>-hands</code> <i>color</i> (or <code>-hd</code> <i>color</i>)</p>
<dd> This option specifies the color of the hands on an analog clock. The default is <i>black</i>. This option is effectively ignored when Xrender is in use.</p>
<dt><code>-highlight</code> <i>color</i> (or <code>-hl</code> <i>color</i>)</p>
<dd> This option specifies the color of the edges of the hands on an analog clock, and is only useful on color displays. The default is <i>black</i>. This option is effectively ignored when Xrender is in use.</p>
<dt><code>-update </code><i>seconds</i></p>
<dd> This option specifies the frequency in seconds at which <i>xclock</i> should update its display. If the clock is obscured and then exposed, it will be updated immediately. A value of 30 seconds or less will enable a second hand on an analog clock. The default is 60 seconds.</p>
<dt><code>-padding </code><i>number</i></p>
<dd> This option specifies the width in pixels of the padding between the window border and clock text or picture. The default is 10 on a digital clock and 8 on an analog clock.</p>
<dt><code>-render</code></p>
<dd> This option tells <i>xclock</i> to use the Xrender extension to draw an anti-aliased face. This is the default if <i>xclock</i> has been compiled with Xrender support. Note that the color selection options and resources used when Xrender is in effect differ from the standard options.</p>
<dt><code>-norender</code></p>
<dd> This option turns off the use of Xrender to draw the clock.</p>
<dt><code>-sharp</code></p>
<dd> This option tells <i>xclock</i> to use sharper edges when drawn using the Xrender extension.</p>
<dt><code>-face </code><i>pattern</i></p>
<dd> This option specifies the font to use in digital mode when the Xrender extension is used. Patterns are specified using the fontconfig face format described in the <i>Font Names</i> section of <i><a href="/docs/linux/man/5-fonts-conf/">fonts.conf</a></i>(5).</dl>
<h2>X DEFAULTS</h2>
<p> This program uses the <i>Clock</i> widget. It understands all of the core resource names and classes as well as: </p>
<dl>
<dt><code>width (</code>class<code> Width)</code></p>
<dd> Specifies the width of the clock. The default for analog clocks is 164 pixels; the default for digital clocks is whatever is needed to hold the clock when displayed in the chosen font.</p>
<dt><code>height (</code>class<code> Height)</code></p>
<dd> Specifies the height of the clock. The default for analog clocks is 164 pixels; the default for digital clocks is whatever is needed to hold the clock when displayed in the chosen font.</p>
<dt><code>update (</code>class<code> Interval)</code></p>
<dd> Specifies the frequency in seconds at which the time should be redisplayed.</p>
<dt><code>foreground (</code>class<code> Foreground)</code></p>
<dd> Specifies the color for the tick marks. The default depends on whether <i>reverseVideo</i> is specified. If <i>reverseVideo</i> is specified the default is <i>lwhite</i>, otherwise the default is <i>black</i>. </p>
<dt><code>hands (</code>class<code> Foreground)</code></p>
<dd> Specifies the color of the insides of the clock&#8217;s hands. The default depends on whether <i>reverseVideo</i> is specified. If <i>reverseVideo</i> is specified the default is <i>lwhite</i>, otherwise the default is <i>black</i>. Note that this resource is not used when Xrender is in effect.</p>
<dt><code>highlight (</code>class<code> Foreground)</code></p>
<dd> Specifies the color used to highlight the clock&#8217;s hands. The default is<br />
&nbsp;depends on whether <i>reverseVideo</i> is specified. If <i>reverseVideo</i> is specified the default is <i>lwhite</i>, otherwise the default is <i>black</i>. Note that this resource is not used when Xrender is in effect.</p>
<dt><code>analog (</code>class<code> Boolean)</code></p>
<dd> Specifies whether or not an analog clock should be used instead of a digital one. The default is True.</p>
<dt><code>twentyfour (</code>class<code> Boolean)</code></p>
<dd> Specifies whether or not a digital clock should display the time in twenty-four hour format. The default is True.</p>
<dt><code>chime (</code>class<code> Boolean)</code></p>
<dd> Specifies whether or not a bell should be rung on the hour and half hour.</p>
<dt><code>padding (</code>class<code> Margin)</code></p>
<dd> Specifies the amount of internal padding in pixels to be used. The default is 8.</p>
<dt><code>font (</code>class<code> Font)</code></p>
<dd> Specifies the font to be used for the digital clock. Note that variable width fonts currently will not always display correctly. This font is only used when Xrender is not in effect.</p>
<dt><code>render (</code>class<code> Boolean)</code></p>
<dd> Specifies whether or not the Xrender extension should be used for the display. The default is True if <i>xclock</i> has been compiled with Xrender support.</dl>
<p> When Xrender is in effect, the following additional resources are understood: </p>
<dl>
<dt><code>face (</code>class<code> FaceName)</code></p>
<dd> Specify the pattern for the font to be used for the digital clock when Xrender is used. Patterns are specified using the fontconfig face format described in the <i>Font Names</i> section of <i><a href="/docs/linux/man/5-fonts-conf/">fonts.conf</a></i>(5).</p>
<dt><code>sharp (</code>class<code> Boolean)</code></p>
<dd> Specifies if sharp edges should be used when rendering the clock. The default is False.</p>
<dt><code>buffer (</code>class<code> Boolean)</code></p>
<dd> Specifies that the updates of the image are drawn to a pixmap before copied into the window instead drawing them into the window directly.</dl>
<p> The defaults of the following color resources depend on whether <i>reverseVideo</i> is specified. If <i>reverseVideo</i> is specified the default is <i>lwhite</i>, otherwise the default is <i>black</i>.</p>
<dl>
<dt><code>hourColor (</code>class<code> Foreground)</code></p>
<dd> The color of the hour hand.</p>
<dt><code>minuteColor (</code>class<code> Foreground)</code></p>
<dd> The color of the minute hand.</p>
<dt><code>secondColor (</code>class<code> Foreground)</code></p>
<dd> The color of the second hand.</p>
<dt><code>majorColor (</code>class<code> Foreground)</code></p>
<dd> The color of the major scale ticks (i. e. each five minutes).</p>
<dt><code>minorColor (</code>class<code> Foreground)</code></p>
<dd> The color of the minor scale ticks (between major ticks).</dl>
<h2>WIDGETS</h2>
<p> In order to specify resources, it is useful to know the hierarchy of the widgets which compose <i>xclock</i>. In the notation below, indentation indicates hierarchical structure. The widget class name is given first, followed by the widget instance name. </p>
<pre>
XClock  xclock
        Clock  clock
</pre>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>DISPLAY</code></p>
<dd> to get the default host and display number.</p>
<dt><code>XENVIRONMENT</code></p>
<dd> to get the name of a resource file that overrides the global resources stored in the RESOURCE_MANAGER property.</dl>
<h2>FILES</h2>
<dl>
<dt><i>/etc/X11/app-defaults/XClock</i></p>
<dd> specifies required resources</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-x/">X</a>(7), <a href="/docs/linux/man/1-xrdb/">xrdb</a>(1), <a href="/docs/linux/man/3-time/">time</a>(3), fonts.conf (5).</p>
<h2>BUGS</h2>
<p> <i>Xclock</i> believes the system clock. </p>
<p> When in digital mode, the string should be centered automatically.</p>
<h2>AUTHORS</h2>
<p> Tony Della Fera (MIT-Athena, DEC)<br />
 Dave Mankins (MIT-Athena, BBN)<br />
 Ed Moy (UC Berkeley) </p>
<h2>Index</h2>
