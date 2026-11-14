---
title: "perlrun(1)"
name: "perlrun"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlrun/"
description: "perlrun – how to execute the Perl interpreter"
---

<h2 class="name">NAME</h2>
<p> perlrun &#8211; how to execute the Perl interpreter </p>
<h2>SYNOPSIS</h2>
<p> <code>perl</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>[ <code>-sTtuUWX</code> ]<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>[ <code>-hv</code> ] [ <code>-V</code>[:<i>configvar</i>] ]<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>[ <code>-cw</code> ] [ <code>-d</code>[<code>t</code>][:<i>debugger</i>] ] [ <code>-D</code>[<i>number/list</i>] ]<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>[ <code>-pna</code> ] [ <code>-F</code><i>pattern</i> ] [ <code>-l</code>[<i>octal</i>] ] [ <code>-0</code>[<i>octal/hexadecimal</i>] ]<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>[ <code>-I</code><i>dir</i> ] [ <code>-m</code>[<code>&#8211;</code>]<i>module</i> ] [ <code>-M</code>[<code>&#8211;</code>]<i>&#8216;module&#8230;&#8217;</i> ] [ <code>-f</code> ]<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>[ <code>-C [</code>number/list<code>] </code>]<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>[ <code>-S</code> ]<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>[ <code>-x</code>[<i>dir</i>] ]<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>[ <code>-i</code>[<i>extension</i>] ]<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>[ [<code>-e</code>|<code>-E</code>] <i>&#8216;command&#8217;</i> ] [ <code>&#8212;</code> ] [ <i>programfile</i> ] [ <i>argument</i> ]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> The normal way to run a Perl program is by making it directly executable, or else by passing the name of the source file as an argument on the command line. (An interactive Perl environment is also possible&#8212;see perldebug for details on how to do that.) Upon startup, Perl looks for your program in one of the following places:</p>
<dl>
<dt>1.</p>
<dd> Specified line by line via <code>-e</code> or <code>-E</code> switches on the command line.</p>
<dt>2.</p>
<dd> Contained in the file specified by the first filename on the command line. (Note that systems supporting the <tt>&quot;#!&quot;</tt> notation invoke interpreters this way. See &#8220;Location of Perl&#8221;.)</p>
<dt>3.</p>
<dd> Passed in implicitly via standard input. This works only if there are no filename arguments&#8212;to pass arguments to a STDIN-read program you must explicitly specify a &#8220;-&#8221; for the program name.</dl>
<p> With methods 2 and 3, Perl starts parsing the input file from the beginning, unless you&#8217;ve specified a <code>-x</code> switch, in which case it scans for the first line starting with <tt>&quot;#!&quot;</tt> and containing the word &#8220;perl&#8221;, and starts there instead. This is useful for running a program embedded in a larger message. (In this case you would indicate the end of the program using the <tt>&quot;__END__&quot;</tt> token.) </p>
<p> The <tt>&quot;#!&quot;</tt> line is always examined for switches as the line is being parsed. Thus, if you&#8217;re on a machine that allows only one argument with the <tt>&quot;#!&quot;</tt> line, or worse, doesn&#8217;t even recognize the <tt>&quot;#!&quot;</tt> line, you still can get consistent switch behaviour regardless of how Perl was invoked, even if <code>-x</code> was used to find the beginning of the program. </p>
<p> Because historically some operating systems silently chopped off kernel interpretation of the <tt>&quot;#!&quot;</tt> line after 32 characters, some switches may be passed in on the command line, and some may not; you could even get a &#8220;-&#8221; without its letter, if you&#8217;re not careful. You probably want to make sure that all your switches fall either before or after that 32-character boundary. Most switches don&#8217;t actually care if they&#8217;re processed redundantly, but getting a &#8220;-&#8221; instead of a complete switch could cause Perl to try to execute standard input instead of your program. And a partial <code>-I</code> switch could also cause odd results. </p>
<p> Some switches do care if they are processed twice, for instance combinations of <code>-l</code> and <code>-0</code>. Either put all the switches after the 32-character boundary (if applicable), or replace the use of <code>-0</code><i>digits</i> by <tt>&quot;BEGIN{ $/ = &quot;
