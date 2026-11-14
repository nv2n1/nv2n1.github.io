---
title: "pamx(1)"
name: "pamx"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pamx/"
description: "pamx – display Netpbm image in X Window System window"
---

<h2 class="name">NAME</h2>
<p> pamx &#8211; display Netpbm image in X Window System window</p>
<h2>SYNOPSIS</h2>
<p> <code>pamx</code> </p>
<p> [<code>-fullscreen</code>] [<code>-install</code>] [<code>-private</code>] [<code>-fit</code>] [<code>-pixmap</code>] [<code>-verbose</code>] [<code>-display=</code><i>x-display</i>] [<code>-title=</code><i>text</i>] [<code>-foreground=</code><i>color</i>] [<code>-background=</code><i>color</i>] [<code>-border=</code><i>color</i>] [<code>-geometry=</code><i>x-geometry-string</i>] [<code>-visual=</code><i>name</i>] <i>netpbm_file</i> </p>
<p> All options can be abbreviated to their shortest unique prefix. You may use two hyphens instead of one to designate an option. You may use either white space or an equals sign between an option name and its value. </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pamx</code> displays a Netpbm image in an X Window System window. It is like a very simple version of the classic X image viewer <code>xloadimage</code>. </p>
<p> If you don&#8217;t specify the input file <i>netpbm_file</i>, the input is from Standard Input. The input image can be any Netpbm image format. If the input is a multi-image stream, <code>pamx</code> ignores all but the first image. </p>
<p> <code>pamx</code> is not the best choice for general purpose viewing of images, because it is a traditional simple Netpbm building block. It is a good thing to build into other programs and can be useful for debugging more complex systems, but you can get much more powerful viewers that can display Netpbm images. For example, <code>xloadimage</code>, <code>xli</code>, <code>xzgv</code>, and any web browser. </p>
<p> The program <code>xwud</code> (X Window Undump) is part of the X Window System and performs the same basic display function, though with input in the special X Window Dump format (for which Netpbm has converters). </p>
<p> The initial window is at most 90% of the size of the display unless the window manager does not correctly handle window size requests or if you&#8217;ve used the <code>-fullscreen</code> option. You may move the image around in the window by dragging with the first mouse button. The cursor will indicate which directions you may drag, if any. You may exit the window by typing &#8216;q&#8217; or control-C when the keyboard focus is on the window. </p>
<p> <code>ppmsvgalib</code> is a similar program that displays an image on a Linux system without the need for the X Window System. </p>
<h2>X RESOURCE CLASS</h2>
<p> <code>pamx</code> uses the resource class name <code>Xloadimage</code> for window managers which need this resource set. This is, of course, the same resource class that the conventional viewer program <code>xloadimage</code> uses. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-border=</code><i>color</i></p>
<dd> This sets the background portion of the window which is not covered by any images to be <i>color</i>. </p>
<dt><code>-display=</code><i>display_name</i></p>
<dd> This names the X display in which to put the window. E.g. <code>0:0</code>. </p>
<dt><code>-fit</code></p>
<dd> Force image to use the default visual and colormap. This is useful if you do not want technicolor effects when the colormap focus is inside the image window, but it may reduce the quality of the displayed image. </p>
<dt><code>-fullscreen</code></p>
<dd> Use the entire screen to display the image. </p>
<dt><code>-geometry=</code><i>W</i><code>x</code><i>H</i>[{<code>+</code>,<code>&#8211;</code>}<i>X</i>{<code>+</code>,<code>&#8211;</code>}<i>Y</i></p>
<dd> This sets the size and position of the window in which <code>pamx</code> displays the image. </p>
<p> By default, the window size exactly matches the image size, except that if you don&#8217;t specify <code>-fullscreen</code>, the maximum is 90% of the screen dimensions. </p>
<dt><code>-install</code></p>
<dd> Forcibly install the image&#8217;s colormap when the window is focused. This violates ICCCM standards and only exists to allow operation with naive window managers. Use this option only if your window manager does not install colormaps properly. </p>
<dt><code>-pixmap</code></p>
<dd> Force the use of a pixmap as backing-store. This is provided for servers where backing-store is broken (such as some versions of the AIXWindows server). It may improve scrolling performance on servers which provide backing-store. </p>
<dt><code>-private</code></p>
<dd> Force <code>pamx</code> to use of a private colormap. By default, <code>pamx</code> allocates colors shared unless there are not enough colors available. </p>
<dt><code>-verbose</code></p>
<dd> Causes <code>pamx</code> to print various information about what it&#8217;s doing to Standard Error. </p>
<dt><code>-visual=</code><i>visual_name</i></p>
<dd> Force the use of a specific visual type to display an image. By default, <code>pamx</code> tries to pick the best available image for a particular image type. The available visual types are: <code>DirectColor</code>, <code>TrueColor</code>, <code>PseudoColor</code>, <code>StaticColor</code>, <code>GrayScale</code>, and <code>StaticGray</code>. You may use the shortest unique prefix of these names, and case is not significant. </p>
<dt><code>-background=</code><i>color</i></p>
<dd> Use <i>color</i> as the background color instead of the default (usually white but this depends on the image type) if you are transferring a monochrome image to a color display. </p>
<dt><code>-foreground=</code><i>color</i></p>
<dd> Use <i>color</i> as the foreground color instead of black if you are transferring a monochrome image to a color display. You can also use this to invert the foreground and background colors of a monochrome image. </p>
<dt><code>-title=</code><i>text</i></p>
<dd> Set the title bar title of the window. Default is the file name of the input file, or &#8216;stdin&#8217; if the image is from Standard Input. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ppmsvgalib/">ppmsvgalib</a></code>(1) , <code><a href="/docs/linux/man/1-pam/">pam</a></code>(1) , <code><a href="/docs/linux/man/1-pnm/">pnm</a></code>(1) , <code>xzgv</code>, <code>xwud</code>, <code>xloadimage</code>, <code>xli</code> </p>
<h2>AUTHOR</h2>
<p> <code>pamx</code> is by Bryan Henderson, in March 2006, based on <code>xloadimage</code> by Jim Frost, Centerline Software, jimf [at] centerline.com, 1989-1993. </p>
<p> Jim&#8217;s code contained the following copyright notice and license: </p>
<dl>
<dt>
<dd>
<p> Copyright 1989, 1993 Jim Frost </p>
<p> Permission to use, copy, modify, distribute, and sell this software and its documentation for any purpose is hereby granted without fee, provided that the above copyright notice appear in all copies and that both that copyright notice and this permission notice appear in supporting documentation. The author makes no representations about the suitability of this software for any purpose. It is provided &quot;as is&quot; without express or implied warranty. </p>
<p> THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS, IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE. </p>
</dl>
<p> Lots of other people contributed to Xloadimage, and they are listed in the file COPYRIGHT in the source code. </p>
<h2>HISTORY</h2>
<p> <code>pamx</code> was new in Netpbm 10.34 (May 2006). </p>
<p> <code>pamx</code> is essentially based on the classic X displayer program <code>xloadimage</code> by Jim Frost, 1989. Bryan Henderson stripped it down and adapted it to Netpbm in March 2006. </p>
<p> The following features of <code>xloadimage</code> are left out of <code>pamx</code>, to be more compatible with Netpbm&#8217;s philosophy of simple building blocks. Note that there are other programs in Netpbm that do most of these things: </p>
<dl>
<dt>&bull;</p>
<dd> zoom in/out</p>
<dt>&bull;</p>
<dd> ability to accept formats other than Netpbm</p>
<dt>&bull;</p>
<dd> image transformations (brightening, clipping, rotating, etc)</p>
<dt>&bull;</p>
<dd> decompressing and other decoding of input</p>
<dt>&bull;</p>
<dd> ability to display on the root window</p>
<dt>&bull;</p>
<dd> slide show </p>
<p> <code>pamx</code> also differs from <code>xloadimage</code> in that it uses Libnetpbm.</dl>
<p> There is virtually no code from <code>xloadimage</code> actually in <code>pamx</code>, because Bryan rewrote it all to make it easier to understand. </p>
<h2>Index</h2>
