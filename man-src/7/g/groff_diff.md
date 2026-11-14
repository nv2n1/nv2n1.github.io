---
title: "groff_diff(7)"
name: "groff_diff"
section: "7"
letter: "g"
url: "/docs/linux/man/7-groff_diff/"
description: "groff_diff – differences between GNU troff and classical troff"
---

<p>groff_diff &#8211; differences between GNU troff and classical troff</p>
<h2>Description</h2>
<p>This manual page describes the language differences between <i>groff</i>, the GNU <i>roff</i> text processing system, and the classical <i>roff</i> formatter of the freely available Unix~7 of the 1970s, documented in the <i>Troff User&#8217;s Manual</i> by <i>Ossanna</i> and <i>Kernighan</i>. This includes the roff language as well as the intermediate output format (troff output). </p>
<p> Section &#8220;See Also&#8221; below gives pointers to both the classical <i>roff</i> and the modern <i>groff</i> documentation.</p>
<h2>Groff Language</h2>
<p>In this section, all additional features of <i>groff</i> compared to the classical Unix~7 <i>troff</i> are described in detail.</p>
<h3>Long names</h3>
<p>The names of number registers, fonts, strings/:macros/:diversions, special characters (glyphs), and colors can be of any length. In escape sequences, additionally to the classical &#8216;<code>(</code>,<i>xx/</i>&#8216; construction for a two-character glyph name, you can use &#8216;<code>[</code>,<i>xxx/</i><code>]</code>&#8216; for a name of arbitrary length.</p>
<dl>
<dt><code>\[</code><i>xxx</i><code>]</code></p>
<dd>Print the special character (glyph) called <i>xxx</i>.</p>
<dt><code>\[</code><i>comp1 comp2 </i><code>]</code></p>
<dd>Print composite glyph consisting of multiple components. Example: &#8216;\[A~ho]&#8217; is capital letter A with ogonek which finally maps to glyph name &#8216;u0041_0328&#8217;. See <i>Groff: The GNU Implementation of troff</i>, the <i>groff</i> Texinfo manual, for details of how a glyph name for a composite glyph is constructed, and <code><a href="/docs/linux/man/7-groff_char/">groff_char</a></code>(7) for a list of glyph name components used in composite glyph names.</p>
<dt><code>[</code><i>xxx</i><code>]</code></p>
<dd>Set font <i>xxx</i>. Additionally, <code>[]</code> is a new syntax form equal to <code>P</code>, i.e., to return to the previous font.</p>
<dt><code>\*[</code><i>xxx arg1 arg2 </i><code>]</code></p>
<dd>Interpolate string <i>xxx</i>, taking <i>arg1</i>, <i>arg2</i>, <i></i>, as arguments.</p>
<dt><code>
[</code><i>xxx</i><code>]</code></p>
<dd>Interpolate number register <i>xxx</i>.</dl>
<h3>Fractional point sizes</h3>
<p>A <i>scaled point</i> is equal to <code>1/sizescale</code> points, where <code>sizescale</code> is specified in the <i>DESC</i> file (1 by default). There is a new scale indicator~<code>z</code> that has the effect of multiplying by sizescale. Requests and escape sequences in troff interpret arguments that represent a point size as being in units of scaled points, but they evaluate each such argument using a default scale indicator of~<code>z</code>. Arguments treated in this way are the argument to the <code>ps</code> request, the third argument to the <code>cs</code> request, the second and fourth arguments to the <code>tkf</code> request, the argument to the <code>\H</code> escape sequence, and those variants of the <code>\s</code> escape sequence that take a numeric expression as their argument. </p>
<p> For example, suppose sizescale is 1000; then a scaled point is equivalent to a millipoint; the call <code>.ps 10.25</code> is equivalent to <code>.ps 10.25z</code> and so sets the point size to 10250 scaled points, which is equal to 10.25 points. </p>
<p> The number register <code>
[.s]</code> returns the point size in points as decimal fraction. There is also a new number register <code>
[.ps]</code> that returns the point size in scaled points. </p>
<p> It would make no sense to use the <code>z</code>~scale indicator in a numeric expression whose default scale indicator was neither <code>u</code> nor~<code>z</code>, and so <code>troff</code> disallows this. Similarly it would make no sense to use a scaling indicator other than <code>z</code> or~<code>u</code> in a numeric expression whose default scale indicator was~<code>z</code>, and so <code>troff</code> disallows this as well. </p>
<p> There is also new scale indicator~<code>s</code> which multiplies by the number of units in a scaled point. So, for example, <code>
[.ps]s</code> is equal to <code>1m</code>. Be sure not to confuse the <code>s</code> and <code>z</code>~scale indicators.</p>
<h3>Numeric expressions</h3>
<p>Spaces are permitted in a number expression within parentheses. </p>
<p> <code>M</code> indicates a scale of 100ths of an em. <code>f</code> indicates a scale of 65536 units, providing fractions for color definitions with the <code>defcolor</code> request. For example, 0.5f = 32768u.</p>
<dl>
<dt><i>e1</i><code>&gt;?</code><i>e2</i></p>
<dd>The maximum of <i>e1</i> and <i>e2</i>.</p>
<dt><i>e1</i><code>&lt;?</code><i>e2</i></p>
<dd>The minimum of <i>e1</i> and <i>e2</i>.</p>
<dt><code>(</code><i>c</i><code>;</code><i>e</i><code>)</code></p>
<dd>Evaluate <i>e</i> using <i>c</i> as the default scaling indicator. If <i>c</i> is missing, ignore scaling indicators in the evaluation of~<i>e</i>.</dl>
<h3>New escape sequences</h3>
<dl>
<dt><code>\A&#8217;</code><i>anything</i><code>&#8216;</code></p>
<dd>This expands to <code>1</code> or~<code>0</code>, depending on whether <i>anything</i> is or is not acceptable as the name of a string, macro, diversion, number register, environment, font, or color. It returns~<code>0</code> if <i>anything</i> is empty. This is useful if you want to look up user input in some sort of associative table.</p>
<dt><code>\B&#8217;</code><i>anything</i><code>&#8216;</code></p>
<dd>This expands to <code>1</code> or~<code>0</code>, depending on whether <i>anything</i> is or is not a valid numeric expression. It returns~<code>0</code> if <i>anything</i> is empty.</p>
<dt><code>\C&#8217;</code><i>xxx</i><code>&#8216;</code></p>
<dd>Typeset glyph named <i>xxx</i>. Normally it is more convenient to use <code>\[</code><i>xxx</i><code>]</code>. But <code>\C</code> has the advantage that it is compatible with recent versions of Unix and is available in compatibility mode.</p>
<dt><code>\E</code></p>
<dd>This is equivalent to an escape character, but it is not interpreted in copy mode. For example, strings to start and end superscripting could be defined like this</p>
<dl>
<dd>
<dl>
<dd>.ds { &#8217;-.3m&#8217;\s&#8217;\En[.s]*6u/10u&#8217; .ds } \s0&#8217;.3m&#8217;</dl>
</dl>
<dd>The use of <code>\E</code> ensures that these definitions work even if <code>\*{</code> gets interpreted in copy mode (for example, by being used in a macro argument).</p>
<dt><code>\F</code><i>f</i></p>
<dd><code>\F(</code><i>fm</i> <code>\F[</code><i>fam</i><code>]</code> Change font family. This is the same as the <code>fam</code> request. <code>\F[]</code> switches back to the previous font family (note that <code>\FP</code> won&#8217;t work; it selects font family &#8216;P&#8217; instead).</p>
<dt><code>\m</code><i>x</i></p>
<dd><code>\m(</code><i>xx</i> <code>\m[</code><i>xxx</i><code>]</code> Set drawing color. <code>\m[]</code> switches back to the previous color.</p>
<dt><code>\M</code><i>x</i></p>
<dd><code>\M(</code><i>xx</i> <code>\M[</code><i>xxx</i><code>]</code> Set background color for filled objects drawn with the <code>\D&#8217;</code><i></i><code>&#8216;</code> commands. <code>\M[]</code> switches back to the previous color.</p>
<dt><code>\N&#8217;</code><i>n</i><code>&#8216;</code></p>
<dd>Typeset the glyph with index~<i>n</i> in the current font. <i>n</i>~can be any integer. Most devices only have glyphs with indices between 0 and 255. If the current font does not contain a glyph with that code, special fonts are <i>not</i> searched. The <code>\N</code> escape sequence can be conveniently used in conjunction with the <code>char</code> request, for example</p>
<dl>
<dd>
<dl>
<dd>.char \[phone] (ZD\N&#8217;37&#8217;</dl>
</dl>
<dd>The index of each glyph is given in the fourth column in the font description file after the <code>charset</code> command. It is possible to include unnamed glyphs in the font description file by using a name of <code>&#8212;</code>; the <code>\N</code> escape sequence is the only way to use these.</p>
<dt><code>\O</code><i>n</i></p>
<dd><code>\O[</code><i>n</i><code>]</code> Suppress troff output. The escapes <code>\O2</code>, <code>\O3</code>, <code>\O4</code>, and <code>\O5</code> are intended for internal use by <code>grohtml</code>.</p>
<dl>
<dd>
<dl>
<dt><code>\O0</code></p>
<dd>Disable any ditroff glyphs from being emitted to the device driver, provided that the escape occurs at the outer level (see <code>\O3</code> and <code>\O4</code>).</p>
<dt><code>\O1</code></p>
<dd>Enable output of glyphs, provided that the escape occurs at the outer level.</p>
<dd><code>\O0</code> and <code>\O1</code> also reset the registers <code>
[opminx]</code>, <code>
[opminy]</code>, <code>
[opmaxx]</code>, and <code>
[opmaxy]</code> to~-1. These four registers mark the top left and bottom right hand corners of a box which encompasses all written glyphs.</p>
<dt><code>\O2</code></p>
<dd>Provided that the escape occurs at the outer level, enable output of glyphs and also write out to stderr the page number and four registers encompassing the glyphs previously written since the last call to <code>\O</code>.</p>
<dt><code>\O3</code></p>
<dd>Begin a nesting level. At start-up, <code>troff</code> is at outer level. This is really an internal mechanism for <code>grohtml</code> while producing images. They are generated by running the troff source through <code>troff</code> to the PostScript device and <code>ghostscript</code> to produce images in PNG format. The <code>\O3</code> escape starts a new page if the device is not html (to reduce the possibility of images crossing a page boundary).</p>
<dt><code>\O4</code></p>
<dd>End a nesting level.</p>
<dt><code>\O5[</code><i>Pfilename</i><code>]</code></p>
<dd>This escape is <code>grohtml</code> specific. Provided that this escape occurs at the outer nesting level, write <i>filename</i> to stderr. The position of the image, <i>P</i>, must be specified and must be one of <code>l</code>, <code>r</code>, <code>c</code>, or <code>i</code> (left, right, centered, inline). <i>filename</i> is associated with the production of the next inline image.</dl>
</dl>
<dt><code>\R&#8217;</code><i>name&nbsp;&plusmn;n</i><code>&#8216;</code></p>
<dd>This has the same effect as</p>
<dl>
<dd>
<dl>
<dd><code>.nr&nbsp;</code><i>name&nbsp;&plusmn;n</i></dl>
</dl>
<dt><code>\s(</code><i>nn</i></p>
<dd><code>\s&plusmn;(</code><i>nn</i> Set the point size to <i>nn</i> points; <i>nn</i> must be exactly two digits.</p>
<dt><code>\s[&plusmn;</code><i>n</i><code>]</code></p>
<dd><code>\s&plusmn;[</code><i>n</i><code>]</code> <code>\s&#8217;&plusmn;</code><i>n</i><code>&#8216;</code> <code>\s&plusmn;&#8217;</code><i>n</i><code>&#8216;</code> Set the point size to <i>n</i> scaled points; <i>n</i> is a numeric expression with a default scale indicator of~<code>z</code>.</p>
<dt><code>\V</code><i>x</i></p>
<dd><code>\V(</code><i>xx</i> <code>\V[</code><i>xxx</i><code>]</code> Interpolate the contents of the environment variable <i>xxx</i>, as returned by <code><a href="/docs/linux/man/3-getenv/">getenv</a></code>(3). <code>\V</code> is interpreted in copy mode.</p>
<dt><code>\Y</code><i>x</i></p>
<dd><code>\Y(</code><i>xx</i> <code>\Y[</code><i>xxx</i><code>]</code> This is approximately equivalent to <code>\X&#8217;\*[</code><i>xxx</i><code>]&#8217;</code>. However the contents of the string or macro <i>xxx</i> are not interpreted; also it is permitted for <i>xxx</i> to have been defined as a macro and thus contain newlines (it is not permitted for the argument to <code>\X</code> to contain newlines). The inclusion of newlines requires an extension to the Unix troff output format, and confuses drivers that do not know about this extension.</p>
<dt><code>\Z&#8217;</code><i>anything</i><code>&#8216;</code></p>
<dd>Print anything and then restore the horizontal and vertical position; <i>anything</i> may not contain tabs or leaders.</p>
<dt><code>\$0</code></p>
<dd>The name by which the current macro was invoked. The <code>als</code> request can make a macro have more than one name.</p>
<dt><code>\$*</code></p>
<dd>In a macro or string, the concatenation of all the arguments separated by spaces.</p>
<dt><code>\$@</code></p>
<dd>In a macro or string, the concatenation of all the arguments with each surrounded by double quotes, and separated by spaces.</p>
<dt><code>\$^</code></p>
<dd>In a macro, the representation of all parameters as if they were an argument to the <code>ds</code> request.</p>
<dt><code>\$(</code><i>nn</i></p>
<dd><code>\$[</code><i>nnn</i><code>]</code> In a macro or string, this gives the <i>nn</i>-th or <i>nnn</i>-th argument. Macros and strings can have an unlimited number of arguments.</p>
<dt><code>\?</code><i>anything</i><code>\?</code></p>
<dd>When used in a diversion, this transparently embeds <i>anything</i> in the diversion. <i>anything</i> is read in copy mode. When the diversion is reread, <i>anything</i> is interpreted. <i>anything</i> may not contain newlines; use <code>\!</code> if you want to embed newlines in a diversion. The escape sequence <code>\?</code> is also recognized in copy mode and turned into a single internal code; it is this code that terminates <i>anything</i>. Thus</p>
<dl>
<dd>
<dl>
<dd>.nr x 1 .nf .di d \?\?\\?\\\\nx\\?\?\? .di .nr x 2 .di e .d .di .nr x 3 .di f .e .di .nr x 4 .f</dl>
</dl>
<dd>prints~<code>4</code>.</p>
<dt><code>\/</code></p>
<dd>This increases the width of the preceding glyph so that the spacing between that glyph and the following glyph is correct if the following glyph is a roman glyph. It is a good idea to use this escape sequence whenever an italic glyph is immediately followed by a roman glyph without any intervening space.</p>
<dt><code>\,</code></p>
<dd>This modifies the spacing of the following glyph so that the spacing between that glyph and the preceding glyph is correct if the preceding glyph is a roman glyph. It is a good idea to use this escape sequence whenever a roman glyph is immediately followed by an italic glyph without any intervening space.</p>
<dt><code>\)</code></p>
<dd>Like <code>\&amp;</code> except that it behaves like a character declared with the <code>cflags</code> request to be transparent for the purposes of end-of-sentence recognition.</p>
<dt><code>\~</code></p>
<dd>This produces an unbreakable space that stretches like a normal inter-word space when a line is adjusted.</p>
<dt><code>\:</code></p>
<dd>This causes the insertion of a zero-width break point. It is equal to <code>\%</code> within a word but without insertion of a soft hyphen glyph.</p>
<dt><code>\#</code></p>
<dd>Everything up to and including the next newline is ignored. This is interpreted in copy mode. It is like <code>\</code> except that <code>\</code> does not ignore the terminating newline.</dl>
<h3>New requests</h3>
<dl>
<dt><code>.aln&nbsp;</code><i>xx yy</i></p>
<dd>Create an alias <i>xx</i> for number register object named <i>yy</i>. The new name and the old name are exactly equivalent. If <i>yy</i> is undefined, a warning of type <code>reg</code> is generated, and the request is ignored.</p>
<dt><code>.als&nbsp;</code><i>xx yy</i></p>
<dd>Create an alias <i>xx</i> for request, string, macro, or diversion object named <i>yy</i>. The new name and the old name are exactly equivalent (it is similar to a hard rather than a soft link). If <i>yy</i> is undefined, a warning of type <code>mac</code> is generated, and the request is ignored. The <code>de</code>, <code>am</code>, <code>di</code>, <code>da</code>, <code>ds</code>, and <code>as</code> requests only create a new object if the name of the macro, diversion or string is currently undefined or if it is defined to be a request; normally they modify the value of an existing object.</p>
<dt><code>.am1&nbsp;</code><i>xx yy</i></p>
<dd>Similar to <code>.am</code>, but compatibility mode is switched off during execution. To be more precise, a &#8216;compatibility save&#8217; token is inserted at the beginning of the macro addition, and a &#8216;compatibility restore&#8217; token at the end. As a consequence, the requests <code>am</code>, <code>am1</code>, <code>de</code>, and <code>de1</code> can be intermixed freely since the compatibility save/:restore tokens only affect the macro parts defined by <code>.am1</code> and <code>.ds1</code>.</p>
<dt><code>.ami&nbsp;</code><i>xx yy</i></p>
<dd>Append to macro indirectly. See the <code>dei</code> request below for more information.</p>
<dt><code>.ami1&nbsp;</code><i>xx yy</i></p>
<dd>Same as the <code>ami</code> request but compatibility mode is switched off during execution.</p>
<dt><code>.as1&nbsp;</code><i>xx yy</i></p>
<dd>Similar to <code>.as</code>, but compatibility mode is switched off during expansion. To be more precise, a &#8216;compatibility save&#8217; token is inserted at the beginning of the string, and a &#8216;compatibility restore&#8217; token at the end. As a consequence, the requests <code>as</code>, <code>as1</code>, <code>ds</code>, and <code>ds1</code> can be intermixed freely since the compatibility save/:restore tokens only affect the (sub)strings defined by <code>as1</code> and <code>ds1</code>.</p>
<dt><code>.asciify&nbsp;</code><i>xx</i></p>
<dd>This request &#8216;unformats&#8217; the diversion <i>xx</i> in such a way that ASCII and space characters (and some escape sequences) that were formatted and diverted into <i>xx</i> are treated like ordinary input characters when <i>xx</i> is reread. Useful for diversions in conjunction with the <code>writem</code> request. It can be also used for gross hacks; for example, this</p>
<dl>
<dd>
<dl>
<dd>.tr @. .di x @nr n 1 .br .di .tr @@ .asciify x .x</dl>
</dl>
<dd>sets register~<code>n</code> to~1. Note that glyph information (font, font size, etc.) is not preserved; use <code>.unformat</code> instead.</p>
<dt><code>.backtrace</code></p>
<dd>Print a backtrace of the input stack on stderr.</p>
<dt><code>.blm&nbsp;</code><i>xx</i></p>
<dd>Set the blank line macro to <i>xx</i>. If there is a blank line macro, it is invoked when a blank line is encountered instead of the usual troff behaviour.</p>
<dt><code>.box&nbsp;</code><i>xx</i></p>
<dd><code>.boxa&nbsp;</code><i>xx</i> These requests are similar to the <code>di</code> and <code>da</code> requests with the exception that a partially filled line does not become part of the diversion (i.e., the diversion always starts with a new line) but is restored after ending the diversion, discarding the partially filled line which possibly comes from the diversion.</p>
<dt><code>.break</code></p>
<dd>Break out of a while loop. See also the <code>while</code> and <code>continue</code> requests. Be sure not to confuse this with the <code>br</code> request.</p>
<dt><code>.brp</code></p>
<dd>This is the same as <code>\p</code>.</p>
<dt><code>.cflags&nbsp;</code><i>n c1 c2 </i></p>
<dd>Characters <i>c1</i>, <i>c2</i>, <i></i>, have properties determined by <i>n</i>, which is ORed from the following:</p>
<dl>
<dd>
<dl>
<dt>1</p>
<dd>The character ends sentences (initially characters <code>.?!</code> have this property).</p>
<dt>2</p>
<dd>Lines can be broken before the character (initially no characters have this property); a line is not broken at a character with this property unless the characters on each side both have non-zero hyphenation codes. This can be overridden with value 64.</p>
<dt>4</p>
<dd>Lines can be broken after the character (initially characters <code>-\[hy]\[em]</code> have this property); a line is not broken at a character with this property unless the characters on each side both have non-zero hyphenation codes. This can be overridden with value 64.</p>
<dt>8</p>
<dd>The glyph associated with this character overlaps horizontally (initially characters <code>\[ul]\[rn]\[ru]\[radicalex]\[sqrtex]</code> have this property).</p>
<dt>16</p>
<dd>The glyph associated with this character overlaps vertically (initially glyph <code>\[br]</code> has this property).</p>
<dt>32</p>
<dd>An end-of-sentence character followed by any number of characters with this property is treated as the end of a sentence if followed by a newline or two spaces; in other words the character is transparent for the purposes of end-of-sentence recognition; this is the same as having a zero space factor in TeX (initially characters <code>&quot;&#8217;)]*\[dg]\[rq]\[cq]</code> have this property).</p>
<dt>64</p>
<dd>Ignore hyphenation code values of the surrounding characters. Use this in combination with values 2 and~4 (initially no characters have this property).</p>
<dt>128</p>
<dd>Prohibit a line break before the character, but allow a line break after the character. This works only in combination with flags 256 and 512 and has no effect otherwise.</p>
<dt>256</p>
<dd>Prohibit a line break after the character, but allow a line break before the character. This works only in combination with flags 128 and 512 and has no effect otherwise.</p>
<dt>512</p>
<dd>Allow line break before or after the character. This works only in combination with flags 128 and 256 and has no effect otherwise.</dl>
</dl>
<dd>Contrary to flag values 2 and~4, the flags 128, 256, and 512 work pairwise. If, for example, the left character has value 512, and the right character 128, no line break gets inserted. If we use value~6 instead for the left character, a line break after the character can&#8217;t be suppressed since the right neighbour character doesn&#8217;t get examined.</p>
<dt><code>.char&nbsp;</code><i>c string</i></p>
<dd>[This request can both define characters and glyphs.]</p>
<dd>Define entity~<i>c</i> to be <i>string</i>. To be more precise, define (or even override) a groff entity which can be accessed with name~<i>c</i> on the input side, and which uses <i>string</i> on the output side. Every time glyph~<i>c</i> needs to be printed, <i>string</i> is processed in a temporary environment and the result is wrapped up into a single object. Compatibility mode is turned off and the escape character is set to~<code>\</code> while <i>string</i> is being processed. Any emboldening, constant spacing or track kerning is applied to this object rather than to individual glyphs in <i>string</i>.</p>
<dd>A groff object defined by this request can be used just like a normal glyph provided by the output device. In particular other characters can be translated to it with the <code>tr</code> request; it can be made the leader glyph by the <code>lc</code> request; repeated patterns can be drawn with the glyph using the <code>\l</code> and <code>\L</code> escape sequences; words containing~<i>c</i> can be hyphenated correctly, if the <code>hcode</code> request is used to give the object a hyphenation code.</p>
<dd>There is a special anti-recursion feature: Use of glyph within the glyph&#8217;s definition is handled like normal glyphs not defined with <code>char</code>.</p>
<dd>A glyph definition can be removed with the <code>rchar</code> request.</p>
<dt><code>.chop&nbsp;</code><i>xx</i></p>
<dd>Chop the last element off macro, string, or diversion <i>xx</i>. This is useful for removing the newline from the end of diversions that are to be interpolated as strings.</p>
<dt><code>.class&nbsp;</code><i>name c1 c2 </i></p>
<dd>Assign <i>name</i> to a set of characters <i>c1</i>, <i>c2</i>, <i></i>, so that they can be referred to from other requests easily (currently <code>.cflags</code> only). Character ranges (indicated by an intermediate &#8216;-&#8216;) and nested classes are possible also. This is useful to assign properties to a large set of characters.</p>
<dt><code>.close&nbsp;</code><i>stream</i></p>
<dd>Close the stream named <i>stream</i>; <i>stream</i> will no longer be an acceptable argument to the <code>write</code> request. See the <code>open</code> request.</p>
<dt><code>.composite&nbsp;</code><i>glyph1 glyph2</i></p>
<dd>Map glyph name <i>glyph1</i> to glyph name <i>glyph2</i> if it is used in <code>\[</code><i></i><code>]</code> with more than one component.</p>
<dt><code>.continue</code></p>
<dd>Finish the current iteration of a while loop. See also the <code>while</code> and <code>break</code> requests.</p>
<dt><code>.color&nbsp;</code><i>n</i></p>
<dd>If <i>n</i> is non-zero or missing, enable colors (this is the default), otherwise disable them.</p>
<dt><code>.cp&nbsp;</code><i>n</i></p>
<dd>If <i>n</i> is non-zero or missing, enable compatibility mode, otherwise disable it. In compatibility mode, long names are not recognized, and the incompatibilities caused by long names do not arise.</p>
<dt><code>.defcolor&nbsp;</code><i>xxx scheme color_components</i></p>
<dd>Define color <i>xxx</i>. <i>scheme</i> can be one of the following values: <code>rgb</code> (three components), <code>cmy</code> (three components), <code>cmyk</code> (four components), and <code>gray</code> or <code>grey</code> (one component). Color components can be given either as a hexadecimal string or as positive decimal integers in the range 0-65535. A hexadecimal string contains all color components concatenated; it must start with either <code>#</code> or <code>##</code>. The former specifies hex values in the range 0-255 (which are internally multiplied by~257), the latter in the range 0-65535. Examples: #FFC0CB (pink), ##ffff0000ffff (magenta). A new scaling indicator~<code>f</code> has been introduced which multiplies its value by~65536; this makes it convenient to specify color components as fractions in the range 0 to~1. Example:</p>
<dl>
<dd>
<dl>
<dd>.defcolor darkgreen rgb 0.1f 0.5f 0.2f</dl>
</dl>
<dd>Note that <code>f</code> is the default scaling indicator for the <code>defcolor</code> request, thus the above statement is equivalent to</p>
<dl>
<dd>
<dl>
<dd>.defcolor darkgreen rgb 0.1 0.5 0.2</dl>
</dl>
<dd>The color named <code>default</code> (which is device-specific) can&#8217;t be redefined. It is possible that the default color for <code>\M</code> and <code>\m</code> is not the same.</p>
<dt><code>.de1&nbsp;</code><i>xx yy</i></p>
<dd>Similar to <code>.de</code>, but compatibility mode is switched off during execution. On entry, the current compatibility mode is saved and restored at exit.</p>
<dt><code>.dei&nbsp;</code><i>xx yy</i></p>
<dd>Define macro indirectly. The following example</p>
<dl>
<dd>
<dl>
<dd>.ds xx aa .ds yy bb .dei xx yy</dl>
</dl>
<dd>is equivalent to</p>
<dl>
<dd>
<dl>
<dd>.de aa bb</dl>
</dl>
<dt><code>.dei1&nbsp;</code><i>xx yy</i></p>
<dd>Similar to the <code>dei</code> request but compatibility mode is switched off during execution.</p>
<dt><code>.device&nbsp;</code><i>anything</i></p>
<dd>This is (almost) the same as the <code>\X</code> escape. <i>anything</i> is read in copy mode; a leading~<code>&quot;</code> is stripped.</p>
<dt><code>.devicem&nbsp;</code><i>xx</i></p>
<dd>This is the same as the <code>\Y</code> escape (to embed the contents of a macro into the intermediate output preceded with &#8216;x~X&#8217;).</p>
<dt><code>.do&nbsp;</code><i>xxx</i></p>
<dd>Interpret <i>.xxx</i> with compatibility mode disabled. For example,</p>
<dl>
<dd>
<dl>
<dd>.do fam T</dl>
<p> would have the same effect as</p>
<dl>
<dd>.fam T</dl>
<p> except that it would work even if compatibility mode had been enabled. Note that the previous compatibility mode is restored before any files sourced by <i>xxx</i> are interpreted.</dl>
<dt><code>.ds1&nbsp;</code><i>xx yy</i></p>
<dd>Similar to <code>.ds</code>, but compatibility mode is switched off during expansion. To be more precise, a &#8216;compatibility save&#8217; token is inserted at the beginning of the string, and a &#8216;compatibility restore&#8217; token at the end.</p>
<dt><code>.ecs</code></p>
<dd>Save current escape character.</p>
<dt><code>.ecr</code></p>
<dd>Restore escape character saved with <code>ecs</code>. Without a previous call to <code>ecs</code>, &#8216;<code>\</code>&#8216; will be the new escape character.</p>
<dt><code>.evc&nbsp;</code><i>xx</i></p>
<dd>Copy the contents of environment <i>xx</i> to the current environment. No pushing or popping of environments is done.</p>
<dt><code>.fam&nbsp;</code><i>xx</i></p>
<dd>Set the current font family to <i>xx</i>. The current font family is part of the current environment. If <i>xx</i> is missing, switch back to previous font family. The value at start-up is &#8216;T&#8217;. See the description of the <code>sty</code> request for more information on font families.</p>
<dt><code>.fchar&nbsp;</code><i>c string</i></p>
<dd>Define fallback character (or glyph)~<i>c</i> to be <i>string</i>. The syntax of this request is the same as the <code>char</code> request; the only difference is that a glyph defined with <code>char</code> hides the glyph with the same name in the current font, whereas a glyph defined with <code>fchar</code> is checked only if the particular glyph isn&#8217;t found in the current font. This test happens before checking special fonts.</p>
<dt><code>.fcolor&nbsp;</code><i>c</i></p>
<dd>Set the fill color to~<i>c</i>. If <i>c</i> is missing, switch to the previous fill color.</p>
<dt><code>.fschar&nbsp;</code><i>f c string</i></p>
<dd>Define fallback character (or glyph)~<i>c</i> for font~<i>f</i> to be <i>string</i>. The syntax of this request is the same as the <code>char</code> request (with an additional argument to specify the font); a glyph defined with <code>fschar</code> is searched after the list of fonts declared with the <code>fspecial</code> request but before the list of fonts declared with <code>.special</code>.</p>
<dt><code>.fspecial&nbsp;</code><i>f s1 s2 </i></p>
<dd>When the current font is~<i>f</i>, fonts <i>s1</i>, <i>s2</i>, <i></i>, are special, that is, they are searched for glyphs not in the current font. Any fonts specified in the <code>special</code> request are searched after fonts specified in the <code>fspecial</code> request. Without argument, reset the list of global special fonts to be empty.</p>
<dt><code>.ftr&nbsp;</code><i>f g</i></p>
<dd>Translate font~<i>f</i> to~<i>g</i>. Whenever a font named~<i>f</i> is referred to in an <code></code> escape sequence, in the <code>F</code> and <code>S</code> conditional operators, or in the <code>ft</code>, <code>ul</code>, <code>bd</code>, <code>cs</code>, <code>tkf</code>, <code>special</code>, <code>fspecial</code>, <code>fp</code>, or <code>sty</code> requests, font~<i>g</i> is used. If <i>g</i> is missing, or equal to~<i>f</i> then font~<i>f</i> is not translated.</p>
<dt><code>.fzoom&nbsp;</code><i>f zoom</i></p>
<dd>Set zoom factor <i>zoom</i> for font~<i>f</i>. <i>zoom</i> must a non-negative integer multiple of 1/1000th. If it is missing or is equal to zero, it means the same as 1000, namely no magnification. <i>f</i>~must be a real font name, not a style.</p>
<dt><code>.gcolor&nbsp;</code><i>c</i></p>
<dd>Set the glyph color to~<i>c</i>. If <i>c</i> is missing, switch to the previous glyph color.</p>
<dt><code>.hcode&nbsp;</code><i>c1 code1 c2 code2 </i></p>
<dd>Set the hyphenation code of character <i>c1</i> to <i>code1</i> and that of <i>c2</i> to <i>code2</i>, and so on. A hyphenation code must be a single input character (not a special character) other than a digit or a space. Initially each lower-case letter a-z has a hyphenation code, which is itself, and each upper-case letter A-Z has a hyphenation code which is the lower-case version of itself. See also the <code>hpf</code> request.</p>
<dt><code>.hla&nbsp;</code><i>lang</i></p>
<dd>Set the current hyphenation language to <i>lang</i>. Hyphenation exceptions specified with the <code>hw</code> request and hyphenation patterns specified with the <code>hpf</code> request are both associated with the current hyphenation language. The <code>hla</code> request is usually invoked by the <code>troffrc</code> file to set up a default language.</p>
<dt><code>.hlm&nbsp;</code><i>n</i></p>
<dd>Set the maximum number of consecutive hyphenated lines to~<i>n</i>. If <i>n</i> is negative, there is no maximum. The default value is~-1. This value is associated with the current environment. Only lines output from an environment count towards the maximum associated with that environment. Hyphens resulting from <code>\%</code> are counted; explicit hyphens are not.</p>
<dt><code>.hpf&nbsp;</code><i>file</i></p>
<dd>Read hyphenation patterns from <i>file</i>; this is searched for in the same way that <i>name</i><code>.tmac</code> is searched for when the <code>-m</code><i>name</i> option is specified. It should have the same format as (simple) TeX patterns files. More specifically, the following scanning rules are implemented.</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>A percent sign starts a comment (up to the end of the line) even if preceded by a backslash.</p>
<dt>&bull;</p>
<dd>No support for &#8216;digraphs&#8217; like <code>\$</code>.</p>
<dt>&bull;</p>
<dd><code>^^</code><i>xx</i> (<i>x</i> is 0-9 or a-f) and <code>^^</code><i>x</i> (character code of~<i>x</i> in the range 0-127) are recognized; other use of~<code>^</code> causes an error.</p>
<dt>&bull;</p>
<dd>No macro expansion.</p>
<dt>&bull;</p>
<dd><code>hpf</code> checks for the expression <code>\patterns{</code><code>}</code> (possibly with whitespace before and after the braces). Everything between the braces is taken as hyphenation patterns. Consequently, <code>{</code>~and~<code>}</code> are not allowed in patterns.</p>
<dt>&bull;</p>
<dd>Similarly, <code>\hyphenation{</code><code>}</code> gives a list of hyphenation exceptions.</p>
<dt>&bull;</p>
<dd><code>ndinput</code> is recognized also.</p>
<dt>&bull;</p>
<dd>For backwards compatibility, if <code>\patterns</code> is missing, the whole file is treated as a list of hyphenation patterns (only recognizing the <code>%</code>~character as the start of a comment).</dl>
</dl>
<dd>Use the <code>hpfcode</code> request to map the encoding used in hyphenation patterns files to <code>groff</code>&#8216;s input encoding. By default, everything maps to itself except letters &#8216;A&#8217; to &#8216;Z&#8217; which map to &#8216;a&#8217; to &#8216;z&#8217;.</p>
<dd>The set of hyphenation patterns is associated with the current language set by the <code>hla</code> request. The <code>hpf</code> request is usually invoked by the <code>troffrc</code> file; a second call replaces the old patterns with the new ones.</p>
<dt><code>.hpfa&nbsp;</code><i>file</i></p>
<dd>The same as <code>hpf</code> except that the hyphenation patterns from <i>file</i> are appended to the patterns already loaded in the current language.</p>
<dt><code>.hpfcode&nbsp;</code><i>a b c d </i></p>
<dd>After reading a hyphenation patterns file with the <code>hpf</code> or <code>hpfa</code> request, convert all characters with character code~<i>a</i> in the recently read patterns to character code~<i>b</i>, character code~<i>c</i> to~<i>d</i>, etc. Initially, all character codes map to themselves. The arguments of <code>hpfcode</code> must be integers in the range 0 to~255. Note that it is even possible to use character codes which are invalid in <code>groff</code> otherwise.</p>
<dt><code>.hym&nbsp;</code><i>n</i></p>
<dd>Set the <i>hyphenation margin</i> to~<i>n</i>: when the current adjustment mode is not~<code>b</code>, the line is not hyphenated if the line is no more than <i>n</i> short. The default hyphenation margin is~0. The default scaling indicator for this request is~<code>m</code>. The hyphenation margin is associated with the current environment. The current hyphenation margin is available in the <code>
[.hym]</code> register.</p>
<dt><code>.hys&nbsp;</code><i>n</i></p>
<dd>Set the <i>hyphenation space</i> to~<i>n</i>: When the current adjustment mode is~<code>b</code> don&#8217;t hyphenate the line if the line can be justified by adding no more than <i>n</i> extra space to each word space. The default hyphenation space is~0. The default scaling indicator for this request is~<code>m</code>. The hyphenation space is associated with the current environment. The current hyphenation space is available in the <code>
[.hys]</code> register.</p>
<dt><code>.itc&nbsp;</code><i>n macro</i></p>
<dd>Variant of <code>.it</code> for which a line interrupted with <code>
