---
title: "sfddiff(1)"
name: "sfddiff"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sfddiff/"
description: "sfddiff – compare two font files"
---

<h2>NAME</h2>
<p> <code>sfddiff &#8211; compare two font files</code></p>
<h2>SYNOPSIS</h2>
<p> <code>sfddiff</code> [<code>&#8211;help</code>] [<code>&#8211;ignorehints</code>] [<code>&#8211;ignorenames</code>] [<code>&#8211;ignoregpos</code>] [<code>&#8211;ignoregsub</code>] [<code>&#8211;ignorebitmaps</code>] [<code>&#8211;exact</code>] [<code>&#8211;warn</code>] [<code>&#8211;merge</code> <i>outfile</i>] [<code>&#8211;usage</code>] [<code>&#8211;version</code>] <i>fontfile1</i> <i>fontfile2 </i></p>
<h2>DESCRIPTION</h2>
<p> The program <code>sfddiff</code> compares two font files, which may be in any format <code><a href="/docs/linux/man/1-fontforge/">fontforge</a></code>(1) can read. It will notice the following differences:</p>
<dl>
<dt>1)</p>
<dd> Characters are present in one font but not in the other.</p>
<dt>2)</p>
<dd> Characters are present in both fonts but have different sets of outlines or references. The outlines may be compared so that only exact matches are accepted, or so that a fuzzier match is used. Similarly references may need to match exactly, or may be matched after an unlink.</p>
<dt>
<dd> This fuzzy comparison is useful when comparing truetype and postscript fonts, or when comparing a font with references to one without.</p>
<dt>3)</p>
<dd> The postscript hints or truetype instructions are different.</p>
<dt>4)</p>
<dd> The font names (the truetype `name&#8217; table) differ.</p>
<dt>5)</p>
<dd> The kerning (and other `gpos&#8217; information) differs.</p>
<dt>6)</p>
<dd> The ligatures (and other `gsub&#8217; information) differ.</p>
<dt>7)</p>
<dd> Any bitmap strikes present in one font but not in the other.</p>
<dt>8)</p>
<dd> Any bitmap characters present in one strike of one font but in the equivalent strike of the other.</p>
<dt>9)</p>
<dd> Any bitmap characters which differ.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Provide a description with a list of the available options.</p>
<dt><code>&#8211;ignorehints</code></p>
<dd> Suppress the reporting of hint/instruction differences.</p>
<dt><code>&#8211;ignoregpos</code></p>
<dd> Suppress the reporting of kerning (and other `gpos&#8217;) differences.</p>
<dt><code>&#8211;ignoregsub</code></p>
<dd> Suppress the reporting of ligature (and other `gsub&#8217;) differences.</p>
<dt><code>&#8211;ignorenames</code></p>
<dd> Suppress the reporting of name string differences.</p>
<dt><code>&#8211;ignorebitmaps</code></p>
<dd> Suppress the reporting of bitmap differences.</p>
<dt><code>&#8211;exact</code></p>
<dd> Require outlines to match exactly.</p>
<dt><code>&#8211;warn</code></p>
<dd> Warn if the outlines/references are slightly different.</p>
<dt><code>&#8211;merge</code><i> outfile</i></p>
<dd> Store a merged version of the two fonts into the specified output file. The merged data will be based on <i>sfdfile1</i>, as well as any characters present in <i>sfdfile2</i> but not in <i>sfdfile1</i> will be added, and the outlines of <i>sfdfile2</i> will be placed in the background. Finally, for any characters with different outlines or references the background of the character will contain the outlines from <i>sfdfile2</i> (references will be unlinked into outlines and those outlines also will be added).</p>
<dt><code>&#8211;usage</code></p>
<dd> Display the usage description.</p>
<dt><code>&#8211;version</code></p>
<dd> Display the current version.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-fontforge/">fontforge</a></code>(1) </p>
<p> The HTML version of the <i>fontforge</i> manual at:</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://fontforge.sourceforge.net/">http://fontforge.sourceforge.net/</a></dl>
<h2>AUTHOR</h2>
<p> Copyright (C) 2000-2006 by George Williams (gww [at] silcom.com). Manual page heavily rewritten and modified to use standard <i><a href="/docs/linux/man/5--man/">-man</a></i>(5) macros by R.P.C. Rodgers (rodgers [at] nlm.nih.gov), 23 October 2002. </p>
<h2>Index</h2>
