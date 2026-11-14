---
title: "perlhaiku(1)"
name: "perlhaiku"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlhaiku/"
---

<h2 class="name">NAME</h2>
 

 perlhaiku - Perl version 5.10+ on Haiku 

<h2>DESCRIPTION</h2>

 This file contains instructions how to build Perl for Haiku and lists known problems.

<h2>BUILD AND INSTALL</h2>

 The build procedure is completely standard: 

 <pre>
  ./Configure -de
  make
  make install
</pre> 

 Make perl executable and create a symlink for libperl: 

 <pre>
  chmod a+x /boot/common/bin/perl
  cd /boot/common/lib; ln -s perl5/5.30.0/BePC-haiku/CORE/libperl.so .
</pre> 

 Replace <tt>5.30.0</tt> with your respective version of Perl.

<h2>KNOWN PROBLEMS</h2>

 The following problems are encountered with Haiku revision 28311:
<dl>
<dt>&bull;
<dd> Perl cannot be compiled with threading support <font SIZE="-1">ATM.</font>
<dt>&bull;
<dd> The <i>cpan/Socket/t/socketpair.t</i> test fails. More precisely: the subtests using datagram sockets fail. Unix datagram sockets aren't implemented in Haiku yet.
<dt>&bull;
<dd> A subtest of the <i>cpan/Sys-Syslog/t/syslog.t</i> test fails. This is due to Haiku not implementing <i>/dev/log</i> support yet.
<dt>&bull;
<dd> The tests <i>dist/Net-Ping/t/450_service.t</i> and <i>dist/Net-Ping/t/510_ping_udp.t</i> fail. This is due to bugs in Haiku's network stack implementation.</dl>

<h2>CONTACT</h2>

 For Haiku specific problems contact the HaikuPorts developers: &lt;<a rel="nofollow" HREF="http://ports.haiku-files.org/">http://ports.haiku-files.org/</a>&gt; 

 The initial Haiku port was done by Ingo Weinhold &lt;ingo_weinhold [at] gmx.de&gt;. 

 Last update: 2008-10-29 

<h2>Index</h2>


