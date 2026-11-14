---
title: "fbset(8)"
name: "fbset"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fbset/"
description: "fbset – show and modify frame buffer device settings"
---

<p>fbset &#8211; show and modify frame buffer device settings</p>
<h2>Synopsis</h2>
<p><code>fbset</code> [<i>options</i>] [<i>mode</i>]</p>
<h2>Description</h2>
<p><code>This documentation is out of date!!</code> </p>
<p> <code>fbset</code> is a system utility to show or change the settings of the frame buffer device. The frame buffer device provides a simple and unique interface to access different kinds of graphic displays. </p>
<p> Frame buffer devices are accessed via special device nodes located in the /dev directory. The naming scheme for these nodes is always <i></i><code>fb</code>&lt;<i>n</i>&gt;, where <i>n</i> is the number of the used frame buffer device. </p>
<p> <code>fbset</code> uses an own video mode database located in /etc/fb.modes. An unlimited number of video modes can be defined in this database. For further information see <code><a href="/docs/linux/man/5-fb-modes/">fb.modes</a></code>(5).</p>
<h2>Options</h2>
<p>If no option is given, <code>fbset</code> will display the current frame buffer settings. </p>
<p> General options:</p>
<dl>
<dd>
<dl>
<dt><code>&#8211;help</code>,&nbsp;<wbr><code>-h</code></p>
<dd>display an usage information</p>
<dt><code>&#8211;now</code>,&nbsp;<wbr><code>-n</code></p>
<dd>change the video mode immediately. If no frame buffer device is given via <code>-fb</code> , then this option is activated by default</p>
<dt><code>&#8211;show</code>,&nbsp;<wbr><code>-s</code></p>
<dd>display the video mode settings. This is default if no further option or only a frame buffer device via <code>-fb</code> is given</p>
<dt><code>&#8211;info</code>,&nbsp;<wbr><code>-i</code></p>
<dd>display all available frame buffer information</p>
<dt><code>&#8211;verbose</code>,&nbsp;<wbr><code>-v</code></p>
<dd>display information what <code>fbset</code> is currently doing</p>
<dt><code>&#8211;version</code>,&nbsp;<wbr><code>-V</code></p>
<dd>display the version information about <code>fbset</code></p>
<dt><code>&#8211;xfree86</code>,&nbsp;<wbr><code>-x</code></p>
<dd>display the timing information as it&#8217;s needed by XFree86</dl>
</dl>
<p> Frame buffer device nodes:</p>
<dl>
<dd>
<dl>
<dt><code>-fb</code>&nbsp;<wbr>&lt;<i>device</i>&gt;</p>
<dd><i>device</i> gives the frame buffer device node. If no device via <code>-fb</code> is given, <i>/dev/fb0</i> is used</dl>
</dl>
<p> Video mode database:</p>
<dl>
<dd>
<dl>
<dt><code>-db</code>&nbsp;<wbr>&lt;<i>file</i>&gt;</p>
<dd>set an alternative video mode database file (default is <i>/etc/fb.modes</i>), see also <code><a href="/docs/linux/man/5-fb-modes/">fb.modes</a></code>(5)</dl>
</dl>
<p> Display geometry:</p>
<dl>
<dd>
<dl>
<dt><code>-xres</code>&nbsp;<wbr>&lt;<i>value</i>&gt;</p>
<dd>set visible horizontal resolution (in pixels)</p>
<dt><code>-yres</code>&nbsp;<wbr>&lt;<i>value</i>&gt;</p>
<dd>set visible vertical resolution (in pixels)</p>
<dt><code>-vxres</code>&nbsp;<wbr>&lt;<i>value</i>&gt;</p>
<dd>set virtual horizontal resolution (in pixels)</p>
<dt><code>-vyres</code>&nbsp;<wbr>&lt;<i>value</i>&gt;</p>
<dd>set virtual vertical resolution (in pixels)</p>
<dt><code>-depth</code>&nbsp;<wbr>&lt;<i>value</i>&gt;</p>
<dd>set display depth (in bits per pixel)</p>
<dt><code>&#8211;geometry</code>,&nbsp;<wbr><code>-g</code>&nbsp;<wbr>&#8230;</p>
<dd>set all geometry parameters at once in the order &lt;<i>xres</i>&gt; &lt;<i>yres</i>&gt; &lt;<i>vxres</i>&gt; &lt;<i>vyres</i>&gt; &lt;<i>depth</i>&gt;, e.g. <code>-g</code> <i>640 400 640 400 4</i></p>
<dt><code>-match</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></p>
<dd>make the physical resolution match the virtual resolution</dl>
</dl>
<p> Display timings:</p>
<dl>
<dd>
<dl>
<dt><code>-pixclock</code>&nbsp;<wbr>&lt;<i>value</i>&gt;</p>
<dd>set the length of one pixel (in picoseconds). Note that the frame buffer device may only support some pixel lengths</p>
<dt><code>-left</code>&nbsp;<wbr>&lt;<i>value</i>&gt;</p>
<dd>set left margin (in pixels)</p>
<dt><code>-right</code>&nbsp;<wbr>&lt;<i>value</i>&gt;</p>
<dd>set right margin (in pixels)</p>
<dt><code>-upper</code>&nbsp;<wbr>&lt;<i>value</i>&gt;</p>
<dd>set upper margin (in pixel lines)</p>
<dt><code>-lower</code>&nbsp;<wbr>&lt;<i>value</i>&gt;</p>
<dd>set lower margin (in pixel lines)</p>
<dt><code>-hslen</code>&nbsp;<wbr>&lt;<i>value</i>&gt;</p>
<dd>set horizontal sync length (in pixels)</p>
<dt><code>-vslen</code>&nbsp;<wbr>&lt;<i>value</i>&gt;</p>
<dd>set vertical sync length (in pixel lines)</p>
<dt><code>&#8211;timings</code>,&nbsp;<wbr><code>-t</code>&nbsp;<wbr>&#8230;</p>
<dd>set all timing parameters at once in the order &lt;<i>pixclock</i>&gt; &lt;<i>left</i>&gt; &lt;<i>right</i>&gt; &lt;<i>upper</i>&gt; &lt;<i>lower</i>&gt; &lt;<i>hslen</i>&gt; &lt;<i>vslen</i>&gt;, e.g. <code>-g</code> <i>35242 64 96 35 12 112 2</i></dl>
</dl>
<p> Display flags:</p>
<dl>
<dd>
<dl>
<dt><i></i><code>-hsync</code>&nbsp;<wbr>{<i>low</i>|<i>high</i>}</p>
<dd>set the horizontal sync polarity</p>
<dt><i></i><code>-vsync</code>&nbsp;<wbr>{<i>low</i>|<i>high</i>}</p>
<dd>set the vertical sync polarity</p>
<dt><i></i><code>-csync</code>&nbsp;<wbr>{<i>low</i>|<i>high</i>}</p>
<dd>set the composite sync polarity</p>
<dt><i></i><code>-extsync</code>&nbsp;<wbr>{<i>false</i>|<i>true</i>}</p>
<dd>enable or disable external resync. If enabled the sync timings are not generated by the frame buffer device and must be provided externally instead. Note that this option may not be supported by every frame buffer device</p>
<dt><i></i><code>-bcast</code>&nbsp;<wbr>{<i>false</i>|<i>true</i>}</p>
<dd>enable or disable broadcast modes. If enabled the frame buffer generates the exact timings for several broadcast modes (e.g. PAL or NTSC). Note that this option may not be supported by every frame buffer device</p>
<dt><i></i><code>-laced</code>&nbsp;<wbr>{<i>false</i>|<i>true</i>}</p>
<dd>enable or disable interlace. If enabled the display will be split in two frames, each frame contains only even and odd lines respectively. These two frames will be displayed alternating, this way twice the lines can be displayed and the vertical frequency for the monitor stays the same, but the visible vertical frequency gets halved</p>
<dt><i></i><code>-double</code>&nbsp;<wbr>{<i>false</i>|<i>true</i>}</p>
<dd>enable or disable doublescan. If enabled every line will be displayed twice and this way the horizontal frequency can easily be doubled, so that the same resolution can be displayed on different monitors, even if the horizontal frequency specification differs. Note that this option may not be supported by every frame buffer device</dl>
</dl>
<p> Display positioning:</p>
<dl>
<dd>
<dl>
<dt><i></i><code>-move</code>&nbsp;<wbr>{<i>left</i>|<i>right</i>|<i>up</i>|<i>down</i>}</p>
<dd>move the visible part of the display in the specified direction</p>
<dt><code>-step</code>&nbsp;<wbr>&lt;<i>value</i>&gt;</p>
<dd>set step size for display positioning (in pixels or pixel lines), if <code>-step</code> is not given display will be moved 8 pixels horizontally or 2 pixel lines vertically</dl>
</dl>
<h2>Example</h2>
<p>To set the used video mode for <code>X</code> insert the following in rc.local:</p>
<dl>
<dd><code>fbset</code> -fb <i>/dev/fb0</i> vga </p>
</dl>
<p> and make the used frame buffer device known to <code>X</code>:</p>
<dl>
<dd><code>export</code> FRAMEBUFFER=<i>/dev/fb0</i></dl>
<h2>Files</h2>
<p><i>/dev/fb*</i><br />
 <i>/etc/fb.modes</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-fb-modes/">fb.modes</a></code>(5), <code><a href="/docs/linux/man/4-fbdev/">fbdev</a></code>(4)</p>
<h2>Authors</h2>
<dl>
<dt>Geert Uytterhoeven &lt;Geert.Uytterhoeven [at] cs.kuleuven.ac.be&gt;</p>
<dd>
<dt>Roman Zippel &lt;zippel [at] fh-brandenburg.de&gt;</p>
<dd>man files </p>
</dl>
