---
title: "streqvmap(3)"
name: "streqvmap"
section: "3"
letter: "s"
url: "/docs/linux/man/3-streqvmap/"
description: "streqvmap – Set the character mappings for the streqv functions"
---

<p>streqvmap &#8211; Set the character mappings for the streqv functions</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;your-opts.h&gt;

cc[...] - o outfile infile.c - lopts[...] void streqvmap(char from, char to, int ct);
</code></pre>
<h2>Description</h2>
<p>Set the character mapping. If the count (<code>ct</code>) is set to zero, then the map is cleared by setting all entries in the map to their index value. Otherwise, the &quot;<code>From</code>&quot; character is mapped to the &quot;<code>To</code>&quot; character. If <code>ct</code> is greater than 1, then <code>From</code> and <code>To</code> are incremented and the process repeated until <code>ct</code> entries have been set. For example, </p>
<pre> streqvmap('a', 'A', 26);</pre>
<p>will alter the mapping so that all English lower case letters will map to upper case. This function name is mapped to option_streqvmap so as to not conflict with the POSIX name space.</p>
<dl>
<dt><i>from</i></p>
<dd>Input character</p>
<dt><i>to</i></p>
<dd>Mapped-to character</p>
<dt><i>ct</i></p>
<dd>compare length </p>
<h2>Errors</h2>
<p>none.</p>
<h2>See Also</h2>
<p>The <i>info</i> documentation for the -l<i>opts</i> library.<br />
 <a href="/docs/linux/man/3-ao_string_tokenize/">ao_string_tokenize</a>(3), <a href="/docs/linux/man/3-configfileload/">configFileLoad</a>(3), <a href="/docs/linux/man/3-optionfileload/">optionFileLoad</a>(3), <a href="/docs/linux/man/3-optionfindnextvalue/">optionFindNextValue</a>(3), <a href="/docs/linux/man/3-optionfindvalue/">optionFindValue</a>(3), <a href="/docs/linux/man/3-optionfree/">optionFree</a>(3), <a href="/docs/linux/man/3-optiongetvalue/">optionGetValue</a>(3), <a href="/docs/linux/man/3-optionloadline/">optionLoadLine</a>(3), <a href="/docs/linux/man/3-optionmemberlist/">optionMemberList</a>(3), <a href="/docs/linux/man/3-optionnextvalue/">optionNextValue</a>(3), <a href="/docs/linux/man/3-optiononlyusage/">optionOnlyUsage</a>(3), <a href="/docs/linux/man/3-optionprocess/">optionProcess</a>(3), <a href="/docs/linux/man/3-optionrestore/">optionRestore</a>(3), <a href="/docs/linux/man/3-optionsavefile/">optionSaveFile</a>(3), <a href="/docs/linux/man/3-optionsavestate/">optionSaveState</a>(3), <a href="/docs/linux/man/3-optionunloadnested/">optionUnloadNested</a>(3), <a href="/docs/linux/man/3-optionversion/">optionVersion</a>(3), <a href="/docs/linux/man/3-strequate/">strequate</a>(3), <a href="/docs/linux/man/3-streqvcmp/">streqvcmp</a>(3), <a href="/docs/linux/man/3-strneqvcmp/">strneqvcmp</a>(3), <a href="/docs/linux/man/3-strtransform/">strtransform</a>(3), </p>
