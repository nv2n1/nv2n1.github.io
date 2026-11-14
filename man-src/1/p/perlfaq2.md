---
title: "perlfaq2(1)"
name: "perlfaq2"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlfaq2/"
---

<h2 class="name">NAME</h2>
 

 perlfaq2 - Obtaining and Learning about Perl 

<h2>VERSION</h2>

 version 5.20190126

<h2>DESCRIPTION</h2>

 This section of the <font SIZE="-1">FAQ</font> answers questions about where to find source and documentation for Perl, support, and related matters.

<h3>What machines support Perl? Where do I get it?</h3>

 The standard release of Perl (the one maintained by the Perl development team) is distributed only in source code form. You can find the latest releases at &lt;<a rel="nofollow" HREF="http://www.cpan.org/src/">http://www.cpan.org/src/</a>&gt;. 

 Perl builds and runs on a bewildering number of platforms. Virtually all known and current Unix derivatives are supported (perl's native platform), as are other systems like <font SIZE="-1">VMS, DOS, OS/2,</font> Windows, <font SIZE="-1">QNX,</font> BeOS, <font SIZE="-1">OS X,</font> MPE/iX and the Amiga. 

 Binary distributions for some proprietary platforms can be found &lt;<a rel="nofollow" HREF="http://www.cpan.org/ports/">http://www.cpan.org/ports/</a>&gt; directory. Because these are not part of the standard distribution, they may and in fact do differ from the base perl port in a variety of ways. You'll have to check their respective release notes to see just what the differences are. These differences can be either positive (e.g. extensions for the features of the particular platform that are not supported in the source release of perl) or negative (e.g. might be based upon a less current source release of perl).

<h3>How can I get a binary version of Perl?</h3>

 See <font SIZE="-1">CPAN</font> Ports &lt;<a rel="nofollow" HREF="http://www.cpan.org/ports/">http://www.cpan.org/ports/</a>&gt;

<h3>I don't have a C compiler. How can I build my own Perl interpreter?</h3>

 For Windows, use a binary version of Perl, Strawberry Perl &lt;<a rel="nofollow" HREF="http://strawberryperl.com/">http://strawberryperl.com/</a>&gt; and ActivePerl &lt;<a rel="nofollow" HREF="http://www.activestate.com/activeperl">http://www.activestate.com/activeperl</a>&gt; come with a bundled C compiler. 

 Otherwise if you really do want to build Perl, you need to get a binary version of <tt>&quot;gcc&quot;</tt> for your system first. Use a search engine to find out how to do this for your operating system.

<h3>I copied the Perl binary from one machine to another, but scripts don't work.</h3>

 That's probably because you forgot libraries, or library paths differ. You really should build the whole distribution on the machine it will eventually live on, and then type <tt>&quot;make install&quot;</tt>. Most other approaches are doomed to failure. 

 One simple way to check that things are in the right place is to print out the hard-coded <tt>@INC</tt> that perl looks through for libraries: 

 <pre>
    % perl -le 'print for @INC'
</pre> 

 If this command lists any paths that don't exist on your system, then you may need to move the appropriate libraries to these locations, or create symbolic links, aliases, or shortcuts appropriately. <tt>@INC</tt> is also printed as part of the output of 

 <pre>
    % perl -V
</pre> 

 You might also want to check out ``How do I keep my own module/library directory?'' in perlfaq8.

<h3>I grabbed the sources and tried to compile but gdbm/dynamic loading/malloc/linking/... failed. How do I make it work?</h3>

 Read the <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file, which is part of the source distribution. It describes in detail how to cope with most idiosyncrasies that the <tt>&quot;Configure&quot;</tt> script can't work around for any given system or architecture.

<h3>What modules and extensions are available for Perl? What is <font SIZE="-1">CPAN</font>?</h3>

 <font SIZE="-1">CPAN</font> stands for Comprehensive Perl Archive Network, a multi-gigabyte archive replicated on hundreds of machines all over the world. <font SIZE="-1">CPAN</font> contains tens of thousands of modules and extensions, source code and documentation, designed for <i>everything</i> from commercial database interfaces to keyboard/screen control and running large web sites. 

 You can search <font SIZE="-1">CPAN</font> on &lt;<a rel="nofollow" HREF="http://metacpan.org">http://metacpan.org</a>&gt;. 

 The master web site for <font SIZE="-1">CPAN</font> is &lt;<a rel="nofollow" HREF="http://www.cpan.org/">http://www.cpan.org/</a>&gt;, &lt;<a rel="nofollow" HREF="http://www.cpan.org/SITES.html">http://www.cpan.org/SITES.html</a>&gt; lists all mirrors. 

 See the <font SIZE="-1">CPAN FAQ</font> at &lt;<a rel="nofollow" HREF="http://www.cpan.org/misc/cpan-faq.html">http://www.cpan.org/misc/cpan-faq.html</a>&gt; for answers to the most frequently asked questions about <font SIZE="-1">CPAN.</font> 

 The Task::Kensho module has a list of recommended modules which you should review as a good starting point.

<h3>Where can I get information on Perl?</h3>

<dl>
<dt>&bull;
<dd> &lt;<a rel="nofollow" HREF="http://www.perl.org/">http://www.perl.org/</a>&gt;
<dt>&bull;
<dd> &lt;<a rel="nofollow" HREF="http://perldoc.perl.org/">http://perldoc.perl.org/</a>&gt;
<dt>&bull;
<dd> &lt;<a rel="nofollow" HREF="http://learn.perl.org/">http://learn.perl.org/</a>&gt;</dl>
 

 The complete Perl documentation is available with the Perl distribution. If you have Perl installed locally, you probably have the documentation installed as well: type <tt>&quot;perldoc perl&quot;</tt> in a terminal or view online &lt;<a rel="nofollow" HREF="http://perldoc.perl.org/perl.html">http://perldoc.perl.org/perl.html</a>&gt;. 

 (Some operating system distributions may ship the documentation in a different package; for instance, on Debian, you need to install the <tt>&quot;perl-doc&quot;</tt> package.) 

 Many good books have been written about Perl---see the section later in perlfaq2 for more details.

<h3>What is perl.com? Perl Mongers? pm.org? perl.org? cpan.org?</h3>

 Perl.com &lt;<a rel="nofollow" HREF="http://www.perl.com/">http://www.perl.com/</a>&gt; used to be part of the O'Reilly Network, a subsidiary of O'Reilly Media. Although it retains most of the original content from its O'Reilly Network, it is now hosted by The Perl Foundation &lt;<a rel="nofollow" HREF="http://www.perlfoundation.org/">http://www.perlfoundation.org/</a>&gt;. 

 The Perl Foundation is an advocacy organization for the Perl language which maintains the web site &lt;<a rel="nofollow" HREF="http://www.perl.org/">http://www.perl.org/</a>&gt; as a general advocacy site for the Perl language. It uses the domain to provide general support services to the Perl community, including the hosting of mailing lists, web sites, and other services. There are also many other sub-domains for special topics like learning Perl and jobs in Perl, such as:
<dl>
<dt>&bull;
<dd> &lt;<a rel="nofollow" HREF="http://www.perl.org/">http://www.perl.org/</a>&gt;
<dt>&bull;
<dd> &lt;<a rel="nofollow" HREF="http://learn.perl.org/">http://learn.perl.org/</a>&gt;
<dt>&bull;
<dd> &lt;<a rel="nofollow" HREF="http://jobs.perl.org/">http://jobs.perl.org/</a>&gt;
<dt>&bull;
<dd> &lt;<a rel="nofollow" HREF="http://lists.perl.org/">http://lists.perl.org/</a>&gt;</dl>
 

 Perl Mongers &lt;<a rel="nofollow" HREF="http://www.pm.org/">http://www.pm.org/</a>&gt; uses the pm.org domain for services related to local Perl user groups, including the hosting of mailing lists and web sites. See the Perl Mongers web site &lt;<a rel="nofollow" HREF="http://www.pm.org/">http://www.pm.org/</a>&gt; for more information about joining, starting, or requesting services for a Perl user group. 

 <font SIZE="-1">CPAN,</font> or the Comprehensive Perl Archive Network &lt;<a rel="nofollow" HREF="http://www.cpan.org/">http://www.cpan.org/</a>&gt;, is a replicated, worldwide repository of Perl software. See What is <font SIZE="-1">CPAN</font>?.

<h3>Where can I post questions?</h3>

 There are many Perl mailing lists for various topics, specifically the beginners list &lt;<a rel="nofollow" HREF="http://lists.perl.org/list/beginners.html">http://lists.perl.org/list/beginners.html</a>&gt; may be of use. 

 Other places to ask questions are on the PerlMonks site &lt;<a rel="nofollow" HREF="http://www.perlmonks.org/">http://www.perlmonks.org/</a>&gt; or stackoverflow &lt;<a rel="nofollow" HREF="http://stackoverflow.com/questions/tagged/perl">http://stackoverflow.com/questions/tagged/perl</a>&gt;.

<h3>Perl Books</h3>

 There are many good books on Perl &lt;<a rel="nofollow" HREF="http://www.perl.org/books/library.html">http://www.perl.org/books/library.html</a>&gt;.

<h3>Which magazines have Perl content?</h3>

 There's also <i></i>$foo<i> Magazin</i>, a German magazine dedicated to Perl, at ( &lt;<a rel="nofollow" HREF="http://www.foo-magazin.de">http://www.foo-magazin.de</a>&gt; ). The <i>Perl-Zeitung</i> is another German-speaking magazine for Perl beginners (see &lt;<a rel="nofollow" HREF="http://perl-zeitung.at.tf">http://perl-zeitung.at.tf</a>&gt; ). 

 Several Unix/Linux related magazines frequently include articles on Perl.

<h3>Which Perl blogs should I read?</h3>

 Perl News &lt;<a rel="nofollow" HREF="http://perlnews.org/">http://perlnews.org/</a>&gt; covers some of the major events in the Perl world, Perl Weekly &lt;<a rel="nofollow" HREF="http://perlweekly.com/">http://perlweekly.com/</a>&gt; is a weekly e-mail (and <font SIZE="-1">RSS</font> feed) of hand-picked Perl articles. 

 &lt;<a rel="nofollow" HREF="http://blogs.perl.org/">http://blogs.perl.org/</a>&gt; hosts many Perl blogs, there are also several blog aggregators: Perlsphere &lt;<a rel="nofollow" HREF="http://perlsphere.net/">http://perlsphere.net/</a>&gt; and IronMan &lt;<a rel="nofollow" HREF="http://ironman.enlightenedperl.org/">http://ironman.enlightenedperl.org/</a>&gt; are two of them.

<h3>What mailing lists are there for Perl?</h3>

 A comprehensive list of Perl-related mailing lists can be found at &lt;<a rel="nofollow" HREF="http://lists.perl.org/">http://lists.perl.org/</a>&gt;

<h3>Where can I buy a commercial version of Perl?</h3>

 Perl already <i>is</i> commercial software: it has a license that you can grab and carefully read to your manager. It is distributed in releases and comes in well-defined packages. There is a very large and supportive user community and an extensive literature. 

 If you still need commercial support ActiveState &lt;<a rel="nofollow" HREF="http://www.activestate.com/activeperl">http://www.activestate.com/activeperl</a>&gt; offers this.

<h3>Where do I send bug reports?</h3>

 (contributed by brian d foy) 

 First, ensure that you've found an actual bug. Second, ensure you've found an actual bug. 

 If you've found a bug with the perl interpreter or one of the modules in the standard library (those that come with Perl), you can use the perlbug utility that comes with Perl (&gt;= 5.004). It collects information about your installation to include with your message, then sends the message to the right place. 

 To determine if a module came with your version of Perl, you can install and use the Module::CoreList module. It has the information about the modules (with their versions) included with each release of Perl. 

 Every <font SIZE="-1">CPAN</font> module has a bug tracker set up in <font SIZE="-1">RT,</font> &lt;<a rel="nofollow" HREF="http://rt.cpan.org">http://rt.cpan.org</a>&gt;. You can submit bugs to <font SIZE="-1">RT</font> either through its web interface or by email. To email a bug report, send it to bug-&lt;distribution-name&gt;@rt.cpan.org . For example, if you wanted to report a bug in Business::ISBN, you could send a message to bug-Business-ISBN [at] rt.cpan.org . 

 Some modules might have special reporting requirements, such as a Github or Google Code tracking system, so you should check the module documentation too.

<h2>AUTHOR AND COPYRIGHT</h2>

 Copyright (c) 1997-2010 Tom Christiansen, Nathan Torkington, and other authors as noted. All rights reserved. 

 This documentation is free; you can redistribute it and/or modify it under the same terms as Perl itself. 

 Irrespective of its distribution, all code examples here are in the public domain. You are permitted and encouraged to use this code and any derivatives thereof in your own programs for fun or for profit as you see fit. A simple comment in the code giving credit to the <font SIZE="-1">FAQ</font> would be courteous but is not required. 

<h2>Index</h2>



<dt><a HREF="#lbAT">AUTHOR AND COPYRIGHT</a>
<dd></dl>
