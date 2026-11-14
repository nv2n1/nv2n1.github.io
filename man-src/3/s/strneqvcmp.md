---
title: "strneqvcmp(3)"
name: "strneqvcmp"
section: "3"
letter: "s"
url: "/docs/linux/man/3-strneqvcmp/"
description: "strneqvcmp – compare two strings with an equivalence mapping"
---

<p>strneqvcmp &#8211; compare two strings with an equivalence mapping</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;your-opts.h&gt;

cc[...] - o outfile infile.c - lopts[...] int strneqvcmp(char const *str1, char const *str2, int ct);
</code></pre>
<h2>Description</h2>
<p>Using a character mapping, two strings are compared for &quot;equivalence&quot;. Each input character is mapped to a comparison character and the mapped-to characters are compared for the two NUL terminated input strings. The comparison is limited to <code>ct</code> bytes. This function name is mapped to option_strneqvcmp so as to not conflict with the POSIX name space.</p>
<dl>
<dt><i>str1</i></p>
<dd>first string</p>
<dt><i>str2</i></p>
<dd>second string</p>
<dt><i>ct</i></p>
<dd>compare length </p>
<h2>Return Value</h2>
<p>the difference between two differing characters </p>
<h2>Errors</h2>
<p>none checked. Caller responsible for seg faults.</p>
<h2>See Also</h2>
<p>The <i>info</i> documentation for the -l<i>opts</i> library.<br />
 <a href="/docs/linux/man/3-ao_string_tokenize/">ao_string_tokenize</a>(3), <a href="/docs/linux/man/3-configfileload/">configFileLoad</a>(3), <a href="/docs/linux/man/3-optionfileload/">optionFileLoad</a>(3), <a href="/docs/linux/man/3-optionfindnextvalue/">optionFindNextValue</a>(3), <a href="/docs/linux/man/3-optionfindvalue/">optionFindValue</a>(3), <a href="/docs/linux/man/3-optionfree/">optionFree</a>(3), <a href="/docs/linux/man/3-optiongetvalue/">optionGetValue</a>(3), <a href="/docs/linux/man/3-optionloadline/">optionLoadLine</a>(3), <a href="/docs/linux/man/3-optionmemberlist/">optionMemberList</a>(3), <a href="/docs/linux/man/3-optionnextvalue/">optionNextValue</a>(3), <a href="/docs/linux/man/3-optiononlyusage/">optionOnlyUsage</a>(3), <a href="/docs/linux/man/3-optionprocess/">optionProcess</a>(3), <a href="/docs/linux/man/3-optionrestore/">optionRestore</a>(3), <a href="/docs/linux/man/3-optionsavefile/">optionSaveFile</a>(3), <a href="/docs/linux/man/3-optionsavestate/">optionSaveState</a>(3), <a href="/docs/linux/man/3-optionunloadnested/">optionUnloadNested</a>(3), <a href="/docs/linux/man/3-optionversion/">optionVersion</a>(3), <a href="/docs/linux/man/3-strequate/">strequate</a>(3), <a href="/docs/linux/man/3-streqvcmp/">streqvcmp</a>(3), <a href="/docs/linux/man/3-streqvmap/">streqvmap</a>(3), <a href="/docs/linux/man/3-strtransform/">strtransform</a>(3), </p>
