---
title: "perlvos(1)"
name: "perlvos"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlvos/"
---

<h2 class="name">NAME</h2>
 

 perlvos - Perl for Stratus OpenVOS 

<h2>SYNOPSIS</h2>

 This file contains notes for building perl on the Stratus OpenVOS operating system. Perl is a scripting or macro language that is popular on many systems. See perlbook for a number of good books on Perl. 

 These are instructions for building Perl from source. This version of Perl requires the dynamic linking support that is found in OpenVOS Release 17.1 and thus is not supported on OpenVOS Release 17.0 or earlier releases. 

 If you are running <font SIZE="-1">VOS</font> Release 14.4.1 or later, you can obtain a pre-compiled, supported copy of perl by purchasing the <font SIZE="-1">GNU</font> Tools product from Stratus Technologies.

<h2>BUILDING PERL FOR OPENVOS</h2>

 To build perl from its source code on the Stratus V Series platform you must have OpenVOS Release 17.1.0 or later, <font SIZE="-1">GNU</font> Tools Release 3.5 or later, and the C/POSIX Runtime Libraries. 

 Follow the normal instructions for building perl; e.g, enter bash, run the Configure script, then use ``gmake'' to build perl.

<h2>INSTALLING PERL IN OPENVOS</h2>

<dl>
<dt>1.
<dd> After you have built perl using the Configure script, ensure that you have modify and default write permission to <tt>&quot;&gt;system&gt;ported&quot;</tt> and all subdirectories. Then type 

 <pre>
     gmake install
</pre>
<dt>2.
<dd> While there are currently no architecture-specific extensions or modules distributed with perl, the following directories can be used to hold such files (replace the string <font SIZE="-1">VERSION</font> by the appropriate version number): 

 <pre>
     &gt;system&gt;ported&gt;lib&gt;perl5&gt;VERSION&gt;i786
</pre>
<dt>3.
<dd> Site-specific perl extensions and modules can be installed in one of two places. Put architecture-independent files into: 

 <pre>
     &gt;system&gt;ported&gt;lib&gt;perl5&gt;site_perl&gt;VERSION
</pre> 

 Put site-specific architecture-dependent files into one of the following directories: 

 <pre>
     &gt;system&gt;ported&gt;lib&gt;perl5&gt;site_perl&gt;VERSION&gt;i786
</pre>
<dt>4.
<dd> You can examine the <tt>@INC</tt> variable from within a perl program to see the order in which Perl searches these directories.</dl>

<h2>USING PERL IN OPENVOS</h2>

<h3>Restrictions of Perl on OpenVOS</h3>

 This port of Perl version 5 prefers Unix-style, slash-separated pathnames over OpenVOS-style greater-than-separated pathnames. OpenVOS-style pathnames should work in most contexts, but if you have trouble, replace all greater-than characters by slash characters. Because the slash character is used as a pathname delimiter, Perl cannot process OpenVOS pathnames containing a slash character in a directory or file name; these must be renamed. 

 This port of Perl also uses Unix-epoch date values internally. As long as you are dealing with <font SIZE="-1">ASCII</font> character string representations of dates, this should not be an issue. The supported epoch is January 1, 1980 to January 17, 2038. 

 See the file pod/perlport.pod for more information about the OpenVOS port of Perl.

<h2>TEST STATUS</h2>

 A number of the perl self-tests fails for various reasons; generally these are minor and due to subtle differences between common POSIX-based environments and the OpenVOS <font SIZE="-1">POSIX</font> environment. Ensure that you conduct sufficient testing of your code to guarantee that it works properly in the OpenVOS environment.

<h2>SUPPORT STATUS</h2>

 I'm offering this port ``as is''. You can ask me questions, but I can't guarantee I'll be able to answer them. There are some excellent books available on the Perl language; consult a book seller. 

 If you want a supported version of perl for OpenVOS, purchase the OpenVOS <font SIZE="-1">GNU</font> Tools product from Stratus Technologies, along with a support contract (or from anyone else who will sell you support).

<h2>AUTHOR</h2>

 Paul Green (Paul.Green [at] stratus.com)

<h2>LAST UPDATE</h2>

 February 28, 2013 

<h2>Index</h2>


