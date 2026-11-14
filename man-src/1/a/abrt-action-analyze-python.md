---
title: "abrt-action-analyze-python(1)"
name: "abrt-action-analyze-python"
section: "1"
letter: "a"
url: "/docs/linux/man/1-abrt-action-analyze-python/"
---

<h2 class="name">NAME</h2>
 

 abrt-action-analyze-python - Calculate and save UUID and duplicate hash for a problem data directory DIR with Python crash data. 

<h2>SYNOPSIS</h2>

 

 <i>abrt-action-analyze-python</i> [-v] [-d DIR]

<h2>DESCRIPTION</h2>

 

 The tool reads the file named <i>backtrace</i> from a problem data directory, parses it as a Python exception and generates a duplication hash and a universally unique identifier (UUID). Then it saves this data as new elements <i>duphash</i> and <i>uuid</i>.

<h3>Integration with ABRT events</h3>

 

 <i>abrt-action-analyze-python</i> can be used to generate the duplication hash of a newly discovered Python crash. 

<dl>
<dt>
<dd> <pre>
EVENT=post-create analyzer=Python   abrt-action-analyze-python
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


