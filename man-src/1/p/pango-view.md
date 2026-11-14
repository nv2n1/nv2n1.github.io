---
title: "pango-view(1)"
name: "pango-view"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pango-view/"
description: "pango-view (pango) – Pango text viewer"
---

<h2 class="name">NAME</h2>
<p> pango-view (pango) &#8211; Pango text viewer </p>
<h2>DESCRIPTION</h2>
<h3>Usage:</h3>
<dl>
<dt>
<dd> pango-view [OPTION?] &#8211; FILE</dl>
<h3>Help Options:</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Show help options</p>
<dt><code>&#8211;help-all</code></p>
<dd> Show all help options</p>
<dt><code>&#8211;help-cairo</code></p>
<dd> Options understood by the cairo backend</dl>
<h3>Cairo backend options:</h3>
<dl>
<dt><code>&#8211;annotate</code>=<i>,1/</i>, 2 or 3</p>
<dd> Annotate the output</dl>
<h3>Application Options:</h3>
<dl>
<dt><code>&#8211;no-auto-dir</code></p>
<dd> No layout direction according to contents</p>
<dt><code>&#8211;backend</code>=<i>,cairo/</i>/xft/ft2</p>
<dd> Pango backend to use for rendering (default: cairo)</p>
<dt><code>&#8211;background</code>=<i>,red/</i>/#rrggbb/#rrggbbaa/transparent</p>
<dd> Set the background color</p>
<dt><code>-q</code>, <code>&#8211;no-display</code></p>
<dd> Do not display (just write to file or whatever)</p>
<dt><code>&#8211;dpi</code>=<i>,number/</i></p>
<dd> Set the resolution</p>
<dt><code>&#8211;align</code>=<i>,left/</i>/center/right</p>
<dd> Text alignment</p>
<dt><code>&#8211;ellipsize</code>=<i>,start/</i>/middle/end</p>
<dd> Ellipsization mode</p>
<dt><code>&#8211;font</code>=<i>,description/</i></p>
<dd> Set the font description</p>
<dt><code>&#8211;foreground</code>=<i>,red/</i>/#rrggbb/#rrggbbaa</p>
<dd> Set the text color</p>
<dt><code>&#8211;gravity</code>=<i>,south/</i>/east/north/west/auto</p>
<dd> Base gravity: glyph rotation</p>
<dt><code>&#8211;gravity-hint</code>=<i>,natural/</i>/strong/line</p>
<dd> Gravity hint</p>
<dt><code>&#8211;header</code></p>
<dd> Display the options in the output</p>
<dt><code>&#8211;height=</code>+points/-numlines</p>
<dd> Height in points (positive) or number of lines (negative) for ellipsizing</p>
<dt><code>&#8211;hinting</code>=<i>,none/</i>/auto/slight/medium/full</p>
<dd> Hinting style</p>
<dt><code>&#8211;antialias</code>=<i>,none/</i>/gray/subpixel</p>
<dd> Antialiasing</p>
<dt><code>&#8211;hint-metrics</code>=<i>,on/</i>/off</p>
<dd> Hint metrics</p>
<dt><code>&#8211;subpixel-positions</code></p>
<dd> Subpixel positioning</p>
<dt><code>&#8211;subpixel-order</code>=<i>,rgb/</i>/bgr/vrgb/vbgr</p>
<dd> Subpixel order</p>
<dt><code>&#8211;indent</code>=<i>,points/</i></p>
<dd> Width in points to indent paragraphs</p>
<dt><code>&#8211;spacing</code>=<i>,points/</i></p>
<dd> Spacing in points between lines</p>
<dt><code>&#8211;line-spacing</code>=<i>,factor/</i></p>
<dd> Spread factor for line height</p>
<dt><code>&#8211;justify</code></p>
<dd> Align paragraph lines to be justified</p>
<dt><code>&#8211;language</code>=<i>,en_US/</i>/etc</p>
<dd> Language to use for font selection</p>
<dt><code>&#8211;margin</code>=<i>,CSS-style/</i> numbers in pixels</p>
<dd> Set the margin on the output in pixels</p>
<dt><code>&#8211;markup</code></p>
<dd> Interpret text as Pango markup</p>
<dt><code>-o</code>, <code>&#8211;output</code>=<i>,file/</i></p>
<dd> Save rendered image to output file</p>
<dt><code>&#8211;pixels</code></p>
<dd> Use pixel units instead of points (sets dpi to 72)</p>
<dt><code>&#8211;rtl</code></p>
<dd> Set base direction to right-to-left</p>
<dt><code>&#8211;rotate</code>=<i>,degrees/</i></p>
<dd> Angle at which to rotate results</p>
<dt><code>-n</code>, <code>&#8211;runs</code>=<i>,integer/</i></p>
<dd> Run Pango layout engine this many times</p>
<dt><code>&#8211;single-par</code></p>
<dd> Enable single-paragraph mode</p>
<dt><code>-t</code>, <code>&#8211;text</code>=<i>,string/</i></p>
<dd> Text to display (instead of a file)</p>
<dt><code>&#8211;version</code></p>
<dd> Show version numbers</p>
<dt><code>&#8211;waterfall</code></p>
<dd> Create a waterfall display</p>
<dt><code>-w</code>, <code>&#8211;width</code>=<i>,points/</i></p>
<dd> Width in points to which to wrap lines or ellipsize</p>
<dt><code>&#8211;wrap</code>=<i>,word/</i>/char/word-char</p>
<dd> Text wrapping mode (needs a width to be set) </p>
</dl>
<h2>Index</h2>
