---
title: "gcov2perl(1)"
name: "gcov2perl"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gcov2perl/"
---

<h2 class="name">NAME</h2>
 

 gcov2perl - convert gcov files to Devel::Cover databases 

<h2>VERSION</h2>

 version 1.03

<h2>SYNOPSIS</h2>

 <pre>
 gcov2perl -h -i -v -db database gcov_files
</pre>

<h2>DESCRIPTION</h2>

 Convert gcov files to Devel::Cover databases.

<h2>OPTIONS</h2>

 The following command line options are supported: 

 <pre>
 -db database    - specify the database to use
 -h -help        - show help
 -i -info        - show documentation
 -v -version     - show version
</pre>

<h2>DETAILS</h2>

 To obtain coverage of <font SIZE="-1">XS</font> files they must first be compiled with the appropriate options. In a standard Makefile environment, such as that created by ExtUtils::MakeMaker, this can be accomplished with the command: 

 <pre>
 HARNESS_PERL_SWITCHES=-MDevel::Cover make test \
   CCFLAGS=-O0\ -fprofile-arcs\ -ftest-coverage \
   OTHERLDFLAGS=-fprofile-arcs\ -ftest-coverage
</pre> 

 If you have already built your object files it may be necessary to run make clean first, or to find some other way to ensure that they get rebuilt with the options gcov requires. 

 Now the code coverage data has been collected <tt>&quot;gcov&quot;</tt> needs to be run: 

 <pre>
 gcov Mylib.xs
</pre> 

 This will create one or more gcov files on which you can run <tt>&quot;gcov2perl&quot;</tt>: 

 <pre>
 gcov2perl Mylib.xs.gcov
</pre> 

 Finally, <tt>&quot;cover&quot;</tt> should be run as usual with any options required: 

 <pre>
 cover
</pre> 

 If you are running everything with standard options, you can do all this with one command: 

 <pre>
 cover -test
</pre>

<h2>EXIT STATUS</h2>

 The following exit values are returned: 

 <pre>
 0   All files converted successfully
 &gt;0  An error occurred.
</pre>

<h2>SEE ALSO</h2>

 <pre>
 Devel::Cover
</pre>

<h2>BUGS</h2>

 Huh?

<h2>LICENCE</h2>

 Copyright 2001-2013, Paul Johnson (paul [at] pjcj.net) 

 This software is free. It is licensed under the same terms as Perl itself. 

 The latest version of this software should be available from my homepage: <a rel="nofollow" HREF="http://www.pjcj.net">http://www.pjcj.net</a> 

<h2>Index</h2>


