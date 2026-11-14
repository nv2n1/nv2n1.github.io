---
title: "dh_autotools-dev_restoreconfig(1)"
name: "dh_autotools-dev_restoreconfig"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_autotools-dev_restoreconfig/"
description: "dh_autotools-dev_restoreconfig – restore config.sub and config.guess"
---

<h2 class="name">NAME</h2>
<p> dh_autotools-dev_restoreconfig &#8211; restore config.sub and config.guess </p>
<h2>SYNOPSIS</h2>
<p> <code>dh_autotools-dev_restoreconfig</code> [<i>debhelper options</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>Deprecated</code>: dh_autotools-dev_updateconfig and dh_autotools-dev_restoreconfig are deprecated and replaced by <code><a href="/docs/linux/man/1-dh_update_autotools_config/">dh_update_autotools_config</a></code>(1) and <code><a href="/docs/linux/man/1-dh_clean/">dh_clean</a></code>(1) from debhelper. Please replace all uses of dh_autotools-dev_updateconfig with dh_update_autotools_config and then remove any use of dh_autotools-dev_restoreconfig. </p>
<p> dh_autotools-dev_restoreconfig restores the original <code>config.sub</code> and <code>config.guess</code> files that have been backed up by dh_autotools-dev_updateconfig under the names <code>config.sub.dh-orig</code> and <code>config.guess.dh-orig</code>.</p>
<h2>EXAMPLES</h2>
<p> dh_autotools-dev_restoreconfig is usually called indirectly in a rules file via the dh command. </p>
<pre>
        %:
                dh $@ --with autotools_dev
</pre>
<p> It can also be direcly called in the clean rule. </p>
<pre>
        clean:
                dh_testdir
                dh_testroot
                [ ! -f Makefile ] || $(MAKE) clean
                dh_autotools-dev_restoreconfig
                dh_clean
</pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-debhelper/">debhelper</a></code>(7), <code><a href="/docs/linux/man/1-dh/">dh</a></code>(1). </p>
<p> This program is meant to be used together with debhelper.</p>
<h2>AUTHOR</h2>
<p> Fabian Greffrath &lt;fabian+debian [at] greffrath.com&gt; </p>
<h2>Index</h2>
