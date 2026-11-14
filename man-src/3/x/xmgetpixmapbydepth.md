---
title: "xmgetpixmapbydepth(3)"
name: "xmgetpixmapbydepth"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmgetpixmapbydepth/"
description: "XmGetPixmapByDepth — A pixmap caching function that generates a pixmap, stores it in a pixmap cache, and returns the pixmap"
---

<p><code>XmGetPixmapByDepth</code> &#8212; A pixmap caching function that generates a pixmap, stores it in a pixmap cache, and returns the pixmap</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>Pixmap XmGetPixmapByDepth</code>(
<code>Screen *screen</code>,
<code>char *image_name</code>,
<code>Pixel foreground</code>,
<code>Pixel background</code>,
<code>int depth</code>);</pre>
<h2>Description</h2>
<p><code>XmGetPixmapByDepth</code> uses the parameter data to perform a lookup in the pixmap cache to see if a pixmap has already been generated that matches the data. If one is found, a reference count is incremented and the pixmap is returned. Applications should use <code>XmDestroyPixmap</code> when the pixmap is no longer needed.</p>
<dl COMPACT>
<dt><i>screen</i></p>
<dd>Specifies the display screen on which the pixmap is to be drawn</p>
<dt><i>image_name</i></p>
<dd>Specifies the name of the image to be used to generate the pixmap</p>
<dt><i>foreground</i></p>
<dd>Combines the image with the <i>foreground</i> color to create the pixmap if the image referenced is a bit-per-pixel image</p>
<dt><i>background</i></p>
<dd>Combines the image with the <i>background</i> color to create the pixmap if the image referenced is a bit-per-pixel image</p>
<dt><i>depth</i></p>
<dd>Specifies the depth of the pixmap</dl>
<p> If a matching pixmap is not found, <i>image_name</i> is used to perform a lookup in the image cache. If an image is found, it is used to generate the pixmap, which is then cached and returned. </p>
<p> If an image is not found, <i>image_name</i> is used as a filename, and a search is made for an <code>X10</code> or <code>X11</code> bitmap file. If it is found, the file is read, converted into an image, and cached in the image cache. The image is then used to generate a pixmap, which is cached and returned. </p>
<p> If <i>image_name</i> has a leading / (slash), it specifies a full pathname, and <code>XmGetPixmapByDepth</code> opens the file as specified. Otherwise, <i>image_name</i> specifies a filename. In this case, <code>XmGetPixmapByDepth</code> looks for the file along a search path specified by the <code>XBMLANGPATH</code> environment variable or by a default search path, which varies depending on whether or not the <code>XAPPLRESDIR</code> environment variable is set. The default search path contains a lot of directories. Therefore, <code>XmGetPixmapByDepth</code> will need a relatively long time to search through all these directories for pixmaps and bitmaps. Applications that use a lot of pixmaps and bitmaps will probably run more quickly if <code>XBMLANGPATH</code> is set to a short list of directories. In addition to X bitmap files (XBM), Motif also supports XPM (X Pixmap) file formats, and, from version 2.3, JPEG and PNG image formats. (Note that support of JPEG and PNG image format is an optional feature of Motif, in order to check if current version supports PNG ang JPEG image formats the PNG_SUPPORT and JPEG_SUPPORT macros should be checked correspondingly.) The <code>XBMLANGPATH</code> specifies the path for both XBM, XPM, PNG and JPEG files. XPM files are described in more detail later in this reference page. </p>
<p> The <code>XBMLANGPATH</code> environment variable specifies a search path for X bitmap files. It can contain the substitution field <code>%B</code>, where the <i>image_name</i> argument to <code>XmGetPixmapByDepth</code> is substituted for <code>%B</code>. It can also contain the substitution fields accepted by <code>XtResolvePathname</code>. The substitution field <code>%T</code> is always mapped to <i>bitmaps</i>, and <code>%S</code> is always mapped to NULL. </p>
<p> If <code>XBMLANGPATH</code> is not set, but the environment variable <code>XAPPLRESDIR</code> is set, the following pathnames are searched:</p>
<dl COMPACT>
<dt> &bull;</p>
<dd><code>%B</code></p>
<dt> &bull;</p>
<dd><code>$XAPPLRESDIR/%L/bitmaps/%N/%B</code></p>
<dt> &bull;</p>
<dd><code>$XAPPLRESDIR/%l_%t/bitmaps/%N/%B</code></p>
<dt> &bull;</p>
<dd><code>$XAPPLRESDIR/%l/bitmaps/%N/%B</code></p>
<dt> &bull;</p>
<dd><code>$XAPPLRESDIR/bitmaps/%N/%B</code></p>
<dt> &bull;</p>
<dd><code>$XAPPLRESDIR/%L/bitmaps/%B</code></p>
<dt> &bull;</p>
<dd><code>$XAPPLRESDIR/%l_%t/bitmaps/%B</code></p>
<dt> &bull;</p>
<dd><code>$XAPPLRESDIR/%l/bitmaps/%B</code></p>
<dt> &bull;</p>
<dd><code>$XAPPLRESDIR/bitmaps/%B</code></p>
<dt> &bull;</p>
<dd><code>$HOME/bitmaps/%B</code></p>
<dt> &bull;</p>
<dd><code>$HOME/%B</code></p>
<dt> &bull;</p>
<dd><code>/usr/lib/X11/%L/bitmaps/%N/%B</code></p>
<dt> &bull;</p>
<dd><code>/usr/lib/X11/%l_%t/bitmaps/%N/%B</code></p>
<dt> &bull;</p>
<dd><code>/usr/lib/X11/%l/bitmaps/%N/%B</code></p>
<dt> &bull;</p>
<dd><code>/usr/lib/X11/bitmaps/%N/%B</code></p>
<dt> &bull;</p>
<dd><code>/usr/lib/X11/%L/bitmaps/%B</code></p>
<dt> &bull;</p>
<dd><code>/usr/lib/X11/%l_%t/bitmaps/%B</code></p>
<dt> &bull;</p>
<dd><code>/usr/lib/X11/%l/bitmaps/%B</code></p>
<dt> &bull;</p>
<dd><code>/usr/lib/X11/bitmaps/%B</code></p>
<dt> &bull;</p>
<dd><code>/usr/include/X11/bitmaps/%B</code></dl>
<p> If neither <code>XBMLANGPATH</code> nor <code>XAPPLRESDIR</code> is set, the following pathnames are searched:</p>
<dl COMPACT>
<dt> &bull;</p>
<dd><code>%B</code></p>
<dt> &bull;</p>
<dd><code>$HOME/%L/bitmaps/%N/%B</code></p>
<dt> &bull;</p>
<dd><code>$HOME/%l_%t/bitmaps/%N/%B</code></p>
<dt> &bull;</p>
<dd><code>$HOME/%l/bitmaps/%N/%B</code></p>
<dt> &bull;</p>
<dd><code>$HOME/bitmaps/%N/%B</code></p>
<dt> &bull;</p>
<dd><code>$HOME/%L/bitmaps/%B</code></p>
<dt> &bull;</p>
<dd><code>$HOME/%l_%t/bitmaps/%B</code></p>
<dt> &bull;</p>
<dd><code>$HOME/%l/bitmaps/%B</code></p>
<dt> &bull;</p>
<dd><code>$HOME/bitmaps/%B</code></p>
<dt> &bull;</p>
<dd><code>$HOME/%B</code></p>
<dt> &bull;</p>
<dd><code>/usr/lib/X11/%L/bitmaps/%N/%B</code></p>
<dt> &bull;</p>
<dd><code>/usr/lib/X11/%l_%t/bitmaps/%N/%B</code></p>
<dt> &bull;</p>
<dd><code>/usr/lib/X11/%l/bitmaps/%N/%B</code></p>
<dt> &bull;</p>
<dd><code>/usr/lib/X11/bitmaps/%N/%B</code></p>
<dt> &bull;</p>
<dd><code>/usr/lib/X11/%L/bitmaps/%B</code></p>
<dt> &bull;</p>
<dd><code>/usr/lib/X11/%l_%t/bitmaps/%B</code></p>
<dt> &bull;</p>
<dd><code>/usr/lib/X11/%l/bitmaps/%B</code></p>
<dt> &bull;</p>
<dd><code>/usr/lib/X11/bitmaps/%B</code></p>
<dt> &bull;</p>
<dd><code>/usr/include/X11/bitmaps/%B</code></dl>
<p> These paths are defaults that vendors may change. For example, a vendor may use different directories for <code>/usr/lib/X11</code> and <code>/usr/include/X11</code>. </p>
<p> The following substitutions are used in these paths:</p>
<dl COMPACT>
<dt><code>%B</code></p>
<dd>The image name, from the <i>image_name</i> argument</p>
<dt><code>%N</code></p>
<dd>The class name of the application</p>
<dt><code>%L</code></p>
<dd>The display&#8217;s language string. This string is influenced by <code>XtSetLanguageProc</code>. The default string is determined by calling setlocale(<code>LC_ALL, NULL</code>).</p>
<dt><code>%l_%t</code></p>
<dd>The language and territory component of the display&#8217;s language string</p>
<dt><code>%l</code></p>
<dd>The language component of the display&#8217;s language string</dl>
<p> The contents of the file must conform to the rules for X11 bitmap files. In other words, Motif can read any X11 conformant bitmap file. </p>
<p> The XPM file format is used for storing or getting back colored X pixmaps from files. The XPM library is provided as unsupported with Motif. To build applications without XPM, use the <code>NO_XPM</code> macro. The following shows both XBM and XPM files, respectively, for a plaid pattern. </p>
<pre><tt>/* XBM file */
#define plaid_width 22
#define plaid_height 22
#define plaid_x_hot -1
#define plaid_y_hot -1
static char plaid_bits[] = {
 0x75, 0xfd, 0x3f, 0xaa, 0xfa, 0x3e, 0x75, 0xfd, 0x3f, 0xaa, 0xfa, 0x3e,
 0x75, 0xfd, 0x3f, 0xff, 0x57, 0x15, 0x75, 0xfd, 0x3f, 0xaa, 0xfa, 0x3e,
 0x75, 0xfd, 0x3f, 0xaa, 0xfa, 0x3e, 0x75, 0xfd, 0x3f, 0x20, 0xa8, 0x2b,
 0x20, 0x50, 0x15, 0x20, 0xa8, 0x2b, 0x20, 0x50, 0x15, 0x20, 0xa8, 0x2b,
 0xff, 0xff, 0x3f, 0x20, 0xa8, 0x2b, 0x20, 0x50, 0x15, 0x20, 0xa8, 0x2b,
 0x20, 0x50, 0x15, 0x20, 0xa8, 0x2b};</tt></pre>
<pre><tt>/* XPM file */
static char * plaid[] = {
/* plaid pixmap
 * width height ncolors chars_per_pixel */
&quot;22 22 4 2 &quot;,
/* colors */
&quot; c red m white s light_color &quot;,
&quot;Y c green m black s lines_in_mix &quot;,
&quot;+ c yellow m white s lines_in_dark &quot;,
&quot;x m black s dark_color &quot;,
/* pixels */
&quot;x x x x x x x x x x x x + x x x x x &quot;,
&quot; x x x x x x x x x x x x x x x x &quot;,
&quot;x x x x x x x x x x x x + x x x x x &quot;,
&quot; x x x x x x x x x x x x x x x x &quot;,
&quot;x x x x x x x x x x x x + x x x x x &quot;,
&quot;Y Y Y Y Y x Y Y Y Y Y + x + x + x + x + x + &quot;,
&quot;x x x x x x x x x x x x + x x x x x &quot;,
&quot; x x x x x x x x x x x x x x x x &quot;,
&quot;x x x x x x x x x x x x + x x x x x &quot;,
&quot; x x x x x x x x x x x x x x x x &quot;,
&quot;x x x x x x x x x x x x + x x x x x &quot;,
&quot; x x x x Y x x x &quot;,
&quot; x x x Y x x &quot;,
&quot; x x x x Y x x x &quot;,
&quot;x x x x x x x x x x x x x x x x x x x x x x &quot;,
&quot; x x x x Y x x x &quot;,
&quot; x x x Y x x &quot;,
&quot; x x x x Y x x x &quot;,
&quot; x x x Y x x &quot;,
&quot; x x x x Y x x x &quot;
};</tt></pre>
<h2>Return</h2>
<p>Returns a pixmap when successful; returns <code>XmUNSPECIFIED_PIXMAP</code> if the image corresponding to <i>image_name</i> cannot be found.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmdestroypixmap/">XmDestroyPixmap</a></code>(3), <code><a href="/docs/linux/man/3-xminstallimage/">XmInstallImage</a></code>(3), and <code><a href="/docs/linux/man/3-xmuninstallimage/">XmUninstallImage</a></code>(3).</p>
