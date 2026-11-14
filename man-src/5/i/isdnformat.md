---
title: "isdnformat(5)"
name: "isdnformat"
section: "5"
letter: "i"
url: "/docs/linux/man/5-isdnformat/"
description: "isdnformat – common isdn config file format"
---

<p>isdnformat &#8211; common isdn config file format</p>
<h2>Description</h2>
<p>This man page describes the format of all isdn config files. </p>
<h2>Format</h2>
<p>Empty lines are ignored. </p>
<p> If a # is encountered, this character and the rest of the line is ignored (it&#8217;s considered a comment). You can prepend a backslash \ to prevent this and use the # character. </p>
<p> If the last character of a line is a backslash \, the next line is a continuation of the current line. </p>
<p> The file format is like smb.conf or win.ini: there are sections and entries within the section. However, the syntax was expanded with subsections; these can be nested as often as you like. </p>
<p> All whitespace (space and tabs) at the end of the line are ignored. </p>
<p> Section and entry names are case insensitive. </p>
<p> Values are case sensitive, of course (the case is preserved). </p>
<p> Section and entry names may not use the characters &quot;*?|&amp;/&quot;; if one of these is encountered, it is ignored. </p>
<p> At the beginning of the line you may use as much whitespace as you like. </p>
<p> A section has the format &quot;[&quot; NAME &quot;]&quot;. You may use whitespace between the braces and the name, or none at all. </p>
<p> An entry has the format ENTRY &quot;=&quot; VALUE. You may use whitespace before and after the equal sign, or none at all. </p>
<p> A subsection starts with ENTRY &quot;=&quot; &quot;{&quot; and ends with &quot;}&quot;. You may use sections, entries and subsections between the start and the end tag. </p>
<p> Beware: unlike samba or windows the semicolon is <code>not</code> used for comments ! </p>
<p> You can use <code>INCLUDE(File)</code> to include a file. If the filename is not absolute, it&#8217;s considered relative to the directory of the including document. You may use it anywhere in a file, but there may be no space characters in the file! </p>
<p> All subsections started in an include file must end in that include file, so the number of opened and closed brackets must match. </p>
<p> Beware: recursive including will cause the program to break. The library does not prevent this.</p>
<h2>Author</h2>
<p>This manual page was written by Andreas Jellinghaus &lt;aj [at] dungeon.inka.de&gt;, for Debian GNU/Linux and isdn4linux. Now maintained by Paul Slootman &lt;paul [at] isdn4linux.de&gt;.</p>
