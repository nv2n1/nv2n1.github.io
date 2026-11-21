---

title: "maketext(1)"
name: "maketext"
section: "1"
letter: "m"
url: "/docs/linux/man/1-maketext/"
---

maketext - translate and make messages 

<h2>SYNOPSIS</h2>

 <pre><code>
maketext[OPTION][--domain = TEXTDOMAIN] MSGKEY[PARAM...] maketext[OPTION] - s MSGID[PARAM...]
</code></pre>

<h2>DESCRIPTION</h2>

 The <tt>&quot;maketext&quot;</tt> script translates a natural language message into the user's language, by looking up the translation in a message <font SIZE="-1">MO</font> file, and process the plural transformation with Maketext. 

 The <tt>&quot;maketext&quot;</tt> script is a command-line interface to <i>Locale::Maketext::Gettext</i>(3) (and <i>Locale::Maketext</i>(3)). It can be used in shell scripts, etc, to translate, maketext and return the result. By this way, it enables Maketext to be integrated into other programming languages/systems, like bash/csh, python, <font SIZE="-1">PHP, C,</font> etc. It works like the command-line program gettext. 

 For example: 

 <pre><code>
% maketext - s "[*,_1,virus was,viruses were] found in [*,_2,file,files]." 0 1 0 viruses were found in 1 file.% maketext - s "[*,_1,virus was,viruses were] found in [*,_2,file,files]." 1 3 1 virus was found in 3 files.%
</code></pre>

<h2>OPTIONS</h2>

<dl>
<dt>-d,--domain=TEXTDOMAIN
</dt><dd> Retrieve translated messages from <font SIZE="-1">TEXTDOMAIN.</font>
</dd><dt>-s
</dt><dd> Adds a new line to the end of the output so that it behaves like the `echo' or the `gettext' command.
</dd><dt>-h,--help
</dt><dd> Display the help messages.
</dd><dt>-V,--version
</dt><dd> Display version information and exit.
</dd><dt><font SIZE="-1">MSGKEY</font>
</dt><dd> The original text used to look up translated text.
</dd><dt><font SIZE="-1">PARAM...</font>
</dt><dd> Parameters to Maketext for the plural and other text functions.</dd></dl>

<h2>ENVIRONMENT</h2>

<dl>
<dt><font SIZE="-1">TEXTDOMAIN</font>
</dt><dd> <font SIZE="-1">TEXTDOMAIN</font> is used to determine the text domain when the -d parameter is not given.
</dd><dt><font SIZE="-1">TEXTDOMAINDIR</font>
</dt><dd> <font SIZE="-1">TEXTDOMAINDIR</font> is used to search the message catelog/MO file if it does not reside in the system locale directories.</dd></dl>

<h2>NOTES</h2>

 Maketext language function override, like <tt>&quot;quant&quot;</tt> or <tt>&quot;numerate&quot;</tt>, is not available here. Suggestions are welcome. 

 The current system locale directory search order is: /usr/share/locale, /usr/lib/locale, /usr/local/share/locale, /usr/local/lib/locale. Suggestions are welcome.

<h2>BUGS</h2>

 Report bugs to imacat &lt;imacat [at] mail.imacat.idv.tw&gt;

<h2>SEE ALSO</h2>

 <i>Locale::Maketext</i>(3), <i>Locale::Maketext::TPJ13</i>(3), <i>Locale::Maketext::Gettext</i>(3), <i>Locale::Maketext::Gettext::Functions</i>(3), <i><a HREF="/docs/linux/man/3-bindtextdomain/">bindtextdomain</a></i>(3), <i><a HREF="/docs/linux/man/3-textdomain/">textdomain</a></i>(3). Also, please refer to the official <font SIZE="-1">GNU</font> gettext manual at &lt;<a rel="nofollow" HREF="http://www.gnu.org/software/gettext/manual/">http://www.gnu.org/software/gettext/manual/</a>&gt;.

<h2>AUTHOR</h2>

 imacat &lt;imacat [at] mail.imacat.idv.tw&gt;

<h2>COPYRIGHT</h2>

 Copyright (c) 2003-2007 imacat. All rights reserved. This program is free software; you can redistribute it and/or modify it under the same terms as Perl itself.
