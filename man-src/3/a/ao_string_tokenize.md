---
title: "ao_string_tokenize(3)"
name: "ao_string_tokenize"
section: "3"
letter: "a"
url: "/docs/linux/man/3-ao_string_tokenize/"
description: "ao_string_tokenize – tokenize an input string"
---

<h2 class="name">NAME</h2>
<p> ao_string_tokenize &#8211; tokenize an input string</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;<i>your-opts.h</i>&gt;<br />
 cc [&#8230;] -o outfile infile.c -l<code>opts</code> [&#8230;] </p>
<p> token_list_t* <code>ao_string_tokenize</code>(char const* <i>string</i>); </p>
<h2>DESCRIPTION</h2>
<p> This function will convert one input string into a list of strings. The list of strings is derived by separating the input based on white space separation. However, if the input contains either single or double quote characters, then the text after that character up to a matching quote will become the string in the list. </p>
<p> The returned pointer should be deallocated with <code><a href="//www.systutorials.com/docs/linux/man/3C-free/">free</a>(3C)</code> when are done using the data. The data are placed in a single block of allocated memory. Do not deallocate individual token/strings. </p>
<p> The structure pointed to will contain at least these two fields: </p>
<p> <i>tkn_ct</i> The number of tokens found in the input string. </p>
<p> <i>tok_list</i> An array of <code>tkn_ct + 1</code> pointers to substring tokens, with the last pointer set to NULL. </p>
<p> There are two types of quoted strings: single quoted (<code>&#8216;</code>) and double quoted (<code>&quot;</code>). Singly quoted strings are fairly raw in that escape characters (<code>\</code>) are simply another character, except when preceding the following characters: </p>
<pre>
    <code>\</code>  double backslashes reduce to one
    <code>'</code>   incorporates the single quote into the string
    <code>fP  suppresses both the backslash and newline character
</code></pre>
<p> Double quote strings are formed according to the rules of string constants in ANSI-C programs.</p>
<dl>
<dt><i>string</i></p>
<dd> string to be tokenized </p>
</dl>
<h2>RETURN VALUE</h2>
<p> pointer to a structure that lists each token </p>
<h2>ERRORS</h2>
<p> NULL is returned and <code>errno</code> will be set to indicate the problem: </p>
<p> <code>EINVAL</code> &#8211; There was an unterminated quoted string. </p>
<p> <code>ENOENT</code> &#8211; The input string was empty. </p>
<p> <code>ENOMEM</code> &#8211; There is not enough memory. @end itemize </p>
<h2>EXAMPLES</h2>
<pre><code>
#include &lt;stdlib.h&gt;
int ix;
token_list_t *ptl = ao_string_tokenize(some_string) for (ix = 0; ix &lt; ptl-&gt;tkn_ct; ix++)
    do_something_with_tkn(ptl-&gt;tkn_list[ix]);
free(ptl);
</code></pre>
<p> Note that everything is freed with the one call to <code><a href="//www.systutorials.com/docs/linux/man/3C-free/">free</a>(3C)</code>.</p>
<h2>SEE ALSO</h2>
<p> The <i>info</i> documentation for the -l<i>opts</i> library.<br />
 <a href="/docs/linux/man/3-configfileload/">configFileLoad</a>(3), <a href="/docs/linux/man/3-optionfileload/">optionFileLoad</a>(3), <a href="/docs/linux/man/3-optionfindnextvalue/">optionFindNextValue</a>(3), <a href="/docs/linux/man/3-optionfindvalue/">optionFindValue</a>(3), <a href="/docs/linux/man/3-optionfree/">optionFree</a>(3), <a href="/docs/linux/man/3-optiongetvalue/">optionGetValue</a>(3), <a href="/docs/linux/man/3-optionloadline/">optionLoadLine</a>(3), <a href="/docs/linux/man/3-optionmemberlist/">optionMemberList</a>(3), <a href="/docs/linux/man/3-optionnextvalue/">optionNextValue</a>(3), <a href="/docs/linux/man/3-optiononlyusage/">optionOnlyUsage</a>(3), <a href="/docs/linux/man/3-optionprocess/">optionProcess</a>(3), <a href="/docs/linux/man/3-optionrestore/">optionRestore</a>(3), <a href="/docs/linux/man/3-optionsavefile/">optionSaveFile</a>(3), <a href="/docs/linux/man/3-optionsavestate/">optionSaveState</a>(3), <a href="/docs/linux/man/3-optionunloadnested/">optionUnloadNested</a>(3), <a href="/docs/linux/man/3-optionversion/">optionVersion</a>(3), <a href="/docs/linux/man/3-strequate/">strequate</a>(3), <a href="/docs/linux/man/3-streqvcmp/">streqvcmp</a>(3), <a href="/docs/linux/man/3-streqvmap/">streqvmap</a>(3), <a href="/docs/linux/man/3-strneqvcmp/">strneqvcmp</a>(3), <a href="/docs/linux/man/3-strtransform/">strtransform</a>(3), </p>
<h2>Index</h2>
