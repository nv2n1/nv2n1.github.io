---
title: "perlrebackslash(1)"
name: "perlrebackslash"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlrebackslash/"
description: "perlrebackslash – Perl Regular Expression Backslash Sequences and Escapes"
---

<h2 class="name">NAME</h2>
<p> perlrebackslash &#8211; Perl Regular Expression Backslash Sequences and Escapes </p>
<h2>DESCRIPTION</h2>
<p> The top level documentation about Perl regular expressions is found in perlre. </p>
<p> This document describes all backslash and escape sequences. After explaining the role of the backslash, it lists all the sequences that have a special meaning in Perl regular expressions (in alphabetical order), then describes each of them. </p>
<p> Most sequences are described in detail in different documents; the primary purpose of this document is to have a quick reference guide describing all backslash and escape sequences.</p>
<h3>The backslash</h3>
<p> In a regular expression, the backslash can perform one of two tasks: it either takes away the special meaning of the character following it (for instance, <tt>&quot;\|&quot;</tt> matches a vertical bar, it&#8217;s not an alternation), or it is the start of a backslash or escape sequence. </p>
<p> The rules determining what it is are quite simple: if the character following the backslash is an <font SIZE="-1">ASCII</font> punctuation (non-word) character (that is, anything that is not a letter, digit, or underscore), then the backslash just takes away any special meaning of the character following it. </p>
<p> If the character following the backslash is an <font SIZE="-1">ASCII</font> letter or an <font SIZE="-1">ASCII</font> digit, then the sequence may be special; if so, it&#8217;s listed below. A few letters have not been used yet, so escaping them with a backslash doesn&#8217;t change them to be special. A future version of Perl may assign a special meaning to them, so if you have warnings turned on, Perl issues a warning if you use such a sequence. [1]. </p>
<p> It is however guaranteed that backslash or escape sequences never have a punctuation character following the backslash, not now, and not in a future version of Perl 5. So it is safe to put a backslash in front of a non-word character. </p>
<p> Note that the backslash itself is special; if you want to match a backslash, you have to escape the backslash with a backslash: <tt>&quot;/\/&quot;</tt> matches a single backslash.</p>
<dl>
<dt>[1]</p>
<dd> There is one exception. If you use an alphanumeric character as the delimiter of your pattern (which you probably shouldn&#8217;t do for readability reasons), you have to escape the delimiter if you want to match it. Perl won&#8217;t warn then. See also &#8220;Gory details of parsing quoted constructs&#8221; in perlop.</dl>
<h3>All the sequences and escapes</h3>
<p> Those not usable within a bracketed character class (like <tt>&quot;[\da-z]&quot;</tt>) are marked as <tt>&quot;Not in [].&quot;</tt> </p>
<pre><code>

