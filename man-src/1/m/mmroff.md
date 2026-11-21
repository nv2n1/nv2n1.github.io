---

title: "mmroff(1)"
name: "mmroff"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mmroff/"
description: "mmroff – cross-reference preprocessor for GNU roff mm macro package"
---

<p> [ <code>-x</code> ] <i>groff-arguments</i></p>
<p> <i>mmroff</i> is a simple preprocessor for <i>groff</i>, used for expanding cross references in <i>mm</i>; see <i><a href="/docs/linux/man/7-groff_mm/">groff_mm</a></i>(7). <i>groff</i> is executed twice, first with <code>-z</code> and <code>-rRef=1</code> to collect all cross references and then to do the real processing when the cross-reference file is up to date.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-x</code></dt>
<dd> Just create the cross-reference file. This can be used to refresh the cross-reference file; it isn&#8217;t always needed to have accurate cross references and by using this option <i>groff</i> will only be run once.</dd></dl>
<h2>AUTHORS</h2>
<p> <code>mmroff</code> was written by Jörgen Hägg of Lund, Sweden.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-groff_mm/">groff_mm</a></i>(7), <i><a href="/docs/linux/man/7-groff_mmse/">groff_mmse</a></i>(7) (only in Swedish locales), <i><a href="/docs/linux/man/1-groff/">groff</a></i>(1), <i><a href="/docs/linux/man/1-troff/">troff</a></i>(1), <i><a href="/docs/linux/man/1-tbl/">tbl</a></i>(1), <i><a href="/docs/linux/man/1-pic/">pic</a></i>(1), <i><a href="/docs/linux/man/1-eqn/">eqn</a></i>(1) </p>
