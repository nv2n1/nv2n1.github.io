---
title: "pdlfaq(1)"
name: "pdlfaq"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdlfaq/"
description: "PDL::FAQ – Frequently asked questions about PDL"
---

<p>PDL::FAQ &#8211; Frequently asked questions about PDL </p>
<h2>Version</h2>
<p>Current <font SIZE="-1">FAQ</font> version: 1.004</p>
<h2>Description</h2>
<p>This is version 1.004 of the <font SIZE="-1">PDL FAQ,</font> a collection of frequently asked questions about <font SIZE="-1">PDL &#8211;</font> the Perl Data Language.</p>
<h2>About This Document</h2>
<h3>Q: 1.1 Where to find this document</h3>
<p>You can find the latest version of this document at &lt;<a rel="nofollow" href="http://pdl.perl.org/?docs=FAQ">http://pdl.perl.org/?docs=FAQ</a>&amp;title=Frequently%20Asked%20Questions&gt; .</p>
<h3>Q: 1.2 How to contribute to this document</h3>
<p>This is a considerably reworked version of the <font SIZE="-1">PDL FAQ.</font> As such many errors might have crept in and many updates might not have made it in. You are explicitly encouraged to let us know about questions which you think should be answered in this document but currently aren&#8217;t. </p>
<p> Similarly, if you think parts of this document are unclear, please tell the <font SIZE="-1">FAQ</font> maintainer about it. Where a specific answer is taken in full from someones posting the authorship should be indicated, let the <font SIZE="-1">FAQ</font> maintainer know if it isn&#8217;t. For more general information explicit acknowledgment is not made in the text, but rather there is an incomplete list of contributors at the end of this document. Please contact the <font SIZE="-1">FAQ</font> maintainer if you feel hard done by. </p>
<p> Send your comments, additions, suggestions or corrections to the <font SIZE="-1">PDL</font> mailing list at perldl [at] jach.hawaii.edu. See Q: 3.2 below for instructions on how to join the mailing lists.</p>
<h2>General Questions</h2>
<h3>Q: 2.1 What is <font SIZE="-1">PDL </font>?</h3>
<p><font SIZE="-1">PDL</font> stands for <i>Perl Data Language</i> . To say it with the words of Karl Glazebrook, initiator of the <font SIZE="-1">PDL</font> project: </p>
<pre> The PDL concept is to give standard perl5 the ability
 to COMPACTLY store and SPEEDILY manipulate the large
 N-dimensional data sets which are the bread and butter
 of scientific computing. e.g. $a=$b+$c can add two
 2048x2048 images in only a fraction of a second.</pre>
<p>It provides tons of useful functionality for scientific and numeric analysis. </p>
<p> For readers familiar with other scientific data evaluation packages it may be helpful to add that <font SIZE="-1">PDL</font> is in many respects similar to <font SIZE="-1">IDL, MATLAB</font> and similar packages. However, it tries to improve on a number of issues which were perceived (by the authors of <font SIZE="-1">PDL</font>) as shortcomings of those existing packages.</p>
<h3>Q: 2.2 Who supports <font SIZE="-1">PDL</font>? Who develops it?</h3>
<p><font SIZE="-1">PDL</font> is supported by its users. General informal support for <font SIZE="-1">PDL</font> is provided through the <font SIZE="-1">PDL</font> mailing list (perldl [at] jach.hawaii.edu , see below). </p>
<p> As a Perl extension (see Q: 2.5 below) it is devoted to the idea of free and open development put forth by the Perl community. <font SIZE="-1">PDL</font> was and is being actively developed by a loosely knit group of people around the world who coordinate their activities through the <font SIZE="-1">PDL</font> development mailing list (pdl-porters [at] jach.hawaii.edu , see Q: 3.2 below). If you would like to join in the ongoing efforts to improve <font SIZE="-1">PDL</font> please join this list.</p>
<h3>Q: 2.3 Why yet another Data Language ?</h3>
<p>There are actually several reasons and everyone should decide for himself which are the most important ones:</p>
<dl>
<dt>&bull;</p>
<dd><font SIZE="-1">PDL</font> is &#8220;free software&#8221;. The authors of <font SIZE="-1">PDL</font> think that this concept has several advantages: everyone has access to the sources -&gt; better debugging, easily adaptable to your own needs, extensible for your purposes, etc&#8230; In comparison with commercial packages such as <font SIZE="-1">MATLAB</font> and <font SIZE="-1">IDL</font> this is of considerable importance for workers who want to do some work at home and cannot afford the considerable cost to buy commercial packages for personal use.</p>
<dt>&bull;</p>
<dd><font SIZE="-1">PDL</font> is based on a powerful and well designed scripting language: Perl. In contrast to other scientific/numeric data analysis languages it has been designed using the features of a proven language instead of having grown into existence from scratch. Defining the control structures while features were added during development leads to languages that often appear clumsy and badly planned for most existing packages with similar scope as <font SIZE="-1">PDL.</font></p>
<dt>&bull;</p>
<dd>Using Perl as the basis a <font SIZE="-1">PDL</font> programmer has all the powerful features of Perl at his hand, right from the start. This includes regular expressions, associative arrays (hashes), well designed interfaces to the operating system, network, etc. Experience has shown that even in mainly numerically oriented programming it is often extremely handy if you have easy access to powerful semi-numerical or completely non-numerical functionality as well. For example, you might want to offer the results of a complicated computation as a server process to other processes on the network, perhaps directly accepting input from other processes on the network. Using Perl and existing Perl extension packages things like this are no problem at all (and it all will fit into your &#8220;<font SIZE="-1">PDL</font> script&#8221;).</p>
<dt>&bull;</p>
<dd>Extremely easy extensibility and interoperability as <font SIZE="-1">PDL</font> is a Perl extension; development support for Perl extensions is an integral part of Perl and there are already numerous extensions to standard Perl freely available on the network.</p>
<dt>&bull;</p>
<dd>Integral language features of Perl (regular expressions, hashes, object modules) immensely facilitated development and implementation of key concepts of <font SIZE="-1">PDL.</font> One of the most striking examples for this point is probably <font SIZE="-1">PDL::PP</font> (see Q: 6.16 below), a code generator/parser/pre-processor that generates <font SIZE="-1">PDL</font> functions from concise descriptions.</p>
<dt>&bull;</p>
<dd>None of the existing data languages follow the Perl language rules, which the authors firmly believe in:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd><font SIZE="-1">TIMTOWTDI:</font> There is more than one way to do it. Minimalist languages are interesting for computer scientists, but for users, a little bit of redundancy makes things wildly easier to cope with and allows individual programming styles &#8211; just as people speak in different ways. For many people this will undoubtedly be a reason to avoid <font SIZE="-1">PDL </font>;)</p>
<dt>&bull;</p>
<dd>Simple things are simple, complicated things possible: Things that are often done should be easy to do in the language, whereas seldom done things shouldn&#8217;t be too cumbersome.</dl>
</dl>
<dl>
<dd>All existing languages violate at least one of these rules.</dl>
<dt>&bull;</p>
<dd>As a project for the future <font SIZE="-1">PDL</font> should be able to use super computer features, e.g. vector capabilities/parallel processing, <font SIZE="-1">GPGPU</font> acceleration. This will probably be achieved by having <font SIZE="-1">PDL::PP</font> (see Q: 6.16 below) generate appropriate code on such architectures to exploit these features.</p>
<dt>&bull;</p>
<dd>[ fill in your personal 111 favourite reasons here&#8230;]</dl>
<h3>Q: 2.4 What is <font SIZE="-1">PDL</font> good for ?</h3>
<p>Just in case you do not yet know what the main features of <font SIZE="-1">PDL</font> are and what one could do with them, here is a (necessarily selective) list of key features: </p>
<p> <font SIZE="-1">PDL</font> is well suited for matrix computations, general handling of multidimensional data, image processing, general scientific computation, numerical applications. It supports I/O for many popular image and data formats, 1D (line plots), 2D (images) and 3D (volume visualization, surface plots via OpenGL &#8211; for instance implemented using Mesa or video card OpenGL drivers), graphics display capabilities and implements many numerical and semi-numerical algorithms. </p>
<p> Through the powerful pre-processor it is also easy to interface Perl to your favorite C routines, more of that further below.</p>
<h3>Q: 2.5 What is the connection between <font SIZE="-1">PDL</font> and Perl ?</h3>
<p><font SIZE="-1">PDL</font> is a Perl5 extension package. As such it needs an existing Perl5 installation (see below) to run. Furthermore, much of <font SIZE="-1">PDL</font> is written in Perl (+ some core functionality that is written in C). <font SIZE="-1">PDL</font> programs are (syntactically) just Perl scripts that happen to use some of the functionality implemented by the package &#8220;<font SIZE="-1">PDL&#8221;.</font></p>
<h3>Q: 2.6 What do I need to run <font SIZE="-1">PDL</font> on my machine ?</h3>
<p>Since <font SIZE="-1">PDL</font> is just a Perl5 package you need first of all an installation of Perl5 on your machine. As of this writing <font SIZE="-1">PDL</font> requires version 5.8 of perl, or higher. More information on where and how to get a Perl installation can be found at the Perl home page &lt;<a rel="nofollow" href="http://www.perl.org">http://www.perl.org</a>&gt; and at many <font SIZE="-1">CPAN</font> sites (if you do not know what <i></i><font SIZE="-1"><i>CPAN</i></font><i></i> is, check the answer to the next question). </p>
<p> To build <font SIZE="-1">PDL</font> you also need a working C compiler, support for Xsubs, and the package Extutils::MakeMaker. If you don&#8217;t have a compiler there might be a binary distribution available, see &#8220;Binary distributions&#8221; below. </p>
<p> If you can (or cannot) get <font SIZE="-1">PDL</font> working on a new (previously unsupported) platform we would like to hear about it. Please, report your success/failure to the <font SIZE="-1">PDL</font> mailing list at perldl [at] jach.hawaii.edu . We will do our best to assist you in porting <font SIZE="-1">PDL</font> to a new system.</p>
<h3>Q: 2.7 Where do I get it?</h3>
<p><font SIZE="-1">PDL</font> is available as source distribution in the <i>Comprehensive Perl Archive Network</i> (or <font SIZE="-1">CPAN</font>) and from the sourceforge.net project page at &lt;<a rel="nofollow" href="https://sourceforge.net/projects/pdl/files/">https://sourceforge.net/projects/pdl/files/</a>&gt;. The <font SIZE="-1">CPAN</font> archives contains not only the <font SIZE="-1">PDL</font> distribution but also just about everything else that is Perl-related. <font SIZE="-1">CPAN</font> is mirrored by dozens of sites all over the world. The main site is &lt;<a rel="nofollow" href="http://www.cpan.org">http://www.cpan.org</a>&gt;, and local <font SIZE="-1">CPAN</font> sites (mirrors) can be found there. Within <font SIZE="-1">CPAN</font> you find the latest released version of <font SIZE="-1">PDL</font> in the directory /modules/by-module/PDL/. <font SIZE="-1">PDL</font>&#8216;s homepage is at &lt;<a rel="nofollow" href="http://pdl.perl.org">http://pdl.perl.org</a>&gt; and the latest version can also be downloaded from there.</p>
<h3>Q: 2.8 What do I have to pay to get <font SIZE="-1">PDL</font>?</h3>
<p>We are delighted to be able to give you the nicest possible answer on a question like this: <font SIZE="-1">PDL</font> is *free software* and all sources are publicly available. But still, there are some copyrights to comply with. So please, try to be as nice as we (the <font SIZE="-1">PDL</font> authors) are and try to comply with them. </p>
<p> Oh, before you think it is *completely* free: you have to invest some time to pull the distribution from the net, compile and install it and (maybe) read the manuals.</p>
<h2>Getting Help/More Information</h2>
<h3>Q: 3.1 Where can I get information on <font SIZE="-1">PDL</font>?</h3>
<p>The complete <font SIZE="-1">PDL</font> documentation is available with the <font SIZE="-1">PDL</font> distribution. Use the command <tt>&quot;perldoc PDL&quot;</tt> to start learning about <font SIZE="-1">PDL.</font> </p>
<p> The easiest way by far, however, to get familiar with <font SIZE="-1">PDL</font> is to use the <font SIZE="-1">PDL</font> on-line help facility from within the <font SIZE="-1">PDL</font> shell, <tt>&quot;pdl2&quot;</tt> Just type <tt>&quot;pdl2&quot;</tt> at your system prompt. Once you are inside the <tt>&quot;pdl2&quot;</tt> shell type <tt>&quot;help&quot;</tt> . Using the <tt>&quot;help&quot;</tt> and <tt>&quot;apropos&quot;</tt> commands inside the shell you should be able to find the way round the documentation. </p>
<p> Even better, you can immediately try your newly acquired knowledge about <font SIZE="-1">PDL</font> by issuing PDL/Perl commands directly at the command line. To illustrate this process, here is the record of a typical <tt>&quot;pdl2&quot;</tt> session of a <font SIZE="-1">PDL</font> beginner (lengthy output is only symbolically reproduced in braces ( &lt;&#8230; &#8230;&gt; ) ): </p>
<pre> unix&gt; pdl2
 pdl&gt; help
 &lt; ... help output ... &gt;
 pdl&gt; help PDL::QuickStart
 &lt; ... perldoc page ... &gt;
 pdl&gt; $a = pdl (1,5,7.3,1.0)
 pdl&gt; $b = sequence float, 4, 4
 pdl&gt; help inner
 &lt; ... help on the 'inner' function ... &gt;
 pdl&gt; $c = inner $a, $b
 pdl&gt; p $c
 [22.6 79.8 137 194.2]</pre>
<p>For further sources of information that are accessible through the Internet see next question.</p>
<h3>Q: 3.2 Are there other <font SIZE="-1">PDL</font> information sources on the Internet?</h3>
<p>First of all, for all purely Perl-related questions there are tons of sources on the net. Good points to start are &lt;<a rel="nofollow" href="http://www.perl.com">http://www.perl.com</a>&gt; and &lt;<a href="http://www.perl.org">http://www.perl.org</a>&gt; . </p>
<p> The <font SIZE="-1">PDL</font> home site can be accessed by pointing your web browser to &lt;<a rel="nofollow" href="http://pdl.perl.org">http://pdl.perl.org</a>&gt; . It has tons of goodies for anyone interested in <font SIZE="-1">PDL:</font></p>
<dl>
<dt>&bull;</p>
<dd><font SIZE="-1">PDL</font> distributions</p>
<dt>&bull;</p>
<dd>On-line documentation</p>
<dt>&bull;</p>
<dd>Pointers to an <font SIZE="-1">HTML</font> archive of the <font SIZE="-1">PDL</font> mailing lists</p>
<dt>&bull;</p>
<dd>A list of platforms on which <font SIZE="-1">PDL</font> has been successfully tested.</p>
<dt>&bull;</p>
<dd>News about recently added features, ported libraries, etc.</p>
<dt>&bull;</p>
<dd>Name of the current pumpkin holders for the different <font SIZE="-1">PDL</font> modules (if you want to know what that means you better had a look at the web pages).</dl>
<p> If you are interested in <font SIZE="-1">PDL</font> in general you can join the <font SIZE="-1">PDL</font> mailing list perldl [at] jach.hawaii.edu. This is a forum to discuss programming issues in <font SIZE="-1">PDL,</font> report bugs, seek assistance with <font SIZE="-1">PDL</font> related problems, etc. To subscribe, fill out the form at &lt;<a rel="nofollow" href="http://mailman.jach.hawaii.edu/mailman/listinfo/perldl">http://mailman.jach.hawaii.edu/mailman/listinfo/perldl</a>&gt; . </p>
<p> A searchable archive and a hypertext version of the traffic on this list (1997-2004) can be found at &lt;<a rel="nofollow" href="http://www.xray.mpe.mpg.de/mailing-lists/perldl/">http://www.xray.mpe.mpg.de/mailing-lists/perldl/</a>&gt; . More recent messages (since June 2005) can be found at &lt;<a rel="nofollow" href="http://mailman.jach.hawaii.edu/mailman/listinfo/perldl">http://mailman.jach.hawaii.edu/mailman/listinfo/perldl</a>&gt; . </p>
<p> If you are interested in all the technical details of the ongoing <font SIZE="-1">PDL</font> development you can join the <font SIZE="-1">PDL</font> developers mailing list pdl-porters [at] jach.hawaii.edu . To subscribe, fill out the form at &lt;<a rel="nofollow" href="http://mailman.jach.hawaii.edu/mailman/listinfo/pdl-porters">http://mailman.jach.hawaii.edu/mailman/listinfo/pdl-porters</a>&gt; . </p>
<p> A searchable archive and a hypertext version of the traffic on this list (1997-2004) can be found at &lt;<a rel="nofollow" href="http://www.xray.mpe.mpg.de/mailing-lists/pdl-porters/">http://www.xray.mpe.mpg.de/mailing-lists/pdl-porters/</a>&gt; . More recent messages (since June 2005) can be found at &lt;<a rel="nofollow" href="http://mailman.jach.hawaii.edu/mailman/listinfo/pdl-porters">http://mailman.jach.hawaii.edu/mailman/listinfo/pdl-porters</a>&gt; . </p>
<p> Cross-posting between these lists should be avoided unless there is a <i>very</i> good reason for doing that.</p>
<h3>Q: 3.3 What is the current version of <font SIZE="-1">PDL </font>?</h3>
<p>As of this writing (<font SIZE="-1">FAQ</font> version 1.004 of 16 Sep 2013) the latest stable version is 2.006. The latest stable version should always be available from a <font SIZE="-1">CPAN</font> mirror site near you (see Question 2.7 for info on where to get <font SIZE="-1">PDL</font>). </p>
<p> The most current (possibly unstable) version of <font SIZE="-1">PDL</font> can be obtained from the Git repository, see Question 4.10 and periodic <font SIZE="-1">CPAN</font> developers releases of the Git code will be made for testing purposes and more general availability. The current post-PDL-2.006 developers release of <font SIZE="-1">PDL</font> is available as <i></i><font SIZE="-1"><i>CHM/PDL-2.006_07</i></font><i>.tar.gz</i> .</p>
<h3>Q: 3.4 I want to contribute to the further development of <font SIZE="-1">PDL.</font> How can I help?</h3>
<p>Two ways that you could help almost immediately are (1) participate in <font SIZE="-1">CPAN</font> Testers for <font SIZE="-1">PDL</font> and related modules, and (2) proofreading and clarifying the <font SIZE="-1">PDL</font> documentation so that it is most useable for <font SIZE="-1">PDL</font> users, especially new users. </p>
<p> To participate in <font SIZE="-1">CPAN</font> Testers and contribute test reports, the page &lt;<a rel="nofollow" href="http://wiki.cpantesters.org/wiki/QuickStart">http://wiki.cpantesters.org/wiki/QuickStart</a>&gt; has instructions for starting for either <tt>&quot;CPAN&quot;</tt> or <tt>&quot;CPANPLUS&quot;</tt> users. </p>
<p> If you have a certain project in mind you should check if somebody else is already working on it or if you could benefit from existing modules. Do so by posting your planned project to the <font SIZE="-1">PDL</font> developers mailing list at pdl-porters [at] jach.hawaii.edu . See the subscription instructions in Question 3.2. We are always looking for people to write code and/or documentation ;).</p>
<h3>Q: 3.5 I think I have found a bug in the current version of <font SIZE="-1">PDL.</font> What shall I do?</h3>
<p>First, make sure that the bug/problem you came across has not already been dealt with somewhere else in this <font SIZE="-1">FAQ. </font> Secondly, you can check the searchable archive of the <font SIZE="-1">PDL</font> mailing lists to find whether this bug has already been discussed. If you still haven&#8217;t found any explanations you can post a bug report to perldl [at] jach.hawaii.edu , or through the Bugs link on &lt;<a rel="nofollow" href="http://pdl.perl.org">http://pdl.perl.org</a>&gt; . See the <i></i><font SIZE="-1"><i>BUGS</i></font><i></i> file in the <font SIZE="-1">PDL</font> distribution for what information to include. If you are unsure, discussions via the perldl mailing list can be most helpful.</p>
<h2>Installation</h2>
<h3>Q: 4.1 I have problems installing <font SIZE="-1">PDL.</font> What shall I do?</h3>
<p>First make sure you have read the file <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> in the distribution. This contains a list of common problems which are unnecessary to repeat here. </p>
<p> Next, check the file <i>perldl.conf</i> to see if by editing the configuration options in that file you will be able to successfully build <font SIZE="-1">PDL.</font> Some of the modules need additional software installed, please refer to the file <i></i><font SIZE="-1"><i>DEPENDENCIES</i></font><i></i> for further details. Make sure to edit the location of these packages in perldl.conf if you have them in non-standard locations. </p>
<p> N.B. Unix shell specific: If you would like to save an edited perldl.conf for future builds just copy it as <i>~/.perldl.conf</i> into your home directory where it will be picked up automatically during the <font SIZE="-1">PDL</font> build process. </p>
<p> Also, check for another, pre-existing version of <font SIZE="-1">PDL</font> on the build system. Multiple <font SIZE="-1">PDL</font> installs in the same <font SIZE="-1">PATH</font> or <tt>@INC</tt> can cause puzzling test or build failures. </p>
<p> If you still can&#8217;t make it work properly please submit a bug report including detailed information on the problems you encountered to the perldl mailing list ( perldl [at] jach.hawaii.edu , see also above). Response is often rapid.</p>
<h3>Q: 4.2 Are there configuration files for <font SIZE="-1">PDL I</font> have to edit?</h3>
<p>Most users should not have to edit any configuration files manually. However, in some cases you might have to supply some information about awkwardly placed include files/libraries or you might want to explicitly disable building some of the optional <font SIZE="-1">PDL</font> modules. Check the files <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> and <i>perldl.conf</i> for details. </p>
<p> If you had to manually edit <i>perldl.conf</i> and are happy with the results you can keep the file handy for future reference. Place it in <i>~/.perldl.conf</i> where it will be picked up automatically or use <tt>&quot;perl Makefile.PL PDLCONF=your_file_name&quot;</tt> next time you build <font SIZE="-1">PDL.</font></p>
<h3>Q: 4.3 Do I need other software for successful operation?</h3>
<p>For the basic <font SIZE="-1">PDL</font> functionality you don&#8217;t need any additional software. However, some of the optional <font SIZE="-1">PDL</font> modules included in the distribution (notably most graphics and some I/O modules) require certain other libraries/programs to be installed. Check the file <i></i><font SIZE="-1"><i>DEPENDENCIES</i></font><i></i> in the distribution for details and directions on how to get these.</p>
<h3>Q: 4.4 How can I install <font SIZE="-1">PDL</font> in a non-standard location?</h3>
<p>To install <font SIZE="-1">PDL</font> in a non-standard location, use the <font SIZE="-1">INSTALL_BASE</font> option in the <tt>&quot;perl Makefile.PL&quot;</tt> configure step. For example, <tt>&quot;perl Makefile.PL INSTALL_BASE=/mydir/perl5&quot;</tt> will configure <font SIZE="-1">PDL</font> to install into the tree rooted at <tt>&quot;/mydir/perl5&quot;</tt>. For more details see &#8220;How do I keep my own module/library directory?&#8221; in perlfaq8 and subsequent sections. Another alternative is to use local::lib to do the heavy listing for the needed configuration.</p>
<h3>Q: 4.5 How can I force a completely clean installation?</h3>
<p>To guarantee a completely clean installation of <font SIZE="-1">PDL,</font> you will need to first delete the current installation files and folders. These will be all directories named <tt>&quot;PDL&quot;</tt> in the Perl <tt>@INC</tt> path, files named <tt>&quot;*Pdlpp*&quot;</tt> in any <tt>&quot;Inline&quot;</tt> directories, and the programs <tt>&quot;pdl, pdldoc, pdl2, perldl, and pptemplate&quot;</tt>. Then just build and install as usual. This is much easier to keep track of if you always install <tt>&quot;PDL&quot;</tt> into a non-standard location. See Q: 4.4 above.</p>
<h2>Binary Distributions</h2>
<h3>Q: 4.5 What binary distributions are available?</h3>
<p>Information about binary distributions of <font SIZE="-1">PDL</font> can be found on &lt;<a rel="nofollow" href="http://pdl.perl.org">http://pdl.perl.org</a>&gt; . At present there are binary distributions of <font SIZE="-1">PDL</font> for Linux (RedHat and Debian), FreeBSD, Mac <font SIZE="-1">OS X</font> and Windows, though they might not be the most recent version. </p>
<p> If someone is interested in providing binary distributions for other architectures, that would be very welcome. Let us know on the pdl-porters [at] jach.hawaii.edu mailing list. Also check your Linux distribution&#8217;s package manager as many now include <font SIZE="-1">PDL. </font> PPMs for win32 versions (both 32bit and 64bit) are also available.</p>
<h3>Q: 4.6 Does <font SIZE="-1">PDL</font> run on Linux? (And what about packages?)</h3>
<p>Yes, <font SIZE="-1">PDL</font> does run on Linux and indeed much of the development has been done under Linux. On &lt;<a rel="nofollow" href="http://pdl.perl.org">http://pdl.perl.org</a>&gt; you can find links to packages for some of the major distributions. Also check your distribution&#8217;s package manager (yum, apt, urpmi, &#8230;) as <font SIZE="-1">PDL</font> is now found by many of these.</p>
<h3>Q: 4.7 Does <font SIZE="-1">PDL</font> run under Windows?</h3>
<p><font SIZE="-1">PDL</font> builds fine on Win32 using MinGW or Microsoft compilers. See the <i>win32/INSTALL</i> file in the <font SIZE="-1">PDL</font> source distribution for details. Other compilers have not been tested&#8212;input is welcome. There is also a distribution of <font SIZE="-1">PDL</font> through ActiveState&#8217;s ppm, though it might not always be the latest version. <font SIZE="-1">PDL-2.006</font> builds out of the box on Strawberry Perl and ActiveState Perl.</p>
<h2>Cvs, Git, And On-Going Development</h2>
<h3>Q: 4.8 Can I get <font SIZE="-1">PDL</font> via <font SIZE="-1">CVS</font>?</h3>
<p>No. <font SIZE="-1">PDL</font> development was conducted with a <font SIZE="-1">CVS</font> repository from December 1999 to April 2009. In April 2009 the project switched to the Git version control system (see &lt;<a rel="nofollow" href="http://git-scm.com">http://git-scm.com</a>&gt;).</p>
<h3>Q: 4.9 How do I get <font SIZE="-1">PDL</font> via Git?</h3>
<p>Assume you have Git installed on your system and want to download the project source code into the directory <tt>&quot;PDL&quot;</tt>. To get read-only access to the repository, you type at the command line </p>
<pre> git clone <a href="git://git.code.sf.net/p/pdl/code">git://git.code.sf.net/p/pdl/code</a> pdl-code</pre>
<p>For official <font SIZE="-1">PDL</font> developers, to get read/write access to the repository type at the command line </p>
<pre> git clone <a href="ssh://USERNAME@git.code.sf.net/p/pdl/code">ssh://USERNAME@git.code.sf.net/p/pdl/code</a> pdl-code</pre>
<h3>Q: 4.10 I had a problem with the Git version, how do I check if someone has submitted a patch?</h3>
<p>The Sourceforge system contains a patch-manager which contains patches that have not yet been applied to the distribution. This can be accessed via the Tickets menu at <font SIZE="-1">PDL</font>&#8216;s Sourceforge project page &lt;<a rel="nofollow" href="http://sourceforge.net/projects/pdl">http://sourceforge.net/projects/pdl</a>&gt; . </p>
<p> In addition, if you are not subscribing to the mailing list, check the archive of the <tt>&quot;pdl-porters&quot;</tt> and <tt>&quot;perldl&quot;</tt> mailing lists. See Question 3.2 for details.</p>
<h3>Q: 4.11 I have gotten developer access to Git, how do I upload my changes?</h3>
<p>The first thing you should do is to read the Git documentation and learn the basics about Git. There are many sources available online. But here are the basics: </p>
<p> Before you upload your changes, commit them to <font SIZE="-1">YOUR</font> repository </p>
<pre> git add &lt;file1&gt; &lt;file2&gt; ...
 git commit</pre>
<p>or combine these two with </p>
<pre> git commit -a</pre>
<p>Then pull in any changes others have made </p>
<pre> git pull origin</pre>
<p>Test the <font SIZE="-1">PDL</font> before you push it to the main repository. If the code is broken for you, then it is most likely broken for others and they won&#8217;t be happy to have their recent <font SIZE="-1">PDL</font> fail to build! <font SIZE="-1">NOTE:</font> git makes it very easy to maintain a separate branch of development. [ <font SIZE="-1">TBD,</font> provide information on how ]. </p>
<p> Then update the shared repository (at <font SIZE="-1">SF</font>.net) with your changes </p>
<pre> git push origin master</pre>
<h2>Pdl Jargon</h2>
<h3>Q: 5.1 What is threading (is <font SIZE="-1">PDL</font> a newsreader) ?</h3>
<p>Unfortunately, in the context of <font SIZE="-1">PDL</font> the term threading can have two different (but related) meanings:</p>
<dl>
<dt>&bull;</p>
<dd>When mentioned in the <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> directions and possibly during the build process we have the usual computer science meaning of multi-threading in mind (useful mainly on multiprocessor machines or clusters)</p>
<dt>&bull;</p>
<dd><font SIZE="-1">PDL</font> threading of operations on piddles (as mentioned in the indexing docs) is the iteration of a basic operation over appropriate sub-slices of piddles, e.g. the inner product <tt>&quot;inner $a, $b&quot;</tt> of a (3) pdl <tt>$a</tt> and a (3,5,4) pdl <tt>$b</tt> results in a (5,4) piddle where each value is the result of an inner product of the (3) pdl with a (3) sub-slice of the (3,5,4) piddle. For details check PDL::Indexing</dl>
<p> <font SIZE="-1">PDL</font> threading leads naturally to potentially parallel code which can make use of multi threading on multiprocessor machines/networks; there you have the connection between the two types of use of the term.</p>
<h3>Q: 5.2 What is a piddle?</h3>
<p>Well, <font SIZE="-1">PDL</font> scalar variables (which are instances of a particular class of Perl objects, i.e. blessed thingies (see <tt>&quot;perldoc perlobj&quot;</tt> )) are in common <font SIZE="-1">PDL</font> parlance often called <i>piddles</i> (for example, check the mailing list archives). Err, clear? If not, simply use the term <i>piddle</i> when you refer to a <font SIZE="-1">PDL</font> variable (an instance of a <font SIZE="-1">PDL</font> object as you might remember) regardless of what actual data the <font SIZE="-1">PDL</font> variable contains.</p>
<h2>Technical Questions</h2>
<h3>Q: 6.1 What is perldl? What is pdl2?</h3>
<p>Sometimes <tt>&quot;perldl&quot;</tt> (<tt>&quot;pdl2&quot;</tt>) is used as a synonym for <font SIZE="-1">PDL.</font> Strictly speaking, however, the name <tt>&quot;perldl&quot;</tt> (<tt>&quot;pdl2&quot;</tt>) is reserved for the little shell that comes with the <font SIZE="-1">PDL</font> distribution and is supposed to be used for the interactive prototyping of <font SIZE="-1">PDL</font> scripts. For details check perldl or pdl2.</p>
<h3>Q: 6.2 How do I get on-line help for <font SIZE="-1">PDL</font>?</h3>
<p>Just type <tt>&quot;help&quot;</tt> (shortcut = &#8220;?&#8221;) at the <tt>&quot;pdl2&quot;</tt> shell prompt and proceed from there. Another useful command is the <tt>&quot;apropos&quot;</tt> (shortcut = &#8220;??&#8221;) command. Also try the <tt>&quot;demo&quot;</tt> command in the <tt>&quot;perldl&quot;</tt> or <tt>&quot;pdl2&quot;</tt> shell if you are new to <font SIZE="-1">PDL.</font></p>
<h2>Manipulation Of Piddles</h2>
<h3>Q: 6.3 I want to access the third element of a pdl but $a[2] doesn&#8217;t work ?!</h3>
<p>See answer to the next question why the normal Perl array syntax doesn&#8217;t work for piddles.</p>
<h3>Q: 6.4 The docs say piddles are some kind of array. But why doesn&#8217;t the Perl array syntax work with piddles then ?</h3>
<p><font SIZE="-1">OK,</font> you are right in a way. The docs say that piddles can be thought of arrays. More specifically, it says ( PDL::QuickStart ): </p>
<pre> I find when using the Perl Data Language it is most useful
 to think of standard Perl @x variables as &quot;lists&quot; of generic
 &quot;things&quot; and PDL variables like $x as &quot;arrays&quot; which can be
 contained in lists or hashes.</pre>
<p>So, while piddles can be thought of as some kind of multi-dimensional array they are <code> not</code> arrays in the Perl sense. Rather, from the point of view of Perl they are some special class (which is currently implemented as an opaque pointer to some stuff in memory) and therefore need special functions (or &#8216;methods&#8217; if you are using the <font SIZE="-1">OO</font> version) to access individual elements or a range of elements. The functions/methods to check are <tt>&quot;at&quot;</tt> / <tt>&quot;set&quot;</tt> (see the section &#8216;Sections&#8217; in PDL::QuickStart ) or the powerful <tt>&quot;slice&quot;</tt> function and friends (see PDL::Slices and PDL::Indexing and especially PDL::NiceSlice ). </p>
<p> Finally, to confuse you completely, you can have Perl arrays of piddles, e.g. <tt>$spec[3]</tt> can refer to a pdl representing ,e.g, a spectrum, where <tt>$spec[3]</tt> is the fourth element of the Perl list (or array ;) <tt>@spec</tt> . This may be confusing but is very useful !</p>
<h3>Q: 6.5 How do I concatenate piddles?</h3>
<p>Most people will try to form new piddles from old piddles using some variation over the theme: <tt>&quot;$a = pdl([$b, 0, 2])&quot;</tt> , but this does not work. The way to concatenate piddles is to use the function <tt>&quot;cat&quot;</tt> (see also <tt>&quot;append&quot;</tt> and <tt>&quot;glue&quot;</tt>). Similarly you can split piddles using the command <tt>&quot;dog&quot;</tt> .</p>
<h3>Q: 6.6 Sometimes I am getting these strange results when using inplace operations?</h3>
<p>This question is related to the <tt>&quot;inplace&quot;</tt> function. From the documentation (see PDL::QuickStart): </p>
<pre> Most functions, e.g. log(), return a result which is a
 transformation of their argument. This makes for good
 programming practice. However many operations can be done
 &quot;in-place&quot; and this may be required when large arrays are in
 use and memory is at a premium. For these circumstances the
 operator inplace() is provided which prevents the extra copy
 and allows the argument to be modified. e.g.:
 
 $x = log($array); # $array unaffected
 log( inplace($bigarray) ); # $bigarray changed in situ</pre>
<p>And also from the doc !!: </p>
<pre> Obviously when used with some functions which can not be
 applied in situ (e.g. convolve()) unexpected effects may
 occur!</pre>
<h3>Q: 6.7 What is this strange usage of the string concatenation operator .= in <font SIZE="-1">PDL</font> scripts?</h3>
<p>See next question on assignment in <font SIZE="-1">PDL.</font></p>
<h3>Q: 6.8 Why are there two different kinds of assignment in <font SIZE="-1">PDL </font>?</h3>
<p>This is caused by the fact that currently the assignment operator <tt>&quot;=&quot;</tt> allows only restricted overloading. For some purposes of <font SIZE="-1">PDL</font> it turned out to be necessary to have more control over the overloading of an assignment operator. Therefore, <font SIZE="-1">PDL</font> peruses the operator <tt>&quot;.=&quot;</tt> for certain types of assignments.</p>
<h3>Q: 6.9 How do I set a set of values in a piddle?</h3>
<p>In Perl 5.6.7 and higher this assignment can be made using lvalue subroutines: </p>
<pre> pdl&gt; $a = <a href="//www.systutorials.com/docs/linux/man/5-sequence/">sequence</a>(5); p $a
 [0 1 2 3 4]
 pdl&gt; $a-&gt;slice('1:2') .= pdl([5,6])
 pdl&gt; p $a
 [0 5 6 3 4]</pre>
<p>see PDL::Lvalue for more info. <font SIZE="-1">PDL</font> also supports a more matrix-like slice syntax via the PDL::NiceSlice module: </p>
<pre> pdl&gt; $a(1:2) .= pdl([5,6])
 pdl&gt; p $a
 [0 5 6 3 4]</pre>
<p>With versions of Perl prior to 5.6.7 <code>or when running under the perl debugger</code> this has to be done using a temporary variable: </p>
<pre> pdl&gt; $a = <a href="//www.systutorials.com/docs/linux/man/5-sequence/">sequence</a>(5); p $a
 [0 1 2 3 4]
 pdl&gt; $tmp = $a-&gt;slice('1:2'); p $tmp;
 [1 2]
 pdl&gt; $tmp .= pdl([5, 6]); # Note .= !!
 pdl&gt; p $a
 [0 5 6 3 4]</pre>
<p>This can also be made into one expression, which is often seen in <font SIZE="-1">PDL</font> code: </p>
<pre> pdl&gt; ($tmp = $a-&gt;slice('1:2')) .= pdl([5,6])
 pdl&gt; p $a
 [0 5 6 3 4]</pre>
<h3>Q: 6.10 Can I use a piddle in a conditional expression?</h3>
<p>Yes you can, but not in the way you probably tried first. It is not possible to use a piddle directly in a conditional expression since this is usually poorly defined. Instead <font SIZE="-1">PDL</font> has two very useful functions: <tt>&quot;any&quot;</tt> and <tt>&quot;all&quot;</tt> . Use these to test if any or all elements in a piddle fulfills some criterion: </p>
<pre> pdl&gt; $a=pdl ( 1, -2, 3);
 pdl&gt; print '$a has at least one element &lt; 0' if (any $a &lt; 0);
 $a has at least one element &lt; 0
 
 pdl&gt; print '$a is not positive definite' unless (all $a &gt; 0);
 $a is not positive definite</pre>
<h3>Q: 6.11 Logical operators and piddles &#8211; &#8216;||&#8217; and &#8216;&amp;&amp;&#8217; don&#8217;t work!</h3>
<p>It is a common problem that you try to make a mask array or something similar using a construct such as </p>
<pre> $mask = which($piddle &gt; 1 &amp;&amp; $piddle &lt; 2); # incorrect</pre>
<p>This <code> does not</code> work! What you are looking for is the <code> bitwise</code> logical operators &#8216;|&#8217; and &#8216;&amp;&#8217; which work on an element-by-element basis. So it is really very simple: Do not use logical operators on multi-element piddles since that really doesn&#8217;t make sense, instead write the example as: </p>
<pre> $mask = which($piddle &gt; 1 &amp; $piddle &lt; 2);</pre>
<p>which works correctly.</p>
<h2>Advanced Topics</h2>
<h3>Q: 6.12 What is a null pdl ?</h3>
<p><tt>&quot;null&quot;</tt> is a special token for &#8217;empty piddle&#8217;. A null pdl can be used to flag to a <font SIZE="-1">PDL</font> function that it should create an appropriately sized and typed piddle. <i>Null</i> piddles can be used in places where a <font SIZE="-1">PDL</font> function expects an <i>output</i> or <i>temporary</i> argument. <i>Output</i> and <i>temporary</i> arguments are flagged in the <i>signature</i> of a <font SIZE="-1">PDL</font> function with the <tt>&quot;[o]&quot;</tt> and <tt>&quot;[t]&quot;</tt> qualifiers (see next question if you don&#8217;t know what the <i>signature</i> of a <font SIZE="-1">PDL</font> function is). For example, you can invoke the <tt>&quot;sumover&quot;</tt> function as follows: </p>
<pre> sumover $a, $b=null;</pre>
<p>which is equivalent to </p>
<pre> $b = sumover $a;</pre>
<p>If this seems still a bit murky check PDL::Indexing and <font SIZE="-1">PDL::PP</font> for details about calling conventions, the <i>signature</i> and <i>threading</i> (see also below).</p>
<h3>Q: 6.13 What is the signature of a <font SIZE="-1">PDL</font> function ?</h3>
<p>The <i>signature</i> of a function is an important concept in <font SIZE="-1">PDL.</font> Many (but not all) <font SIZE="-1">PDL</font> function have a <i>signature</i> which specifies the arguments and their (minimal) dimensionality. As an example, look at the signature of the <tt>&quot;maximum&quot;</tt> function: </p>
<pre> '<a href="//www.systutorials.com/docs/linux/man/n-a/">a</a>(n); [o] b;'</pre>
<p>this says that <tt>&quot;maximum&quot;</tt> takes two arguments, the first of which is (at least) one-dimensional while the second one is zero-dimensional and an <i>output</i> argument (flagged by the <tt>&quot;[o]&quot;</tt> qualifier). If the function is called with piddles of higher dimension the function will be repeatedly called with slices of these piddles of appropriate dimension(this is called <i>threading</i> in <font SIZE="-1">PDL</font>). </p>
<p> For details and further explanations consult PDL::Indexing and <font SIZE="-1">PDL::PP</font> .</p>
<h3>Q: 6.14 How can I subclass (inherit from) piddles?</h3>
<p>The short answer is: read PDL::Objects (e.g. type <tt>&quot;help PDL::Objects&quot;</tt> in the <i>perldl</i> or <i>pdl2</i> shell). </p>
<p> The longer answer (extracted from PDL::Objects ): Since a <font SIZE="-1">PDL</font> object is an opaque reference to a C struct, it is not possible to extend the <font SIZE="-1">PDL</font> class by e.g. extra data via sub-classing (as you could do with a hash based Perl object). To circumvent this problem <font SIZE="-1">PDL</font> has built-in support to extend the <font SIZE="-1">PDL</font> class via the <i>has-a</i> relation for blessed hashes. You can get the <i>HAS-A</i> to behave like <i>IS-A</i> simply in that you assign the <font SIZE="-1">PDL</font> object to the attribute named <tt>&quot;PDL&quot;</tt> and redefine the method <i>initialize()</i>. For example: </p>
<pre> package FOO;
 
 @FOO::ISA = qw(PDL);
 sub initialize {
 my $class = shift;
 my $self = {
 creation_time =&gt; time(), # necessary extension :-)
 PDL =&gt; PDL-&gt;null, # used to store PDL object
 };
 bless $self, $class;
 }</pre>
<p>For another example check the script <i>t/subclass.t</i> in the <font SIZE="-1">PDL</font> distribution.</p>
<h3>Q: 6.15 What on earth is this dataflow stuff ?</h3>
<p>Dataflow is an experimental project that you don&#8217;t need to concern yourself with (it should not interfere with your usual programming). However, if you want to know, have a look at PDL::Dataflow . There are applications which will benefit from this feature (and it is already at work behind the scenes).</p>
<h3>Q: 6.16 What is <font SIZE="-1">PDL::PP</font>?</h3>
<p>Simple answer: <font SIZE="-1">PDL::PP</font> is both a glue between external libraries and <font SIZE="-1">PDL</font> and a concise language for writing <font SIZE="-1">PDL</font> functions. </p>
<p> Slightly longer answer: <font SIZE="-1">PDL::PP</font> is used to compile very concise definitions into <font SIZE="-1">XSUB</font> routines implemented in C that can easily be called from <font SIZE="-1">PDL</font> and which automatically support threading, dataflow and other things without you having to worry about it. </p>
<p> For further details check <font SIZE="-1">PDL::PP</font> and the section below on Extensions of <font SIZE="-1">PDL</font>.</p>
<h3>Q: 6.17 What happens when I have several references to the same <font SIZE="-1">PDL</font> object in different variables (cloning, etc?) ?</h3>
<p>Piddles behave like Perl references in many respects. So when you say </p>
<pre> $a = pdl [0,1,2,3];
 $b = $a;</pre>
<p>then both <tt>$b</tt> and <tt>$a</tt> point to the same object, e.g. then saying </p>
<pre> $b++;</pre>
<p>will *not* create a copy of the original piddle but just increment in place, of which you can convince yourself by saying </p>
<pre> print $a;
 [1 2 3 4]</pre>
<p>This should not be mistaken for dataflow which connects several *different* objects so that data changes are propagated between the so linked piddles (though, under certain circumstances, dataflown piddles can share physically the same data). </p>
<p> It is important to keep the &#8220;reference nature&#8221; of piddles in mind when passing piddles into subroutines. If you modify the input piddles you modify the original argument, <i>not</i> a copy of it. This is different from some other array processing languages but makes for very efficient passing of piddles between subroutines. If you do not want to modify the original argument but rather a copy of it just create a copy explicitly (this example also demonstrates how to properly check for an <i>explicit</i> request to process inplace, assuming your routine can work inplace): </p>
<pre> sub myfunc {
 my $pdl = shift;
 if ($pdl-&gt;is_inplace) {
 $pdl-&gt;set_inplace(0)
 } else {
 # modify a copy by default
 $pdl = $pdl-&gt;copy
 }
 $pdl-&gt;set(0,0);
 return $pdl;
 }</pre>
<h2>Miscellaneous</h2>
<h3>Q: 6.18 What I/O formats are supported by <font SIZE="-1">PDL </font>?</h3>
<p>The current versions of <font SIZE="-1">PDL</font> already support quite a number of different I/O formats. However, it is not always obvious which module implements which formats. To help you find the right module for the format you require, here is a short list of the current list of I/O formats and a hint in which module to find the implementation:</p>
<dl>
<dt>&bull;</p>
<dd>A home brew fast raw (binary) I/O format for <font SIZE="-1">PDL</font> is implemented by the FastRaw module</p>
<dt>&bull;</p>
<dd>The FlexRaw module implements generic methods for the input and output of `raw&#8217; data arrays. In particular, it is designed to read output from <font SIZE="-1">FORTRAN 77 UNFORMATTED</font> files and the low-level C <tt>&quot;write&quot;</tt> function, even if the files are compressed or gzipped. </p>
<p> It is possible that the FastRaw functionality will be included in the FlexRaw module at some time in the future.</p>
<dt>&bull;</p>
<dd><font SIZE="-1">FITS I/O</font> is implemented by the <tt>&quot;wfits&quot;</tt>/<tt>&quot;rfits&quot;</tt> functions in <font SIZE="-1">PDL::IO::FITS</font> .</p>
<dt>&bull;</p>
<dd><font SIZE="-1">ASCII</font> file I/O in various formats can be achieved by using the <tt>&quot;rcols&quot;</tt> and <tt>&quot;rgrep&quot;</tt> functions, also in PDL::IO::Misc .</p>
<dt>&bull;</p>
<dd>PDL::IO::Pic implements an interface to the NetPBM/PBM+ filters to read/write several popular image formats; also supported is output of image sequences as <font SIZE="-1">MPEG</font> movies, animated GIFs and a wide variety of other video formats.</p>
<dt>&bull;</p>
<dd>On <font SIZE="-1">CPAN</font> you can find the PDL::NetCDF module that works with the current released version of <font SIZE="-1">PDL 2.006.</font></dl>
<p> For further details consult the more detailed list in the <font SIZE="-1">PDL::IO</font> documentation or the documentation for the individual modules.</p>
<h3>Q: 6.19 How can I stack a set of 2D arrays (images) into a 3D piddle?</h3>
<p>Assuming all arrays are of the same size and in some format recognized by <tt>&quot;rpic&quot;</tt> (see PDL::IO::Pic ) you could say: </p>
<pre> use PDL::IO::Pic;
 @names = qw/name1.tif .... nameN.tif/; # some file names
 $dummy = PDL-&gt;rpic($names[0]);
 $cube = PDL-&gt;zeroes($dummy-&gt;type,$dummy-&gt;dims,$#names+1); # make 3D piddle
 for (0..$#names) {
 # this is the slice assignment
 ($tmp = $cube-&gt;slice(&quot;:,:,($_)&quot;)) .= PDL-&gt;rpic($names[$_]);
 }</pre>
<p>or </p>
<pre> $cube(:,:,($_)) .= PDL-&gt;rpic($names[$_]);</pre>
<p>for the slice assignment using the new PDL::NiceSlice syntax and Lvalue assignments. </p>
<p> The for loop reads the actual images into a temporary 2D piddle whose values are then assigned (using the overloaded <tt>&quot;.=&quot;</tt> operator) to the appropriate slices of the 3D piddle <tt>$cube</tt> .</p>
<h3>Q: 6.20 Where are test files for the graphics modules?</h3>
<p>This answer applies mainly to PDL::Graphics::TriD (<font SIZE="-1">PDL</font>&#8216;s device independent 3D graphics model) which is the trickiest one in this respect. You find some test scripts in Demos/TriD in the distribution. There are also <i>3dtest.pl</i> and <i>line3d.pl</i> in the PDL/Example/TriD directory. After you have built <font SIZE="-1">PDL</font> you can do: </p>
<pre> perl -Mblib Example/TriD/3dtest.pl
 perl -Mblib Example/TriD/line3d.pl</pre>
<p>to try the two TriD test programs. They only exercise one TriD function each but their simplicity makes it easy to debug if needed with the Perl debugger, see perldbug. </p>
<p> The programs in the Demo directory can be run most easily from the <tt>&quot;perldl&quot;</tt> or <tt>&quot;pdl2&quot;</tt> interactive shell: </p>
<pre> perl -Mblib perldl or perl -Mblib Perldl2/pdl2</pre>
<p>followed by <tt>&quot;demo 3d&quot;</tt> or <tt>&quot;demo 3d2&quot;</tt> at the prompt. <tt>&quot;demo&quot;</tt> by itself will give you a list of the available <font SIZE="-1">PDL</font> demos. </p>
<p> You can run the test scripts in the Demos/TriD directory manually by changing to that directory and running </p>
<pre> perl -Mblib &lt;testfile&gt;</pre>
<p>where <tt>&quot;testfile&quot;</tt> ; should match the pattern <tt>&quot;test[3-9].p&quot;</tt> and watch the results. Some of the tests should bring up a window where you can control (twiddle) the 3D objects with the mouse. Try using mouse button 1 for turning the objects in 3D space, mouse button 3 to zoom in and out, and &#8216;q&#8217; to advance to the next stage of the test.</p>
<h3>Q: 6.21 What is TriD or PDL::TriD or PDL::Graphics::TriD?</h3>
<p>Questions like this should be a thing of the past with the <font SIZE="-1">PDL</font> on-line help system in place. Just try (after installation): </p>
<pre> un*x&gt; pdl2
 pdl&gt; apropos trid</pre>
<p>Check the output for promising hits and then try to look up some of them, e.g. </p>
<pre> pdl&gt; help PDL::Graphics::TriD</pre>
<p>Note that case matters with <tt>&quot;help&quot;</tt> but not with <tt>&quot;apropos&quot;</tt> .</p>
<h3>Q: 6.22 <font SIZE="-1">PGPLOT</font> does not write out <font SIZE="-1">PNG</font> files.</h3>
<p>There are a few sources of trouble with <font SIZE="-1">PGPLOT</font> and <font SIZE="-1">PNG</font> files. First, when compiling the pgplot libraries, make sure you uncomment the <font SIZE="-1">PNG</font> entries in the <i>drivers.list</i> file. Then when running &#8216;make&#8217; you probably got an error like </p>
<pre> C&lt;make: *** No rule to make target `png.h', needed by `pndriv.o'. Stop.&gt;</pre>
<p>To fix this, find the line in the &#8216;makefile&#8217; that starts with &#8216;pndriv.o:&#8217; (it&#8217;s near the bottom). Change, for example, ./png.h to /usr/include/png.h, if that is where your header files are (you do have the libpng and libz devel packages, don&#8217;t you?). Do this for all four entries on that line, then go back and run <tt>&quot;make&quot;</tt>. </p>
<p> Second, if you already have the <font SIZE="-1">PGPLOT</font> Perl module and <font SIZE="-1">PDL</font> installed, you probably tried to write out a <font SIZE="-1">PNG</font> file and got fatal error message like: </p>
<pre> C&lt;undefined symbol: png_create_write_struct&gt;</pre>
<p>This is because the <font SIZE="-1">PGPLOT</font> Perl module does not automatically link against the png and z libraries. So when you are installing the <font SIZE="-1">PGPLOT</font> Perl module (version 2.19) from <font SIZE="-1">CPAN,</font> don&#8217;t do <tt>&quot;install PGPLOT&quot;</tt>, but just do <tt>&quot;get PGPLOT&quot;</tt>. Then exit from <font SIZE="-1">CPAN</font> and manually install <font SIZE="-1">PGPLOT,</font> calling the makefile thusly: </p>
<pre> C&lt;perl Makefile.PL EXLIB=png,z EXDIR=/usr/lib&gt;</pre>
<p>assuming that there exist files such as /usr/lib/libpng.so.*, /usr/lib/libz.so.*. Then do the standard <tt>&quot;make;make test;make install;&quot;</tt> sequence. Now you can write png files from <font SIZE="-1">PDL</font>!</p>
<h2>Extensions Of Pdl</h2>
<h3>Q: 7.1 I am looking for a package to do <font SIZE="-1">XXX</font> in <font SIZE="-1">PDL.</font> Where shall I look for it?</h3>
<p>The first stop is again <tt>&quot;perldl&quot;</tt> or <tt>&quot;pdl2&quot;</tt> and the on-line help or the <font SIZE="-1">PDL</font> documentation. There is already a lot of functionality in <font SIZE="-1">PDL</font> which you might not be aware of. The easiest way to look for functionality is to use the <tt>&quot;apropos&quot;</tt> command: </p>
<pre> pdl&gt; apropos 'integral'
 ceil Round to integral values in floating-point format
 floor Round to integral values in floating-point format
 intover Project via integral to N-1 dimensions
 rint Round to integral values in floating-point format</pre>
<p>Since the apropos command is no sophisticated search engine make sure that you search on a couple of related topics and use short phrases. </p>
<p> However there is a good chance that what you need is not part of the <font SIZE="-1">PDL</font> distribution. You are then well advised to check out &lt;<a rel="nofollow" href="http://pdl.perl.org">http://pdl.perl.org</a>&gt; where there is a list of packages using <font SIZE="-1">PDL.</font> If that does not solve your problem, ask on the mailing-list, if nothing else you might get assistance which will let you interface your package with <font SIZE="-1">PDL</font> yourself, see also the next question.</p>
<h3>Q: 7.2 Can I access my C/FORTRAN library routines in <font SIZE="-1">PDL</font>?</h3>
<p>Yes, you can, in fact it is very simple for many simple applications. What you want is the <font SIZE="-1">PDL</font> pre-processor <font SIZE="-1">PP </font>(<font SIZE="-1">PDL::PP</font> ). This will allow you to make a simple interface to your C routine. </p>
<p> The two functions you need to learn (at least first) are <tt>&quot;pp_def&quot;</tt> which defines the calling interface to the function, specifying input and output parameters, and contains the code that links to the external library. The other command is <tt>&quot;pp_end&quot;</tt> which finishes the <font SIZE="-1">PP</font> definitions. For details see the <font SIZE="-1">PDL::PP</font> man-page, but we also have a worked example here. </p>
<pre> double eight_sum(int n)
 {
 int i;
 double sum, x;
 
 sum = 0.0; x=0.0;
 for (i=1; i&lt;=n; i++) {
 x++;
 sum += x/((4.0*x*x-1.0)*(4.0*x*x-1.0));
 } 
 return 1.0/sum;
 }</pre>
<p>We will here show you an example of how you interface C code with <font SIZE="-1">PDL.</font> This is the first example and will show you how to approximate the number 8&#8230; </p>
<p> The C code is shown above and is a simple function returning a double, and expecting an integer &#8211; the number of terms in the sum &#8211; as input. This function could be defined in a library or, as we do here, as an inline function. </p>
<p> We will postpone the writing of the Makefile till later. First we will construct the <tt>&quot;.pd&quot;</tt> file. This is the file containing <font SIZE="-1">PDL::PP</font> code. We call this <tt>&quot;eight.pd&quot;</tt> . </p>
<pre> # 
 # pp_def defines a PDL function. 
 #
 pp_addhdr (
 '
 double eight_sum(int n)
 {
 int i;
 double sum, x;
 
 sum = 0.0; x=0.0;
 for (i=1; i&lt;=n; i++) {
 x++; 
 sum += x/((4.0*x*x-1.0)*(4.0*x*x-1.0));
 }
 return 1.0/sum; 
 
 } 
 '); 
 
 pp_def (
 'eight',
 Pars =&gt; 'int a(); double [o]b();',
 Code =&gt; '$b()=eight_sum($a());'
 );
 
 # Always make sure that you finish your PP declarations with
 # pp_done
 
 pp_done();</pre>
<p>A peculiarity with our example is that we have included the entire code with <tt>&quot;pp_addhdr&quot;</tt> instead of linking it in. This is only for the purposes of example, in a typical application you will use <tt>&quot;pp_addhdr&quot;</tt> to include header files. Note that the argument to <tt>&quot;pp_addhdr&quot;</tt> is enclosed in quotes. </p>
<p> What is most important in this example is however the <tt>&quot;pp_def&quot;</tt> command. The first argument to this is the name of the new function <i>eight </i> , then comes a hash which the real meat:</p>
<dl>
<dt>&bull;</p>
<dd>This gives the input parameters (here <tt>&quot;a&quot;</tt>) and the output parameters (here <tt>&quot;b&quot;</tt>). The latter are indicated by the <tt>&quot;[o]&quot;</tt> specifier. Both arguments can have a type specification as shown here. </p>
<p> Many variations and further flexibility in the interface can be specified. See <tt>&quot;perldoc PDL::PP&quot;</tt> for details.</p>
<dt>&bull;</p>
<dd>This switch contains the code that should be executed. As you can see this is a rather peculiar mix of C and Perl, but essentially it is just as you would write it in C, but the variables that are passed from <font SIZE="-1">PDL</font> are treated differently and have to be referred to with a preceding &#8216;$&#8217;. </p>
<p> There are also simple macros to pass pointers to data and to obtain the values of other Perl quantities, see the manual page for further details.</dl>
<p> Finally note the call to <tt>&quot;pp_done()&quot;</tt> at the end of the file. This is necessary in all <font SIZE="-1">PP</font> files. </p>
<p> <font SIZE="-1">OK.</font> So now we have a file with code that we dearly would like to use in Perl via <font SIZE="-1">PDL.</font> To do this we need to compile the function, and to do that we need a Makefile. </p>
<pre> use PDL::Core::Dev;
 use ExtUtils::MakeMaker;
 PDL::Core::Dev-&gt;import();
 
 $package = [&quot;eight.pd&quot;,Eight,PDL::Eight];
 %hash = pdlpp_stdargs($package);
 
 WriteMakefile( %hash );
 
 sub MY::postamble {pdlpp_postamble($package)};</pre>
<p>The code above should go in a file called Makefile.PL, which should subsequently be called in the standard Perl way: <tt>&quot;perl Makefile.PL&quot;</tt> . This should give you a Makefile and running <tt>&quot;make&quot;</tt> should compile the module for you and <tt>&quot;make install&quot;</tt> will install it for you.</p>
<h3>Q: 7.3 How can I interface package <font SIZE="-1">XXX</font> in <font SIZE="-1">PDL</font>?</h3>
<p>This question is closely related to the previous one, and as we said there, the <font SIZE="-1">PDL::PP</font> pre-processor is the standard way of interfacing external packages with <font SIZE="-1">PDL.</font> The most usual way to use <font SIZE="-1">PDL::PP</font> is to write a short interface routine, see the <font SIZE="-1">PDL::PP</font> perldoc page and the answer to the previous question for examples. </p>
<p> However it is also possible to interface a package to <font SIZE="-1">PDL</font> by re-writing your function in <font SIZE="-1">PDL::PP</font> directly. This can be convenient in certain situations, in particular if you have a routine that expects a function as input and you would like to pass the function a Perl function for convenience. </p>
<p> The <font SIZE="-1">PDL::PP</font> perldoc page is the main source of information for writing <font SIZE="-1">PDL::PP</font> extensions, but it is very useful to look for files in the distribution of <font SIZE="-1">PDL</font> as many of the core functions are written in <font SIZE="-1">PDL::PP.</font> Look for files that end in <tt>&quot;.pd&quot;</tt> which is the generally accepted suffix for <font SIZE="-1">PDL::PP</font> files. But we also have a simple example here. </p>
<p> The following example will show you how to write a simple function that automatically allows threading. To make this concise the example is of an almost trivial function, but the intention is to show the basics of writing a <font SIZE="-1">PDL::PP</font> interface. </p>
<p> We will write a simple function that calculates the minimum, maximum and average of a piddle. On my machine the resulting function is 8 times faster than the built-in function <tt>&quot;stats&quot;</tt> (of course the latter also calculates the median). </p>
<p> Let&#8217;s jump straight in. Here is the code (from a file called <tt>&quot;quickstats.pd&quot;</tt> ) </p>
<pre> #
 pp_def('quickstats',
 Pars =&gt; '<a href="//www.systutorials.com/docs/linux/man/n-a/">a</a>(n); [o]avg(); [o]max(); [o]min()',
 Code =&gt; '$GENERIC(a) curmax, curmin;
 $GENERIC(a) tmp=0;
 <a href="//www.systutorials.com/docs/linux/man/n-loop/">loop</a>(n) %{
 tmp += $a();
 if (!n || $a() &gt; curmax) { curmax = $a();}
 if (!n || $a() &lt; curmin) { curmin = $a();}
 %}
 $avg() = tmp/$<a href="//www.systutorials.com/docs/linux/man/n-SIZE/">SIZE</a>(n);
 $max() = curmax;
 $min() = curmin;
 '
 );
 
 pp_done();</pre>
<p>The above might look like a confusing mixture of C and Perl, but behind the peculiar syntax lies a very powerful language. Let us take it line by line. </p>
<p> The first line declares that we are starting the definition of a <font SIZE="-1">PDL:PP</font> function called <tt>&quot;quickstats&quot;</tt> . </p>
<p> The second line is very important as it specifies the input and output parameters of the function. <tt><a href="/docs/linux/man/n-a/">a</a>(n)</tt> tells us that there is one input parameter that we will refer to as <tt>&quot;a&quot;</tt> which is expected to be a vector of length n (likewise matrices, both square and rectangular would be written as <tt>&quot;a(n,n)&quot;</tt> and <tt>&quot;a(n,m)&quot;</tt> respectively). To indicate that something is an output parameter we put <tt>&quot;[o]&quot;</tt> in front of their names, so referring back to the code we see that avg, max and min are three output parameters, all of which are scalar (since they have no dimensional size indicated. </p>
<p> The third line starts the code definition which is essentially pure C but with a couple of convenient functions. <tt>$GENERIC</tt> is a function that returns the C type of its argument &#8211; here the input parameter a. Thus the first two lines of the code section are variable declarations. </p>
<p> The <tt><a href="/docs/linux/man/n-loop/">loop</a>(n)</tt> construct is a convenience function that loops over the dimension called n in the parameter section. Inside this loop we calculate the cumulative sum of the input vector and keep track of the maximum and minimum values. Finally we assign the resulting values to the output parameters. </p>
<p> Finally we finish our function declaration with <tt>&quot;pp_done()&quot;</tt> . </p>
<p> To compile our new function we need to create a Makefile, which we will just list since its creation is discussed in an earlier question. </p>
<pre> use PDL::Core::Dev;
 use ExtUtils::MakeMaker;
 PDL::Core::Dev-&gt;import();
 
 $package = [&quot;quickstats.pd&quot;,Quickstats,PDL::Quickstats];
 %hash = pdlpp_stdargs($package);
 
 WriteMakefile( %hash );
 
 sub MY::postamble {pdlpp_postamble($package)};</pre>
<p>An example Makefile.PL </p>
<p> Our new statistic function should now compile using the tried and tested Perl way: <tt>&quot;perl Makefile.PL; make&quot;</tt> . </p>
<p> You should experiment with this function, changing the calculations and input and output parameters. In conjunction with the <font SIZE="-1">PDL::PP</font> perldoc page this should allow you to quickly write more advanced routines directly in <font SIZE="-1">PDL::PP.</font></p>
<h2>Bugs</h2>
<p>If you find any inaccuracies in this document (or dis-functional URLs) please report to the perldl mailing list perldl [at] jach.hawaii.edu.</p>
<h2>Acknowledgments</h2>
<p>Achim Bohnet (ach [at] mpe.mpg.de ) for suggesting CoolHTML as a prettypodder (although we have switched to <font SIZE="-1">XML</font> now) and various other improvements. Suggestions for some questions were taken from Perl <font SIZE="-1">FAQ</font> and adapted for <font SIZE="-1">PDL.</font></p>
<h2>Contributors</h2>
<p>Many people have contributed or given feedback on the current version of the <font SIZE="-1">FAQ,</font> here is an incomplete list of individuals whose contributions or posts to the mailing-list have improved this <font SIZE="-1">FAQ</font> at some point in time alphabetically listed by first name: Christian Soeller, Chris Marshall, Doug Burke, Doug Hunt, Frank Schmauder, Jarle Brinchmann, John Cerney, Karl Glazebrook, Kurt Starsinic, Thomas Yengst, Tuomas J. Lukka.</p>
<h2>Author And Copyright</h2>
<p>This document emerged from a joint effort of several <font SIZE="-1">PDL</font> developers (Karl Glazebrook, Tuomas J. Lukka, Christian Soeller) to compile a list of the most frequently asked questions about <font SIZE="-1">PDL</font> with answers. Permission is granted for verbatim copying (and formatting) of this material as part of <font SIZE="-1">PDL.</font> </p>
<p> Permission is explicitly not granted for distribution in book or any corresponding form. Ask on the <font SIZE="-1">PDL</font> mailing list perldl [at] jach.hawaii.edu if some of the issues covered in here are unclear.</p>
