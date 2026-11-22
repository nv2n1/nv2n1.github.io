---

title: "yapp(1)"
name: "yapp"
section: "1"
letter: "y"
url: "/docs/linux/man/1-yapp/"
---

yapp - A perl frontend to the Parse::Yapp module 

<h2>SYNOPSYS</h2>

 yapp [options] <i>grammar</i>[.yp] 

 yapp <i>-V</i> 

 yapp <i>-h</i>

<h2>DESCRIPTION</h2>

 yapp is a frontend to the Parse::Yapp module, which lets you compile Parse::Yapp grammar input files into Perl <i>LALR</i><i></i>(1) OO parser modules.

<h2>OPTIONS</h2>

 Options, as of today, are all optionals :-)
<dl>
<dt><i>-v</i>
</dt><dd> Creates a file <i>grammar</i>.output describing your parser. It will show you a summary of conflicts, rules, the DFA (Deterministic Finite Automaton) states and overall usage of the parser.
</dd><dt><i>-s</i>
</dt><dd> Create a standalone module in which the driver is included. Note that if you have more than one parser module called from a program, to have it standalone, you need this option only for one of your parser module.
</dd><dt><i>-n</i>
</dt><dd> Disable source file line numbering embedded in your parser module. I don't know why one should need it, but it's there.
</dd><dt><i>-m module</i>
</dt><dd> Gives your parser module the package name (or name space or module name or class name or whatever-you-call-it) of <i>module</i>. It defaults to <i>grammar</i>
</dd><dt><i>-o outfile</i>
</dt><dd> The compiled output file will be named <i>outfile</i> for your parser module. It defaults to <i>grammar</i>.pm or, if you specified the option <i>-m A::Module::Name</i> (see below), to <i>Name.pm</i>.
</dd><dt><i>-t filename</i>
</dt><dd> The <i>-t filename</i> option allows you to specify a file which should be used as template for generating the parser output. The default is to use the internal template defined in <i>Parse::Yapp::Output.pm</i>. For how to write your own template and which substitutions are available, have a look to the module <i>Parse::Yapp::Output.pm</i> : it should be obvious.
</dd><dt><i>-b shebang</i>
</dt><dd> If you work on systems that understand so called <i>shebangs</i>, and your generated parser is directly an executable script, you can specifie one with the <i>-b</i> option, ie: 
 <pre>
    yapp -b '/usr/local/bin/perl -w' -o myscript.pl myscript.yp
</pre> 
 This will output a file called <i>myscript.pl</i> whose very first line is: 
 <pre>
    #!/usr/local/bin/perl -w
</pre> 
 The argument is mandatory, but if you specify an empty string, the value of <i></i>$Config<i>{perlpath}</i> will be used instead.
</dd><dt><i>grammar</i>
</dt><dd> The input grammar file. If no suffix is given, and the file does not exists, an attempt to open the file with a suffix of <i>.yp</i> is tried before exiting.
</dd><dt><i>-V</i>
</dt><dd> Display current version of Parse::Yapp and gracefully exits.
</dd><dt><i>-h</i>
</dt><dd> Display the usage screen.</dd></dl>

<h2>BUGS</h2>

 None known now :-)

<h2>AUTHOR</h2>

 Francois Desarmenien &lt;francois [at] fdesar.net&gt;

<h2>COPYRIGHT</h2>

 (c) Copyright 1998-1999 Francois Desarmenien, all rights reserved. See <i>Parse::Yapp</i>(3) for legal use and distribution rights

<h2>SEE ALSO</h2>

 <i>Parse::Yapp</i>(3) <i><a HREF="/docs/linux/man/1-perl/">Perl</a></i>(1) <i><a HREF="/docs/linux/man/1-yacc/">yacc</a></i>(1) <i><a HREF="/docs/linux/man/1-bison/">bison</a></i>(1)
