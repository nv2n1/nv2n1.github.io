---
title: "enc2xs(1)"
name: "enc2xs"
section: "1"
letter: "e"
url: "/docs/linux/man/1-enc2xs/"
description: "enc2xs — Perl Encode Module Generator"
---

<h2 class="name">NAME</h2>
<p> enc2xs &#8212; Perl Encode Module Generator </p>
<h2>SYNOPSIS</h2>
<pre>
  enc2xs -[options]
  enc2xs -M ModName mapfiles...
  enc2xs -C
</pre>
<h2>DESCRIPTION</h2>
<p> <i>enc2xs</i> builds a Perl extension for use by Encode from either Unicode Character Mapping files (.ucm) or Tcl Encoding Files (.enc). Besides being used internally during the build process of the Encode module, you can use <i>enc2xs</i> to add your own encoding to perl. No knowledge of <font SIZE="-1">XS</font> is necessary.</p>
<h2>Quick Guide</h2>
<p> If you want to know as little about Perl as possible but need to add a new encoding, just read this chapter and forget the rest.</p>
<dl>
<dt>0.</p>
<dd> Have a .ucm file ready. You can get it from somewhere or you can write your own from scratch or you can grab one from the Encode distribution and customize it. For the <font SIZE="-1">UCM</font> format, see the next Chapter. In the example below, I&#8217;ll call my theoretical encoding myascii, defined in <i>my.ucm</i>. <tt>&quot;$&quot;</tt> is a shell prompt. </p>
<pre>
  $ ls -F
  my.ucm
</pre>
<dt>1.</p>
<dd> Issue a command as follows; </p>
<pre>
  $ enc2xs -M My my.ucm
  generating Makefile.PL
  generating My.pm
  generating README
  generating Changes
</pre>
<p> Now take a look at your current directory. It should look like this. </p>
<pre>
  $ ls -F
  Makefile.PL   My.pm         my.ucm        t/
</pre>
<p> The following files were created. </p>
<pre>
  Makefile.PL - MakeMaker script
  My.pm       - Encode submodule
  t/My.t      - test file
</pre>
<dl>
<dt>
<dd>
<dl>
<dt>1.1.</p>
<dd> If you want *.ucm installed together with the modules, do as follows; </p>
<pre>
  $ mkdir Encode
  $ mv *.ucm Encode
  $ enc2xs -M My Encode/*ucm
</pre>
</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>2.</p>
<dd> Edit the files generated. You don&#8217;t have to if you have no time <font SIZE="-1">AND</font> no intention to give it to someone else. But it is a good idea to edit the pod and to add more tests.</p>
<dt>3.</p>
<dd> Now issue a command all Perl Mongers love: </p>
<pre>
  $ perl Makefile.PL
  Writing Makefile for Encode::My
</pre>
<dt>4.</p>
<dd> Now all you have to do is make. </p>
<pre>
  $ make
  cp My.pm blib/lib/Encode/My.pm
  /usr/local/bin/perl /usr/local/bin/enc2xs -Q -O \
    -o encode_t.c -f encode_t.fnm
  Reading myascii (myascii)
  Writing compiled form
  128 bytes in string tables
  384 bytes (75%) saved spotting duplicates
  1 bytes (0.775%) saved using substrings
  ....
  chmod 644 blib/arch/auto/Encode/My/My.bs
  $
</pre>
<p> The time it takes varies depending on how fast your machine is and how large your encoding is. Unless you are working on something big like euc-tw, it won&#8217;t take too long.</p>
<dt>5.</p>
<dd> You can &#8220;make install&#8221; already but you should test first. </p>
<pre><code>
$ make test
    PERL_DL_NONLAZY = 1 / usr / local / bin / perl - Iblib / arch - Iblib / lib - e 'use Test::Harness  qw(&amp;runtests $verbose); \
    $verbose=0; runtests @ARGV;' t/*.t
  t/My....ok
  All tests successful.
  Files=1, Tests=2,  0 wallclock secs
   ( 0.09 cusr + 0.01 csys = 0.09 CPU)
</code></pre>
<dt>6.</p>
<dd> If you are content with the test result, just &#8220;make install&#8221;</p>
<dt>7.</p>
<dd> If you want to add your encoding to Encode&#8217;s demand-loading list (so you don&#8217;t have to &#8220;use Encode::YourEncoding&#8221;), run </p>
<pre>
  enc2xs -C
</pre>
<p> to update Encode::ConfigLocal, a module that controls local settings. After that, &#8220;use Encode;&#8221; is enough to load your encodings on demand.</dl>
<h2>The Unicode Character Map</h2>
<p> Encode uses the Unicode Character Map (<font SIZE="-1">UCM</font>) format for source character mappings. This format is used by <font SIZE="-1">IBM</font>&#8216;s <font SIZE="-1">ICU</font> package and was adopted by Nick Ing-Simmons for use with the Encode module. Since <font SIZE="-1">UCM</font> is more flexible than Tcl&#8217;s Encoding Map and far more user-friendly, this is the recommended format for Encode now. </p>
<p> A <font SIZE="-1">UCM</font> file looks like this. </p>
<pre>
  #
  # Comments
  #
  &lt;code_set_name&gt; &quot;US-ascii&quot; # Required
  &lt;code_set_alias&gt; &quot;ascii&quot;   # Optional
  &lt;mb_cur_min&gt; 1             # Required; usually 1
  &lt;mb_cur_max&gt; 1             # Max. # of bytes/char
  &lt;subchar&gt; ?             # Substitution char
  #
  CHARMAP
  &lt;U0000&gt; 
