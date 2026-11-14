---
title: "perlver(1)"
name: "perlver"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlver/"
---

<h2 class="name">NAME</h2>
 

 perlver - The Perl Minimum Version Analyzer 

<h2>SYNOPSIS</h2>

 <pre><code>
  adam@red:~$ perlver Perl-MinimumVersion
  Found directory '.'
  Searching for Perl files... found 3 file(s)
  Scanning lib/Perl/MinimumVersion.pm... done
  Scanning t/01_compile.t... done
  Scanning t/02_main.t... done
      ---------------------------------------------------------
    | file                       | explicit | syntax | external |
    | --------------------------------------------------------- |
    | lib/Perl/MinimumVersion.pm | 5.005    | ~      | n/a      |
    | t/01_compile.t             | ~        | ~      | n/a      |
    | t/02_main.t                | ~        | ~      | n/a      |
      ---------------------------------------------------------
  Minimum version of Perl required: ...
  adam@red:~$
</code></pre>

<h2>DESCRIPTION</h2>

 <tt>&quot;perlver&quot;</tt> is a console script created to provide convenient access to the functionality provided by Perl::MinimumVersion. 

 --blame option shows code which requires this version of perl 

 The synopsis above pretty much covers all you need to know at this point.

<h2>TO DO</h2>

 - Add PPI::Cache integration 

 - Add PPI::Metrics integration (once it exists) 

 - Add some sort of parseable output

<h2>SUPPORT</h2>

 All bugs should be filed via the bug tracker at 

 &lt;<a rel="nofollow" HREF="http://rt.cpan.org/NoAuth/ReportBug.html?Queue=Perl-MinimumVersion">http://rt.cpan.org/NoAuth/ReportBug.html?Queue=Perl-MinimumVersion</a>&gt; 

 For other issues, or commercial enhancement and support, contact the author

<h2>AUTHORS</h2>

 Adam Kennedy &lt;adamk [at] cpan.org&gt;

<h2>SEE ALSO</h2>

 <font SIZE="-1">PPI</font>, Perl::MinimumVersion

<h2>COPYRIGHT</h2>

 Copyright 2005 - 2012 Adam Kennedy. 

 This program is free software; you can redistribute it and/or modify it under the same terms as Perl itself. 

 The full text of the license can be found in the <font SIZE="-1">LICENSE</font> file included with this module. 

<h2>Index</h2>


