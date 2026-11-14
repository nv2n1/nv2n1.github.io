---
title: "xminstallimage(3)"
name: "xminstallimage"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xminstallimage/"
description: "XmInstallImage — A pixmap caching function that adds an image to the image cache"
---

<p><code>XmInstallImage</code> &#8212; A pixmap caching function that adds an image to the image cache</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>Boolean XmInstallImage</code>(
<code>XImage * image</code>,
<code>char * image_name</code>);</pre>
<h2>Description</h2>
<p><code>XmInstallImage</code> stores an image in an image cache that can later be used to generate a pixmap. Part of the installation process is to extend the resource converter used to reference these images. The resource converter is given the image name so that the image can be referenced in a <code>.Xdefaults</code> file. Since an image can be referenced by a widget through its pixmap resources, it is up to the application to ensure that the image is installed before the widget is created.</p>
<dl COMPACT>
<dt><i>image</i></p>
<dd>Points to the image structure to be installed. The installation process does not make a local copy of the image. Therefore, the application should not destroy the image until it is uninstalled from the caching functions.</p>
<dt><i>image_name</i></p>
<dd>Specifies a string that the application uses to name the image. After installation, this name can be used in <code>.Xdefaults</code> for referencing the image. A local copy of the name is created by the image caching functions.</dl>
<p> The image caching functions provide a set of eight preinstalled images. These names can be used within a <code>.Xdefaults</code> file for generating pixmaps for the resource for which they are provided. </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td><code>Image Name</code></td>
<td><code>Description</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>background</td>
<td>A tile of solid background
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>25_foreground</td>
<td> A tile of 25% foreground, 75% background
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>50_foreground</td>
<td> A tile of 50% foreground, 50% background
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>75_foreground</td>
<td> A tile of 75% foreground, 25% background
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>horizontal</td>
<td> A tile of horizontal lines of the two colors
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>vertical</td>
<td> A tile of vertical lines of the two colors
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>slant_right</td>
<td> A tile of slanting lines of the two colors
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>slant_left</td>
<td> A tile of slanting lines of the two colors
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>menu_cascade</td>
<td> A tile of an arrow of the foreground color
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>menu_checkmark</td>
<td> A tile of a checkmark of the foreground color
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>menu_dash</td>
<td> A tile of one horizontal line of the foreground color
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
</table>
</table>
<h2>Return</h2>
<p>Returns True when successful; returns False if NULL <i>image</i>, NULL <i>image_name</i>, or duplicate <i>image_name</i> is used as a parameter value.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmuninstallimage/">XmUninstallImage</a></code>(3), <code><a href="/docs/linux/man/3-xmgetpixmap/">XmGetPixmap</a></code>(3), and <code><a href="/docs/linux/man/3-xmdestroypixmap/">XmDestroyPixmap</a></code>(3).</p>
