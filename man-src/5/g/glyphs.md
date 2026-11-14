---
title: "glyphs(5)"
name: "glyphs"
section: "5"
letter: "g"
url: "/docs/linux/man/5-glyphs/"
description: "glyphs – format of .glyphs files"
---

<p>glyphs &#8211; format of .glyphs files</p>
<h2>Description</h2>
<p>Glyph files (&#8220;.glyph&#8221; extension) are used to store commonly-used bit patterns (glyphs) for Magic. Right now, the bit patterns are used for two purposes in Magic. First, they specify patterns for programmable cursors: each cursor shape (e.g. the arrow used for the wiring tool) is read in as a glyph from a glyph file. Second, glyphs are used by the window manager to represent the icons displayed at the ends of scroll bars. Glyph file names normally have the extension <code>.glyph</code>. Glyph files are stored in ASCII format. Lines beginning with &#8220;#&#8221; are considered to be comments and are ignored. Blank lines are also ignored. The first non-comment line in a glyph file must have the syntax <code>size </code><i>nGlyphs width height</i> The <i>nGlyphs</i> field must be a number giving the total number of glyphs stored in the file. The <i>width</i> and <i>height</i> fields give the dimensions of each glyph in pixels. All glyphs in the same file must have the same size. The <code>size</code> line is followed by a description for each of the glyphs. Each glyph consists of <i>height</i> lines each containing 2&#215;<i>width</i> characters. Each pair of characters corresponds to a bit position in the glyph, with the leftmost pair on the topmost line corresponding to the upper-left pixel in the glyph. The first character of each pair specifies the color to appear in that pixel. The color is represented as as a single character, which must be the short name of a display style in the current display style file. Some commonly-used characters are <code>K</code> for black, <code>W</code> for white, and <code>.</code> for the background color (when <code>.</code> is used in a cursor, it means that that pixel position is transparent: the underlying picture appears through the cursor). See &#8220;Magic Maintainer&#8217;s Manual #3: Display Styles, Color Maps, and Glyphs&#8221; for more information. The second character of each pair is normally blank, except for one pixel per glyph which may contain a &#8220;*&#8221; in the second character. The &#8220;*&#8221; is used for programmable cursors to indicate the hot-spot: the pixel corresponding to the &#8220;*&#8221; is the one that the cursor is considered to point to. For an example of a glyph file, see ~cad/lib/magic/sys/color.glyphs. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-magic/">magic</a>(1), <a href="/docs/linux/man/5-dstyle/">dstyle</a>(5) </p>
