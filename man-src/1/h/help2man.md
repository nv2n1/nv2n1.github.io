---
title: "help2man(1)"
name: "help2man"
section: "1"
letter: "h"
url: "/docs/linux/man/1-help2man/"
description: "help2man – generate a simple manual page"
---

<h2>NAME</h2>
<p> help2man &#8211; generate a simple manual page</p>
<h2>SYNOPSIS</h2>
<p> <code>help2man</code> [<i>OPTION</i>]&#8230; <i>EXECUTABLE</i></p>
<h2>DESCRIPTION</h2>
<p> `help2man&#8217; generates a man page out of `&#8211;help&#8217; and `&#8211;version&#8217; output.</p>
<dl>
<dt><code>-n</code>, <code>&#8211;name</code>=<i>STRING</i></p>
<dd> description for the NAME paragraph</p>
<dt><code>-s</code>, <code>&#8211;section</code>=<i>SECTION</i></p>
<dd> section number for manual page (1, 6, 8)</p>
<dt><code>-m</code>, <code>&#8211;manual</code>=<i>TEXT</i></p>
<dd> name of manual (User Commands, &#8230;)</p>
<dt><code>-S</code>, <code>&#8211;source</code>=<i>TEXT</i></p>
<dd> source of program (FSF, Debian, &#8230;)</p>
<dt><code>-L</code>, <code>&#8211;locale</code>=<i>STRING</i></p>
<dd> select locale (default &quot;C&quot;)</p>
<dt><code>-i</code>, <code>&#8211;include</code>=<i>FILE</i></p>
<dd> include material from `FILE&#8217;</p>
<dt><code>-I</code>, <code>&#8211;opt-include</code>=<i>FILE</i></p>
<dd> include material from `FILE&#8217; if it exists</p>
<dt><code>-o</code>, <code>&#8211;output</code>=<i>FILE</i></p>
<dd> send output to `FILE&#8217;</p>
<dt><code>-p</code>, <code>&#8211;info-page</code>=<i>TEXT</i></p>
<dd> name of Texinfo manual</p>
<dt><code>-N</code>, <code>&#8211;no-info</code></p>
<dd> suppress pointer to Texinfo manual</p>
<dt><code>-l</code>, <code>&#8211;libtool</code></p>
<dd> exclude the `lt-&#8216; from the program name</p>
<dt><code>&#8211;help</code></p>
<dd> print this help, then exit</p>
<dt><code>&#8211;version</code></p>
<dd> print version number, then exit</dl>
<p> EXECUTABLE should accept `&#8211;help&#8217; and `&#8211;version&#8217; options and produce output on stdout although alternatives may be specified using:</p>
<dl>
<dt><code>-h</code>, <code>&#8211;help-option</code>=<i>STRING</i></p>
<dd> help option string</p>
<dt><code>-v</code>, <code>&#8211;version-option</code>=<i>STRING</i></p>
<dd> version option string</p>
<dt><code>&#8211;version-string</code>=<i>STRING</i></p>
<dd> version string</p>
<dt><code>&#8211;no-discard-stderr</code></p>
<dd> include stderr when parsing option output</dl>
<h2>INCLUDE FILES</h2>
<p> Additional material may be included in the generated output with the <code>&#8211;include</code> and <code>&#8211;opt-include</code> options. The format is simple: </p>
<p>&nbsp;<wbr>[section]<br />
&nbsp;<wbr>text </p>
<p>&nbsp;<wbr>/pattern/<br />
&nbsp;<wbr>text </p>
<p> Blocks of verbatim *roff text are inserted into the output either at the start of the given <code>[</code><i>section</i><code>]</code> (case insensitive), or after a paragraph matching <code>/</code><i>pattern</i><code>/</code>. </p>
<p> Patterns use the Perl regular expression syntax and may be followed by the <i>i</i>, <i>s</i> or <i>m</i> modifiers (see <code><a href="/docs/linux/man/1-perlre/">perlre</a></code>(1)). </p>
<p> Lines before the first section or pattern which begin with `-&#8216; are processed as options. Anything else is silently ignored and may be used for comments, RCS keywords and the like. </p>
<p> The section output order (for those included) is: </p>
<p>&nbsp;<wbr>NAME<br />
&nbsp;<wbr>SYNOPSIS<br />
&nbsp;<wbr>DESCRIPTION<br />
&nbsp;<wbr>OPTIONS<br />
&nbsp;<wbr>ENVIRONMENT<br />
&nbsp;<wbr>FILES<br />
&nbsp;<wbr>EXAMPLES<br />
&nbsp;<wbr><i>other</i><br />
&nbsp;<wbr>AUTHOR<br />
&nbsp;<wbr>REPORTING BUGS<br />
&nbsp;<wbr>COPYRIGHT<br />
&nbsp;<wbr>SEE ALSO </p>
<p> Any <code>[NAME]</code> or <code>[SYNOPSIS]</code> sections appearing in the include file will replace what would have automatically been produced (although you can still override the former with <code>&#8211;name</code> if required). </p>
<p> Other sections are prepended to the automatically produced output for the standard sections given above, or included at <i>other</i> (above) in the order they were encountered in the include file.</p>
<h2>AVAILABILITY</h2>
<p> The latest version of this distribution is available on-line from: </p>
<p>&nbsp;<wbr><a href="ftp://ftp.gnu.org/gnu/help2man/">ftp://ftp.gnu.org/gnu/help2man/</a></p>
<h2>AUTHOR</h2>
<p> Written by Brendan O&#8217;Dea &lt;bod [at] debian.org&gt;</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;bug-help2man [at] gnu.org&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2009, 2010, 2011, 2012 Free Software Foundation, Inc.<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>help2man</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>help2man</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info help2man</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
