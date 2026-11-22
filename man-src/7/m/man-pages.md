---
title: "man-pages(7)"
name: "man-pages"
section: "7"
letter: "m"
url: "/docs/linux/man/7-man-pages/"
description: "man-pages – conventions for writing Linux man pages"
---

<p>man-pages &#8211; conventions for writing Linux man pages</p>
<h2>Synopsis</h2>
<p><code>man</code> [<i>section</i>] <i>title</i></p>
<h2>Description</h2>
<p>This page describes the conventions that should be employed when writing man pages for the Linux <i>man-pages</i> project, which documents the user-space API provided by the Linux kernel and the GNU C library. The project thus provides most of the pages in Section 2, many of the pages that appear in Sections 3, 4, and 7, and a few of the pages that appear in Sections 1, 5, and 8 of the man pages on a Linux system. The conventions described on this page may also be useful for authors writing man pages for other projects.</p>
<h3>Sections of the manual pages</h3>
<p>The manual Sections are traditionally defined as follows:</p>
<dl>
<dt><code>1 User commands (Programs)</code></dt>
<dd>Commands that can be executed by the user from within a shell.</dd>
<dt><code>2 System calls</code></dt>
<dd>Functions which wrap operations performed by the kernel.</dd>
<dt><code>3 Library calls</code></dt>
<dd>All library functions excluding the system call wrappers (Most of the <i>libc</i> functions).</dd>
<dt><code>4 Special files (devices)</code></dt>
<dd>Files found in <i>/dev</i> which allow to access to devices through the kernel.</dd>
<dt><code>5 File formats and configuration files</code></dt>
<dd>Describes various human-readable file formats and configuration files.</dd>
<dt><code>6 Games</code></dt>
<dd>Games and funny little programs available on the system.</dd>
<dt><code>7 Overview, conventions, and miscellaneous</code></dt>
<dd>Overviews or descriptions of various topics, conventions and protocols, character set standards, the standard filesystem layout, and miscellaneous other things.</dd>
<dt><code>8 System management commands</code></dt>
<dd>Commands like <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8), many of which only root can execute.</dd></dl>
<h3>Macro package</h3>
<p>New manual pages should be marked up using the <code>groff an.tmac</code> package described in <code><a href="/docs/linux/man/7-man/">man</a></code>(7). This choice is mainly for consistency: the vast majority of existing Linux manual pages are marked up using these macros.</p>
<h3>Conventions for source file layout</h3>
<p>Please limit source code line length to no more than about 75 characters wherever possible. This helps avoid line-wrapping in some mail clients when patches are submitted inline.</p>
<h3>Title line</h3>
<p>The first command in a man page should be a <code>TH</code> command: </p>
<dl>
<dd><code>.TH</code> <i>title section date source manual</i></dd></dl>
<p> The arguments of the command are as follows:</p>
<dl>
<dt><i>title</i></dt>
<dd>The title of the man page, written in all caps (e.g., <i>MAN-PAGES</i>).</dd>
<dt><i>section</i></dt>
<dd>The section number in which the man page should be placed (e.g., <i>7</i>).</dd>
<dt><i>date</i></dt>
<dd>The date of the last nontrivial change that was made to the man page. (Within the <i>man-pages</i> project, the necessary updates to these timestamps are handled automatically by scripts, so there is no need to manually update them as part of a patch.) Dates should be written in the form YYYY-MM-DD.</dd>
<dt><i>source</i></dt>
<dd>The source of the command, function, or system call.</dd>
<dd>For those few <i>man-pages</i> pages in Sections 1 and 8, probably you just want to write <i>GNU</i>.</dd>
<dd>For system calls, just write <i>Linux</i>. (An earlier practice was to write the version number of the kernel from which the manual page was being written/checked. However, this was never done consistently, and so was probably worse than including no version number. Henceforth, avoid including a version number.)</dd>
<dd>For library calls that are part of glibc or one of the other common GNU libraries, just use <i>GNU C Library</i>, <i>GNU</i>, or an empty string.</dd>
<dd>For Section 4 pages, use <i>Linux</i>.</dd>
<dd>In cases of doubt, just write <i>Linux</i>, or <i>GNU</i>.</dd>
<dt><i>manual</i></dt>
<dd>The title of the manual (e.g., for Section 2 and 3 pages in the <i>man-pages</i> package, use <i>Linux Programmer&#8217;s Manual</i>).</dd></dl>
<h3>Sections within a manual page</h3>
<p>The list below shows conventional or suggested sections. Most manual pages should include at least the <code>highlighted</code> sections. Arrange a new manual page so that sections are placed in the order shown in the list. </p>
<dl>
<dd>
<table>
<tr VALIGN=top>
<td><code>NAME</code></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>SYNOPSIS</code></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>CONFIGURATION</td>
<td>[Normally only in Section 4]
</td>
</tr>
<tr VALIGN=top>
<td><code>DESCRIPTION</code></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>OPTIONS</td>
<td>[Normally only in Sections 1, 8]
</td>
</tr>
<tr VALIGN=top>
<td>EXIT STATUS</td>
<td>[Normally only in Sections 1, 8]
</td>
</tr>
<tr VALIGN=top>
<td>RETURN VALUE</td>
<td>[Normally only in Sections 2, 3]
</td>
</tr>
<tr VALIGN=top>
<td>ERRORS</td>
<td>[Typically only in Sections 2, 3]
</td>
</tr>
<tr VALIGN=top>
<td>ENVIRONMENT</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>FILES</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>VERSIONS</td>
<td>[Normally only in Sections 2, 3]
</td>
</tr>
<tr VALIGN=top>
<td>ATTRIBUTES</td>
<td>[Normally only in Sections 2, 3]
</td>
</tr>
<tr VALIGN=top>
<td>CONFORMING TO</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>NOTES</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>BUGS</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>EXAMPLES</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>AUTHORS</td>
<td>[Discouraged]
</td>
</tr>
<tr VALIGN=top>
<td>REPORTING BUGS</td>
<td>[Not used in man-pages]
</td>
</tr>
<tr VALIGN=top>
<td>COPYRIGHT</td>
<td>[Not used in man-pages]
</td>
</tr>
<tr VALIGN=top>
<td><code>SEE ALSO</code></td>
<td>
</td>
</tr>
</table>
</dd></dl>
<p> <i>Where a traditional heading would apply</i>, <i>please use it</i>; this kind of consistency can make the information easier to understand. If you must, you can create your own headings if they make things easier to understand (this can be especially useful for pages in Sections 4 and 5). However, before doing this, consider whether you could use the traditional headings, with some subsections (<i>.SS</i>) within those sections. </p>
<p> The following list elaborates on the contents of each of the above sections.</p>
<dl>
<dt><code>NAME</code></dt>
<dd>The name of this manual page.</dd>
<dd>See <code><a href="/docs/linux/man/7-man/">man</a></code>(7) for important details of the line(s) that should follow the <code>.SH NAME</code> command. All words in this line (including the word immediately following the &quot;\-&quot;) should be in lowercase, except where English or technical terminological convention dictates otherwise.</dd>
<dt><code>SYNOPSIS</code></dt>
<dd>A brief summary of the command or function&#8217;s interface.</dd>
<dd>For commands, this shows the syntax of the command and its arguments (including options); boldface is used for as-is text and italics are used to indicate replaceable arguments. Brackets ([]) surround optional arguments, vertical bars (|) separate choices, and ellipses (&#8230;) can be repeated. For functions, it shows any required data declarations or <code>#include</code> directives, followed by the function declaration.</dd>
<dd>Where a feature test macro must be defined in order to obtain the declaration of a function (or a variable) from a header file, then the SYNOPSIS should indicate this, as described in <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7).</dd>
<dt><code>CONFIGURATION</code></dt>
<dd>Configuration details for a device.</dd>
<dd>This section normally appears only in Section 4 pages.</dd>
<dt><code>DESCRIPTION</code></dt>
<dd>An explanation of what the program, function, or format does.</dd>
<dd>Discuss how it interacts with files and standard input, and what it produces on standard output or standard error. Omit internals and implementation details unless they&#8217;re critical for understanding the interface. Describe the usual case; for information on command-line options of a program use the <code>OPTIONS</code> section.</dd>
<dd>When describing new behavior or new flags for a system call or library function, be careful to note the kernel or C library version that introduced the change. The preferred method of noting this information for flags is as part of a <code>.TP</code> list, in the following form (here, for a new system call flag):</dd>
<dl>
<dd>
</dd><dl>
<dt><code>XYZ_FLAG</code> (since Linux 3.7)</dt>
<dd>Description of flag&#8230;</dd></dl>
</dl>
<dd>Including version information is especially useful to users who are constrained to using older kernel or C library versions (which is typical in embedded systems, for example).</dd>
<dt><code>OPTIONS</code></dt>
<dd>A description of the command-line options accepted by a program and how they change its behavior.</dd>
<dd>This section should appear only for Section 1 and 8 manual pages.</dd>
<dt><code>EXIT STATUS</code></dt>
<dd>A list of the possible exit status values of a program and the conditions that cause these values to be returned.</dd>
<dd>This section should appear only for Section 1 and 8 manual pages.</dd>
<dt><code>RETURN VALUE</code></dt>
<dd>For Section 2 and 3 pages, this section gives a list of the values the library routine will return to the caller and the conditions that cause these values to be returned.</dd>
<dt><code>ERRORS</code></dt>
<dd>For Section 2 and 3 manual pages, this is a list of the values that may be placed in <i>errno</i> in the event of an error, along with information about the cause of the errors.</dd>
<dd>Where several different conditions produce the same error, the preferred approach is to create separate list entries (with duplicate error names) for each of the conditions. This makes the separate conditions clear, may make the list easier to read, and allows metainformation (e.g., kernel version number where the condition first became applicable) to be more easily marked for each condition.</dd>
<dd><i>The error list should be in alphabetical order</i>.</dd>
<dt><code>ENVIRONMENT</code></dt>
<dd>A list of all environment variables that affect the program or function and how they affect it.</dd>
<dt><code>FILES</code></dt>
<dd>A list of the files the program or function uses, such as configuration files, startup files, and files the program directly operates on.</dd>
<dd>Give the full pathname of these files, and use the installation process to modify the directory part to match user preferences. For many programs, the default installation location is in <i>/usr/local</i>, so your base manual page should use <i>/usr/local</i> as the base.</dd>
<dt><code>ATTRIBUTES</code></dt>
<dd>A summary of various attributes of the function(s) documented on this page. See <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7) for further details.</dd>
<dt><code>VERSIONS</code></dt>
<dd>A brief summary of the Linux kernel or glibc versions where a system call or library function appeared, or changed significantly in its operation.</dd>
<dd>As a general rule, every new interface should include a VERSIONS section in its manual page. Unfortunately, many existing manual pages don&#8217;t include this information (since there was no policy to do so when they were written). Patches to remedy this are welcome, but, from the perspective of programmers writing new code, this information probably matters only in the case of kernel interfaces that have been added in Linux 2.4 or later (i.e., changes since kernel 2.2), and library functions that have been added to glibc since version 2.1 (i.e., changes since glibc 2.0).</dd>
<dd>The <code><a href="/docs/linux/man/2-syscalls/">syscalls</a></code>(2) manual page also provides information about kernel versions in which various system calls first appeared.</dd>
<dt><code>CONFORMING TO</code></dt>
<dd>A description of any standards or conventions that relate to the function or command described by the manual page.</dd>
<dd>The preferred terms to use for the various standards are listed as headings in <code><a href="/docs/linux/man/7-standards/">standards</a></code>(7).</dd>
<dd>For a page in Section 2 or 3, this section should note the POSIX.1 version(s) that the call conforms to, and also whether the call is specified in C99. (Don&#8217;t worry too much about other standards like SUS, SUSv2, and XPG, or the SVr4 and 4.xBSD implementation standards, unless the call was specified in those standards, but isn&#8217;t in the current version of POSIX.1.)</dd>
<dd>If the call is not governed by any standards but commonly exists on other systems, note them. If the call is Linux-specific, note this.</dd>
<dd>If this section consists of just a list of standards (which it commonly does), terminate the list with a period (&#8216;.&#8217;).</dd>
<dt><code>NOTES</code></dt>
<dd>Miscellaneous notes.</dd>
<dd>For Section 2 and 3 man pages you may find it useful to include subsections (<code>SS</code>) named <i>Linux Notes</i> and <i>Glibc Notes</i>.</dd>
<dd>In Section 2, use the heading <i>C library/kernel differences</i> to mark off notes that describe the differences (if any) between the C library wrapper function for a system call and the raw system call interface provided by the kernel.</dd>
<dt><code>BUGS</code></dt>
<dd>A list of limitations, known defects or inconveniences, and other questionable activities.</dd>
<dt><code>EXAMPLES</code></dt>
<dd>One or more examples demonstrating how this function, file or command is used.</dd>
<dd>For details on writing example programs, see <i>Example programs</i> below.</dd>
<dt><code>AUTHORS</code></dt>
<dd>A list of authors of the documentation or program.</dd>
<dd><code>Use of an AUTHORS section is strongly discouraged</code>. Generally, it is better not to clutter every page with a list of (over time potentially numerous) authors; if you write or significantly amend a page, add a copyright notice as a comment in the source file. If you are the author of a device driver and want to include an address for reporting bugs, place this under the BUGS section.</dd>
<dt><code>REPORTING BUGS</code></dt>
<dd>The <i>man-pages</i> project doesn&#8217;t use a REPORTING BUGS section in manual pages. Information on reporting bugs is instead supplied in the script-generated COLOPHON section. However, various projects do use a REPORTING BUGS section. it is recommended to place it near the foot of the page.</dd>
<dt><code>COPYRIGHT</code></dt>
<dd>The <i>man-pages</i> project doesn&#8217;t use a COPYRIGHT section in manual pages. Copyright information is instead maintained in the page source. In pages where this section is present, it is recommended to place it near the foot of the page, just above SEE ALSO.</dd>
<dt><code>SEE ALSO</code></dt>
<dd>A comma-separated list of related man pages, possibly followed by other related pages or documents.</dd>
<dd>The list should be ordered by section number and then alphabetically by name. Do not terminate this list with a period.</dd>
<dd>Where the SEE ALSO list contains many long manual page names, to improve the visual result of the output, it may be useful to employ the <i>.ad l</i> (don&#8217;t right justify) and <i>.nh</i> (don&#8217;t hyphenate) directives. Hyphenation of individual page names can be prevented by preceding words with the string &quot;\%&quot;.</dd>
<dd>Given the distributed, autonomous nature of FOSS projects and their documentation, it is sometimes necessary&#8212;and in many cases desirable&#8212;that the SEE ALSO section includes references to manual pages provided by other projects.</dd></dl>
<h2>Style Guide</h2>
<p>The following subsections describe the preferred style for the <i>man-pages</i> project. For details not covered below, the Chicago Manual of Style is usually a good source; try also grepping for preexisting usage in the project source tree.</p>
<h3>Use of gender-neutral language</h3>
<p>As far as possible, use gender-neutral language in the text of man pages. Use of &quot;they&quot; (&quot;them&quot;, &quot;themself&quot;, &quot;their&quot;) as a gender-neutral singular pronoun is acceptable.</p>
<h3>Formatting conventions for manual pages describing commands</h3>
<p>For manual pages that describe a command (typically in Sections 1 and 8), the arguments are always specified using italics, <i>even in the SYNOPSIS section</i>. </p>
<p> The name of the command, and its options, should always be formatted in bold.</p>
<h3>Formatting conventions for manual pages describing functions</h3>
<p>For manual pages that describe functions (typically in Sections 2 and 3), the arguments are always specified using italics, <i>even in the SYNOPSIS section</i>, where the rest of the function is specified in bold: </p>
<p> <code> int myfunction(int </code><i>argc</i><code>, char **</code><i>argv</i><code>);</code> </p>
<p> Variable names should, like argument names, be specified in italics. </p>
<p> Any reference to the subject of the current manual page should be written with the name in bold followed by a pair of parentheses in Roman (normal) font. For example, in the <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) man page, references to the subject of the page would be written as: <code>fcntl</code>(). The preferred way to write this in the source file is: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.BR fcntl&nbsp;() </p>
<p> (Using this format, rather than the use of &quot;B&#8230;P()&quot; makes it easier to write tools that parse man page source files.)</p>
<h3>Use semantic newlines</h3>
<p>In the source of a manual page, new sentences should be started on new lines, and long sentences should split into lines at clause breaks (commas, semicolons, colons, and so on). This convention, sometimes known as &quot;semantic newlines&quot;, makes it easier to see the effect of patches, which often operate at the level of individual sentences or sentence clauses.</p>
<h3>Formatting conventions (general)</h3>
<p>Paragraphs should be separated by suitable markers (usually either <i>.PP</i> or <i>.IP</i>). Do <i>not</i> separate paragraphs using blank lines, as this results in poor rendering in some output formats (such as PostScript and PDF). </p>
<p> Filenames (whether pathnames, or references to header files) are always in italics (e.g., <i>&lt;stdio.h&gt;</i>), except in the SYNOPSIS section, where included files are in bold (e.g., <code>#include &lt;stdio.h&gt;</code>). When referring to a standard header file include, specify the header file surrounded by angle brackets, in the usual C way (e.g., <i>&lt;stdio.h&gt;</i>). </p>
<p> Special macros, which are usually in uppercase, are in bold (e.g., <code>MAXINT</code>). Exception: don&#8217;t boldface NULL. </p>
<p> When enumerating a list of error codes, the codes are in bold (this list usually uses the <code>.TP</code> macro). </p>
<p> Complete commands should, if long, be written as an indented line on their own, with a blank line before and after the command, for example </p>
<p> man 7 man-pages </p>
<p> If the command is short, then it can be included inline in the text, in italic format, for example, <i>man 7 man-pages</i>. In this case, it may be worth using nonbreaking spaces (&quot;\&nbsp;&quot;) at suitable places in the command. Command options should be written in italics (e.g., <i>-l</i>). </p>
<p> Expressions, if not written on a separate indented line, should be specified in italics. Again, the use of nonbreaking spaces may be appropriate if the expression is inlined with normal text. </p>
<p> When showing example shell sessions, user input should be formatted in bold, for example </p>
<p> $ <code>date</code> Thu Jul 7 13:01:27 CEST 2016 </p>
<p> Any reference to another man page should be written with the name in bold, <i>always</i> followed by the section number, formatted in Roman (normal) font, without any separating spaces (e.g., <code><a href="/docs/linux/man/2-intro/">intro</a></code>(2)). The preferred way to write this in the source file is: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.BR intro&nbsp;(2) </p>
<p> (Including the section number in cross references lets tools like <code><a href="/docs/linux/man/1-man2html/">man2html</a></code>(1) create properly hyperlinked pages.) </p>
<p> Control characters should be written in bold face, with no quotes; for example, <code>haX</code>.</p>
<h3>Spelling</h3>
<p>Starting with release 2.59, <i>man-pages</i> follows American spelling conventions (previously, there was a random mix of British and American spellings); please write all new pages and patches according to these conventions. </p>
<p> Aside from the well-known spelling differences, there are a few other subtleties to watch for:</p>
<dl>
<dt>*</dt>
<dd>American English tends to use the forms &quot;backward&quot;, &quot;upward&quot;, &quot;toward&quot;, and so on rather than the British forms &quot;backwards&quot;, &quot;upwards&quot;, &quot;towards&quot;, and so on.</dd></dl>
<h3>BSD version numbers</h3>
<p>The classical scheme for writing BSD version numbers is <i>x.yBSD</i>, where <i>x.y</i> is the version number (e.g., 4.2BSD). Avoid forms such as <i>BSD 4.3</i>.</p>
<h3>Capitalization</h3>
<p>In subsection (&quot;SS&quot;) headings, capitalize the first word in the heading, but otherwise use lowercase, except where English usage (e.g., proper nouns) or programming language requirements (e.g., identifier names) dictate otherwise. For example: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.SS Unicode under Linux</p>
<h3>Indentation of structure definitions, shell session logs, and so on</h3>
<p>When structure definitions, shell session logs, and so on are included in running text, indent them by 4 spaces (i.e., a block enclosed by <i>.in&nbsp;+4n</i> and <i>.in</i>), format them using the <i>.EX</i> and <i>EE</i> macros, and surround them with suitable paragraph markers (either <i>.PP</i> or <i>.IP</i>). For example: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.PP<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.in&nbsp;+4n<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.EX<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;main(int argc, char&nbsp;*argv[])<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;{<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return 0;<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.EE<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.in<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.PP</p>
<h3>Preferred terms</h3>
<p>The following table lists some preferred terms to use in man pages, mainly to ensure consistency across pages. </p>
<table>
<tr VALIGN=top>
<td>Term</td>
<td>Avoid using</td>
<td>Notes
</td>
</tr>
<tr VALIGN=top>
<td></td>
</tr>
<tr VALIGN=top>
<td>bit mask</td>
<td>bitmask</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>built-in</td>
<td>builtin</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>Epoch</td>
<td>epoch</td>
<td> For the UNIX Epoch (00:00:00, 1 Jan 1970 UTC)
</td>
</tr>
<tr VALIGN=top>
<td>filename</td>
<td>file name</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>filesystem</td>
<td>file system</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>hostname</td>
<td>host name</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>inode</td>
<td>i-node</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>lowercase</td>
<td>lower case, lower-case</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>nonzero</td>
<td>non-zero</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>pathname</td>
<td>path name</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>pseudoterminal</td>
<td>pseudo-terminal</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>privileged port</td>
<td> reserved port, system port </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>real-time</td>
<td> realtime, real time </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>run time</td>
<td>runtime</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>saved set-group-ID</td>
<td> saved group ID, saved set-GID </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>saved set-user-ID</td>
<td> saved user ID, saved set-UID </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>set-group-ID</td>
<td>set-GID, setgid</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>set-user-ID</td>
<td>set-UID, setuid</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>superuser</td>
<td> super user, super-user </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>superblock</td>
<td> super block, super-block </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>timestamp</td>
<td>time stamp</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>timezone</td>
<td>time zone</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>uppercase</td>
<td>upper case, upper-case</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>usable</td>
<td>useable</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>user space</td>
<td>userspace</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>username</td>
<td>user name</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>x86-64</td>
<td>x86_64</td>
<td> Except if referring to result of &quot;uname -m&quot; or similar
</td>
</tr>
<tr VALIGN=top>
<td>zeros</td>
<td>zeroes</td>
<td>
</td>
</tr>
</table>
<p> See also the discussion <i>Hyphenation of attributive compounds</i> below.</p>
<h3>Terms to avoid</h3>
<p>The following table lists some terms to avoid using in man pages, along with some suggested alternatives, mainly to ensure consistency across pages. </p>
<table>
<tr VALIGN=top>
<td>Avoid</td>
<td>Use instead</td>
<td>Notes
</td>
</tr>
<tr VALIGN=top>
<td></td>
</tr>
<tr VALIGN=top>
<td>32bit</td>
<td>32-bit</td>
<td> same for 8-bit, 16-bit, etc.
</td>
</tr>
<tr VALIGN=top>
<td>current process</td>
<td>calling process</td>
<td> A common mistake made by kernel programmers when writing man pages
</td>
</tr>
<tr VALIGN=top>
<td>manpage</td>
<td> man page, manual page </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>minus infinity</td>
<td>negative infinity</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>non-root</td>
<td>unprivileged user</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>non-superuser</td>
<td>unprivileged user</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>nonprivileged</td>
<td>unprivileged</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>OS</td>
<td>operating system</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>plus infinity</td>
<td>positive infinity</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>pty</td>
<td>pseudoterminal</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>tty</td>
<td>terminal</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>Unices</td>
<td>UNIX systems</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>Unixes</td>
<td>UNIX systems</td>
<td>
</td>
</tr>
</table>
<h3>Trademarks</h3>
<p>Use the correct spelling and case for trademarks. The following is a list of the correct spellings of various relevant trademarks that are sometimes misspelled: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;DG/UX<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;HP-UX<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;UNIX<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;UnixWare</p>
<h3>NULL, NUL, null pointer, and null character</h3>
<p>A <i>null pointer</i> is a pointer that points to nothing, and is normally indicated by the constant <i>NULL</i>. On the other hand, <i>NUL</i> is the <i>null byte,</i> a byte with the value 0, represented in C via the character constant <i>&#8216;</i>\0&#8217;</i>. </p>
<p> The preferred term for the pointer is &quot;null pointer&quot; or simply &quot;NULL&quot;; avoid writing &quot;NULL pointer&quot;. </p>
<p> The preferred term for the byte is &quot;null byte&quot;. Avoid writing &quot;NUL&quot;, since it is too easily confused with &quot;NULL&quot;. Avoid also the terms &quot;zero byte&quot; and &quot;null character&quot;. The byte that terminates a C string should be described as &quot;the terminating null byte&quot;; strings may be described as &quot;null-terminated&quot;, but avoid the use of &quot;NUL-terminated&quot;.  </p>
<h3>Hyperlinks</h3>
<p> For hyperlinks, use the <i>.UR</i>/<i>.UE</i> macro pair (see <code><a href="/docs/linux/man/7-groff_man/">groff_man</a></code>(7)). This produces proper hyperlinks that can be used in a web browser, when rendering a page with, say: </p>
<p> <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BROWSER=firefox man -H pagename  </p>
<h3>Use of e.g., i.e., etc., a.k.a., and similar</h3>
<p> In general, the use of abbreviations such as &quot;e.g.&quot;, &quot;i.e.&quot;, &quot;etc.&quot;, &quot;cf.&quot;, and &quot;a.k.a.&quot; should be avoided, in favor of suitable full wordings (&quot;for example&quot;, &quot;that is&quot;, &quot;and so on&quot;, &quot;compare to&quot;, &quot;also known as&quot;). </p>
<p> The only place where such abbreviations may be acceptable is in <i>short</i> parenthetical asides (e.g., like this one). </p>
<p> Always include periods in such abbreviations, as shown here. In addition, &quot;e.g.&quot; and &quot;i.e.&quot; should always be followed by a comma.  </p>
<h3>Em-dashes</h3>
<p> The way to write an em-dash---the glyph that appears at either end of this subphrase---in *roff is with the macro &quot;\(em&quot;. (On an ASCII terminal, an em-dash typically renders as two hyphens, but in other typographical contexts it renders as a long dash.) Em-dashes should be written <i>without</i> surrounding spaces.  </p>
<h3>Hyphenation of attributive compounds</h3>
<p> Compound terms should be hyphenated when used attributively (i.e., to qualify a following noun). Some examples: </p>
<p> <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;32-bit value <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;command-line argument <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;floating-point number <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;run-time check <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;user-space function <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;wide-character string  </p>
<h3>Hyphenation with multi, non, pre, re, sub, and so on</h3>
<p> The general tendency in modern English is not to hyphenate after prefixes such as &quot;multi&quot;, &quot;non&quot;, &quot;pre&quot;, &quot;re&quot;, &quot;sub&quot;, and so on. Manual pages should generally follow this rule when these prefixes are used in natural English constructions with simple suffixes. The following list gives some examples of the preferred forms: </p>
<p> <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;interprocess <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;multithreaded <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;multiprocess <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;nonblocking <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;nondefault <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;nonempty <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;noninteractive <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;nonnegative <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;nonportable <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;nonzero <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;preallocated <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;precreate <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;prerecorded <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;reestablished <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;reinitialize <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;rearm <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;reread <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;subcomponent <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;subdirectory <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;subsystem </p>
<p> Hyphens should be retained when the prefixes are used in nonstandard English words, with trademarks, proper nouns, acronyms, or compound terms. Some examples: </p>
<p> <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;non-ASCII <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;non-English <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;non-NULL <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;non-real-time </p>
<p> Finally, note that &quot;re-create&quot; and &quot;recreate&quot; are two different verbs, and the former is probably what you want.  </p>
<h3>Generating optimal glyphs</h3>
<p> Where a real minus character is required (e.g., for numbers such as -1, for man page cross references such as <code><a href="/docs/linux/man/7-utf-8/">utf-8</a></code>(7), or when writing options that have a leading dash, such as in <i>ls -l),</i> use the following form in the man page source: </p>
<p> <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;\- </p>
<p> This guideline applies also to code examples. </p>
<p> To produce unslanted single quotes that render well in ASCII, UTF-8, and PDF, use &quot;\(aq&quot; (&quot;apostrophe quote&quot;); for example </p>
<p> <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;\(aqC\(aq </p>
<p> where <i>C</i> is the quoted character. This guideline applies also to character constants used in code examples. </p>
<p> Where a proper caret (ha) that renders well in both a terminal and PDF is required, use &quot;\(ha&quot;. This is especially necessary in code samples, to get a nicely rendered caret when rendering to PDF. </p>
<p> Using a naked &quot;~&quot; character results in a poor rendering in PDF. Instead use &quot;\(ti&quot;. This is especially necessary in code samples, to get a nicely rendered tilde when rendering to PDF.  </p>
<h3>Example programs and shell sessions</h3>
<p> Manual pages may include example programs demonstrating how to use a system call or library function. However, note the following: </p>
<dl>
<dt>*</dt>
<dd> <p> Example programs should be written in C. </p>
 </dd>
<dt>*</dt>
<dd> <p> An example program is necessary and useful only if it demonstrates something beyond what can easily be provided in a textual description of the interface. An example program that does nothing other than call an interface usually serves little purpose. </p>
 </dd>
<dt>*</dt>
<dd> <p> Example programs should ideally be short (e.g., a good example can often be provided in less than 100 lines of code), though in some cases longer programs may be necessary to properly illustrate the use of an API. </p>
 </dd>
<dt>*</dt>
<dd> <p> Expressive code and useful comments are appreciated. </p>
 </dd>
<dt>*</dt>
<dd> <p> Example programs should do error checking after system calls and library function calls. </p>
 </dd>
<dt>*</dt>
<dd> <p> Example programs should be complete, and compile without warnings when compiled with <i>cc -Wall</i>. </p>
 </dd>
<dt>*</dt>
<dd> <p> Where possible and appropriate, example programs should allow experimentation, by varying their behavior based on inputs (ideally from command-line arguments, or alternatively, via input read by the program). </p>
 </dd>
<dt>*</dt>
<dd> <p> Example programs should be laid out according to Kernighan and Ritchie style, with 4-space indents. (Avoid the use of TAB characters in source code!) The following command can be used to format your source code to something close to the preferred style: </p>
 </dd>
<dd> <p> <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;indent -npro -kr -i4 -ts4 -sob -l72 -ss -nut -psl prog.c </p>
 </dd>
<dt>*</dt>
<dd> <p> For consistency, all example programs should terminate using either of: </p>
 </dd>
<dd> <p> <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE); </p>
 </dd>
<dd> <p> Avoid using the following forms to terminate a program: </p>
 </dd>
<dd> <p> <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(0); <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<a href="/docs/linux/man/1-exit/">exit</a>(1); <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return n; </p>
 </dd>
<dt>*</dt>
<dd> <p> If there is extensive explanatory text before the program source code, mark off the source code with a subsection heading <i>Program source</i>, as in: </p>
 </dd>
<dd> <p> <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.SS Program source </p>
 </dd>
<dd> <p> Always do this if the explanatory text includes a shell session log. </p>
 </dd></dl>
<p> If you include a shell session log demonstrating the use of a program or other system feature: </p>
<dl>
<dt>*</dt>
<dd> <p> Place the session log above the source code listing </p>
 </dd>
<dt>*</dt>
<dd> <p> Indent the session log by four spaces. </p>
 </dd>
<dt>*</dt>
<dd> <p> Boldface the user input text, to distinguish it from output produced by the system. </p>
 </dd></dl>
<p> For some examples of what example programs should look like, see <code><a href="/docs/linux/man/2-wait/">wait</a></code>(2) and <code><a href="/docs/linux/man/2-pipe/">pipe</a></code>(2).  </p>
<h2>EXAMPLES</h2>
<p> For canonical examples of how man pages in the <i>man-pages</i> package should look, see <code><a href="/docs/linux/man/2-pipe/">pipe</a></code>(2) and <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2).  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-man/">man</a></code>(1), <code><a href="/docs/linux/man/1-man2html/">man2html</a></code>(1), <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7), <code><a href="/docs/linux/man/7-groff/">groff</a></code>(7), <code><a href="/docs/linux/man/7-groff_man/">groff_man</a></code>(7), <code><a href="/docs/linux/man/7-man/">man</a></code>(7), <code><a href="/docs/linux/man/7-mdoc/">mdoc</a></code>(7)  </p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
