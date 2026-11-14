---
title: "perltru64(1)"
name: "perltru64"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perltru64/"
description: "perltru64 – Perl version 5 on Tru64 (formerly known as Digital UNIX formerly known as DEC OSF/1) systems"
---

<h2 class="name">NAME</h2>
<p> perltru64 &#8211; Perl version 5 on Tru64 (formerly known as Digital UNIX formerly known as DEC OSF/1) systems </p>
<h2>DESCRIPTION</h2>
<p> This document describes various features of <font SIZE="-1">HP</font>&#8216;s (formerly Compaq&#8217;s, formerly Digital&#8217;s) Unix operating system (Tru64) that will affect how Perl version 5 (hereafter just Perl) is configured, compiled and/or runs.</p>
<h3>Compiling Perl 5 on Tru64</h3>
<p> The recommended compiler to use in Tru64 is the native C compiler. The native compiler produces much faster code (the speed difference is noticeable: several dozen percentages) and also more correct code: if you are considering using the <font SIZE="-1">GNU C</font> compiler you should use at the very least the release of 2.95.3 since all older gcc releases are known to produce broken code when compiling Perl. One manifestation of this brokenness is the lib/sdbm test dumping core; another is many of the op/regexp and op/pat, or ext/Storable tests dumping core (the exact pattern of failures depending on the <font SIZE="-1">GCC</font> release and optimization flags). </p>
<p> Both the native cc and gcc seem to consume lots of memory when building Perl. toke.c is a known trouble spot when optimizing: 256 megabytes of data section seems to be enough. Another known trouble spot is the mktables script which builds the Unicode support tables. The default setting of the process data section in Tru64 should be one gigabyte, but some sites/setups might have lowered that. The configuration process of Perl checks for too low process limits, and lowers the optimization for the toke.c if necessary, and also gives advice on how to raise the process limits (for example: <tt>&quot;ulimit -d 262144&quot;</tt>) </p>
<p> Also, Configure might abort with </p>
<pre><code>
Build a threading Perl ? [n] Configure[2437] : Syntax error at line 1 : 'config.sh' is not expected.
</code></pre>
<p> This indicates that Configure is being run with a broken Korn shell (even though you think you are using a Bourne shell by using &#8220;sh Configure&#8221; or &#8220;./Configure&#8221;). The Korn shell bug has been reported to Compaq as of February 1999 but in the meanwhile, the reason ksh is being used is that you have the environment variable <font SIZE="-1">BIN_SH</font> set to &#8216;xpg4&#8217;. This causes /bin/sh to delegate its duties to /bin/posix/sh (a ksh). Unset the environment variable and rerun Configure.</p>
<h3>Using Large Files with Perl on Tru64</h3>
<p> In Tru64 Perl is automatically able to use large files, that is, files larger than 2 gigabytes, there is no need to use the Configure -Duselargefiles option as described in <font SIZE="-1">INSTALL</font> (though using the option is harmless).</p>
<h3>Threaded Perl on Tru64</h3>
<p> If you want to use threads, you should primarily use the Perl 5.8.0 threads model by running Configure with -Duseithreads. </p>
<p> Perl threading is going to work only in Tru64 4.0 and newer releases, older operating releases like 3.2 aren&#8217;t probably going to work properly with threads. </p>
<p> In Tru64 V5 (at least V5.1A, V5.1B) you cannot build threaded Perl with gcc because the system header &lt;pthread.h&gt; explicitly checks for supported C compilers, gcc (at least 3.2.2) not being one of them. But the system C compiler should work just fine.</p>
<h3>Long Doubles on Tru64</h3>
<p> You cannot Configure Perl to use long doubles unless you have at least Tru64 V5.0, the long double support simply wasn&#8217;t functional enough before that. Perl&#8217;s Configure will override attempts to use the long doubles (you can notice this by Configure finding out that the <code>modfl()</code> function does not work as it should). </p>
<p> At the time of this writing (June 2002), there is a known bug in the Tru64 libc printing of long doubles when not using &#8220;e&#8221; notation. The values are correct and usable, but you only get a limited number of digits displayed unless you force the issue by using <tt>&quot;printf &quot;%.33e&quot;,$num&quot;</tt> or the like. For Tru64 versions V5.0A through V5.1A, a patch is expected sometime after perl 5.8.0 is released. If your libc has not yet been patched, you&#8217;ll get a warning from Configure when selecting long doubles.</p>
<h3>DB_File tests failing on Tru64</h3>
<p> The DB_File tests (db-btree.t, db-hash.t, db-recno.t) may fail you have installed a newer version of Berkeley <font SIZE="-1">DB</font> into the system and the -I and -L compiler and linker flags introduce version conflicts with the <font SIZE="-1">DB 1.85</font> headers and libraries that came with the Tru64. For example, mixing a <font SIZE="-1">DB</font> v2 library with the <font SIZE="-1">DB</font> v1 headers is a bad idea. Watch out for Configure options -Dlocincpth and -Dloclibpth, and check your /usr/local/include and /usr/local/lib since they are included by default. </p>
<p> The second option is to explicitly instruct Configure to detect the newer Berkeley <font SIZE="-1">DB</font> installation, by supplying the right directories with <tt>&quot;-Dlocincpth=/some/include&quot;</tt> and <tt>&quot;-Dloclibpth=/some/lib&quot;</tt> <code>and</code> before running &#8220;make test&#8221; setting your <font SIZE="-1">LD_LIBRARY_PATH</font> to <i>/some/lib</i>. </p>
<p> The third option is to work around the problem by disabling the DB_File completely when build Perl by specifying -Ui_db to Configure, and then using the BerkeleyDB module from <font SIZE="-1">CPAN</font> instead of DB_File. The BerkeleyDB works with Berkeley <font SIZE="-1">DB</font> versions 2.* or greater. </p>
<p> The Berkeley <font SIZE="-1">DB 4.1.25</font> has been tested with Tru64 V5.1A and found to work. The latest Berkeley <font SIZE="-1">DB</font> can be found from &lt;<a rel="nofollow" href="http://www.sleepycat.com">http://www.sleepycat.com</a>&gt;.</p>
<h3>64-bit Perl on Tru64</h3>
<p> In Tru64 Perl&#8217;s integers are automatically 64-bit wide, there is no need to use the Configure -Duse64bitint option as described in <font SIZE="-1">INSTALL.</font> Similarly, there is no need for -Duse64bitall since pointers are automatically 64-bit wide.</p>
<h3>Warnings about floating-point overflow when compiling Perl on Tru64</h3>
<p> When compiling Perl in Tru64 you may (depending on the compiler release) see two warnings like this </p>
<p>cc : Warning : numeric.c, line 104 : In this statement, floating &#8211; point overflow occurs in evaluating the expression &#8220;1.8e308&#8221;.(floatoverfl) return HUGE_VAL;<br />
&#8212; &#8212; &#8212; &#8212; &#8212; -^</p>
<p> and when compiling the <font SIZE="-1">POSIX</font> extension </p>
<pre><code>
cc : Warning : const - c.inc, line 2007 : In this statement, floating - point overflow occurs in evaluating the expression "1.8e308".(floatoverfl) return HUGE_VAL;
-- -- -- -- -- -- -- -- -- -^
</code></pre>
<p> The exact line numbers may vary between Perl releases. The warnings are benign and can be ignored: in later C compiler releases the warnings should be gone. </p>
<p> When the file <i>pp_sys.c</i> is being compiled you may (depending on the operating system release) see an additional compiler flag being used: <tt>&quot;-DNO_EFF_ONLY_OK&quot;</tt>. This is normal and refers to a feature that is relevant only if you use the <tt>&quot;filetest&quot;</tt> pragma. In older releases of the operating system the feature was broken and the <font SIZE="-1">NO_EFF_ONLY_OK</font> instructs Perl not to use the feature.</p>
<h2>Testing Perl on Tru64</h2>
<p> During &#8220;make test&#8221; the <tt>&quot;comp&quot;</tt>/<tt>&quot;cpp&quot;</tt> will be skipped because on Tru64 it cannot be tested before Perl has been installed. The test refers to the use of the <tt>&quot;-P&quot;</tt> option of Perl.</p>
<h2>ext/ODBM_File/odbm Test Failing With Static Builds</h2>
<p> The ext/ODBM_File/odbm is known to fail with static builds (Configure -Uusedl) due to a known bug in Tru64&#8217;s static libdbm library. The good news is that you very probably don&#8217;t need to ever use the ODBM_File extension since more advanced NDBM_File works fine, not to mention the even more advanced DB_File.</p>
<h2>Perl Fails Because Of Unresolved Symbol sockatmark</h2>
<p> If you get an error like </p>
<pre>
    Can't load '.../OSF1/lib/perl5/5.8.0/alpha-dec_osf/auto/IO/IO.so' for module IO: Unresolved symbol in .../lib/perl5/5.8.0/alpha-dec_osf/auto/IO/IO.so: sockatmark at .../lib/perl5/5.8.0/alpha-dec_osf/XSLoader.pm line 75.
</pre>
<p> you need to either recompile your Perl in Tru64 4.0D or upgrade your Tru64 4.0D to at least 4.0F: the <code>sockatmark()</code> system call was added in Tru64 4.0F, and the <font SIZE="-1">IO</font> extension refers that symbol.</p>
<h2>read_cur_obj_info: bad file magic number</h2>
<p> You may be mixing the Tru64 cc/ar/ld with the <font SIZE="-1">GNU</font> gcc/ar/ld. That may work, but sometimes it doesn&#8217;t (your gcc or <font SIZE="-1">GNU</font> utils may have been compiled for an incompatible <font SIZE="-1">OS</font> release). </p>
<p> Try &#8216;which ld&#8217; and &#8216;which ld&#8217; (or try &#8216;ar &#8211;version&#8217; and &#8216;ld &#8211;version&#8217;, which work only for the <font SIZE="-1">GNU</font> tools, and will announce themselves to be such), and adjust your <font SIZE="-1">PATH</font> so that you are consistently using either the native tools or the <font SIZE="-1">GNU</font> tools. After fixing your <font SIZE="-1">PATH,</font> you should do &#8216;make distclean&#8217; and start all the way from running the Configure since you may have quite a confused situation.</p>
<h2>AUTHOR</h2>
<p> Jarkko Hietaniemi &lt;jhi [at] iki.fi&gt; </p>
<h2>Index</h2>
