---
title: "perlivp(1)"
name: "perlivp"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlivp/"
---

<h2 class="name">NAME</h2>
 

 perlivp - Perl Installation Verification Procedure 

<h2>SYNOPSIS</h2>

 <b>perlivp</b> [<b>-p</b>] [<b>-v</b>] [<b>-h</b>]

<h2>DESCRIPTION</h2>

 The <b>perlivp</b> program is set up at Perl source code build time to test the Perl version it was built under. It can be used after running: 

 <pre>
    make install
</pre> 

 (or your platform's equivalent procedure) to verify that <b>perl</b> and its libraries have been installed correctly. A correct installation is verified by output that looks like: 

 <pre>
    ok 1
    ok 2
</pre> 

 etc.

<h2>OPTIONS</h2>

<dl>
<dt><b>-h</b> help
<dd> Prints out a brief help message.
<dt><b>-p</b> print preface
<dd> Gives a description of each test prior to performing it.
<dt><b>-v</b> verbose
<dd> Gives more detailed information about each test, after it has been performed. Note that any failed tests ought to print out some extra information whether or not -v is thrown.</dl>

<h2>DIAGNOSTICS</h2>

<dl>
<dt>&bull;
<dd> print ``# Perl binary '$perlpath' does not appear executable.\n''; 

 Likely to occur for a perl binary that was not properly installed. Correct by conducting a proper installation.
<dt>&bull;
<dd> print ``# Perl version '$]' installed, expected <tt>$ivp_VERSION</tt>.\n''; 

 Likely to occur for a perl that was not properly installed. Correct by conducting a proper installation.
<dt>&bull;
<dd> print ``# Perl \@INC directory '$_' does not appear to exist.\n''; 

 Likely to occur for a perl library tree that was not properly installed. Correct by conducting a proper installation.
<dt>&bull;
<dd> print ``# Needed module '$_' does not appear to be properly installed.\n''; 

 One of the two modules that is used by perlivp was not present in the installation. This is a serious error since it adversely affects perlivp's ability to function. You may be able to correct this by performing a proper perl installation.
<dt>&bull;
<dd> print ``# Required module '$_' does not appear to be properly installed.\n''; 

 An attempt to <tt>&quot;eval &quot;require $module&quot;&quot;</tt> failed, even though the list of extensions indicated that it should succeed. Correct by conducting a proper installation.
<dt>&bull;
<dd> print ``# Unnecessary module 'bLuRfle' appears to be installed.\n''; 

 This test not coming out ok could indicate that you have in fact installed a bLuRfle.pm module or that the <tt>&quot;eval &quot; require \&quot;$module_name.pm\&quot;; &quot;&quot;</tt> test may give misleading results with your installation of perl. If yours is the latter case then please let the author know.
<dt>&bull;
<dd> print ``# file'',+($#missing == 0) ? '' : 's',`` missing from installation:\n''; 

 One or more files turned up missing according to a run of <tt>&quot;ExtUtils::Installed -&gt; validate()&quot;</tt> over your installation. Correct by conducting a proper installation.</dl>
 

 For further information on how to conduct a proper installation consult the <font SIZE="-1">INSTALL</font> file that comes with the perl source and the <font SIZE="-1">README</font> file for your platform.

<h2>AUTHOR</h2>

 Peter Prymmer 

<h2>Index</h2>


