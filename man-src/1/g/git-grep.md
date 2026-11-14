---
title: "git-grep(1)"
name: "git-grep"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-grep/"
description: "git-grep – Print lines matching a pattern"
---

<h2 class="name">NAME</h2>
<p> git-grep &#8211; Print lines matching a pattern </p>
<h2>SYNOPSIS</h2>
<pre><code>
git grep[-a | --text][-I][--textconv][-i | --ignore - case][-w | --word - regexp]
        [-v | --invert - match][-h | -H][--full - name]
        [-E | --extended - regexp][-G | --basic - regexp]
        [-P | --perl - regexp]
        [-F | --fixed - strings][-n | --line - number][--column]
        [-l | --files - with - matches][-L | --files - without - match]
        [(-O | --open - files - in - pager)[&lt;pager&gt;]]
        [-z | --null]
        [-o | --only - matching][-c | --count][--all - match][-q | --quiet]
        [--max - depth&lt;depth&gt;][--[no - ] recursive]
        [--color[=&lt;when&gt;] | --no - color]
        [--break][--heading][-p | --show - function]
        [-A&lt;post - context&gt;][-B&lt;pre - context&gt;][-C&lt;context&gt;]
        [-W | --function - context]
        [--threads&lt;num&gt;]
        [-f&lt;file&gt;][-e]&lt;pattern&gt;[--and | -- or | --not | (|) | -e&lt;pattern&gt;...]
                               [--recurse - submodules][--parent - basename&lt;basename&gt;]
                               [[--[no - ] exclude - standard][--cached | --no - index | --untracked] | &lt;tree&gt;...]
                               [--][&lt;pathspec&gt;...]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Look for specified patterns in the tracked files in the work tree, blobs registered in the index file, or blobs in given tree objects. Patterns are lists of one or more search expressions separated by newline characters. An empty string as search expression matches all lines.</p>
<h2>OPTIONS</h2>
<p> &#8211;cached</p>
<dl>
<dt>
<dd> Instead of searching tracked files in the working tree, search blobs registered in the index file.</dl>
<p> &#8211;no-index</p>
<dl>
<dt>
<dd> Search files in the current directory that is not managed by Git.</dl>
<p> &#8211;untracked</p>
<dl>
<dt>
<dd> In addition to searching in the tracked files in the working tree, search also in untracked files.</dl>
<p> &#8211;no-exclude-standard</p>
<dl>
<dt>
<dd> Also search in ignored files by not honoring the <code>.gitignore</code> mechanism. Only useful with <code>&#8211;untracked</code>.</dl>
<p> &#8211;exclude-standard</p>
<dl>
<dt>
<dd> Do not pay attention to ignored files specified via the <code>.gitignore</code> mechanism. Only useful when searching files in the current directory with <code>&#8211;no-index</code>.</dl>
<p> &#8211;recurse-submodules</p>
<dl>
<dt>
<dd> Recursively search in each submodule that is active and checked out in the repository. When used in combination with the &lt;tree&gt; option the prefix of all submodule output will be the name of the parent project&#8217;s &lt;tree&gt; object. This option has no effect if <code>&#8211;no-index</code> is given.</dl>
<p> -a, &#8211;text</p>
<dl>
<dt>
<dd> Process binary files as if they were text.</dl>
<p> &#8211;textconv</p>
<dl>
<dt>
<dd> Honor textconv filter settings.</dl>
<p> &#8211;no-textconv</p>
<dl>
<dt>
<dd> Do not honor textconv filter settings. This is the default.</dl>
<p> -i, &#8211;ignore-case</p>
<dl>
<dt>
<dd> Ignore case differences between the patterns and the files.</dl>
<p> -I</p>
<dl>
<dt>
<dd> Don&#8217;t match the pattern in binary files.</dl>
<p> &#8211;max-depth &lt;depth&gt;</p>
<dl>
<dt>
<dd> For each &lt;pathspec&gt; given on command line, descend at most &lt;depth&gt; levels of directories. A value of -1 means no limit. This option is ignored if &lt;pathspec&gt; contains active wildcards. In other words if &quot;a*&quot; matches a directory named &quot;a*&quot;, &quot;*&quot; is matched literally so &#8211;max-depth is still effective.</dl>
<p> -r, &#8211;recursive</p>
<dl>
<dt>
<dd> Same as <code>&#8211;max-depth=-1</code>; this is the default.</dl>
<p> &#8211;no-recursive</p>
<dl>
<dt>
<dd> Same as <code>&#8211;max-depth=0</code>.</dl>
<p> -w, &#8211;word-regexp</p>
<dl>
<dt>
<dd> Match the pattern only at word boundary (either begin at the beginning of a line, or preceded by a non-word character; end at the end of a line or followed by a non-word character).</dl>
<p> -v, &#8211;invert-match</p>
<dl>
<dt>
<dd> Select non-matching lines.</dl>
<p> -h, -H</p>
<dl>
<dt>
<dd> By default, the command shows the filename for each match. <code>-h</code> option is used to suppress this output. <code>-H</code> is there for completeness and does not do anything except it overrides <code>-h</code> given earlier on the command line.</dl>
<p> &#8211;full-name</p>
<dl>
<dt>
<dd> When run from a subdirectory, the command usually outputs paths relative to the current directory. This option forces paths to be output relative to the project top directory.</dl>
<p> -E, &#8211;extended-regexp, -G, &#8211;basic-regexp</p>
<dl>
<dt>
<dd> Use POSIX extended/basic regexp for patterns. Default is to use basic regexp.</dl>
<p> -P, &#8211;perl-regexp</p>
<dl>
<dt>
<dd> Use Perl-compatible regular expressions for patterns. </p>
<p> Support for these types of regular expressions is an optional compile-time dependency. If Git wasn&#8217;t compiled with support for them providing this option will cause it to die.</dl>
<p> -F, &#8211;fixed-strings</p>
<dl>
<dt>
<dd> Use fixed strings for patterns (don&#8217;t interpret pattern as a regex).</dl>
<p> -n, &#8211;line-number</p>
<dl>
<dt>
<dd> Prefix the line number to matching lines.</dl>
<p> &#8211;column</p>
<dl>
<dt>
<dd> Prefix the 1-indexed byte-offset of the first match from the start of the matching line.</dl>
<p> -l, &#8211;files-with-matches, &#8211;name-only, -L, &#8211;files-without-match</p>
<dl>
<dt>
<dd> Instead of showing every matched line, show only the names of files that contain (or do not contain) matches. For better compatibility with <i>git diff</i>, <code>&#8211;name-only</code> is a synonym for <code>&#8211;files-with-matches</code>.</dl>
<p> -O[&lt;pager&gt;], &#8211;open-files-in-pager[=&lt;pager&gt;]</p>
<dl>
<dt>
<dd> Open the matching files in the pager (not the output of <i>grep</i>). If the pager happens to be &quot;less&quot; or &quot;vi&quot;, and the user specified only one pattern, the first file is positioned at the first match automatically. The <code>pager</code> argument is optional; if specified, it must be stuck to the option without a space. If <code>pager</code> is unspecified, the default pager will be used (see <code>core.pager</code> in <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)).</dl>
<p> -z, &#8211;null</p>
<dl>
<dt>
<dd> Use 
