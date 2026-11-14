---
title: "pod2readme(1)"
name: "pod2readme"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pod2readme/"
---

<h2 class="name">NAME</h2>
 

 pod2readme - script to convert POD to README file 

<h2>SYNOPSIS</h2>

 <pre>
  pod2readme lib/Some/Module.pm
</pre>

<h2>DESCRIPTIONS</h2>

 Converts <font SIZE="-1">POD</font> in the specified file to a <i></i><font SIZE="-1"><i>README</i></font><i></i> text file. If a second argument is given, it will use that as the output file and assume that is the type of file to export: 

 <pre>
  pod2readme Module.pm COPYING
</pre> 

 If need be, this can be overridden in cases where the output file is not the same as the type, using a third argument: 

 <pre>
  pod2readme Module.pm Module-Install.HOWTO install
</pre>

<h2>SEE ALSO</h2>

 Pod::Readme

<h2>AUTHOR</h2>

 Robert Rothenberg &lt;rrwo at cpan.org&gt;

<h2>LICENSE</h2>

 Copyright (c) 2005 Robert Rothenberg. All rights reserved. This program is free software; you can redistribute it and/or modify it under the same terms as Perl itself. 

<h2>Index</h2>


