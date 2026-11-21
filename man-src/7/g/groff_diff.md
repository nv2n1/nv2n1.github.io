---

title: "groff_diff(7)"
name: "groff_diff"
section: "7"
letter: "g"
url: "/docs/linux/man/7-groff_diff/"
description: "groff_diff – differences between GNU troff and classical troff"
---

<p>groff_diff &#8211; differences between GNU troff and classical troff </p>
<p> This manual page describes the language differences between <i>groff</i>, the GNU <i>roff</i> text processing system, and the classical <i>roff</i> formatter of the freely available Unix~7 of the 1970s, documented in the <i>Troff User&#8217;s Manual</i> by <i>Ossanna</i> and <i>Kernighan</i>. This includes the roff language as well as the intermediate output format (troff output). </p>
<p>Section "See Also" below gives pointers to both the classical <i>roff</i> and the modern <i>groff</i> documentation.  </p>
<h2>GROFF LANGUAGE</h2>
<p> In this section, all additional features of <i>groff</i> compared to the classical Unix~7 <i>troff</i> are described in detail.  </p>
<h3>Long names</h3>
<p> The names of number registers, fonts, strings/:macros/:diversions, special characters (glyphs), and colors can be of any length. In escape sequences, additionally to the classical &#8216;<code>(</code>,<i>xx/</i>&#8216; construction for a two-character glyph name, you can use &#8216;<code>[</code>,<i>xxx/</i><code>]</code>&#8216; for a name of arbitrary length. </p>
<dl>
<dt><code>\[</code><i>xxx</i><code>]</code></dt>
<dd> <p> Print the special character (glyph) called <i>xxx</i>. </p>
 </dd>
<dt><code>\[</code><i>comp1 comp2 </i><code>]</code></dt>
<dd> <p> Print composite glyph consisting of multiple components. Example: &#8216;\[A~ho]&#8216; is capital letter A with ogonek which finally maps to glyph name &#8216;u0041_0328&#8217;. See <i>Groff: The GNU Implementation of troff</i>, the <i>groff</i> Texinfo manual, for details of how a glyph name for a composite glyph is constructed, and <code><a href="/docs/linux/man/7-groff_char/">groff_char</a></code>(7) for a list of glyph name components used in composite glyph names. </p>
 </dd>
<dt><code>\f[</code><i>xxx</i><code>]</code></dt>
<dd> <p> Set font <i>xxx</i>. Additionally, <code>\f[]</code> is a new syntax form equal to <code>\fP</code>, i.e., to return to the previous font. </p>
 </dd>
<dt><code>\*[</code><i>xxx arg1 arg2 </i><code>]</code></dt>
<dd> <p> Interpolate string <i>xxx</i>, taking <i>arg1</i>, <i>arg2</i>, <i></i>, as arguments. </p>
 </dd>
<dt><code>\n[</code><i>xxx</i><code>]</code></dt>
<dd> <p> Interpolate number register <i>xxx</i>. </p>
 </dd></dl>
<h3>Fractional point sizes</h3>
<p> A <i>scaled point</i> is equal to <code>1/sizescale</code> points, where <code>sizescale</code> is specified in the <i>DESC</i> file (1 by default). There is a new scale indicator~<code>z</code> that has the effect of multiplying by sizescale. Requests and escape sequences in troff interpret arguments that represent a point size as being in units of scaled points, but they evaluate each such argument using a default scale indicator of~<code>z</code>. Arguments treated in this way are the argument to the <code>ps</code> request, the third argument to the <code>cs</code> request, the second and fourth arguments to the <code>tkf</code> request, the argument to the <code>\H</code> escape sequence, and those variants of the <code>\s</code> escape sequence that take a numeric expression as their argument. </p>
<p>For example, suppose sizescale is 1000; then a scaled point is equivalent to a millipoint; the call <code>.ps 10.25</code> is equivalent to <code>.ps 10.25z</code> and so sets the point size to 10250 scaled points, which is equal to 10.25 points. </p>
<p>The number register <code>\n[.s]</code> returns the point size in points as decimal fraction. There is also a new number register <code>\n[.ps]</code> that returns the point size in scaled points. </p>
<p>It would make no sense to use the <code>z</code>~scale indicator in a numeric expression whose default scale indicator was neither <code>u</code> nor~<code>z</code>, and so <code>troff</code> disallows this. Similarly it would make no sense to use a scaling indicator other than <code>z</code> or~<code>u</code> in a numeric expression whose default scale indicator was~<code>z</code>, and so <code>troff</code> disallows this as well. </p>
<p>There is also new scale indicator~<code>s</code> which multiplies by the number of units in a scaled point. So, for example, <code>\n[.ps]s</code> is equal to <code>1m</code>. Be sure not to confuse the <code>s</code> and <code>z</code>~scale indicators.  </p>
<h3>Numeric expressions</h3>
<p> Spaces are permitted in a number expression within parentheses. </p>
<p> <code>M</code> indicates a scale of 100ths of an em. <code>f</code> indicates a scale of 65536 units, providing fractions for color definitions with the <code>defcolor</code> request. For example, 0.5f = 32768u. </p>
<dl>
<dt><i>e1</i><code>&gt;?</code><i>e2</i></dt>
<dd> <p> The maximum of <i>e1</i> and <i>e2</i>. </p>
 </dd>
<dt><i>e1</i><code>&lt;?</code><i>e2</i></dt>
<dd> <p> The minimum of <i>e1</i> and <i>e2</i>. </p>
 </dd>
<dt><code>(</code><i>c</i><code>;</code><i>e</i><code>)</code></dt>
<dd> <p> Evaluate <i>e</i> using <i>c</i> as the default scaling indicator. If <i>c</i> is missing, ignore scaling indicators in the evaluation of~<i>e</i>. </p>
 </dd></dl>
<h3>New escape sequences</h3>
<dl>
<dt><code>\A&#8217;</code><i>anything</i><code>&#8216;</code></dt>
<dd> <p> This expands to <code>1</code> or~<code>0</code>, depending on whether <i>anything</i> is or is not acceptable as the name of a string, macro, diversion, number register, environment, font, or color. It returns~<code>0</code> if <i>anything</i> is empty. This is useful if you want to look up user input in some sort of associative table. </p>
 </dd>
<dt><code>\B&#8217;</code><i>anything</i><code>&#8216;</code></dt>
<dd> <p> This expands to <code>1</code> or~<code>0</code>, depending on whether <i>anything</i> is or is not a valid numeric expression. It returns~<code>0</code> if <i>anything</i> is empty. </p>
 </dd>
<dt><code>\C&#8217;</code><i>xxx</i><code>&#8216;</code></dt>
<dd> <p> Typeset glyph named <i>xxx</i>. Normally it is more convenient to use <code>\[</code><i>xxx</i><code>]</code>. But <code>\C</code> has the advantage that it is compatible with recent versions of Unix and is available in compatibility mode. </p>
 </dd>
<dt><code>\E</code></dt>
<dd> <p> This is equivalent to an escape character, but it is not interpreted in copy mode. For example, strings to start and end superscripting could be defined like this </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <p> .ds { \v&#8217;-.3m&#8217;\s&#8217;\En[.s]*6u/10u&#8217; .ds } \s0\v&#8217;.3m&#8217; </p>
 </dd></dl>
</dl>
<dd> <p> The use of <code>\E</code> ensures that these definitions work even if <code>\*{</code> gets interpreted in copy mode (for example, by being used in a macro argument). </p>
 </dd>
<dt><code>\F</code><i>f</i></dt>
<dd> <p> <code>\F(</code><i>fm</i> <code>\F[</code><i>fam</i><code>]</code> Change font family. This is the same as the <code>fam</code> request. <code>\F[]</code> switches back to the previous font family (note that <code>\FP</code> won&#8217;t work; it selects font family &#8216;P&#8217; instead). </p>
 </dd>
<dt><code>\m</code><i>x</i></dt>
<dd> <p> <code>\m(</code><i>xx</i> <code>\m[</code><i>xxx</i><code>]</code> Set drawing color. <code>\m[]</code> switches back to the previous color. </p>
 </dd>
<dt><code>\M</code><i>x</i></dt>
<dd> <p> <code>\M(</code><i>xx</i> <code>\M[</code><i>xxx</i><code>]</code> Set background color for filled objects drawn with the <code>\D&#8217;</code><i></i><code>&#8216;</code> commands. <code>\M[]</code> switches back to the previous color. </p>
 </dd>
<dt><code>\N&#8217;</code><i>n</i><code>&#8216;</code></dt>
<dd> <p> Typeset the glyph with index~<i>n</i> in the current font. <i>n</i>~can be any integer. Most devices only have glyphs with indices between 0 and 255. If the current font does not contain a glyph with that code, special fonts are <i>not</i> searched. The <code>\N</code> escape sequence can be conveniently used in conjunction with the <code>char</code> request, for example </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <p> .char \[phone] \f(ZD\N&#8217;37&#8217; </p>
 </dd></dl>
</dl>
<dd> <p> The index of each glyph is given in the fourth column in the font description file after the <code>charset</code> command. It is possible to include unnamed glyphs in the font description file by using a name of <code>---</code>; the <code>\N</code> escape sequence is the only way to use these. </p>
 </dd>
<dt><code>\O</code><i>n</i></dt>
<dd> <p> <code>\O[</code><i>n</i><code>]</code> Suppress troff output. The escapes <code>\O2</code>, <code>\O3</code>, <code>\O4</code>, and <code>\O5</code> are intended for internal use by <code>grohtml</code>. </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>\O0</code></dt>
<dd> <p> Disable any ditroff glyphs from being emitted to the device driver, provided that the escape occurs at the outer level (see <code>\O3</code> and <code>\O4</code>). </p>
 </dd>
<dt><code>\O1</code></dt>
<dd> <p> Enable output of glyphs, provided that the escape occurs at the outer level. </p>
 </dd>
<dd> <p> <code>\O0</code> and <code>\O1</code> also reset the registers <code>\n[opminx]</code>, <code>\n[opminy]</code>, <code>\n[opmaxx]</code>, and <code>\n[opmaxy]</code> to~-1. These four registers mark the top left and bottom right hand corners of a box which encompasses all written glyphs. </p>
 </dd>
<dt><code>\O2</code></dt>
<dd> <p> Provided that the escape occurs at the outer level, enable output of glyphs and also write out to stderr the page number and four registers encompassing the glyphs previously written since the last call to <code>\O</code>. </p>
 </dd>
<dt><code>\O3</code></dt>
<dd> <p> Begin a nesting level. At start-up, <code>troff</code> is at outer level. This is really an internal mechanism for <code>grohtml</code> while producing images. They are generated by running the troff source through <code>troff</code> to the PostScript device and <code>ghostscript</code> to produce images in PNG format. The <code>\O3</code> escape starts a new page if the device is not html (to reduce the possibility of images crossing a page boundary). </p>
 </dd>
<dt><code>\O4</code></dt>
<dd> <p> End a nesting level. </p>
 </dd>
<dt><code>\O5[</code><i>Pfilename</i><code>]</code></dt>
<dd> <p> This escape is <code>grohtml</code> specific. Provided that this escape occurs at the outer nesting level, write <i>filename</i> to stderr. The position of the image, <i>P</i>, must be specified and must be one of <code>l</code>, <code>r</code>, <code>c</code>, or <code>i</code> (left, right, centered, inline). <i>filename</i> is associated with the production of the next inline image. </p>
 </dd></dl>
</dl>
<dt><code>\R&#8217;</code><i>name&nbsp;&plusmn;n</i><code>&#8216;</code></dt>
<dd> <p> This has the same effect as </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <p> <code>.nr&nbsp;</code><i>name&nbsp;&plusmn;n</i> </p>
 </dd></dl>
</dl>
<dt><code>\s(</code><i>nn</i></dt>
<dd> <p> <code>\s&plusmn;(</code><i>nn</i> Set the point size to <i>nn</i> points; <i>nn</i> must be exactly two digits. </p>
 </dd>
<dt><code>\s[&plusmn;</code><i>n</i><code>]</code></dt>
<dd> <p> <code>\s&plusmn;[</code><i>n</i><code>]</code> <code>\s&#8217;&plusmn;</code><i>n</i><code>&#8216;</code> <code>\s&plusmn;&#8216;</code><i>n</i><code>&#8216;</code> Set the point size to <i>n</i> scaled points; <i>n</i> is a numeric expression with a default scale indicator of~<code>z</code>. </p>
 </dd>
<dt><code>\V</code><i>x</i></dt>
<dd> <p> <code>\V(</code><i>xx</i> <code>\V[</code><i>xxx</i><code>]</code> Interpolate the contents of the environment variable <i>xxx</i>, as returned by <code><a href="/docs/linux/man/3-getenv/">getenv</a></code>(3). <code>\V</code> is interpreted in copy mode. </p>
 </dd>
<dt><code>\Y</code><i>x</i></dt>
<dd> <p> <code>\Y(</code><i>xx</i> <code>\Y[</code><i>xxx</i><code>]</code> This is approximately equivalent to <code>\X&#8217;\*[</code><i>xxx</i><code>]&#8216;</code>. However the contents of the string or macro <i>xxx</i> are not interpreted; also it is permitted for <i>xxx</i> to have been defined as a macro and thus contain newlines (it is not permitted for the argument to <code>\X</code> to contain newlines). The inclusion of newlines requires an extension to the Unix troff output format, and confuses drivers that do not know about this extension. </p>
 </dd>
<dt><code>\Z&#8217;</code><i>anything</i><code>&#8216;</code></dt>
<dd> <p> Print anything and then restore the horizontal and vertical position; <i>anything</i> may not contain tabs or leaders. </p>
 </dd>
<dt><code>\$0</code></dt>
<dd> <p> The name by which the current macro was invoked. The <code>als</code> request can make a macro have more than one name. </p>
 </dd>
<dt><code>\$*</code></dt>
<dd> <p> In a macro or string, the concatenation of all the arguments separated by spaces. </p>
 </dd>
<dt><code>\$@</code></dt>
<dd> <p> In a macro or string, the concatenation of all the arguments with each surrounded by double quotes, and separated by spaces. </p>
 </dd>
<dt><code>\$^</code></dt>
<dd> <p> In a macro, the representation of all parameters as if they were an argument to the <code>ds</code> request. </p>
 </dd>
<dt><code>\$(</code><i>nn</i></dt>
<dd> <p> <code>\$[</code><i>nnn</i><code>]</code> In a macro or string, this gives the <i>nn</i>-th or <i>nnn</i>-th argument. Macros and strings can have an unlimited number of arguments. </p>
 </dd>
<dt><code>\?</code><i>anything</i><code>\?</code></dt>
<dd> <p> When used in a diversion, this transparently embeds <i>anything</i> in the diversion. <i>anything</i> is read in copy mode. When the diversion is reread, <i>anything</i> is interpreted. <i>anything</i> may not contain newlines; use <code>\!</code> if you want to embed newlines in a diversion. The escape sequence <code>\?</code> is also recognized in copy mode and turned into a single internal code; it is this code that terminates <i>anything</i>. Thus </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <p> .nr x 1 .nf .di d \?\\?\\\\?\\\\\\\\nx\\\\?\\?\? .di .nr x 2 .di e .d .di .nr x 3 .di f .e .di .nr x 4 .f </p>
 </dd></dl>
</dl>
<dd> <p> prints~<code>4</code>. </p>
 </dd>
<dt><code>\/</code></dt>
<dd> <p> This increases the width of the preceding glyph so that the spacing between that glyph and the following glyph is correct if the following glyph is a roman glyph. It is a good idea to use this escape sequence whenever an italic glyph is immediately followed by a roman glyph without any intervening space. </p>
 </dd>
<dt><code>\,</code></dt>
<dd> <p> This modifies the spacing of the following glyph so that the spacing between that glyph and the preceding glyph is correct if the preceding glyph is a roman glyph. It is a good idea to use this escape sequence whenever a roman glyph is immediately followed by an italic glyph without any intervening space. </p>
 </dd>
<dt><code>\)</code></dt>
<dd> <p> Like <code>\&amp;</code> except that it behaves like a character declared with the <code>cflags</code> request to be transparent for the purposes of end-of-sentence recognition. </p>
 </dd>
<dt><code>\~</code></dt>
<dd> <p> This produces an unbreakable space that stretches like a normal inter-word space when a line is adjusted. </p>
 </dd>
<dt><code>\:</code></dt>
<dd> <p> This causes the insertion of a zero-width break point. It is equal to <code>\%</code> within a word but without insertion of a soft hyphen glyph. </p>
 </dd>
<dt><code>\#</code></dt>
<dd> <p> Everything up to and including the next newline is ignored. This is interpreted in copy mode. It is like <code>\</code> except that <code>\</code> does not ignore the terminating newline. </p>
 </dd></dl>
<h3>New requests</h3>
<dl>
<dt><code>.aln&nbsp;</code><i>xx yy</i></dt>
<dd> <p> Create an alias <i>xx</i> for number register object named <i>yy</i>. The new name and the old name are exactly equivalent. If <i>yy</i> is undefined, a warning of type <code>reg</code> is generated, and the request is ignored. </p>
 </dd>
<dt><code>.als&nbsp;</code><i>xx yy</i></dt>
<dd> <p> Create an alias <i>xx</i> for request, string, macro, or diversion object named <i>yy</i>. The new name and the old name are exactly equivalent (it is similar to a hard rather than a soft link). If <i>yy</i> is undefined, a warning of type <code>mac</code> is generated, and the request is ignored. The <code>de</code>, <code>am</code>, <code>di</code>, <code>da</code>, <code>ds</code>, and <code>as</code> requests only create a new object if the name of the macro, diversion or string is currently undefined or if it is defined to be a request; normally they modify the value of an existing object. </p>
 </dd>
<dt><code>.am1&nbsp;</code><i>xx yy</i></dt>
<dd> <p> Similar to <code>.am</code>, but compatibility mode is switched off during execution. To be more precise, a &#8216;compatibility save&#8217; token is inserted at the beginning of the macro addition, and a &#8216;compatibility restore&#8217; token at the end. As a consequence, the requests <code>am</code>, <code>am1</code>, <code>de</code>, and <code>de1</code> can be intermixed freely since the compatibility save/:restore tokens only affect the macro parts defined by <code>.am1</code> and <code>.ds1</code>. </p>
 </dd>
<dt><code>.ami&nbsp;</code><i>xx yy</i></dt>
<dd> <p> Append to macro indirectly. See the <code>dei</code> request below for more information. </p>
 </dd>
<dt><code>.ami1&nbsp;</code><i>xx yy</i></dt>
<dd> <p> Same as the <code>ami</code> request but compatibility mode is switched off during execution. </p>
 </dd>
<dt><code>.as1&nbsp;</code><i>xx yy</i></dt>
<dd> <p> Similar to <code>.as</code>, but compatibility mode is switched off during expansion. To be more precise, a &#8216;compatibility save&#8217; token is inserted at the beginning of the string, and a &#8216;compatibility restore&#8217; token at the end. As a consequence, the requests <code>as</code>, <code>as1</code>, <code>ds</code>, and <code>ds1</code> can be intermixed freely since the compatibility save/:restore tokens only affect the (sub)strings defined by <code>as1</code> and <code>ds1</code>. </p>
 </dd>
<dt><code>.asciify&nbsp;</code><i>xx</i></dt>
<dd> <p> This request &#8216;unformats&#8217; the diversion <i>xx</i> in such a way that ASCII and space characters (and some escape sequences) that were formatted and diverted into <i>xx</i> are treated like ordinary input characters when <i>xx</i> is reread. Useful for diversions in conjunction with the <code>writem</code> request. It can be also used for gross hacks; for example, this </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <p> .tr @. .di x @nr n 1 .br .di .tr @@ .asciify x .x </p>
 </dd></dl>
</dl>
<dd> <p> sets register~<code>n</code> to~1. Note that glyph information (font, font size, etc.) is not preserved; use <code>.unformat</code> instead. </p>
 </dd>
<dt><code>.backtrace</code></dt>
<dd> <p> Print a backtrace of the input stack on stderr. </p>
 </dd>
<dt><code>.blm&nbsp;</code><i>xx</i></dt>
<dd> <p> Set the blank line macro to <i>xx</i>. If there is a blank line macro, it is invoked when a blank line is encountered instead of the usual troff behaviour. </p>
 </dd>
<dt><code>.box&nbsp;</code><i>xx</i></dt>
<dd> <p> <code>.boxa&nbsp;</code><i>xx</i> These requests are similar to the <code>di</code> and <code>da</code> requests with the exception that a partially filled line does not become part of the diversion (i.e., the diversion always starts with a new line) but is restored after ending the diversion, discarding the partially filled line which possibly comes from the diversion. </p>
 </dd>
<dt><code>.break</code></dt>
<dd> <p> Break out of a while loop. See also the <code>while</code> and <code>continue</code> requests. Be sure not to confuse this with the <code>br</code> request. </p>
 </dd>
<dt><code>.brp</code></dt>
<dd> <p> This is the same as <code>\p</code>. </p>
 </dd>
<dt><code>.cflags&nbsp;</code><i>n c1 c2 </i></dt>
<dd> <p> Characters <i>c1</i>, <i>c2</i>, <i></i>, have properties determined by <i>n</i>, which is ORed from the following: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>1</dt>
<dd> <p> The character ends sentences (initially characters <code>.?!</code> have this property). </p>
 </dd>
<dt>2</dt>
<dd> <p> Lines can be broken before the character (initially no characters have this property); a line is not broken at a character with this property unless the characters on each side both have non-zero hyphenation codes. This can be overridden with value 64. </p>
 </dd>
<dt>4</dt>
<dd> <p> Lines can be broken after the character (initially characters <code>-\[hy]\[em]</code> have this property); a line is not broken at a character with this property unless the characters on each side both have non-zero hyphenation codes. This can be overridden with value 64. </p>
 </dd>
<dt>8</dt>
<dd> <p> The glyph associated with this character overlaps horizontally (initially characters <code>\[ul]\[rn]\[ru]\[radicalex]\[sqrtex]</code> have this property). </p>
 </dd>
<dt>16</dt>
<dd> <p> The glyph associated with this character overlaps vertically (initially glyph <code>\[br]</code> has this property). </p>
 </dd>
<dt>32</dt>
<dd> <p> An end-of-sentence character followed by any number of characters with this property is treated as the end of a sentence if followed by a newline or two spaces; in other words the character is transparent for the purposes of end-of-sentence recognition; this is the same as having a zero space factor in TeX (initially characters <code>&quot;&#8216;)]*\[dg]\[rq]\[cq]</code> have this property). </p>
 </dd>
<dt>64</dt>
<dd> <p> Ignore hyphenation code values of the surrounding characters. Use this in combination with values 2 and~4 (initially no characters have this property). </p>
 </dd>
<dt>128</dt>
<dd> <p> Prohibit a line break before the character, but allow a line break after the character. This works only in combination with flags 256 and 512 and has no effect otherwise. </p>
 </dd>
<dt>256</dt>
<dd> <p> Prohibit a line break after the character, but allow a line break before the character. This works only in combination with flags 128 and 512 and has no effect otherwise. </p>
 </dd>
<dt>512</dt>
<dd> <p> Allow line break before or after the character. This works only in combination with flags 128 and 256 and has no effect otherwise. </p>
 </dd></dl>
</dl>
<dd> <p> Contrary to flag values 2 and~4, the flags 128, 256, and 512 work pairwise. If, for example, the left character has value 512, and the right character 128, no line break gets inserted. If we use value~6 instead for the left character, a line break after the character can&#8217;t be suppressed since the right neighbour character doesn&#8217;t get examined. </p>
 </dd>
<dt><code>.char&nbsp;</code><i>c string</i></dt>
<dd> <p> [This request can both define characters and glyphs.] </p>
 </dd>
<dd> <p> Define entity~<i>c</i> to be <i>string</i>. To be more precise, define (or even override) a groff entity which can be accessed with name~<i>c</i> on the input side, and which uses <i>string</i> on the output side. Every time glyph~<i>c</i> needs to be printed, <i>string</i> is processed in a temporary environment and the result is wrapped up into a single object. Compatibility mode is turned off and the escape character is set to~<code>\</code> while <i>string</i> is being processed. Any emboldening, constant spacing or track kerning is applied to this object rather than to individual glyphs in <i>string</i>. </p>
 </dd>
<dd> <p> A groff object defined by this request can be used just like a normal glyph provided by the output device. In particular other characters can be translated to it with the <code>tr</code> request; it can be made the leader glyph by the <code>lc</code> request; repeated patterns can be drawn with the glyph using the <code>\l</code> and <code>\L</code> escape sequences; words containing~<i>c</i> can be hyphenated correctly, if the <code>hcode</code> request is used to give the object a hyphenation code. </p>
 </dd>
<dd> <p> There is a special anti-recursion feature: Use of glyph within the glyph&#8217;s definition is handled like normal glyphs not defined with <code>char</code>. </p>
 </dd>
<dd> <p> A glyph definition can be removed with the <code>rchar</code> request. </p>
 </dd>
<dt><code>.chop&nbsp;</code><i>xx</i></dt>
<dd> <p> Chop the last element off macro, string, or diversion <i>xx</i>. This is useful for removing the newline from the end of diversions that are to be interpolated as strings. </p>
 </dd>
<dt><code>.class&nbsp;</code><i>name c1 c2 </i></dt>
<dd> <p> Assign <i>name</i> to a set of characters <i>c1</i>, <i>c2</i>, <i></i>, so that they can be referred to from other requests easily (currently <code>.cflags</code> only). Character ranges (indicated by an intermediate &#8216;-&#8216;) and nested classes are possible also. This is useful to assign properties to a large set of characters. </p>
 </dd>
<dt><code>.close&nbsp;</code><i>stream</i></dt>
<dd> <p> Close the stream named <i>stream</i>; <i>stream</i> will no longer be an acceptable argument to the <code>write</code> request. See the <code>open</code> request. </p>
 </dd>
<dt><code>.composite&nbsp;</code><i>glyph1 glyph2</i></dt>
<dd> <p> Map glyph name <i>glyph1</i> to glyph name <i>glyph2</i> if it is used in <code>\[</code><i></i><code>]</code> with more than one component. </p>
 </dd>
<dt><code>.continue</code></dt>
<dd> <p> Finish the current iteration of a while loop. See also the <code>while</code> and <code>break</code> requests. </p>
 </dd>
<dt><code>.color&nbsp;</code><i>n</i></dt>
<dd> <p> If <i>n</i> is non-zero or missing, enable colors (this is the default), otherwise disable them. </p>
 </dd>
<dt><code>.cp&nbsp;</code><i>n</i></dt>
<dd> <p> If <i>n</i> is non-zero or missing, enable compatibility mode, otherwise disable it. In compatibility mode, long names are not recognized, and the incompatibilities caused by long names do not arise. </p>
 </dd>
<dt><code>.defcolor&nbsp;</code><i>xxx scheme color_components</i></dt>
<dd> <p> Define color <i>xxx</i>. <i>scheme</i> can be one of the following values: <code>rgb</code> (three components), <code>cmy</code> (three components), <code>cmyk</code> (four components), and <code>gray</code> or <code>grey</code> (one component). Color components can be given either as a hexadecimal string or as positive decimal integers in the range 0-65535. A hexadecimal string contains all color components concatenated; it must start with either <code>#</code> or <code>##</code>. The former specifies hex values in the range 0-255 (which are internally multiplied by~257), the latter in the range 0-65535. Examples: #FFC0CB (pink), ##ffff0000ffff (magenta). A new scaling indicator~<code>f</code> has been introduced which multiplies its value by~65536; this makes it convenient to specify color components as fractions in the range 0 to~1. Example: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <p> .defcolor darkgreen rgb 0.1f 0.5f 0.2f </p>
 </dd></dl>
</dl>
<dd> <p> Note that <code>f</code> is the default scaling indicator for the <code>defcolor</code> request, thus the above statement is equivalent to </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <p> .defcolor darkgreen rgb 0.1 0.5 0.2 </p>
 </dd></dl>
</dl>
<dd> <p> The color named <code>default</code> (which is device-specific) can&#8217;t be redefined. It is possible that the default color for <code>\M</code> and <code>\m</code> is not the same. </p>
 </dd>
<dt><code>.de1&nbsp;</code><i>xx yy</i></dt>
<dd> <p> Similar to <code>.de</code>, but compatibility mode is switched off during execution. On entry, the current compatibility mode is saved and restored at exit. </p>
 </dd>
<dt><code>.dei&nbsp;</code><i>xx yy</i></dt>
<dd> <p> Define macro indirectly. The following example </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <p> .ds xx aa .ds yy bb .dei xx yy </p>
 </dd></dl>
</dl>
<dd> <p> is equivalent to </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <p> .de aa bb </p>
 </dd></dl>
</dl>
<dt><code>.dei1&nbsp;</code><i>xx yy</i></dt>
<dd> <p> Similar to the <code>dei</code> request but compatibility mode is switched off during execution. </p>
 </dd>
<dt><code>.device&nbsp;</code><i>anything</i></dt>
<dd> <p> This is (almost) the same as the <code>\X</code> escape. <i>anything</i> is read in copy mode; a leading~<code>&quot;</code> is stripped. </p>
 </dd>
<dt><code>.devicem&nbsp;</code><i>xx</i></dt>
<dd> <p> This is the same as the <code>\Y</code> escape (to embed the contents of a macro into the intermediate output preceded with &#8216;x~X&#8217;). </p>
 </dd>
<dt><code>.do&nbsp;</code><i>xxx</i></dt>
<dd> <p> Interpret <i>.xxx</i> with compatibility mode disabled. For example, </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <p> .do fam T </p>
 </dd></dl>
<p>would have the same effect as </p>
<dl>
<dd> <p> .fam T </p>
 </dd></dl>
<p>except that it would work even if compatibility mode had been enabled. Note that the previous compatibility mode is restored before any files sourced by <i>xxx</i> are interpreted. </dl>
 </p>
<dt><code>.ds1&nbsp;</code><i>xx yy</i></dt>
<dd> <p> Similar to <code>.ds</code>, but compatibility mode is switched off during expansion. To be more precise, a &#8216;compatibility save&#8217; token is inserted at the beginning of the string, and a &#8216;compatibility restore&#8217; token at the end. </p>
 </dd>
<dt><code>.ecs</code></dt>
<dd> <p> Save current escape character. </p>
 </dd>
<dt><code>.ecr</code></dt>
<dd> <p> Restore escape character saved with <code>ecs</code>. Without a previous call to <code>ecs</code>, &#8216;<code>\</code>&#8216; will be the new escape character. </p>
 </dd>
<dt><code>.evc&nbsp;</code><i>xx</i></dt>
<dd> <p> Copy the contents of environment <i>xx</i> to the current environment. No pushing or popping of environments is done. </p>
 </dd>
<dt><code>.fam&nbsp;</code><i>xx</i></dt>
<dd> <p> Set the current font family to <i>xx</i>. The current font family is part of the current environment. If <i>xx</i> is missing, switch back to previous font family. The value at start-up is &#8216;T&#8217;. See the description of the <code>sty</code> request for more information on font families. </p>
 </dd>
<dt><code>.fchar&nbsp;</code><i>c string</i></dt>
<dd> <p> Define fallback character (or glyph)~<i>c</i> to be <i>string</i>. The syntax of this request is the same as the <code>char</code> request; the only difference is that a glyph defined with <code>char</code> hides the glyph with the same name in the current font, whereas a glyph defined with <code>fchar</code> is checked only if the particular glyph isn&#8217;t found in the current font. This test happens before checking special fonts. </p>
 </dd>
<dt><code>.fcolor&nbsp;</code><i>c</i></dt>
<dd> <p> Set the fill color to~<i>c</i>. If <i>c</i> is missing, switch to the previous fill color. </p>
 </dd>
<dt><code>.fschar&nbsp;</code><i>f c string</i></dt>
<dd> <p> Define fallback character (or glyph)~<i>c</i> for font~<i>f</i> to be <i>string</i>. The syntax of this request is the same as the <code>char</code> request (with an additional argument to specify the font); a glyph defined with <code>fschar</code> is searched after the list of fonts declared with the <code>fspecial</code> request but before the list of fonts declared with <code>.special</code>. </p>
 </dd>
<dt><code>.fspecial&nbsp;</code><i>f s1 s2 </i></dt>
<dd> <p> When the current font is~<i>f</i>, fonts <i>s1</i>, <i>s2</i>, <i></i>, are special, that is, they are searched for glyphs not in the current font. Any fonts specified in the <code>special</code> request are searched after fonts specified in the <code>fspecial</code> request. Without argument, reset the list of global special fonts to be empty. </p>
 </dd>
<dt><code>.ftr&nbsp;</code><i>f g</i></dt>
<dd> <p> Translate font~<i>f</i> to~<i>g</i>. Whenever a font named~<i>f</i> is referred to in an <code>\f</code> escape sequence, in the <code>F</code> and <code>S</code> conditional operators, or in the <code>ft</code>, <code>ul</code>, <code>bd</code>, <code>cs</code>, <code>tkf</code>, <code>special</code>, <code>fspecial</code>, <code>fp</code>, or <code>sty</code> requests, font~<i>g</i> is used. If <i>g</i> is missing, or equal to~<i>f</i> then font~<i>f</i> is not translated. </p>
 </dd>
<dt><code>.fzoom&nbsp;</code><i>f zoom</i></dt>
<dd> <p> Set zoom factor <i>zoom</i> for font~<i>f</i>. <i>zoom</i> must a non-negative integer multiple of 1/1000th. If it is missing or is equal to zero, it means the same as 1000, namely no magnification. <i>f</i>~must be a real font name, not a style. </p>
 </dd>
<dt><code>.gcolor&nbsp;</code><i>c</i></dt>
<dd> <p> Set the glyph color to~<i>c</i>. If <i>c</i> is missing, switch to the previous glyph color. </p>
 </dd>
<dt><code>.hcode&nbsp;</code><i>c1 code1 c2 code2 </i></dt>
<dd> <p> Set the hyphenation code of character <i>c1</i> to <i>code1</i> and that of <i>c2</i> to <i>code2</i>, and so on. A hyphenation code must be a single input character (not a special character) other than a digit or a space. Initially each lower-case letter a-z has a hyphenation code, which is itself, and each upper-case letter A-Z has a hyphenation code which is the lower-case version of itself. See also the <code>hpf</code> request. </p>
 </dd>
<dt><code>.hla&nbsp;</code><i>lang</i></dt>
<dd> <p> Set the current hyphenation language to <i>lang</i>. Hyphenation exceptions specified with the <code>hw</code> request and hyphenation patterns specified with the <code>hpf</code> request are both associated with the current hyphenation language. The <code>hla</code> request is usually invoked by the <code>troffrc</code> file to set up a default language. </p>
 </dd>
<dt><code>.hlm&nbsp;</code><i>n</i></dt>
<dd> <p> Set the maximum number of consecutive hyphenated lines to~<i>n</i>. If <i>n</i> is negative, there is no maximum. The default value is~-1. This value is associated with the current environment. Only lines output from an environment count towards the maximum associated with that environment. Hyphens resulting from <code>\%</code> are counted; explicit hyphens are not. </p>
 </dd>
<dt><code>.hpf&nbsp;</code><i>file</i></dt>
<dd> <p> Read hyphenation patterns from <i>file</i>; this is searched for in the same way that <i>name</i><code>.tmac</code> is searched for when the <code>-m</code><i>name</i> option is specified. It should have the same format as (simple) TeX patterns files. More specifically, the following scanning rules are implemented. </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> A percent sign starts a comment (up to the end of the line) even if preceded by a backslash. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> No support for &#8216;digraphs&#8217; like <code>\$</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>^^</code><i>xx</i> (<i>x</i> is 0-9 or a-f) and <code>^^</code><i>x</i> (character code of~<i>x</i> in the range 0-127) are recognized; other use of~<code>^</code> causes an error. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> No macro expansion. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>hpf</code> checks for the expression <code>\patterns{</code><code>}</code> (possibly with whitespace before and after the braces). Everything between the braces is taken as hyphenation patterns. Consequently, <code>{</code>~and~<code>}</code> are not allowed in patterns. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Similarly, <code>\hyphenation{</code><code>}</code> gives a list of hyphenation exceptions. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>\endinput</code> is recognized also. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> For backwards compatibility, if <code>\patterns</code> is missing, the whole file is treated as a list of hyphenation patterns (only recognizing the <code>%</code>~character as the start of a comment). </p>
 </dd></dl>
</dl>
<dd> <p> Use the <code>hpfcode</code> request to map the encoding used in hyphenation patterns files to <code>groff</code>&#8216;s input encoding. By default, everything maps to itself except letters &#8216;A&#8217; to &#8216;Z&#8217; which map to &#8216;a&#8217; to &#8216;z&#8217;. </p>
 </dd>
<dd> <p> The set of hyphenation patterns is associated with the current language set by the <code>hla</code> request. The <code>hpf</code> request is usually invoked by the <code>troffrc</code> file; a second call replaces the old patterns with the new ones. </p>
 </dd>
<dt><code>.hpfa&nbsp;</code><i>file</i></dt>
<dd> <p> The same as <code>hpf</code> except that the hyphenation patterns from <i>file</i> are appended to the patterns already loaded in the current language. </p>
 </dd>
<dt><code>.hpfcode&nbsp;</code><i>a b c d </i></dt>
<dd> <p> After reading a hyphenation patterns file with the <code>hpf</code> or <code>hpfa</code> request, convert all characters with character code~<i>a</i> in the recently read patterns to character code~<i>b</i>, character code~<i>c</i> to~<i>d</i>, etc. Initially, all character codes map to themselves. The arguments of <code>hpfcode</code> must be integers in the range 0 to~255. Note that it is even possible to use character codes which are invalid in <code>groff</code> otherwise. </p>
 </dd>
<dt><code>.hym&nbsp;</code><i>n</i></dt>
<dd> <p> Set the <i>hyphenation margin</i> to~<i>n</i>: when the current adjustment mode is not~<code>b</code>, the line is not hyphenated if the line is no more than <i>n</i> short. The default hyphenation margin is~0. The default scaling indicator for this request is~<code>m</code>. The hyphenation margin is associated with the current environment. The current hyphenation margin is available in the <code>\n[.hym]</code> register. </p>
 </dd>
<dt><code>.hys&nbsp;</code><i>n</i></dt>
<dd> <p> Set the <i>hyphenation space</i> to~<i>n</i>: When the current adjustment mode is~<code>b</code> don&#8217;t hyphenate the line if the line can be justified by adding no more than <i>n</i> extra space to each word space. The default hyphenation space is~0. The default scaling indicator for this request is~<code>m</code>. The hyphenation space is associated with the current environment. The current hyphenation space is available in the <code>\n[.hys]</code> register. </p>
 </dd>
<dt><code>.itc&nbsp;</code><i>n macro</i></dt>
<dd> <p> Variant of <code>.it</code> for which a line interrupted with <code>\c</code> is not counted as an input line. </p>
 </dd>
<dt><code>.kern&nbsp;</code><i>n</i></dt>
<dd> <p> If <i>n</i> is non-zero or missing, enable pairwise kerning, otherwise disable it. </p>
 </dd>
<dt><code>.length&nbsp;</code><i>xx string</i></dt>
<dd> <p> Compute the length of <i>string</i> and return it in the number register <i>xx</i> (which is not necessarily defined before). </p>
 </dd>
<dt><code>.linetabs&nbsp;</code><i>n</i></dt>
<dd> <p> If <i>n</i> is non-zero or missing, enable line-tabs mode, otherwise disable it (which is the default). In line-tabs mode, tab distances are computed relative to the (current) output line. Otherwise they are taken relative to the input line. For example, the following </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <p> .ds x a\t\c .ds y b\t\c .ds z c .ta 1i 3i \*x \*y \*z </p>
 </dd></dl>
</dl>
<dd> <p> yields </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <p> a b c </p>
 </dd></dl>
</dl>
<dd> <p> In line-tabs mode, the same code gives </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <p> a b c </p>
 </dd></dl>
</dl>
<dd> <p> Line-tabs mode is associated with the current environment; the read-only number register <code>\n[.linetabs]</code> is set to~1 if in line-tabs mode, and 0 otherwise. </p>
 </dd>
<dt><code>.lsm&nbsp;</code><i>xx</i></dt>
<dd> <p> Set the leading spaces macro to <i>xx</i>. If there are leading spaces in an input line, it is invoked instead of the usual troff behaviour; the leading spaces are removed. Registers <code>\n[lsn]</code> and <code>\n[lss]</code> hold the number of removed leading spaces and the corresponding horizontal space, respectively. </p>
 </dd>
<dt><code>.mso&nbsp;</code><i>file</i></dt>
<dd> <p> The same as the <code>so</code> request except that <i>file</i> is searched for in the same directories as macro files for the <code>-m</code> command-line option. If the file name to be included has the form <i>name</i><code>.tmac</code> and it isn&#8217;t found, <code>mso</code> tries to include <code>tmac.</code><i>name</i> instead and vice versa. A warning of type <code>file</code> is generated if <i>file</i> can&#8217;t be loaded, and the request is ignored. </p>
 </dd>
<dt><code>.nop</code><i>&nbsp;anything</i></dt>
<dd> <p> Execute <i>anything</i>. This is similar to &#8216;.if 1&#8217;. </p>
 </dd>
<dt><code>.nroff</code></dt>
<dd> <p> Make the <code>n</code> built-in condition true and the <code>t</code> built-in condition false. This can be reversed using the <code>troff</code> request. </p>
 </dd>
<dt><code>.open&nbsp;</code><i>stream filename</i></dt>
<dd> <p> Open <i>filename</i> for writing and associate the stream named <i>stream</i> with it. See also the <code>close</code> and <code>write</code> requests. </p>
 </dd>
<dt><code>.opena&nbsp;</code><i>stream filename</i></dt>
<dd> <p> Like <code>open</code>, but if <i>filename</i> exists, append to it instead of truncating it. </p>
 </dd>
<dt><code>.output&nbsp;</code><i>string</i></dt>
<dd> <p> Emit <i>string</i> directly to the intermediate output (subject to copy-mode interpretation); this is similar to <code>\!</code> used at the top level. An initial double quote in <i>string</i> is stripped off to allow initial blanks. </p>
 </dd>
<dt><code>.pev</code></dt>
<dd> <p> Print the current environment and each defined environment state on stderr. </p>
 </dd>
<dt><code>.pnr</code></dt>
<dd> <p> Print the names and contents of all currently defined number registers on stderr. </p>
 </dd>
<dt><code>.psbb</code><i>&nbsp;filename</i></dt>
<dd> <p> Get the bounding box of a PostScript image <i>filename</i>. This file must conform to Adobe&#8217;s Document Structuring Conventions; the command looks for a <code>%%BoundingBox</code> comment to extract the bounding box values. After a successful call, the coordinates (in PostScript units) of the lower left and upper right corner can be found in the registers <code>\n[llx]</code>, <code>\n[lly]</code>, <code>\n[urx]</code>, and <code>\n[ury]</code>, respectively. If some error has occurred, the four registers are set to zero. </p>
 </dd>
<dt><code>.pso</code><i>&nbsp;command</i></dt>
<dd> <p> This behaves like the <code>so</code> request except that input comes from the standard output of <i>command</i>. </p>
 </dd>
<dt><code>.ptr</code></dt>
<dd> <p> Print the names and positions of all traps (not including input line traps and diversion traps) on stderr. Empty slots in the page trap list are printed as well, because they can affect the priority of subsequently planted traps. </p>
 </dd>
<dt><code>.pvs</code><i>&nbsp;&plusmn;n</i></dt>
<dd> <p> Set the post-vertical line space to~<i>n</i>; default scale indicator is~<code>p</code>. This value is added to each line after it has been output. With no argument, the post-vertical line space is set to its previous value. </p>
 </dd>
<dd> <p> The total vertical line spacing consists of four components: <code>.vs</code> and <code>\x</code> with a negative value which are applied before the line is output, and <code>.pvs</code> and <code>\x</code> with a positive value which are applied after the line is output. </p>
 </dd>
<dt><code>.rchar&nbsp;</code><i>c1 c2 </i></dt>
<dd> <p> Remove the definitions of glyphs <i>c1</i>, <i>c2</i>, <i>&nbsp;This undoes the effect of a</i> <code>char</code> request. </p>
 </dd>
<dt><code>.return</code></dt>
<dd> <p> Within a macro, return immediately. If called with an argument, return twice, namely from the current macro and from the macro one level higher. No effect otherwise. </p>
 </dd>
<dt><code>.rfschar&nbsp;</code><i>c1 c2 </i></dt>
<dd> <p> Remove the font-specific definitions of glyphs <i>c1</i>, <i>c2</i>, <i>&nbsp;This undoes the effect of an</i> <code>fschar</code> request. </p>
 </dd>
<dt><code>.rj</code></dt>
<dd> <p> <code>.rj</code><i>~n</i> Right justify the next <i>n</i>~input lines. Without an argument right justify the next input line. The number of lines to be right justified is available in the <code>\n[.rj]</code> register. This implicitly does <code>.ce~0</code>. The <code>ce</code> request implicitly does <code>.rj~0</code>. </p>
 </dd>
<dt><code>.rnn</code><i>&nbsp;xx yy</i></dt>
<dd> <p> Rename number register <i>xx</i> to <i>yy</i>. </p>
 </dd>
<dt><code>.schar&nbsp;</code><i>c string</i></dt>
<dd> <p> Define global fallback character (or glyph)~<i>c</i> to be <i>string</i>. The syntax of this request is the same as the <code>char</code> request; a glyph defined with <code>schar</code> is searched after the list of fonts declared with the <code>special</code> request but before the mounted special fonts. </p>
 </dd>
<dt><code>.shc&nbsp;</code><i>c</i></dt>
<dd> <p> Set the soft hyphen character to~<i>c</i>. If <i>c</i> is omitted, the soft hyphen character is set to the default <code>\[hy]</code>. The soft hyphen character is the glyph which is inserted when a word is hyphenated at a line break. If the soft hyphen character does not exist in the font of the glyph immediately preceding a potential break point, then the line is not broken at that point. Neither definitions (specified with the <code>char</code> request) nor translations (specified with the <code>tr</code> request) are considered when finding the soft hyphen character. </p>
 </dd>
<dt><code>.shift&nbsp;</code><i>n</i></dt>
<dd> <p> In a macro, shift the arguments by <i>n</i> positions: argument~<i>i</i> becomes argument <i>i</i>-<i>n</i>; arguments 1 to~<i>n</i> are no longer available. If <i>n</i> is missing, arguments are shifted by~1. Shifting by negative amounts is currently undefined. </p>
 </dd>
<dt><code>.sizes&nbsp;</code><i>s1 s2&nbsp;<wbr>&nbsp;sn&nbsp;</i><code>[0]</code></dt>
<dd> <p> This command is similar to the <code>sizes</code> command of a <i>DESC</i> file. It sets the available font sizes for the current font to <i>s1</i>, <i>s2</i>, <i></i>,~<i>sn</i> scaled points. The list of sizes can be terminated by an optional~<code>0</code>. Each <i>si</i> can also be a range of sizes <i>m</i>-<i>n</i>. Contrary to the font file command, the list can&#8217;t extend over more than a single line. </p>
 </dd>
<dt><code>.special&nbsp;</code><i>s1 s2 </i></dt>
<dd> <p> Fonts <i>s1</i>, <i>s2</i>, <i></i>, are special and are searched for glyphs not in the current font. Without arguments, reset the list of special fonts to be empty. </p>
 </dd>
<dt><code>.spreadwarn&nbsp;</code><i>limit</i></dt>
<dd> <p> Make <code>troff</code> emit a warning if the additional space inserted for each space between words in an output line is larger or equal to <i>limit</i>. A negative value is changed to zero; no argument toggles the warning on and off without changing <i>limit</i>. The default scaling indicator is~<code>m</code>. At startup, <code>spreadwarn</code> is deactivated, and <i>limit</i> is set to 3m. For example, <code>.spreadwarn 0.2m</code> causes a warning if <code>troff</code> must add 0.2m or more for each interword space in a line. This request is active only if text is justified to both margins (using <code>.ad b</code>). </p>
 </dd>
<dt><code>.sty&nbsp;</code><i>n f</i></dt>
<dd> <p> Associate style~<i>f</i> with font position~<i>n</i>. A font position can be associated either with a font or with a style. The current font is the index of a font position and so is also either a font or a style. When it is a style, the font that is actually used is the font the name of which is the concatenation of the name of the current family and the name of the current style. For example, if the current font is~1 and font position~1 is associated with style~<code>R</code> and the current font family is~<code>T</code>, then font <code>TR</code> is used. If the current font is not a style, then the current family is ignored. When the requests <code>cs</code>, <code>bd</code>, <code>tkf</code>, <code>uf</code>, or <code>fspecial</code> are applied to a style, then they are applied instead to the member of the current family corresponding to that style. The default family can be set with the <code>-f</code> command-line option. The <code>styles</code> command in the DESC file controls which font positions (if any) are initially associated with styles rather than fonts. </p>
 </dd>
<dt><code>.substring&nbsp;</code><i>xx n1&nbsp;</i><code>[</code><i>n2</i><code>]</code></dt>
<dd> <p> Replace the string named <i>xx</i> with the substring defined by the indices <i>n1</i> and <i>n2</i>. The first character in the string has index~0. If <i>n2</i> is omitted, it is taken to be equal to the string&#8217;s length. If the index value <i>n1</i> or <i>n2</i> is negative, it is counted from the end of the string, going backwards: The last character has index~-1, the character before the last character has index~-2, etc. </p>
 </dd>
<dt><code>.tkf&nbsp;</code><i>f s1 n1 s2 n2</i></dt>
<dd> <p> Enable track kerning for font~<i>f</i>. When the current font is~<i>f</i> the width of every glyph is increased by an amount between <i>n1</i> and <i>n2</i>; when the current point size is less than or equal to <i>s1</i> the width is increased by <i>n1</i>; when it is greater than or equal to <i>s2</i> the width is increased by <i>n2</i>; when the point size is greater than or equal to <i>s1</i> and less than or equal to <i>s2</i> the increase in width is a linear function of the point size. </p>
 </dd>
<dt><code>.tm1&nbsp;</code><i>string</i></dt>
<dd> <p> Similar to the <code>tm</code> request, <i>string</i> is read in copy mode and written on the standard error, but an initial double quote in <i>string</i> is stripped off to allow initial blanks. </p>
 </dd>
<dt><code>.tmc&nbsp;</code><i>string</i></dt>
<dd> <p> Similar to <code>tm1</code> but without writing a final newline. </p>
 </dd>
<dt><code>.trf&nbsp;</code><i>filename</i></dt>
<dd> <p> Transparently output the contents of file <i>filename</i>. Each line is output as if preceded by <code>\!</code>; however, the lines are not subject to copy-mode interpretation. If the file does not end with a newline, then a newline is added. For example, you can define a macro~<i>x</i> containing the contents of file~<i>f</i>, using </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <p> .di x .trf f .di </p>
 </dd></dl>
</dl>
<dd> <p> Unlike with the <code>cf</code> request, the file cannot contain characters, such as NUL, that are not valid troff input characters. </p>
 </dd>
<dt><code>.trin&nbsp;</code><i>abcd</i></dt>
<dd> <p> This is the same as the <code>tr</code> request except that the <code>asciify</code> request uses the character code (if any) before the character translation. Example: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <p> .trin ax .di xxx a .br .di .xxx .trin aa .asciify xxx .xxx </p>
 </dd></dl>
</dl>
<dd> <p> The result is <code>x a</code>. Using <code>tr</code>, the result would be <code>x x</code>. </p>
 </dd>
<dt><code>.trnt&nbsp;</code><i>abcd</i></dt>
<dd> <p> This is the same as the <code>tr</code> request except that the translations do not apply to text that is transparently throughput into a diversion with <code>\!</code>. For example, </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <p> .tr ab .di x \!.tm a .di .x </p>
 </dd></dl>
</dl>
<dd> <p> prints~<code>b</code>; if <code>trnt</code> is used instead of <code>tr</code> it prints~<code>a</code>. </p>
 </dd>
<dt><code>.troff</code></dt>
<dd> <p> Make the <code>n</code> built-in condition false, and the <code>t</code> built-in condition true. This undoes the effect of the <code>nroff</code> request. </p>
 </dd>
<dt><code>.unformat&nbsp;</code><i>xx</i></dt>
<dd> <p> This request &#8216;unformats&#8217; the diversion <i>xx</i>. Contrary to the <code>asciify</code> request, which tries to convert formatted elements of the diversion back to input tokens as much as possible, <code>.unformat</code> only handles tabs and spaces between words (usually caused by spaces or newlines in the input) specially. The former are treated as if they were input tokens, and the latter are stretchable again. Note that the vertical size of lines is not preserved. Glyph information (font, font size, space width, etc.) is retained. Useful in conjunction with the <code>box</code> and <code>boxa</code> requests. </p>
 </dd>
<dt><code>.vpt&nbsp;</code><i>n</i></dt>
<dd> <p> Enable vertical position traps if <i>n</i> is non-zero, disable them otherwise. Vertical position traps are traps set by the <code>wh</code> or <code>dt</code> requests. Traps set by the <code>it</code> request are not vertical position traps. The parameter that controls whether vertical position traps are enabled is global. Initially vertical position traps are enabled. </p>
 </dd>
<dt><code>.warn&nbsp;</code><i>n</i></dt>
<dd> <p> Control warnings. <i>n</i>~is the sum of the numbers associated with each warning that is to be enabled; all other warnings are disabled. The number associated with each warning is listed in <code><a href="/docs/linux/man/1-troff/">troff</a></code>(1). For example, <code>.warn~0</code> disables all warnings, and <code>.warn~1</code> disables all warnings except that about missing glyphs. If <i>n</i> is not given, all warnings are enabled. </p>
 </dd>
<dt><code>.warnscale&nbsp;</code><i>si</i></dt>
<dd> <p> Set the scaling indicator used in warnings to <i>si</i>. Valid values for <i>si</i> are <code>u</code>, <code>i</code>, <code>c</code>, <code>p</code>, and~<code>P</code>. At startup, it is set to~<code>i</code>. </p>
 </dd>
<dt><code>.while</code><i>&nbsp;c anything</i></dt>
<dd> <p> While condition~<i>c</i> is true, accept <i>anything</i> as input; <i>c</i>~can be any condition acceptable to an <code>if</code> request; <i>anything</i> can comprise multiple lines if the first line starts with <code>\{</code> and the last line ends with <code>\}</code>. See also the <code>break</code> and <code>continue</code> requests. </p>
 </dd>
<dt><code>.write&nbsp;</code><i>stream anything</i></dt>
<dd> <p> Write <i>anything</i> to the stream named <i>stream</i>. <i>stream</i> must previously have been the subject of an <code>open</code> request. <i>anything</i> is read in copy mode; a leading~<code>&quot;</code> is stripped. </p>
 </dd>
<dt><code>.writec&nbsp;</code><i>stream anything</i></dt>
<dd> <p> Similar to <code>write</code> but without writing a final newline. </p>
 </dd>
<dt><code>.writem&nbsp;</code><i>stream xx</i></dt>
<dd> <p> Write the contents of the macro or string <i>xx</i> to the stream named <i>stream</i>. <i>stream</i> must previously have been the subject of an <code>open</code> request. <i>xx</i> is read in copy mode. </p>
 </dd></dl>
<h3>Extended escape sequences</h3>
<dl>
<dt><code>\D&#8217;</code><code>&#8216;</code></dt>
<dd> <p> All drawing commands of groff&#8217;s intermediate output are accepted. See subsection "Drawing Commands" below. </p>
 </dd></dl>
<h3>Extended requests</h3>
<dl>
<dt><code>.cf&nbsp;</code><i>filename</i></dt>
<dd> <p> When used in a diversion, this embeds in the diversion an object which, when reread, will cause the contents of <i>filename</i> to be transparently copied through to the output. In Unix troff, the contents of <i>filename</i> is immediately copied through to the output regardless of whether there is a current diversion; this behaviour is so anomalous that it must be considered a bug. </p>
 </dd>
<dt><code>.de&nbsp;</code><i>xx yy</i></dt>
<dd> <p> <code>.am&nbsp;</code><i>xx yy</i> <code>.ds&nbsp;</code><i>xx yy</i> <code>.as&nbsp;</code><i>xx yy</i> In compatibility mode, these requests behaves similar to <code>.de1</code>, <code>.am1</code>, <code>.ds1</code>, and <code>.as1</code>, respectively: A &#8216;compatibility save&#8217; token is inserted at the beginning, and a &#8216;compatibility restore&#8217; token at the end, with compatibility mode switched on during execution. </p>
 </dd>
<dt><code>.ev&nbsp;</code><i>xx</i></dt>
<dd> <p> If <i>xx</i> is not a number, this switches to a named environment called <i>xx</i>. The environment should be popped with a matching <code>ev</code> request without any arguments, just as for numbered environments. There is no limit on the number of named environments; they are created the first time that they are referenced. </p>
 </dd>
<dt><code>.hy&nbsp;</code><i>n</i></dt>
<dd> <p> New additive values 16 and~32 are available; the former enables hyphenation before the last character, the latter enables hyphenation after the first character. </p>
 </dd>
<dt><code>.ss&nbsp;</code><i>m n</i></dt>
<dd> <p> When two arguments are given to the <code>ss</code> request, the second argument gives the <i>sentence space size</i>. If the second argument is not given, the sentence space size is the same as the word space size. Like the word space size, the sentence space is in units of one twelfth of the spacewidth parameter for the current font. Initially both the word space size and the sentence space size are~12. Contrary to Unix troff, GNU troff handles this request in nroff mode also; a given value is then rounded down to the nearest multiple of~12. The sentence space size is used in two circumstances. If the end of a sentence occurs at the end of a line in fill mode, then both an inter-word space and a sentence space are added; if two spaces follow the end of a sentence in the middle of a line, then the second space is a sentence space. Note that the behaviour of Unix troff is exactly that exhibited by GNU troff if a second argument is never given to the <code>ss</code> request. In GNU troff, as in Unix troff, you should always follow a sentence with either a newline or two spaces. </p>
 </dd>
<dt><code>.ta&nbsp;</code><i>n1 n2 nn </i><code>T </code><i>r1 r2 rn</i></dt>
<dd> <p> Set tabs at positions <i>n1</i>, <i>n2</i>, <i></i>, <i>nn</i> and then set tabs at <i>nn</i>+<i>r1</i>, <i>nn</i>+<i>r2</i>, <i></i>, <i>nn</i>+<i>rn</i> and then at <i>nn</i>+<i>rn</i>+<i>r1</i>, <i>nn</i>+<i>rn</i>+<i>r2</i>, <i></i>, <i>nn</i>+<i>rn</i>+<i>rn</i>, and so on. For example, </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <p> .ta T .5i </p>
 </dd></dl>
<p>sets tabs every half an inch. </dl>
 </dl>
  </p>
<h3>New number registers</h3>
<p> The following read-only registers are available: </p>
<dl>
<dt><code>\n[.br]</code></dt>
<dd> <p> Within a macro call, it is set to~1 if the macro is called with the &#8216;normal&#8217; control character (&#8216;.&#8216; by default), and set to~0 otherwise. This allows the reliable modification of requests. </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <p> .als bp*orig bp .de bp .tm before bp .ie \\n[.br] .bp*orig .el &#8216;bp*orig .tm after bp .. </p>
 </dd></dl>
</dl>
<dd> <p> Using this register outside of a macro makes no sense (it always returns zero in such cases). </p>
 </dd>
<dt><code>\n[.C]</code></dt>
<dd> <p> 1~if compatibility mode is in effect, 0~otherwise. </p>
 </dd>
<dt><code>\n[.cdp]</code></dt>
<dd> <p> The depth of the last glyph added to the current environment. It is positive if the glyph extends below the baseline. </p>
 </dd>
<dt><code>\n[.ce]</code></dt>
<dd> <p> The number of lines remaining to be centered, as set by the <code>ce</code> request. </p>
 </dd>
<dt><code>\n[.cht]</code></dt>
<dd> <p> The height of the last glyph added to the current environment. It is positive if the glyph extends above the baseline. </p>
 </dd>
<dt><code>\n[.color]</code></dt>
<dd> <p> 1~if colors are enabled, 0~otherwise. </p>
 </dd>
<dt><code>\n[.csk]</code></dt>
<dd> <p> The skew of the last glyph added to the current environment. The <i>skew</i> of a glyph is how far to the right of the center of a glyph the center of an accent over that glyph should be placed. </p>
 </dd>
<dt><code>\n[.ev]</code></dt>
<dd> <p> The name or number of the current environment. This is a string-valued register. </p>
 </dd>
<dt><code>\n[.fam]</code></dt>
<dd> <p> The current font family. This is a string-valued register. </p>
 </dd>
<dt><code>\n[.fn]</code></dt>
<dd> <p> The current (internal) real font name. This is a string-valued register. If the current font is a style, the value of <code>\n[.fn]</code> is the proper concatenation of family and style name. </p>
 </dd>
<dt><code>\n[.fp]</code></dt>
<dd> <p> The number of the next free font position. </p>
 </dd>
<dt><code>\n[.g]</code></dt>
<dd> <p> Always~1. Macros should use this to determine whether they are running under GNU troff. </p>
 </dd>
<dt><code>\n[.height]</code></dt>
<dd> <p> The current height of the font as set with <code>\H</code>. </p>
 </dd>
<dt><code>\n[.hla]</code></dt>
<dd> <p> The current hyphenation language as set by the <code>hla</code> request. </p>
 </dd>
<dt><code>\n[.hlc]</code></dt>
<dd> <p> The number of immediately preceding consecutive hyphenated lines. </p>
 </dd>
<dt><code>\n[.hlm]</code></dt>
<dd> <p> The maximum allowed number of consecutive hyphenated lines, as set by the <code>hlm</code> request. </p>
 </dd>
<dt><code>\n[.hy]</code></dt>
<dd> <p> The current hyphenation flags (as set by the <code>hy</code> request). </p>
 </dd>
<dt><code>\n[.hym]</code></dt>
<dd> <p> The current hyphenation margin (as set by the <code>hym</code> request). </p>
 </dd>
<dt><code>\n[.hys]</code></dt>
<dd> <p> The current hyphenation space (as set by the <code>hys</code> request). </p>
 </dd>
<dt><code>\n[.in]</code></dt>
<dd> <p> The indentation that applies to the current output line. </p>
 </dd>
<dt><code>\n[.int]</code></dt>
<dd> <p> Set to a positive value if last output line is interrupted (i.e., if it contains <code>\c</code>). </p>
 </dd>
<dt><code>\n[.kern]</code></dt>
<dd> <p> 1~if pairwise kerning is enabled, 0~otherwise. </p>
 </dd>
<dt><code>\n[.lg]</code></dt>
<dd> <p> The current ligature mode (as set by the <code>lg</code> request). </p>
 </dd>
<dt><code>\n[.linetabs]</code></dt>
<dd> <p> The current line-tabs mode (as set by the <code>linetabs</code> request). </p>
 </dd>
<dt><code>\n[.ll]</code></dt>
<dd> <p> The line length that applies to the current output line. </p>
 </dd>
<dt><code>\n[.lt]</code></dt>
<dd> <p> The title length as set by the <code>lt</code> request. </p>
 </dd>
<dt><code>\n[.m]</code></dt>
<dd> <p> The name of the current drawing color. This is a string-valued register. </p>
 </dd>
<dt><code>\n[.M]</code></dt>
<dd> <p> The name of the current background color. This is a string-valued register. </p>
 </dd>
<dt><code>\n[.ne]</code></dt>
<dd> <p> The amount of space that was needed in the last <code>ne</code> request that caused a trap to be sprung. Useful in conjunction with the <code>\n[.trunc]</code> register. </p>
 </dd>
<dt><code>\n[.ns]</code></dt>
<dd> <p> 1~if no-space mode is active, 0~otherwise. </p>
 </dd>
<dt><code>\n[.O]</code></dt>
<dd> <p> The current output level as set with <code>\O</code>. </p>
 </dd>
<dt><code>\n[.P]</code></dt>
<dd> <p> 1~if the current page is in the output list set with <code>-o</code>. </p>
 </dd>
<dt><code>\n[.pe]</code></dt>
<dd> <p> 1~during a page ejection caused by the <code>bp</code> request, 0~otherwise. </p>
 </dd>
<dt><code>\n[.pn]</code></dt>
<dd> <p> The number of the next page, either the value set by a <code>pn</code> request, or the number of the current page plus~1. </p>
 </dd>
<dt><code>\n[.ps]</code></dt>
<dd> <p> The current point size in scaled points. </p>
 </dd>
<dt><code>\n[.psr]</code></dt>
<dd> <p> The last-requested point size in scaled points. </p>
 </dd>
<dt><code>\n[.pvs]</code></dt>
<dd> <p> The current post-vertical line space as set with the <code>pvs</code> request. </p>
 </dd>
<dt><code>\n[.rj]</code></dt>
<dd> <p> The number of lines to be right-justified as set by the <code>rj</code> request. </p>
 </dd>
<dt><code>\n[.slant]</code></dt>
<dd> <p> The slant of the current font as set with <code>\S</code>. </p>
 </dd>
<dt><code>\n[.sr]</code></dt>
<dd> <p> The last requested point size in points as a decimal fraction. This is a string-valued register. </p>
 </dd>
<dt><code>\n[.ss]</code></dt>
<dd> <p> <code>\n[.sss]</code> These give the values of the parameters set by the first and second arguments of the <code>ss</code> request. </p>
 </dd>
<dt><code>\n[.sty]</code></dt>
<dd> <p> The current font style. This is a string-valued register. </p>
 </dd>
<dt><code>\n[.tabs]</code></dt>
<dd> <p> A string representation of the current tab settings suitable for use as an argument to the <code>ta</code> request. </p>
 </dd>
<dt><code>\n[.trunc]</code></dt>
<dd> <p> The amount of vertical space truncated by the most recently sprung vertical position trap, or, if the trap was sprung by an <code>ne</code> request, minus the amount of vertical motion produced by the <code>ne</code> request. In other words, at the point a trap is sprung, it represents the difference of what the vertical position would have been but for the trap, and what the vertical position actually is. Useful in conjunction with the <code>\n[.ne]</code> register. </p>
 </dd>
<dt><code>\n[.U]</code></dt>
<dd> <p> Set to~1 if in safer mode and to~0 if in unsafe mode (as given with the <code>-U</code> command-line option). </p>
 </dd>
<dt><code>\n[.vpt]</code></dt>
<dd> <p> 1~if vertical position traps are enabled, 0~otherwise. </p>
 </dd>
<dt><code>\n[.warn]</code></dt>
<dd> <p> The sum of the numbers associated with each of the currently enabled warnings. The number associated with each warning is listed in <code><a href="/docs/linux/man/1-troff/">troff</a></code>(1). </p>
 </dd>
<dt><code>\n[.x]</code></dt>
<dd> <p> The major version number. For example, if the version number is 1.03, then <code>\n[.x]</code> contains~1. </p>
 </dd>
<dt><code>\n[.y]</code></dt>
<dd> <p> The minor version number. For example, if the version number is 1.03, then <code>\n[.y]</code> contains~03. </p>
 </dd>
<dt><code>\n[.Y]</code></dt>
<dd> <p> The revision number of groff. </p>
 </dd>
<dt><code>\n[.zoom]</code></dt>
<dd> <p> The zoom value of the current font, in multiples of 1/1000th. Zero if no magnification. </p>
 </dd>
<dt><code>\n[llx]</code></dt>
<dd> <p> <code>\n[lly]</code> <code>\n[urx]</code> <code>\n[ury]</code> These four read/:write registers are set by the <code>psbb</code> request and contain the bounding box values (in PostScript units) of a given PostScript image. </p>
 </dd></dl>
<p>The following read/:write registers are set by the <code>\w</code> escape sequence: </p>
<dl>
<dt><code>\n[rst]</code></dt>
<dd> <p> <code>\n[rsb]</code> Like the <code>st</code> and <code>sb</code> registers, but take account of the heights and depths of glyphs. </p>
 </dd>
<dt><code>\n[ssc]</code></dt>
<dd> <p> The amount of horizontal space (possibly negative) that should be added to the last glyph before a subscript. </p>
 </dd>
<dt><code>\n[skw]</code></dt>
<dd> <p> How far to right of the center of the last glyph in the <code>\w</code> argument, the center of an accent from a roman font should be placed over that glyph. </p>
 </dd></dl>
<p>Other available read/write number registers are: </p>
<dl>
<dt><code>\n[c.]</code></dt>
<dd> <p> The current input line number. <code>\n[.c]</code> is a read-only alias to this register. </p>
 </dd>
<dt><code>\n[hours]</code></dt>
<dd> <p> The number of hours past midnight. Initialized at start-up. </p>
 </dd>
<dt><code>\n[hp]</code></dt>
<dd> <p> The current horizontal position at input line. </p>
 </dd>
<dt><code>\n[lsn]</code></dt>
<dd> <p> <code>\n[lss]</code> If there are leading spaces in an input line, these registers hold the number of leading spaces and the corresponding horizontal space, respectively. </p>
 </dd>
<dt><code>\n[minutes]</code></dt>
<dd> <p> The number of minutes after the hour. Initialized at start-up. </p>
 </dd>
<dt><code>\n[seconds]</code></dt>
<dd> <p> The number of seconds after the minute. Initialized at start-up. </p>
 </dd>
<dt><code>\n[systat]</code></dt>
<dd> <p> The return value of the system() function executed by the last <code>sy</code> request. </p>
 </dd>
<dt><code>\n[slimit]</code></dt>
<dd> <p> If greater than~0, the maximum number of objects on the input stack. If less than or equal to~0, there is no limit on the number of objects on the input stack. With no limit, recursion can continue until virtual memory is exhausted. </p>
 </dd>
<dt><code>\n[year]</code></dt>
<dd> <p> The current year. Note that the traditional <code>troff</code> number register <code>\n[yr]</code> is the current year minus 1900. </p>
 </dd></dl>
<h3>Miscellaneous</h3>
<p> <code>troff</code> predefines a single (read/write) string-based register, <code>\*[.T]</code>, which contains the argument given to the <code>-T</code> command-line option, namely the current output device (for example, <i>latin1</i> or <i>ascii</i>). Note that this is not the same as the (read-only) number register <code>\n[.T]</code> which is defined to be~1 if <code>troff</code> is called with the <code>-T</code> command-line option, and zero otherwise. This behaviour is different from Unix troff. </p>
<p>Fonts not listed in the DESC file are automatically mounted on the next available font position when they are referenced. If a font is to be mounted explicitly with the <code>fp</code> request on an unused font position, it should be mounted on the first unused font position, which can be found in the <code>\n[.fp]</code> register; although <code>troff</code> does not enforce this strictly, it does not allow a font to be mounted at a position whose number is much greater than that of any currently used position. </p>
<p>Interpolating a string does not hide existing macro arguments. Thus in a macro, a more efficient way of doing </p>
<dl>
<dd> <p> <code>.</code><i>xx&nbsp;</i><code>\\$@</code> </p>
 </dd></dl>
<p>is </p>
<dl>
<dd> <p> <code>\\*[</code><i>xx</i><code>]\\</code> </p>
 </dd></dl>
<p>If the font description file contains pairwise kerning information, glyphs from that font are kerned. Kerning between two glyphs can be inhibited by placing a <code>\&amp;</code> between them. </p>
<p>In a string comparison in a condition, characters that appear at different input levels to the first delimiter character are not recognized as the second or third delimiters. This applies also to the <code>tl</code> request. In a <code>\w</code> escape sequence, a character that appears at a different input level to the starting delimiter character is not recognized as the closing delimiter character. The same is true for <code>\A</code>, <code>\b</code>, <code>\B</code>, <code>\C</code>, <code>\l</code>, <code>\L</code>, <code>\o</code>, <code>\X</code>, and <code>\Z</code>. When decoding a macro or string argument that is delimited by double quotes, a character that appears at a different input level to the starting delimiter character is not recognized as the closing delimiter character. The implementation of <code>\$@</code> ensures that the double quotes surrounding an argument appear at the same input level, which is different to the input level of the argument itself. In a long escape name <code>]</code> is not recognized as a closing delimiter except when it occurs at the same input level as the opening~<code>[</code>. In compatibility mode, no attention is paid to the input-level. </p>
<p>There are some new types of condition: </p>
<dl>
<dt><code>.if r</code><i>xxx</i></dt>
<dd> <p> True if there is a number register named <i>xxx</i>. </p>
 </dd>
<dt><code>.if d</code><i>xxx</i></dt>
<dd> <p> True if there is a string, macro, diversion, or request named <i>xxx</i>. </p>
 </dd>
<dt><code>.if m</code><i>xxx</i></dt>
<dd> <p> True if there is a color named <i>xxx</i>. </p>
 </dd>
<dt><code>.if c</code><i>ch</i></dt>
<dd> <p> True if there is a character (or glyph) <i>ch</i> available; <i>ch</i> is either an ASCII character or a glyph (special character) <code>\N&#8217;</code><i>xxx</i><code>&#8216;</code>, <code>\(</code><i>xx</i> or <code>\[</code><i>xxx</i><code>]</code>; the condition is also true if <i>ch</i> has been defined by the <code>char</code> request. </p>
 </dd>
<dt><code>.if F</code><i>f</i></dt>
<dd> <p> True if font~<i>f</i> exists. <code>f</code>~is handled as if it was opened with the <code>ft</code> request (this is, font translation and styles are applied), without actually mounting it. </p>
 </dd>
<dt><code>.if S</code><i>s</i></dt>
<dd> <p> True if style~<i>s</i> has been registered. Font translation is applied. </p>
 </dd></dl>
<p>The <code>tr</code> request can now map characters onto <code>\~</code>. </p>
<p>The space width emitted by the <code>\|</code> and <code>\^</code> escape sequences can be controlled on a per-font basis. If there is a glyph named <code>\|</code> or <code>\^</code>, respectively (note the leading backslash), defined in the current font file, use this glyph&#8217;s width instead of the default value. </p>
<p>It is now possible to have whitespace between the first and second dot (or the name of the ending macro) to end a macro definition. Example: </p>
<dl>
<dd> <p> .if t \{\ . de bar . nop Hello, I&#8217;m &#8216;bar&#8217;. . . .\} </p>
 </dd></dl>
<h2>INTERMEDIATE OUTPUT FORMAT</h2>
<p> This section describes the format output by GNU troff. The output format used by GNU troff is very similar to that used by Unix device-independent troff. Only the differences are documented here.  </p>
<h3>Units</h3>
<p> The argument to the <code>s</code>~command is in scaled points (units of points/<i>n</i>, where <i>n</i> is the argument to the <code>sizescale</code> command in the DESC file). The argument to the <code>x Height</code> command is also in scaled points.  </p>
<h3>Text Commands</h3>
<dl>
<dt><code>N</code><i>n</i></dt>
<dd> <p> Print glyph with index~<i>n</i> (a non-negative integer) of the current font. </p>
 </dd></dl>
<p>If the <code>tcommand</code> line is present in the DESC file, troff uses the following two commands. </p>
<dl>
<dt><code>t</code><i>xxx</i></dt>
<dd> <p> <i>xxx</i> is any sequence of characters terminated by a space or a newline (to be more precise, it is a sequence of glyphs which are accessed with the corresponding characters); the first character should be printed at the current position, the current horizontal position should be increased by the width of the first character, and so on for each character. The width of the glyph is that given in the font file, appropriately scaled for the current point size, and rounded so that it is a multiple of the horizontal resolution. Special characters cannot be printed using this command. </p>
 </dd>
<dt><code>u</code><i>n xxx</i></dt>
<dd> <p> This is same as the <code>t</code>~command except that after printing each character, the current horizontal position is increased by the sum of the width of that character and~<i>n</i>. </p>
 </dd></dl>
<p>Note that single characters can have the eighth bit set, as can the names of fonts and special characters. </p>
<p>The names of glyphs and fonts can be of arbitrary length; drivers should not assume that they are only two characters long. </p>
<p>When a glyph is to be printed, that glyph is always in the current font. Unlike device-independent troff, it is not necessary for drivers to search special fonts to find a glyph. </p>
<p>For color support, some new commands have been added: </p>
<dl>
<dt>mc cyan magenta yellow</dt>
<dd> <p> md mg gray mk cyan magenta yellow black mr red green blue Set the color components of the current drawing color, using various color schemes. <code>md</code> resets the drawing color to the default value. The arguments are integers in the range 0 to 65536. </p>
 </dd></dl>
<p>The <code>x</code>~device control command has been extended. </p>
<dl>
<dt>x u n</dt>
<dd> <p> If <i>n</i> is~1, start underlining of spaces. If <i>n</i> is~0, stop underlining of spaces. This is needed for the <code>cu</code> request in nroff mode and is ignored otherwise. </p>
 </dd></dl>
<h3>Drawing Commands</h3>
<p> The <code>D</code> drawing command has been extended. These extensions are not used by GNU pic if the <code>-n</code> option is given. </p>
<dl>
<dt>Df n/\n</dt>
<dd> <p> Set the shade of gray to be used for filling solid objects to <i>n</i>; <i>n</i> must be an integer between 0 and 1000, where 0 corresponds solid white and 1000 to solid black, and values in between correspond to intermediate shades of gray. This applies only to solid circles, solid ellipses and solid polygons. By default, a level of 1000 is used. Whatever color a solid object has, it should completely obscure everything beneath it. A value greater than 1000 or less than~0 can also be used: this means fill with the shade of gray that is currently being used for lines and text. Normally this is black, but some drivers may provide a way of changing this. </p>
 </dd>
<dd> <p> The corresponding <code>\D&#8217;f</code><i></i><code>&#8216;</code> command shouldn&#8217;t be used since its argument is always rounded to an integer multiple of the horizontal resolution which can lead to surprising results. </p>
 </dd>
<dt>DC /d\n</dt>
<dd> <p> Draw a solid circle with a diameter of <i>d</i> with the leftmost point at the current position. </p>
 </dd>
<dt>DE dx dy/\n</dt>
<dd> <p> Draw a solid ellipse with a horizontal diameter of <i>dx</i> and a vertical diameter of <i>dy</i> with the leftmost point at the current position. delim $$ </p>
 </dd>
<dt>Dp $dx sub 1$ $dy sub 1$ $dx sub 2$ $dy sub 2$ $...$ $dx sub n$ $dy sub n$\n</dt>
<dd> <p> Draw a polygon with, for $i = 1 ,..., n+1$, the <i>i</i>-th vertex at the current position $+ sum from j=1 to i-1 ( dx sub j , dy sub j )$. At the moment, GNU pic only uses this command to generate triangles and rectangles. </p>
 </dd>
<dt>DP $dx sub 1$ $dy sub 1$ $dx sub 2$ $dy sub 2$ $...$ $dx sub n$ $dy sub n$\n</dt>
<dd> <p> Like <code>Dp</code> but draw a solid rather than outlined polygon. </p>
 </dd>
<dt>Dt n/\n</dt>
<dd> <p> Set the current line thickness to <i>n</i>~machine units. Traditionally Unix troff drivers use a line thickness proportional to the current point size; drivers should continue to do this if no <code>Dt</code> command has been given, or if a <code>Dt</code> command has been given with a negative value of~<i>n</i>. A zero value of~<i>n</i> selects the smallest available line thickness. </p>
 </dd></dl>
<p>A difficulty arises in how the current position should be changed after the execution of these commands. This is not of great importance since the code generated by GNU pic does not depend on this. Given a drawing command of the form </p>
<dl>
<dd> <p> \D&#8217;c $x sub 1$ $y sub 1$ $x sub 2$ $y sub 2$ $...$ $x sub n$ $y sub n$&#8216; </p>
 </dd></dl>
<p>where <i>c</i> is not one of <code>c</code>, <code>e</code>, <code>l</code>, <code>a</code>, or~<code>~</code>, Unix troff treats each of the $x sub i$ as a horizontal quantity, and each of the $y sub i$ as a vertical quantity and assumes that the width of the drawn object is $sum from i=1 to n x sub i$, and that the height is $sum from i=1 to n y sub i$. (The assumption about the height can be seen by examining the <code>st</code> and <code>sb</code> registers after using such a <code>D</code>~command in a <code>\w</code> escape sequence). This rule also holds for all the original drawing commands with the exception of <code>De</code>. For the sake of compatibility GNU troff also follows this rule, even though it produces an ugly result in the case of the <code>Dt</code> and <code>Df</code>, and, to a lesser extent, <code>DE</code> commands. Thus after executing a <code>D</code>~command of the form </p>
<dl>
<dd> <p> Dc $x sub 1$ $y sub 1$ $x sub 2$ $y sub 2$ $...$ $x sub n$ $y sub n$\n </p>
 </dd></dl>
<p>the current position should be increased by $( sum from i=1 to n x sub i , sum from i=1 to n y sub i )$. </p>
<p>Another set of extensions is </p>
<dl>
<dt>DFc cyan magenta yellow\n</dt>
<dd> <p> DFd\n DFg gray/\n DFk cyan magenta yellow black\n DFr red green blue\n Set the color components of the filling color similar to the <code>m</code>~commands above. </p>
 </dd></dl>
<p>The current position isn&#8217;t changed by those colour commands (contrary to <code>Df</code>).  </p>
<h3>Device Control Commands</h3>
<p> There is a continuation convention which permits the argument to the <code>x X</code> command to contain newlines: when outputting the argument to the <code>x X</code> command, GNU troff follows each newline in the argument with a <code>+</code> character (as usual, it terminates the entire argument with a newline); thus if the line after the line containing the <code>x X</code> command starts with <code>+</code>, then the newline ending the line containing the <code>x X</code> command should be treated as part of the argument to the <code>x X</code> command, the <code>+</code> should be ignored, and the part of the line following the <code>+</code> should be treated like the part of the line following the <code>x X</code> command. </p>
<p>The first three output commands are guaranteed to be: </p>
<dl>
<dd> <p> <code>x T&nbsp;</code><i>device</i> <br />
 <code>x res&nbsp;</code><i>n h v</i> <br />
 <code>x init</code> </p>
 </dd></dl>
<h2>INCOMPATIBILITIES</h2>
<p> In spite of the many extensions, groff has retained compatibility to classical troff to a large degree. For the cases where the extensions lead to collisions, a special compatibility mode with the restricted, old functionality was created for groff.  </p>
<h3>Groff Language</h3>
<p> <i>groff</i> provides a <code>compatibility mode</code> that allows the processing of roff code written for classical <code>troff</code> or for other implementations of roff in a consistent way. </p>
<p>Compatibility mode can be turned on with the <code>-C</code> command-line option, and turned on or off with the <code>.cp</code> request. The number register <code>\n(.C</code> is~1 if compatibility mode is on, 0~otherwise. </p>
<p>This became necessary because the GNU concept for long names causes some incompatibilities. <i>Classical troff</i> interprets </p>
<dl>
<dd> <p> <code>.dsabcd</code> </p>
 </dd></dl>
<p>as defining a string <code>ab</code> with contents <code>cd</code>. In <i>groff</i> mode, this is considered as a call of a macro named <code>dsabcd</code>. </p>
<p>Also <i>classical troff</i> interprets <code>\*[</code> or <code>\n[</code> as references to a string or number register called~<code>[</code> while <i>groff</i> takes this as the start of a long name. </p>
<p>In <i>compatibility mode</i>, groff interprets these things in the traditional way; so long names are not recognized. </p>
<p>On the other hand, groff in <i>GNU native mode</i> does not allow to use the single-character escapes <code>\\</code> (backslash), <code>\|</code> (vertical bar), <code>\ha</code> (caret), <code>\&amp;</code> (ampersand), <code>\{</code> (opening brace), <code>\}</code> (closing brace), &#8216;<code>\&nbsp;</code>&#8216; (space), <code>\&#8216;</code> (single quote), <code>\`</code> (backquote), <code>\-</code> (minus), <code>\_</code> (underline), <code>\!</code> (bang), <code>\%</code> (percent), and <code>\c</code> (character~c) in names of strings, macros, diversions, number registers, fonts or environments, whereas <i>classical troff</i> does. </p>
<p>The <code>\A</code> escape sequence can be helpful in avoiding these escape sequences in names. </p>
<p>Fractional point sizes cause one noteworthy incompatibility. In <i>classical</i> <i>troff</i>, the <code>ps</code> request ignores scale indicators and so </p>
<dl>
<dd> <p> <code>.ps~10u</code> </p>
 </dd></dl>
<p>sets the point size to 10~points, whereas in groff native mode the point size is set to 10~scaled points. </p>
<p>In <i>groff</i>, there is a fundamental difference between unformatted input characters, and formatted output characters (glyphs). Everything that affects how a glyph is output is stored with the glyph; once a glyph has been constructed it is unaffected by any subsequent requests that are executed, including the <code>bd</code>, <code>cs</code>, <code>tkf</code>, <code>tr</code>, or <code>fp</code> requests. </p>
<p>Normally glyphs are constructed from input characters at the moment immediately before the glyph is added to the current output line. Macros, diversions and strings are all, in fact, the same type of object; they contain lists of input characters and glyphs in any combination. </p>
<p>Special characters can be both; before being added to the output, they act as input entities, afterwards they denote glyphs. </p>
<p>A glyph does not behave like an input character for the purposes of macro processing; it does not inherit any of the special properties that the input character from which it was constructed might have had. The following example makes things clearer. </p>
<dl>
<dd> <p> .di x \\\\ .br .di .x </p>
 </dd></dl>
<p>With <i>GNU troff</i> this is printed as <code>\\</code>. So each pair of input backslashes &#8216;\\&#8216; is turned into a single output backslash glyph &#8216;\&#8216; and the resulting output backslashes are not interpreted as escape characters when they are reread. </p>
<p> <i>Classical troff</i> would interpret them as escape characters when they were reread and would end up printing a single backslash &#8216;\&#8216;. </p>
<p>In GNU, the correct way to get a printable version of the backslash character &#8216;\&#8216; is the <code>\(rs</code> escape sequence, but classical troff does not provide a clean feature for getting a non-syntactical backslash. A close method is the printable version of the current escape character using the <code>\e</code> escape sequence; this works if the current escape character is not redefined. It works in both GNU mode and compatibility mode, while dirty tricks like specifying a sequence of multiple backslashes do not work reliably; for the different handling in diversions, macro definitions, or text mode quickly leads to a confusion about the necessary number of backslashes. </p>
<p>To store an escape sequence in a diversion that is interpreted when the diversion is reread, either the traditional <code>\!</code> transparent output facility or the new <code>\?</code> escape sequence can be used.  </p>
<h3>Intermediate Output</h3>
<p> The groff intermediate output format is in a state of evolution. So far it has some incompatibilities, but it is intended to establish a full compatibility to the classical troff output format. Actually the following incompatibilities exist: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> The positioning after the drawing of the polygons conflicts with the classical definition. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The intermediate output cannot be rescaled to other devices as classical &#8216;device-independent&#8217; troff did. </p>
 </dd></dl>
<h2>AUTHORS</h2>
<p> This document was written by James Clark and modified by Werner Lemberg and Bernd Warken  </p>
<h2>SEE ALSO</h2>
<p> <i>Groff: The GNU Implementation of troff</i>, by Trent A. Fisher and Werner Lemberg, is the primary <i>groff</i> manual. You can browse it interactively with "info groff". </p>
<dl>
<dt><code><a href="/docs/linux/man/1-groff/">groff</a></code>(1) </dt>
<dd> <p> A list of all documentation around <i>groff</i>. </p>
 </dd>
<dt><code><a href="/docs/linux/man/7-groff/">groff</a></code>(7) </dt>
<dd> <p> A description of the <i>groff</i> language, including a short, but complete reference of all predefined requests, registers, and escapes of plain <i>groff</i>. From the command line, this is called using </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <p> man 7 groff </p>
 </dd></dl>
</dl>
<dt><code><a href="/docs/linux/man/7-roff/">roff</a></code>(7) </dt>
<dd> <p> A survey of <i>roff</i> systems, including pointers to further historical documentation. </p>
 </dd>
<dt>[<i>CSTR~#54/</i>] </dt>
<dd> <p> The <i>Nroff/:Troff User&#8217;s Manual</i> by <i>J. F. Ossanna</i> of 1976 in the revision of <i>Brian Kernighan</i> of 1992, being the classical troff documentation </p>
 </dd></dl>
