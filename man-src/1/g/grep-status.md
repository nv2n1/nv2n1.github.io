---
title: "grep-status(1)"
name: "grep-status"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grep-status/"
description: "grep-dctrl, grep-status, grep-available, grep-aptavail, grep-debtags – grep Debian control files"
---

<h2 class="name">NAME</h2>
<p> grep-dctrl, grep-status, grep-available, grep-aptavail, grep-debtags &#8211; grep Debian control files </p>
<h2>SYNOPSIS</h2>
<p> <i>command</i> <code>&#8211;copying</code>|<code>-C</code> | <code>&#8211;help</code>|<code>-h</code> | <code>&#8211;version</code>|<code>-V</code> </p>
<p> <i>command</i> [<i>options</i>] <i>filter</i> [ <i>file</i>&#8230; ] </p>
<p> where <i>command</i> is one of <code>grep-dctrl</code>, <code>grep-status</code>, <code>grep-available</code>, <code>grep-aptavail </code> and <code>grep-debtags</code>.</p>
<h2>DESCRIPTION</h2>
<p> The <code>grep-dctrl</code> program can answer such questions as <i>What is the Debian package foo?</i>, <i>Which version of the Debian package bar is now current?</i>, <i>Which Debian packages does John Doe maintain?</i>, <i>Which Debian packages are somehow related to the Scheme</i> <i>programming language?</i>, and with some help, <i>Who maintain the essential packages of a Debian system?</i>, given a useful input file. </p>
<p> The programs <code>grep-available</code>, <code>grep-status</code>, <code>grep-aptavail</code> and <code>grep-debtags</code> are aliases of (actually, symbolic links to) <code>grep-dctrl</code>. These aliases use as their default input the <code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1) <i>available</i> and <i>status</i> files, the <code>apt-cache dumpavail</code> output and the <code>debtags dumpavail</code> output, respectively. </p>
<p> <code>grep-dctrl</code> is a specialised <code>grep</code> program that is meant for processing any file which has the general format of a Debian package <i>control</i> file, as described in the Debian Policy. These include the <code>dpkg</code> <i>available</i> file, the <code>dpkg</code> <i>status</i> file, and the <i>Packages</i> files on a distribution medium (such as a Debian CD-ROM or an FTP site carrying Debian). </p>
<p> You must give a <i>filter</i> expression on the command line. The <i>filter</i> defines which kind of paragraphs (aka package records) are output. A simple <i>filter</i> is a search pattern along with any options that modify it. Possible modifiers are <code>&#8211;eregex</code>, <code>&#8211;field</code>, <code>&#8211;ignore-case</code>, <code>&#8211;regex</code> and <code>&#8211;exact-match</code>, along with their single-letter equivalents. By default, the search is a case-sensitive fixed substring match on each paragraph (in other words, package record) in the input. With suitable modifiers, this can be changed: the search can be case-insensitive and the pattern can be seen as an extended POSIX regular expression. </p>
<p> <i>Filter</i>s can be combined to form more complex <i>filter</i>s using the connectives <code>&#8211;and</code>, <code>&#8211;or</code> and <code>&#8211;not</code>. Parentheses (which usually need to be escaped for the shell) can be used for grouping. </p>
<p> By default, the full matching paragraphs are printed on the standard output; specific fields can be selected for output with the <code>-s</code> option. </p>
<p> After the <i>filter</i> expression comes zero or more <i>file</i> names. The <i>file</i> name <code>&#8211;</code> is taken to mean the standard input stream. The <i>file</i>s are searched in order but separately; they are <code>not</code> concatenated together. In other words, the end of a <i>file</i> always implies the end of the current paragraph. </p>
<p> If no <i>file</i> names are specified, the program name is used to identify a default input file. The program names are matched with the base form of the name of the current program (the 0&#8217;th command line argument, if you will).</p>
<h2>OPTIONS</h2>
<h3>Specifying the search pattern</h3>
<dl>
<dt><code>&#8211;pattern=</code><i>pattern</p>
<dd> Specify a pattern</i> to be searched. This switch is not generally needed, as the <i>pattern</i> can be given by itself. However, <i>pattern</i>s that start with a dash (<code>&#8211;</code>) must be given using this switch, so that they wouldn&#8217;t be mistaken for switches.</dl>
<h3>Modifiers of simple filters</h3>
<dl>
<dt><code>-F </code><i>field</i>,<i>field</i>, &#8230; | <code>&#8211;field=</code><i>field</i>,<i>field</i>, &#8230;</p>
<dd> Restrict pattern matching to the <i>field</i>s given. Multiple <i>field</i> names in one <code>-F</code> option and multiple <code>-F</code> options in one simple <i>filter </i> are allowed. The search named by the filter will be performed among all the <i>field</i>s named, and as soon as any one of them matches, the whole simple <i>filter</i> is considered matching.</p>
<dt>
<dd> A <i>field</i> specification can contain a colon (<code>:</code>). In such a case, the part up to the colon is taken as the name of the field to be searched in, and the part after the colon is taken as the name of the field whose content is to be used if the field to search in is empty.</p>
<dt><code>-P</p>
<dd> Shorthand for -FPackage</code>.</p>
<dt><code>-S</p>
<dd> Shorthand for -FSource:Package</code>.</p>
<dt><code>-e</code>, <code>&#8211;eregex</p>
<dd> Regard the pattern of the current simple filter as an extended POSIX regular expression</p>
<dt>-r</code>, <code>&#8211;regex</p>
<dd> Regard the pattern of the current simple filter as a standard POSIX regular expression.</p>
<dt>-i</code>, <code>&#8211;ignore-case</p>
<dd> Ignore case when looking for a match in the current simple filter.</p>
<dt>-X</code>, <code>&#8211;exact-match</p>
<dd> Do an exact match (as opposed to a substring match) in the current simple filter.</p>
<dt>-w</code>, <code>&#8211;whole-pkg</p>
<dd> Do an extended regular expression match on whole package names, assuming the syntax of inter-package relationship fields such as Depends</code>,<code>Recommends</code>, &#8230; When this flag is given you should not worry about sub-package names such as &quot;libpcre3&quot; also matching &quot;libpcre3-dev&quot;. This flag implies (and is incompatible with) <code>-e</code>.</p>
<dt><code>&#8211;eq</p>
<dd> Do an equality comparison under the Debian version number system. If the pattern or the field to be searched in is not a valid Debian version number, the paragraph is regarded as not matching. As a special case, this is capable of comparing simple nonnegative integers for equality.</p>
<dt>&#8211;lt</p>
<dd> Do an strictly-less-than comparison under the Debian version number system. If the pattern or the field to be searched in is not a valid Debian version number, the paragraph is regarded as not matching. As a special case, this is capable of comparing simple nonnegative integers.</p>
<dt>&#8211;le</p>
<dd> Do an less-than-or-equal comparison under the Debian version number system. If the pattern or the field to be searched in is not a valid Debian version number, the paragraph is regarded as not matching. As a special case, this is capable of comparing simple nonnegative integers.</p>
<dt>&#8211;gt</p>
<dd> Do an strictly-greater-than comparison under the Debian version number system. If the pattern or the field to be searched in is not a valid Debian version number, the paragraph is regarded as not matching. As a special case, this is capable of comparing simple nonnegative integers.</p>
<dt>&#8211;ge</p>
<dd> Do an greater-than-or-equal comparison under the Debian version number system. If the pattern or the field to be searched in is not a valid Debian version number, the paragraph is regarded as not matching. As a special case, this is capable of comparing simple nonnegative integers.</dl>
<p> </code></p>
<h3>Combining filters</h3>
<dl>
<dt><code>-!</code>, <code>&#8211;not</code>, <code>!</p>
<dd> Match if the following filter does not</code> match.</p>
<dt><code>-o</code>, <code>&#8211;or</p>
<dd> Match if either one or both of the preceding and following filters matches.</p>
<dt>-a</code>, <code>&#8211;and</p>
<dd> Match if both the preceding and the following filter match.</p>
<dt>(</code> &#8230; <code>)</p>
<dd> Parentheses can be used for grouping. Note that they need to be escaped for most shells. Filter modifiers can be given before the opening parentheses; they will be treated as if they had been repeated for each simple filter inside the parentheses.</dl>
<p> </code></p>
<h3>Output format modifiers</h3>
<dl>
<dt><code>-l</code>, <code>&#8211;files-with-matches</p>
<dd> Output only the file names, each on its own line, of those files that contain at least one matching paragraph. This is incompatible with the -v</code> and <code>-L</code> options, and all other output format modifiers will be ignored.</p>
<dt><code>-L</code>, <code>&#8211;files-without-matches</p>
<dd> Output only the file names, each on its own line, of those files that do not contain any matching paragraphs. This is incompatible with the -v</code> and <code>-l</code> options, and all other output format modifiers will be ignored.</p>
<dt><code>-s </code><i>field</i>,<i>field</i>, &#8230; | <code>&#8211;show-field=</code><i>field</i>,<i>field</i>, &#8230;</p>
<dd> Show only the body of these <i>field</i>s from the matching paragraphs. The <i>field</i> names must not include any colons or commas. Commas are used to delimit <i>field</i> names in the argument to this option. The <i>field</i>s are shown in the order given here. See also the option <code>-I</code>. Note that in the absence of the <code>&#8211;ensure&#8211;dctrl</code> option, if only one field is selected, no paragraph separator is output.</p>
<dt><code>-I</code>, <code>&#8211;invert-show</p>
<dd> Invert the meaning of option -s</code>: show only the fields that have <code>not</code> been named using a <code>-s</code> option. As an artefact of the implementation, the order of the fields in the original paragraph is not preserved.</dl>
<p> A <i>field</i> specification can contain a colon. In such a case, the part up to the colon is taken as the name of the field to be shown, and the part after the colon is taken as the name of the field whose content is to be used if the field to be shown is empty.</p>
<dl>
<dt><code>-d</p>
<dd> Show only the first line of the Description</code> field from the matching paragraphs. If no <code>-s</code> option is specified, this option also effects <code>-s Description;</code> if there is a <code>-s</code> option but it does not include the <code>Description</code> field name, one is appended to the option. Thus the <code>Description</code> field&#8217;s location in the output is determined by the <code>-s</code> option, if any, the last field being the default.</p>
<dt><code>-n</code>, <code>&#8211;no-field-names</p>
<dd> Suppress field names when showing specified fields, only their bodies are shown. Each field is printed in its original form without the field name, the colon after it and any whitespace preceding the start of the body.</p>
<dt>-v</code>, <code>&#8211;invert-match</p>
<dd> Instead of showing all the paragraphs that match, show those paragraphs that do not</code> match.</p>
<dt><code>-c</code>, <code>&#8211;count</p>
<dd> Instead of showing the paragraphs that match (or, with -v</code>, that don&#8217;t match), show the count of those paragraphs.</p>
<dt><code>-q</code>, <code>&#8211;quiet</code>, <code>&#8211;silent</p>
<dd> Output nothing to the standard output stream. Instead, exit immediately after finding the first match.</dl>
<p> </code></p>
<h3>Miscellaneous</h3>
<dl>
<dt><code>&#8211;ensure-dctrl</p>
<dd> Ensure that the output is in dctrl format, specifically that there always is an empty line separating paragraphs. This option is not honored if the -n</code> option has been selected, as that option deliberately requests a non-dctrl format for the output. In a future version, this option may be made the default behaviour.</p>
<dt><code>&#8211;compat</p>
<dd> Override any &#8211;ensure-dctrl</code> option given earlier on the command line.</p>
<dt><code>&#8211;ignore-parse-errors</p>
<dd> Ignore errors in parsing input. A paragraph which cannot be parsed is ignored in its entirety, and the next paragraph is assumed to start after the first newline since the location of the error.</p>
<dt>&#8211;debug-optparse</p>
<dd> Show how the current command line has been parsed.</p>
<dt>&#8211;errorlevel=</code><i>level</p>
<dd> Set log level to level</i>. <i>level</i> is one of <code>fatal</code>, <code>important</code>, <code>informational</code> and <code>debug</code>, but the last may not be available, depending on the compile-time options. These categories are given here in order; every message that is emitted when <code>fatal</code> is in effect, will be emitted in the <code>important</code> error level, and so on. The default is <code>important</code>.</p>
<dt><code>-V</code>, <code>&#8211;version</p>
<dd> Print out version information.</p>
<dt>-C</code>, <code>&#8211;copying</p>
<dd> Print out the copyright license. This produces much output; be sure to redirect or pipe it somewhere (such as your favourite pager).</p>
<dt>-h</code>, <code>&#8211;help</p>
<dd> Print out a help summary.</dl>
<p> </code></p>
<h2>EXAMPLES</h2>
<p> The almost simplest use of this program is to print out the status or available record of a package. In this respect, <code>grep-dctrl</code> is like <code>dpkg -s</code> or <code>dpkg &#8211;print-avail.</code> To print out the status record of the package &quot;mixal&quot;, do </p>
<pre>
% grep-status -PX mixal
</pre>
<p> and to get its available record, use </p>
<pre>
% grep-available -PX mixal
</pre>
<p> In fact, you can ask for the record of the &quot;mixal&quot; package from any Debian control file. Say, you have the Debian 6.0 CD-ROM&#8217;s <i>Packages</i> file in the current directory; now you can do a </p>
<pre>
% grep-dctrl -PX mixal Packages
</pre>
<p> But <code>grep-dctrl</code> can do more than just emulate <code>dpkg</code>. It can more-or-less emulate <code>apt-cache</code>! That program has a search feature that searches package descriptions. But we can do that too: </p>
<pre>
% grep-available -F Description foo
</pre>
<p> searches for the string &quot;foo&quot; case-sensitively in the descriptions of all available packages. If you want case-insensitivity, use </p>
<pre>
% grep-available -F Description -i foo
</pre>
<p> Truth to be told, <code>apt-cache</code> searches package names, too. We can separately search in the names; to do so, do </p>
<pre>
% grep-available -F Package foo
</pre>
<p> or </p>
<pre>
% grep-available -P foo
</pre>
<p> which is pretty much the same thing. We can also search in both descriptions and names; if match is found in either, the package record is printed: </p>
<pre>
% grep-available -P -F Description foo
</pre>
<p> or </p>
<pre>
% grep-available -F Package -F Description foo
</pre>
<p> This kind of search is the exactly same that <code>apt-cache</code> does. </p>
<p> Here&#8217;s one thing neither <code>dpkg</code> nor <code>apt-cache</code> do. Search for a string in the whole <i>status</i> or <i>available</i> file (or any Debian control file, for that matter) and print out all package records where we have a match. Try </p>
<pre>
% grep-available dpkg
</pre>
<p> sometime and watch how thoroughly <code>dpkg</code> has infiltrated Debian. </p>
<p> All the above queries were based on simple substring searches. But <code>grep-dctrl</code> can handle regular expressions in the search pattern. For example, to see the status records of all packages with either &quot;apt&quot; or &quot;dpkg&quot; in their names, use </p>
<pre>
% grep-status -P -e 'apt|dpkg'
</pre>
<p> Now that we have seen all these fine and dandy queries, you might begin to wonder whether it is necessary to always see the whole paragraph. You may be, for example, interest only in the dependency information of the packages involved. Fine. To show the depends lines of all packages maintained by me, do a </p>
<pre>
% grep-available -F Maintainer -s Depends 'ajk [at] debian.org'
</pre>
<p> If you want to see the packages&#8217; names, too, use </p>
<pre>
% grep-available -F Maintainer -s Package,Depends \
  'ajk [at] debian.org'
</pre>
<p> Note that there must be no spaces in the argument to the <code>-s</code> switch. </p>
<p> More complex queries are also possible. For example, to see the list of packages maintained by me and depending on libc6, do </p>
<pre>
% grep-available -F Maintainer 'ajk [at] debian.org' \
   -a -F Depends libc6 -s Package,Depends
</pre>
<p> Remember that you can use other UNIX filters to help you, too. Ever wondered, who&#8217;s the most active Debian developer based on the number of source packages being maintained? Easy. You just need to have a copy of the most recent <i>Sources</i> file from any Debian mirror. </p>
<pre>
% grep-dctrl -n -s Maintainer '' Sources | sort | \
  uniq -c | sort -nr
</pre>
<p> This example shows a neat trick: if you want to selectively show only some field of <i>all</i> packages, just supply an empty pattern. </p>
<p> The term &quot;bogopackage&quot; means the count of the packages that a Debian developer maintains. To get the bogopackage count for the maintainer of <code>dctrl-tools</code>, say </p>
<pre>
% grep-available -c -FMaintainer \
  &quot;`grep-available -sMaintainer -n -PX dctrl-tools`&quot;
</pre>
<p> Sometimes it is useful to output the data of several fields on the same line. For example, the following command outputs the list of installed packages, sorted by their <code>Installed-Size</code>. </p>
<pre>
% grep-status -FStatus -sInstalled-Size,Package -n \
  &quot;install ok installed&quot; -a -FInstalled-Size --gt 0 \
  | paste -sd &quot;  
&quot; | sort -n
</pre>
<p> Note that there should be exactly 2 spaces in the &quot; 
&quot; string. </p>
<p> Another usual use-case is looking for packages that have another one as build dependency: </p>
<pre>
% grep-dctrl -s Package -F Build-Depends,Build-Depends-Indep \
  quilt /var/lib/apt/lists/*Sources
</pre>
<p> These examples cover a lot of typical uses of this utility, but not all possible uses. Use your imagination! The building blocks are there, and if something&#8217;s missing, let me know.</p>
<h2>DIAGNOSTICS</h2>
<p> In the absence of errors, the exit code <code>0</code> is used if at least one match was found, and the exit code <code>1</code> is used if no matches were found. If there were errors, the exit code is <code>2</code>, with one exception. If the <code>-q</code>, <code>&#8211;quiet</code> or <code>&#8211;silent</code> options are used, the exit code <code>0</code> is used when a match is found regardless of whether there have been non-fatal errors. </p>
<p> These messages are emitted in log levels <code>fatal</code> and <code>important</code>. Additional messages may be provided by the system libraries. <code>This list is incomplete.</code></p>
<dl>
<dt><code>A pattern is mandatory</p>
<dd> You must specify a pattern to be searched for.</p>
<dt>malformed filter</p>
<dd> No filter was specified, but one is required.</p>
<dt>cannot find enough memory</p>
<dd> More memory was needed than was available. This error may be transient, that is, if you try again, all may go well.</p>
<dt>cannot suppress field names when showing whole paragraphs</p>
<dd> When you do not use the -s</code> switch, <code>grep-dctrl</code> just passes the matching paragraphs through, not touching them any way. This means, for example, that you can only use <code>-n</code> when you use <code>-s</code>.</p>
<dt><code>inconsistent modifiers of simple filters</p>
<dd> Conflicting modifiers of simple filters were used; for example, perhaps both -X</code> and <code>-e</code> were specified for the same simple filter.</p>
<dt><code>missing &#8216;)&#8217; in command line</p>
<dd> There were more opening than closing parentheses in the given filter.</p>
<dt>no such log level</p>
<dd> The argument to &#8211;errorlevel</code> was invalid.</p>
<dt><code>too many file names</p>
<dd> The number of file names specified in the command line exceeded a compile-time limit.</p>
<dt>too many output fields</p>
<dd> The argument to -s</code> had too many field names in it. This number is limited to 256.</p>
<dt><code>unexpected &#8216;)&#8217; in command line</p>
<dd> There was no opening parenthesis that would match some closing parenthesis in the command line.</dl>
<p> </code></p>
<h2>FILES</h2>
<dl>
<dt><i>/var/lib/dpkg/available</p>
<dd> The default input file of </i><code>grep-available</code>.</p>
<dt><i>/var/lib/dpkg/status</p>
<dd> The default input file of </i><code>grep-status</code>.</dl>
<h2>AUTHOR</h2>
<p> The program and this manual page were written by Antti-Juhani Kaijanaho &lt;<i>gaia [at] iki.fi</i>&gt;. Bill Allombert &lt;<i>ballombe [at] debian.org</i>&gt; provided one of the examples in the manual page.</p>
<h2>SEE ALSO</h2>
<p> Debian Policy Manual. Published as the Debian package <code>debian-policy</code>. Also available in the Debian website. </p>
<p> <code><a href="/docs/linux/man/1-apt-cache/">apt-cache</a></code>(1), <code><a href="/docs/linux/man/1-ara/">ara</a></code>(1), <code><a href="/docs/linux/man/1-dpkg-awk/">dpkg-awk</a></code>(1), <code><a href="/docs/linux/man/1-sgrep/">sgrep</a></code>(1), <code><a href="/docs/linux/man/8-dpkg/">dpkg</a></code>(8) </p>
<h2>Index</h2>
