---
title: "abrt-action-analyze-java(1)"
name: "abrt-action-analyze-java"
section: "1"
letter: "a"
url: "/docs/linux/man/1-abrt-action-analyze-java/"
---

<h2 class="name">NAME</h2>
 

 abrt-action-analyze-java - Calculate and save UUID &amp; DUPHASH and determine the level of usability for reporting of a Java stack trace. 

<h2>SYNOPSIS</h2>

 

 <i>abrt-action-analyze-java</i> [-v] [-d DIR] [-o] [-f FILE]

<h2>DESCRIPTION</h2>

 

 The tool reads the file named <i>backtrace</i> from a problem data directory, processes it and generates a universally unique identifier (UUID). Then it saves this data as new element <i>uuid</i>. It also checks whether the stack trace contains a remote address in any of its frames and if so it creates <i>not-reportable</i> element whose contents explains why the stack trace should not be reported into a bug tracking system.

<h3>Integration with ABRT events</h3>

 

 <i>abrt-action-analyze-java</i> can be used to generate the UUID &amp; DUPHAS of a newly saved Java stack trace. 

<dl>
<dt>
<dd> <pre>
EVENT=post-create analyzer=Java   abrt-action-analyze-java
</pre></dl>

<h2>OPTIONS</h2>

 

 -d DIR
<dl>
<dt>
<dd> Path to a problem directory. The tool reads the backtrace from stdin when neither this option nor -f is provided.</dl>
 

 -f FILE
<dl>
<dt>
<dd> Path to a stack trace. The tool reads the backtrace from stdin when neither this option nor -d is provided.</dl>
 

 -o
<dl>
<dt>
<dd> Print the result to stdout.</dl>
 

 -v
<dl>
<dt>
<dd> Be more verbose. Can be given multiple times.</dl>

<h2>AUTHORS</h2>

 

<dl>
<dt>
<dd> &bull; ABRT team</dl>
 

<h2>Index</h2>


