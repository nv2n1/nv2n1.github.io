---
title: "groff_mom(7)"
name: "groff_mom"
section: "7"
letter: "g"
url: "/docs/linux/man/7-groff_mom/"
description: "groff_mom – groff “mom” macros; “mom” is a “roff” language, part of “groff”"
---

<p>groff_mom &#8211; groff &#8220;mom&#8221; macros; &#8220;mom&#8221; is a &#8220;roff&#8221; language, part of &#8220;groff&#8221;</p>
<h2>Synopsis</h2>
<p>[<code>-Tps</code> [<i>pdfroff-option</i> ]] [<i>groff-option</i> ] <i>file</i> <code>-mom</code> [<i>option</i> ] <i>file</i> <code>-m mom</code> [<i>option</i> ] <i>file</i></p>
<h2>Calling Mom</h2>
<p><code>mom</code> is a macro set for <code>groff</code>, designed primarily to format documents for <i>PDF</i> and <i>PostScript</i> output. </p>
<p> <code>mom</code> provides two categories of macros: macros for typesetting, and macros for document processing. The typesetting macros provide access to groff&#8217;s typesetting capabilities in ways that are simpler to master than groff&#8217;s primitives. The document processing macros provide highly customizable markup tags that allow the user to design and output professional-looking documents with a minimum of typesetting intervention. </p>
<p> Files processed with <code><a href="/docs/linux/man/1-pdfmom/">pdfmom</a></code>(1) with or without the -T<i>ps</i> option, produce <i>PDF</i> documents. The documents include a <i>PDF</i> outline that appears in the &#8216;Contents&#8217; panel of document viewers, and may contain clickable internal and external links. </p>
<p> When -T<i>ps</i> is absent, <code>groff&#8217;s</code> native <i>PDF</i> driver, <code>gropdf</code>, is used to generate the output. When given, the output is still <i>PDF</i>, but processing is passed over to <code>pdfroff</code>, which uses <code>groff&#8217;s</code> PostScript driver, <code>grops</code>. Not all <i>PDF</i> features are available when -T<i>ps</i> is given; its primary use is to allow processing of files with embedded <i>PostScript</i> images. </p>
<p> Files processed with <code>groff -mom</code> (or <code>-m </code><i>mom/</i>) produce <i>PostScript</i> output by default. </p>
<p> <code>mom</code> comes with her own very complete documentation in <i>HTML</i> format. A separate <i>PDF manual</i>, <i>Producing PDFs</i> with groff and <code>mom</code>, covers full <code>mom</code> or <i>PDF</i> usage.</p>
<h2>Files</h2>
<dl>
<dt><i>/usr/:share/:groff/:1.22.4/:tmac/:om.tmac</i></p>
<dd>&#8211; the main macro file <i>/usr/:share/:groff/:1.22.4/:tmac/:mom.tmac</i> &#8211; a wrapper file that calls om.tmac directly.</p>
<dt><i>/usr/:share/:doc/:groff-base/:html/:mom/:toc.html</i></p>
<dd>&#8211; entry point to the HTML documentation</p>
<dt><i>/usr/:share/:doc/:groff-base/:pdf/:mom-pdf.pdf</i></p>
<dd>&#8211; the PDF manual, <i>Producing PDFs with groff and mom</i></p>
<dt><i>/usr/:share/:doc/:groff-base/:examples/:mom/:</i>*<i>.mom</i></p>
<dd>&#8211; example files using mom</dl>
<h2>Documentation In Alphabetical Order</h2>
<p>This part of the man page contains information just as in <a href="/docs/linux/man/7-groff/">groff</a>(7), <i>mom macros</i> and <i>mom escape sequences</i> in alphabetical order. </p>
<p> The logical order of <i>mom macros</i> and <i>mom escape sequences</i> is very well documented in</p>
<dl>
<dt><i>/usr/:share/:doc/:groff-base/:html/:mom/:toc.html</i></p>
<dd>&#8211; entry point to the HTML documentation</dl>
<p> That document is quite good for beginners, but other users should be happy to have some documentation in reference style. </p>
<p> So we restrict this part to the alphabetical order of macros and escape sequences. But, so far, we took all documentation details from the <i>toc.html</i> file, just in a more useful alphabetical order. So this part of the man page is nothing new, but only a logical arrangement.</p>
<h2>Quick Reference</h2>
<h3>Quick Reference of Inline Escape Sequences in alphabetical Order</h3>
<dl>
<dd>begin using an initialized colour inline</p>
<dd>move backwards in a line</p>
<dt><code>\*[BOLDER]</code></p>
<dd>invoke pseudo bold inline (related to macro <code>.SETBOLDER</code>)</p>
<dt><code>\*[BOLDERX]</code></p>
<dd>off pseudo bold inline (related to macro <code>.SETBOLDER</code>)</p>
<dd>move characters pairs closer together inline (related to macro <code>.KERN</code>)</p>
<dt><code>\*[COND]</code></p>
<dd>invoke pseudo condensing inline (related to macro <code>.CONDENSE</code>)</p>
<dt><code>\*[CONDX]</code></p>
<dd>off pseudo condensing inline (related to macro <code>.CONDENSE</code>)</p>
<dd>pseudo-condensed superscript</p>
<dd>temporarily move downwards in a line</p>
<dt><code>\*[EN-MARK]</code></p>
<dd>mark initial line of a range of line numbers (for use with line numbered endnotes)</p>
<dt><code>\*[EXT]</code></p>
<dd>invoke pseudo extending inline (related to macro <code>.EXTEND</code>)</p>
<dt><code>\*[EXTX]</code></p>
<dd>off pseudo condensing inline (related to macro <code>.EXTEND</code>)</p>
<dd>pseudo extended superscript</p>
<dd>move characters pairs further apart inline (related to macro <code>.KERN</code>)</p>
<dd>move forward in a line</p>
<dt><code>\*[LEADER]</code></p>
<dd>insert leaders at the end of a line</p>
<dt><code>\*[RULE]</code></p>
<dd>draw a full measure rule</p>
<dd>change the point size inline (related to macro <code>.PT_SIZE</code>)</p>
<dt><code>\*[SLANT]</code></p>
<dd>invoke pseudo italic inline (related to macro <code>.SETSLANT</code>)</p>
<dt><code>\*[SLANTX]</code></p>
<dd>off pseudo italic inline (related to macro <code>.SETSLANT</code>)</p>
<dd>string tabs (mark tab positions inline)</p>
<dd>superscript</p>
<dt><code>\*[TB+]</code></p>
<dd>inline escape for <code>.TN</code> (<i>Tab Next</i>)</p>
<dd>invoke underlining inline (fixed width fonts only)</p>
<dd>temporarily move upwards in a line</dl>
<h3>Quick Reference of Macros in alphabetical Order</h3>
<dl>
<dt><code>.AUTOLEAD</code></p>
<dd>set the linespacing relative to the point size</p>
<dt><code>.B_MARGIN</code></p>
<dd>set a bottom margin</p>
<dt><code>.BR</code></p>
<dd>break a justified line</p>
<dt><code>.CENTER</code></p>
<dd>set line-by-line quad centre</p>
<dt><code>.CONDENSE</code></p>
<dd>set the amount to pseudo condense</p>
<dt><code>.EL</code></p>
<dd>break a line without advancing on the page</p>
<dt><code>.EXTEND</code></p>
<dd>set the amount to pseudo extend</p>
<dt><code>.FALLBACK_FONT</code></p>
<dd>establish a fallback font (for missing fonts)</p>
<dt><code>.FAM</code></p>
<dd>alias to <code>.FAMILY</code></p>
<dt><code>.FAMILY </code><i>&lt;family&gt;</i></p>
<dd>set the <i>family type</i></p>
<dt><code>.FT</code></p>
<dd>set the font style (roman, italic, etc.)</p>
<dt><code>.HI [</code><i> &lt;measure&gt; </i><code>]</code></p>
<dd>hanging indent</p>
<dt><code>.HY</code></p>
<dd>automatic hyphenation on/off</p>
<dt><code>.HY_SET</code></p>
<dd>set automatic hyphenation parameters</p>
<dt><code>.IB [</code><i> &lt;left measure&gt; &lt;right measure&gt; </i><code>]</code></p>
<dd>indent both</p>
<dt><code>.IBX [ CLEAR ]</code></p>
<dd>exit indent both</p>
<dt><code>.IL [</code><i> &lt;measure&gt; </i><code>]</code></p>
<dd>indent left</p>
<dt><code>.ILX [ CLEAR ]</code></p>
<dd>exit indent left</p>
<dt><code>.IQ [ CLEAR ]</code></p>
<dd>quit any/all indents</p>
<dt><code>.IR [</code><i> &lt;measure&gt; </i><code>]</code></p>
<dd>indent right</p>
<dt><code>.IRX [ CLEAR ]</code></p>
<dd>exit indent right</p>
<dt><code>.JUSTIFY</code></p>
<dd>justify text to both margins</p>
<dt><code>.KERN</code></p>
<dd>automatic character pair kerning on/off</p>
<dt><code>.L_MARGIN</code></p>
<dd>set a left margin (page offset)</p>
<dt><code>.LEFT</code></p>
<dd>set line-by-line quad left</p>
<dt><code>.LL</code></p>
<dd>set a line length</p>
<dt><code>.LS</code></p>
<dd>set a linespacing (leading)</p>
<dt><code>.PAGE</code></p>
<dd>set explicit page dimensions and margins</p>
<dt><code>.PAGEWIDTH</code></p>
<dd>set a custom page width</p>
<dt><code>.PAGELENGTH</code></p>
<dd>set a custom page length</p>
<dt><code>.PAPER</code><i> &lt;paper_type&gt;</i></p>
<dd>set common paper sizes (letter, A4, etc)</p>
<dt><code>.PT_SIZE</code></p>
<dd>set the point size</p>
<dt><code>.QUAD</code></p>
<dd>&quot;justify&quot; text left, centre, or right</p>
<dt><code>.R_MARGIN</code></p>
<dd>set a right margin</p>
<dt><code>.RIGHT</code></p>
<dd>set line-by-line quad right</p>
<dt><code>.SETBOLDER</code></p>
<dd>set the amount of emboldening</p>
<dt><code>.SETSLANT</code></p>
<dd>set the degree of slant</p>
<dt><code>.SPREAD</code></p>
<dd>force justify a line</p>
<dt><code>.SS</code></p>
<dd>set the sentence space size</p>
<dt><code>.T_MARGIN</code></p>
<dd>set a top margin</p>
<dt><code>.TI [</code><i> &lt;measure&gt; </i><code>]</code></p>
<dd>temporary left indent</p>
<dt><code>.WS</code></p>
<dd>set the minimum word space size</dl>
<h2>Documentation Of Details</h2>
<h3>Details of Inline Escape Sequences in alphabetical Order</h3>
<dl>
<dd>begin using an initialized colour inline</p>
<dd>move wards in a line</p>
<dt><code>\*[BOLDER]</code></p>
<dd><code>\*[BOLDERX]</code> Emboldening on/off</p>
<dl>
<dd><code>\*[BOLDER]</code> begins emboldening type. <code>\*[BOLDERX]</code> turns the feature off. Both are inline escapes, therefore they should not appear as separate lines, but rather be embedded in text lines, like this:</p>
<dl>
<dd></dl>
<p> Alternatively, if you wanted the whole line emboldened, you should do</p>
<dl>
<dd></dl>
<p> Once <code>\*[BOLDER]</code> is invoked, it remains in effect until turned off. </p>
<p> Note: If you&#8217;re using the document processing macros with <code>.PRINTSTYLE TYPEWRITE</code>, <code>mom</code> ignores <code>\*[BOLDER]</code> requests.</dl>
<dd>move characters pairs closer together inline (related to macro <code>.KERN</code>)</p>
<dt><code>\*[COND]</code></p>
<dd><code>\*[CONDX]</code> Pseudo-condensing on/off</p>
<dl>
<dd><code>\*[COND]</code> begins pseudo-condensing type. <code>\*[CONDX]</code> turns the feature off. Both are inline escapes, therefore they should not appear as separate lines, but rather be embedded in text lines, like this:</p>
<dl>
<dd></dl>
<p> <code>\*[COND]</code> remains in effect until you turn it off with <code>\*[CONDX]</code>. </p>
<p> IMPORTANT: You must turn <code>\*[COND]</code> off before making any changes to the point size of your type, either via the <code>.PT_SIZE</code> macro or with the <code>\s</code> inline escape. If you wish the new point size to be pseudo-condensed, simply reinvoke <code>\*[COND]</code> afterwards. Equally, <code>\*[COND]</code> must be turned off before changing the condense percentage with <code>.CONDENSE</code>. </p>
<p> Note: If you&#8217;re using the document processing macros with <code>.PRINTSTYLE TYPEWRITE</code>, <code>mom</code> ignores <code>\*[COND]</code> requests.</dl>
<dd>pseudo-condensed superscript</p>
<dd>temporarily move downwards in a line</p>
<dt><code>\*[EN-MARK]</code></p>
<dd>mark initial line of a range of line numbers (for use with line numbered endnotes)</p>
<dt><code>\*[EXT]</code></p>
<dd><code>\*[EXTX]</code> Pseudo-extending on/off</p>
<dl>
<dd><code>\*[EXT]</code> begins pseudo-extending type. <code>\*[EXTX]</code> turns the feature off. Both are inline escapes, therefore they should not appear as separate lines, but rather be embedded in text lines, like this:</p>
<dl>
<dd></dl>
<p> <code>\*[EXT]</code> remains in effect until you turn it off with <code>\*[EXTX]</code>. </p>
<p> IMPORTANT: You must turn <code>\*[EXT]</code> off before making any changes to the point size of your type, either via the <code>.PT_SIZE</code> macro or with the <code>\s</code> inline escape. If you wish the new point size to be <i>pseudo-extended</i>, simply reinvoke <code>\*[EXT]</code> afterwards. Equally, <code>\*[EXT]</code> must be turned off before changing the extend percentage with <code>.EXTEND</code>. </p>
<p> Note: If you are using the document processing macros with <code>.PRINTSTYLE TYPEWRITE</code>, <code>mom</code> ignores <code>\*[EXT]</code> requests.</dl>
<dd>pseudo extended superscript</p>
<dd>move characters pairs further apart inline (related to macro <code>.KERN</code>)</p>
<dd>move forward in a line</p>
<dt><code>\*[LEADER]</code></p>
<dd>insert leaders at the end of a line</p>
<dt><code>\*[RULE]</code></p>
<dd>draw a full measure rule</p>
<dd>change the point size inline (related to macro <code>.PT_SIZE</code>)</p>
<dt><code>\*[SLANT]</code></p>
<dd><code>\*[SLANTX]</code> Pseudo italic on/off</p>
<dl>
<dd><code>\*[SLANT]</code> begins <i>pseudo-italicizing</i> <i>type</i>. <code>\*[SLANTX]</code> turns the feature off. Both are <i>inline</i> <i>escapes</i>, therefore they should not appear as separate lines, but rather be embedded in text lines, like this:</p>
<dl>
<dd></dl>
<p> Alternatively, if you wanted the whole line <i>pseudo-italicized</i>, you&#8217;d do</p>
<dl>
<dd></dl>
<p> Once <code>\*[SLANT]</code> is invoked, it remains in effect until turned off. </p>
<p> Note: If you&#8217;re using the document processing macros with <code>.PRINTSTYLE TYPEWRITE</code>, <code>mom</code> underlines pseudo-italics by default. To change this behaviour, use the special macro <code>.SLANT_MEANS_SLANT</code>.</dl>
<dd>Mark positions of string tabs</p>
<dl>
<dd>The <i>quad</i> direction must be <code>LEFT</code> or <code>JUSTIFY</code> (see <code>.QUAD</code> and <code>.JUSTIFY</code>) or the <i>no-fill mode</i> set to <code>LEFT</code> in order for these inlines to function properly. Please see <i>IMPORTANT</i>, below. </p>
<p> String tabs need to be marked off with inline escapes before being set up with the <code>.ST</code> macro. Any input line may contain string tab markers. <i>&lt;number&gt;</i>, above, means the numeric identifier of the tab. </p>
<p> The following shows a sample input line with string tab markers.</p>
<dl>
<dd></dl>
<p> String <i>tab 1</i> begins at the start of the line and ends after the word <i>time</i>. String <i>tab 2</i> starts at <i>good</i> and ends after <i>men</i>. <i>Inline escapes</i> (e.g. <i>font</i> or <i>point size</i> <i>changes</i>, or horizontal movements, including padding) are taken into account when <code>mom</code> determines the <i>position</i> and <i>length</i> of <i>string</i> <i>tabs</i>. </p>
<p> Up to nineteen string tabs may be marked (not necessarily all on the same line, of course), and they must be numbered between 1 and 19. </p>
<p> Once string tabs have been marked in input lines, they have to be <i>set</i> with <code>.ST</code>, after which they may be called, by number, with <code>.TAB</code>. </p>
<p> Note: Lines with string tabs marked off in them are normal input lines, i.e. they get printed, just like any input line. If you want to set up string tabs without the line printing, use the <code>.SILENT</code> macro. </p>
<p> <i>IMPORTANT:</i> Owing to the way <code>groff</code> processes input lines and turns them into output lines, it is not possible for <code>mom</code> to <i>guess</i> the correct starting position of string tabs marked off in lines that are centered or set flush right. </p>
<p> Equally, she cannot guess the starting position if a line is fully justified and broken with <code>.SPREAD</code>. </p>
<p> In other words, in order to use string tabs, <code>LEFT</code> must be active, or, if <code>.QUAD LEFT</code> or <code>JUSTIFY</code> are active, the line on which the <i>string tabs</i> are marked must be broken <i>manually</i> with <code>.BR</code> (but not <code>.SPREAD</code>). </p>
<p> To circumvent this behaviour, I recommend using the <code>PAD</code> to set up string tabs in centered or flush right lines. Say, for example, you want to use a <i>string tab</i> to <i>underscore</i> the text of a centered line with a rule. Rather than this,</p>
<dl>
<dd><code>.CENTER</code> <code>\*[ST1]A line of text\*[ST1X]
