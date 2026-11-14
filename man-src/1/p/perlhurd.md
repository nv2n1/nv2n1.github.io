---
title: "perlhurd(1)"
name: "perlhurd"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlhurd/"
---

<h2 class="name">NAME</h2>
 

 perlhurd - Perl version 5 on Hurd 

<h2>DESCRIPTION</h2>

 If you want to use Perl on the Hurd, I recommend using the Debian GNU/Hurd distribution ( see &lt;<a rel="nofollow" HREF="http://www.debian.org/">http://www.debian.org/</a>&gt; ), even if an official, stable release has not yet been made. The old ``gnu-0.2'' binary distribution will most certainly have additional problems.

<h3>Known Problems with Perl on Hurd</h3>

 The Perl test suite may still report some errors on the Hurd. The ``lib/anydbm'' and ``pragma/warnings'' tests will almost certainly fail. Both failures are not really specific to the Hurd, as indicated by the test suite output. 

 The socket tests may fail if the network is not configured. You have to make ``/hurd/pfinet'' the translator for ``/servers/socket/2'', giving it the right arguments. Try ``/hurd/pfinet --help'' for more information. 

 Here are the statistics for Perl 5.005_62 on my system: 

 <pre><code>
Failed Test Status Wstat Total Fail Failed List of failed-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -lib / anydbm.t 12 1 8.33 % 12 pragma / warnings 333 1 0.30 % 215 8 tests and 24 subtests skipped.Failed 2 / 229 test scripts, 99.13 % okay.2 / 10850 subtests failed,
    99.98 % okay.
</code></pre> 

 There are quite a few systems out there that do worse! 

 However, since I am running a very recent Hurd snapshot, in which a lot of bugs that were exposed by the Perl test suite have been fixed, you may encounter more failures. Likely candidates are: ``op/stat'', ``lib/io_pipe'', ``lib/io_sock'', ``lib/io_udp'' and ``lib/time''. 

 In any way, if you're seeing failures beyond those mentioned in this document, please consider upgrading to the latest Hurd before reporting the failure as a bug.

<h2>AUTHOR</h2>

 Mark Kettenis &lt;kettenis [at] gnu.org&gt; 

 Last Updated: Fri, 29 Oct 1999 22:50:30 +0200 

<h2>Index</h2>


