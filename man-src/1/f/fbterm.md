---
title: "fbterm(1)"
name: "fbterm"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fbterm/"
description: "FbTerm – a fast Frame Buffer based TERMinal emulator for linux"
---

<h2>NAME</h2>
<p> FbTerm &#8211; a fast Frame Buffer based TERMinal emulator for linux</p>
<h2>SYNOPSIS</h2>
<p> <code>fbterm</code> [<i>options</i>] [&#8211;] [<i>command</i> [<i>arguments</i>]]</p>
<h2>DESCRIPTION</h2>
<p> FbTerm is a fast terminal emulator for linux with frame buffer device or VESA video card. Features include:<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>mostly as fast as terminal of linux kernel while accelerated scrolling is enabled<br />
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>select font with fontconfig and draw text with freetype2, same as Qt/Gtk+&nbsp;<wbr>based GUI apps<br />
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>dynamically create/destroy up to 10 windows initially running default shell<br />
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>record scroll-back history for every window<br />
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>auto-detect current locale and convert text encoding, support double width scripts like Chinese, Japanese etc<br />
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>switch between configurable additional text encodings with hot keys on the fly<br />
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>copy/past selected text between windows with mouse when gpm server is running<br />
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>change the orientation of screen display, a.k.a. screen rotation<br />
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>lightweight input method framework with client-server architecture<br />
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>background image for eye candy</p>
<h2>OPTIONS</h2>
<p> <i>command</i> [<i>arguments</i>] may be given to override the built-in choice of shell program. Normally FbTerm checks the <i>SHELL</i> variable. If that is not set, it tries to use the user&#8217;s login shell program specified in the password file. If that is not set, /bin/sh will be used. You should use the <i>&#8212;</i> argument to separate FbTerm&#8217;s options from the arguments supplied to the <i>command</i>. </p>
<p> FbTerm first uses option value specified in command line arguments, then in the configure file <i>$HOME/.fbtermrc</i>. If that file doesn&#8217;t exist, FbTerm will create it with default options on startup.</p>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> display the help and exit</p>
<dt><code>-V, &#8211;version</code></p>
<dd> display FbTerm version and exit</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd> display extra FbTerm&#8217;s information</p>
<dt><code>-n, &#8211;font-names=</code><i>text</i></p>
<dd> specify font family names</p>
<dt><code>-s, &#8211;font-size=</code><i>num</i></p>
<dd> specify font pixel size</p>
<dt><code>&#8211;font-width=</code><i>num</i></p>
<dd> force font width</p>
<dt><code>-f, &#8211;color-foreground=</code><i>num</i></p>
<dd> specify foreground color</p>
<dt><code>-b, &#8211;color-background=</code><i>num</i></p>
<dd> specify background color</p>
<dt><code>-e, &#8211;text-encodings=</code><i>text</i></p>
<dd> specify additional text encodings</p>
<dt><code>-r, &#8211;screen-rotate=</code><i>num</i></p>
<dd> specify the orientation of screen display</p>
<dt><code>-i, &#8211;input-method=</code><i>text</i></p>
<dd> specify input method program</p>
<dt><code>&#8211;cursor-shape=</code><i>num</i></p>
<dd> specify default cursor shape</p>
<dt><code>&#8211;cursor-interval=</code><i>num</i></p>
<dd> specify cursor flash interval</p>
<dt><code>&#8211;vesa-mode=</code><i>num</i></p>
<dd> specify VESA video mode</p>
<dt><code>&#8211;vesa-mode=list</code></p>
<dd> display available VESA video modes </p>
<dt>see comments in <i>$HOME/.fbtermrc</i> for details of these options.</p>
<dd></dl>
<h2>SHORTCUT SUMMARY</h2>
<p> keyboard:<br />
&nbsp;<wbr>&nbsp;<wbr>CTRL_ALT_E:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>exit from FbTerm<br />
&nbsp;<wbr>&nbsp;<wbr>CTRL_ALT_C:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>create a new window<br />
&nbsp;<wbr>&nbsp;<wbr>CTRL_ALT_D:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>destroy current window<br />
&nbsp;<wbr>&nbsp;<wbr>CTRL_ALT_1:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>switch to window 1<br />
&nbsp;<wbr>&nbsp;<wbr>CTRL_ALT_2:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>switch to window 2<br />
&nbsp;<wbr>&nbsp;<wbr>CTRL_ALT_3:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>switch to window 3<br />
&nbsp;<wbr>&nbsp;<wbr>CTRL_ALT_4:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>switch to window 4<br />
&nbsp;<wbr>&nbsp;<wbr>CTRL_ALT_5:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>switch to window 5<br />
&nbsp;<wbr>&nbsp;<wbr>CTRL_ALT_6:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>switch to window 6<br />
&nbsp;<wbr>&nbsp;<wbr>CTRL_ALT_7:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>switch to window 7<br />
&nbsp;<wbr>&nbsp;<wbr>CTRL_ALT_8:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>switch to window 8<br />
&nbsp;<wbr>&nbsp;<wbr>CTRL_ALT_9:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>switch to window 9<br />
&nbsp;<wbr>&nbsp;<wbr>CTRL_ALT_0:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>switch to window 10<br />
&nbsp;<wbr>&nbsp;<wbr>SHIFT_LEFT:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>switch to previous window<br />
&nbsp;<wbr>&nbsp;<wbr>SHIFT_RIGHT:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>switch to next window<br />
&nbsp;<wbr>&nbsp;<wbr>SHIFT_PAGEUP:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>history scroll up<br />
&nbsp;<wbr>&nbsp;<wbr>SHIFT_PAGEDOWN:&nbsp;<wbr>&nbsp;<wbr>history scroll down<br />
&nbsp;<wbr>&nbsp;<wbr>CTRL_ALT_F1:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>switch to encoding of current locale<br />
&nbsp;<wbr>&nbsp;<wbr>CTRL_ALT_F2 to CTRL_ALT_F6:&nbsp;<wbr>&nbsp;<wbr>switch to additional encodings<br />
&nbsp;<wbr>&nbsp;<wbr>CTRL_SPACE:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>toggle input method </p>
<p> mouse:<br />
&nbsp;<wbr>&nbsp;<wbr>move when left button down:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>select text<br />
&nbsp;<wbr>&nbsp;<wbr>double click with left button:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>auto select text<br />
&nbsp;<wbr>&nbsp;<wbr>click with right button:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>paste selected text </p>
<p> Sometimes above actions will not work, please try to redo them with shift key holding down.</p>
<h2>FRAME BUFFER DEVICE</h2>
<p> Before executing FbTerm, make sure there is a frame buffer device in your system, and you have read/write access right with it. Normally FbTerm tries to open /dev/fb0 and /dev/fb/0, environment variable &quot;<i>FRAMEBUFFER</i>&quot; may be used to override this built-in behavior.</p>
<h2>VESA VIDEO DEVICE</h2>
<p> From version 1.6, FbTerm adds VESA video card support. By default, FbTerm tries frame buffer device first, if failure, then tries to use VESA device with highest resolution and color depth. option &quot;<i>vesa-mode</i>&quot; may be given to force only open VESA device with the specified video mode. To see available video modes for your VESA card, execute &quot;<code>fbterm &#8211;vesa-mode=list</code>&quot;. </p>
<p> Attention: 1) VESA support requires root privilege to work; 2) do not force to use VESA device on the system with frame buffer device enabled, they maybe conflict with each other.</p>
<h2>FONT</h2>
<p> FbTerm invokes fontconfig to get a font list, if the first font doesn&#8217;t contain the glyph for the rendering character, it will try second font, then the third, &#8230; and so on, user can see this ordered font list with &quot;<code>fbterm -v</code>&quot;. </p>
<p> If you don&#8217;t like the fonts selected by FbTerm, execute &quot;fc-list&quot; to get available fonts, choose favorites as the value of option &quot;<i>font-names</i>&quot;. You may also modify the configure file of fontconfig, which will change the behavior of all programs based on fontconfig!</p>
<h2>TEXT ENCODING</h2>
<p> By using iconv, FbTerm converts other encodings to internal encoding UTF-8. On startup, FbTerm checks variable <i>LC_CTYPE</i> to determine the default text encoding, which is binded to shortcut CTRL_ALT_F1. User can specify up to 5 additional encodings with option &quot;<i>text-encodings</i>&quot;, for example, as a Chinese user, you set &quot;text-encodings=gbk,big5&quot;, shortcut CTRL_ALT_F2 will bind to gbk, and CTRL_ALT_F3 bind to big5.</p>
<h2>BACKGROUND IMAGE</h2>
<p> FbTerm doesn&#8217;t load and parse any image file with various formats directly, instead it takes a screen shot of frame buffer device on startup if variable <i>FBTERM_BACKGROUND_IMAGE</i> is defined, then uses this screen shot as the background for text rendering. In order to enable background image support, user should first put a image to frame buffer device with a image viewer. A wrapper script using fbv is listed below: <code> </p>
<p>&nbsp;<wbr>#!/bin/bash </p>
<p>&nbsp;<wbr>#&nbsp;<wbr>fbterm-bi: a wrapper script to enable background image with fbterm<br />
&nbsp;<wbr>#&nbsp;<wbr>usage: fbterm-bi&nbsp;<wbr>/path/to/image fbterm-options </p>
<p>&nbsp;<wbr>echo -ne&nbsp;<wbr>&quot;[?25l&quot;&nbsp;<wbr>#&nbsp;<wbr>hide cursor </p>
<p>&nbsp;<wbr>fbv -ciuker&nbsp;<wbr>&quot;$1&quot;&nbsp;<wbr>&lt;&lt;&nbsp;<wbr>EOF<br />
&nbsp;<wbr>q<br />
&nbsp;<wbr>EOF </p>
<p>&nbsp;<wbr>shift<br />
&nbsp;<wbr>export FBTERM_BACKGROUND_IMAGE=1<br />
&nbsp;<wbr>exec fbterm&nbsp;<wbr>&quot;$@&quot; </code> Attention: 1) do not enable background image on frame buffer device with 8bpp depth, because FbTerm changes color map table for correct text rendering; 2) if the screen shot is different from the original image, try to use a fast scrolling disabled frame buffer device.</p>
<h2>INPUT METHOD</h2>
<p> Instead of adding input method directly in FbTerm, a client-server based input method framework is designed to do this work. FbTerm acts as a client, standalone IM program as a server, and they run in separated processes. </p>
<p> As a normal IM user, you should have a IM program written for FbTerm, and specify it as the value of option &quot;<i>input-method</i>&quot;. CTRL_SPACE is the shortcut to activate/deactivate input method. </p>
<h2>SECURITY NOTES</h2>
<p> FbTerm tries to change linux kernel key map table to setup shortcuts, which requires <i>SYS_TTY_CONFIG</i> capability from kernel version 2.6.15. It means FbTerm should be a setuid 0 program to allow non-root users to use shortcuts. FbTerm only switches to root privilege temporarily when changing key map table, we believe it&#8217;s pretty much free from security problems. </p>
<p> If you really don&#8217;t like this and not use VESA support, and have a linux kernel with file system capabilities enabled, which allow user to give binaries a subset of root&#8217;s powers without using setuid 0 (official kernel 2.6.27 includes it), you can run command &quot;<code>sudo setcap &#8216;cap_sys_tty_config+ep&#8217; /path/to/fbterm</code>&quot;.</p>
<h2>PERFORMANCE</h2>
<p> According test result, FbTerm spends more than 95% time on painting screen. Speedup painting will significantly increase performance. Here are some suggestions for frame buffer device: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>Enable fast scrolling on frame buffer device. The visible screen will be just a window of the video memory, when scrolling, FbTerm only change the start of window, no need to repaint the whole screen.<br />
&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>On Intel P6 family processors the Memory Type Range Registers&nbsp;<wbr>(MTRRs)&nbsp;<wbr>may be used to control processor access to memory ranges. If you have video card on a PCI or AGP bus, enabling write-combining allows bus write transfers to be combined into a larger transfer before bursting over the PCI/AGP bus. This can increase performance of FbTerm&#8217;s paint operations. </p>
<p> Maybe you need to enable them manually for your video card. For example, by default fast scrolling and write-combining are all disabled on general VESA frame buffer device, GRUB/LILO configure file should be modified to enable them. A GRUB example is showed below: </p>
<p> title Ubuntu<br />
&nbsp;<wbr>root&nbsp;<wbr>(hd0,0)<br />
&nbsp;<wbr>kernel&nbsp;<wbr>/boot/vmlinuz ro root=LABEL=UBUNTU splash vga=0x317&nbsp;<wbr><code>video=vesafb:ywrap,mtrr:3</code><br />
&nbsp;<wbr>initrd&nbsp;<wbr>/boot/initrd.img<br />
&nbsp;<wbr> You may check fast scrolling status with &quot;<code>fbterm -v</code>&quot;, a message with &quot;scrolling: redraw&quot; means fast scrolling is disabled, otherwise enabled.</p>
<h2>AUTHOR</h2>
<p> Written by dragchan.</p>
<h2>REPORTING BUGS</h2>
<p> Please submit bug reports to &lt;<code><a rel="nofollow" href="http://code.google.com/p/fbterm/issues">http://code.google.com/p/fbterm/issues</a></code>&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2008-2009 dragchan. License GPLv2: GNU GPL version 2 or later &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law. </p>
<h2>Index</h2>
