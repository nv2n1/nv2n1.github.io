---
title: "optionloadline(3)"
name: "optionloadline"
section: "3"
letter: "o"
url: "/docs/linux/man/3-optionloadline/"
---

optionLoadLine - process a string for an option name and value

<h2>Synopsis</h2>

<pre><code>#include &lt;your-opts.h&gt;

cc[...] - o outfile infile.c - lopts[...] void optionLoadLine(tOptions *opts, char const *line);
</code></pre>

<h2>Description</h2>

This is a client program callable routine for setting options from, for example, the contents of a file that they read in. Only one option may appear in the text. It will be treated as a normal (non-preset) option. When passed a pointer to the option struct and a string, it will find the option named by the first token on the string and set the option argument to the remainder of the string. The caller must NUL terminate the string. The caller need not skip over any introductory hyphens. Any embedded new lines will be included in the option argument. If the input looks like one or more quoted strings, then the input will be &quot;cooked&quot;. The &quot;cooking&quot; is identical to the string formation used in AutoGen definition files (@pxref{basic expression}), except that you may not use backquotes.
<dl><dt><i>opts</i>
<dd>program options descriptor
<dt><i>line</i>
<dd>NUL-terminated text 

<h2>Errors</h2>

Invalid options are silently ignored. Invalid option arguments will cause a warning to print, but the function should return.

<h2>See Also</h2>

The <i>info</i> documentation for the -l<i>opts</i> library. 
 <a HREF="/docs/linux/man/3-ao_string_tokenize/">ao_string_tokenize</a>(3), <a HREF="/docs/linux/man/3-configfileload/">configFileLoad</a>(3), <a HREF="/docs/linux/man/3-optionfileload/">optionFileLoad</a>(3), <a HREF="/docs/linux/man/3-optionfindnextvalue/">optionFindNextValue</a>(3), <a HREF="/docs/linux/man/3-optionfindvalue/">optionFindValue</a>(3), <a HREF="/docs/linux/man/3-optionfree/">optionFree</a>(3), <a HREF="/docs/linux/man/3-optiongetvalue/">optionGetValue</a>(3), <a HREF="/docs/linux/man/3-optionmemberlist/">optionMemberList</a>(3), <a HREF="/docs/linux/man/3-optionnextvalue/">optionNextValue</a>(3), <a HREF="/docs/linux/man/3-optiononlyusage/">optionOnlyUsage</a>(3), <a HREF="/docs/linux/man/3-optionprocess/">optionProcess</a>(3), <a HREF="/docs/linux/man/3-optionrestore/">optionRestore</a>(3), <a HREF="/docs/linux/man/3-optionsavefile/">optionSaveFile</a>(3), <a HREF="/docs/linux/man/3-optionsavestate/">optionSaveState</a>(3), <a HREF="/docs/linux/man/3-optionunloadnested/">optionUnloadNested</a>(3), <a HREF="/docs/linux/man/3-optionversion/">optionVersion</a>(3), <a HREF="/docs/linux/man/3-strequate/">strequate</a>(3), <a HREF="/docs/linux/man/3-streqvcmp/">streqvcmp</a>(3), <a HREF="/docs/linux/man/3-streqvmap/">streqvmap</a>(3), <a HREF="/docs/linux/man/3-strneqvcmp/">strneqvcmp</a>(3), <a HREF="/docs/linux/man/3-strtransform/">strtransform</a>(3), 
