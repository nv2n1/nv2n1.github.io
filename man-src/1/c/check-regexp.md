---
title: "check-regexp(1)"
name: "check-regexp"
section: "1"
letter: "c"
url: "/docs/linux/man/1-check-regexp/"
description: "check-regexp – test regular expressions from the command line"
---

<h2>NAME</h2>
<p> check-regexp &#8211; test regular expressions from the command line</p>
<h2>SYNOPSIS</h2>
<p> <code>check-regexp</code> <i>&#8216;regular expression&#8217; &#8216;string1&#8217; &#8216;string2&#8217; </i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> check-regexp (GNU Source-highlight) </p>
<p> You simply pass as the first command line argument the regular expression and then the strings you want to try to match.<br />
 It is crucial, in order to avoid shell substitutions, to enclose both the expression and the strings in single quotes. </p>
<p> The program then prints some information about the possibly successful matching.<br />
 In the output the what[0] part represents the whole match, and the what[i] part represents the i-th marked subexpression that matched. </p>
<p> The program also prints possible prefix and suffix.</p>
<h2>OPTIONS</h2>
<p> This program follows the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). A summary of options is included below.</p>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Print help and exit</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Print version and exit</dl>
<h2>AUTHOR</h2>
<p> check-regexp was written by Lorenzo Bettini &lt;<a rel="nofollow" href="http://www.lorenzobettini.it">www.lorenzobettini.it</a>&gt;. This man page was written by Cesare Tirabassi &lt;norsetto [at] ubuntu.com&gt;. </p>
<h2>Index</h2>
