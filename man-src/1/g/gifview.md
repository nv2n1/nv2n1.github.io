---
title: "gifview(1)"
name: "gifview"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gifview/"
description: "gifview – displays GIF images and animations on the X window system"
---

<h2>NAME</h2>
<p> gifview &#8211; displays GIF images and animations on the X window system</p>
<h2>SYNOPSIS</h2>
<p> <code>gifview</code> [<code>&#8211;display</code> <i>display</i>] [options] [filenames and frames]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>gifview</code> displays GIF image files on workstations and terminals running the X Window System. <code>gifview</code> understands multi-image GIFs, which can be displayed either as slideshows or as animations.</p>
<h2>INTERACTION</h2>
<p> <code>gifview</code> windows recognize several keystrokes and button commands. Many of them are only useful for multi-image GIFs.</p>
<dl>
<dt>Space or <code>n</code></p>
<dd> Go to the next frame.</p>
<dt><code>b</code> or <code>p</code></p>
<dd> Go to the previous frame.</p>
<dt><code>r</code> or <code>&lt;</code></p>
<dd> Go to the first frame.</p>
<dt><code>&gt;</code></p>
<dd> Go to the last frame.</p>
<dt>ESC</p>
<dd> Stop the animation.</p>
<dt><code>s</code> or <code>a</code></p>
<dd> Toggle between animation and slideshow mode.</p>
<dt><code>u</code></p>
<dd> Toggle between normal and unoptimized mode.</p>
<dt>Backspace</p>
<dd> Delete this window.</p>
<dt><code>q</code></p>
<dd> Quit <code>gifview</code>.</dl>
<p> Left-clicking on a window goes to the next frame; right-clicking on a window deletes that window.</p>
<h2>COMMAND LINE</h2>
<p> <code>gifview</code>&#8216;s command line consists of <i>GIF input files</i> and <i>options</i>. Most options start with a dash (-) or plus (+); frame selections, a kind of option, start with a number sign (#). Anything else is a GIF input file. </p>
<p> <code>gifview</code> displays one window for each GIF input file you specify. If no GIF input file is given, or you give the special filename `-&#8216;, it reads from the standard input.</p>
<h2>OPTIONS</h2>
<dl>
<dt> <code>&#8211;animate</code>, <code>-a</code></p>
<dd> Animate multi-image GIFs by default. Normally, multi-image GIFs first appear in slideshow mode. You can always use the `<code>a</code>&#8216; keystroke to toggle between modes. This option has a converse, `<code>&#8211;no-animate</code>&#8216; or `<code>+a</code>&#8216;. </p>
<dt> <code>&#8211;unoptimize</code>, <code>-U</code></p>
<dd> Display multi-image GIFs as &#8220;unoptimized&#8221;, which shows a faithful representation of what a user will see at each frame of an animation. See <code><a href="/docs/linux/man/1-gifsicle/">gifsicle</a></code>(1) for a more detailed description of unoptimization. This option has a converse, `<code>&#8211;no-unoptimize</code>&#8216; or `<code>+U</code>&#8216;. GIFs are always displayed unoptimized in animation mode. </p>
<dt> <i></i><code>-d </code><i>display</i><i></i><i></i></p>
<dd>
<dt> <i></i><code>&#8211;display </code><i>display</i><i></i><i></i></p>
<dd> Sets the X display to <i>display</i>. This option must come before any GIF files. </p>
<dt> <i></i><code>&#8211;name </code><i>name</i><i></i><i></i></p>
<dd> Sets the application name under which resources are found, rather than the default of &quot;gifview&quot;. Since <code>gifview</code> itself does not use the resource database, this is mostly useful for communication with your window manager. </p>
<dt> <i></i><code>&#8211;geometry </code><i>geometry</i><i></i><i></i></p>
<dd> Set the size and position of <code>gifview</code>&#8216;s windows. This is a standard X option. At most one <code>&#8211;geometry</code> option can be given per window (that is, per input GIF file). </p>
<dt> <i></i><code>&#8211;title </code><i>title</i><i></i><i></i></p>
<dd> Sets the <code>gifview</code> window&#8217;s title. The default is &quot;gifview&quot;, followed by information about the currently displayed file and frame. </p>
<dt> <i></i><code>-w </code><i>window</i><i></i><i></i></p>
<dd>
<dt> <i></i><code>&#8211;window </code><i>window</i><i></i><i></i></p>
<dd> Display the next GIF input in an existing X window, instead of making a new top-level window. This way, you can use <code>gifview</code> to display animated GIFs in a window you created with another program. The <i>window</i> argument should be an integer (<code>gifview</code> will use that window ID) or `root&#8217; (<code>gifview</code> will use the root window). </p>
<dt> <i></i><code>&#8211;new-window </code><i>window</i><i></i><i></i></p>
<dd> Display the next GIF input in a new child of an existing X window. This child window will disappear when <code>gifview</code> exits. The <i>window</i> argument should be an integer (<code>gifview</code> will use that window ID) or `root&#8217; (<code>gifview</code> will use the root window). </p>
<dt> <code>&#8211;install-colormap</code>, <code>-i</code></p>
<dd> Use a private colormap for each window (if you are using a PseudoColor display). This avoids polluting the existing colormap, and may produce better results if your colormap is full, but causes annoying colormap flashing. </p>
<dt> <i></i><code>&#8211;background </code><i>color</i><i></i><i></i></p>
<dd>
<dt> <i></i><code>&#8211;bg </code><i>color</i><i></i><i></i></p>
<dd> Set the background color, which is used for transparent pixels. </p>
<dt> <i></i><code>&#8211;min-delay </code><i>delay</i><i></i><i></i></p>
<dd> Set the minimum delay between frames to <i>delay</i>, which is measured in hundredths of a second. Default is 0. </p>
<dt> <i></i><code>&#8211;fallback-delay </code><i>delay</i><i></i><i></i></p>
<dd> Set the frame delay of GIFs that do not specify a delay value or have a delay of 0. The final value is still subject to the value of &#8211;min-delay. Like &#8211;min-delay, <i>delay</i> is measured in hundredths of a second. Default is 0. </p>
<dt> <code>&#8211;no-interactive</code>, <code>+e</code></p>
<dd> Don&#8217;t pay attention to mouse buttons or keystrokes. </p>
<dt> <code>&#8211;memory-limit</code>lim</p>
<dd> Cache at most <i>lim</i> megabytes of images in memory when animating. Default is 40. </p>
<dt> <code>&#8211;help</code></p>
<dd> Print usage information and exit. </p>
<dt> <code>&#8211;version</code></p>
<dd> Print the version number and some quickie warranty information and exit.</dl>
<h3>Frame Selections</h3>
<p> A frame selection tells <code>gifview</code> which frame to initially display from the current input file. They are useful only for animations, as non-animated GIFs only have one frame. Frame selections can only be displayed in slideshow mode. </p>
<dl>
<dt><code>#</code><i>num</i></p>
<dd> Select frame <i>num</i>. (The first frame is `<code>#0</code>&#8216;. Negative numbers count backwards from the last frame, which is `<code>#-1</code>&#8216;.)</p>
<dt><code>#</code><i>name</i></p>
<dd> Select the frame named <i>name</i>.</dl>
<p> If you give two or more frame selections, you will get one window per frame selection.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gifsicle/">gifsicle</a></code>(1)</p>
<h2>BUGS</h2>
<p> Please email suggestions, additions, patches and bugs to ekohler [at] gmail.com.</p>
<h2>AUTHORS</h2>
<p> Eddie Kohler, ekohler [at] gmail.com<br />
 <a rel="nofollow" href="http://www.read.seas.harvard.edu/~kohler/">http://www.read.seas.harvard.edu/~kohler/</a> </p>
<p> <a rel="nofollow" href="http://www.lcdf.org/gifsicle/">http://www.lcdf.org/gifsicle/</a><br />
 The <code>gifsicle</code> home page. </p>
<h2>Index</h2>
