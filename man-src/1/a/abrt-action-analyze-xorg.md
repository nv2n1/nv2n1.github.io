---
title: "abrt-action-analyze-xorg(1)"
name: "abrt-action-analyze-xorg"
section: "1"
letter: "a"
url: "/docs/linux/man/1-abrt-action-analyze-xorg/"
---

<h2 class="name">NAME</h2>
 

 abrt-action-analyze-xorg - Calculate and save UUID and duplicate hash for a problem data directory DIR with Xorg backtrace. 

<h2>SYNOPSIS</h2>

 

 <i>abrt-action-analyze-xorg</i> [-v] [-d DIR]

<h2>DESCRIPTION</h2>

 

 The tool reads the file named <i>Xorg.0.log</i> and checks if any black listed module was loaded. If so, <i>not-reportable</i> file is created with an appropriate explanation text. If no black listed module was loaded, the tool reads the file named <i>backtrace</i> from a problem data directory record and generates a duplication hash and a universally unique identifier (UUID). Then it saves this data as new elements <i>duphash</i> and <i>uuid</i>.

<h3>Integration with ABRT events</h3>

 

 <i>abrt-action-analyze-xorg</i> can be used to generate the duplication hash of a newly discovered Xorg backtraces. 

<dl>
<dt>
<dd> <pre>
EVENT=post-create analyzer=Xorg   abrt-action-analyze-xorg
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

<h2>FILES</h2>

 

 /etc/abrt/xorg.conf List of modules which, when loaded, should make Xorg crashes non-reportable.

<h2>AUTHORS</h2>

 

<dl>
<dt>
<dd> &bull; ABRT team</dl>
 

<h2>Index</h2>


