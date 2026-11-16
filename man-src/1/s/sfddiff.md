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
<dt>1)</dt>
<dd> Characters are present in one font but not in the other.</dd>
<dt>2)</dt>
<dd> Characters are present in both fonts but have different sets of outlines or references. The outlines may be compared so that only exact matches are accepted, or so that a fuzzier match is used. Similarly references may need to match exactly, or may be matched after an unlink.</dd>
<dt>
</dt><dd> This fuzzy comparison is useful when comparing truetype and postscript fonts, or when comparing a font with references to one without.</dd>
<dt>3)</dt>
<dd> The postscript hints or truetype instructions are different.</dd>
<dt>4)</dt>
<dd> The font names (the truetype `name&#8217; table) differ.</dd>
<dt>5)</dt>
<dd> The kerning (and other `gpos&#8217; information) differs.</dd>
<dt>6)</dt>
<dd> The ligatures (and other `gsub&#8217; information) differ.</dd>
<dt>7)</dt>
<dd> Any bitmap strikes present in one font but not in the other.</dd>
<dt>8)</dt>
<dd> Any bitmap characters present in one strike of one font but in the equivalent strike of the other.</dd>
<dt>9)</dt>
<dd> Any bitmap characters which differ.</dd></dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></dt>
<dd> Provide a description with a list of the available options.</dd>
<dt><code>&#8211;ignorehints</code></dt>
<dd> Suppress the reporting of hint/instruction differences.</dd>
<dt><code>&#8211;ignoregpos</code></dt>
<dd> Suppress the reporting of kerning (and other `gpos&#8217;) differences.</dd>
<dt><code>&#8211;ignoregsub</code></dt>
<dd> Suppress the reporting of ligature (and other `gsub&#8217;) differences.</dd>
<dt><code>&#8211;ignorenames</code></dt>
<dd> Suppress the reporting of name string differences.</dd>
<dt><code>&#8211;ignorebitmaps</code></dt>
<dd> Suppress the reporting of bitmap differences.</dd>
<dt><code>&#8211;exact</code></dt>
<dd> Require outlines to match exactly.</dd>
<dt><code>&#8211;warn</code></dt>
<dd> Warn if the outlines/references are slightly different.</dd>
<dt><code>&#8211;merge</code><i> outfile</i></dt>
<dd> Store a merged version of the two fonts into the specified output file. The merged data will be based on <i>sfdfile1</i>, as well as any characters present in <i>sfdfile2</i> but not in <i>sfdfile1</i> will be added, and the outlines of <i>sfdfile2</i> will be placed in the background. Finally, for any characters with different outlines or references the background of the character will contain the outlines from <i>sfdfile2</i> (references will be unlinked into outlines and those outlines also will be added).</dd>
<dt><code>&#8211;usage</code></dt>
<dd> Display the usage description.</dd>
<dt><code>&#8211;version</code></dt>
<dd> Display the current version.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-fontforge/">fontforge</a></code>(1) </p>
<p> The HTML version of the <i>fontforge</i> manual at:</p>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://fontforge.sourceforge.net/">http://fontforge.sourceforge.net/</a></dd></dl>
<h2>AUTHOR</h2>
<p> Copyright (C) 2000-2006 by George Williams (gww [at] silcom.com). Manual page heavily rewritten and modified to use standard <i>-man</i>(5) macros by R.P.C. Rodgers (rodgers [at] nlm.nih.gov), 23 October 2002. </p>
<h2>Index</h2>
