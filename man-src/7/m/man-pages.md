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
<dt><code>1 User commands (Programs)</code></p>
<dd>Commands that can be executed by the user from within a shell.</p>
<dt><code>2 System calls</code></p>
<dd>Functions which wrap operations performed by the kernel.</p>
<dt><code>3 Library calls</code></p>
<dd>All library functions excluding the system call wrappers (Most of the <i>libc</i> functions).</p>
<dt><code>4 Special files (devices)</code></p>
<dd>Files found in <i>/dev</i> which allow to access to devices through the kernel.</p>
<dt><code>5 File formats and configuration files</code></p>
<dd>Describes various human-readable file formats and configuration files.</p>
<dt><code>6 Games</code></p>
<dd>Games and funny little programs available on the system.</p>
<dt><code>7 Overview, conventions, and miscellaneous</code></p>
<dd>Overviews or descriptions of various topics, conventions and protocols, character set standards, the standard filesystem layout, and miscellaneous other things.</p>
<dt><code>8 System management commands</code></p>
<dd>Commands like <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8), many of which only root can execute.</dl>
<h3>Macro package</h3>
<p>New manual pages should be marked up using the <code>groff an.tmac</code> package described in <code><a href="/docs/linux/man/7-man/">man</a></code>(7). This choice is mainly for consistency: the vast majority of existing Linux manual pages are marked up using these macros.</p>
<h3>Conventions for source file layout</h3>
<p>Please limit source code line length to no more than about 75 characters wherever possible. This helps avoid line-wrapping in some mail clients when patches are submitted inline.</p>
<h3>Title line</h3>
<p>The first command in a man page should be a <code>TH</code> command: </p>
<dl>
<dd><code>.TH</code> <i>title section date source manual</i></dl>
<p> The arguments of the command are as follows:</p>
<dl>
<dt><i>title</i></p>
<dd>The title of the man page, written in all caps (e.g., <i>MAN-PAGES</i>).</p>
<dt><i>section</i></p>
<dd>The section number in which the man page should be placed (e.g., <i>7</i>).</p>
<dt><i>date</i></p>
<dd>The date of the last nontrivial change that was made to the man page. (Within the <i>man-pages</i> project, the necessary updates to these timestamps are handled automatically by scripts, so there is no need to manually update them as part of a patch.) Dates should be written in the form YYYY-MM-DD.</p>
<dt><i>source</i></p>
<dd>The source of the command, function, or system call.</p>
<dd>For those few <i>man-pages</i> pages in Sections 1 and 8, probably you just want to write <i>GNU</i>.</p>
<dd>For system calls, just write <i>Linux</i>. (An earlier practice was to write the version number of the kernel from which the manual page was being written/checked. However, this was never done consistently, and so was probably worse than including no version number. Henceforth, avoid including a version number.)</p>
<dd>For library calls that are part of glibc or one of the other common GNU libraries, just use <i>GNU C Library</i>, <i>GNU</i>, or an empty string.</p>
<dd>For Section 4 pages, use <i>Linux</i>.</p>
<dd>In cases of doubt, just write <i>Linux</i>, or <i>GNU</i>.</p>
<dt><i>manual</i></p>
<dd>The title of the manual (e.g., for Section 2 and 3 pages in the <i>man-pages</i> package, use <i>Linux Programmer&#8217;s Manual</i>).</dl>
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
</dl>
<p> <i>Where a traditional heading would apply</i>, <i>please use it</i>; this kind of consistency can make the information easier to understand. If you must, you can create your own headings if they make things easier to understand (this can be especially useful for pages in Sections 4 and 5). However, before doing this, consider whether you could use the traditional headings, with some subsections (<i>.SS</i>) within those sections. </p>
<p> The following list elaborates on the contents of each of the above sections.</p>
<dl>
<dt><code>NAME</code></p>
<dd>The name of this manual page.</p>
<dd>See <code><a href="/docs/linux/man/7-man/">man</a></code>(7) for important details of the line(s) that should follow the <code>.SH NAME</code> command. All words in this line (including the word immediately following the &quot;\-&quot;) should be in lowercase, except where English or technical terminological convention dictates otherwise.</p>
<dt><code>SYNOPSIS</code></p>
<dd>A brief summary of the command or function&#8217;s interface.</p>
<dd>For commands, this shows the syntax of the command and its arguments (including options); boldface is used for as-is text and italics are used to indicate replaceable arguments. Brackets ([]) surround optional arguments, vertical bars (|) separate choices, and ellipses (&#8230;) can be repeated. For functions, it shows any required data declarations or <code>#include</code> directives, followed by the function declaration.</p>
<dd>Where a feature test macro must be defined in order to obtain the declaration of a function (or a variable) from a header file, then the SYNOPSIS should indicate this, as described in <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7).</p>
<dt><code>CONFIGURATION</code></p>
<dd>Configuration details for a device.</p>
<dd>This section normally appears only in Section 4 pages.</p>
<dt><code>DESCRIPTION</code></p>
<dd>An explanation of what the program, function, or format does.</p>
<dd>Discuss how it interacts with files and standard input, and what it produces on standard output or standard error. Omit internals and implementation details unless they&#8217;re critical for understanding the interface. Describe the usual case; for information on command-line options of a program use the <code>OPTIONS</code> section.</p>
<dd>When describing new behavior or new flags for a system call or library function, be careful to note the kernel or C library version that introduced the change. The preferred method of noting this information for flags is as part of a <code>.TP</code> list, in the following form (here, for a new system call flag):</p>
<dl>
<dd>
<dl>
<dt><code>XYZ_FLAG</code> (since Linux 3.7)</p>
<dd>Description of flag&#8230;</dl>
</dl>
<dd>Including version information is especially useful to users who are constrained to using older kernel or C library versions (which is typical in embedded systems, for example).</p>
<dt><code>OPTIONS</code></p>
<dd>A description of the command-line options accepted by a program and how they change its behavior.</p>
<dd>This section should appear only for Section 1 and 8 manual pages.</p>
<dt><code>EXIT STATUS</code></p>
<dd>A list of the possible exit status values of a program and the conditions that cause these values to be returned.</p>
<dd>This section should appear only for Section 1 and 8 manual pages.</p>
<dt><code>RETURN VALUE</code></p>
<dd>For Section 2 and 3 pages, this section gives a list of the values the library routine will return to the caller and the conditions that cause these values to be returned.</p>
<dt><code>ERRORS</code></p>
<dd>For Section 2 and 3 manual pages, this is a list of the values that may be placed in <i>errno</i> in the event of an error, along with information about the cause of the errors.</p>
<dd>Where several different conditions produce the same error, the preferred approach is to create separate list entries (with duplicate error names) for each of the conditions. This makes the separate conditions clear, may make the list easier to read, and allows metainformation (e.g., kernel version number where the condition first became applicable) to be more easily marked for each condition.</p>
<dd><i>The error list should be in alphabetical order</i>.</p>
<dt><code>ENVIRONMENT</code></p>
<dd>A list of all environment variables that affect the program or function and how they affect it.</p>
<dt><code>FILES</code></p>
<dd>A list of the files the program or function uses, such as configuration files, startup files, and files the program directly operates on.</p>
<dd>Give the full pathname of these files, and use the installation process to modify the directory part to match user preferences. For many programs, the default installation location is in <i>/usr/local</i>, so your base manual page should use <i>/usr/local</i> as the base.</p>
<dt><code>ATTRIBUTES</code></p>
<dd>A summary of various attributes of the function(s) documented on this page. See <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7) for further details.</p>
<dt><code>VERSIONS</code></p>
<dd>A brief summary of the Linux kernel or glibc versions where a system call or library function appeared, or changed significantly in its operation.</p>
<dd>As a general rule, every new interface should include a VERSIONS section in its manual page. Unfortunately, many existing manual pages don&#8217;t include this information (since there was no policy to do so when they were written). Patches to remedy this are welcome, but, from the perspective of programmers writing new code, this information probably matters only in the case of kernel interfaces that have been added in Linux 2.4 or later (i.e., changes since kernel 2.2), and library functions that have been added to glibc since version 2.1 (i.e., changes since glibc 2.0).</p>
<dd>The <code><a href="/docs/linux/man/2-syscalls/">syscalls</a></code>(2) manual page also provides information about kernel versions in which various system calls first appeared.</p>
<dt><code>CONFORMING TO</code></p>
<dd>A description of any standards or conventions that relate to the function or command described by the manual page.</p>
<dd>The preferred terms to use for the various standards are listed as headings in <code><a href="/docs/linux/man/7-standards/">standards</a></code>(7).</p>
<dd>For a page in Section 2 or 3, this section should note the POSIX.1 version(s) that the call conforms to, and also whether the call is specified in C99. (Don&#8217;t worry too much about other standards like SUS, SUSv2, and XPG, or the SVr4 and 4.xBSD implementation standards, unless the call was specified in those standards, but isn&#8217;t in the current version of POSIX.1.)</p>
<dd>If the call is not governed by any standards but commonly exists on other systems, note them. If the call is Linux-specific, note this.</p>
<dd>If this section consists of just a list of standards (which it commonly does), terminate the list with a period (&#8216;.&#8217;).</p>
<dt><code>NOTES</code></p>
<dd>Miscellaneous notes.</p>
<dd>For Section 2 and 3 man pages you may find it useful to include subsections (<code>SS</code>) named <i>Linux Notes</i> and <i>Glibc Notes</i>.</p>
<dd>In Section 2, use the heading <i>C library/kernel differences</i> to mark off notes that describe the differences (if any) between the C library wrapper function for a system call and the raw system call interface provided by the kernel.</p>
<dt><code>BUGS</code></p>
<dd>A list of limitations, known defects or inconveniences, and other questionable activities.</p>
<dt><code>EXAMPLES</code></p>
<dd>One or more examples demonstrating how this function, file or command is used.</p>
<dd>For details on writing example programs, see <i>Example programs</i> below.</p>
<dt><code>AUTHORS</code></p>
<dd>A list of authors of the documentation or program.</p>
<dd><code>Use of an AUTHORS section is strongly discouraged</code>. Generally, it is better not to clutter every page with a list of (over time potentially numerous) authors; if you write or significantly amend a page, add a copyright notice as a comment in the source file. If you are the author of a device driver and want to include an address for reporting bugs, place this under the BUGS section.</p>
<dt><code>REPORTING BUGS</code></p>
<dd>The <i>man-pages</i> project doesn&#8217;t use a REPORTING BUGS section in manual pages. Information on reporting bugs is instead supplied in the script-generated COLOPHON section. However, various projects do use a REPORTING BUGS section. it is recommended to place it near the foot of the page.</p>
<dt><code>COPYRIGHT</code></p>
<dd>The <i>man-pages</i> project doesn&#8217;t use a COPYRIGHT section in manual pages. Copyright information is instead maintained in the page source. In pages where this section is present, it is recommended to place it near the foot of the page, just above SEE ALSO.</p>
<dt><code>SEE ALSO</code></p>
<dd>A comma-separated list of related man pages, possibly followed by other related pages or documents.</p>
<dd>The list should be ordered by section number and then alphabetically by name. Do not terminate this list with a period.</p>
<dd>Where the SEE ALSO list contains many long manual page names, to improve the visual result of the output, it may be useful to employ the <i>.ad l</i> (don&#8217;t right justify) and <i>.nh</i> (don&#8217;t hyphenate) directives. Hyphenation of individual page names can be prevented by preceding words with the string &quot;\%&quot;.</p>
<dd>Given the distributed, autonomous nature of FOSS projects and their documentation, it is sometimes necessary&#8212;and in many cases desirable&#8212;that the SEE ALSO section includes references to manual pages provided by other projects.</dl>
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
<dt>*</p>
<dd>American English tends to use the forms &quot;backward&quot;, &quot;upward&quot;, &quot;toward&quot;, and so on rather than the British forms &quot;backwards&quot;, &quot;upwards&quot;, &quot;towards&quot;, and so on.</dl>
<h3>BSD version numbers</h3>
<p>The classical scheme for writing BSD version numbers is <i>x.yBSD</i>, where <i>x.y</i> is the version number (e.g., 4.2BSD). Avoid forms such as <i>BSD 4.3</i>.</p>
<h3>Capitalization</h3>
<p>In subsection (&quot;SS&quot;) headings, capitalize the first word in the heading, but otherwise use lowercase, except where English usage (e.g., proper nouns) or programming language requirements (e.g., identifier names) dictate otherwise. For example: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.SS Unicode under Linux</p>
<h3>Indentation of structure definitions, shell session logs, and so on</h3>
<p>When structure definitions, shell session logs, and so on are included in running text, indent them by 4 spaces (i.e., a block enclosed by <i>.in&nbsp;+4n</i> and <i>.in</i>), format them using the <i>.EX</i> and <i>EE</i> macros, and surround them with suitable paragraph markers (either <i>.PP</i> or <i>.IP</i>). For example: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.PP<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.in&nbsp;+4n<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.EX<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;main(int argc, char&nbsp;*argv[])<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return 0;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.EE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.in<br />
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
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;DG/UX<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;HP-UX<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;UNIX<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;UnixWare</p>
<h3>NULL, NUL, null pointer, and null character</h3>
<p>A <i>null pointer</i> is a pointer that points to nothing, and is normally indicated by the constant <i>NULL</i>. On the other hand, <i>NUL</i> is the <i>null byte,</i> a byte with the value 0, represented in C via the character constant <i>&#8216;
