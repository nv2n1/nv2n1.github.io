---
title: "groff_me(7)"
name: "groff_me"
section: "7"
letter: "g"
url: "/docs/linux/man/7-groff_me/"
description: "groff_me – “me” macro package for formatting documents with GNU roff"
---

<p>groff_me &#8211; &#8220;me&#8221; macro package for formatting documents with GNU roff</p>
<h2>Synopsis</h2>
<p>[<i>option</i> &#8230;] [<i>input-file</i> &#8230;] [<i>option</i> &#8230;] [<i>input-file</i> &#8230;]</p>
<h2>Description</h2>
<p>The <i>me</i> package of macro definitions for the <i>roff</i> language provides a convenient facility for preparing technical papers in various formats. This manual page describes the GNU version of the <i>me</i> macros, which is part of the <i>groff</i> document formatting system. This version can be used with both GNU <i>troff</i> and Unix <i>troff</i>. </p>
<p> Many <i>roff</i> requests are unsafe in conjunction with this package; however, the following requests may be used with impunity after the first <code>.pp</code>: </p>
<table>
<tr VALIGN=top>
<td><code>.bp</code></td>
<td>begin new page
</td>
</tr>
<tr VALIGN=top>
<td><code>.br</code></td>
<td>break output line here
</td>
</tr>
<tr VALIGN=top>
<td><code>.sp</code> <i>n</i></td>
<td>insert <i>n</i> spacing lines
</td>
</tr>
<tr VALIGN=top>
<td><code>.ls</code> <i>n</i></td>
<td>(line spacing) <i>n</i>=1 single, <i>n</i>=2 double space
</td>
</tr>
<tr VALIGN=top>
<td><code>.na</code></td>
<td>no alignment of right margin
</td>
</tr>
<tr VALIGN=top>
<td><code>.ce</code> <i>n</i></td>
<td>center next <i>n</i> lines
</td>
</tr>
<tr VALIGN=top>
<td><code>.ul</code> <i>n</i></td>
<td>underline next <i>n</i> lines
</td>
</tr>
</table>
<p> <i>Note:</i> In contrast to its behavior with other macro packages and &#8220;raw&#8221; <i>roff</i>, when using the <i>me</i> package, the <code>.sp</code> request will <i>not</i> put space at the top of a page. </p>
<p> Output of the <i>pic</i>, <i>eqn</i>, <i>refer</i>, and <i>tbl</i> preprocessors is acceptable as input.</p>
<h3>Macro Reference</h3>
<p>Numeric arguments to macros are denoted with lowercase letters and string arguments with uppercase. An optional macro argument such as <i>x</i> appears in brackets, <code>[</code><i>x</i><code>/</code><code>]</code>. Note that arguments to macros generally must be quoted if they contain whitespace. An exception is the argument to header and footer macros, which require some explanation. They take the form &#8220;<i>c</i> <i>left c middle c right</i> <i>c</i>&#8220;, with spaces added here for clarity. The strings <i>left</i>, <i>middle</i>, and <i>right</i> correspond to their page placement and can contain unprotected whitespace, but must not contain the (non-space) character <i>c</i>, which delimits them. For brevity, the table presents header and footer arguments as <i>clcmcrc</i>. Popular choices for <i>c</i> are the ASCII apostrophe &#8220;<code>&#8216;</code>&#8221; and the ASCII double quote &#8220;<code>&quot;</code>&#8220;. </p>
<p> This list is incomplete; some requests are too complex to summarize in a table, and some that are listed below accept additional arguments not shown. See the <i>-me Reference Manual</i> for interesting details. </p>
<table>
<tr VALIGN=top>
<td>Request</td>
<td>Initial</td>
<td>Causes</td>
<td>Explanation
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Value</td>
<td>Break</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>.(c</td>
<td>&#8211;</td>
<td>yes</td>
<td> Begin centered block.
</td>
</tr>
<tr VALIGN=top>
<td>.(d</td>
<td>&#8211;</td>
<td>no</td>
<td> Begin delayed text.
</td>
</tr>
<tr VALIGN=top>
<td>.(f</td>
<td>&#8211;</td>
<td>no</td>
<td> Begin footnote.
</td>
</tr>
<tr VALIGN=top>
<td>.(l</td>
<td>&#8211;</td>
<td>yes</td>
<td>Begin list.
</td>
</tr>
<tr VALIGN=top>
<td>.(q</td>
<td>&#8211;</td>
<td>yes</td>
<td> Begin major quote.
</td>
</tr>
<tr VALIGN=top>
<td>.(x [<i>X</i>]</td>
<td>&#8211;</td>
<td>no</td>
<td> Begin item in index (named <i>X</i>).
</td>
</tr>
<tr VALIGN=top>
<td>.(z</td>
<td>&#8211;</td>
<td>no</td>
<td> Begin floating keep.
</td>
</tr>
<tr VALIGN=top>
<td>.)c</td>
<td>&#8211;</td>
<td>yes</td>
<td> End centered block.
</td>
</tr>
<tr VALIGN=top>
<td>.)d</td>
<td>&#8211;</td>
<td>yes</td>
<td> End delayed text.
</td>
</tr>
<tr VALIGN=top>
<td>.)f</td>
<td>&#8211;</td>
<td>yes</td>
<td> End footnote.
</td>
</tr>
<tr VALIGN=top>
<td>.)l</td>
<td>&#8211;</td>
<td>yes</td>
<td>End list.
</td>
</tr>
<tr VALIGN=top>
<td>.)q</td>
<td>&#8211;</td>
<td>yes</td>
<td> End major quote.
</td>
</tr>
<tr VALIGN=top>
<td>.)x</td>
<td>&#8211;</td>
<td>yes</td>
<td> End index item.
</td>
</tr>
<tr VALIGN=top>
<td>.)z</td>
<td>&#8211;</td>
<td>yes</td>
<td> End floating keep.
</td>
</tr>
<tr VALIGN=top>
<td>.++ <i>M</i> [<i>clcmcrc</i>]</td>
<td>&#8211;</td>
<td>no</td>
<td> Define paper section as <i>M</i>, which must be one of <code>C</code> (chapter), <code>A</code> (appendix), <code>P</code> (preliminary, i.e., front matter or table of contents), <code>AB</code> (abstract), <code>B</code> (bibliography), <code>RC</code> (chapters renumbered from page one each chapter), or <code>RA</code> (appendix renumbered from page one) (and set page header to <i>clcmcrc</i>).
</td>
</tr>
<tr VALIGN=top>
<td>.+c [<i>T</i>]</td>
<td>&#8211;</td>
<td>yes</td>
<td> Begin chapter (or appendix, etc., as set by <code>.++</code>) (with title <i>T</i>).
</td>
</tr>
<tr VALIGN=top>
<td>.1c</td>
<td>1</td>
<td>yes</td>
<td> One-column format on a new page.
</td>
</tr>
<tr VALIGN=top>
<td>.2c</td>
<td>1</td>
<td>yes</td>
<td> Two-column format.
</td>
</tr>
<tr VALIGN=top>
<td>.EN</td>
<td>&#8211;</td>
<td>yes</td>
<td> Space after equation produced by <i>eqn</i> or <i>neqn</i>.
</td>
</tr>
<tr VALIGN=top>
<td>.EQ [<i>M</i> [<i>T</i>]]</td>
<td>&#8211;</td>
<td>yes</td>
<td> Begin displayed equation (with indentation <i>M</i>, which must be one of <code>C</code> (centered, default), <code>I</code> (indented), or <code>L</code> (justified left) (and title <i>T</i> in right margin)).
</td>
</tr>
<tr VALIGN=top>
<td>.GE</td>
<td>&#8211;</td>
<td>yes</td>
<td> End <i>gremlin</i> picture.
</td>
</tr>
<tr VALIGN=top>
<td>.GS</td>
<td>&#8211;</td>
<td>yes</td>
<td> Begin <i>gremlin</i> picture.
</td>
</tr>
<tr VALIGN=top>
<td>.PE</td>
<td>&#8211;</td>
<td>yes</td>
<td> End <i>pic</i> picture.
</td>
</tr>
<tr VALIGN=top>
<td>.PS</td>
<td>&#8211;</td>
<td>yes</td>
<td> Begin <i>pic</i> picture.
</td>
</tr>
<tr VALIGN=top>
<td>.TE</td>
<td>&#8211;</td>
<td>yes</td>
<td> End <i>tbl</i> table.
</td>
</tr>
<tr VALIGN=top>
<td>.TH</td>
<td>&#8211;</td>
<td>yes</td>
<td> End heading of <i>tbl</i> table.
</td>
</tr>
<tr VALIGN=top>
<td>.TS [<code>H</code>]</td>
<td>&#8211;</td>
<td>yes</td>
<td> Begin <i>tbl</i> table; if <code>H</code>, table repeats heading on each page.
</td>
</tr>
<tr VALIGN=top>
<td>.b [<i>X</i> [<i>Y</i>]]</td>
<td>&#8211;</td>
<td>no</td>
<td> Print <i>X</i> in bold (appending <i>Y</i> in the previous font); if no arguments, switch to bold.
</td>
</tr>
<tr VALIGN=top>
<td>.ba <i>n</i></td>
<td>0</td>
<td>yes</td>
<td> Augment the base indent (for regular text, like paragraphs) by <i>n</i>.
</td>
</tr>
<tr VALIGN=top>
<td>.bc</td>
<td>&#8211;</td>
<td>yes</td>
<td> Begin new column.
</td>
</tr>
<tr VALIGN=top>
<td>.bi [<i>X</i> [<i>Y</i>]]</td>
<td>&#8211;</td>
<td>no</td>
<td> Print <i>X</i> in bold italics (appending <i>Y</i> in the previous font); if no arguments, switch to bold italics.
</td>
</tr>
<tr VALIGN=top>
<td>.bu</td>
<td>&#8211;</td>
<td>yes</td>
<td> Begin bulleted paragraph.
</td>
</tr>
<tr VALIGN=top>
<td>.bx [<i>X</i> [<i>Y</i>]]</td>
<td>&#8211;</td>
<td>no</td>
<td> Print <i>X</i> in a box (with Y appended). Renders reliably only in no-fill mode.
</td>
</tr>
<tr VALIGN=top>
<td>.ef <i>clcmcrc</i></td>
<td>&quot;&quot;&quot;&quot;</td>
<td>no</td>
<td> Set even-numbered page footer.
</td>
</tr>
<tr VALIGN=top>
<td>.eh <i>clcmcrc</i></td>
<td>&quot;&quot;&quot;&quot;</td>
<td>no</td>
<td> Set even-numbered page header.
</td>
</tr>
<tr VALIGN=top>
<td>.fo <i>clcmcrc</i></td>
<td>&quot;&quot;&quot;&quot;</td>
<td>no</td>
<td> Set page footer.
</td>
</tr>
<tr VALIGN=top>
<td>.hx</td>
<td>&#8211;</td>
<td>no</td>
<td> Suppress headers and footers on next page.
</td>
</tr>
<tr VALIGN=top>
<td>.he <i>clcmcrc</i></td>
<td>&quot;&quot;&quot;&quot;</td>
<td>no</td>
<td> Set page header.
</td>
</tr>
<tr VALIGN=top>
<td>.hl</td>
<td>&#8211;</td>
<td>yes</td>
<td> Draw a horizontal line.
</td>
</tr>
<tr VALIGN=top>
<td>.i [<i>X</i> [<i>Y</i>]]</td>
<td>&#8211;</td>
<td>no</td>
<td> Print <i>X</i> in italics (appending <i>Y</i> in the previous font); if no arguments, switch to italics.
</td>
</tr>
<tr VALIGN=top>
<td>.ip [<i>X</i> [<i>n</i>]]</td>
<td><i>n</i>=5n</td>
<td>yes</td>
<td> Start indented paragraph (with hanging tag <i>X</i> (and indentation <i>n</i>)).
</td>
</tr>
<tr VALIGN=top>
<td>.lp</td>
<td>&#8211;</td>
<td>yes</td>
<td> Begin paragraph with first line flush left.
</td>
</tr>
<tr VALIGN=top>
<td>.np</td>
<td>1</td>
<td>yes</td>
<td> Start numbered paragraph.
</td>
</tr>
<tr VALIGN=top>
<td>.of <i>clcmcrc</i></td>
<td>&quot;&quot;&quot;&quot;</td>
<td>no</td>
<td> Set odd-numbered page footer.
</td>
</tr>
<tr VALIGN=top>
<td>.oh <i>clcmcrc</i></td>
<td>&quot;&quot;&quot;&quot;</td>
<td>no</td>
<td> Set odd-numbered page header.
</td>
</tr>
<tr VALIGN=top>
<td>.pd</td>
<td>&#8211;</td>
<td>yes</td>
<td> Print delayed text.
</td>
</tr>
<tr VALIGN=top>
<td>.pp</td>
<td>&#8211;</td>
<td>yes</td>
<td> Begin paragraph with indented first line.
</td>
</tr>
<tr VALIGN=top>
<td>.r [<i>X</i> [<i>Y</i>]]</td>
<td>&#8211;</td>
<td>no</td>
<td> Print <i>X</i> in roman (appending <i>Y</i> in the previous font); if no arguments, switch to roman.
</td>
</tr>
<tr VALIGN=top>
<td>.re</td>
<td>0.5i</td>
<td>no</td>
<td> Reset tabs to default values.
</td>
</tr>
<tr VALIGN=top>
<td>.sh [<i>n</i> [<i>T</i>]]</td>
<td><i>n</i>=1</td>
<td>yes</td>
<td> Start numbered section; print section number (set to <i>n</i> (and title <i>T</i>)) in bold.
</td>
</tr>
<tr VALIGN=top>
<td>.sk</td>
<td>&#8211;</td>
<td>no</td>
<td> Leave the next page blank. Only one page is remembered ahead.
</td>
</tr>
<tr VALIGN=top>
<td>.sm <i>X</i> [<i>Y</i>]</td>
<td>&#8211;</td>
<td>no</td>
<td> Print <i>X</i> in a smaller point size (appending <i>Y</i> at the previous size).
</td>
</tr>
<tr VALIGN=top>
<td>.sz <i>n</i></td>
<td>10p</td>
<td>no</td>
<td> Augment the point size by <i>n</i> points.
</td>
</tr>
<tr VALIGN=top>
<td>.tp</td>
<td>&#8211;</td>
<td>yes</td>
<td> Begin title page.
</td>
</tr>
<tr VALIGN=top>
<td>.u <i>X</i> [<i>Y</i>]</td>
<td>&#8211;</td>
<td>no</td>
<td> Underline <i>X</i> (appending <i>Y</i> without underlining). Renders reliably only in no-fill mode.
</td>
</tr>
<tr VALIGN=top>
<td>.uh [<i>T</i>]</td>
<td>&#8211;</td>
<td>yes</td>
<td> Start unnumbered section (and print title <i>T</i> in bold).
</td>
</tr>
<tr VALIGN=top>
<td>.xp [<i>X</i>]</td>
<td>&#8211;</td>
<td>no</td>
<td> Print index (named <i>X</i>).
</td>
</tr>
</table>
<h2>Files</h2>
<p><i>/usr/:share/:groff/:1.22.4/:tmac/me.tmac</i> (a wrapper file for <i>e.tmac</i>)<br />
 <i>/usr/:share/:groff/:1.22.4/:tmac/e.tmac</i></p>
<h2>Notes</h2>
<p>Early <i>roff</i> macro packages limited themselves to a single-letter namespace (<i>mm</i>, <i>ms</i>, <i>mv</i>, <i>mn</i>, etc.). The &#8220;e&#8221; in &#8220;me&#8221; stands for &#8220;Eric P. Allman&#8221;, who wrote the macro package and the original technical papers documenting it while an undergraduate at the University of California.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-groff/">groff</a></code>(1), <code><a href="/docs/linux/man/1-troff/">troff</a></code>(1) Two manuals are available in source and rendered form. On your system, they may be compressed and/or available in additional formats.</p>
<dl>
<dt><i>/usr/:share/:doc/:groff-base/meintro.me</i></p>
<dd><i>/usr/:share/:doc/:groff-base/meintro.ps</i> is <i>Writing Papers with Groff Using -me</i>, by Eric P. Allman and James Clark.</p>
<dt><i>/usr/:share/:doc/:groff-base/meref.me</i></p>
<dd><i>/usr/:share/:doc/:groff-base/meref.ps</i> is the <i>-me Reference Manual</i>, by Eric P. Allman and James Clark.</dl>
<p> For preprocessors supported by <i>me</i>, see <code><a href="/docs/linux/man/1-eqn/">eqn</a></code>(1), <code><a href="/docs/linux/man/1-grn/">grn</a></code>(1), <code><a href="/docs/linux/man/1-pic/">pic</a></code>(1), <code><a href="/docs/linux/man/1-refer/">refer</a></code>(1), and <code><a href="/docs/linux/man/1-tbl/">tbl</a></code>(1). </p>
