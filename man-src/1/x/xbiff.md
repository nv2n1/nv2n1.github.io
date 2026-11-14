---
title: "xbiff(1)"
name: "xbiff"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xbiff/"
description: "xbiff – mailbox flag for X"
---

<h2 class="name">NAME</h2>
<p> xbiff &#8211; mailbox flag for X </p>
<h2>SYNOPSIS</h2>
<p> <code>xbiff</code> [ &#8211;<i>toolkitoption</i> &#8230; ] [ <i>-option</i> &#8230; ]</p>
<h2>DESCRIPTION</h2>
<p> The <i>xbiff</i> program displays a little image of a mailbox. When there is no mail, the flag on the mailbox is down. When mail arrives, the flag goes up and the mailbox beeps. By default, pressing any mouse button in the image forces <i>xbiff</i> to remember the current size of the mail file as being the &#8220;empty&#8221; size and to lower the flag.</p>
<h2>OPTIONS</h2>
<p> <i>Xbiff</i> accepts all of the standard X Toolkit command line options along with the additional options listed below:</p>
<dl>
<dt><code>-help</code></p>
<dd> This option indicates that a brief summary of the allowed options should be printed on the standard error.</p>
<dt><code>-update </code><i>seconds</i></p>
<dd> This option specifies the frequency in seconds at which <i>xbiff</i> should update its display. If the mailbox is obscured and then exposed, it will be updated immediately. The default is 30 seconds.</p>
<dt><code>-file </code><i>filename</i></p>
<dd> This option specifies the name of the file which should be monitored. By default it watches your inbox in the default location for your system (some examples are /var/mail/<i>username</i>, /usr/spool/mail/<i>username</i>, /var/spool/mail/<i>username</i> (where <i>username</i> is your login name). If the MAIL environment variable is set, the file specified by it will be monitored.</p>
<dt><code>-volume </code><i>percentage</i></p>
<dd> This option specifies how loud the bell should be rung when new mail comes in. The percentage is relative to the current volume in <i>xset</i>. So 0 is normal volume, negative percentages are towards minimum (-100 is silent), and positive percentages are towards maximum volume (100 is loudest).</p>
<dt><code>-shape</code></p>
<dd> This option indicates that the mailbox window should be shaped if masks for the empty or full images are given.</dl>
<p> The following standard X Toolkit command line arguments are commonly used with <i>xbiff:</i></p>
<dl>
<dt><code>-display </code><i>display</i></p>
<dd> This option specifies the X server to contact.</p>
<dt><code>-geometry </code><i>geometry</i></p>
<dd> This option specifies the preferred size and position of the mailbox window. The mailbox is 48 pixels wide and 48 pixels high and will be centered in the window.</p>
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
<p> The application class name is XBiff. This program uses the <i>Mailbox</i> widget. It understands all of the core resource names and classes as well as: </p>
<dl>
<dt><code>checkCommand (</code>class<code> CheckCommand)</code></p>
<dd> Specifies a shell command to be executed to check for new mail rather than examining the size of <code>file</code>. The specified string value is used as the argument to a <i><a href="/docs/linux/man/3-system/">system</a></i>(3) call and may therefore contain i/o redirection. An exit status of 0 indicates that new mail is waiting, 1 indicates that there has been no change in size, and 2 indicates that the mail has been cleared. By default, no shell command is provided.</p>
<dt><code>file (</code>class<code> File)</code></p>
<dd> Specifies the name of the file to monitor. The default is as described above for the <code>-file</code> command line option.</p>
<dt><code>onceOnly (</code>class<code> Boolean)</code></p>
<dd> Specifies that the bell is only rung the first time new mail is found and is not rung again until at least one interval has passed with no mail waiting. The window will continue to indicate the presence of new mail until it has been retrieved. The default is false.</p>
<dt><code>width (</code>class<code> Width)</code></p>
<dd> Specifies the width of the mailbox.</p>
<dt><code>height (</code>class<code> Height)</code></p>
<dd> Specifies the height of the mailbox.</p>
<dt><code>update (</code>class<code> Interval)</code></p>
<dd> Specifies the frequency in seconds at which the mail should be checked. The default is 30.</p>
<dt><code>volume (</code>class<code> Volume)</code></p>
<dd> Specifies how loud the bell should be rung. The default is 33 percent. Note that this is a percentage of the current <i>xset</i> volume. To reduce the volume, specify a negative percentage.</p>
<dt><code>foreground (</code>class<code> Foreground)</code></p>
<dd> Specifies the color for the foreground.</p>
<dt><code>reverseVideo (</code>class<code> ReverseVideo)</code></p>
<dd> Specifies that the foreground and background should be reversed.</p>
<dt><code>flip (</code>class<code> Flip)</code></p>
<dd> Specifies whether or not the image that is shown when mail has arrived should be inverted. The default is &#8220;true.&#8221;</p>
<dt><code>fullPixmap (</code>class<code> Pixmap)</code></p>
<dd> Specifies a bitmap to be shown when new mail has arrived. The default is flagup.</p>
<dt><code>emptyPixmap (</code>class<code> Pixmap)</code></p>
<dd> Specifies a bitmap to be shown when no new mail is present. The default is flagdown.</p>
<dt><code>shapeWindow (</code>class<code> ShapeWindow)</code></p>
<dd> Specifies whether or not the mailbox window should be shaped to the given fullPixmapMask and emptyPixmapMask. The default is false.</p>
<dt><code>fullPixmapMask (</code>class<code> PixmapMask)</code></p>
<dd> Specifies a mask for the bitmap to be shown when new mail has arrived. The default is none.</p>
<dt><code>emptyPixmapMask (</code>class<code> PixmapMask)</code></p>
<dd> Specifies a mask for the bitmap to be shown when no new mail is present. The default is none.</dl>
<h2>ACTIONS</h2>
<p> The <i>Mailbox</i> widget provides the following actions for use in event translations:</p>
<dl>
<dt><code>check()</code></p>
<dd> This action causes the widget to check for new mail and display the flag appropriately.</p>
<dt><code>unset()</code></p>
<dd> This action causes the widget to lower the flag until new mail comes in.</p>
<dt><code>set()</code></p>
<dd> This action causes the widget to raise the flag until the user resets it.</dl>
<p> The default translation is </p>
<pre>
        &lt;ButtonPress&gt;:  unset()
</pre>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>DISPLAY</code></p>
<dd> to get the default host and display number.</p>
<dt><code>XENVIRONMENT</code></p>
<dd> to get the name of a resource file that overrides the global resources stored in the RESOURCE_MANAGER property.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-x/">X</a>(7), <a href="/docs/linux/man/1-xrdb/">xrdb</a>(1), <a href="/docs/linux/man/2-stat/">stat</a>(2)</p>
<h2>BUGS</h2>
<p> The mailbox bitmaps are ugly.</p>
<h2>AUTHOR</h2>
<p> Jim Fulton, MIT X Consortium<br />
 Additional hacks by Ralph Swick, DEC/MIT Project Athena </p>
<h2>Index</h2>
