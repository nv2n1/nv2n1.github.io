---
title: "optionprocess(3)"
name: "optionprocess"
section: "3"
letter: "o"
url: "/docs/linux/man/3-optionprocess/"
description: "optionProcess – this is the main option processing routine"
---

<p>optionProcess &#8211; this is the main option processing routine</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;your-opts.h&gt;

cc[...] - o outfile infile.c - lopts[...] int optionProcess(tOptions *opts, int a_ct, char **a_v);
</code></pre>
<h2>Description</h2>
<p>This is the main entry point for processing options. It is intended that this procedure be called once at the beginning of the execution of a program. Depending on options selected earlier, it is sometimes necessary to stop and restart option processing, or to select completely different sets of options. This can be done easily, but you generally do not want to do this. The number of arguments processed always includes the program name. If one of the arguments is &quot;&#8211;&quot;, then it is counted and the processing stops. If an error was encountered and errors are to be tolerated, then the returned value is the index of the argument causing the error. A hyphen by itself (&quot;-&quot;) will also cause processing to stop and will <i>not</i> be counted among the processed arguments. A hyphen by itself is treated as an operand. Encountering an operand stops option processing.</p>
<dl>
<dt><i>opts</i></p>
<dd>program options descriptor</p>
<dt><i>a_ct</i></p>
<dd>program arg count</p>
<dt><i>a_v</i></p>
<dd>program arg vector </p>
<h2>Return Value</h2>
<p>the count of the arguments processed </p>
<h2>Errors</h2>
<p>Errors will cause diagnostics to be printed. <code><a href="/docs/linux/man/3-exit/">exit</a>(3)</code> may or may not be called. It depends upon whether or not the options were generated with the &quot;allow-errors&quot; attribute, or if the ERRSKIP_OPTERR or ERRSTOP_OPTERR macros were invoked.</p>
<h2>See Also</h2>
<p>The <i>info</i> documentation for the -l<i>opts</i> library.<br />
 <a href="/docs/linux/man/3-ao_string_tokenize/">ao_string_tokenize</a>(3), <a href="/docs/linux/man/3-configfileload/">configFileLoad</a>(3), <a href="/docs/linux/man/3-optionfileload/">optionFileLoad</a>(3), <a href="/docs/linux/man/3-optionfindnextvalue/">optionFindNextValue</a>(3), <a href="/docs/linux/man/3-optionfindvalue/">optionFindValue</a>(3), <a href="/docs/linux/man/3-optionfree/">optionFree</a>(3), <a href="/docs/linux/man/3-optiongetvalue/">optionGetValue</a>(3), <a href="/docs/linux/man/3-optionloadline/">optionLoadLine</a>(3), <a href="/docs/linux/man/3-optionmemberlist/">optionMemberList</a>(3), <a href="/docs/linux/man/3-optionnextvalue/">optionNextValue</a>(3), <a href="/docs/linux/man/3-optiononlyusage/">optionOnlyUsage</a>(3), <a href="/docs/linux/man/3-optionrestore/">optionRestore</a>(3), <a href="/docs/linux/man/3-optionsavefile/">optionSaveFile</a>(3), <a href="/docs/linux/man/3-optionsavestate/">optionSaveState</a>(3), <a href="/docs/linux/man/3-optionunloadnested/">optionUnloadNested</a>(3), <a href="/docs/linux/man/3-optionversion/">optionVersion</a>(3), <a href="/docs/linux/man/3-strequate/">strequate</a>(3), <a href="/docs/linux/man/3-streqvcmp/">streqvcmp</a>(3), <a href="/docs/linux/man/3-streqvmap/">streqvmap</a>(3), <a href="/docs/linux/man/3-strneqvcmp/">strneqvcmp</a>(3), <a href="/docs/linux/man/3-strtransform/">strtransform</a>(3), </p>
