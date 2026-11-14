---
title: "fbi(1)"
name: "fbi"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fbi/"
description: "fbi – Linux framebuffer imageviewer # #"
---

<p>#</p>
<h2 class="name">NAME</h2>
<p> fbi &#8211; Linux framebuffer imageviewer # # </p>
<h2>SYNOPSIS</h2>
<p> <code>fbi</code> [<i>options</i>] <i>file &#8230;</i> # #</p>
<h2>DESCRIPTION</h2>
<p> <code>Fbi</code> displays the specified file(s) on the linux console using the framebuffer device. <i>PhotoCD</i>, <i>jpeg</i>, <i>ppm</i>, <i>gif</i>, <i>tiff</i>, <i>xwd</i>, <i>bmp</i>, <i>png</i> and <i>webp</i> formats are supported natively. For other <code>fbi</code> tries to use <code><a href="/docs/linux/man/1-imagemagick/">ImageMagick</a></code>(1)&#8217;s <code><a href="/docs/linux/man/1-convert/">convert</a></code>(1). # #</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Print usage info.</p>
<dt><code>-V, &#8211;version</code></p>
<dd> Print <code>fbi</code> version number.</p>
<dt><code>&#8211;store</code></p>
<dd> Write command line arguments to config file.</p>
<dt><code>-l</code><i>&nbsp;<wbr>file</i><code>, &#8211;list</code><i>&nbsp;<wbr>file</i></p>
<dd> Read image filelist from <i>file</i>.</p>
<dt><code>-P, &#8211;text</code></p>
<dd> Enable textreading mode. In this mode <code>fbi</code> will display large images without vertical offset (default is to center the images). The <code>SPACE</code> command will first try to scroll down and go to the next image only if it is already on the bottom of the page. Useful if the images you are watching are text pages, all you have to do to get the next piece of text is to press space&#8230;</p>
<dt><code>-a, &#8211;autozoom</code></p>
<dd> Enable autozoom. <code>Fbi</code> will automagically pick a reasonable zoom factor when loading a new image.</p>
<dt><code>&#8211;(no)autoup</code></p>
<dd> Like autozoom, but scale up only.</p>
<dt><code>&#8211;(no)autodown</code></p>
<dd> Like autozoom, but scale down only.</p>
<dt><code>&#8211;(no)fitwidth</code></p>
<dd> Use width only for autoscaling.</p>
<dt><code>-v, &#8211;(no)verbose</code></p>
<dd> Be verbose: enable status line on the bottom of the screen.</p>
<dt><code>-u, &#8211;(no)random</code></p>
<dd> Randomize the order of the filenames.</p>
<dt><code>&#8211;(no)comments</code></p>
<dd> Display comment tags (if present) instead of the filename. Probably only useful if you added reasonable comments yourself (using <code><a href="/docs/linux/man/1-wrjpgcom/">wrjpgcom</a></code>(1) for example), otherwise you likely just find texts pointing to the software which created the image.</p>
<dt><code>-e, &#8211;(no)edit</code></p>
<dd> Enable editing commands.</p>
<dt><code>&#8211;(no)backup</code></p>
<dd> Create backup files (when editing images).</p>
<dt><code>-p, &#8211;(no)preserve</code></p>
<dd> Preserve timestamps (when editing images).</p>
<dt><code>&#8211;(no)readahead</code></p>
<dd> Read ahead images into cache.</p>
<dt><code>&#8211;cachemem</code><i>&nbsp;<wbr>size</i></p>
<dd> Image cache <i>size</i> in megabytes (MB).</p>
<dt><code>&#8211;blend</code><i>&nbsp;<wbr>time</i></p>
<dd> Image blend <i>time</i> in miliseconds.</p>
<dt><code>-T</code><i>&nbsp;<wbr>n</i><code>, &#8211;vt</code><i>&nbsp;<wbr>n</i></p>
<dd> Start on virtual console <i>n</i>.</p>
<dt><code>-s</code><i>&nbsp;<wbr>steps</i><code>, &#8211;scroll</code><i>&nbsp;<wbr>steps</i></p>
<dd> Set scroll <i>steps</i> in pixels (default is 50).</p>
<dt><code>-t</code><i>&nbsp;<wbr>sec</i><code>, &#8211;timeout</code><i>&nbsp;<wbr>sec</i></p>
<dd> Load next image after <i>sec</i> seconds without any keypress (i.e. slideshow).</p>
<dt><code>-1, &#8211;(no)once</code></p>
<dd> Don&#8217;t loop (only use with <code>-t</code>).</p>
<dt><code>-r</code><i>&nbsp;<wbr>n</i><code>, &#8211;resolution</code><i>&nbsp;<wbr>n</i></p>
<dd> Select resolution, <i>n = 1..5</i> (only <i>PhotoCD</i>).</p>
<dt><code>-g</code><i>&nbsp;<wbr>n</i><code>, &#8211;gamma</code><i>&nbsp;<wbr>n</i></p>
<dd> Gamma correction. Default is 1.0. Requires <i>Pseudocolor</i> or <i>Directcolor</i> visual, doesn&#8217;t work for <i>Truecolor</i>.</p>
<dt><code>-f</code><i>&nbsp;<wbr>&lt;arg&gt;</i><code>, &#8211;font</code><i>&nbsp;<wbr>&lt;arg&gt;</i></p>
<dd> Set font. This <i>&lt;arg&gt;</i> can be anything fontconfig accepts (see <code><a href="/docs/linux/man/5-fonts-conf/">fonts-conf</a></code>(5)). Try <code><a href="/docs/linux/man/1-fc-list/">fc-list</a></code>(1) for a list of known fonts on your system. The fontconfig config file is evaluated as well, so any generic stuff defined there (such as mono, sans) will work as well. It is recommended to use monospaced fonts, the textboxes (help text, exif info) look better then.</p>
<dt><code>-d</code><i>&nbsp;<wbr>/dev/fbN</i><code>, &#8211;device</code><i>&nbsp;<wbr>/dev/fbN</i></p>
<dd> Use <i>/dev/fbN</i> device framebuffer. Default is the one your virtual console is mapped to.</p>
<dt><code>-m</code><i>&nbsp;<wbr>videomode</i><code>, &#8211;mode</code><i>&nbsp;<wbr>videomode</i></p>
<dd> Name of the video mode to use (video mode must be listed in <i>/etc/fb.modes</i>). Default is not to change the video mode. # #</dl>
<h2>ENVIRONMENT</h2>
<p> <code>Fbi</code> uses the following environment variables:</p>
<dl>
<dt><code>FBGAMMA</code></p>
<dd> This variable may be used to specify a default gamma correction. # #</dl>
<h2>COMMAND USAGE</h2>
<p> The commands take effect immediately; it is not necessary to type a carriage return. </p>
<p> In the following commands, <i>i</i> is a numerical argument.</p>
<h3>Scrolling</h3>
<dl>
<dt><code>LEFT_ARROW</code>, <code>RIGHT_ARROW</code>, <code>UP_ARROW</code>, <code>DOWN_ARROW</code></p>
<dd> Scroll large images.</p>
<dt><code>PREV_SCREEN</code>, <code>k</code></p>
<dd> Previous image.</p>
<dt><code>NEXT_SCREEN</code>, <code>SPACE</code>, <code>j</code></p>
<dd> Next image.</p>
<dt><i>i</i><code>g</code></p>
<dd> Jump to image #<i>i</i>.</p>
<dt><code>RETURN</code></p>
<dd> Write the filename of the current image to <code><a href="/docs/linux/man/3-stdout/">stdout</a></code>(3), then go to the next image.</dl>
<p> The <code>RETURN</code> vs. <code>SPACE</code> key thing can be used to create a file list while reviewing the images and use the list for batch processing later on: </p>
<p> <i>fbi file1.gif file2.jpg file3.jpg &gt;&nbsp;<wbr>fileimagelist.lst</i> </p>
<p> some <code>RETURN</code> and <code>SPACE</code>&#8230; </p>
<p> <i>fbi -l fileimagelist.lst</i></p>
<h3>Zoom</h3>
<dl>
<dt><code>a</code></p>
<dd> Autozoom.</p>
<dt><code>+</code></p>
<dd> In.</p>
<dt><code>&#8211;</code></p>
<dd> Out.</p>
<dt><i>i</i><code>s</code></p>
<dd> Set zoom to <i>i</i>%.</dl>
<h3>Other</h3>
<dl>
<dt><code>ESQ</code>, <code>q</code></p>
<dd> Quit.</p>
<dt><code>v</code></p>
<dd> Toggle status line.</p>
<dt><code>h</code></p>
<dd> Display textbox with brief help.</p>
<dt><code>i</code></p>
<dd> Display textbox with some <i>EXIF</i> info.</p>
<dt><code>p</code></p>
<dd> Pause the slideshow (if started with <code>-t</code>, toggle).</dl>
<h3>Edit mode</h3>
<p> <code>Fbi</code> also provides some very basic image editing facilities. You have to start <code>fbi</code> with the <i>-e</i> switch to use them.</p>
<dl>
<dt><code>D</code>, <code>Shift+d</code></p>
<dd> Delete image.</p>
<dt><code>r</code></p>
<dd> Rotate 90 degrees clockwise.</p>
<dt><code>l</code></p>
<dd> Rotate 90 degrees counter-clock wise.</p>
<dt><code>x</code></p>
<dd> Mirror image vertically (top / bottom).</p>
<dt><code>y</code></p>
<dd> Mirror image horizontally (left to right).</dl>
<p> The delete function actually wants a capital letter <code>D</code>, thus you have to type <code>Shift+d</code>. This is done to avoid deleting images by mistake because there are no safety bells: If you ask <code>Â fbi</code> to delete the image, it will be deleted without questions asked. </p>
<p> The rotate function actually works for <i>JPEG</i> images only. It does a lossless transformation of the image. # #</p>
<h2>BUGS</h2>
<p> <code>Fbi</code> needs rw access to the framebuffer devices (<i>/dev/fbN</i>), i.e you (our your admin) have to make sure <code>fbi</code> can open the devices in rw mode. The IMHO most elegant way is to use <code><a href="/docs/linux/man/7-pam/">PAM</a></code>(7) to chown the devices to the user logged in on the console. Another way is to create some group, chown the special files to that group and put the users which are allowed to use the framebuffer device into the group. You can also make the special files world writable, but be aware of the security implications this has. On a private box it might be fine to handle it this way though. </p>
<p> <code>Fbi</code> also needs access to the linux console (<i>/dev/ttyN</i>) for sane console switch handling. That is obviously no problem for console logins, but any kind of a pseudo tty (xterm, ssh, screen, &#8230;) will <code>not</code> work. # #</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-convert/">convert</a></code>(1), <code><a href="/docs/linux/man/1-fbset/">fbset</a></code>(1), <code><a href="/docs/linux/man/1-fc-list/">fc-list</a></code>(1), <code><a href="/docs/linux/man/1-imagemagick/">imagemagick</a></code>(1), <code><a href="/docs/linux/man/1-wrjpgcom/">wrjpgcom</a></code>(1), <code><a href="/docs/linux/man/5-fonts-conf/">fonts-conf</a></code>(5), <code><a href="/docs/linux/man/7-pam/">PAM</a></code>(7) # #</p>
<h2>AUTHOR</h2>
<p> Gerd Hoffmann <code>&lt;gerd [at] kraxel.org&gt;</code> # #</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 1999-2012 Gerd Hoffmann &lt;gerd [at] kraxel.org&gt; </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA. </p>
<h2>Index</h2>
