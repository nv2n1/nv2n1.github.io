---
title: "gif2png(1)"
name: "gif2png"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gif2png/"
description: "gif2png – convert GIFs to PNGs"
---

<h2>NAME</h2>
<p> gif2png &#8211; convert GIFs to PNGs</p>
<h2>SYNOPSIS</h2>
<pre><code>
gif2png[-bdfghinprsvwO][file.[gif]...]
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>gif2png</code> program converts files in the obsolescent and patent-encumbered Graphic Interchange Format (GIF) to Portable Network Graphics (PNG) format, an open W3C standard. </p>
<p> Normally <code>gif2png</code> converts each file named on the command line, leaving the original in place. If a name does not have a .gif extension, the unmodified name will be tried first, followed by the name with .gif appended. For each file named `foo.gif&#8217;, a foo.png will be created. </p>
<p> When a multi-image GIF file named foo.gif is converted, gif2png creates multiple PNG files, each containing one frame; their names will be foo.png, foo.p01, foo.p02 etc. </p>
<p> If no source files are specified and stdin is a terminal, <code>gif2png</code> lists a usage summary and version information, then exits. </p>
<p> If no source files are specified, and stdin is a device or pipe, stdin is converted to noname.png. (The program can&#8217;t be a normal stdin-to-stdout filter because of the possibility that the input GIF might have multiple images). </p>
<p> However, if filter mode is forced (with -f) stdin will be converted to stdout, with <code>gif2png</code> returning an error code if the GIF is multi-image. </p>
<p> The program will preserve the information contained in a GIF file as closely as possible, including GIF comment and application-data extension blocks. All graphics data (pixels, RGB color tables) will be converted without loss of information. Transparency is also preserved. There is one exception; GIF plain-text extensions are skipped. </p>
<p> The program automatically converts interlaced GIFs to interlaced PNGs. It detects images in which all colors are gray (equal R, G, and B values) and converts such images to PNG grayscale. Other images are converted to use the PNG palette type. Duplicate color entries are silently preserved. Unused color-table entries cause an error message. </p>
<p> The action of the program can be modified with the following command-line switches: </p>
<dl>
<dt><code>-b</code> {#}RRGGBB</p>
<dd> Background. Replace transparent pixels with given RGB value, six hexadecimal digits interpreted as two hexits each of red, green, and blue value. The value may optionally be led with a #, HTML-style. </p>
<dt><code>-d </code></p>
<dd> Delete source GIF files after successful conversion. </p>
<dt><code>-f </code></p>
<dd> Filter mode. Convert GIF on stdin to PNG on stdout, return error if the GIF is multi-image. </p>
<dt><code>-g </code></p>
<dd> Write gamma=1/2.2 and sRGB chunks in the PNG. </p>
<dt><code>-h </code></p>
<dd> Generate PNG color-frequency histogram chunks into converted color files. </p>
<dt><code>-i </code></p>
<dd> Force conversion to interlaced PNG files. </p>
<dt><code>-n </code></p>
<dd> Force conversion to non-interlaced PNG files. </p>
<dt><code>-p </code></p>
<dd> Display progress of PNG writing. </p>
<dt><code>-r </code></p>
<dd> Try to recover data from corrupted GIF files. </p>
<dt><code>-s </code></p>
<dd> Do not translate the GIF Software chunk to a PNG annotation. </p>
<dt><code>-t </code></p>
<dd> Change behavior of web-probe (-w) mode to accept GIFs with transparency. </p>
<dt><code>-v </code></p>
<dd> Verbose mode; show summary line, -vv enables conversion-statistics and debugging messages. </p>
<dt><code>-w </code></p>
<dd> Web-probe switch; list GIFs that do not have multiple images or transparency to stdout. GIFs that fail this filter cause error messages to stderr. </p>
<dt><code>-O </code></p>
<dd> Optimize; remove unused color-table entries. Normally these trigger an error message and disable <code>-d</code> (but conversion is completed anyway). Also, use zlib compression level 9 (best compression) instead of the default level. The recovery algorithm enabled by <code>-r</code> is as follows: Unused color table entries will not trigger an error message as they normally do, but will still be preserved unless <code>-O</code> is also on, in which case they will be discarded. Missing color tables will be patched with a default that puts black at index 0, white at index 1, and supplies red, green, blue, yellow, purple and cyan as the remaining color values. Missing image pixels will be set to 0. Unrecognized or corrupted extensions will be discarded. </p>
</dl>
<h2>PROBLEMS</h2>
<p> Naively converting all your GIFs at one go with <code>gif2png</code> is not likely to give you the results you want. The problem is not with PNG itself or with gif2png, but with the poor-to-nonexistent support for PNG transparency and animation in most browsers. </p>
<p> The web-probe switch is intended to be used with scripts for converting web sites. All PNGs generated from the pathnames it returns will be properly rendered in Netscape Navigator 4.04+, Internet Explorer versions 4.0b1+, and all other current web browsers. Note: in future releases of gif2png, the meaning of this switch may change to reflect the capabilities of prevalent browsers. </p>
<h2>PATENT ISSUES</h2>
<p> The GIF format is encumbered by a Unisys patent (see &lt;<a rel="nofollow" href="http://www.delphion.com/details?">http://www.delphion.com/details?</a>&amp;pn10=US04464650&gt;) for the Lempel-Ziv-Welch compression algorithm. Use of any GIF image generator not licensed by Unisys can make you liable to lawsuit. Unisys apparently refuses to issue licenses for use of LZW in open-source programs, and in 1999 stated that its policy is to require a $5000 fee from websites that carry GIF images made by unlicensed software &#8212; even nonprofit websites created and displayed with free software. See &lt;<a href="http://corp2.unisys.com/LeadStory/lzw-license.html">http://corp2.unisys.com/LeadStory/lzw-license.html</a>&gt; for details. </p>
<p> The patent probably does not cover LZW decompressors such as the one gif2png uses; legal opinions are divided on this, there has been no court test, and Unisys refuses to commit itself. It is possible that you may be liable if you distribute <code>gif2png</code> in a commercial program, or distribute <code>gif2png</code> on a for-profit basis. </p>
<p> For a history of the GIF patent controversy, see &lt;<a rel="nofollow" href="http://lpf.ai.mit.edu/Patents/Gif/Gif.html">http://lpf.ai.mit.edu/Patents/Gif/Gif.html</a>&gt;. To avoid legal problems, it would be a good idea to convert all GIFs on your websites and elsewhere to PNGs without delay. See &lt;<a href="http://burnallgifs.org/">http://burnallgifs.org/</a>&gt; for discussion. </p>
<h2>STANDARDS AND SPECIFICATIONS</h2>
<p> Copies of the GIF89 specification are widely available on the Web; search for &quot;GRAPHICS INTERCHANGE FORMAT&quot;. The Graphics Interchange Format(c) is the Copyright property of CompuServe Incorporated. GIF(sm) is a Service Mark property of CompuServe Incorporated. </p>
<p> The PNG home site at &lt;<a rel="nofollow" href="http://www.libpng.org/pub/png/">http://www.libpng.org/pub/png/</a>&gt; has very complete information on the PNG standard, PNG libraries, and PNG tools. </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-web2png/">web2png</a>(1) </p>
<h2>AUTHORS</h2>
<p> Code by Alexander Lehmann &lt;alex [at] hal.rhein-main.de&gt;, 1995. Auto-interlace conversion and tRNS optimization by Greg Roelofs &lt;newt [at] pobox.com&gt;, 1999. Man page, -O, -w, and production packaging by Eric S. Raymond &lt;esr [at] thyrsus.com&gt;, 1999. </p>
<h2>Index</h2>
