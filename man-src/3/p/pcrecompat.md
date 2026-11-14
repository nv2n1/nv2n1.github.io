---
title: "pcrecompat(3)"
name: "pcrecompat"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcrecompat/"
description: "PCRE – Perl-compatible regular expressions"
---

<p>PCRE &#8211; Perl-compatible regular expressions</p>
<h2>Differences Between Pcre And Perl</h2>
<p>This document describes the differences in the ways that PCRE and Perl handle regular expressions. The differences described here are with respect to Perl versions 5.10 and above. </p>
<p> 1. PCRE has only a subset of Perl&#8217;s Unicode support. Details of what it does have are given in the <code>pcreunicode</code> page. </p>
<p> 2. PCRE allows repeat quantifiers only on parenthesized assertions, but they do not mean what you might think. For example, (?!a){3} does not assert that the next three characters are not &quot;a&quot;. It just asserts that the next character is not &quot;a&quot; three times (in principle: PCRE optimizes this to run the assertion just once). Perl allows repeat quantifiers on other assertions such as , but these do not seem to have any use. </p>
<p> 3. Capturing subpatterns that occur inside negative lookahead assertions are counted, but their entries in the offsets vector are never set. Perl sometimes (but not always) sets its numerical variables from inside negative assertions. </p>
<p> 4. Though binary zero characters are supported in the subject string, they are not allowed in a pattern string because it is passed as a normal C string, terminated by zero. The escape sequence 
