---
title: "git-check-ref-format(1)"
name: "git-check-ref-format"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-check-ref-format/"
description: "git-check-ref-format – Ensures that a reference name is well formed"
---

<h2 class="name">NAME</h2>
<p> git-check-ref-format &#8211; Ensures that a reference name is well formed </p>
<h2>SYNOPSIS</h2>
<pre><code>
git check - ref - format[--normalize][--[no - ] allow - onelevel][--refspec - pattern]&lt;refname&gt; git check - ref - format-- branch&lt;branchname - shorthand&gt;
</code></pre>
<h2>DESCRIPTION</h2>
<p> Checks if a given <i>refname</i> is acceptable, and exits with a non-zero status if it is not. </p>
<p> A reference is used in Git to specify branches and tags. A branch head is stored in the <code>refs/heads</code> hierarchy, while a tag is stored in the <code>refs/tags</code> hierarchy of the ref namespace (typically in <code>$GIT_DIR/refs/heads</code> and <code>$GIT_DIR/refs/tags</code> directories or, as entries in file <code>$GIT_DIR/packed-refs</code> if refs are packed by <code>git gc</code>). </p>
<p> Git imposes the following rules on how references are named: </p>
<dl>
<dt>
<dd> 1. They can include slash <code>/</code> for hierarchical (directory) grouping, but no slash-separated component can begin with a dot <code>.</code> or end with the sequence <code>.lock</code>.</dl>
<dl>
<dt>
<dd> 2. They must contain at least one <code>/</code>. This enforces the presence of a category like <code>heads/</code>, <code>tags/</code> etc. but the actual names are not restricted. If the <code>&#8211;allow-onelevel</code> option is used, this rule is waived.</dl>
<dl>
<dt>
<dd> 3. They cannot have two consecutive dots <code>..</code> anywhere.</dl>
<dl>
<dt>
<dd> 4. They cannot have ASCII control characters (i.e. bytes whose values are lower than  , or \177 <code>DEL</code>), space, tilde <code>~</code>, caret <code>^</code>, or colon <code>:</code> anywhere.</dl>
<dl>
<dt>
<dd> 5. They cannot have question-mark <code>?</code>, asterisk <code>*</code>, or open bracket <code>[</code> anywhere. See the <code>&#8211;refspec-pattern</code> option below for an exception to this rule.</dl>
<dl>
<dt>
<dd> 6. They cannot begin or end with a slash <code>/</code> or contain multiple consecutive slashes (see the <code>&#8211;normalize</code> option below for an exception to this rule)</dl>
<dl>
<dt>
<dd> 7. They cannot end with a dot <code>.</code>.</dl>
<dl>
<dt>
<dd> 8. They cannot contain a sequence <code>@{</code>.</dl>
<dl>
<dt>
<dd> 9. They cannot be the single character <code>@</code>.</dl>
<dl>
<dt>
<dd> 10. They cannot contain a <code>\</code>.</dl>
<p> These rules make it easy for shell script based tools to parse reference names, pathname expansion by the shell when a reference name is used unquoted (by mistake), and also avoid ambiguities in certain reference name expressions (see <code><a href="/docs/linux/man/7-gitrevisions/">gitrevisions</a></code>(7)): </p>
<dl>
<dt>
<dd> 1. A double-dot <code>..</code> is often used as in <code>ref1..ref2</code>, and in some contexts this notation means <code>^ref1 ref2</code> (i.e. not in <code>ref1</code> and in <code>ref2</code>).</dl>
<dl>
<dt>
<dd> 2. A tilde <code>~</code> and caret <code>^</code> are used to introduce the postfix <i>nth parent</i> and <i>peel onion</i> operation.</dl>
<dl>
<dt>
<dd> 3. A colon <code>:</code> is used as in <code>srcref:dstref</code> to mean &quot;use srcref&#8217;s value and store it in dstref&quot; in fetch and push operations. It may also be used to select a specific object such as with <i>git cat-file</i>: &quot;git cat-file blob v1.3.3:refs.c&quot;.</dl>
<dl>
<dt>
<dd> 4. at-open-brace <code>@{</code> is used as a notation to access a reflog entry.</dl>
<p> With the <code>&#8211;branch</code> option, the command takes a name and checks if it can be used as a valid branch name (e.g. when creating a new branch). But be cautious when using the previous checkout syntax that may refer to a detached HEAD state. The rule <code>git check-ref-format &#8211;branch $name</code> implements may be stricter than what <code>git check-ref-format refs/heads/$name</code> says (e.g. a dash may appear at the beginning of a ref component, but it is explicitly forbidden at the beginning of a branch name). When run with <code>&#8211;branch</code> option in a repository, the input is first expanded for the &#8220;previous checkout syntax&#8221; <code>@{-n}</code>. For example, <code>@{-1}</code> is a way to refer the last thing that was checked out using &quot;git switch&quot; or &quot;git checkout&quot; operation. This option should be used by porcelains to accept this syntax anywhere a branch name is expected, so they can act as if you typed the branch name. As an exception note that, the &#8220;previous checkout operation&#8221; might result in a commit object name when the N-th last thing checked out was not a branch.</p>
<h2>OPTIONS</h2>
<p> &#8211;[no-]allow-onelevel</p>
<dl>
<dt>
<dd> Controls whether one-level refnames are accepted (i.e., refnames that do not contain multiple <code>/</code>-separated components). The default is <code>&#8211;no-allow-onelevel</code>.</dl>
<p> &#8211;refspec-pattern</p>
<dl>
<dt>
<dd> Interpret &lt;refname&gt; as a reference name pattern for a refspec (as used with remote repositories). If this option is enabled, &lt;refname&gt; is allowed to contain a single <code>*</code> in the refspec (e.g., <code>foo/bar*/baz</code> or <code>foo/bar*baz/</code> but not <code>foo/bar*/baz*</code>).</dl>
<p> &#8211;normalize</p>
<dl>
<dt>
<dd> Normalize <i>refname</i> by removing any leading slash (<code>/</code>) characters and collapsing runs of adjacent slashes between name components into a single slash. If the normalized refname is valid then print it to standard output and exit with a status of 0, otherwise exit with a non-zero status. (<code>&#8211;print</code> is a deprecated way to spell <code>&#8211;normalize</code>.)</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd> &bull; Print the name of the previous thing checked out: </p>
<dl>
<dt>
<dd>
<pre>
$ git check-ref-format --branch @{-1}
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; Determine the reference name to use for a new branch: </p>
<dl>
<dt>
<dd>
<pre><code>
$ ref = $(git check - ref - format-- normalize "refs/heads/$newbranch") ||
{
    echo "we do not like '$newbranch' as a branch name." &gt; &amp;2;
    exit 1;
}
</code></pre>
</dl>
</dl>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
