---
title: "git-backpan-init(1)"
name: "git-backpan-init"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-backpan-init/"
---

<h2 class="name">NAME</h2>
 

 git-backpan-init - Initialize a repository for a CPAN module with full history from the backpan. 

<h2>SYNOPSIS</h2>

 <pre><code>
git backpan - init[--help | --man][--mkdir&lt;directory&gt;][--force] Foo::Bar
</code></pre>

<h2>DESCRIPTION</h2>

 This command is like <tt>&quot;cpan-init&quot;</tt> except it imports all the historical versions of a module as well, allowing you to run <tt>&quot;git bisect&quot;</tt> or to browse history. 

 The name of the module can be written with double-colons or dashes (i.e., <i>Foo::Bar</i> or <i>Foo-Bar</i>). 

 Unless the <i>-force</i> option is used, the command will abort if a git repository is found to be already present in the directory.

<h2>OPTIONS</h2>

<dl>
<dt>--mkdir <i>directory</i>
<dd> Creates a sub-directory and create the git repository there instead than in the current directory. If no directory name is given, figures one out based on the name of the module.
<dt>--force, -f
<dd> Forces the imports, even if a git repository was already present in the directory.
<dt>--help, -h
<dd> Prints the synopsis and valid options and exits.
<dt>--man
<dd> Prints the man page and exits.</dl>

<h2>EXAMPLES</h2>

 Most of the time, you want to use <i>git backpan-init</i> like this: 

 <pre>
    % cd ~/work/
    % git backpan-init -mkdir Foo::Bar
</pre>

<h2>VERSION</h2>

 This document describes git-backpan-init version 0.2.1

<h2>BUGS AND LIMITATIONS</h2>

 When importing a package history with git-backpan-init, version checking will be automatically turned off. This is to circumvent the cases where, e.g., version 0.38.1 (morphed into 0.038001 by the module <i>version</i>) follows version 0.38. We are making the (hopefully reasonable) assumption that the chronological order reported by the Backpan trumps all. 

 If a version of the package can't be extracted, <i>git-backpan-init</i> will issue a warning and skip to the next version. 

 Please report any bugs or feature requests to <tt>&quot;bug-git-cpan-patch [at] rt.cpan.org&quot;</tt>, or through the web interface at &lt;<a rel="nofollow" HREF="http://rt.cpan.org">http://rt.cpan.org</a>&gt;.

<h2>AUTHORS</h2>

 Yanick Champoux <tt>&quot;&lt;yanick [at] cpan.org&gt;&quot;</tt> 

 Yuval Kogman <tt>&quot;&lt;nothingmuch [at] woobling.org&gt;&quot;</tt>

<h2>LICENCE</h2>

 This module is free software; you can redistribute it and/or modify it under the same terms as Perl itself. See perlartistic.

<h2>SEE ALSO</h2>

 Git::CPAN::Patch 

<h2>Index</h2>


