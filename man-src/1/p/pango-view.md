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
</dt><dd> pango-view [OPTION?] &#8211; FILE</dd></dl>
<h3>Help Options:</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> Show help options</dd>
<dt><code>&#8211;help-all</code></dt>
<dd> Show all help options</dd>
<dt><code>&#8211;help-cairo</code></dt>
<dd> Options understood by the cairo backend</dd></dl>
<h3>Cairo backend options:</h3>
<dl>
<dt><code>&#8211;annotate</code>=<i>,1/</i>, 2 or 3</dt>
<dd> Annotate the output</dd></dl>
<h3>Application Options:</h3>
<dl>
<dt><code>&#8211;no-auto-dir</code></dt>
<dd> No layout direction according to contents</dd>
<dt><code>&#8211;backend</code>=<i>,cairo/</i>/xft/ft2</dt>
<dd> Pango backend to use for rendering (default: cairo)</dd>
<dt><code>&#8211;background</code>=<i>,red/</i>/#rrggbb/#rrggbbaa/transparent</dt>
<dd> Set the background color</dd>
<dt><code>-q</code>, <code>&#8211;no-display</code></dt>
<dd> Do not display (just write to file or whatever)</dd>
<dt><code>&#8211;dpi</code>=<i>,number/</i></dt>
<dd> Set the resolution</dd>
<dt><code>&#8211;align</code>=<i>,left/</i>/center/right</dt>
<dd> Text alignment</dd>
<dt><code>&#8211;ellipsize</code>=<i>,start/</i>/middle/end</dt>
<dd> Ellipsization mode</dd>
<dt><code>&#8211;font</code>=<i>,description/</i></dt>
<dd> Set the font description</dd>
<dt><code>&#8211;foreground</code>=<i>,red/</i>/#rrggbb/#rrggbbaa</dt>
<dd> Set the text color</dd>
<dt><code>&#8211;gravity</code>=<i>,south/</i>/east/north/west/auto</dt>
<dd> Base gravity: glyph rotation</dd>
<dt><code>&#8211;gravity-hint</code>=<i>,natural/</i>/strong/line</dt>
<dd> Gravity hint</dd>
<dt><code>&#8211;header</code></dt>
<dd> Display the options in the output</dd>
<dt><code>&#8211;height=</code>+points/-numlines</dt>
<dd> Height in points (positive) or number of lines (negative) for ellipsizing</dd>
<dt><code>&#8211;hinting</code>=<i>,none/</i>/auto/slight/medium/full</dt>
<dd> Hinting style</dd>
<dt><code>&#8211;antialias</code>=<i>,none/</i>/gray/subpixel</dt>
<dd> Antialiasing</dd>
<dt><code>&#8211;hint-metrics</code>=<i>,on/</i>/off</dt>
<dd> Hint metrics</dd>
<dt><code>&#8211;subpixel-positions</code></dt>
<dd> Subpixel positioning</dd>
<dt><code>&#8211;subpixel-order</code>=<i>,rgb/</i>/bgr/vrgb/vbgr</dt>
<dd> Subpixel order</dd>
<dt><code>&#8211;indent</code>=<i>,points/</i></dt>
<dd> Width in points to indent paragraphs</dd>
<dt><code>&#8211;spacing</code>=<i>,points/</i></dt>
<dd> Spacing in points between lines</dd>
<dt><code>&#8211;line-spacing</code>=<i>,factor/</i></dt>
<dd> Spread factor for line height</dd>
<dt><code>&#8211;justify</code></dt>
<dd> Align paragraph lines to be justified</dd>
<dt><code>&#8211;language</code>=<i>,en_US/</i>/etc</dt>
<dd> Language to use for font selection</dd>
<dt><code>&#8211;margin</code>=<i>,CSS-style/</i> numbers in pixels</dt>
<dd> Set the margin on the output in pixels</dd>
<dt><code>&#8211;markup</code></dt>
<dd> Interpret text as Pango markup</dd>
<dt><code>-o</code>, <code>&#8211;output</code>=<i>,file/</i></dt>
<dd> Save rendered image to output file</dd>
<dt><code>&#8211;pixels</code></dt>
<dd> Use pixel units instead of points (sets dpi to 72)</dd>
<dt><code>&#8211;rtl</code></dt>
<dd> Set base direction to right-to-left</dd>
<dt><code>&#8211;rotate</code>=<i>,degrees/</i></dt>
<dd> Angle at which to rotate results</dd>
<dt><code>-n</code>, <code>&#8211;runs</code>=<i>,integer/</i></dt>
<dd> Run Pango layout engine this many times</dd>
<dt><code>&#8211;single-par</code></dt>
<dd> Enable single-paragraph mode</dd>
<dt><code>-t</code>, <code>&#8211;text</code>=<i>,string/</i></dt>
<dd> Text to display (instead of a file)</dd>
<dt><code>&#8211;version</code></dt>
<dd> Show version numbers</dd>
<dt><code>&#8211;waterfall</code></dt>
<dd> Create a waterfall display</dd>
<dt><code>-w</code>, <code>&#8211;width</code>=<i>,points/</i></dt>
<dd> Width in points to which to wrap lines or ellipsize</dd>
<dt><code>&#8211;wrap</code>=<i>,word/</i>/char/word-char</dt>
<dd> Text wrapping mode (needs a width to be set) </dd>
</dl>
<h2>Index</h2>
