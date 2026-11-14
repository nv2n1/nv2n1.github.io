---
title: "l3build(1)"
name: "l3build"
section: "1"
letter: "l"
url: "/docs/linux/man/1-l3build/"
---

<h2 class="name">NAME</h2>
 

 l3build - Checking and building packages 

<h2>SYNOPSIS</h2>

 l3build &lt;command&gt; [&lt;options&gt;] [&lt;names&gt;]

<h2>DESCRIPTION</h2>

 The l3build system is a Lua script for building TeX packages, with particular emphasis on regression testing. It is written in cross-platform Lua code, so can be used by any modern TeX distribution with the texlua interpreter. A package for building with l3build can be written in any TeX dialect; its defaults are set up for LaTeX packages written in the DocStrip style. 

 The most commonly used l3build commands are:
<dl>
<dt>check
<dd> Run all automated tests
<dt>clean
<dd> Clean out directory tree
<dt>doc
<dd> Typesets all documentation files
<dt>install
<dd> Installs files into the local texmf tree
<dt>save
<dd> Saves test validation log
<dt>tag
<dd> Update release tags in files
<dt>uninstall
<dd> Uninstalls files from the local texmf tree
<dt>unpack
<dd> Unpacks the source files into the build tree</dl>

<h2>OPTIONS</h2>

 Various options apply
<dl>
<dt>--config|-c
<dd> Sets the config(s) used for running tests
<dt>--date
<dd> Sets the date to insert into sources
<dt>--dry-run
<dd> Dry run for install
<dt>--engine|-e
<dd> Sets the engine(s) to use for running test
<dt>--epoch
<dd> Sets the epoch for tests and typesetting
<dt>--first
<dd> Name of first test to run
<dt>--force|-f
<dd> Force tests to run if engine is not set up
<dt>--halt-on-error|-H
<dd> Stops running tests after the first failure
<dt>--last
<dd> Name of last test to run
<dt>--pdf|-p
<dd> Check/save PDF files
<dt>--quiet|-q
<dd> Suppresses TeX output when unpacking
<dt>--rerun
<dd> Skip setup: simply rerun tests
<dt>--shuffle
<dd> Shuffle order of tests
<dt>--texmfhome
<dd> Location of user texmf tree</dl>

<h2>BUGS</h2>

<h2>AUTHOR</h2>

 The LaTeX Project (latex-team [at] latex-project.org) 

 Please log issues on the GitHub homepage: <a rel="nofollow" HREF="https://github.com/latex3/l3build/issues.">https://github.com/latex3/l3build/issues.</a>

<h2>SEE ALSO</h2>

 See l3build.pdf for more details. 

<h2>Index</h2>


