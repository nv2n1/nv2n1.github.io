---
title: "perlriscos(1)"
name: "perlriscos"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlriscos/"
---

<h2 class="name">NAME</h2>
 

 perlriscos - Perl version 5 for RISC OS 

<h2>DESCRIPTION</h2>

 This document gives instructions for building Perl for <font SIZE="-1">RISC OS.</font> It is complicated by the need to cross compile. There is a binary version of perl available from &lt;<a rel="nofollow" HREF="http://www.cp15.org/perl/">http://www.cp15.org/perl/</a>&gt; which you may wish to use instead of trying to compile it yourself.

<h2>BUILD</h2>

 You need an installed and working gccsdk cross compiler &lt;<a rel="nofollow" HREF="http://gccsdk.riscos.info/">http://gccsdk.riscos.info/</a>&gt; and <font SIZE="-1">REXEN</font> &lt;<a rel="nofollow" HREF="http://www.cp15.org/programming/">http://www.cp15.org/programming/</a>&gt; 

 Firstly, copy the source and build a native copy of perl for your host system. Then, in the source to be cross compiled:
<dl>
<dt>1.
<dd> <pre>
    $ ./Configure
</pre>
<dt>2.
<dd> Select the riscos hint file. The default answers for the rest of the questions are usually sufficient. 

 Note that, if you wish to run Configure non-interactively (see the <font SIZE="-1">INSTALL</font> document for details), to have it select the correct hint file, you'll need to provide the argument -Dhintfile=riscos on the Configure command-line.
<dt>3.
<dd> <pre>
    $ make miniperl
</pre>
<dt>4.
<dd> This should build miniperl and then fail when it tries to run it.
<dt>5.
<dd> Copy the miniperl executable from the native build done earlier to replace the cross compiled miniperl.
<dt>6.
<dd> <pre>
    $ make
</pre>
<dt>7.
<dd> This will use miniperl to complete the rest of the build.</dl>

<h2>AUTHOR</h2>

 Alex Waugh &lt;alex [at] alexwaugh.com&gt; 

<h2>Index</h2>


