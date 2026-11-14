---
title: "gitcli(7)"
name: "gitcli"
section: "7"
letter: "g"
url: "/docs/linux/man/7-gitcli/"
description: "gitcli – Git command-line interface and conventions"
---

<p>gitcli &#8211; Git command-line interface and conventions</p>
<h2>Synopsis</h2>
<p>gitcli</p>
<h2>Description</h2>
<p>This manual describes the convention used throughout Git CLI. </p>
<p> Many commands take revisions (most often &quot;commits&quot;, but sometimes &quot;tree-ish&quot;, depending on the context and command) and paths as their arguments. Here are the rules: </p>
<dl>
<dd>&bull; Revisions come first and then paths. E.g. in <code>git diff v1.0 v2.0 arch/x86 include/asm-x86</code>, <code>v1.0</code> and <code>v2.0</code> are revisions and <code>arch/x86</code> and <code>include/asm-x86</code> are paths.</dl>
<dl>
<dd>&bull; When an argument can be misunderstood as either a revision or a path, they can be disambiguated by placing <code>&#8212;</code> between them. E.g. <code>git diff &#8212; HEAD</code> is, &quot;I have a file called HEAD in my work tree. Please show changes between the version I staged in the index and what I have in the work tree for that file&quot;, not &quot;show difference between the HEAD commit and the work tree as a whole&quot;. You can say <code>git diff HEAD &#8212;</code> to ask for the latter.</dl>
<dl>
<dd>&bull; Without disambiguating <code>&#8212;</code>, Git makes a reasonable guess, but errors out and asking you to disambiguate when ambiguous. E.g. if you have a file called HEAD in your work tree, <code>git diff HEAD</code> is ambiguous, and you have to say either <code>git diff HEAD &#8212;</code> or <code>git diff &#8212; HEAD</code> to disambiguate.</dl>
<dl>
<dd>&bull; Because <code>&#8212;</code> disambiguates revisions and paths in some commands, it cannot be used for those commands to separate options and revisions. You can use <code>&#8211;end-of-options</code> for this (it also works for commands that do not distinguish between revisions in paths, in which case it is simply an alias for <code>&#8212;</code>). </p>
<p> When writing a script that is expected to handle random user-input, it is a good practice to make it explicit which arguments are which by placing disambiguating <code>&#8212;</code> at appropriate places.</dl>
<dl>
<dd>&bull; Many commands allow wildcards in paths, but you need to protect them from getting globbed by the shell. These two mean different things: </p>
<dl>
<dd>
<pre>$ git restore *.c
$ git restore \*.c</pre>
</dl>
<p> The former lets your shell expand the fileglob, and you are asking the dot-C files in your working tree to be overwritten with the version in the index. The latter passes the <code>*.c</code> to Git, and you are asking the paths in the index that match the pattern to be checked out to your working tree. After running <code>git add hello.c; rm hello.c</code>, you will <i>not</i> see <code>hello.c</code> in your working tree with the former, but with the latter you will.</dl>
<dl>
<dd>&bull; Just as the filesystem <i>.</i> (period) refers to the current directory, using a <i>.</i> as a repository name in Git (a dot-repository) is a relative path and means your current repository.</dl>
<p> Here are the rules regarding the &quot;flags&quot; that you should follow when you are scripting Git: </p>
<dl>
<dd>&bull; it&#8217;s preferred to use the non-dashed form of Git commands, which means that you should prefer <code>git foo</code> to <code>git-foo</code>.</dl>
<dl>
<dd>&bull; splitting short options to separate words (prefer <code>git foo -a -b</code> to <code>git foo -ab</code>, the latter may not even work).</dl>
<dl>
<dd>&bull; when a command-line option takes an argument, use the <i>stuck</i> form. In other words, write <code>git foo -oArg</code> instead of <code>git foo -o Arg</code> for short options, and <code>git foo &#8211;long-opt=Arg</code> instead of <code>git foo &#8211;long-opt Arg</code> for long options. An option that takes optional option-argument must be written in the <i>stuck</i> form.</dl>
<dl>
<dd>&bull; when you give a revision parameter to a command, make sure the parameter is not ambiguous with a name of a file in the work tree. E.g. do not write <code>git log -1 HEAD</code> but write <code>git log -1 HEAD &#8212;</code>; the former will not work if you happen to have a file called <code>HEAD</code> in the work tree.</dl>
<dl>
<dd>&bull; many commands allow a long option <code>&#8211;option</code> to be abbreviated only to their unique prefix (e.g. if there is no other option whose name begins with <code>opt</code>, you may be able to spell <code>&#8211;opt</code> to invoke the <code>&#8211;option</code> flag), but you should fully spell them out when writing your scripts; later versions of Git may introduce a new option whose name shares the same prefix, e.g. <code>&#8211;optimize</code>, to make a short prefix that used to be unique no longer unique.</dl>
<h2>Enhanced Option Parser</h2>
<p>From the Git 1.5.4 series and further, many Git commands (not all of them at the time of the writing though) come with an enhanced option parser. </p>
<p> Here is a list of the facilities provided by this option parser.</p>
<h3>Magic Options</h3>
<p>Commands which have the enhanced option parser activated all understand a couple of magic command-line options: </p>
<p> -h</p>
<dl>
<dd>gives a pretty printed usage of the command. </p>
<dl>
<dd>
<pre>$ git describe -h
usage: git describe [&lt;options&gt;] &lt;commit-ish&gt;*
 or: git describe [&lt;options&gt;] --dirty
 --contains find the tag that comes after the commit
 --debug debug search strategy on stderr
 --all use any ref
 --tags use any tag, even unannotated
 --long always use long format
 --abbrev[=&lt;n&gt;] use &lt;n&gt; digits to display SHA-1s</pre>
</dl>
<p> Note that some subcommand (e.g. <code>git grep</code>) may behave differently when there are things on the command line other than <code>-h</code>, but <code>git subcmd -h</code> without anything else on the command line is meant to consistently give the usage.</dl>
<p> &#8211;help-all</p>
<dl>
<dd>Some Git commands take options that are only used for plumbing or that are deprecated, and such options are hidden from the default usage. This option gives the full list of options.</dl>
<h3>Negating options</h3>
<p>Options with long option names can be negated by prefixing <code>&#8211;no-</code>. For example, <code>git branch</code> has the option <code>&#8211;track</code> which is <i>on</i> by default. You can use <code>&#8211;no-track</code> to override that behaviour. The same goes for <code>&#8211;color</code> and <code>&#8211;no-color</code>.</p>
<h3>Aggregating short options</h3>
<p>Commands that support the enhanced option parser allow you to aggregate short options. This means that you can for example use <code>git rm -rf</code> or <code>git clean -fdx</code>.</p>
<h3>Abbreviating long options</h3>
<p>Commands that support the enhanced option parser accepts unique prefix of a long option as if it is fully spelled out, but use this with a caution. For example, <code>git commit &#8211;amen</code> behaves as if you typed <code>git commit &#8211;amend</code>, but that is true only until a later version of Git introduces another option that shares the same prefix, e.g. <code>git commit &#8211;amenity</code> option.</p>
<h3>Separating argument from the option</h3>
<p>You can write the mandatory option parameter to an option as a separate word on the command line. That means that all the following uses work: </p>
<dl>
<dd>
<pre>$ git foo --long-opt=Arg
$ git foo --long-opt Arg
$ git foo -oArg
$ git foo -o Arg</pre>
</dl>
<p> However, this is <code>NOT</code> allowed for switches with an optional value, where the <i>stuck</i> form must be used: </p>
<dl>
<dd>
<pre>$ git describe --abbrev HEAD # correct
$ git describe --abbrev=10 HEAD # correct
$ git describe --abbrev 10 HEAD # NOT WHAT YOU MEANT</pre>
</dl>
<h2>Notes On Frequently Confused Options</h2>
<p>Many commands that can work on files in the working tree and/or in the index can take <code>&#8211;cached</code> and/or <code>&#8211;index</code> options. Sometimes people incorrectly think that, because the index was originally called cache, these two are synonyms. They are <code>not</code> &#8212; these two options mean very different things. </p>
<dl>
<dd>&bull; The <code>&#8211;cached</code> option is used to ask a command that usually works on files in the working tree to <code>only</code> work with the index. For example, <code>git grep</code>, when used without a commit to specify from which commit to look for strings in, usually works on files in the working tree, but with the <code>&#8211;cached</code> option, it looks for strings in the index.</dl>
<dl>
<dd>&bull; The <code>&#8211;index</code> option is used to ask a command that usually works on files in the working tree to <code>also</code> affect the index. For example, <code>git stash apply</code> usually merges changes recorded in a stash entry to the working tree, but with the <code>&#8211;index</code> option, it also merges changes to the index as well.</dl>
<p> <code>git apply</code> command can be used with <code>&#8211;cached</code> and <code>&#8211;index</code> (but not at the same time). Usually the command only affects the files in the working tree, but with <code>&#8211;index</code>, it patches both the files and their index entries, and with <code>&#8211;cached</code>, it modifies only the index entries. </p>
<p> See also m[blue]<code><a rel="nofollow" href="https://lore.kernel.org/git/7v64clg5u9.fsf@assigned-by-dhcp.cox.net/">https://lore.kernel.org/git/7v64clg5u9.fsf@assigned-by-dhcp.cox.net/</a></code>m[] and m[blue]<code><a rel="nofollow" href="https://lore.kernel.org/git/7vy7ej9g38.fsf@gitster.siamese.dyndns.org/">https://lore.kernel.org/git/7vy7ej9g38.fsf@gitster.siamese.dyndns.org/</a></code>m[] for further information. </p>
<p> Some other commands that also work on files in the working tree and/or in the index can take <code>&#8211;staged</code> and/or <code>&#8211;worktree</code>. </p>
<dl>
<dd>&bull; <code>&#8211;staged</code> is exactly like <code>&#8211;cached</code>, which is used to ask a command to only work on the index, not the working tree.</dl>
<dl>
<dd>&bull; <code>&#8211;worktree</code> is the opposite, to ask a command to work on the working tree only, not the index.</dl>
<dl>
<dd>&bull; The two options can be specified together to ask a command to work on both the index and the working tree.</dl>
<h2>Git</h2>
<p>Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite</p>
