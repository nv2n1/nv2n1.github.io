---

title: "xcfview(1)"
name: "xcfview"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xcfview/"
description: "xcfview – display GIMP xcf files"
---

<p> xcfview &#8211; display GIMP xcf files</p>
<h2>SYNOPSIS</h2>
<p> <code>xcfview</code> [ <i>options</i> ] <i>filename</i> [ <i>layer names</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>xcfview</code> is a wrapper script that uses <code><a href="/docs/linux/man/1-xcf2png/">xcf2png</a></code>(1) or <code><a href="/docs/linux/man/1-xcf2pnm/">xcf2pnm</a></code>(1) (q.v.) to flatten an XCF image and then displays the flattened image using a PNG or PPM viewer found using the <code><a href="/docs/linux/man/5-mailcap/">mailcap</a></code>(5) database.</p>
<h2>OPTIONS</h2>
<p> Every command-line parameter to <code>xcfview</code> will be passed through to the underlying <code>xcf2png</code> or <code>xcf2pnm</code> command. Because it is not certain which converter will be used, the options given should be ones that make sense for both of these:</p>
<dl>
<dt><code>&#8211;mask</code></dt>
<dd> Enable the layer mask.</dd>
<dt><code>&#8211;mode</code> <i>mode</i></dt>
<dd> Set the layer mode (e.g., <code>Normal</code> or <code>Multiply</code>).</dd>
<dt><code>&#8211;nomask</code></dt>
<dd> Disable the layer mask.</dd>
<dt><code>&#8211;opacity</code> <i>n</i></dt>
<dd> Set the opacity on a scale from 0 to 255 (as used internally)</dd>
<dt><code>&#8211;percent</code> <i>n</i></dt>
<dd> Set the opacity on a scale from 0 to 100 (as in the Gimp user interface).</dd>
<dt><code>-A</code>, <code>&#8211;force-alpha</code></dt>
<dd> Invent a trivial alpha channel even if the flattened image is completely opaque.</dd>
<dt><code>-b</code> <i>color</i>, <code>&#8211;background</code> <i>color</i></dt>
<dd> Use this color for transparent pixels in the image. The color can be given as <code>#rrggbb</code> or <code>#rgb</code> hexadecimal values, or as an X11 color name (which will only work if a color name database can be found in one of a number of standard locations).</dd>
<dt><code>-c</code>, <code>&#8211;color</code>, <code>&#8211;colour</code></dt>
<dd> Force the output to use RGB color space even if it there are more compact alternatives.</dd>
<dt><code>-C</code>, <code>&#8211;autocrop</code></dt>
<dd> Set the converted part of the image such that it just include the boundaries of the visible (or selected) layers. This may make it either smaller or larger than the canvas, depending on the position and size of the visible layers. (Note that the <i>contents</i> of the layers is not taken into account when autocropping).</dd>
<dt>
</dt><dd> In the absence of options that specify otherwise, the converted image will cover the entire XCF canvas.</dd>
<dt><code>-D</code>, <code>&#8211;dissolve</code></dt>
<dd> Do a &quot;dissolve&quot; step to eliminate partial transparency after flattening. If <code>-b</code> is also given, this happens before the background color is applied.</dd>
<dt><code>-f</code>, <code>&#8211;full-image</code></dt>
<dd> First flatten the entire image to a memory buffer before writing output. Then analyse the image to decide on the details of the output format (e.g., whether a grayscale output is sufficient). Without this option, the program flattens only a singe row of &quot;tiles&quot; (height 64) at a time.</dd>
<dt><code>-g</code>, <code>&#8211;gray</code>, <code>&#8211;grey</code></dt>
<dd> Force the output to be a grayscale image even if it may be monochrome. If any colored pixels are encountered, exit with status 103. This will be selected automatically if the output file&#8217;s name ends with <code>.pgm</code>.</dd>
<dt><code>-G</code>, <code>&#8211;for-gif</code></dt>
<dd> Assert that the flattened image will have no partial transparency (allowing a more compact representation of the alpha output). Exit with status 102 if the flattened image has any partial transparency. If <code>-b</code> is also given, this tests whether there there is partial transparency before applying the background color.</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> Print an option summery to standard output and exit with a return code of 0.</dd>
<dt><code>-j</code>, <code>&#8211;bzip</code></dt>
<dd> Equivalent to <code>-Z bzcat</code>. Default if the filename ends with <code>bz2</code>.</dd>
<dt><code>-o</code> <i>filename</i>, <code>&#8211;output</code> <i>filename</i></dt>
<dd> Write the converted picture to <i>filename</i> instead of to standard output.</dd>
<dt><code>-O</code> <i>x</i><code>,</code>y, <code>&#8211;offset</code> <i>x</i><code>,</code>y</dt>
<dd> Offset the converted part of the image from the top-left corner of the XCF canvas. Usually used with <code>-S</code>.</dd>
<dt><code>-S</code> <i>w</i><code>x</code>h, <code>&#8211;size</code> <i>w</i><code>x</code>h</dt>
<dd> Crop the converted image to width <i>w</i> and height <i>h</i>.</dd>
<dt><code>-T</code>, <code>&#8211;truecolor</code></dt>
<dd> Use standard RGB compositing for flattening indexed layers. Without this option, <code>xcfview</code> will mimic the Gimp&#8217;s current strategy of rounding each alpha value to either full transparency or full opacity, and interpret all layer modes as <code>Normal</code>.</dd>
<dt><code>-u</code>, <code>&#8211;utf8</code></dt>
<dd> Use the raw UTF-8 representation from the XCF file to compare and display layer names. Ordinarily, layer names will be converted to the character set of the current locale.</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> Print progress messages about the conversion to standard error.</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd> Print the version numer of <code>xcftools</code> to standard output and exit with a return code of 0.</dd>
<dt><code>-z</code>, <code>&#8211;gzip</code></dt>
<dd> Equivalent to <code>-Z zcat</code>. Default if the filename ends with <code>gz</code>.</dd>
<dt><code>-Z</code> <i>command</i>, <code>&#8211;unpack</code> <i>command</i></dt>
<dd> Specify a command that the input file is filtered through before being interpreted as an XCF file. The command is invoked as <i>command filename</i> and must produce output to its standard output. Note that it is not possible to specify arguments as part of <i>command</i>. An uncompressor is selected automatically if the filename ends with <code>gz</code> or <code>bz2</code>; to suppress this, use <code>-Z cat</code> (which is implemented without actually starting a <code><a href="/docs/linux/man/1-cat/">cat</a></code>(1) process).</dd></dl>
<h2>EXIT STATUS</h2>
<p> The exit status is 0 in case of success. A nonzero exit status may either be that of the <code>xcf2</code><i>foo</i> converter or that of the image viewer.</p>
<h2>AUTHOR</h2>
<p> <code>xcfview</code> was written by Henning Makholm &lt;henning [at] makholm.net&gt;. Parts of the script originate from the <code><a href="/docs/linux/man/1-run-mailcap/">run-mailcap</a></code>(1) script by Brian White &lt;bcwhite [at] pobox.com&gt;.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-xcf2pnm/">xcf2pnm</a></code>(1), <code><a href="/docs/linux/man/1-xcf2png/">xcf2png</a></code>(1) </p>
