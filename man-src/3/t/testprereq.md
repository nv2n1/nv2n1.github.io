---
title: "testprereq(3)"
name: "testprereq"
section: "3"
letter: "t"
url: "/docs/linux/man/3-testprereq/"
---

Test::Prereq - check if Makefile.PL has the right pre-requisites 

<h2>Synopsis</h2><pre> # if you use Makefile.PL
 use Test::More;
 eval &quot;use Test::Prereq&quot;;
 plan skip_all =&gt; &quot;Test::Prereq required to test dependencies&quot; if $@;
 prereq_ok();
 # specify a perl version, test name, or module names to skip
 prereq_ok( $version, $name, \@skip );
 # if you use Module::Build
 use Test::More;
 eval &quot;use Test::Prereq::Build&quot;;
 plan skip_all =&gt; &quot;Test::Prereq::Build required to test dependencies&quot; if $@;
 prereq_ok();
 # or from the command line for a one-off check
 perl -MTest::Prereq -eprereq_ok</pre><h2>Description</h2>The <i>prereq_ok()</i> function examines the modules it finds in blib/lib/, blib/script, and the test files it finds in t/ (and test.pl). It figures out which modules they use, skips the modules that are in the Perl core, and compares the remaining list of modules to those in the <font SIZE="-1">PREREQ_PM</font> section of Makefile.PL. 

 If you use Module::Build instead, see Test::Prereq::Build instead.
<h3>Modules Test::Prereq can't find</h3>Module::Info only tells Test::Prereq which modules you used, not which distribution they came in. This can be a problem for things in packages like libnet, libwww, Tk, and so on. At the moment Test::Prereq asks <font SIZE="-1">CPAN</font>.pm to expand anything in <font SIZE="-1">PREREQ_PM</font> to see if one of the distributions you explicity list contains the module you actually used. This might fail in some cases. Please send me anything that does not do what you think it should. 

 Test::Prereq only asks <font SIZE="-1">CPAN</font>.pm for help if it needs it, since <font SIZE="-1">CPAN</font>.pm can be slow if it has to fetch things from the network. Once it fetches the right things, it should be much faster.
<h3>Problem with Module::Info</h3>Module::Info appears to do something weird if a file it analyzes does not use (or require) any modules. You may get a message like 

 <pre> Can't locate object method &quot;name&quot; via package &quot;B::NULL&quot; at
 /usr/perl5.8.0/lib/site_perl/5.8.0/B/Module/Info.pm line 176.</pre>Also, if a file cannot compile, Module::Info dumps a lot of text to the terminal. You probably want to bail out of testing if the files do not compile, though.
<h3>Problem with <font SIZE="-1">CPANPLUS</font></h3><font SIZE="-1">CPANPLUS</font> apparently does some weird things, and since it is still young and not part of the Standard Library, Test::Prereq's tests do not do the right thing under it (for some reason). Test::Prereq cheats by ignoring <font SIZE="-1">CPANPLUS</font> completely in the tests---at least until someone has a better solution. If you do not like that, you can set <tt>$EXCLUDE_CPANPLUS</tt> to a false value. 

 You should be able to do a 'make test' manually to make everything work, though.
<h3>Warning about redefining ExtUtils::MakeMaker::WriteMakefile</h3>Test::Prereq has its own version of ExtUtils::MakeMaker::WriteMakefile so it can run the Makefile.PL and get the argument list of that function. You may see warnings about this.
<h2>Functions</h2><dl COMPACT><dt>prereq_ok( [ <font SIZE="-1">VERSION,</font> [ <font SIZE="-1">NAME</font> [, <font SIZE="-1">SKIP_ARRAY</font>] ] ] )
<dd>Tests Makefile.PL to ensure all non-core module dependencies are in <font SIZE="-1">PREREQ_PM.</font> If you haven't set a testing plan already, <i>prereq_ok()</i> creates a plan of one test. 

 If you don't specify a version, prereq_ok assumes you want to compare the list of prerequisite modules to version 5.008005. 

 Valid versions come from Module::CoreList (which uses $[). 

 <pre> #!/usr/bin/perl
 use Module::CoreList;
 print map &quot;$_\n&quot;, sort keys %Module::CoreList::version;
 5.00307
 5.004
 5.00405
 5.005
 5.00503
 5.00504
 5.006
 5.006001
 5.006002
 5.007003
 5.008
 5.008001
 5.008002
 5.008003
 5.008004
 5.008005
 5.009
 5.009001</pre>prereq_ok attempts to remove modules found in blib and libraries found in t from the reported prerequisites. 

 The optional third argument is an array reference to a list of names that prereq_ok should ignore. You might want to use this if your tests do funny things with require.</dl><h2>To Do</h2>* set up a couple fake module distributions to test 

 * warn about things that show up in <font SIZE="-1">PREREQ_PM</font> unnecessarily
<h2>Source Availability</h2>This source is in Github: 

 <pre> <a rel="nofollow" HREF="http://github.com/briandfoy/test-prereq">http://github.com/briandfoy/test-prereq</a></pre><h2>Contributors</h2>Many thanks to: 

 Andy Lester, Slavin Rezic, Randal Schwartz, Iain Truskett, Dylan Martin
<h2>Author</h2>brian d foy, <tt>&quot;&lt;bdfoy [at] cpan.org&gt;&quot;</tt>
<h2>COPYRIGHT and LICENSE</h2>Copyright 2002-2009, brian d foy, All rights reserved 

 This software is available under the same terms as perl.
