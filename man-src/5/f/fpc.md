---
title: "fpc(5)"
name: "fpc"
section: "5"
letter: "f"
url: "/docs/linux/man/5-fpc/"
description: "fpc.cfg – Free Pascal Compiler (FPC) configuration file, name derived from Free Pascal Compiler."
---

<p>fpc.cfg &#8211; Free Pascal Compiler (FPC) configuration file, name derived from Free Pascal Compiler. </p>
<h2>Description</h2>
<p>This is the main configuration file of the <i>Free Pascal Compiler (FPC)</i> All commandline options of the compiler (described in <code><a href="/docs/linux/man/1-fpc/">fpc</a></code>(1) ) can be specified in fpc.cfg When the configuration file is found, it is read, and the lines it contains are treated like you typed them on the command line see <code><a href="/docs/linux/man/1-fpc/">fpc</a></code>(1) with some extra condtional possibilities. </p>
<h2>Syntax</h2>
<p>You can specify comments in the configuration file with the # sign. Everything from the # on will be ignored, unless it is one of the keywords (see below). </p>
<p> The compiler looks for the fpc.cfg file in the following places : </p>
<p> <i>&#8211; Under Linux and unix</i><br />
 &#8211; The current directory.<br />
 &#8211; Home directory, looks for .fpc.cfg<br />
 &#8211; The directory specified in the environment<br />
 variable PPC_CONFIG_PATH, and if it&#8217;s not<br />
 set under compilerdir/../etc.<br />
 &#8211; If it is not yet found: in /etc. </p>
<p> <i>&#8211; Under all other OSes:</i><br />
 &#8211; The current directory.<br />
 &#8211; The directory specified in the environment<br />
 variable PPC_CONFIG_PATH.<br />
 &#8211; The directory where the compiler binary is. </p>
<p> When the compiler has finished reading the configuration file, it continues to treat the command line options. </p>
<p> One of the command-line options allows you to specify a second configuration file: Specifying @foo on the command line will use file foo instead of fpc.cfg and read further options from there. When the compiler has finished reading this file, it continues to process the command line. </p>
<p> The configuration file allows some kind of preprocessing. It understands the following directives, which you should place on the first column of a line : </p>
<p> #IFDEF<br />
 #IFNDEF<br />
 #ELSE<br />
 #ENDIF<br />
 #DEFINE<br />
 #UNDEF<br />
 #WRITE<br />
 #INCLUDE<br />
 #SECTION<br />
 They work the same way as their $&#8230; directive counterparts in Pascal: </p>
<dl>
<dt><i>#IFDEF</i></p>
<dd>
<dl>
<dd>
<dl>
<dt><i>Syntax</i></p>
<dd>#IFDEF name </p>
<p> Lines following #IFDEF are skipped read if the keyword &quot;name&quot; following it is not defined. </p>
<p> They are read until the keywords #ELSE or #ENDIF are encountered, after which normal processing is resumed. </p>
<dt><i>Example</i></p>
<dd>#IFDEF VER0_99_12<br />
 -Fu/usr/lib/fpc/0.99.12/rtl<br />
 #ENDIF
</dl>
<p> In the above example, /usr/lib/fpc/0.99.12/rtl will be added to the path if you&#8217;re compiling with version 0.99.12 of the compiler.</dl>
<dt><i>#IFNDEF</i></p>
<dd>
<dl>
<dd>
<dl>
<dt><i>Syntax</i></p>
<dd>#IFNDEF name </p>
<p> Lines following #IFDEF are skipped read if the keyword &quot;name&quot; following it is defined. </p>
<p> They are read until the keywords #ELSE or #ENDIF are encountered, after which normal processing is resumed. </p>
<dt><i>Example</i></p>
<dd>#IFNDEF VER0_99_12<br />
 -Fu/usr/lib/fpc/0.99.13/rtl<br />
 #ENDIF</dl>
<p> In the above example, /usr/lib/fpc/0.99.13/rtl will be added to the path if you&#8217;re NOT compiling with version 0.99.12 of the compiler.</dl>
<dt><i>#ELSE</i></p>
<dd>
<dl>
<dd>
<dl>
<dt><i>Syntax</i></p>
<dd>#ELSE </p>
<p> #ELSE can be specified after a #IFDEF or #IFNDEF directive as an alternative. Lines following #ELSE are skipped read if the preceding #IFDEF #IFNDEF was accepted. </p>
<p> They are skipped until the keyword #ENDIF is encountered, after which normal processing is resumed. </p>
<dt><i>Example</i></p>
<dd>#IFDEF VER0_99_12<br />
 -Fu/usr/lib/fpc/0.99.12/rtl<br />
 #ELSE<br />
 -Fu/usr/lib/fpc/0.99.13/rtl<br />
 #ENDIF
</dl>
<p> In the above example, /usr/lib/fpc/0.99.12/rtl will be added to the path if you&#8217;re compiling with version 0.99.12 of the compiler, otherwise /usr/lib/fpc/0.99.13/rtl will be added to the path.</dl>
<dt><i>#ENDIF</i></p>
<dd>
<dl>
<dd>
<dl>
<dt><i>Syntax</i></p>
<dd>#ENDIF</dl>
<p> #ENDIF marks the end of a block that started with #IF(N)DEF, possibly with an #ELSE between it.</dl>
<dt><i>#DEFINE</i></p>
<dd>
<dl>
<dd>
<dl>
<dt><i>Syntax</i></p>
<dd>#DEFINE name</dl>
<p> #DEFINE defines a new keyword. This has the same effect as a &quot;-dname&quot; command-line option.</dl>
<dt><i>#UNDEF</i></p>
<dd>
<dl>
<dd>
<dl>
<dt><i>Syntax</i></p>
<dd>#UNDEF name </p>
<p> #UNDEF un-defines a keyword if it existed. This has the same effect as a &quot;-uname&quot; command-line option.</dl>
</dl>
<dt><i>#WRITE</i></p>
<dd>
<dl>
<dd>
<dl>
<dt><i>Syntax</i></p>
<dd>#WRITE Message Text </p>
<p> #WRITE writes &quot;Message Text&quot; to the screen. This can be useful to display warnings if certain options are set. </p>
<dt><i>Example</i></p>
<dd>#IFDEF DEBUG<br />
 #WRITE Setting debugging ON&#8230;<br />
 -g<br />
 #ENDIF </p>
</dl>
<p> if &quot;DEBUG is defined, this will produce a line </p>
<p> Setting debugging ON&#8230; </p>
<p> and will then switch on debugging information in the compiler.</dl>
<dt><i>#INCLUDE</i></p>
<dd>
<dl>
<dd>
<dl>
<dt><i>Syntax</i></p>
<dd>#INCLUDE filename </p>
<p> #INCLUDE instructs the compiler to read the contents of &quot;filename&quot; before continuing to process options in the current file. </p>
<p> This can be useful if you want to have a particular configuration file for a project (or, under Unix like systems (such as Linux), in your home directory), but still want to have the global options that are set in a global configuration file. </p>
<dt><i>Example</i></p>
<dd>#IFDEF LINUX </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#INCLUDE&nbsp;<wbr>/etc/fpc.cfg<br />
 #ELSE </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#IFDEF GO32V2 </p>
<p>&nbsp;<wbr>#INCLUDE c:\ppinpc.cfg </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#ENDIF<br />
 #ENDIF
</dl>
<p> This will include /etc/fpc.cfg if you&#8217;re on a unix like machine (like linux), and will include c:\ppinpc.cfg on a dos machine.</dl>
<dt><i>#SECTION</i></p>
<dd>
<dl>
<dd>
<dl>
<dt><i>Syntax</i></p>
<dd>#SECTION name </p>
<p> The #SECTION directive acts as a #IFDEF directive, only it doesn&#8217;t require an #ENDIF directive. the special name COMMON always exists, i.e. lines following #SECTION COMMON are always read.</dl>
</dl>
</dl>
<h2>Example</h2>
<p>A standard block often used in (the Linux version of) fpc.cfg is -vwhin<br />
 #IFDEF VER0_99_12 </p>
<p>&nbsp;<wbr>#IFDEF FPC_LINK_STATIC </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-Fu/usr/lib/fpc/0.99.12/rtl/static </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-Fu/usr/lib/fpc/0.99.12/units/static </p>
<p>&nbsp;<wbr>#ENDIF </p>
<p>&nbsp;<wbr>#IFDEF FPC_LINK_DYNAMIC </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-Fu/usr/lib/fpc/0.99.12/rtl/shared </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-Fu/usr/lib/fpc/0.99.12/units/shared </p>
<p>&nbsp;<wbr>#ENDIF </p>
<p>&nbsp;<wbr>-Fu/usr/lib/fpc/0.99.12/rtl </p>
<p>&nbsp;<wbr>-Fu/usr/lib/fpc/0.99.12/units<br />
 #ENDIF The block is copied into the fpc.cfg file for each version you use (normally the latest release and the lastest developpers snapshot. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-fpc/">fpc</a></code>(1) </p>
