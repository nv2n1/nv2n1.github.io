---
title: "optionsavefile(3)"
name: "optionsavefile"
section: "3"
letter: "o"
url: "/docs/linux/man/3-optionsavefile/"
description: "optionSaveFile – saves the option state to a file"
---

<p>optionSaveFile &#8211; saves the option state to a file</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;your-opts.h&gt;

cc[...] - o outfile infile.c - lopts[...] void optionSaveFile(tOptions *opts);
</code></pre>
<h2>Description</h2>
<p>This routine will save the state of option processing to a file. The name of that file can be specified with the argument to the <code>&#8211;save-opts</code> option, or by appending the <code>rcfile</code> attribute to the last <code>homerc</code> attribute. If no <code>rcfile</code> attribute was specified, it will default to <code>.</code><i>programname</i>rc. If you wish to specify another file, you should invoke the <code>SET_OPT_SAVE_OPTS(</code><i>filename</i>) macro. The recommend usage is as follows: </p>
<pre> optionProcess(&amp;progOptions, argc, argv);
 if (i_want_a_non_standard_place_for_this)
 SET_OPT_SAVE_OPTS(&quot;myfilename&quot;);
 optionSaveFile(&amp;progOptions);</pre>
<dl>
<dt><i>opts</i></p>
<dd>program options descriptor </p>
<h2>Errors</h2>
<p>If no <code>homerc</code> file was specified, this routine will silently return and do nothing. If the output file cannot be created or updated, a message will be printed to <code>stderr</code> and the routine will return.</p>
<h2>See Also</h2>
<p>The <i>info</i> documentation for the -l<i>opts</i> library.<br />
 <a href="/docs/linux/man/3-ao_string_tokenize/">ao_string_tokenize</a>(3), <a href="/docs/linux/man/3-configfileload/">configFileLoad</a>(3), <a href="/docs/linux/man/3-optionfileload/">optionFileLoad</a>(3), <a href="/docs/linux/man/3-optionfindnextvalue/">optionFindNextValue</a>(3), <a href="/docs/linux/man/3-optionfindvalue/">optionFindValue</a>(3), <a href="/docs/linux/man/3-optionfree/">optionFree</a>(3), <a href="/docs/linux/man/3-optiongetvalue/">optionGetValue</a>(3), <a href="/docs/linux/man/3-optionloadline/">optionLoadLine</a>(3), <a href="/docs/linux/man/3-optionmemberlist/">optionMemberList</a>(3), <a href="/docs/linux/man/3-optionnextvalue/">optionNextValue</a>(3), <a href="/docs/linux/man/3-optiononlyusage/">optionOnlyUsage</a>(3), <a href="/docs/linux/man/3-optionprocess/">optionProcess</a>(3), <a href="/docs/linux/man/3-optionrestore/">optionRestore</a>(3), <a href="/docs/linux/man/3-optionsavestate/">optionSaveState</a>(3), <a href="/docs/linux/man/3-optionunloadnested/">optionUnloadNested</a>(3), <a href="/docs/linux/man/3-optionversion/">optionVersion</a>(3), <a href="/docs/linux/man/3-strequate/">strequate</a>(3), <a href="/docs/linux/man/3-streqvcmp/">streqvcmp</a>(3), <a href="/docs/linux/man/3-streqvmap/">streqvmap</a>(3), <a href="/docs/linux/man/3-strneqvcmp/">strneqvcmp</a>(3), <a href="/docs/linux/man/3-strtransform/">strtransform</a>(3), </p>
