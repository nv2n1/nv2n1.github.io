---
title: "pomdump(1)"
name: "pomdump"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pomdump/"
---

<h2 class="name">NAME</h2>
 

 pomdump - dump the POM parse tree for a POD document 

<h2>SYNOPSIS</h2>

 <pre>
    pomdump MyFile.pm
</pre>

<h2>DESCRIPTION</h2>

 This script uses Pod::POM to parse a Pod document and then invokes the dump method on the top level node, resulting in a visualization of the structure of the <font SIZE="-1">POD</font> document (the parse tree).

<h2>AUTHOR</h2>

 Andrew Ford &lt;A.Ford [at] ford-mason.co.uk&gt;

<h2>VERSION</h2>

 This is version 0.1 of pomdump.

<h2>COPYRIGHT</h2>

 Copyright (C) 2009 Andrew Ford. All Rights Reserved. 

 This module is free software; you can redistribute it and/or modify it under the same terms as Perl itself.

<h2>SEE ALSO</h2>

 For further information please see Pod::POM. 

<h2>Index</h2>


