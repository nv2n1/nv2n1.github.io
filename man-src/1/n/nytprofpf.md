---
title: "nytprofpf(1)"
name: "nytprofpf"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nytprofpf/"
---

<h2 class="name">NAME</h2>
 

 nytprofpf - Generate a report for plat_forms (&lt;

<a rel="nofollow" HREF="http://www.plat-forms.org/">http://www.plat-forms.org/</a>&gt;) from Devel::NYTProf data

<h2>SYNOPSIS</h2>

 Typical usage: 

 <pre>
 $ perl -d:NYTProf some_perl_app.pl
 $ nytprofpf
</pre> 

 Options synopsis: 

 <pre><code>
--file&lt;file&gt;, -f&lt;file&gt; Read profile data from the specified file [default:nytprof.out]-- delete, -d Delete any old report files first-- lib&lt;lib&gt;, -l&lt;lib&gt; Add&lt;lib&gt; to the beginning of \@INC-- no - mergeevals Disable merging of string evals-- help, -h Print this message
</code></pre> 

 This script of part of the Devel::NYTProf distribution. Generate a report for plat_forms (&lt;<a rel="nofollow" HREF="http://www.plat-forms.org/">http://www.plat-forms.org/</a>&gt;) from Devel::NYTProf data. See <a rel="nofollow" HREF="http://metacpan.org/release/Devel-NYTProf/">http://metacpan.org/release/Devel-NYTProf/</a> for details and copyright. 

<h2>Index</h2>


