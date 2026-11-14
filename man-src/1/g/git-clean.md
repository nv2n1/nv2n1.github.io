---
title: "git-clean(1)"
name: "git-clean"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-clean/"
description: "git-clean – Remove untracked files from the working tree"
---

<h2 class="name">NAME</h2>
<p> git-clean &#8211; Remove untracked files from the working tree </p>
<h2>SYNOPSIS</h2>
<pre><code>
git clean[-d][-f][-i][-n][-q][-e&lt;pattern&gt;][-x | -X][--]&lt;path&gt;...
</code></pre>
<h2>DESCRIPTION</h2>
<p> Cleans the working tree by recursively removing files that are not under version control, starting from the current directory. </p>
<p> Normally, only files unknown to Git are removed, but if the <code>-x</code> option is specified, ignored files are also removed. This can, for example, be useful to remove all build products. </p>
<p> If any optional <code>&lt;path&gt;&#8230;</code> arguments are given, only those paths are affected.</p>
<h2>OPTIONS</h2>
<p> -d</p>
<dl>
<dt>
<dd> Normally, when no &lt;path&gt; is specified, git clean will not recurse into untracked directories to avoid removing too much. Specify -d to have it recurse into such directories as well. If any paths are specified, -d is irrelevant; all untracked files matching the specified paths (with exceptions for nested git directories mentioned under <code>&#8211;force</code>) will be removed.</dl>
<p> -f, &#8211;force</p>
<dl>
<dt>
<dd> If the Git configuration variable clean.requireForce is not set to false, <i>git clean</i> will refuse to delete files or directories unless given -f or -i. Git will refuse to modify untracked nested git repositories (directories with a .git subdirectory) unless a second -f is given.</dl>
<p> -i, &#8211;interactive</p>
<dl>
<dt>
<dd> Show what would be done and clean files interactively. See &#8220;Interactive mode&#8221; for details.</dl>
<p> -n, &#8211;dry-run</p>
<dl>
<dt>
<dd> Don&#8217;t actually remove anything, just show what would be done.</dl>
<p> -q, &#8211;quiet</p>
<dl>
<dt>
<dd> Be quiet, only report errors, but not the files that are successfully removed.</dl>
<p> -e &lt;pattern&gt;, &#8211;exclude=&lt;pattern&gt;</p>
<dl>
<dt>
<dd> Use the given exclude pattern in addition to the standard ignore rules (see <code><a href="/docs/linux/man/5-gitignore/">gitignore</a></code>(5)).</dl>
<p> -x</p>
<dl>
<dt>
<dd> Don&#8217;t use the standard ignore rules (see <code><a href="/docs/linux/man/5-gitignore/">gitignore</a></code>(5)), but still use the ignore rules given with <code>-e</code> options from the command line. This allows removing all untracked files, including build products. This can be used (possibly in conjunction with <i>git restore</i> or <i>git reset</i>) to create a pristine working directory to test a clean build.</dl>
<p> -X</p>
<dl>
<dt>
<dd> Remove only files ignored by Git. This may be useful to rebuild everything from scratch, but keep manually created files.</dl>
<h2>INTERACTIVE MODE</h2>
<p> When the command enters the interactive mode, it shows the files and directories to be cleaned, and goes into its interactive command loop. </p>
<p> The command loop shows the list of subcommands available, and gives a prompt &quot;What now&gt; &quot;. In general, when the prompt ends with a single <i>&gt;</i>, you can pick only one of the choices given and type return, like this: </p>
<dl>
<dt>
<dd>
<pre>
    *** Commands ***
        1: clean                2: filter by pattern    3: select by numbers
        4: ask each             5: quit                 6: help
    What now&gt; 1
</pre>
</dl>
<p> You also could say <code>c</code> or <code>clean</code> above as long as the choice is unique. </p>
<p> The main command loop has 6 subcommands. </p>
<p> clean</p>
<dl>
<dt>
<dd> Start cleaning files and directories, and then quit.</dl>
<p> filter by pattern</p>
<dl>
<dt>
<dd> This shows the files and directories to be deleted and issues an &quot;Input ignore patterns&gt;&gt;&quot; prompt. You can input space-separated patterns to exclude files and directories from deletion. E.g. &quot;*.c *.h&quot; will excludes files end with &quot;.c&quot; and &quot;.h&quot; from deletion. When you are satisfied with the filtered result, press ENTER (empty) back to the main menu.</dl>
<p> select by numbers</p>
<dl>
<dt>
<dd> This shows the files and directories to be deleted and issues an &quot;Select items to delete&gt;&gt;&quot; prompt. When the prompt ends with double <i>&gt;&gt;</i> like this, you can make more than one selection, concatenated with whitespace or comma. Also you can say ranges. E.g. &quot;2-5 7,9&quot; to choose 2,3,4,5,7,9 from the list. If the second number in a range is omitted, all remaining items are selected. E.g. &quot;7-&quot; to choose 7,8,9 from the list. You can say <i>*</i> to choose everything. Also when you are satisfied with the filtered result, press ENTER (empty) back to the main menu.</dl>
<p> ask each</p>
<dl>
<dt>
<dd> This will start to clean, and you must confirm one by one in order to delete items. Please note that this action is not as efficient as the above two actions.</dl>
<p> quit</p>
<dl>
<dt>
<dd> This lets you quit without do cleaning.</dl>
<p> help</p>
<dl>
<dt>
<dd> Show brief usage of interactive git-clean.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-gitignore/">gitignore</a></code>(5)</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
