---
title: "winicon(1)"
name: "winicon"
section: "1"
letter: "w"
url: "/docs/linux/man/1-winicon/"
description: "Microsoft Windows icon files"
---

<h2 class="name">NAME</h2>
<p> Microsoft Windows icon files</p>
<h2>DESCRIPTION</h2>
<p> A Microsoft Windows icon file contains one or more images, at resolutions up to 256 by 256 pixels and various bpp values. The images are encoded either as Portable Network Graphics file (PNG), or in a format similar to Microsoft&#8217;s BMP format. </p>
<p> If encoded as BMP, the image includes an &amp;lsquo;AND mask&amp;rsquo;, which contains 1-bit transparency data. It may also contain additional 8-bit transparency data together with the color information. </p>
<h3>Color Depth</h3>
<p> Except for the 16 bits per pixel images and images with bit fields, which both are rare, the colors in all BMP encoded images are RGB with 8 bits per channel. Images with bpp values lower than 16 use a palette. </p>
<p> I.e. the bpp value gives the number of distinct colors, not the color depth. </p>
<h3>XOR Mask and AND Mask</h3>
<p> BMP encoded images contain two pixel maps: The so-called &amp;lsquo;XOR mask&amp;rsquo; stores the color information for each pixel, and the &amp;lsquo;AND mask&amp;rsquo; stores the transparency belonging to it. </p>
<p> The names and the function of these maps are most easily understood by looking at how a 1-bpp icon image is rendered on a monochrome screen: The pixels on the screen are logically AND-ed with the bits on the AND mask, then the result is logically XOR-ed with the bits on the XOR mask. </p>
<p> The result is that if a bit on the AND mask is reset, the corresponding bit on the XOR mask determines the color of the pixel on the screen. If a bit in the AND mask is set and the corresponding bit in the XOR mask is black (reset), the image is transparent. Finally, if the bits are set in both the AND and XOR mask (the pixel on the XOR mask is white), the background of the screen is inverted. </p>
<p> In color environments, a pixel on the XOR mask outside the opaque area of the image is usually black and sometimes white, but a color other than black and white will hardly give predictable results. </p>
<p> Since Windows XP, there may also be an 8-bit alpha channel in 32-bpp BMP encoded icon images. The AND mask, however, is still required and used e.g. for generating shadows. </p>
<p> PNG encoded images don&#8217;t contain AND masks. While rendering a PNG encoded image, Windows constructs an AND mask on the fly from the alpha channel, if present. </p>
<h3>Evolution of Windows Icons</h3>
<p> The Windows icon file format has undergone some extensions since it was invented in the mid-eighties for Windows 1: </p>
<dl>
<dt>&bull;</p>
<dd> Windows 1 used monochrome 32&#215;32 icons only.</p>
<dt>&bull;</p>
<dd> Windows 3.0 added color icons with bpp values up to 8.</p>
<dt>&bull;</p>
<dd> Windows 4.0 (a.k.a. Windows95) added support for 32-bpp images and resolutions up to 256 by 256.</p>
<dt>&bull;</p>
<dd> NT 5.1 (a.k.a. Windows XP) added support for the 8-bit alpha channel in the unused bits of 32-bpp images.</p>
<dt>&bull;</p>
<dd> NT 6.0 (a.k.a. Windows Vista) added support for PNG encoded images </p>
</dl>
<h3>Common Resolutions and BPP Values</h3>
<p> Typical resolutions and bpp values of the Windows shell icons include: </p>
<p> &lt;TABLE summary=&quot;BPP values&quot; align=&quot;center&quot; border=1&gt; &lt;TR&gt;&lt;TH&gt;OS&lt;/TH&gt;&lt;TH&gt;resolutions&lt;/TH&gt;&lt;TH&gt;bpp values&lt;/TH&gt;&lt;/TR&gt; &lt;TR&gt;&lt;TD&gt;Windows 3&lt;/TD&gt;&lt;TD&gt;32&#215;32&lt;/TD&gt;&lt;TD&gt;1, 4&lt;BR&gt;&lt;/TD&gt;&lt;/TR&gt; &lt;TR&gt;&lt;TD&gt;Windows 4&lt;/TD&gt;&lt;TD&gt;16&#215;16, 32&#215;32, 48&#215;48&lt;/TD&gt;&lt;TD&gt;4, 8&lt;/TD&gt;&lt;/TR&gt; &lt;TR&gt;&lt;TD&gt;NT 5&lt;/TD&gt;&lt;TD&gt;16&#215;16, 32&#215;32, 48&#215;48&lt;/TD&gt;&lt;TD&gt;4, 8, 32&lt;/TD&gt;&lt;/TR&gt; &lt;TR&gt;&lt;TD rowspan=3&gt;NT 6&lt;/TD&gt;&lt;TD&gt;16&#215;16, 32&#215;32, 48&#215;48&lt;/TD&gt;&lt;TD&gt;4, 8, 32&lt;/TD&gt;&lt;/TR&gt; &lt;TR&gt;&lt;TD&gt;24&#215;24, 96&#215;96&lt;/TD&gt;&lt;TD&gt;8, 32&lt;BR&gt;&lt;/TD&gt;&lt;/TR&gt; &lt;TR&gt;&lt;TD&gt;256&#215;256&lt;/TD&gt;&lt;TD&gt;32 (PNG encoded)&lt;BR&gt;&lt;/TD&gt;&lt;/TR&gt; &lt;/TABLE&gt; </p>
<p> Within the icon file, the images with low bpp values are usually stored first. With the same bpp value, the images are sorted by resolution, large images first. </p>
<h3>MIME Type and File Name Extension</h3>
<p> The MIME type of Windows icon files is registered by IANA as <code>image/vnd.microsoft.icon</code>, but the unofficial name <code>image/x-icon</code> is still widely used. </p>
<p> The file name extension (used by Microsoft operating systems as file type identifier) is <code>.ico</code>. </p>
<h2>Index</h2>
