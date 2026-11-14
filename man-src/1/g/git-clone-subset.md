---
title: "git-clone-subset(1)"
name: "git-clone-subset"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-clone-subset/"
description: "git-clone-subset – Clones a subset of a git repository"
---

<h2 class="name">NAME</h2>
<p> git-clone-subset &#8211; Clones a subset of a git repository </p>
<h2>SYNOPSIS</h2>
<p> <code>git-clone-subset</code> [<i>options</i>] <i>repository destination-dir pattern</i></p>
<h2>DESCRIPTION</h2>
<p> Clones a <i>repository</i> into a <i>destination-dir</i> and runs on the clone<br />
 <code>git filter-branch &#8211;prune-empty &#8211;tree-filter &#8216;git rm &#8230;&#8217; &#8212; &#8211;all</code><br />
 to prune from history all files except the ones matching <i>pattern</i>, effectively creating a clone with a subset of files (and history) of the original repository. </p>
<p> Useful for creating a new repository out of a set of files from another repository, migrating (only) their associated history. Very similar to what<br />
 <code>git filter-branch &#8211;subdirectory-filter</code><br />
 does, but for a file pattern instead of just a single directory.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>,<code>&nbsp;<wbr>&#8211;help</code></p>
<dd> show usage information.</p>
<dt><i>repository</i></p>
<dd> URL or local path to the git repository to be cloned.</p>
<dt><i>destination-dir</i></p>
<dd> Directory to create the clone. Same rules for git-clone applies: it will be created if it does not exist and it must be empty otherwise. But, unlike git-clone, this argument is not optional: git-clone uses several rules to determine the &quot;Humane&quot; dir name of a cloned repo, and git-clone-subset will not risk parse its output, let alone predict the chosen name.</p>
<dt><i>pattern</i></p>
<dd> Glob pattern to match the desired files/dirs. It will be ultimately evaluated by a call to bash, NOT git or sh, using extended glob &#8216;!(&lt;pattern&gt;)&#8217; rule. Quote it or escape it on command line, so it does not get evaluated prematurely by your current shell. Only a single pattern is allowed: if more are required, use extglob&#8217;s &quot;|&quot; syntax. Globs will be evaluated with bash&#8217;s shopt dotglob set, so beware. Patterns should not contain spaces or special chars like &quot; &#8216; $ ( ) { } `, not even quoted or escaped, since that might interphere with the !() syntax after pattern expansion. </p>
<p> Pattern Examples: </p>
<p> &quot;*.png&quot;<br />
 &quot;*.png|*icon*&quot;<br />
 &quot;*.h|src/|lib&quot;</dl>
<h2>LIMITATIONS</h2>
<p> Renames are NOT followed. As a workaround, list the rename history with &#8216;git log &#8211;follow &#8211;name-status &#8211;format=&#8217;%H&#8217; &#8212; file | grep &quot;^[RAD]&quot;&#8217; and include all multiple names of a file in the pattern, as in &quot;currentname|oldname|initialname&quot;. As a side efect, if a different file has taken place of an old name, it will be preserved too, and there is no way around this using this tool. </p>
<p> There is no (easy) way to keep some files in a dir: using &#8216;dir/foo*&#8217; as pattern will not work. So keep the whole dir and remove files afterwards, using git filter-branch and a (quite complex) combination of cloning, remote add, rebases, etc. </p>
<p> Pattern matching is quite limited, and many of bash&#8217;s escaping and quoting does not work properly when pattern is expanded inside !().</p>
<h2>SEE ALSO</h2>
<p> <code><a rel="nofollow" href="https://github.com/MestreLion/git-tools">https://github.com/MestreLion/git-tools</a></code></p>
<h2>AUTHOR</h2>
<p> Rodrigo Silva (MestreLion) linux [at] rodrigosilva.com </p>
<h2>Index</h2>
