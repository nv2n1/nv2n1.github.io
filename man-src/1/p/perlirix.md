---
title: "perlirix(1)"
name: "perlirix"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlirix/"
---

<h2 class="name">NAME</h2>
 

 perlirix - Perl version 5 on Irix systems 

<h2>DESCRIPTION</h2>

 This document describes various features of Irix that will affect how Perl version 5 (hereafter just Perl) is compiled and/or runs.

<h3>Building 32-bit Perl in Irix</h3>

 Use 

 <pre>
        sh Configure -Dcc='cc -n32'
</pre> 

 to compile Perl 32-bit. Don't bother with -n32 unless you have 7.1 or later compilers (use cc -version to check). 

 (Building 'cc -n32' is the default.)

<h3>Building 64-bit Perl in Irix</h3>

 Use 

 <pre>
        sh Configure -Dcc='cc -64' -Duse64bitint
</pre> 

 This requires require a 64-bit <font SIZE="-1">MIPS CPU</font> (R8000, R10000, ...) 

 You can also use 

 <pre>
        sh Configure -Dcc='cc -64' -Duse64bitall
</pre> 

 but that makes no difference compared with the -Duse64bitint because of the <tt>&quot;cc -64&quot;</tt>. 

 You can also do 

 <pre>
        sh Configure -Dcc='cc -n32' -Duse64bitint
</pre> 

 to use long longs for the 64-bit integer type, in case you don't have a 64-bit <font SIZE="-1">CPU.</font> 

 If you are using gcc, just 

 <pre>
        sh Configure -Dcc=gcc -Duse64bitint
</pre> 

 should be enough, the Configure should automatically probe for the correct 64-bit settings.

<h3>About Compiler Versions of Irix</h3>

 Some Irix cc versions, e.g. 7.3.1.1m (try cc -version) have been known to have issues (coredumps) when compiling perl.c. If you've used -OPT:fast_io=ON and this happens, try removing it. If that fails, or you didn't use that, then try adjusting other optimization options (-LNO, -INLINE, -O3 to -O2, etcetera). The compiler bug has been reported to <font SIZE="-1">SGI.</font> (Allen Smith &lt;easmith [at] beatrice.rutgers.edu&gt;)

<h3>Linker Problems in Irix</h3>

 If you get complaints about so_locations then search in the file hints/irix_6.sh for ``lddflags'' and do the suggested adjustments. (David Billinghurst &lt;David.Billinghurst [at] riotinto.com.au&gt;)

<h3>Malloc in Irix</h3>

 Do not try to use Perl's malloc, this will lead into very mysterious errors (especially with -Duse64bitall).

<h3>Building with threads in Irix</h3>

 Run Configure with -Duseithreads which will configure Perl with the Perl 5.8.0 ``interpreter threads'', see threads. 

 For Irix 6.2 with perl threads, you have to have the following patches installed: 

 <pre>
        1404 Irix 6.2 Posix 1003.1b man pages
        1645 Irix 6.2 &amp; 6.3 POSIX header file updates
        2000 Irix 6.2 Posix 1003.1b support modules
        2254 Pthread library fixes
        2401 6.2 all platform kernel rollup
</pre> 

 <font SIZE="-1"><b>IMPORTANT</b></font>: Without patch 2401, a kernel bug in Irix 6.2 will cause your machine to panic and crash when running threaded perl. Irix 6.3 and later are okay. 

 <pre>
    Thanks to Hannu Napari &lt;Hannu.Napari [at] hut.fi&gt; for the IRIX
    pthreads patches information.
</pre>

<h3>Irix 5.3</h3>

 While running Configure and when building, you are likely to get quite a few of these warnings: 

 <pre>
  ld:
  The shared object /usr/lib/libm.so did not resolve any symbols.
        You may want to remove it from your link line.
</pre> 

 Ignore them: in <font SIZE="-1">IRIX 5.3</font> there is no way to quieten ld about this. 

 During compilation you will see this warning from toke.c: 

 <pre>
  uopt: Warning: Perl_yylex: this procedure not optimized because it
        exceeds size threshold; to optimize this procedure, use -Olimit
        option with value &gt;= 4252.
</pre> 

 Ignore the warning. 

 In <font SIZE="-1">IRIX 5.3</font> and with Perl 5.8.1 (Perl 5.8.0 didn't compile in <font SIZE="-1">IRIX 5.3</font>) the following failures are known. 

 <pre><code>
Failed Test Stat Wstat Total Fail Failed List of Failed-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -../ ext / List / Util / t / shuffle.t 0 139 ? ? ? ? % ? ?../ lib / Math / Trig.t 255 65280 29 12 41.38 % 24 - 29../ lib / sort.t 0 138 119 72 60.50 % 48 - 119 56 tests and 474 subtests skipped.Failed 3 / 811 test scripts, 99.63 % okay.78 / 75813 subtests failed,
    99.90 % okay.
</code></pre> 

 They are suspected to be compiler errors (at least the shuffle.t failure is known from some <font SIZE="-1">IRIX 6</font> setups) and math library errors (the Trig.t failure), but since <font SIZE="-1">IRIX 5</font> is long since end-of-lifed, further fixes for the <font SIZE="-1">IRIX</font> are unlikely. If you can get gcc for 5.3, you could try that, too, since gcc in <font SIZE="-1">IRIX 6</font> is a known workaround for at least the shuffle.t and sort.t failures.

<h2>AUTHOR</h2>

 Jarkko Hietaniemi &lt;jhi [at] iki.fi&gt; 

 Please report any errors, updates, or suggestions to <i>perlbug [at] perl.org</i>. 

<h2>Index</h2>


