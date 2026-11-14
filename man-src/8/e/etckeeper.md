---
title: "etckeeper(8)"
name: "etckeeper"
section: "8"
letter: "e"
url: "/docs/linux/man/8-etckeeper/"
description: "etckeeper – store /etc in git, mercurial, bazaar, or darcs"
---

<p>etckeeper &#8211; store /etc in git, mercurial, bazaar, or darcs</p>
<h2>Synopsis</h2>
<p><code>etckeeper command [-d directory]</code></p>
<h2>Description</h2>
<p>etckeeper manages /etc be stored in a git, mercurial, bazaar, or darcs repository. By default each of the commands operates on /etc, but a different directory can be specified to operate on a clone of the /etc repository located elsewhere.</p>
<h2>Commands</h2>
<dl>
<dt><code>init</code></p>
<dd>This initialises and sets up a git, mercurial, bazaar, or darcs repository (depending on the VCS setting in /etc/etckeeper/etckeeper.conf). Typically this is run in /etc once when starting to use etckeeper on a machine. It can also be used to initialise a clone of the /etc repository located elsewhere.</p>
<dt><code>commit [message]</code></p>
<dd>Commits all changes in /etc to the repository. A commit message can be specified. You may also use the underlying VCS to commit manually. (Note that etckeeper commit will notice if a user has used sudo or su to become root, and record the original username in the commit.)</p>
<dt><code>pre-commit</code></p>
<dd>This is called as a pre-commit hook. It stores metadata and does sanity checks.</p>
<dt><code>pre-install</code></p>
<dd>This is called by apt&#8217;s DPkg::Pre-Install-Pkgs hook, or by equivalent hooks of other package managers. It allows committing any uncommitted changes before packages are installed, upgraded, etc.</p>
<dt><code>post-install</code></p>
<dd>This is called by apt&#8217;s DPkg::Post-Invoke hook, or by equivalent hooks of other package managers. It commits changes made by packages into the repository. (You can also call this by hand after running dpkg by hand.)</p>
<dt><code>unclean</code></p>
<dd>This returns true if the directory contains uncommitted changes.</p>
<dt><code>update-ignore [-a]</code></p>
<dd>This updates the VCS ignore file. Content outside a &quot;managed by etckeeper&quot; block is not touched. This is generally run when upgrading to a new version of etckeeper. (The -a switch will add a &quot;managed by etckeeper&quot; block if one is not present.)</p>
<dt><code>vcs subcommand [options &#8230;]</code></p>
<dd>You can use this to run any subcommand of the VCS that etckeeper is configured to run. It will be run in /etc. For example, &quot;etckeeper vcs diff&quot; will run &quot;git diff&quot;, etc.</p>
<dt><code>uninit [-f]</code></p>
<dd>This command DESTROYS DATA! It is the inverse of the init command, removing VCS information and etckeeper&#8217;s own bookkeeping information from the directory. Use with caution. A typical use case would be to run etckeeper uninit, then modify etckeeper.conf to use a different VCS, and then run etckeeper init. (The -f switch can be used to force uninit without prompting.)</dl>
<h2>Files</h2>
<p>/etc/etckeeper/etckeeper.conf is the configuration file. </p>
<p> /etc/etckeeper also contains directories containing the programs that are run for each of the above commands.</p>
<h2>Environment Variables</h2>
<p>ETCKEEPER_CONF_DIR path to configuration directory instead of default /etc/etckeeper.</p>
<h2>See Also</h2>
<p>/usr/share/doc/etckeeper/README.md.gz</p>
<h2>Author</h2>
<p>Joey Hess &lt;id [at] joeyh.name&gt;</p>
