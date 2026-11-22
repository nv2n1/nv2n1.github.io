---

title: "dviselect(1)"
name: "dviselect"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dviselect/"
description: "dviselect – extract pages from DVI files"
---

<p> dviselect &#8211; extract pages from DVI files </p>
<h2>SYNOPSIS</h2>
<p> <code>dviselect</code> [ <code>-s</code> ] [ <code>-i</code> <i>infile</i> ] [ <code>-o</code> <i>outfile</i> ] <i>list of pages</i> [ <i>infile</i> [ <i>outfile</i> ] ]</p>
<h2>DESCRIPTION</h2>
<p> <i>Dviselect</i> selects pages from a DVI file produced by TeX, creating a new DVI file usable by any of the TeX conversion programs, or even by <i>dviselect</i> itself. </p>
<p> A <i>range</i> is a string of the form <i>even</i>, <i>odd</i>, or <i>first:last</i> where both <i>first</i> and <i>last</i> are optional numeric strings, with negative numbers indicated by a leading underscore character &#8220;_&#8221;. If both <i>first</i> and <i>last</i> are omitted, the colon may also be omitted, or may be replaced with an asterisk &#8220;*&#8221;. A <i>page range</i> is a list of ranges separated by periods. A <i>list of pages</i> is described by a set of page ranges separated by commas and/or white space. </p>
<p> <i>Dviselect</i> actually looks at the ten <i>count</i> variables that TeX writes; the first of these (\count0) is the page number, with \count1 through \count9 having varied uses depending on which macro packages are in use. (Typically \count1 might be a chapter or section number.) A page is included in <i>dviselect</i>&#8216;s output if all its \count values match any one of the ranges listed on the command line. For example, the command ``dviselect *.1,35:&#8216;&#8216; might select everything in chapter 1, as well as pages 35 and up. ``dviselect 10:30&#8217;&#8216; would select pages 10 through 30 (inclusive). ``:43&#8217;&#8216; means everything up to and including page 43 (including negative-numbered pages). To get all even-numbered pages, use ``even&#8217;&#8216;; to get all odd-numbered pages, use ``odd&#8217;&#8216;. If a Table of Contents has negative page numbers, ``:_1&#8217;&#8216; will select it. Note that ``*&#8216;&#8216; must be quoted from the shell; the empty string is more convenient to use, if harder to read. </p>
<p> Instead of \count values, <i>dviselect</i> can also select by ``absolute page number&#8217;&#8216;, where the first page is page 1, the second page 2, and so forth. Absolute page numbers are indicated by a leading equal sign ``=&#8216;&#8216;. Ranges of absolute pages are also allowed: ``dviselect =3:7&#8217;&#8216; will extract the third through seventh pages. Dot separators are not legal in absolute ranges, and there are no negative absolute page numbers. Even/odd specifiers, however, are legal; ``dviselect =even&#8217;&#8216; selects every other page, starting with the second. </p>
<p> More precisely, an asterisk or an empty string implies no limit; an equal sign means absolute page number rather than \counts; a leading colon means everything up to and including the given page; a trailing colon means everything from the given page on; the word ``even&#8217;&#8216; means only even values shall be accepted; the word ``odd&#8217;&#8216; means only odd values shall be accepted; and a period indicates that the next \count should be examined. If fewer than 10 ranges are specified, the remaining \counts are left unrestricted (that is, ``1:5&#8217;&#8216; and ``1:5.*&#8216;&#8216; are equivalent). A single number <i>n</i> is treated as if it were the range <i>n:n</i>. An arbitrary number of page selectors may be given, separated by commas or whitespace; a page is selected if any of the selectors matches its \counts or absolute page number. </p>
<p> Dviselect normally prints the page numbers of the pages selected; the <i>-s</i> option suppresses this.  </p>
<h2>AUTHOR</h2>
<p> Chris Torek, University of Maryland  </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-dviconcat/">dviconcat</a>(1), <a href="/docs/linux/man/1-latex/">latex</a>(1), <a href="/docs/linux/man/1-tex/">tex</a>(1) <br/>
 <i>MC-TeX User&#8217;s Guide</i> <br/>
 <i>The TeXbook</i>  </p>
<h2>BUGS</h2>
<p> A leading ``-&#8216;&#8216; ought to be allowed for negative numbers, but it is currently used as a synonym for ``:&#8216;&#8216;, for backwards compatibility. </p>
<p> Section or subsection selection will sometimes fail, for the DVI file lists only the \count values that were active when the page ended. Clever macro packages can alleviate this by making use of other ``free&#8217;&#8216; \count registers. Chapters normally begin on new pages, and do not suffer from this particular problem. </p>
<p> The heuristic that decides which arguments are page selectors and which are file names is often wrong. Using shell redirection or the -i and -o options is safest. </p>
<p> <i>Dviselect</i> does not adjust the parameters in the postamble; however, since these values are normally used only to size certain structures in the output conversion programs, and the parameters never need to be adjusted upward, this has not proven to be a problem. </p>
