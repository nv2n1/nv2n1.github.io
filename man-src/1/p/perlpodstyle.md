---
title: "perlpodstyle(1)"
name: "perlpodstyle"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlpodstyle/"
---

<h2 class="name">NAME</h2>
 

 perlpodstyle - Perl POD style guide 

<h2>DESCRIPTION</h2>

 These are general guidelines for how to write <font SIZE="-1">POD</font> documentation for Perl scripts and modules, based on general guidelines for writing good <font SIZE="-1">UNIX</font> man pages. All of these guidelines are, of course, optional, but following them will make your documentation more consistent with other documentation on the system. 

 The name of the program being documented is conventionally written in bold (using B&lt;&gt;) wherever it occurs, as are all program options. Arguments should be written in italics (I&lt;&gt;). Function names are traditionally written in italics; if you write a function as <b>function()</b>, Pod::Man will take care of this for you. Literal code or commands should be in C&lt;&gt;. References to other man pages should be in the form <tt>&quot;manpage(section)&quot;</tt> or <tt>&quot;L&lt;manpage(section)&gt;&quot;</tt>, and Pod::Man will automatically format those appropriately. The second form, with L&lt;&gt;, is used to request that a <font SIZE="-1">POD</font> formatter make a link to the man page if possible. As an exception, one normally omits the section when referring to module documentation since it's not clear what section module documentation will be in; use <tt>&quot;L&lt;Module::Name&gt;&quot;</tt> for module references instead. 

 References to other programs or functions are normally in the form of man page references so that cross-referencing tools can provide the user with links and the like. It's possible to overdo this, though, so be careful not to clutter your documentation with too much markup. References to other programs that are not given as man page references should be enclosed in B&lt;&gt;. 

 The major headers should be set out using a <tt>&quot;=head1&quot;</tt> directive, and are historically written in the rather startling <font SIZE="-1">ALL UPPER CASE</font> format; this is not mandatory, but it's strongly recommended so that sections have consistent naming across different software packages. Minor headers may be included using <tt>&quot;=head2&quot;</tt>, and are typically in mixed case. 

 The standard sections of a manual page are:
<dl>
<dt><font SIZE="-1">NAME</font>
<dd> Mandatory section; should be a comma-separated list of programs or functions documented by this <font SIZE="-1">POD</font> page, such as: 

 <pre>
    foo, bar - programs to do something
</pre> 

 Manual page indexers are often extremely picky about the format of this section, so don't put anything in it except this line. Every program or function documented by this <font SIZE="-1">POD</font> page should be listed, separated by a comma and a space. For a Perl module, just give the module name. A single dash, and only a single dash, should separate the list of programs or functions from the description. Do not use any markup such as C&lt;&gt; or B&lt;&gt; anywhere in this line. Functions should not be qualified with <tt>&quot;()&quot;</tt> or the like. The description should ideally fit on a single line, even if a man program replaces the dash with a few tabs.
<dt><font SIZE="-1">SYNOPSIS</font>
<dd> A short usage summary for programs and functions. This section is mandatory for section 3 pages. For Perl module documentation, it's usually convenient to have the contents of this section be a verbatim block showing some (brief) examples of typical ways the module is used.
<dt><font SIZE="-1">DESCRIPTION</font>
<dd> Extended description and discussion of the program or functions, or the body of the documentation for man pages that document something else. If particularly long, it's a good idea to break this up into subsections <tt>&quot;=head2&quot;</tt> directives like: 

 <pre>
    =head2 Normal Usage
    =head2 Advanced Features
    =head2 Writing Configuration Files
</pre> 

 or whatever is appropriate for your documentation. 

 For a module, this is generally where the documentation of the interfaces provided by the module goes, usually in the form of a list with an <tt>&quot;=item&quot;</tt> for each interface. Depending on how many interfaces there are, you may want to put that documentation in separate <font SIZE="-1">METHODS, FUNCTIONS, CLASS METHODS,</font> or <font SIZE="-1">INSTANCE METHODS</font> sections instead and save the <font SIZE="-1">DESCRIPTION</font> section for an overview.
<dt><font SIZE="-1">OPTIONS</font>
<dd> Detailed description of each of the command-line options taken by the program. This should be separate from the description for the use of parsers like Pod::Usage. This is normally presented as a list, with each option as a separate <tt>&quot;=item&quot;</tt>. The specific option string should be enclosed in B&lt;&gt;. Any values that the option takes should be enclosed in I&lt;&gt;. For example, the section for the option <b>--section</b>=<i>manext</i> would be introduced with: 

 <pre>
    =item B&lt;--section&gt;=I&lt;manext&gt;
</pre> 

 Synonymous options (like both the short and long forms) are separated by a comma and a space on the same <tt>&quot;=item&quot;</tt> line, or optionally listed as their own item with a reference to the canonical name. For example, since <b>--section</b> can also be written as <b>-s</b>, the above would be: 

 <pre>
    =item B&lt;-s&gt; I&lt;manext&gt;, B&lt;--section&gt;=I&lt;manext&gt;
</pre> 

 Writing the short option first is recommended because it's easier to read. The long option is long enough to draw the eye to it anyway and the short option can otherwise get lost in visual noise.
<dt><font SIZE="-1">RETURN VALUE</font>
<dd> What the program or function returns, if successful. This section can be omitted for programs whose precise exit codes aren't important, provided they return 0 on success and non-zero on failure as is standard. It should always be present for functions. For modules, it may be useful to summarize return values from the module interface here, or it may be more useful to discuss return values separately in the documentation of each function or method the module provides.
<dt><font SIZE="-1">ERRORS</font>
<dd> Exceptions, error return codes, exit statuses, and errno settings. Typically used for function or module documentation; program documentation uses <font SIZE="-1">DIAGNOSTICS</font> instead. The general rule of thumb is that errors printed to <tt>&quot;STDOUT&quot;</tt> or <tt>&quot;STDERR&quot;</tt> and intended for the end user are documented in <font SIZE="-1">DIAGNOSTICS</font> while errors passed internal to the calling program and intended for other programmers are documented in <font SIZE="-1">ERRORS.</font> When documenting a function that sets errno, a full list of the possible errno values should be given here.
<dt><font SIZE="-1">DIAGNOSTICS</font>
<dd> All possible messages the program can print out and what they mean. You may wish to follow the same documentation style as the Perl documentation; see <b><a HREF="/docs/linux/man/1-perldiag/">perldiag</a></b>(1) for more details (and look at the <font SIZE="-1">POD</font> source as well). 

 If applicable, please include details on what the user should do to correct the error; documenting an error as indicating ``the input buffer is too small'' without telling the user how to increase the size of the input buffer (or at least telling them that it isn't possible) aren't very useful.
<dt><font SIZE="-1">EXAMPLES</font>
<dd> Give some example uses of the program or function. Don't skimp; users often find this the most useful part of the documentation. The examples are generally given as verbatim paragraphs. 

 Don't just present an example without explaining what it does. Adding a short paragraph saying what the example will do can increase the value of the example immensely.
<dt><font SIZE="-1">ENVIRONMENT</font>
<dd> Environment variables that the program cares about, normally presented as a list using <tt>&quot;=over&quot;</tt>, <tt>&quot;=item&quot;</tt>, and <tt>&quot;=back&quot;</tt>. For example: 

 <pre>
    =over 6
    =item HOME
    Used to determine the user's home directory.  F&lt;.foorc&gt; in this
    directory is read for configuration details, if it exists.
    =back
</pre> 

 Since environment variables are normally in all uppercase, no additional special formatting is generally needed; they're glaring enough as it is.
<dt><font SIZE="-1">FILES</font>
<dd> All files used by the program or function, normally presented as a list, and what it uses them for. File names should be enclosed in F&lt;&gt;. It's particularly important to document files that will be potentially modified.
<dt><font SIZE="-1">CAVEATS</font>
<dd> Things to take special care with, sometimes called <font SIZE="-1">WARNINGS.</font>
<dt><font SIZE="-1">BUGS</font>
<dd> Things that are broken or just don't work quite right.
<dt><font SIZE="-1">RESTRICTIONS</font>
<dd> Bugs you don't plan to fix. :-)
<dt><font SIZE="-1">NOTES</font>
<dd> Miscellaneous commentary.
<dt><font SIZE="-1">AUTHOR</font>
<dd> Who wrote it (use <font SIZE="-1">AUTHORS</font> for multiple people). It's a good idea to include your current e-mail address (or some e-mail address to which bug reports should be sent) or some other contact information so that users have a way of contacting you. Remember that program documentation tends to roam the wild for far longer than you expect and pick a contact method that's likely to last.
<dt><font SIZE="-1">HISTORY</font>
<dd> Programs derived from other sources sometimes have this. Some people keep a modification log here, but that usually gets long and is normally better maintained in a separate file.
<dt><font SIZE="-1">COPYRIGHT AND LICENSE</font>
<dd> For copyright 

 <pre>
    Copyright YEAR(s) YOUR NAME(s)
</pre> 

 (No, (C) is not needed. No, ``all rights reserved'' is not needed.) 

 For licensing the easiest way is to use the same licensing as Perl itself: 

 <pre>
    This library is free software; you may redistribute it and/or
    modify it under the same terms as Perl itself.
</pre> 

 This makes it easy for people to use your module with Perl. Note that this licensing example is neither an endorsement or a requirement, you are of course free to choose any licensing.
<dt><font SIZE="-1">SEE ALSO</font>
<dd> Other man pages to check out, like <b><a HREF="/docs/linux/man/1-man/">man</a></b>(1), <b><a HREF="/docs/linux/man/7-man/">man</a></b>(7), <b><a HREF="/docs/linux/man/8-makewhatis/">makewhatis</a></b>(8), or <b><a HREF="/docs/linux/man/8-catman/">catman</a></b>(8). Normally a simple list of man pages separated by commas, or a paragraph giving the name of a reference work. Man page references, if they use the standard <tt>&quot;name(section)&quot;</tt> form, don't have to be enclosed in L&lt;&gt; (although it's recommended), but other things in this section probably should be when appropriate. 

 If the package has a mailing list, include a <font SIZE="-1">URL</font> or subscription instructions here. 

 If the package has a web site, include a <font SIZE="-1">URL</font> here.</dl>
 

 Documentation of object-oriented libraries or modules may want to use <font SIZE="-1">CONSTRUCTORS</font> and <font SIZE="-1">METHODS</font> sections, or <font SIZE="-1">CLASS METHODS</font> and <font SIZE="-1">INSTANCE METHODS</font> sections, for detailed documentation of the parts of the library and save the <font SIZE="-1">DESCRIPTION</font> section for an overview. Large modules with a function interface may want to use <font SIZE="-1">FUNCTIONS</font> for similar reasons. Some people use <font SIZE="-1">OVERVIEW</font> to summarize the description if it's quite long. 

 Section ordering varies, although <font SIZE="-1">NAME</font> must always be the first section (you'll break some man page systems otherwise), and <font SIZE="-1">NAME, SYNOPSIS, DESCRIPTION,</font> and <font SIZE="-1">OPTIONS</font> generally always occur first and in that order if present. In general, <font SIZE="-1">SEE ALSO, AUTHOR,</font> and similar material should be left for last. Some systems also move <font SIZE="-1">WARNINGS</font> and <font SIZE="-1">NOTES</font> to last. The order given above should be reasonable for most purposes. 

 Some systems use <font SIZE="-1">CONFORMING TO</font> to note conformance to relevant standards and MT-LEVEL to note safeness for use in threaded programs or signal handlers. These headings are primarily useful when documenting parts of a C library. 

 Finally, as a general note, try not to use an excessive amount of markup. As documented here and in Pod::Man, you can safely leave Perl variables, function names, man page references, and the like unadorned by markup and the <font SIZE="-1">POD</font> translators will figure it out for you. This makes it much easier to later edit the documentation. Note that many existing translators will do the wrong thing with e-mail addresses when wrapped in L&lt;&gt;, so don't do that.

<h2>AUTHOR</h2>

 Russ Allbery &lt;rra [at] cpan.org&gt;, with large portions of this documentation taken from the documentation of the original <b>pod2man</b> implementation by Larry Wall and Tom Christiansen.

<h2>COPYRIGHT AND LICENSE</h2>

 Copyright 1999, 2000, 2001, 2004, 2006, 2008, 2010, 2015, 2018 Russ Allbery &lt;rra [at] cpan.org&gt; 

 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved. This file is offered as-is, without any warranty. 

 SPDX-License-Identifier: <font SIZE="-1">FSFAP</font>

<h2>SEE ALSO</h2>

 For additional information that may be more accurate for your specific system, see either <b><a HREF="/docs/linux/man/5-man/">man</a></b>(5) or <b><a HREF="/docs/linux/man/7-man/">man</a></b>(7) depending on your system manual section numbering conventions. 

 This documentation is maintained as part of the podlators distribution. The current version is always available from its web site at &lt;<a rel="nofollow" HREF="https://www.eyrie.org/~eagle/software/podlators/">https://www.eyrie.org/~eagle/software/podlators/</a>&gt;. 

<h2>Index</h2>


