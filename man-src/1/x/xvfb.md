---
title: "xvfb(1)"
name: "xvfb"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xvfb/"
description: "Xvfb – virtual framebuffer X server for X Version 11"
---

<p>Xvfb &#8211; virtual framebuffer X server for X Version 11</p>
<h2>Synopsis</h2>
<p><code>Xvfb</code> [ option ] &#8230;</p>
<h2>Description</h2>
<p><i>Xvfb</i> is an X server that can run on machines with no display hardware and no physical input devices. It emulates a dumb framebuffer using virtual memory. </p>
<p> The primary use of this server was intended to be server testing. The fb code for any depth can be exercised with this server without the need for real hardware that supports the desired depths. The X community has found many other novel uses for <i>Xvfb</i>, including testing clients against unusual depths and screen configurations, doing batch processing with <i>Xvfb</i> as a background rendering engine, load testing, as an aid to porting the X server to a new platform, and providing an unobtrusive way to run applications that don&#8217;t really need an X server but insist on having one anyway.</p>
<h2>Options</h2>
<p>In addition to the normal server options described in the <i><a href="/docs/linux/man/1-xserver/">Xserver</a>(1)</i> manual page, <i>Xvfb</i> accepts the following command line switches:</p>
<dl>
<dt><code>-screen </code><i>screennum</i> <i>WxHxD</i></p>
<dd>This option creates screen <i>screennum</i> and sets its width, height, and depth to W, H, and D respectively. By default, only screen 0 exists and has the dimensions 1280x1024x8.</p>
<dt><code>-pixdepths </code><i>list-of-depths</i></p>
<dd>This option specifies a list of pixmap depths that the server should support in addition to the depths implied by the supported screens. <i>list-of-depths</i> is a space-separated list of integers that can have values from 1 to 32.</p>
<dt><code>-fbdir </code><i>framebuffer-directory</i></p>
<dd>This option specifies the directory in which the memory mapped files containing the framebuffer memory should be created. See FILES. This option only exists on machines that have the mmap and msync system calls.</p>
<dt><code>-shmem</code></p>
<dd>This option specifies that the framebuffer should be put in shared memory. The shared memory ID for each screen will be printed by the server. The shared memory is in xwd format. This option only exists on machines that support the System V shared memory interface.</dl>
<p> If neither <code>-shmem</code> nor <code>-fbdir</code> is specified, the framebuffer memory will be allocated with malloc().</p>
<dl>
<dt><code>-linebias </code><i>n</i></p>
<dd>This option specifies how to adjust the pixelization of thin lines. The value <i>n</i> is a bitmask of octants in which to prefer an axial step when the Bresenham error term is exactly zero. See the file Xserver/mi/miline.h for more information. This option is probably only useful to server developers to experiment with the range of line pixelization possible with the fb code.</p>
<dt><code>-blackpixel </code><i>pixel-value</i>, -whitepixel <i>pixel-value</i></p>
<dd>These options specify the black and white pixel values the server should use.</dl>
<h2>Files</h2>
<p>The following files are created if the -fbdir option is given.</p>
<dl>
<dt><i>framebuffer-directory</i>/Xvfb_screen&lt;n&gt;</p>
<dd>Memory mapped file containing screen n&#8217;s framebuffer memory, one file per screen. The file is in xwd format. Thus, taking a full-screen snapshot can be done with a file copy command, and the resulting snapshot will even contain the cursor image.</dl>
<h2>Examples</h2>
<dl>
<dt>Xvfb :1 -screen 0 1600x1200x32</p>
<dd>The server will listen for connections as server number 1, and screen 0 will be depth 32 1600&#215;1200.</p>
<dt>Xvfb :1 -screen 1 1600x1200x16</p>
<dd>The server will listen for connections as server number 1, will have the default screen configuration (one screen, 1280x1024x8), and screen 1 will be depth 16 1600&#215;1200.</p>
<dt>Xvfb -pixdepths 3 27 -fbdir /var/tmp</p>
<dd>The server will listen for connections as server number 0, will have the default screen configuration (one screen, 1280x1024x8), will also support pixmap depths of 3 and 27, and will use memory mapped files in /var/tmp for the framebuffer.</p>
<dt>xwud -in /var/tmp/Xvfb_screen0</p>
<dd>Displays screen 0 of the server started by the preceding example.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/7-x/">X</a>(7), <a href="/docs/linux/man/1-xserver/">Xserver</a>(1), <a href="/docs/linux/man/1-xwd/">xwd</a>(1), <a href="/docs/linux/man/1-xwud/">xwud</a>(1), XWDFile.h</p>
<h2>Authors</h2>
<p>David P. Wiggins, The Open Group, Inc.</p>
