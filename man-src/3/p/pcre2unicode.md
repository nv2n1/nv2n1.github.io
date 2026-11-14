---
title: "pcre2unicode(3)"
name: "pcre2unicode"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2unicode/"
description: "PCRE – Perl-compatible regular expressions (revised API)"
---

<p>PCRE &#8211; Perl-compatible regular expressions (revised API)</p>
<h2>Unicode And Utf Support</h2>
<p>PCRE2 is normally built with Unicode support, though if you do not need it, you can build it without, in which case the library will be smaller. With Unicode support, PCRE2 has knowledge of Unicode character properties and can process text strings in UTF-8, UTF-16, or UTF-32 format (depending on the code unit width), but this is not the default. Unless specifically requested, PCRE2 treats each code unit in a string as one character. </p>
<p> There are two ways of telling PCRE2 to switch to UTF mode, where characters may consist of more than one code unit and the range of values is constrained. The program can call <code>pcre2_compile()</code> with the PCRE2_UTF option, or the pattern may start with the sequence (*UTF). However, the latter facility can be locked out by the PCRE2_NEVER_UTF option. That is, the programmer can prevent the supplier of the pattern from switching to UTF mode. </p>
<p> Note that the PCRE2_MATCH_INVALID_UTF option (see below) forces PCRE2_UTF to be set. </p>
<p> In UTF mode, both the pattern and any subject strings that are matched against it are treated as UTF strings instead of strings of individual one-code-unit characters. There are also some other changes to the way characters are handled, as documented below.</p>
<h2>Unicode Property Support</h2>
<p>When PCRE2 is built with Unicode support, the escape sequences \p{..}, \P{..}, and \X can be used. This is not dependent on the PCRE2_UTF setting. The Unicode properties that can be tested are limited to the general category properties such as Lu for an upper case letter or Nd for a decimal number, the Unicode script names such as Arabic or Han, and the derived properties Any and L&amp;. Full lists are given in the <code>pcre2pattern</code> and <code>pcre2syntax</code> documentation. Only the short names for properties are supported. For example, \p{L} matches a letter. Its Perl synonym, \p{Letter}, is not supported. Furthermore, in Perl, many properties may optionally be prefixed by &quot;Is&quot;, for compatibility with Perl 5.6. PCRE2 does not support this.</p>
<h2>Wide Characters And Utf Modes</h2>
<p>Code points less than 256 can be specified in patterns by either braced or unbraced hexadecimal escape sequences (for example, 
