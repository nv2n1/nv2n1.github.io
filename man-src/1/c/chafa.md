---
title: "chafa(1)"
name: "chafa"
section: "1"
letter: "c"
url: "/docs/linux/man/1-chafa/"
description: "chafa – Character art facsimile generator"
---

<h2 class="name">NAME</h2>
<p> chafa &#8211; Character art facsimile generator </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>chafa</code> [OPTION&#8230;] [IMAGE&#8230;]</dl>
<h2>DESCRIPTION</h2>
<p> <code>chafa</code></p>
<dd>is a utility that converts all kinds of images, including animated GIFs, into (potentially animated) ANSI/Unicode character output that can be displayed in a terminal. It supports alpha transparency and multiple color modes and color spaces, and combines a range of Unicode characters for optimal output. </p>
<p> You can specify one or more input files, but the default behavior is slightly different with multiple files &#8212; for instance, animations will not loop forever when there is more than one input file.</p>
<h2>OPTIONS</h2>
<p> <code>&#8211;bg </code><i>color</i></p>
<dl>
<dt>
<dd> Background color of display (color name or hex). Partially transparent input will be blended with this color. Color names are based on those provided with X.Org. Defaults to black.</dl>
<p> <code>&#8211;clear</code></p>
<dl>
<dt>
<dd> Clear screen before processing each file.</dl>
<p> <code>-c </code><i>mode</i><code>, &#8211;colors </code><i>mode</i></p>
<dl>
<dt>
<dd> Set output color mode; one of [none, 2, 16, 240, 256, full]. Defaults to full (24-bit). The 240-color mode is recommended over the 256-color one, since the lower 16 colors are unreliable and tend to differ between terminals. 16-color mode will use aixterm extensions to produce 16 foreground and background colors. 2-color mode will only emit the ANSI codes for reverse color and attribute reset, while &quot;none&quot; will emit no ANSI color codes whatsoever.</dl>
<p> <code>&#8211;color-space </code><i>cs</i></p>
<dl>
<dt>
<dd> Color space used for quantization; one of [rgb, din99d]. Defaults to rgb, which is faster but less accurate.</dl>
<p> <code>&#8211;dither </code><i>type</i></p>
<dl>
<dt>
<dd> Type of dithering to apply during quantization. One of [none, ordered, diffusion]. &quot;Bayer&quot; is a synonym for &quot;ordered&quot;, and &quot;fs&quot; (Floyd-Steinberg) is a synonym for &quot;diffusion&quot;.</dl>
<p> <code>&#8211;dither-grain </code><i>width</i><code>x</code><i>height</i></p>
<dl>
<dt>
<dd> Dimensions of grain used when dithering. Specified as width x height, where each can be one of [1, 2, 4, 8] pixels. One character cell is by definition 8 pixels across in both dimensions. Defaults to 4&#215;4.</dl>
<p> <code>&#8211;dither-intensity </code><i>intensity</i></p>
<dl>
<dt>
<dd> Intensity of dithering pattern. Ranges from 0.0 to infinity, with 1.0 considered neutral. Lower values tend to reduce the amount of dithering done, while higher values increase it. In practice, values higher than 10.0 are unlikely to produce useful results.</dl>
<p> <code>-d, &#8211;duration </code><i>seconds</i></p>
<dl>
<dt>
<dd> Time to show each file. If showing a single file, defaults to zero for a still image and infinite for an animation. For multiple files, defaults to 3.0. Animations will always be played through at least once.</dl>
<p> <code>&#8211;fg </code><i>color</i></p>
<dl>
<dt>
<dd> Foreground color of display (color name or hex). Together with the background color specified by &#8211;bg, this specifies the terminal&#8217;s palette in color modes 2 and none. Color names are based on those provided with X.Org. Defaults to white.</dl>
<p> <code>&#8211;fill </code><i>symbols</i></p>
<dl>
<dt>
<dd> Specify character symbols to use for fill/gradients. Defaults to none. Usage is similar to that of &#8211;symbols; see below.</dl>
<p> <code>&#8211;font-ratio </code><i>width</i><code>/</code><i>height</i></p>
<dl>
<dt>
<dd> Target font&#8217;s width/height ratio. Can be specified as a real number or a fraction. Defaults to 1/2.</dl>
<p> <code>-h, &#8211;help</code></p>
<dl>
<dt>
<dd> Show a brief help text.</dl>
<p> <code>&#8211;invert</code></p>
<dl>
<dt>
<dd> Invert video. For display with bright backgrounds in color modes 2 and none. Swaps &#8211;fg and &#8211;bg.</dl>
<p> <code>-p </code><i>bool</i><code>, &#8211;preprocess </code><i>bool</i></p>
<dl>
<dt>
<dd> Image preprocessing [on, off]. Defaults to on with 16 colors or lower, off otherwise. This enhances colors and contrast prior to conversion, which can be useful in low-color modes.</dl>
<p> <code>-s </code><i>width</i><code>x</code><i>height</i><code>, &#8211;size </code><i>width</i><code>x</code><i>height</i></p>
<dl>
<dt>
<dd> Set maximum output dimensions in columns and rows. By default this will be the size of your terminal, or 80&#215;25 if size detection fails.</dl>
<p> <code>&#8211;stretch</code></p>
<dl>
<dt>
<dd> Stretch image to fit output dimensions; ignore aspect. Implies &#8211;zoom.</dl>
<p> <code>&#8211;symbols </code><i>symbols</i></p>
<dl>
<dt>
<dd> Specify character symbols to employ in final output. See below for full usage and a list of symbol classes.</dl>
<p> <code>-t </code><i>threshold</i><code>, &#8211;threshold </code><i>threshold</i></p>
<dl>
<dt>
<dd> Threshold above which full transparency will be used [0.0 &#8211; 1.0]. Setting this to 0.0 will render a blank image, while a value of 1.0 will replace any transparency with the background color (configurable with &#8211;bg).</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Show version, feature and copyright information.</dl>
<p> <code>&#8211;watch</code></p>
<dl>
<dt>
<dd> Watch a single input file, redisplaying it whenever its contents change. Will run until manually interrupted or, if &#8211;duration is set, until it expires.</dl>
<p> <code>-w </code><i>num</i><code>, &#8211;work </code><i>num</i></p>
<dl>
<dt>
<dd> How hard to work in terms of CPU and memory [1-9]. 1 is the cheapest, 9 is the most accurate. Defaults to 5.</dl>
<p> <code>&#8211;zoom</code></p>
<dl>
<dt>
<dd> Allow scaling up beyond one character per pixel.</dl>
<h2>SYMBOLS</h2>
<p> Accepted classes for &#8211;symbols are [all, none, space, solid, stipple, block, border, diagonal, dot, quad, half, hhalf, vhalf, inverted, braille, technical, geometric, ascii]. Some symbols belong to multiple classes, e.g. diagonals are also borders. </p>
<p> You can specify a list of classes separated by commas, or prefix them with + and &#8211; to add or remove symbols relative to the existing set. The ordering is significant. </p>
<p> The default symbol set is all-stipple-braille-ascii+space-extra-inverted for all modes except for &quot;none&quot;, which uses all-stipple-braille-ascii+space-extra.</p>
<h2>EXAMPLES</h2>
<p> chafa in.gif</p>
<dl>
<dt>
<dd> Show a potentially animated GIF image in the terminal. If this is an animation, it will run until the user generates an interrupt (typically ctrl-c). All parameters will be autodetected based on the current environment.</dl>
<p> chafa -c full -s 200 in.gif</p>
<dl>
<dt>
<dd> Like the above, but force truecolor output that is 200 characters wide and calculate the height preserving the aspect of the original image.</dl>
<p> chafa -c 16 &#8211;color-space din99d &#8211;symbols -dot in.jpg</p>
<dl>
<dt>
<dd> Generate 16-color output with perceptual color picking and avoid using dot symbols.</dl>
<p> chafa -c none &#8211;symbols block+border-solid in.png</p>
<dl>
<dt>
<dd> Generate uncolored output using block and border symbols, but avoid the solid block symbol.</dl>
<h2>AUTHOR</h2>
<p> Written by Hans Petter Jansson &lt;hpj [at] copyleft.no&gt;. </p>
<h2>Index</h2>
