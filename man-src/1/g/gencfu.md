---
title: "gencfu(1)"
name: "gencfu"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gencfu/"
description: "gencfu – Generates Unicode Confusable data files"
---

<h2 class="name">NAME</h2>
<p> <code>gencfu</code> &#8211; Generates Unicode Confusable data files </p>
<h2>SYNOPSIS</h2>
<p> <code>gencfu</code> [ <code>-h</code>, <code>-?</code>, <code>&#8211;help</code> ] [ <code>-V</code>, <code>&#8211;version</code> ] [ <code>-c</code>, <code>&#8211;copyright</code> ] [ <code>-v</code>, <code>&#8211;verbose</code> ] [ <code>-d</code>, <code>&#8211;destdir</code><i> destination</i> ] [ <code>-i</code>, <code>&#8211;icudatadir</code><i> directory</i> ] <code>-r</code>, <code>&#8211;rules</code><i> rule-file</i> <code>-w</code>, <code>&#8211;wsrules</code><i> whole-script-rule-file</i> <code>-o</code>, <code>&#8211;out</code><i> output-file</i></p>
<h2>DESCRIPTION</h2>
<p> <code>gencfu</code> reads confusable character definitions in the input file, which are plain text files containing confusable character definitions in the input format defined by Unicode UAX39 for the files <i>confusables.txt</i> and <i>confusablesWholeScript.txt.</i> This source (.txt) format is also accepted by ICU spoof detectors. The files must be encoded in utf-8 format, with or without a BOM. Normally the output data file has the <code>.cfu</code> extension.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>-?</code>, <code>&#8211;help</code></p>
<dd> Print help about usage and exit.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Print the version of <code>gencfu</code> and exit.</p>
<dt><code>-c</code>, <code>&#8211;copyright</code></p>
<dd> Embeds the standard ICU copyright into the <i>output-file</i>.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Display extra informative messages during execution.</p>
<dt><code>-d</code>, <code>&#8211;destdir</code><i> destination</i></p>
<dd> Set the destination directory of the <i>output-file</i> to <i>destination</i>.</p>
<dt><code>-i</code>, <code>&#8211;icudatadir</code><i> directory</i></p>
<dd> Look for any necessary ICU data files in <i>directory</i>. For example, the file <code>pnames.icu</code> must be located when ICU&#8217;s data is not built as a shared library. The default ICU data directory is specified by the environment variable <code>ICU_DATA</code>. Most configurations of ICU do not require this argument.</p>
<dt><code>-r</code>, <code>&#8211;rules</code><i> rule-file</i></p>
<dd> The source file to read.</p>
<dt><code>-w</code>, <code>&#8211;wsrules</code><i> whole-script-rule-file</i></p>
<dd> The whole script source file to read.</p>
<dt><code>-o</code>, <code>&#8211;out</code><i> output-file</i></p>
<dd> The output data file to write.</dl>
<h2>VERSION</h2>
<p> 1.0</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2009 International Business Machines Corporation and others </p>
<h2>Index</h2>
