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
</dt><dd> Run all automated tests
</dd><dt>clean
</dt><dd> Clean out directory tree
</dd><dt>doc
</dt><dd> Typesets all documentation files
</dd><dt>install
</dt><dd> Installs files into the local texmf tree
</dd><dt>save
</dt><dd> Saves test validation log
</dd><dt>tag
</dt><dd> Update release tags in files
</dd><dt>uninstall
</dt><dd> Uninstalls files from the local texmf tree
</dd><dt>unpack
</dt><dd> Unpacks the source files into the build tree</dd></dl>

<h2>OPTIONS</h2>

 Various options apply
<dl>
<dt>--config|-c
</dt><dd> Sets the config(s) used for running tests
</dd><dt>--date
</dt><dd> Sets the date to insert into sources
</dd><dt>--dry-run
</dt><dd> Dry run for install
</dd><dt>--engine|-e
</dt><dd> Sets the engine(s) to use for running test
</dd><dt>--epoch
</dt><dd> Sets the epoch for tests and typesetting
</dd><dt>--first
</dt><dd> Name of first test to run
</dd><dt>--force|-f
</dt><dd> Force tests to run if engine is not set up
</dd><dt>--halt-on-error|-H
</dt><dd> Stops running tests after the first failure
</dd><dt>--last
</dt><dd> Name of last test to run
</dd><dt>--pdf|-p
</dt><dd> Check/save PDF files
</dd><dt>--quiet|-q
</dt><dd> Suppresses TeX output when unpacking
</dd><dt>--rerun
</dt><dd> Skip setup: simply rerun tests
</dd><dt>--shuffle
</dt><dd> Shuffle order of tests
</dd><dt>--texmfhome
</dt><dd> Location of user texmf tree</dd></dl>

<h2>BUGS</h2>

<h2>AUTHOR</h2>

 The LaTeX Project (latex-team [at] latex-project.org) 

 Please log issues on the GitHub homepage: <a rel="nofollow" HREF="https://github.com/latex3/l3build/issues.">https://github.com/latex3/l3build/issues.</a>

<h2>SEE ALSO</h2>

 See l3build.pdf for more details. 

<h2>Index</h2>


