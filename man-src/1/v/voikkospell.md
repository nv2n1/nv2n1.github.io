---
title: "voikkospell(1)"
name: "voikkospell"
section: "1"
letter: "v"
url: "/docs/linux/man/1-voikkospell/"
description: "voikkospell – test program for Voikko spell checker"
---

<h2 class="name">NAME</h2>
<p> voikkospell &#8211; test program for Voikko spell checker </p>
<h2>SYNOPSIS</h2>
<p> <code>voikkospell</code> [<i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>voikkospell</code> is a test program for spell checking functionality in libvoikko, library of Finnish language tools. It reads words from stdin (one word on a line) and print them to stdout, adding &quot;C: &quot; in front of correct words and &quot;W: &quot; in front of incorrect words. </p>
<p> Common options of different Voikko test programs are listed in COMMON OPTIONS.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-m</code></dt>
<dd> In addition to spelling result, prints morphological analysis info (A:) for recognized words.</dd>
<dt><code>-M</code></dt>
<dd> Prints morphological analysis info (A:) for recognized words without displaying spelling result.</dd>
<dt><code>-t</code></dt>
<dd> Prints only &quot;C&quot; or &quot;W&quot; instead of typical full output.</dd>
<dt><code>-tt</code></dt>
<dd> Prints only misspelled words.</dd>
<dt><code>-s</code></dt>
<dd> Prints suggestions (S:) for incorrectly spelled words.</dd>
<dt><code>-c</code><i>n</i></dt>
<dd> Set cache size parameter to <i>n</i>. -1 disables the cache and 0 is the default. For checking large amounts of unsorted text you may want to set <i>n</i> to 5 to get better performance.</dd>
<dt><code>-j</code><i> n</i></dt>
<dd> Use <i>n</i> threads for spell checking. When more than one thread is used checking is performed using large internal buffers which is why this mode should only be used for batch processing.</dd>
<dt><code>-x</code><i>c</i></dt>
<dd> Like <code>voikkospell -s</code> but output is printed on one line separated by character <i>c</i> without &quot;C&quot;, &quot;W&quot; or &quot;S&quot; in front of the words. If <i>c</i> is not defined words are separated by space and suggestions that have spaces in them are not printed.</dd>
<dt><code>-l</code></dt>
<dd> Prints a list of available dictionary variants and exits. The first variant is the default to be used when no specific variant has been requested.</dd>
<dt><code>ignore_nonwords=</code><i>n</i></dt>
<dd>
</dd><dt><code>accept_first_uppercase=</code><i>n</i></dt>
<dd>
</dd><dt><code>accept_extra_hyphens=</code><i>n</i></dt>
<dd>
</dd><dt><code>accept_missing_hyphens=</code><i>n</i></dt>
<dd>
</dd><dt><code>ocr_suggestions=</code><i>n</i></dt>
<dd>
 Set the value of the specified boolean option. <i>n</i> can be either 0 (false) or 1 (true).</dd></dl>
<h2>COMMON OPTIONS</h2>
<dl>
<dt><code>-p</code><i> directory</i></dt>
<dd> (voikkospell, voikkohyphenate, voikkogc) Look from <i>directory</i> before the standard locations when searching for dictionary files.</dd>
<dt><code>-d</code><i> variant</i></dt>
<dd> (voikkospell, voikkohyphenate, voikkogc) Use dictionary variant <i>variant</i> instead of the default dictionary variant. The variant must be represented as a BCP 47 language tag.</dd>
<dt><code>ignore_dot=</code><i>n</i></dt>
<dd> (voikkospell, voikkohyphenate)</dd>
<dt><code>ignore_numbers=</code><i>n</i></dt>
<dd> (voikkospell, voikkohyphenate)<br />
 Set the value of the specified boolean option. <i>n</i> can be either 0 (false) or 1 (true).</dd>
<dt><code>-h, &#8211;help</code></dt>
<dd> Print a help message and exit.</dd>
<dt><code>&#8211;version</code></dt>
<dd> Print version numbers for libvoikko and the test tool.</dd></dl>
<h2>AUTHOR</h2>
<p> voikkospell and this manual page were written by Harri Pitk&auml;nen (hatapitk [at] iki.fi). </p>
