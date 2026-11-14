---
title: "ipython(1)"
name: "ipython"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ipython/"
description: "ipython – Tools for Interactive Computing in Python."
---

<h2 class="name">NAME</h2>
<p> ipython &#8211; Tools for Interactive Computing in Python. </p>
<h2>SYNOPSIS</h2>
<p> <code>ipython</code> [<i>options</i>]<i> files</i>&#8230; </p>
<p> <code>ipython subcommand</code> [<i>options</i>]<i>&#8230;</i> </p>
<h2>DESCRIPTION</h2>
<p> An interactive Python shell with automatic history (input and output), dynamic object introspection, easier configuration, command completion, access to the system shell, integration with numerical and scientific computing tools, web notebook, Qt console, and more. </p>
<p> For more information on how to use IPython, see &#8216;ipython &#8211;help&#8217;, or &#8216;ipython &#8211;help-all&#8217; for all available command-line options. </p>
<h2>ENVIRONMENT VARIABLES</h2>
<p> <i>IPYTHONDIR</i></p>
<dl>
<dt>
<dd> This is the location where IPython stores all its configuration files. The default is $HOME/.ipython if IPYTHONDIR is not defined. </p>
<p> You can see the computed value of IPYTHONDIR with `ipython locate`. </p>
</dl>
<h2>FILES</h2>
<p> IPython uses various configuration files stored in profiles within IPYTHONDIR. To generate the default configuration files and start configuring IPython, do &#8216;ipython profile create&#8217;, and edit &#8216;*_config.py&#8217; files located in IPYTHONDIR/profile_default. </p>
<h2>AUTHORS</h2>
<p> IPython is written by the IPython Development Team &lt;<a rel="nofollow" href="https://github.com/ipython/ipython">https://github.com/ipython/ipython</a>&gt;. </p>
<h2>Index</h2>
