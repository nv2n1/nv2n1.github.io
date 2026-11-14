---
title: "git-show-ref(1)"
name: "git-show-ref"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-show-ref/"
description: "git-show-ref – List references in a local repository"
---

<h2 class="name">NAME</h2>
<p> git-show-ref &#8211; List references in a local repository </p>
<h2>SYNOPSIS</h2>
<pre><code>
git show - ref[-q | --quiet][--verify][--head][-d | --dereference][-s | --hash[=&lt;n&gt;]][--abbrev[=&lt;n&gt;]][--tags][--heads][--][&lt;pattern&gt;...] git show - ref-- exclude - existing[=&lt;pattern&gt;]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Displays references available in a local repository along with the associated commit IDs. Results can be filtered using a pattern and tags can be dereferenced into object IDs. Additionally, it can be used to test whether a particular ref exists. </p>
<p> By default, shows the tags, heads, and remote refs. </p>
<p> The &#8211;exclude-existing form is a filter that does the inverse. It reads refs from stdin, one ref per line, and shows those that don&#8217;t exist in the local repository. </p>
<p> Use of this utility is encouraged in favor of directly accessing files under the <code>.git</code> directory.</p>
<h2>OPTIONS</h2>
<p> &#8211;head</p>
<dl>
<dt>
<dd> Show the HEAD reference, even if it would normally be filtered out.</dl>
<p> &#8211;heads, &#8211;tags</p>
<dl>
<dt>
<dd> Limit to &quot;refs/heads&quot; and &quot;refs/tags&quot;, respectively. These options are not mutually exclusive; when given both, references stored in &quot;refs/heads&quot; and &quot;refs/tags&quot; are displayed.</dl>
<p> -d, &#8211;dereference</p>
<dl>
<dt>
<dd> Dereference tags into object IDs as well. They will be shown with &quot;^{}&quot; appended.</dl>
<p> -s, &#8211;hash[=&lt;n&gt;]</p>
<dl>
<dt>
<dd> Only show the SHA-1 hash, not the reference name. When combined with &#8211;dereference the dereferenced tag will still be shown after the SHA-1.</dl>
<p> &#8211;verify</p>
<dl>
<dt>
<dd> Enable stricter reference checking by requiring an exact ref path. Aside from returning an error code of 1, it will also print an error message if <code>&#8211;quiet</code> was not specified.</dl>
<p> &#8211;abbrev[=&lt;n&gt;]</p>
<dl>
<dt>
<dd> Abbreviate the object name. When using <code>&#8211;hash</code>, you do not have to say <code>&#8211;hash &#8211;abbrev</code>; <code>&#8211;hash=n</code> would do.</dl>
<p> -q, &#8211;quiet</p>
<dl>
<dt>
<dd> Do not print any results to stdout. When combined with <code>&#8211;verify</code> this can be used to silently check if a reference exists.</dl>
<p> &#8211;exclude-existing[=&lt;pattern&gt;]</p>
<dl>
<dt>
<dd> Make <i>git show-ref</i> act as a filter that reads refs from stdin of the form &quot;<code>^(?:&lt;anything&gt;\s)?&lt;refname&gt;(?:\^{})?$</code>&quot; and performs the following actions on each: (1) strip &quot;^{}&quot; at the end of line if any; (2) ignore if pattern is provided and does not head-match refname; (3) warn if refname is not a well-formed refname and skip; (4) ignore if refname is a ref that exists in the local repository; (5) otherwise output the line.</dl>
<p> &lt;pattern&gt;&#8230;</p>
<dl>
<dt>
<dd> Show references matching one or more patterns. Patterns are matched from the end of the full name, and only complete parts are matched, e.g. <i>master</i> matches <i>refs/heads/master</i>, <i>refs/remotes/origin/master</i>, <i>refs/tags/jedi/master</i> but not <i>refs/heads/mymaster</i> or <i>refs/remotes/master/jedi</i>.</dl>
<h2>OUTPUT</h2>
<p> The output is in the format: <i>&lt;SHA-1 ID&gt;</i> <i>&lt;space&gt;</i> <i>&lt;reference name&gt;</i>. </p>
<dl>
<dt>
<dd>
$ git show &#8211; ref&#8211; head&#8211; dereference 832e76a9899f560a90ffd62ae2ce83bbeff58f54 HEAD 832e76a9899f560a90ffd62ae2ce83bbeff58f54 refs / heads / master 832e76a9899f560a90ffd62ae2ce83bbeff58f54 refs / heads / origin 3521017556c5de4159da4615a39fa4d5d2c279b5 refs / tags / v0 .99.9c 6ddc0964034342519a87fe013781abf31c6db6ad refs / tags / v0 .99.9c ^ {} 055e4ae3ae6eb344cbabf2a5256a49ea66040131 refs / tags / v1 .0rc4 423325a2d24638ddcc82ce47be5e40be550f4507 refs / tags / v1 .0rc4 ^ {}&#8230;
</dl>
<p> When using &#8211;hash (and not &#8211;dereference) the output format is: <i>&lt;SHA-1 ID&gt;</i> </p>
<dl>
<dt>
<dd>
<pre>
$ git show-ref --heads --hash
2e3ba0114a1f52b47df29743d6915d056be13278
185008ae97960c8d551adcd9e23565194651b5d1
03adf42c988195b50e1a1935ba5fcbc39b2b029b
...
</pre>
</dl>
<h2>EXAMPLES</h2>
<p> To show all references called &quot;master&quot;, whether tags or heads or anything else, and regardless of how deep in the reference naming hierarchy they are, use: </p>
<dl>
<dt>
<dd>
<pre>
        git show-ref master
</pre>
</dl>
<p> This will show &quot;refs/heads/master&quot; but also &quot;refs/remote/other-repo/master&quot;, if such references exists. </p>
<p> When using the <code>&#8211;verify</code> flag, the command requires an exact path: </p>
<dl>
<dt>
<dd>
<pre>
        git show-ref --verify refs/heads/master
</pre>
</dl>
<p> will only match the exact branch called &quot;master&quot;. </p>
<p> If nothing matches, <i>git show-ref</i> will return an error code of 1, and in the case of verification, it will show an error message. </p>
<p> For scripting, you can ask it to be quiet with the &quot;&#8211;quiet&quot; flag, which allows you to do things like </p>
<dl>
<dt>
<dd>
<pre><code>
git show - ref-- quiet-- verify-- "refs/heads/$headname" ||
    echo "$headname is not a valid branch"
</code></pre>
</dl>
<p> to check whether a particular branch exists or not (notice how we don&#8217;t actually want to show any results, and we want to use the full refname for it in order to not trigger the problem with ambiguous partial matches). </p>
<p> To show only tags, or only proper branch heads, use &quot;&#8211;tags&quot; and/or &quot;&#8211;heads&quot; respectively (using both means that it shows tags and heads, but not other random references under the refs/ subdirectory). </p>
<p> To do automatic tag object dereferencing, use the &quot;-d&quot; or &quot;&#8211;dereference&quot; flag, so you can do </p>
<dl>
<dt>
<dd>
<pre>
        git show-ref --tags --dereference
</pre>
</dl>
<p> to get a listing of all tags together with what they dereference.</p>
<h2>FILES</h2>
<p> <code>.git/refs/*</code>, <code>.git/packed-refs</code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-git-for-each-ref/">git-for-each-ref</a></code>(1), <code><a href="/docs/linux/man/1-git-ls-remote/">git-ls-remote</a></code>(1), <code><a href="/docs/linux/man/1-git-update-ref/">git-update-ref</a></code>(1), <code><a href="/docs/linux/man/5-gitrepository-layout/">gitrepository-layout</a></code>(5)</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
