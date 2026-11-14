---
title: "xditview(1)"
name: "xditview"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xditview/"
description: "xditview – display ditroff output"
---

<h2 class="name">NAME</h2>
<p> xditview &#8211; display ditroff output </p>
<h2>SYNOPSIS</h2>
<p> <code>xditview</code> [ &#8211;<i>toolkitoption</i> &#8230; ] [ &#8211;<i>option</i> &#8230; ] [ <i>filename</i> ]</p>
<h2>DESCRIPTION</h2>
<p> The <i>xditview</i> program displays <i>ditroff</i> output on an X display. It uses no special metrics and automatically converts the printer coordinates into screen coordinates; using the user-specified screen resolution, rather than the actual resolution so that the appropriate fonts can be found. If &#8220;<code>&#8211;</code>&#8221; is given as the <i>filename,</i> <i>xditview</i> reads from standard input. If &#8220;<code>|</code>&#8221; is the first character of <i>filename,</i> <i>xditview</i> forks <i>sh</i> to run the rest of the &#8220;file name&#8221; and uses the standard output of that command.</p>
<h2>OPTIONS</h2>
<p> <i>Xditview</i> accepts all of the standard X Toolkit command line options along with the additional options listed below:</p>
<dl>
<dt><code>-page </code><i>page-number</i></p>
<dd> This option specifies the page number of the document to be displayed at start up time.</p>
<dt><code>-resolution </code><i>screen-resolution</i></p>
<dd> This specifies the desired screen resolution to use; fonts will be opened by requesting this resolution field in the XLFD names.</p>
<dt><code>-noPolyText</code></p>
<dd> Some X servers incorrectly implement PolyText with multiple strings per request. This option suppresses the use of this feature in <i>xditview.</i></p>
<dt><code>-backingStore </code><i>backing-store-type</i></p>
<dd> Redisplay can take up to a second or so; this option causes the server to save the window contents so that when it is scrolled around the viewport, the window is painted from contents saved in backing store. <i>backing-store-type</i> can be one of <code>Always</code>, WhenMapped or NotUseful.</dl>
<p> The following standard X Toolkit command line arguments are commonly used with <i>xditview:</i></p>
<dl>
<dt><code>-bg </code><i>color</i></p>
<dd> This option specifies the color to use for the background of the window. The default is <i>white</i>.</p>
<dt><code>-bd </code><i>color</i></p>
<dd> This option specifies the color to use for the border of the window. The default is <i>black</i>.</p>
<dt><code>-bw </code><i>number</i></p>
<dd> This option specifies the width in pixels of the border surrounding the window.</p>
<dt><code>-fg </code><i>color</i></p>
<dd> This option specifies the color to use for displaying text. The default is <i>black</i>.</p>
<dt><code>-fn </code><i>font</i></p>
<dd> This option specifies the font to be used for displaying widget text. The default is <i>fixed</i>.</p>
<dt><code>-rv</code></p>
<dd> This option indicates that reverse video should be simulated by swapping the foreground and background colors.</p>
<dt><code>-geometry </code><i>geometry</i></p>
<dd> This option specifies the preferred size and position of the window.</p>
<dt><code>-display </code><i>host</i>:<i>display</i></p>
<dd> This option specifies the X server to contact.</p>
<dt><code>-xrm </code><i>resourcestring</i></p>
<dd> This option specifies a resource string to be used.</dl>
<h2>X DEFAULTS</h2>
<p> This program uses a <i>Dvi</i> widget. It understands all of the core resource names and classes as well as: </p>
<dl>
<dt><code>width (</code>class<code> Width)</code></p>
<dd> Specifies the width of the window.</p>
<dt><code>height (</code>class<code> Height)</code></p>
<dd> Specifies the height of the window.</p>
<dt><code>foreground (</code>class<code> Foreground)</code></p>
<dd> Specifies the default foreground color.</p>
<dt><code>font (</code>class<code> Font)</code></p>
<dd> Specifies the font to be used for error messages.</p>
<dt><code>FontMap (class FontMap)</code></p>
<dd> To associate the <i>ditroff</i> fonts with appropriate X fonts, this string resource contains a set of new-line separated specifications, each of which consists of a ditroff name, some white space and an XLFD pattern with * characters in appropriate places to allow all sizes to be listed. The default fontMap is: </p>
<pre><code>
R - *-times - medium - r - normal-- * -*-*-*-*-*-iso8859 - 1
\
I - *-times -
    medium - i - normal-- * -*-*-*-*-*-iso8859 - 1
\
B - *-times -
    bold - r - normal-- * -*-*-*-*-*-iso8859 - 1
\
F - *-times -
    bold - i - normal-- * -*-*-*-*-*-iso8859 - 1
\
BI - *-times -
    bold - i - normal-- * -*-*-*-*-*-iso8859 - 1
\
C - *-courier -
    medium - r - normal-- * -*-*-*-*-*-iso8859 - 1
\
CO - *-courier -
    medium - o - normal-- * -*-*-*-*-*-iso8859 - 1
\
CB - *-courier -
    bold - r - normal-- * -*-*-*-*-*-iso8859 - 1
\
CF - *-courier -
    bold - o - normal-- * -*-*-*-*-*-iso8859 - 1
\
H - *-helvetica -
    medium - r - normal-- * -*-*-*-*-*-iso8859 - 1
\
HO - *-helvetica -
    medium - o - normal-- * -*-*-*-*-*-iso8859 - 1
\
HB - *-helvetica -
    bold - r - normal-- * -*-*-*-*-*-iso8859 - 1
\
HF - *-helvetica -
    bold - o - normal-- * -*-*-*-*-*-iso8859 - 1
\
N - *-new century schoolbook -
    medium - r - normal-- * -*-*-*-*-*-iso8859 - 1
\
NI - *-new century schoolbook -
    medium - i - normal-- * -*-*-*-*-*-iso8859 - 1
\
NB - *-new century schoolbook -
    bold - r - normal-- * -*-*-*-*-*-iso8859 - 1
\
NF - *-new century schoolbook -
    bold - i - normal-- * -*-*-*-*-*-iso8859 - 1
\
A - *-charter -
    medium - r - normal-- * -*-*-*-*-*-iso8859 - 1
\
AI - *-charter -
    medium - i - normal-- * -*-*-*-*-*-iso8859 - 1
\
AB - *-charter -
    bold - r - normal-- * -*-*-*-*-*-iso8859 - 1
\
AF - *-charter -
    bold - i - normal-- * -*-*-*-*-*-iso8859 - 1
\
S - *-symbol -
    medium - r - normal-- * -*-*-*-*-*-adobe - fontspecific
\
S2 - *-symbol -
    medium - r - normal-- * -*-*-*-*-*-adobe - fontspecific

</code></pre>
</dl>
<h2>USING XDITVIEW WITH DITROFF</h2>
<p> You can use any ditroff output file with <i>xditview,</i> although files which use the fonts appropriate to the fontMap will look more accurate on the screen. On servers which support scaled fonts, all requested font sizes will be accurately reflected on the screen; for servers which do not support scaled <i>xditview</i> will use the closest font from the same family.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-x/">X</a></i>(7), <i><a href="/docs/linux/man/1-xrdb/">xrdb</a></i>(1), <i><a href="/docs/linux/man/1-ditroff/">ditroff</a></i>(1), <i>X Logical Font Description Conventions</i></p>
<h2>ORIGIN</h2>
<p> Portions of this program originated in <i>xtroff which was derived</i> from <i>suntroff.</i></p>
<h2>COPYRIGHT</h2>
<p> Copyright 1994 X Consortium<br />
 See <i><a href="/docs/linux/man/7-x/">X</a></i>(7) for a full statement of rights and permissions.</p>
<h2>AUTHORS</h2>
<p> Keith Packard (MIT X Consortium)<br />
 Richard L. Hyde (Purdue)<br />
 David Slattengren (Berkeley)<br />
 Malcom Slaney (Schlumberger Palo Alto Research)<br />
 Mark Moraes (University of Toronto) </p>
<h2>Index</h2>
