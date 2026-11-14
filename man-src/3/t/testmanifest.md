---
title: "testmanifest(3)"
name: "testmanifest"
section: "3"
letter: "t"
url: "/docs/linux/man/3-testmanifest/"
---

Test::Manifest - interact with a t/test_manifest file 

<h2>Synopsis</h2><pre> # in Makefile.PL
 eval &quot;use Test::Manifest&quot;;
 # in the file t/test_manifest, list the tests you want 
 # to run</pre><h2>Description</h2>Test::Harness assumes that you want to run all of the .t files in the t/ directory in ascii-betical order during <tt>&quot;make test&quot;</tt> unless you say otherwise. This leads to some interesting naming schemes for test files to get them in the desired order. This interesting names ossify when they get into source control, and get even more interesting as more tests show up. 

 Test::Manifest overrides the default behaviour by replacing the test_via_harness target in the Makefile. Instead of running at the t/*.t files in ascii-betical order, it looks in the t/test_manifest file to find out which tests you want to run and the order in which you want to run them. It constructs the right value for MakeMaker to do the right thing. 

 In t/test_manifest, simply list the tests that you want to run. Their order in the file is the order in which they run. You can comment lines with a #, just like in Perl, and Test::Manifest will strip leading and trailing whitespace from each line. It also checks that the specified file is actually in the t/ directory. If the file does not exist, it does not put its name in the list of test files to run. 

 Optionally, you can add a number after the test name in test_manifest to define sets of tests. See <i>get_t_files()</i> for more information.
<h2>Functions</h2><dl COMPACT><dt>run_t_manifest( <font SIZE="-1">TEST_VERBOSE</font>, <font SIZE="-1">INST_LIB</font>, <font SIZE="-1">INST_ARCHLIB</font>, <font SIZE="-1">TEST_LEVEL</font> )
<dd>Run all of the files in t/test_manifest through Test::Harness:runtests in the order they appear in the file. 

 <pre> eval &quot;use Test::Manifest&quot;;</pre><dt>get_t_files( [<font SIZE="-1">LEVEL</font>] )
<dd>In scalar context it returns a single string that you can use directly in <i>WriteMakefile()</i>. In list context it returns a list of the files it found in t/test_manifest. 

 If a t/test_manifest file does not exist, <i>get_t_files()</i> returns nothing. 

 <i>get_t_files()</i> warns you if it can't find t/test_manifest, or if entries start with ``t/''. It skips blank lines, and strips Perl style comments from the file. 

 Each line in t/test_manifest can have three parts: the test name, the test level (a floating point number), and a comment. By default, the test level is 1. 

 <pre> test_name.t 2 #Run this only for level 2 testing</pre>Without an argument, <i>get_t_files()</i> returns all the test files it finds. With an argument that is true (so you can't use 0 as a level) and is a number, it skips tests with a level greater than that argument. You can then define sets of tests and choose a set to run. For instance, you might create a set for end users, but also add on a set for deeper testing for developers. 

 Experimentally, you can include a command to grab test names from another file. The command starts with a <tt>&quot;;&quot;</tt> to distinguish it from a true filename. The filename (currently) is relative to the current working directory, unlike the filenames, which are relative to <tt>&quot;t/&quot;</tt>. The filenames in the included are still relative to <tt>&quot;t/&quot;</tt>. 

 <pre> ;include t/file_with_other_test_names.txt</pre>Also experimentally, you can stop Test::Manifest from reading filenames with the <tt>&quot;;skip&quot;</tt> directive. Test::Harness will skip the filenames up to the <tt>&quot;;unskip&quot;</tt> directive (or end of file) 

 <pre> run_this1
 ;skip
 skip_this
 ;unskip
 run_this2</pre>To select sets of tests, specify the level in the variable <font SIZE="-1">TEST_LEVEL</font> during `make test`. 

 <pre> make test # run all tests no matter the level
 make test TEST_LEVEL=2 # run all tests level 2 and below</pre><dt><i>make_test_manifest()</i>
<dd>Creates the test_manifest file in the t directory by reading the contents of the t directory. 

 <font SIZE="-1">TO</font> <font SIZE="-1">DO:</font> specify tests in argument lists. 

 <font SIZE="-1">TO</font> <font SIZE="-1">DO:</font> specify files to skip.
<dt><i>manifest_name()</i>
<dd>Returns the name of the test manifest file, relative to t/</dl><h2>Source Availability</h2>This source is part of a SourceForge project which always has the latest sources in <font SIZE="-1">CVS</font>, as well as all of the previous releases. 

 <pre> <a rel="nofollow" HREF="http://sourceforge.net/projects/brian-d-foy/">http://sourceforge.net/projects/brian-d-foy/</a></pre>If, for some reason, I disappear from the world, one of the other members of the project can shepherd this module appropriately.
<h2>Credits</h2>Matt Vanderpol suggested and supplied a patch for the ;include feature.
<h2>Author</h2>brian d foy, <tt>&quot;&lt;bdfoy [at] cpan.org&gt;&quot;</tt>
<h2>Copyright And License</h2>Copyright (c) 2002-2007 brian d foy. All rights reserved. 

 This program is free software; you can redistribute it and/or modify it under the same terms as Perl itself.
