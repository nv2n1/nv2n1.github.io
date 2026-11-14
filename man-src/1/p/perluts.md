---
title: "perluts(1)"
name: "perluts"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perluts/"
---

<h2 class="name">NAME</h2>
 

 perluts - Perl under UTS 

<h2>SYNOPSIS</h2>

 This document can be read <i>as is</i>: as <i></i><font SIZE="-1"><i>README</i></font><i>.uts</i>, or you can read it after you build your package using ``man perluts''. 

 The purpose is to help you build Perl for <font SIZE="-1">UTS</font>, which, if you follow these instructions, should be easy, and result in a solidly working installation.

<h2>DESCRIPTION</h2>

 Perl 5.7.2 (Developmental) or Perl 5.8.x (forthcoming) for <font SIZE="-1">UTS</font>

<h2>BUILDING PERL ON UTS</h2>

 <font SIZE="-1">NOTE:</font> Some sites have redefined the way uname works, and if yours does this, special steps must be taken so that Configure can recognize your system as a <font SIZE="-1">UTS</font> system. To see if you are in this category, issue the command ``uname -a''. It should look something like: 

 <pre>
  uts juno 4 4.4 9672 370
</pre> 

 At any rate, the first field should be ``uts''. If this is not the case; supposing it is, say telcoUTS, create a script, uts/uname (i.e. uname, in the subdirectory ``uts'' of the main Perl source dir): 
#&nbsp;<wbr>uname 
/usr/bin/uname&nbsp;<wbr>``$@''&nbsp;<wbr>| sed -e&nbsp;<wbr>'s/^telcoUTS/uts/' 

 and when you execute Configure, do it as below, except for adding PATH=uts:$PATH as a prefix. I.e. do: 

 <pre>
   PATH=uts:$PATH ./Configure ...
</pre> 

 There is no need to do an interactive configure, just type 

 <pre><code>
./ Configure - de[-Dusedevel][-Doptimize = -g] 2 &gt; &amp;1 | tee Conf.out
</code></pre> 

 ``-Dusedevel'' may be required to configure Perl 5.7.2 non-interactively. Use -Doptimize=-g if you want to run Perl under sdb or gdb, <font SIZE="-1">OR</font> if you want to be able to use the -D command line flags to perl, which are occasionally useful in debugging perl scripts. 

 In this and the following steps, the ``2&gt;&amp;1 | tee <font SIZE="-1">XXX</font>.out'' records all output from the process, which will be useful if anything unexpected goes wrong. 

 Then do the compilation with 

 <pre>
  make 2&gt;&amp;1 | tee make.out
</pre> 

 Finally, test using 

 <pre>
  make test 2&gt;&amp;1 | tee make-test.out
</pre> 

 In the output, the only failures you should see should look like: 

 <pre>
   lib/Math/BigInt/t/bigfltpm.........Use of uninitialized value ...
   FAILED at test 57
   lib/Math/BigInt/t/bigintc..........ok
   lib/Math/BigInt/t/bigintpm.........FAILED at test 204
   lib/Math/BigInt/t/mbimbf...........Use of uninitialized value ...
   Illegal division by zero at ../lib/Math/BigInt/Calc.pm line 314.
   FAILED at test 71
   lib/Math/Complex...................exp: OVERFLOW
   FAILED at test 250
   lib/Math/Trig......................exp: OVERFLOW
   ok
   lib/Memoize/t/array................ok
        ...
   lib/Net/protoent...................ok
   lib/Net/servent....................FAILED at test 0
</pre> 

 This means that everything passes except for some problems in the packages ``Math::BigInt'', ``Math::Complex'', and ``Math::Trig''. The lib/Net/servent failure seems to be a bug in the test program. To confirm this, from the main Perl source dir, do: 

 <pre>
   LD_LIBRARY_PATH=`pwd` ./perl -Ilib lib/Net/servent.t
</pre> 

 and it should output 

 <pre>
   1..3
   ok 1
   ok 2
   ok 3
</pre>

<h2>Installing the built perl on UTS</h2>

 Run the command ``make install''

<h2>AUTHOR</h2>

 <pre>
   Hal Morris
   UTS Global LLC
   email: hom00 [at] utsglobal.com
</pre> 

<h2>Index</h2>


