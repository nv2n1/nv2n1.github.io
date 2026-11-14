---
title: "mupdisp(1)"
name: "mupdisp"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mupdisp/"
description: "mupdisp – display output from Mup music publisher program"
---

<h2>NAME</h2>
<p> mupdisp &#8211; display output from Mup music publisher program</p>
<h2>SYNOPSIS</h2>
<p> mupdisp <i>[mup_options] file</i></p>
<h2>DESCRIPTION</h2>
<p> Mupdisp provides a way to view Mup output on your screen. The <i>file</i> is Mup input. Any other Mup options can be given, except -C, -E, -f, -F, -l, -m, -M, or -v, which don&#8217;t produce print output. </p>
<p> Mupdisp will run under MS-DOS or will run under UNIX with a TERM of AT386, linux, or xterm (under X windows). </p>
<p> When running under X windows, several standard X options are available:</p>
<dl>
<dt><code>-geometry</code> <i>XxY+M+N</i></p>
<dd> Sets the window size and/or location on the screen. The actual window width will be determined by the width of the Mup output. The height will be adjusted if necessary to be between 400 and the actual height of the Mup output. The window placment specifications can be positive or negative. The actual placement may be adjusted by your window manager.</p>
<dt><code>-fg</code> <i>color</i> or <code>-foreground</code> <i>color</i></p>
<dd> Specifies the foreground color to use.</p>
<dt><code>-bg</code> <i>color</i> or <code>-background</code> <i>color</i></p>
<dd> Specifies the background color to use.</dl>
<p> These X options can also be set in your .Xdefaults file using resource names of mupdisp.geometry, mupdisp.foreground, and mupdisp.background. Command line arguments will override values in the .Xdefaults file. As an example, you could add these lines to your .Xdefaults file: </p>
<pre>
mupdisp.foreground:   navy
mupdisp.background:   gray
mupdisp.geometry:     400x760+100-34
</pre>
<p> The Mupdisp program begins in partial page mode, which displays output at approximately actual size (depending on the size of your monitor). In this mode, it may be that not all of the page fits on the screen, so the scrolling commands can be used to move up and down to view different parts of the page. In full page mode, a small version of the entire page is displayed. This is useful for seeing overall page layout, but is generally too small to see much detail. This mode is now somewhat of a relic of the days when screens were typically much smaller than they are today, and is thus becoming less useful. </p>
<p> If the environment variable MUPDISPMODE is set to some value, Mupdisp will start in full page rather than partial page mode. </p>
<p> The commands are:</p>
<dl>
<dt><i>num</i>&lt;Enter&gt;</p>
<dd> Go to page number <i>num</i>.</p>
<dt>+ or &lt;space&gt; or &lt;control-E&gt; or &lt;control-F&gt;</p>
<dd> move forward on the page by about 1/8 of an inch (partial page mode only)</p>
<dt>&#8211; or &lt;backspace&gt; or &lt;control-Y&gt; or &lt;control-B&gt;</p>
<dd> move backward on the page by about 1/8 of an inch (partial page mode only)</p>
<dt>b or &lt;control-U&gt; or &lt;control-P&gt; or &lt;up-arrow-key&gt;</p>
<dd> move backward on the page by about an inch (partial page mode only)</p>
<dt>f or &lt;Enter&gt; or &lt;control-D&gt; or &lt;control-N&gt; or &lt;down-arrow-key&gt;</p>
<dd> move forward on the page by about an inch (partial page mode only)</p>
<dt>h or ?</p>
<dd> display help screen</p>
<dt>m</p>
<dd> toggle between partial page and full page modes.</p>
<dt>n or &lt;PageDown&gt;</p>
<dd> go to next page</p>
<dt>p or &lt;PageUp&gt;</p>
<dd> go to previous page</p>
<dt>q or ZZ</p>
<dd> quit</p>
<dt>r</p>
<dd> Repaint the page (useful for exiting help page)</dl>
<p> When in X windows, the mouse can be used for scrolling. The left button scrolls downward like the f command, while the right button scrolls backwards like the b command. </p>
<p> Mupdisp supports page sizes of letter (8.5 x 11.0 inches), note (7.5 x 10.0 inches), legal (8.5 x 14.0 inches), A4 (8.26 x 11.69 inches), A5 (5.85 x 8.26 inches), A6 (4.125 x 5.85 inches), flsa (8.5 x 13.0 inches), and halfletter (5.5 x 8.5 inches).</p>
<h2>FILES</h2>
<p> $HOME/.Xdefaults default X window resource definitions</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-gs/">gs</a>(1), <a href="/docs/linux/man/1-mup/">mup</a>(1), <a href="/docs/linux/man/1-mupmate/">mupmate</a>(1), <a href="/docs/linux/man/1-mupprnt/">mupprnt</a>(1).<br />
 Mup &#8212; Music Publisher User&#8217;s Guide</p>
<h2>CAVEATS AND BUGS</h2>
<p> You must have mup in your PATH. You must have ghostscript (gs or gs386.exe) in your PATH and it must be built to include the &quot;bit&quot; device. </p>
<p> Resizing the window does not resize the full page view. </p>
<h2>Index</h2>
