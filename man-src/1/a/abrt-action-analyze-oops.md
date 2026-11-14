---
title: "abrt-action-analyze-oops(1)"
name: "abrt-action-analyze-oops"
section: "1"
letter: "a"
url: "/docs/linux/man/1-abrt-action-analyze-oops/"
---

<h2 class="name">NAME</h2>
 

 abrt-action-analyze-oops - Calculate and save UUID and duplicate hash for a problem data directory DIR with kernel oops. 

<h2>SYNOPSIS</h2>

 

 <i>abrt-action-analyze-oops</i> [-v] [-d DIR]

<h2>DESCRIPTION</h2>

 

 The tool reads the file named <i>backtrace</i> from a problem data directory, parses it as a kernel oops record and generates a duplication hash and a universally unique identifier (UUID). Then it saves this data as new elements <i>duphash</i> and <i>uuid</i>.

<h3>Integration with ABRT events</h3>

 

 <i>abrt-action-analyze-oops</i> can be used to generate the duplication hash of a newly discovered kernel oops. 

<dl>
<dt>
<dd> <pre>
EVENT=post-create analyzer=Kerneloops   abrt-action-analyze-oops
</pre></dl>

<h2>OPTIONS</h2>

 

 -d DIR
<dl>
<dt>
<dd> Path to a problem directory. Current working directory is used when this option is not provided.</dl>
 

 -v
<dl>
<dt>
<dd> Be more verbose. Can be given multiple times.</dl>

<h2>AUTHORS</h2>

 

<dl>
<dt>
<dd> &bull; ABRT team</dl>
 

<h2>Index</h2>


