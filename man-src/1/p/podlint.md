---
title: "podlint(1)"
name: "podlint"
section: "1"
letter: "p"
url: "/docs/linux/man/1-podlint/"
---

<h2 class="name">NAME</h2>
 

 podlint - check POD for correctness using Pod::POM 

<h2>SYNOPSIS</h2>

 <pre>
    podlint MyFile.pm
</pre>

<h2>DESCRIPTION</h2>

 This script uses Pod::POM to parse a Pod document with full warnings enabled, effectively acting as a syntax and structure checker. 

 The -f option can be specified to have the parsed Pod Object Model printed to <font SIZE="-1">STDOUT</font> with any markup errors fixed. Note there are some critical parse errors that can't be handled and fixed by the parser and in this case the script will terminate reporting the error.

<h2>AUTHOR</h2>

 Andy Wardley &lt;abw [at] kfs.org&gt;

<h2>VERSION</h2>

 This is version 0.2 of podlint.

<h2>COPYRIGHT</h2>

 Copyright (C) 2000, 2001 Andy Wardley. All Rights Reserved. 

 This module is free software; you can redistribute it and/or modify it under the same terms as Perl itself.

<h2>SEE ALSO</h2>

 For further information please see Pod::POM. 

<h2>Index</h2>


