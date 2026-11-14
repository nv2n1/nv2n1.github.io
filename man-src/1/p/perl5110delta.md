---
title: "perl5110delta(1)"
name: "perl5110delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5110delta/"
description: "perl5110delta – what is new for perl v5.11.0"
---

<h2 class="name">NAME</h2>
<p> perl5110delta &#8211; what is new for perl v5.11.0 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.10.0 release and the 5.11.0 development release.</p>
<h2>Incompatible Changes</h2>
<h3>Unicode interpretation of \w, \d, \s, and the <font SIZE="-1">POSIX</font> character classes redefined.</h3>
<p> Previous versions of Perl tried to map <font SIZE="-1">POSIX</font> style character class definitions onto Unicode property names so that patterns would &#8220;dwim&#8221; when matches were made against latin-1 or unicode strings. This proved to be a mistake, breaking character class negation, causing forward compatibility problems (as Unicode keeps updating their property definitions and adding new characters), and other problems. </p>
<p> Therefore we have now defined a new set of artificial &#8220;unicode&#8221; property names which will be used to do unicode matching of patterns using <font SIZE="-1">POSIX</font> style character classes and perl short-form escape character classes like \w and \d. </p>
<p> The key change here is that \d will no longer match every digit in the unicode standard (there are thousands) nor will \w match every word character in the standard, instead they will match precisely their <font SIZE="-1">POSIX</font> or Perl definition. </p>
<p> Those needing to match based on Unicode properties can continue to do so by using the \p{} syntax to match whichever property they like, including the new artificial definitions. </p>
<p> <font SIZE="-1"><code>NOTE:</code></font> This is a backwards incompatible no-warning change in behaviour. If you are upgrading and you process large volumes of text look for <font SIZE="-1">POSIX</font> and Perl style character classes and change them to the relevant property name (by removing the word &#8216;Posix&#8217; from the current name). </p>
<p> The following table maps the <font SIZE="-1">POSIX</font> character class names, the escapes and the old and new Unicode property mappings: </p>
<pre><code>
    POSIX  Esc  Class               New-Property  ! Old-Property
    ----------------------------------------------+-------------
    alnum       [0-9A-Za-z]         IsPosixAlnum  ! IsAlnum
    alpha       [A-Za-z]            IsPosixAlpha  ! IsAlpha
    ascii       [
