---
title: "pdlpp-inline(1)"
name: "pdlpp-inline"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdlpp-inline/"
---

<pre> Inline::Pdlpp - Write PDL Subroutines inline with PDL::PP</pre><h2>Description</h2><tt>&quot;Inline::Pdlpp&quot;</tt> is a module that allows you to write PDL subroutines in the PDL::PP style. The big benefit compared to plain <tt>&quot;PDL::PP&quot;</tt> is that you can write these definitions inline in any old perl script (without the normal hassle of creating Makefiles, building, etc). Since version 0.30 the Inline module supports multiple programming languages and each language has its own support module. This document describes how to use Inline with PDL::PP (or rather, it will once these docs are complete <tt>&quot;;)&quot;</tt>. 

 For more information on Inline in general, see Inline. 

 Some example scripts demonstrating <tt>&quot;Inline::Pdlpp&quot;</tt> usage can be found in the <i>Example/InlinePdlpp</i> directory. 

 <tt>&quot;Inline::Pdlpp&quot;</tt> is mostly a shameless rip-off of <tt>&quot;Inline::C&quot;</tt>. Most Kudos goes to Brian I.
<h2>Usage</h2>You never actually use <tt>&quot;Inline::Pdlpp&quot;</tt> directly. It is just a support module for using <tt>&quot;Inline.pm&quot;</tt> with <tt>&quot;PDL::PP&quot;</tt>. So the usage is always: 

 <pre> use Inline Pdlpp =&gt; ...;</pre>or 

 <pre> bind Inline Pdlpp =&gt; ...;</pre><h2>Examples</h2>Pending availability of full docs a few quick examples that illustrate typical usage.
<h3>A simple example</h3><pre> # example script inlpp.pl
 use PDL; # must be called before (!) 'use Inline Pdlpp' calls
 use Inline Pdlpp; # the actual code is in the __Pdlpp__ block below
 $a = sequence 10;
 print $a-&gt;inc,&quot;\n&quot;;
 print $a-&gt;inc-&gt;dummy(1,10)-&gt;tcumul,&quot;\n&quot;;
 __DATA__
 __Pdlpp__
 pp_def('inc',
 Pars =&gt; 'i();[o] o()',
 Code =&gt; '$o() = $i() + 1;',
 );
 pp_def('tcumul',
 Pars =&gt; 'in(n);[o] mul()',
 Code =&gt; '$mul() = 1;
 loop(n) %{
 $mul() *= $in();
 %}',
 );
 # end example script</pre>If you call this script it should generate output similar to this: 

 <pre> prompt&gt; perl inlpp.pl
 Inline running PDL::PP version 2.2...
 [1 2 3 4 5 6 7 8 9 10]
 [3628800 3628800 3628800 3628800 3628800 3628800 3628800 3628800 3628800 3628800]</pre>Usage of <tt>&quot;Inline::Pdlpp&quot;</tt> in general is similar to <tt>&quot;Inline::C&quot;</tt>. In the absence of full docs for <tt>&quot;Inline::Pdlpp&quot;</tt> you might want to compare Inline::C.
<h3>Code that uses external libraries, etc</h3>The script below is somewhat more complicated in that it uses code from an external library (here from Numerical Recipes). All the relevant information regarding include files, libraries and boot code is specified in a config call to <tt>&quot;Inline&quot;</tt>. For more experienced Perl hackers it might be helpful to know that the format is similar to that used with ExtUtils::MakeMaker. The keywords are largely equivalent to those used with <tt>&quot;Inline::C&quot;</tt>. Please see below for further details on the usage of <tt>&quot;INC&quot;</tt>, <tt>&quot;LIBS&quot;</tt>, <tt>&quot;AUTO_INCLUDE&quot;</tt> and <tt>&quot;BOOT&quot;</tt>. 

 <pre> use PDL; # this must be called before (!) 'use Inline Pdlpp' calls
 use Inline Pdlpp =&gt; Config =&gt;
 INC =&gt; &quot;-I$ENV{HOME}/include&quot;,
 LIBS =&gt; &quot;-L$ENV{HOME}/lib -lnr -lm&quot;,
 # code to be included in the generated XS
 AUTO_INCLUDE =&gt; &lt;&lt;'EOINC',
 #include &lt;math.h&gt;
 #include &quot;nr.h&quot; /* for poidev */
 #include &quot;nrutil.h&quot; /* for err_handler */
 static void nr_barf(char *err_txt)
 {
 fprintf(stderr,&quot;Now calling croak...\n&quot;);
 croak(&quot;NR runtime error: %s&quot;,err_txt);
 }
 EOINC
 # install our error handler when loading the Inline::Pdlpp code
 BOOT =&gt; 'set_nr_err_handler(nr_barf);';
 use Inline Pdlpp; # the actual code is in the __Pdlpp__ block below
 $a = zeroes(10) + 30;;
 print $a-&gt;poidev(5),&quot;\n&quot;;
 __DATA__
 __Pdlpp__
 pp_def('poidev',
 Pars =&gt; 'xm(); [o] pd()',
 GenericTypes =&gt; [L,F,D],
 OtherPars =&gt; 'long idum',
 Code =&gt; '$pd() = poidev((float) $xm(), &amp;$COMP(idum));',
 );</pre><h2>Pdlpp Configuration Options</h2>For information on how to specify Inline configuration options, see Inline. This section describes each of the configuration options available for Pdlpp. Most of the options correspond either to MakeMaker or XS options of the same name. See ExtUtils::MakeMaker and perlxs.
<h3>AUTO_INCLUDE</h3>Specifies extra statements to automatically included. They will be added onto the defaults. A newline char will be automatically added. Does essentially the same as a call to <tt>&quot;pp_addhdr&quot;</tt>. For short bits of code <tt>&quot;AUTO_INCLUDE&quot;</tt> is probably syntactically nicer. 

 <pre> use Inline Pdlpp =&gt; Config =&gt; AUTO_INCLUDE =&gt; '#include &quot;yourheader.h&quot;';</pre><h3>BLESS</h3>Same as <tt>&quot;pp_bless&quot;</tt> command. Specifies the package (i.e. class) to which your new <i>pp_def</i>ed methods will be added. Defaults to <tt>&quot;PDL&quot;</tt> if omitted. 

 <pre> use Inline Pdlpp =&gt; Config =&gt; BLESS =&gt; 'PDL::Complex';</pre><h3>BOOT</h3>Specifies C code to be executed in the XS BOOT section. Corresponds to the XS parameter. Does the same as the <tt>&quot;pp_add_boot&quot;</tt> command. Often used to execute code only once at load time of the module, e.g. a library initialization call.
<h3>CC</h3>Specify which compiler to use.
<h3>CCFLAGS</h3>Specify extra compiler flags.
<h3>INC</h3>Specifies an include path to use. Corresponds to the MakeMaker parameter. 

 <pre> use Inline Pdlpp =&gt; Config =&gt; INC =&gt; '-I/inc/path';</pre><h3>LD</h3>Specify which linker to use.
<h3>LDDLFLAGS</h3>Specify which linker flags to use. 

 NOTE: These flags will completely override the existing flags, instead of just adding to them. So if you need to use those too, you must respecify them here.
<h3>LIBS</h3>Specifies external libraries that should be linked into your code. Corresponds to the MakeMaker parameter. 

 <pre> use Inline Pdlpp =&gt; Config =&gt; LIBS =&gt; '-lyourlib';</pre>or 

 <pre> use Inline Pdlpp =&gt; Config =&gt; LIBS =&gt; '-L/your/path -lyourlib';</pre><h3>MAKE</h3>Specify the name of the 'make' utility to use.
<h3>MYEXTLIB</h3>Specifies a user compiled object that should be linked in. Corresponds to the MakeMaker parameter. 

 <pre> use Inline Pdlpp =&gt; Config =&gt; MYEXTLIB =&gt; '/your/path/yourmodule.so';</pre><h3>OPTIMIZE</h3>This controls the MakeMaker OPTIMIZE setting. By setting this value to '-g', you can turn on debugging support for your Inline extensions. This will allow you to be able to set breakpoints in your C code using a debugger like gdb.
<h3>TYPEMAPS</h3>Specifies extra typemap files to use. Corresponds to the MakeMaker parameter. 

 <pre> use Inline Pdlpp =&gt; Config =&gt; TYPEMAPS =&gt; '/your/path/typemap';</pre><h3>NOISY</h3>Show the output of any compilations going on behind the scenes. Uses <tt>&quot;tee&quot;</tt> which must be available on your computer. Default is off.
<h2>Bugs</h2><h3>doing inline scripts</h3>Beware that there is a problem when you use the __DATA__ keyword style of Inline definition and want to <tt>&quot;do&quot;</tt> your script containing inlined code. For example 

 <pre> # myscript.pl contains inlined code
 # in the __DATA__ section
 perl -e 'do &quot;myscript.pl&quot;;'
 One or more DATA sections were not processed by Inline.</pre>According to Brian Ingerson (of Inline fame) the workaround is to include an <tt>&quot;Inline-&gt;init&quot;</tt> call in your script, e.g. 

 <pre> use PDL;
 use Inline Pdlpp;
 Inline-&gt;init;
 # perl code
 __DATA__
 __Pdlpp__
 # pp code</pre><h3>PDL::NiceSlice and Inline::Pdlpp</h3>There is currently an undesired interaction between PDL::NiceSlice and <tt>&quot;Inline::Pdlpp&quot;</tt>. Since PP code generally contains expressions of the type <tt>&quot;$var()&quot;</tt> (to access piddles, etc) PDL::NiceSlice recognizes those incorrectly as slice expressions and does its substitutions. For the moment (until hopefully the parser can deal with that) it is best to explicitly switch PDL::NiceSlice off before the section of inlined Pdlpp code. For example: 

 <pre> use PDL::NiceSlice;
 use Inline::Pdlpp;
 $a = sequence 10;
 $a(0:3)++;
 $a-&gt;inc;
 no PDL::NiceSlice;
 __DATA__
 __C__
 ppdef (...); # your full pp definition here</pre><h2>Acknowledgements</h2>Brian Ingerson for creating the Inline infrastructure.
<h2>Author</h2>Christian Soeller &lt;soellermail [at] excite.com&gt;
<h2>See Also</h2>PDL 

 PDL::PP 

 Inline 

 Inline::C
<h2>Copyright</h2>Copyright (c) 2001. Christian Soeller. All rights reserved. 

 This program is free software; you can redistribute it and/or modify it under the same terms as PDL itself. 

 See <a rel="nofollow" HREF="http://pdl.perl.org">http://pdl.perl.org</a>
