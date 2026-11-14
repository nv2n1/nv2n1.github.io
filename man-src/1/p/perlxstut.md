---
title: "perlxstut(1)"
name: "perlxstut"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlxstut/"
description: "perlxstut – Tutorial for writing XSUBs"
---

<h2 class="name">NAME</h2>
<p> perlxstut &#8211; Tutorial for writing XSUBs </p>
<h2>DESCRIPTION</h2>
<p> This tutorial will educate the reader on the steps involved in creating a Perl extension. The reader is assumed to have access to perlguts, perlapi and perlxs. </p>
<p> This tutorial starts with very simple examples and becomes more complex, with each new example adding new features. Certain concepts may not be completely explained until later in the tutorial in order to slowly ease the reader into building extensions. </p>
<p> This tutorial was written from a Unix point of view. Where I know them to be otherwise different for other platforms (e.g. Win32), I will list them. If you find something that was missed, please let me know.</p>
<h2>SPECIAL NOTES</h2>
<h3>make</h3>
<p> This tutorial assumes that the make program that Perl is configured to use is called <tt>&quot;make&quot;</tt>. Instead of running &#8220;make&#8221; in the examples that follow, you may have to substitute whatever make program Perl has been configured to use. Running <code>perl -V:make</code> should tell you what it is.</p>
<h3>Version caveat</h3>
<p> When writing a Perl extension for general consumption, one should expect that the extension will be used with versions of Perl different from the version available on your machine. Since you are reading this document, the version of Perl on your machine is probably 5.005 or later, but the users of your extension may have more ancient versions. </p>
<p> To understand what kinds of incompatibilities one may expect, and in the rare case that the version of Perl on your machine is older than this document, see the section on &#8220;Troubleshooting these Examples&#8221; for more information. </p>
<p> If your extension uses some features of Perl which are not available on older releases of Perl, your users would appreciate an early meaningful warning. You would probably put this information into the <i></i><font SIZE="-1"><i>README</i></font><i></i> file, but nowadays installation of extensions may be performed automatically, guided by <i></i><font SIZE="-1"><i>CPAN</i></font><i>.pm</i> module or other tools. </p>
<p> In MakeMaker-based installations, <i>Makefile.PL</i> provides the earliest opportunity to perform version checks. One can put something like this in <i>Makefile.PL</i> for this purpose: </p>
<pre>
    eval { require 5.007 }
        or die &lt;&lt;EOD;
    ############
    ### This module uses frobnication framework which is not available
    ### before version 5.007 of Perl.  Upgrade your Perl before
    ### installing Kara::Mba.
    ############
    EOD
</pre>
<h3>Dynamic Loading versus Static Loading</h3>
<p> It is commonly thought that if a system does not have the capability to dynamically load a library, you cannot build XSUBs. This is incorrect. You <i>can</i> build them, but you must link the XSUBs subroutines with the rest of Perl, creating a new executable. This situation is similar to Perl 4. </p>
<p> This tutorial can still be used on such a system. The <font SIZE="-1">XSUB</font> build mechanism will check the system and build a dynamically-loadable library if possible, or else a static library and then, optionally, a new statically-linked executable with that static library linked in. </p>
<p> Should you wish to build a statically-linked executable on a system which can dynamically load libraries, you may, in all the following examples, where the command &quot;<tt>&quot;make&quot;</tt>&#8220; with no arguments is executed, run the command &#8221;<tt>&quot;make perl&quot;</tt>&quot; instead. </p>
<p> If you have generated such a statically-linked executable by choice, then instead of saying &quot;<tt>&quot;make test&quot;</tt>&#8220;, you should say &#8221;<tt>&quot;make test_static&quot;</tt>&#8220;. On systems that cannot build dynamically-loadable libraries at all, simply saying &#8221;<tt>&quot;make test&quot;</tt>&quot; is sufficient.</p>
<h3>Threads and <font SIZE="-1">PERL_NO_GET_CONTEXT</font></h3>
<p> For threaded builds, perl requires the context pointer for the current thread, without <tt>&quot;PERL_NO_GET_CONTEXT&quot;</tt>, perl will call a function to retrieve the context. </p>
<p> For improved performance, include: </p>
<pre><code>
#define PERL_NO_GET_CONTEXT
</code></pre>
<p> as shown below. </p>
<p> For more details, see perlguts.</p>
<h2>TUTORIAL</h2>
<p> Now let&#8217;s go on with the show!</p>
<h3><font SIZE="-1">EXAMPLE 1</font></h3>
<p> Our first extension will be very simple. When we call the routine in the extension, it will print out a well-known message and return. </p>
<p> Run &quot;<tt>&quot;h2xs -A -n Mytest&quot;</tt>&quot;. This creates a directory named Mytest, possibly under ext/ if that directory exists in the current working directory. Several files will be created under the Mytest dir, including <font SIZE="-1">MANIFEST,</font> Makefile.PL, lib/Mytest.pm, Mytest.xs, t/Mytest.t, and Changes. </p>
<p> The <font SIZE="-1">MANIFEST</font> file contains the names of all the files just created in the Mytest directory. </p>
<p> The file Makefile.PL should look something like this: </p>
<p>use ExtUtils::MakeMaker;<br />
#See lib / ExtUtils / MakeMaker.pm for details of how to influence<br />
#the contents of the Makefile that is written.<br />
WriteMakefile(<br />
    NAME = &gt; &#8216;Mytest&#8217;,<br />
    VERSION_FROM = &gt; &#8216;Mytest.pm&#8217;, #finds $VERSION LIBS = &gt; [&#8221;], #e.g., &#8216;-lm&#8217; DEFINE = &gt; &#8221;, #e.g., &#8216;-DHAVE_SOMETHING&#8217; INC = &gt; &#8221;, #e.g., &#8216;-I/usr/include/other&#8217;);</p>
<p> The file Mytest.pm should start with something like this: </p>
<p>package Mytest;<br />
use 5.008008;<br />
use strict;<br />
use warnings;<br />
require Exporter;<br />
our @ISA = qw(Exporter);<br />
our % EXPORT_TAGS = (&#8216;all&#8217; = &gt; [qw()]);<br />
our @EXPORT_OK = (@{$EXPORT_TAGS{&#8216;all&#8217;}});<br />
our @EXPORT = qw();<br />
our $VERSION = &#8216;0.01&#8217;;<br />
require XSLoader;<br />
XSLoader::load(&#8216;Mytest&#8217;, $VERSION);<br />
#Preloaded methods go here.<br />
1;<br />
__END__<br />
#Below is the stub of documentation for your module.You better<br />
#edit it !</p>
<p> The rest of the .pm file contains sample code for providing documentation for the extension. </p>
<p> Finally, the Mytest.xs file should look something like this: </p>
<p>#define PERL_NO_GET_CONTEXT<br />
#include &#8220;EXTERN.h&#8221;<br />
#include &#8220;XSUB.h&#8221;<br />
#include &#8220;perl.h&#8221;<br />
#include &#8220;ppport.h&#8221;<br />
MODULE = Mytest PACKAGE = Mytest</p>
<p> Let&#8217;s edit the .xs file by adding this to the end of the file: </p>
<p>void hello()<br />
    CODE : printf(&#8220;Hello, world!
&#8221;);</p>
<p> It is okay for the lines starting at the &#8220;<font SIZE="-1">CODE:&#8221;</font> line to not be indented. However, for readability purposes, it is suggested that you indent <font SIZE="-1">CODE:</font> one level and the lines following one more level. </p>
<p> Now we&#8217;ll run &quot;<tt>&quot;perl Makefile.PL&quot;</tt>&quot;. This will create a real Makefile, which make needs. Its output looks something like: </p>
<pre>
    % perl Makefile.PL
    Checking if your kit is complete...
    Looks good
    Writing Makefile for Mytest
    %
</pre>
<p> Now, running make will produce output that looks something like this (some long lines have been shortened for clarity and some extraneous lines have been deleted): </p>
<pre>
 % make
 cp lib/Mytest.pm blib/lib/Mytest.pm
 perl xsubpp  -typemap typemap  Mytest.xs &gt; Mytest.xsc &amp;&amp; \
 mv Mytest.xsc Mytest.c
 Please specify prototyping behavior for Mytest.xs (see perlxs manual)
 cc -c     Mytest.c
 Running Mkbootstrap for Mytest ()
 chmod 644 Mytest.bs
 rm -f blib/arch/auto/Mytest/Mytest.so
 cc -shared -L/usr/local/lib Mytest.o -o blib/arch/auto/Mytest/Mytest.so
 chmod 755 blib/arch/auto/Mytest/Mytest.so
 cp Mytest.bs blib/arch/auto/Mytest/Mytest.bs
 chmod 644 blib/arch/auto/Mytest/Mytest.bs
 Manifying blib/man3/Mytest.3pm
 %
</pre>
<p> You can safely ignore the line about &#8220;prototyping behavior&#8221; &#8211; it is explained in &#8220;The <font SIZE="-1">PROTOTYPES:</font> Keyword&#8221; in perlxs. </p>
<p> Perl has its own special way of easily writing test scripts, but for this example only, we&#8217;ll create our own test script. Create a file called hello that looks like this: </p>
<p>#!/ opt / perl5 / bin / perl<br />
use ExtUtils::testlib;<br />
use Mytest;<br />
Mytest::hello();</p>
<p> Now we make the script executable (<tt>&quot;chmod +x hello&quot;</tt>), run the script and we should see the following output: </p>
<pre>
    % ./hello
    Hello, world!
    %
</pre>
<h3><font SIZE="-1">EXAMPLE 2</font></h3>
<p> Now let&#8217;s add to our extension a subroutine that will take a single numeric argument as input and return 1 if the number is even or 0 if the number is odd. </p>
<p> Add the following to the end of Mytest.xs: </p>
<p>int is_even(input)<br />
int input<br />
    CODE : RETVAL = (input % 2 == 0);<br />
OUTPUT : RETVAL</p>
<p> There does not need to be whitespace at the start of the &quot;<tt>&quot;int input&quot;</tt>&#8220; line, but it is useful for improving readability. Placing a semi-colon at the end of that line is also optional. Any amount and kind of whitespace may be placed between the &#8221;<tt>&quot;int&quot;</tt>&#8220; and &#8221;<tt>&quot;input&quot;</tt>&quot;. </p>
<p> Now re-run make to rebuild our new shared library. </p>
<p> Now perform the same steps as before, generating a Makefile from the Makefile.PL file, and running make. </p>
<p> In order to test that our extension works, we now need to look at the file Mytest.t. This file is set up to imitate the same kind of testing structure that Perl itself has. Within the test script, you perform a number of tests to confirm the behavior of the extension, printing &#8220;ok&#8221; when the test is correct, &#8220;not ok&#8221; when it is not. </p>
<p>use Test::More tests = &gt; 4;<br />
BEGIN{use_ok(&#8216;Mytest&#8217;)};<br />
######################## #<br />
#Insert your test code below, the Test::More module is use() ed here<br />
#so read its man page(perldoc Test::More) for help writing this<br />
#test script.<br />
    is(&amp;Mytest::is_even(0), 1);<br />
is(&amp;Mytest::is_even(1), 0);<br />
is(&amp;Mytest::is_even(2), 1);</p>
<p> We will be calling the test script through the command &quot;<tt>&quot;make test&quot;</tt>&quot;. You should see output that looks something like this: </p>
<pre>
 %make test
 PERL_DL_NONLAZY=1 /usr/bin/perl &quot;-MExtUtils::Command::MM&quot; &quot;-e&quot;
 &quot;test_harness(0, 'blib/lib', 'blib/arch')&quot; t/*.t
 t/Mytest....ok
 All tests successful.
 Files=1, Tests=4, 0 wallclock secs ( 0.03 cusr + 0.00 csys = 0.03 CPU)
 %
</pre>
<h3>What has gone on?</h3>
<p> The program h2xs is the starting point for creating extensions. In later examples we&#8217;ll see how we can use h2xs to read header files and generate templates to connect to C routines. </p>
<p> h2xs creates a number of files in the extension directory. The file Makefile.PL is a perl script which will generate a true Makefile to build the extension. We&#8217;ll take a closer look at it later. </p>
<p> The .pm and .xs files contain the meat of the extension. The .xs file holds the C routines that make up the extension. The .pm file contains routines that tell Perl how to load your extension. </p>
<p> Generating the Makefile and running <tt>&quot;make&quot;</tt> created a directory called blib (which stands for &#8220;build library&#8221;) in the current working directory. This directory will contain the shared library that we will build. Once we have tested it, we can install it into its final location. </p>
<p> Invoking the test script via &quot;<tt>&quot;make test&quot;</tt>&quot; did something very important. It invoked perl with all those <tt>&quot;-I&quot;</tt> arguments so that it could find the various files that are part of the extension. It is <i>very</i> important that while you are still testing extensions that you use &quot;<tt>&quot;make test&quot;</tt>&#8220;. If you try to run the test script all by itself, you will get a fatal error. Another reason it is important to use &#8221;<tt>&quot;make test&quot;</tt>&#8220; to run your test script is that if you are testing an upgrade to an already-existing version, using &#8221;<tt>&quot;make test&quot;</tt>&quot; ensures that you will test your new extension, not the already-existing version. </p>
<p> When Perl sees a <tt>&quot;use extension;&quot;</tt>, it searches for a file with the same name as the <tt>&quot;use&quot;</tt>&#8216;d extension that has a .pm suffix. If that file cannot be found, Perl dies with a fatal error. The default search path is contained in the <tt>@INC</tt> array. </p>
<p> In our case, Mytest.pm tells perl that it will need the Exporter and Dynamic Loader extensions. It then sets the <tt>@ISA</tt> and <tt>@EXPORT</tt> arrays and the <tt>$VERSION</tt> scalar; finally it tells perl to bootstrap the module. Perl will call its dynamic loader routine (if there is one) and load the shared library. </p>
<p> The two arrays <tt>@ISA</tt> and <tt>@EXPORT</tt> are very important. The <tt>@ISA</tt> array contains a list of other packages in which to search for methods (or subroutines) that do not exist in the current package. This is usually only important for object-oriented extensions (which we will talk about much later), and so usually doesn&#8217;t need to be modified. </p>
<p> The <tt>@EXPORT</tt> array tells Perl which of the extension&#8217;s variables and subroutines should be placed into the calling package&#8217;s namespace. Because you don&#8217;t know if the user has already used your variable and subroutine names, it&#8217;s vitally important to carefully select what to export. Do <i>not</i> export method or variable names <i>by default</i> without a good reason. </p>
<p> As a general rule, if the module is trying to be object-oriented then don&#8217;t export anything. If it&#8217;s just a collection of functions and variables, then you can export them via another array, called <tt>@EXPORT_OK</tt>. This array does not automatically place its subroutine and variable names into the namespace unless the user specifically requests that this be done. </p>
<p> See perlmod for more information. </p>
<p> The <tt>$VERSION</tt> variable is used to ensure that the .pm file and the shared library are &#8220;in sync&#8221; with each other. Any time you make changes to the .pm or .xs files, you should increment the value of this variable.</p>
<h3>Writing good test scripts</h3>
<p> The importance of writing good test scripts cannot be over-emphasized. You should closely follow the &#8220;ok/not ok&#8221; style that Perl itself uses, so that it is very easy and unambiguous to determine the outcome of each test case. When you find and fix a bug, make sure you add a test case for it. </p>
<p> By running &quot;<tt>&quot;make test&quot;</tt>&#8220;, you ensure that your Mytest.t script runs and uses the correct version of your extension. If you have many test cases, save your test files in the &#8221;t&#8220; directory and use the suffix &#8221;.t&#8220;. When you run &#8221;<tt>&quot;make test&quot;</tt>&quot;, all of these test files will be executed.</p>
<h3><font SIZE="-1">EXAMPLE 3</font></h3>
<p> Our third extension will take one argument as its input, round off that value, and set the <i>argument</i> to the rounded value. </p>
<p> Add the following to the end of Mytest.xs: </p>
<p>void round(arg) double arg<br />
    CODE : if (arg &gt; 0.0)<br />
{<br />
    arg = floor(arg + 0.5);<br />
}<br />
else if (arg &lt; 0.0)<br />
{<br />
    arg = ceil(arg &#8211; 0.5);<br />
}<br />
else<br />
{<br />
    arg = 0.0;<br />
}<br />
OUTPUT : arg</p>
<p> Edit the Makefile.PL file so that the corresponding line looks like this: </p>
<pre>
        'LIBS'      =&gt; ['-lm'],   # e.g., '-lm'
</pre>
<p> Generate the Makefile and run make. Change the test number in Mytest.t to &#8220;9&#8221; and add the following tests: </p>
<p>$i = -1.5;<br />
&amp;Mytest::round($i);<br />
is($i, -2.0);<br />
$i = -1.1;<br />
&amp;Mytest::round($i);<br />
is($i, -1.0);<br />
$i = 0.0;<br />
&amp;Mytest::round($i);<br />
is($i, 0.0);<br />
$i = 0.5;<br />
&amp;Mytest::round($i);<br />
is($i, 1.0);<br />
$i = 1.2;<br />
&amp;Mytest::round($i);<br />
is($i, 1.0);</p>
<p> Running &quot;<tt>&quot;make test&quot;</tt>&quot; should now print out that all nine tests are okay. </p>
<p> Notice that in these new test cases, the argument passed to round was a scalar variable. You might be wondering if you can round a constant or literal. To see what happens, temporarily add the following line to Mytest.t: </p>
<pre>
        &amp;<a href="//www.systutorials.com/docs/linux/man/3-Mytest::round/">Mytest::round</a>(3);
</pre>
<p> Run &quot;<tt>&quot;make test&quot;</tt>&quot; and notice that Perl dies with a fatal error. Perl won&#8217;t let you change the value of constants!</p>
<h3>What&#8217;s new here?</h3>
<dl>
<dt>&bull;</p>
<dd> We&#8217;ve made some changes to Makefile.PL. In this case, we&#8217;ve specified an extra library to be linked into the extension&#8217;s shared library, the math library libm in this case. We&#8217;ll talk later about how to write XSUBs that can call every routine in a library.</p>
<dt>&bull;</p>
<dd> The value of the function is not being passed back as the function&#8217;s return value, but by changing the value of the variable that was passed into the function. You might have guessed that when you saw that the return value of round is of type &#8220;void&#8221;.</dl>
<h3>Input and Output Parameters</h3>
<p> You specify the parameters that will be passed into the <font SIZE="-1">XSUB</font> on the line(s) after you declare the function&#8217;s return value and name. Each input parameter line starts with optional whitespace, and may have an optional terminating semicolon. </p>
<p> The list of output parameters occurs at the very end of the function, just after the <font SIZE="-1">OUTPUT:</font> directive. The use of <font SIZE="-1">RETVAL</font> tells Perl that you wish to send this value back as the return value of the <font SIZE="-1">XSUB</font> function. In Example 3, we wanted the &#8220;return value&#8221; placed in the original variable which we passed in, so we listed it (and not <font SIZE="-1">RETVAL</font>) in the <font SIZE="-1">OUTPUT:</font> section.</p>
<h3>The <font SIZE="-1">XSUBPP</font> Program</h3>
<p> The <code>xsubpp</code> program takes the <font SIZE="-1">XS</font> code in the .xs file and translates it into C code, placing it in a file whose suffix is .c. The C code created makes heavy use of the C functions within Perl.</p>
<h3>The <font SIZE="-1">TYPEMAP</font> file</h3>
<p> The <code>xsubpp</code> program uses rules to convert from Perl&#8217;s data types (scalar, array, etc.) to C&#8217;s data types (int, char, etc.). These rules are stored in the typemap file ($PERLLIB/ExtUtils/typemap). There&#8217;s a brief discussion below, but all the nitty-gritty details can be found in perlxstypemap. If you have a new-enough version of perl (5.16 and up) or an upgraded <font SIZE="-1">XS</font> compiler (<tt>&quot;ExtUtils::ParseXS&quot;</tt> 3.13_01 or better), then you can inline typemaps in your <font SIZE="-1">XS</font> instead of writing separate files. Either way, this typemap thing is split into three parts: </p>
<p> The first section maps various C data types to a name, which corresponds somewhat with the various Perl types. The second section contains C code which <code>xsubpp</code> uses to handle input parameters. The third section contains C code which <code>xsubpp</code> uses to handle output parameters. </p>
<p> Let&#8217;s take a look at a portion of the .c file created for our extension. The file name is Mytest.c: </p>
<p>XS(XS_Mytest_round)<br />
{<br />
    dXSARGS;<br />
    if (items != 1)<br />
        Perl_croak(aTHX_ &#8220;Usage: Mytest::round(arg)&#8221;);<br />
    PERL_UNUSED_VAR(cv); /* -W */<br />
    {<br />
        double arg = (double)SvNV(ST(0)); /* XXXXX */<br />
        if (arg &gt; 0.0) {<br />
            arg = floor(arg + 0.5);<br />
        } else if (arg &lt; 0.0) {<br />
            arg = ceil(arg &#8211; 0.5);<br />
        } else {<br />
            arg = 0.0;<br />
        }<br />
        sv_setnv(ST(0), (double)arg); /* XXXXX */<br />
        SvSETMAGIC(ST(0));<br />
    }<br />
    XSRETURN_EMPTY;<br />
}</p>
<p> Notice the two lines commented with &#8220;<font SIZE="-1">XXXXX&#8221;.</font> If you check the first part of the typemap file (or section), you&#8217;ll see that doubles are of type T_DOUBLE. In the <font SIZE="-1">INPUT</font> part of the typemap, an argument that is T_DOUBLE is assigned to the variable arg by calling the routine SvNV on something, then casting it to double, then assigned to the variable arg. Similarly, in the <font SIZE="-1">OUTPUT</font> section, once arg has its final value, it is passed to the sv_setnv function to be passed back to the calling subroutine. These two functions are explained in perlguts; we&#8217;ll talk more later about what that &#8220;<font SIZE="-1"><code>ST</code></font>(0)&#8221; means in the section on the argument stack.</p>
<h3>Warning about Output Arguments</h3>
<p> In general, it&#8217;s not a good idea to write extensions that modify their input parameters, as in Example 3. Instead, you should probably return multiple values in an array and let the caller handle them (we&#8217;ll do this in a later example). However, in order to better accommodate calling pre-existing C routines, which often do modify their input parameters, this behavior is tolerated.</p>
<h3><font SIZE="-1">EXAMPLE 4</font></h3>
<p> In this example, we&#8217;ll now begin to write XSUBs that will interact with pre-defined C libraries. To begin with, we will build a small library of our own, then let h2xs write our .pm and .xs files for us. </p>
<p> Create a new directory called Mytest2 at the same level as the directory Mytest. In the Mytest2 directory, create another directory called mylib, and cd into that directory. </p>
<p> Here we&#8217;ll create some files that will generate a test library. These will include a C source file and a header file. We&#8217;ll also create a Makefile.PL in this directory. Then we&#8217;ll make sure that running make at the Mytest2 level will automatically run this Makefile.PL file and the resulting Makefile. </p>
<p> In the mylib directory, create a file mylib.h that looks like this: </p>
<p>#define TESTVAL 4<br />
extern double foo(int, long, const char *);</p>
<p> Also create a file mylib.c that looks like this: </p>
<p>#include &#8220;./mylib.h&#8221;<br />
#include &lt;stdlib.h&gt;<br />
double<br />
foo(int a, long b, const char *c)<br />
{<br />
    return (a + b + atof(c) + TESTVAL);<br />
}</p>
<p> And finally create a file Makefile.PL that looks like this: </p>
<p>use ExtUtils::MakeMaker;<br />
$Verbose = 1;<br />
WriteMakefile(<br />
    NAME = &gt; &#8216;Mytest2::mylib&#8217;,<br />
    SKIP = &gt; [qw(all static static_lib dynamic dynamic_lib)],<br />
    clean = &gt; {&#8216;FILES&#8217; = &gt; &#8216;libmylib$(LIB_EXT)&#8217;}, );<br />
sub MY::top_targets<br />
{<br />
    &#8216; all ::static pure_all ::static static ::libmylib$(LIB_EXT)<br />
        libmylib$(LIB_EXT)<br />
        : $(O_FILES)<br />
              $(AR) cr<br />
              libmylib$(LIB_EXT) $(O_FILES)<br />
                  $(RANLIB) libmylib$(LIB_EXT)<br />
        &#8216;;<br />
}</p>
<p> Make sure you use a tab and not spaces on the lines beginning with &#8220;$(<font SIZE="-1">AR</font>)&#8221; and &#8220;$(<font SIZE="-1">RANLIB</font>)&#8221;. Make will not function properly if you use spaces. It has also been reported that the &#8220;cr&#8221; argument to $(<font SIZE="-1">AR</font>) is unnecessary on Win32 systems. </p>
<p> We will now create the main top-level Mytest2 files. Change to the directory above Mytest2 and run the following command: </p>
<pre>
        % h2xs -O -n Mytest2 ./Mytest2/mylib/mylib.h
</pre>
<p> This will print out a warning about overwriting Mytest2, but that&#8217;s okay. Our files are stored in Mytest2/mylib, and will be untouched. </p>
<p> The normal Makefile.PL that h2xs generates doesn&#8217;t know about the mylib directory. We need to tell it that there is a subdirectory and that we will be generating a library in it. Let&#8217;s add the argument <font SIZE="-1">MYEXTLIB</font> to the WriteMakefile call so that it looks like this: </p>
<p>WriteMakefile(<br />
    &#8216;NAME&#8217; = &gt; &#8216;Mytest2&#8217;,<br />
    &#8216;VERSION_FROM&#8217; = &gt; &#8216;Mytest2.pm&#8217;, #finds $VERSION &#8216;LIBS&#8217; = &gt; [&#8221;], #e.g., &#8216;-lm&#8217; &#8216;DEFINE&#8217; = &gt; &#8221;, #e.g., &#8216;-DHAVE_SOMETHING&#8217; &#8216;INC&#8217; = &gt; &#8221;, #e.g., &#8216;-I/usr/include/other&#8217; &#8216;MYEXTLIB&#8217; = &gt; &#8216;mylib/libmylib$(LIB_EXT)&#8217;, );</p>
<p> and then at the end add a subroutine (which will override the pre-existing subroutine). Remember to use a tab character to indent the line beginning with &#8220;cd&#8221;! </p>
<p>sub MY::postamble<br />
{<br />
    &#8216; $(MYEXTLIB)<br />
        : mylib / Makefile<br />
                      cd mylib &amp;&amp;<br />
        $(MAKE) $(PASSTHRU)<br />
        &#8216;;<br />
}</p>
<p> Let&#8217;s also fix the <font SIZE="-1">MANIFEST</font> file so that it accurately reflects the contents of our extension. The single line that says &#8220;mylib&#8221; should be replaced by the following three lines: </p>
<pre>
        mylib/Makefile.PL
        mylib/mylib.c
        mylib/mylib.h
</pre>
<p> To keep our namespace nice and unpolluted, edit the .pm file and change the variable <tt>@EXPORT</tt> to <tt>@EXPORT_OK</tt>. Finally, in the .xs file, edit the #include line to read: </p>
<p>#include &#8220;mylib/mylib.h&#8221;</p>
<p> And also add the following function definition to the end of the .xs file: </p>
<p>double<br />
foo(a, b, c)<br />
int a long b const char *c<br />
    OUTPUT : RETVAL</p>
<p> Now we also need to create a typemap because the default Perl doesn&#8217;t currently support the <tt>&quot;const char *&quot;</tt> type. Include a new <font SIZE="-1">TYPEMAP</font> section in your <font SIZE="-1">XS</font> code before the above function: </p>
<pre>
        TYPEMAP: &lt;&lt;END
        const char *    T_PV
        END
</pre>
<p> Now run perl on the top-level Makefile.PL. Notice that it also created a Makefile in the mylib directory. Run make and watch that it does cd into the mylib directory and run make in there as well. </p>
<p> Now edit the Mytest2.t script and change the number of tests to &#8220;4&#8221;, and add the following lines to the end of the script: </p>
<p>is(&amp;Mytest2::foo(1, 2, &#8220;Hello, world!&#8221;), 7);<br />
is(&amp;Mytest2::foo(1, 2, &#8220;0.0&#8221;), 7);<br />
ok(abs(&amp;Mytest2::foo(0, 0, &#8220;-3.4&#8221;) &#8211; 0.6) &lt;= 0.01);</p>
<p> (When dealing with floating-point comparisons, it is best to not check for equality, but rather that the difference between the expected and actual result is below a certain amount (called epsilon) which is 0.01 in this case) </p>
<p> Run &quot;<tt>&quot;make test&quot;</tt>&quot; and all should be well. There are some warnings on missing tests for the Mytest2::mylib extension, but you can ignore them.</p>
<h3>What has happened here?</h3>
<p> Unlike previous examples, we&#8217;ve now run h2xs on a real include file. This has caused some extra goodies to appear in both the .pm and .xs files.</p>
<dl>
<dt>&bull;</p>
<dd> In the .xs file, there&#8217;s now a #include directive with the absolute path to the mylib.h header file. We changed this to a relative path so that we could move the extension directory if we wanted to.</p>
<dt>&bull;</p>
<dd> There&#8217;s now some new C code that&#8217;s been added to the .xs file. The purpose of the <tt>&quot;constant&quot;</tt> routine is to make the values that are #define&#8217;d in the header file accessible by the Perl script (by calling either <tt>&quot;TESTVAL&quot;</tt> or <tt>&amp;Mytest2::TESTVAL</tt>). There&#8217;s also some <font SIZE="-1">XS</font> code to allow calls to the <tt>&quot;constant&quot;</tt> routine.</p>
<dt>&bull;</p>
<dd> The .pm file originally exported the name <tt>&quot;TESTVAL&quot;</tt> in the <tt>@EXPORT</tt> array. This could lead to name clashes. A good rule of thumb is that if the #define is only going to be used by the C routines themselves, and not by the user, they should be removed from the <tt>@EXPORT</tt> array. Alternately, if you don&#8217;t mind using the &#8220;fully qualified name&#8221; of a variable, you could move most or all of the items from the <tt>@EXPORT</tt> array into the <tt>@EXPORT_OK</tt> array.</p>
<dt>&bull;</p>
<dd> If our include file had contained #include directives, these would not have been processed by h2xs. There is no good solution to this right now.</p>
<dt>&bull;</p>
<dd> We&#8217;ve also told Perl about the library that we built in the mylib subdirectory. That required only the addition of the <tt>&quot;MYEXTLIB&quot;</tt> variable to the WriteMakefile call and the replacement of the postamble subroutine to cd into the subdirectory and run make. The Makefile.PL for the library is a bit more complicated, but not excessively so. Again we replaced the postamble subroutine to insert our own code. This code simply specified that the library to be created here was a static archive library (as opposed to a dynamically loadable library) and provided the commands to build it.</dl>
<h3>Anatomy of .xs file</h3>
<p> The .xs file of &#8220;<font SIZE="-1">EXAMPLE 4&#8221;</font> contained some new elements. To understand the meaning of these elements, pay attention to the line which reads </p>
<pre>
        MODULE = Mytest2                PACKAGE = Mytest2
</pre>
<p> Anything before this line is plain C code which describes which headers to include, and defines some convenience functions. No translations are performed on this part, apart from having embedded <font SIZE="-1">POD</font> documentation skipped over (see perlpod) it goes into the generated output C file as is. </p>
<p> Anything after this line is the description of <font SIZE="-1">XSUB</font> functions. These descriptions are translated by <code>xsubpp</code> into C code which implements these functions using Perl calling conventions, and which makes these functions visible from Perl interpreter. </p>
<p> Pay a special attention to the function <tt>&quot;constant&quot;</tt>. This name appears twice in the generated .xs file: once in the first part, as a static C function, then another time in the second part, when an <font SIZE="-1">XSUB</font> interface to this static C function is defined. </p>
<p> This is quite typical for .xs files: usually the .xs file provides an interface to an existing C function. Then this C function is defined somewhere (either in an external library, or in the first part of .xs file), and a Perl interface to this function (i.e. &#8220;Perl glue&#8221;) is described in the second part of .xs file. The situation in &#8220;<font SIZE="-1">EXAMPLE 1&#8221;</font>, &#8220;<font SIZE="-1">EXAMPLE 2&#8221;</font>, and &#8220;<font SIZE="-1">EXAMPLE 3&#8221;</font>, when all the work is done inside the &#8220;Perl glue&#8221;, is somewhat of an exception rather than the rule.</p>
<h3>Getting the fat out of XSUBs</h3>
<p> In &#8220;<font SIZE="-1">EXAMPLE 4&#8221;</font> the second part of .xs file contained the following description of an <font SIZE="-1">XSUB:</font> </p>
<p>double<br />
foo(a, b, c)<br />
int a long b const char *c<br />
    OUTPUT : RETVAL</p>
<p> Note that in contrast with &#8220;<font SIZE="-1">EXAMPLE 1&#8221;</font>, &#8220;<font SIZE="-1">EXAMPLE 2&#8221;</font> and &#8220;<font SIZE="-1">EXAMPLE 3&#8221;</font>, this description does not contain the actual <i>code</i> for what is done during a call to Perl function <code>foo()</code>. To understand what is going on here, one can add a <font SIZE="-1">CODE</font> section to this <font SIZE="-1">XSUB:</font> </p>
<p>double<br />
foo(a, b, c)<br />
int a long b const char *c<br />
    CODE : RETVAL = foo(a, b, c);<br />
OUTPUT : RETVAL</p>
<p> However, these two XSUBs provide almost identical generated C code: <code>xsubpp</code> compiler is smart enough to figure out the <tt>&quot;CODE:&quot;</tt> section from the first two lines of the description of <font SIZE="-1">XSUB.</font> What about <tt>&quot;OUTPUT:&quot;</tt> section? In fact, that is absolutely the same! The <tt>&quot;OUTPUT:&quot;</tt> section can be removed as well, <i>as far as </i>&quot;CODE:&quot;<i> section or </i>&quot;PPCODE:&quot;<i> section</i> is not specified: <code>xsubpp</code> can see that it needs to generate a function call section, and will autogenerate the <font SIZE="-1">OUTPUT</font> section too. Thus one can shortcut the <font SIZE="-1">XSUB</font> to become: </p>
<p>double<br />
foo(a, b, c)<br />
int a long b const char *c</p>
<p> Can we do the same with an <font SIZE="-1">XSUB</font> </p>
<p>int is_even(input)<br />
int input<br />
    CODE : RETVAL = (input % 2 == 0);<br />
OUTPUT : RETVAL</p>
<p> of &#8220;<font SIZE="-1">EXAMPLE 2&#8221;</font>? To do this, one needs to define a C function <tt>&quot;int is_even(int input)&quot;</tt>. As we saw in &#8220;Anatomy of .xs file&#8221;, a proper place for this definition is in the first part of .xs file. In fact a C function </p>
<p>int is_even(int arg)<br />
{<br />
    return (arg % 2 == 0);<br />
}</p>
<p> is probably overkill for this. Something as simple as a <tt>&quot;#define&quot;</tt> will do too: </p>
<p>#define is_even(arg) ((arg) % 2 == 0)</p>
<p> After having this in the first part of .xs file, the &#8220;Perl glue&#8221; part becomes as simple as </p>
<pre>
        int
        is_even(input)
                int     input
</pre>
<p> This technique of separation of the glue part from the workhorse part has obvious tradeoffs: if you want to change a Perl interface, you need to change two places in your code. However, it removes a lot of clutter, and makes the workhorse part independent from idiosyncrasies of Perl calling convention. (In fact, there is nothing Perl-specific in the above description, a different version of <code>xsubpp</code> might have translated this to <font SIZE="-1">TCL</font> glue or Python glue as well.)</p>
<h3>More about <font SIZE="-1">XSUB</font> arguments</h3>
<p> With the completion of Example 4, we now have an easy way to simulate some real-life libraries whose interfaces may not be the cleanest in the world. We shall now continue with a discussion of the arguments passed to the <code>xsubpp</code> compiler. </p>
<p> When you specify arguments to routines in the .xs file, you are really passing three pieces of information for each argument listed. The first piece is the order of that argument relative to the others (first, second, etc). The second is the type of argument, and consists of the type declaration of the argument (e.g., int, char*, etc). The third piece is the calling convention for the argument in the call to the library function. </p>
<p> While Perl passes arguments to functions by reference, C passes arguments by value; to implement a C function which modifies data of one of the &#8220;arguments&#8221;, the actual argument of this C function would be a pointer to the data. Thus two C functions with declarations </p>
<p>int string_length(char *s);<br />
int upper_case_char(char *cp);</p>
<p> may have completely different semantics: the first one may inspect an array of chars pointed by s, and the second one may immediately dereference <tt>&quot;cp&quot;</tt> and manipulate <tt>*cp</tt> only (using the return value as, say, a success indicator). From Perl one would use these functions in a completely different manner. </p>
<p> One conveys this info to <code>xsubpp</code> by replacing <tt>&quot;*&quot;</tt> before the argument by <tt>&quot;&amp;&quot;</tt>. <tt>&quot;&amp;&quot;</tt> means that the argument should be passed to a library function by its address. The above two function may be XSUB-ified as </p>
<p>int string_length(s)<br />
char *s int<br />
upper_case_char(cp) char &amp;cp</p>
<p> For example, consider: </p>
<pre>
        int
        foo(a,b)
                char    &amp;a
                char *  b
</pre>
<p> The first Perl argument to this function would be treated as a char and assigned to the variable a, and its address would be passed into the function foo. The second Perl argument would be treated as a string pointer and assigned to the variable b. The <i>value</i> of b would be passed into the function foo. The actual call to the function foo that <code>xsubpp</code> generates would look like this: </p>
<pre>
        foo(&amp;a, b);
</pre>
<p> <code>xsubpp</code> will parse the following function argument lists identically: </p>
<pre>
        char    &amp;a
        char&amp;a
        char    &amp; a
</pre>
<p> However, to help ease understanding, it is suggested that you place a &#8220;&amp;&#8221; next to the variable name and away from the variable type), and place a &#8220;*&#8221; near the variable type, but away from the variable name (as in the call to foo above). By doing so, it is easy to understand exactly what will be passed to the C function; it will be whatever is in the &#8220;last column&#8221;. </p>
<p> You should take great pains to try to pass the function the type of variable it wants, when possible. It will save you a lot of trouble in the long run.</p>
<h3>The Argument Stack</h3>
<p> If we look at any of the C code generated by any of the examples except example 1, you will notice a number of references to <font SIZE="-1"><a href="/docs/linux/man/n-st/">ST</a></font>(n), where n is usually 0. &#8220;<font SIZE="-1">ST&#8221;</font> is actually a macro that points to the n&#8217;th argument on the argument stack. <font SIZE="-1"><code>ST</code></font>(0) is thus the first argument on the stack and therefore the first argument passed to the <font SIZE="-1">XSUB, <code><a href="/docs/linux/man/1-st/">ST</a></code></font>(1) is the second argument, and so on. </p>
<p> When you list the arguments to the <font SIZE="-1">XSUB</font> in the .xs file, that tells <code>xsubpp</code> which argument corresponds to which of the argument stack (i.e., the first one listed is the first argument, and so on). You invite disaster if you do not list them in the same order as the function expects them. </p>
<p> The actual values on the argument stack are pointers to the values passed in. When an argument is listed as being an <font SIZE="-1">OUTPUT</font> value, its corresponding value on the stack (i.e., <font SIZE="-1"><code>ST</code></font>(0) if it was the first argument) is changed. You can verify this by looking at the C code generated for Example 3. The code for the <code>round()</code> <font SIZE="-1">XSUB</font> routine contains lines that look like this: </p>
<p>double arg = (double)SvNV(ST(0));<br />
/* Round the contents of the variable arg */<br />
sv_setnv(ST(0), (double)arg);</p>
<p> The arg variable is initially set by taking the value from <font SIZE="-1"><code>ST</code></font>(0), then is stored back into <font SIZE="-1"><code>ST</code></font>(0) at the end of the routine. </p>
<p> XSUBs are also allowed to return lists, not just scalars. This must be done by manipulating stack values <font SIZE="-1"><code>ST</code></font>(0), <font SIZE="-1"><code><a href="/docs/linux/man/1-st/">ST</a></code></font>(1), etc, in a subtly different way. See perlxs for details. </p>
<p> XSUBs are also allowed to avoid automatic conversion of Perl function arguments to C function arguments. See perlxs for details. Some people prefer manual conversion by inspecting <tt>ST(i)</tt> even in the cases when automatic conversion will do, arguing that this makes the logic of an <font SIZE="-1">XSUB</font> call clearer. Compare with &#8220;Getting the fat out of XSUBs&#8221; for a similar tradeoff of a complete separation of &#8220;Perl glue&#8221; and &#8220;workhorse&#8221; parts of an <font SIZE="-1">XSUB.</font> </p>
<p> While experts may argue about these idioms, a novice to Perl guts may prefer a way which is as little Perl-guts-specific as possible, meaning automatic conversion and automatic call generation, as in &#8220;Getting the fat out of XSUBs&#8221;. This approach has the additional benefit of protecting the <font SIZE="-1">XSUB</font> writer from future changes to the Perl <font SIZE="-1">API.</font></p>
<h3>Extending your Extension</h3>
<p> Sometimes you might want to provide some extra methods or subroutines to assist in making the interface between Perl and your extension simpler or easier to understand. These routines should live in the .pm file. Whether they are automatically loaded when the extension itself is loaded or only loaded when called depends on where in the .pm file the subroutine definition is placed. You can also consult AutoLoader for an alternate way to store and load your extra subroutines.</p>
<h3>Documenting your Extension</h3>
<p> There is absolutely no excuse for not documenting your extension. Documentation belongs in the .pm file. This file will be fed to pod2man, and the embedded documentation will be converted to the manpage format, then placed in the blib directory. It will be copied to Perl&#8217;s manpage directory when the extension is installed. </p>
<p> You may intersperse documentation and Perl code within the .pm file. In fact, if you want to use method autoloading, you must do this, as the comment inside the .pm file explains. </p>
<p> See perlpod for more information about the pod format.</p>
<h3>Installing your Extension</h3>
<p> Once your extension is complete and passes all its tests, installing it is quite simple: you simply run &#8220;make install&#8221;. You will either need to have write permission into the directories where Perl is installed, or ask your system administrator to run the make for you. </p>
<p> Alternately, you can specify the exact directory to place the extension&#8217;s files by placing a &#8220;PREFIX=/destination/directory&#8221; after the make install (or in between the make and install if you have a brain-dead version of make). This can be very useful if you are building an extension that will eventually be distributed to multiple systems. You can then just archive the files in the destination directory and distribute them to your destination systems.</p>
<h3><font SIZE="-1">EXAMPLE 5</font></h3>
<p> In this example, we&#8217;ll do some more work with the argument stack. The previous examples have all returned only a single value. We&#8217;ll now create an extension that returns an array. </p>
<p> This extension is very Unix-oriented (struct statfs and the statfs system call). If you are not running on a Unix system, you can substitute for statfs any other function that returns multiple values, you can hard-code values to be returned to the caller (although this will be a bit harder to test the error case), or you can simply not do this example. If you change the <font SIZE="-1">XSUB,</font> be sure to fix the test cases to match the changes. </p>
<p> Return to the Mytest directory and add the following code to the end of Mytest.xs: </p>
<p>void<br />
    statfs(path) char *path<br />
    INIT : int i;<br />
struct statfs buf;<br />
PPCODE : i = statfs(path, &amp;buf);<br />
if (i == 0) {<br />
    XPUSHs(sv_2mortal(newSVnv(buf.f_bavail)));<br />
    XPUSHs(sv_2mortal(newSVnv(buf.f_bfree)));<br />
    XPUSHs(sv_2mortal(newSVnv(buf.f_blocks)));<br />
    XPUSHs(sv_2mortal(newSVnv(buf.f_bsize)));<br />
    XPUSHs(sv_2mortal(newSVnv(buf.f_ffree)));<br />
    XPUSHs(sv_2mortal(newSVnv(buf.f_files)));<br />
    XPUSHs(sv_2mortal(newSVnv(buf.f_type)));<br />
} else {<br />
    XPUSHs(sv_2mortal(newSVnv(errno)));<br />
}</p>
<p> You&#8217;ll also need to add the following code to the top of the .xs file, just after the include of &#8220;<font SIZE="-1">XSUB</font>.h&#8221;: </p>
<p>#include &lt;sys/vfs.h&gt;</p>
<p> Also add the following code segment to Mytest.t while incrementing the &#8220;9&#8221; tests to &#8220;11&#8221;: </p>
<p>@a = &amp;Mytest::statfs(&#8220;/blech&#8221;);<br />
ok(scalar(@a) == 1 &amp;&amp; $a[0] == 2);<br />
@a = &amp;Mytest::statfs(&#8220;/&#8221;);<br />
is(scalar(@a), 7);</p>
<h3>New Things in this Example</h3>
<p> This example added quite a few new concepts. We&#8217;ll take them one at a time.</p>
<dl>
<dt>&bull;</p>
<dd> The <font SIZE="-1">INIT:</font> directive contains code that will be placed immediately after the argument stack is decoded. C does not allow variable declarations at arbitrary locations inside a function, so this is usually the best way to declare local variables needed by the <font SIZE="-1">XSUB.</font> (Alternatively, one could put the whole <tt>&quot;PPCODE:&quot;</tt> section into braces, and put these declarations on top.)</p>
<dt>&bull;</p>
<dd> This routine also returns a different number of arguments depending on the success or failure of the call to statfs. If there is an error, the error number is returned as a single-element array. If the call is successful, then a 7-element array is returned. Since only one argument is passed into this function, we need room on the stack to hold the 7 values which may be returned. </p>
<p> We do this by using the <font SIZE="-1">PPCODE:</font> directive, rather than the <font SIZE="-1">CODE:</font> directive. This tells <code>xsubpp</code> that we will be managing the return values that will be put on the argument stack by ourselves.</p>
<dt>&bull;</p>
<dd> When we want to place values to be returned to the caller onto the stack, we use the series of macros that begin with &#8220;<font SIZE="-1">XPUSH&#8221;.</font> There are five different versions, for placing integers, unsigned integers, doubles, strings, and Perl scalars on the stack. In our example, we placed a Perl scalar onto the stack. (In fact this is the only macro which can be used to return multiple values.) </p>
<p> The XPUSH* macros will automatically extend the return stack to prevent it from being overrun. You push values onto the stack in the order you want them seen by the calling program.</p>
<dt>&bull;</p>
<dd> The values pushed onto the return stack of the <font SIZE="-1">XSUB</font> are actually mortal <font SIZE="-1">SV</font>&#8216;s. They are made mortal so that once the values are copied by the calling program, the <font SIZE="-1">SV</font>&#8216;s that held the returned values can be deallocated. If they were not mortal, then they would continue to exist after the <font SIZE="-1">XSUB</font> routine returned, but would not be accessible. This is a memory leak.</p>
<dt>&bull;</p>
<dd> If we were interested in performance, not in code compactness, in the success branch we would not use <tt>&quot;XPUSHs&quot;</tt> macros, but <tt>&quot;PUSHs&quot;</tt> macros, and would pre-extend the stack before pushing the return values: </p>
<pre>
        EXTEND(SP, 7);
</pre>
<p> The tradeoff is that one needs to calculate the number of return values in advance (though overextending the stack will not typically hurt anything but memory consumption). </p>
<p> Similarly, in the failure branch we could use <tt>&quot;PUSHs&quot;</tt> <i>without</i> extending the stack: the Perl function reference comes to an <font SIZE="-1">XSUB</font> on the stack, thus the stack is <i>always</i> large enough to take one return value.</dl>
<h3><font SIZE="-1">EXAMPLE 6</font></h3>
<p> In this example, we will accept a reference to an array as an input parameter, and return a reference to an array of hashes. This will demonstrate manipulation of complex Perl data types from an <font SIZE="-1">XSUB.</font> </p>
<p> This extension is somewhat contrived. It is based on the code in the previous example. It calls the statfs function multiple times, accepting a reference to an array of filenames as input, and returning a reference to an array of hashes containing the data for each of the filesystems. </p>
<p> Return to the Mytest directory and add the following code to the end of Mytest.xs: </p>
<p>SV *multi_statfs(paths)<br />
SV *paths<br />
    INIT : AV *results;<br />
SSize_t numpaths = 0, n;<br />
int i;<br />
struct statfs buf;<br />
SvGETMAGIC(paths);<br />
if ((!SvROK(paths)) || (SvTYPE(SvRV(paths)) != SVt_PVAV) || ((numpaths = av_top_index((AV *)SvRV(paths))) &lt; 0)) {<br />
    XSRETURN_UNDEF;<br />
}<br />
results = (AV *)sv_2mortal((SV *)newAV());<br />
CODE : for (n = 0; n &lt;= numpaths; n++)<br />
{<br />
    HV *rh;<br />
    STRLEN l;<br />
    char *fn = SvPV(*av_fetch((AV *)SvRV(paths), n, 0), l);<br />
    i = statfs(fn, &amp;buf);<br />
    if (i != 0) {<br />
        av_push(results, newSVnv(errno));<br />
        continue;<br />
    }<br />
    rh = (HV *)sv_2mortal((SV *)newHV());<br />
    hv_store(rh, &#8220;f_bavail&#8221;, 8, newSVnv(buf.f_bavail), 0);<br />
    hv_store(rh, &#8220;f_bfree&#8221;, 7, newSVnv(buf.f_bfree), 0);<br />
    hv_store(rh, &#8220;f_blocks&#8221;, 8, newSVnv(buf.f_blocks), 0);<br />
    hv_store(rh, &#8220;f_bsize&#8221;, 7, newSVnv(buf.f_bsize), 0);<br />
    hv_store(rh, &#8220;f_ffree&#8221;, 7, newSVnv(buf.f_ffree), 0);<br />
    hv_store(rh, &#8220;f_files&#8221;, 7, newSVnv(buf.f_files), 0);<br />
    hv_store(rh, &#8220;f_type&#8221;, 6, newSVnv(buf.f_type), 0);<br />
    av_push(results, newRV_inc((SV *)rh));<br />
}<br />
RETVAL = newRV_inc((SV *)results);<br />
OUTPUT : RETVAL</p>
<p> And add the following code to Mytest.t, while incrementing the &#8220;11&#8221; tests to &#8220;13&#8221;: </p>
<p>$results = Mytest::multi_statfs([ &#8216;/&#8217;, &#8216;/blech&#8217; ]);<br />
ok(ref $results-&gt;[0]);<br />
ok(!ref $results-&gt;[1]);</p>
<h3>New Things in this Example</h3>
<p> There are a number of new concepts introduced here, described below:</p>
<dl>
<dt>&bull;</p>
<dd> This function does not use a typemap. Instead, we declare it as accepting one SV* (scalar) parameter, and returning an SV* value, and we take care of populating these scalars within the code. Because we are only returning one value, we don&#8217;t need a <tt>&quot;PPCODE:&quot;</tt> directive &#8211; instead, we use <tt>&quot;CODE:&quot;</tt> and <tt>&quot;OUTPUT:&quot;</tt> directives.</p>
<dt>&bull;</p>
<dd> When dealing with references, it is important to handle them with caution. The <tt>&quot;INIT:&quot;</tt> block first calls SvGETMAGIC(paths), in case paths is a tied variable. Then it checks that <tt>&quot;SvROK&quot;</tt> returns true, which indicates that paths is a valid reference. (Simply checking <tt>&quot;SvROK&quot;</tt> won&#8217;t trigger <font SIZE="-1">FETCH</font> on a tied variable.) It then verifies that the object referenced by paths is an array, using <tt>&quot;SvRV&quot;</tt> to dereference paths, and <tt>&quot;SvTYPE&quot;</tt> to discover its type. As an added test, it checks that the array referenced by paths is non-empty, using the <tt>&quot;av_top_index&quot;</tt> function (which returns -1 if the array is empty). The <font SIZE="-1">XSRETURN_UNDEF</font> macro is used to abort the <font SIZE="-1">XSUB</font> and return the undefined value whenever all three of these conditions are not met.</p>
<dt>&bull;</p>
<dd> We manipulate several arrays in this <font SIZE="-1">XSUB.</font> Note that an array is represented internally by an AV* pointer. The functions and macros for manipulating arrays are similar to the functions in Perl: <tt>&quot;av_top_index&quot;</tt> returns the highest index in an AV*, much like $#array; <tt>&quot;av_fetch&quot;</tt> fetches a single scalar value from an array, given its index; <tt>&quot;av_push&quot;</tt> pushes a scalar value onto the end of the array, automatically extending the array as necessary. </p>
<p> Specifically, we read pathnames one at a time from the input array, and store the results in an output array (results) in the same order. If statfs fails, the element pushed onto the return array is the value of errno after the failure. If statfs succeeds, though, the value pushed onto the return array is a reference to a hash containing some of the information in the statfs structure. </p>
<p> As with the return stack, it would be possible (and a small performance win) to pre-extend the return array before pushing data into it, since we know how many elements we will return: </p>
<pre>
        av_extend(results, numpaths);
</pre>
<dt>&bull;</p>
<dd> We are performing only one hash operation in this function, which is storing a new scalar under a key using <tt>&quot;hv_store&quot;</tt>. A hash is represented by an HV* pointer. Like arrays, the functions for manipulating hashes from an <font SIZE="-1">XSUB</font> mirror the functionality available from Perl. See perlguts and perlapi for details.</p>
<dt>&bull;</p>
<dd> To create a reference, we use the <tt>&quot;newRV_inc&quot;</tt> function. Note that you can cast an AV* or an HV* to type SV* in this case (and many others). This allows you to take references to arrays, hashes and scalars with the same function. Conversely, the <tt>&quot;SvRV&quot;</tt> function always returns an SV*, which may need to be cast to the appropriate type if it is something other than a scalar (check with <tt>&quot;SvTYPE&quot;</tt>).</p>
<dt>&bull;</p>
<dd> At this point, xsubpp is doing very little work &#8211; the differences between Mytest.xs and Mytest.c are minimal.</dl>
<h3><font SIZE="-1">EXAMPLE 7</font> (Coming Soon)</h3>
<p> <font SIZE="-1">XPUSH</font> args <font SIZE="-1">AND</font> set <font SIZE="-1">RETVAL AND</font> assign return value to array</p>
<h3><font SIZE="-1">EXAMPLE 8</font> (Coming Soon)</h3>
<p> Setting $!</p>
<h3><font SIZE="-1">EXAMPLE 9</font> Passing open files to XSes</h3>
<p> You would think passing files to an <font SIZE="-1">XS</font> is difficult, with all the typeglobs and stuff. Well, it isn&#8217;t. </p>
<p> Suppose that for some strange reason we need a wrapper around the standard C library function <tt>&quot;fputs()&quot;</tt>. This is all we need: </p>
<p>#define PERLIO_NOT_STDIO 0<br />
#define PERL_NO_GET_CONTEXT<br />
#include &#8220;EXTERN.h&#8221;<br />
#include &#8220;XSUB.h&#8221;<br />
#include &#8220;perl.h&#8221;<br />
#include &lt;stdio.h&gt;<br />
int fputs(s, stream)<br />
char *s<br />
    FILE *stream</p>
<p> The real work is done in the standard typemap. </p>
<p> <code>But</code> you lose all the fine stuff done by the perlio layers. This calls the stdio function <tt>&quot;fputs()&quot;</tt>, which knows nothing about them. </p>
<p> The standard typemap offers three variants of PerlIO *: <tt>&quot;InputStream&quot;</tt> (T_IN), <tt>&quot;InOutStream&quot;</tt> (T_INOUT) and <tt>&quot;OutputStream&quot;</tt> (T_OUT). A bare <tt>&quot;PerlIO *&quot;</tt> is considered a T_INOUT. If it matters in your code (see below for why it might) #define or typedef one of the specific names and use that as the argument or result type in your <font SIZE="-1">XS</font> file. </p>
<p> The standard typemap does not contain PerlIO * before perl 5.7, but it has the three stream variants. Using a PerlIO * directly is not backwards compatible unless you provide your own typemap. </p>
<p> For streams coming <i>from</i> perl the main difference is that <tt>&quot;OutputStream&quot;</tt> will get the output PerlIO * &#8211; which may make a difference on a socket. Like in our example&#8230; </p>
<p> For streams being handed <i>to</i> perl a new file handle is created (i.e. a reference to a new glob) and associated with the PerlIO * provided. If the read/write state of the PerlIO * is not correct then you may get errors or warnings from when the file handle is used. So if you opened the PerlIO * as &#8220;w&#8221; it should really be an <tt>&quot;OutputStream&quot;</tt> if open as &#8220;r&#8221; it should be an <tt>&quot;InputStream&quot;</tt>. </p>
<p> Now, suppose you want to use perlio layers in your <font SIZE="-1">XS.</font> We&#8217;ll use the perlio <tt>&quot;PerlIO_puts()&quot;</tt> function as an example. </p>
<p> In the C part of the <font SIZE="-1">XS</font> file (above the first <font SIZE="-1">MODULE</font> line) you have </p>
<p>#define OutputStream PerlIO *<br />
or<br />
    typedef PerlIO *OutputStream;</p>
<p> And this is the <font SIZE="-1">XS</font> code: </p>
<p>int perlioputs(s, stream)<br />
char *s<br />
    OutputStream stream<br />
        CODE : RETVAL = PerlIO_puts(stream, s);<br />
OUTPUT : RETVAL</p>
<p> We have to use a <tt>&quot;CODE&quot;</tt> section because <tt>&quot;PerlIO_puts()&quot;</tt> has the arguments reversed compared to <tt>&quot;fputs()&quot;</tt>, and we want to keep the arguments the same. </p>
<p> Wanting to explore this thoroughly, we want to use the stdio <tt>&quot;fputs()&quot;</tt> on a PerlIO *. This means we have to ask the perlio system for a stdio <tt>&quot;FILE *&quot;</tt>: </p>
<pre><code>
int perliofputs(s, stream)
char *s
    OutputStream stream
        PREINIT : FILE *fp = PerlIO_findFILE(stream);
CODE : if (fp != (FILE *)0)
{
    RETVAL = fputs(s, fp);
}
else
{
    RETVAL = -1;
}
OUTPUT : RETVAL
</code></pre>
<p> Note: <tt>&quot;PerlIO_findFILE()&quot;</tt> will search the layers for a stdio layer. If it can&#8217;t find one, it will call <tt>&quot;PerlIO_exportFILE()&quot;</tt> to generate a new stdio <tt>&quot;FILE&quot;</tt>. Please only call <tt>&quot;PerlIO_exportFILE()&quot;</tt> if you want a <i>new</i> <tt>&quot;FILE&quot;</tt>. It will generate one on each call and push a new stdio layer. So don&#8217;t call it repeatedly on the same file. <tt>&quot;PerlIO_findFILE()&quot;</tt> will retrieve the stdio layer once it has been generated by <tt>&quot;PerlIO_exportFILE()&quot;</tt>. </p>
<p> This applies to the perlio system only. For versions before 5.7, <tt>&quot;PerlIO_exportFILE()&quot;</tt> is equivalent to <tt>&quot;PerlIO_findFILE()&quot;</tt>.</p>
<h3>Troubleshooting these Examples</h3>
<p> As mentioned at the top of this document, if you are having problems with these example extensions, you might see if any of these help you.</p>
<dl>
<dt>&bull;</p>
<dd> In versions of 5.002 prior to the gamma version, the test script in Example 1 will not function properly. You need to change the &#8220;use lib&#8221; line to read: </p>
<pre>
        use lib './blib';
</pre>
<dt>&bull;</p>
<dd> In versions of 5.002 prior to version 5.002b1h, the test.pl file was not automatically created by h2xs. This means that you cannot say &#8220;make test&#8221; to run the test script. You will need to add the following line before the &#8220;use extension&#8221; statement: </p>
<pre>
        use lib './blib';
</pre>
<dt>&bull;</p>
<dd> In versions 5.000 and 5.001, instead of using the above line, you will need to use the following line: </p>
<pre>
        BEGIN { unshift(@INC, &quot;./blib&quot;) }
</pre>
<dt>&bull;</p>
<dd> This document assumes that the executable named &#8220;perl&#8221; is Perl version 5. Some systems may have installed Perl version 5 as &#8220;perl5&#8221;.</dl>
<h2>See also</h2>
<p> For more information, consult perlguts, perlapi, perlxs, perlmod, and perlpod.</p>
<h2>Author</h2>
<p> Jeff Okamoto &lt;<i>okamoto [at] corp.hp.com</i>&gt; </p>
<p> Reviewed and assisted by Dean Roehrich, Ilya Zakharevich, Andreas Koenig, and Tim Bunce. </p>
<p> PerlIO material contributed by Lupe Christoph, with some clarification by Nick Ing-Simmons. </p>
<p> Changes for h2xs as of Perl 5.8.x by Renee Baecker</p>
<h3>Last Changed</h3>
<p> 2012-01-20 </p>
<h2>Index</h2>
<dt><a href="#lbAI">TUTORIAL</a></p>
<dd>
<dt><a href="#lbBK">See also</a></p>
<dd>
<dt><a href="#lbBL">Author</a></p>
<dd>
</dl>
