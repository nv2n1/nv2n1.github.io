---
title: "pcre2compat(3)"
name: "pcre2compat"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2compat/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API)</p>
<h2>Differences Between Pcre2 And Perl</h2>
<p>This document describes the differences in the ways that PCRE2 and Perl handle regular expressions. The differences described here are with respect to Perl versions 5.26, but as both Perl and PCRE2 are continually changing, the information may sometimes be out of date. </p>
<p> 1. PCRE2 has only a subset of Perl&#8217;s Unicode support. Details of what it does have are given in the <code>pcre2unicode</code> page. </p>
<p> 2. Like Perl, PCRE2 allows repeat quantifiers on parenthesized assertions, but they do not mean what you might think. For example, (?!a){3} does not assert that the next three characters are not &quot;a&quot;. It just asserts that the next character is not &quot;a&quot; three times (in principle; PCRE2 optimizes this to run the assertion just once). Perl allows some repeat quantifiers on other assertions, for example, * (but not {3}), but these do not seem to have any use. </p>
<p> 3. Capture groups that occur inside negative lookaround assertions are counted, but their entries in the offsets vector are set only when a negative assertion is a condition that has a matching branch (that is, the condition is false). </p>
<p> 4. The following Perl escape sequences are not supported: \F, \l, \L, 
