---
title: "git-cola(1)"
name: "git-cola"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-cola/"
description: "git-cola – A highly caffeinated Git GUI"
---

<h2 class="name">NAME</h2>
<p> git-cola &#8211; A highly caffeinated Git GUI </p>
<h2>SYNOPSIS</h2>
<p> <i>git cola</i> [options]</p>
<h2>DESCRIPTION</h2>
<p> <i>git-cola</i> is a powerful Git GUI written in Python. It has many unique features that make Gitcqs advanced features simple and accessible. </p>
<p> See below for a full list of options and usage information.</p>
<h2>OPTIONS</h2>
<p> &#8211;repo=&lt;path&gt;</p>
<dl>
<dt>
<dd> Run <i>git-cola</i> on the git repository in &lt;path&gt;.</dl>
<p> &#8211;style=&lt;style&gt;</p>
<dl>
<dt>
<dd> Launch <i>git-cola</i> with a different stylesheet.</dl>
<p> &#8211;classic</p>
<dl>
<dt>
<dd> Launch the standalone <i>cola classic</i> tool.</dl>
<h2>GUI STYLES</h2>
<p> <i>git-cola</i> ships with an alternate &quot;dark&quot; stylesheet. Specify &#8211;style=dark or provide an external stylesheet with &#8211;style=PATH.</p>
<h2>CONFIG VARIABLES</h2>
<p> cola.savewindowsettings</p>
<dl>
<dt>
<dd> Whether <i>git-cola</i> should remember its window settings.</dl>
<p> cola.fontdiff</p>
<dl>
<dt>
<dd> Specifies the font to use for <i>git-cola</i>&#8216;s diff display.</dl>
<p> gui.diffcontext</p>
<dl>
<dt>
<dd> The number of diff context lines used and displayed by <i>git-cola</i></dl>
<p> gui.editor</p>
<dl>
<dt>
<dd> The default text editor is controlled by gui.editor. The config variable overrides the EDITOR environment variable.</dl>
<p> gui.historybrowser</p>
<dl>
<dt>
<dd> Specifies the history browser to use when visualizing history.</dl>
<p> diff.tool</p>
<dl>
<dt>
<dd> The default diff tool to use. The config variable overrides the GIT_DIFF_TOOL environment variable.</dl>
<p> merge.tool</p>
<dl>
<dt>
<dd> The default merge tool to use. The config variable overrides the GIT_MERGE_TOOL environment variable.</dl>
<p> user.email</p>
<dl>
<dt>
<dd> Your email address to be recorded in any newly created commits. Can be overridden by the <i>GIT_AUTHOR_EMAIL</i>, <i>GIT_COMMITTER_EMAIL</i>, and <i>EMAIL</i> environment variables. See linkgit:git-commit-tree[1].</dl>
<p> user.name</p>
<dl>
<dt>
<dd> Your full name to be recorded in any newly created commits. Can be overridden by the <i>GIT_AUTHOR_NAME</i> and <i>GIT_COMMITTER_NAME</i> environment variables. See linkgit:git-commit-tree[1].</dl>
<p> See linkgit:git-config[1] for more details.</p>
<h2>ENVIRONMENT VARIABLES</h2>
<p> EDITOR</p>
<dl>
<dt>
<dd> Specifies the default editor to use. This is ignored when the git config variable gui.editor is defined.</dl>
<p> GIT_DIFF_TOOL</p>
<dl>
<dt>
<dd> Specifies the default diff tool to use. This is ignored when the git config variable diff.tool is defined.</dl>
<p> GIT_MERGE_TOOL</p>
<dl>
<dt>
<dd> Specifies the default merge tool to use. This is ignored when the git config variable merge.tool is defined.</dl>
<h2>SOURCE</h2>
<p> A <i>git-cola</i> development repository can be obtained via git: </p>
<dl>
<dt>
<dd>
<pre>
git clone <a href="git://github.com/davvid/git-cola.git">git://github.com/davvid/git-cola.git</a>
</pre>
</dl>
<h2>STYLESHEETS</h2>
<p> git-cola ships with an alternative stylesheet called <i>dark</i>. You can use this stylesheet by running git cola &#8211;style=dark. </p>
<p> You can also skin git-cola by providing your own Qt stylesheet. E.g. git cola &#8211;style=/path/to/style.qss. </p>
<p> Built-in styles can be found in /usr/share/git-cola/styles.</p>
<h2>LINKS</h2>
<p> <i>git-cola</i> homepage</p>
<dl>
<dt>
<dd> m[blue]<code><a rel="nofollow" href="http://cola.tuxfamily.org/">http://cola.tuxfamily.org/</a></code>m[]</dl>
<p> <i>git-cola</i> sources on github</p>
<dl>
<dt>
<dd> m[blue]<code><a rel="nofollow" href="http://github.com/davvid/git-cola/tree/master">http://github.com/davvid/git-cola/tree/master</a></code>m[]</dl>
<h2>SEE ALSO</h2>
<p> linkgit:git-difftool[1]</p>
<dl>
<dt>
<dd> Compare changes using common merge tools. (New in git-1.6.3).</dl>
<p> linkgit:gitk[1]</p>
<dl>
<dt>
<dd> The git repository browser. Shows branches, commit history and file differences. gitk is the utility started by <i>git-cola</i>&#8216;s Repository Visualize actions.</dl>
<h2>GIT</h2>
<p> <i>git-cola</i> is independently developed from the linkgit:git[7] suite, but you can use it just like any other git command, e.g. git cola.</p>
<h2>AUTHOR</h2>
<p> Written by David Aguilar &lt;m[blue]<code>davvid [at] gmail.com</code>m[]<font SIZE="-2">[1]</font>&gt;.</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> davvid [at] gmail.com</p>
<dl>
<dt>
<dd> mailto:davvid [at] gmail.com</dl>
</dl>
<h2>Index</h2>
