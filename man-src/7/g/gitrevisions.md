---
title: "gitrevisions(7)"
name: "gitrevisions"
section: "7"
letter: "g"
url: "/docs/linux/man/7-gitrevisions/"
description: "gitrevisions – Specifying revisions and ranges for Git"
---

<p>gitrevisions &#8211; Specifying revisions and ranges for Git</p>
<h2>Synopsis</h2>
<p>gitrevisions</p>
<h2>Description</h2>
<p>Many Git commands take revision parameters as arguments. Depending on the command, they denote a specific commit or, for commands which walk the revision graph (such as <code><a href="/docs/linux/man/1-git-log/">git-log</a></code>(1)), all commits which are reachable from that commit. For commands that walk the revision graph one can also specify a range of revisions explicitly. </p>
<p> In addition, some Git commands (such as <code><a href="/docs/linux/man/1-git-show/">git-show</a></code>(1) and <code><a href="/docs/linux/man/1-git-push/">git-push</a></code>(1)) can also take revision parameters which denote other objects than commits, e.g. blobs (&quot;files&quot;) or trees (&quot;directories of files&quot;).</p>
<h2>Specifying Revisions</h2>
<p>A revision parameter <i>&lt;rev&gt;</i> typically, but not necessarily, names a commit object. It uses what is called an <i>extended SHA-1</i> syntax. Here are various ways to spell object names. The ones listed near the end of this list name trees and blobs contained in a commit. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font> </p>
<p> This document shows the &quot;raw&quot; syntax as seen by git. The shell and other UIs might require additional quoting to protect special characters and to avoid word splitting. </p>
</dl>
<p> <i>&lt;sha1&gt;</i>, e.g. <i>dae86e1950b1277e545cee180551750029cfe735</i>, <i>dae86e</i></p>
<dl>
<dd>The full SHA-1 object name (40-byte hexadecimal string), or a leading substring that is unique within the repository. E.g. dae86e1950b1277e545cee180551750029cfe735 and dae86e both name the same commit object if there is no other object in your repository whose object name starts with dae86e.</dl>
<p> <i>&lt;describeOutput&gt;</i>, e.g. <i>v1.7.4.2-679-g3bee7fb</i></p>
<dl>
<dd>Output from <code>git describe</code>; i.e. a closest tag, optionally followed by a dash and a number of commits, followed by a dash, a <i>g</i>, and an abbreviated object name.</dl>
<p> <i>&lt;refname&gt;</i>, e.g. <i>master</i>, <i>heads/master</i>, <i>refs/heads/master</i></p>
<dl>
<dd>A symbolic ref name. E.g. <i>master</i> typically means the commit object referenced by <i>refs/heads/master</i>. If you happen to have both <i>heads/master</i> and <i>tags/master</i>, you can explicitly say <i>heads/master</i> to tell Git which one you mean. When ambiguous, a <i>&lt;refname&gt;</i> is disambiguated by taking the first match in the following rules: </p>
<dl>
<dd>1. If <i>$GIT_DIR/&lt;refname&gt;</i> exists, that is what you mean (this is usually useful only for <code>HEAD</code>, <code>FETCH_HEAD</code>, <code>ORIG_HEAD</code>, <code>MERGE_HEAD</code> and <code>CHERRY_PICK_HEAD</code>);</dl>
<dl>
<dd>2. otherwise, <i>refs/&lt;refname&gt;</i> if it exists;</dl>
<dl>
<dd>3. otherwise, <i>refs/tags/&lt;refname&gt;</i> if it exists;</dl>
<dl>
<dd>4. otherwise, <i>refs/heads/&lt;refname&gt;</i> if it exists;</dl>
<dl>
<dd>5. otherwise, <i>refs/remotes/&lt;refname&gt;</i> if it exists;</dl>
<dl>
<dd>6. otherwise, <i>refs/remotes/&lt;refname&gt;/HEAD</i> if it exists. </p>
<p> <code>HEAD</code> names the commit on which you based the changes in the working tree. <code>FETCH_HEAD</code> records the branch which you fetched from a remote repository with your last <code>git fetch</code> invocation. <code>ORIG_HEAD</code> is created by commands that move your <code>HEAD</code> in a drastic way, to record the position of the <code>HEAD</code> before their operation, so that you can easily change the tip of the branch back to the state before you ran them. <code>MERGE_HEAD</code> records the commit(s) which you are merging into your branch when you run <code>git merge</code>. <code>CHERRY_PICK_HEAD</code> records the commit which you are cherry-picking when you run <code>git cherry-pick</code>. </p>
<p> Note that any of the <i>refs/*</i> cases above may come either from the <code>$GIT_DIR/refs</code> directory or from the <code>$GIT_DIR/packed-refs</code> file. While the ref name encoding is unspecified, UTF-8 is preferred as some output processing may assume ref names in UTF-8.</dl>
</dl>
<p> <i>@</i></p>
<dl>
<dd><i>@</i> alone is a shortcut for <code>HEAD</code>.</dl>
<p> <i>[&lt;refname&gt;]@{&lt;date&gt;}</i>, e.g. <i>master@{yesterday}</i>, <i>HEAD@{5 minutes ago}</i></p>
<dl>
<dd>A ref followed by the suffix <i>@</i> with a date specification enclosed in a brace pair (e.g. <i>{yesterday}</i>, <i>{1 month 2 weeks 3 days 1 hour 1 second ago}</i> or <i>{1979-02-26 18:30:00}</i>) specifies the value of the ref at a prior point in time. This suffix may only be used immediately following a ref name and the ref must have an existing log (<i>$GIT_DIR/logs/&lt;ref&gt;</i>). Note that this looks up the state of your <code>local</code> ref at a given time; e.g., what was in your local <i>master</i> branch last week. If you want to look at commits made during certain times, see <code>&#8211;since</code> and <code>&#8211;until</code>.</dl>
<p> <i>&lt;refname&gt;@{&lt;n&gt;}</i>, e.g. <i>master@{1}</i></p>
<dl>
<dd>A ref followed by the suffix <i>@</i> with an ordinal specification enclosed in a brace pair (e.g. <i>{1}</i>, <i>{15}</i>) specifies the n-th prior value of that ref. For example <i>master@{1}</i> is the immediate prior value of <i>master</i> while <i>master@{5}</i> is the 5th prior value of <i>master</i>. This suffix may only be used immediately following a ref name and the ref must have an existing log (<i>$GIT_DIR/logs/&lt;refname&gt;</i>).</dl>
<p> <i>@{&lt;n&gt;}</i>, e.g. <i>@{1}</i></p>
<dl>
<dd>You can use the <i>@</i> construct with an empty ref part to get at a reflog entry of the current branch. For example, if you are on branch <i>blabla</i> then <i>@{1}</i> means the same as <i>blabla@{1}</i>.</dl>
<p> <i>@{-&lt;n&gt;}</i>, e.g. <i>@{-1}</i></p>
<dl>
<dd>The construct <i>@{-&lt;n&gt;}</i> means the &lt;n&gt;th branch/commit checked out before the current one.</dl>
<p> <i>[&lt;branchname&gt;]@{upstream}</i>, e.g. <i>master@{upstream}</i>, <i>@{u}</i></p>
<dl>
<dd>The suffix <i>@{upstream}</i> to a branchname (short form <i>&lt;branchname&gt;@{u}</i>) refers to the branch that the branch specified by branchname is set to build on top of (configured with <code>branch.&lt;name&gt;.remote</code> and <code>branch.&lt;name&gt;.merge</code>). A missing branchname defaults to the current one. These suffixes are also accepted when spelled in uppercase, and they mean the same thing no matter the case.</dl>
<p> <i>[&lt;branchname&gt;]@{push}</i>, e.g. <i>master@{push}</i>, <i>@{push}</i></p>
<dl>
<dd>The suffix <i>@{push}</i> reports the branch &quot;where we would push to&quot; if <code>git push</code> were run while <code>branchname</code> was checked out (or the current <code>HEAD</code> if no branchname is specified). Since our push destination is in a remote repository, of course, we report the local tracking branch that corresponds to that branch (i.e., something in <code>refs/remotes/</code>). </p>
<p> Here&#8217;s an example to make it more clear: </p>
<dl>
<dd>
<pre>$ git config push.default current
$ git config remote.pushdefault myfork
$ git switch -c mybranch origin/master
$ git rev-parse --symbolic-full-name @{upstream}
refs/remotes/origin/master
$ git rev-parse --symbolic-full-name @{push}
refs/remotes/myfork/mybranch</pre>
</dl>
<p> Note in the example that we set up a triangular workflow, where we pull from one location and push to another. In a non-triangular workflow, <i>@{push}</i> is the same as <i>@{upstream}</i>, and there is no need for it. </p>
<p> This suffix is also accepted when spelled in uppercase, and means the same thing no matter the case.</dl>
<p> <i>&lt;rev&gt;^[&lt;n&gt;]</i>, e.g. <i>HEAD^, v1.5.1^0</i></p>
<dl>
<dd>A suffix <i>^</i> to a revision parameter means the first parent of that commit object. <i>^&lt;n&gt;</i> means the &lt;n&gt;th parent (i.e. <i>&lt;rev&gt;^</i> is equivalent to <i>&lt;rev&gt;^1</i>). As a special rule, <i>&lt;rev&gt;^0</i> means the commit itself and is used when <i>&lt;rev&gt;</i> is the object name of a tag object that refers to a commit object.</dl>
<p> <i>&lt;rev&gt;~[&lt;n&gt;]</i>, e.g. <i>HEAD~, master~3</i></p>
<dl>
<dd>A suffix <i>~</i> to a revision parameter means the first parent of that commit object. A suffix <i>~&lt;n&gt;</i> to a revision parameter means the commit object that is the &lt;n&gt;th generation ancestor of the named commit object, following only the first parents. I.e. <i>&lt;rev&gt;~3</i> is equivalent to <i>&lt;rev&gt;^^^</i> which is equivalent to <i>&lt;rev&gt;^1^1^1</i>. See below for an illustration of the usage of this form.</dl>
<p> <i>&lt;rev&gt;^{&lt;type&gt;}</i>, e.g. <i>v0.99.8^{commit}</i></p>
<dl>
<dd>A suffix <i>^</i> followed by an object type name enclosed in brace pair means dereference the object at <i>&lt;rev&gt;</i> recursively until an object of type <i>&lt;type&gt;</i> is found or the object cannot be dereferenced anymore (in which case, barf). For example, if <i>&lt;rev&gt;</i> is a commit-ish, <i>&lt;rev&gt;^{commit}</i> describes the corresponding commit object. Similarly, if <i>&lt;rev&gt;</i> is a tree-ish, <i>&lt;rev&gt;^{tree}</i> describes the corresponding tree object. <i>&lt;rev&gt;^0</i> is a short-hand for <i>&lt;rev&gt;^{commit}</i>. </p>
<p> <i>&lt;rev&gt;^{object}</i> can be used to make sure <i>&lt;rev&gt;</i> names an object that exists, without requiring <i>&lt;rev&gt;</i> to be a tag, and without dereferencing <i>&lt;rev&gt;</i>; because a tag is already an object, it does not have to be dereferenced even once to get to an object. </p>
<p> <i>&lt;rev&gt;^{tag}</i> can be used to ensure that <i>&lt;rev&gt;</i> identifies an existing tag object.</dl>
<p> <i>&lt;rev&gt;^{}</i>, e.g. <i>v0.99.8^{}</i></p>
<dl>
<dd>A suffix <i>^</i> followed by an empty brace pair means the object could be a tag, and dereference the tag recursively until a non-tag object is found.</dl>
<p> <i>&lt;rev&gt;^{/&lt;text&gt;}</i>, e.g. <i>HEAD^{/fix nasty bug}</i></p>
<dl>
<dd>A suffix <i>^</i> to a revision parameter, followed by a brace pair that contains a text led by a slash, is the same as the <i>:/fix nasty bug</i> syntax below except that it returns the youngest matching commit which is reachable from the <i>&lt;rev&gt;</i> before <i>^</i>.</dl>
<p> <i>:/&lt;text&gt;</i>, e.g. <i>:/fix nasty bug</i></p>
<dl>
<dd>A colon, followed by a slash, followed by a text, names a commit whose commit message matches the specified regular expression. This name returns the youngest matching commit which is reachable from any ref, including HEAD. The regular expression can match any part of the commit message. To match messages starting with a string, one can use e.g. <i>:/^foo</i>. The special sequence <i>:/!</i> is reserved for modifiers to what is matched. <i>:/!-foo</i> performs a negative match, while <i>:/!!foo</i> matches a literal <i>!</i> character, followed by <i>foo</i>. Any other sequence beginning with <i>:/!</i> is reserved for now. Depending on the given text, the shell&#8217;s word splitting rules might require additional quoting.</dl>
<p> <i>&lt;rev&gt;:&lt;path&gt;</i>, e.g. <i>HEAD:README</i>, <i>master:./README</i></p>
<dl>
<dd>A suffix <i>:</i> followed by a path names the blob or tree at the given path in the tree-ish object named by the part before the colon. A path starting with <i>./</i> or <i>../</i> is relative to the current working directory. The given path will be converted to be relative to the working tree&#8217;s root directory. This is most useful to address a blob or tree from a commit or tree that has the same tree structure as the working tree.</dl>
<p> <i>:[&lt;n&gt;:]&lt;path&gt;</i>, e.g. <i>:0:README</i>, <i>:README</i></p>
<dl>
<dd>A colon, optionally followed by a stage number (0 to 3) and a colon, followed by a path, names a blob object in the index at the given path. A missing stage number (and the colon that follows it) names a stage 0 entry. During a merge, stage 1 is the common ancestor, stage 2 is the target branch&#8217;s version (typically the current branch), and stage 3 is the version from the branch which is being merged.</dl>
<p> Here is an illustration, by Jon Loeliger. Both commit nodes B and C are parents of commit node A. Parent commits are ordered left-to-right. </p>
<dl>
<dd>
<pre>G H I J
 \ / \ /
 D E F
 \ | / \
 \ | / |
 \|/ |
 B C
 \ /
 \ /
 A</pre>
</dl>
<dl>
<dd>
<pre>A = = A^0
B = A^ = A^1 = A~1
C = = A^2
D = A^^ = A^1^1 = A~2
E = B^2 = A^^2
F = B^3 = A^^3
G = A^^^ = A^1^1^1 = A~3
H = D^2 = B^^2 = A^^^2 = A~2^2
I = F^ = B^3^ = A^^3^
J = F^2 = B^3^2 = A^^3^2</pre>
</dl>
<h2>Specifying Ranges</h2>
<p>History traversing commands such as <code>git log</code> operate on a set of commits, not just a single commit. </p>
<p> For these commands, specifying a single revision, using the notation described in the previous section, means the set of commits <code>reachable</code> from the given commit. </p>
<p> Specifying several revisions means the set of commits reachable from any of the given commits. </p>
<p> A commit&#8217;s reachable set is the commit itself and the commits in its ancestry chain. </p>
<p> There are several notations to specify a set of connected commits (called a &quot;revision range&quot;), illustrated below.</p>
<h3>Commit Exclusions</h3>
<p><i>^&lt;rev&gt;</i> (caret) Notation</p>
<dl>
<dd>To exclude commits reachable from a commit, a prefix <i>^</i> notation is used. E.g. <i>^r1 r2</i> means commits reachable from <i>r2</i> but exclude the ones reachable from <i>r1</i> (i.e. <i>r1</i> and its ancestors).</dl>
<h3>Dotted Range Notations</h3>
<p>The <i>..</i> (two-dot) Range Notation</p>
<dl>
<dd>The <i>^r1 r2</i> set operation appears so often that there is a shorthand for it. When you have two commits <i>r1</i> and <i>r2</i> (named according to the syntax explained in SPECIFYING REVISIONS above), you can ask for commits that are reachable from r2 excluding those that are reachable from r1 by <i>^r1 r2</i> and it can be written as <i>r1..r2</i>.</dl>
<p> The <i>&#8230;</i> (three-dot) Symmetric Difference Notation</p>
<dl>
<dd>A similar notation <i>r1&#8230;r2</i> is called symmetric difference of <i>r1</i> and <i>r2</i> and is defined as <i>r1 r2 &#8211;not $(git merge-base &#8211;all r1 r2)</i>. It is the set of commits that are reachable from either one of <i>r1</i> (left side) or <i>r2</i> (right side) but not from both.</dl>
<p> In these two shorthand notations, you can omit one end and let it default to HEAD. For example, <i>origin..</i> is a shorthand for <i>origin..HEAD</i> and asks &quot;What did I do since I forked from the origin branch?&quot; Similarly, <i>..origin</i> is a shorthand for <i>HEAD..origin</i> and asks &quot;What did the origin do since I forked from them?&quot; Note that <i>..</i> would mean <i>HEAD..HEAD</i> which is an empty range that is both reachable and unreachable from HEAD. </p>
<p> Commands that are specifically designed to take two distinct ranges (e.g. &quot;git range-diff R1 R2&quot; to compare two ranges) do exist, but they are exceptions. Unless otherwise noted, all &quot;git&quot; commands that operate on a set of commits work on a single revision range. In other words, writing two &quot;two-dot range notation&quot; next to each other, e.g. </p>
<dl>
<dd>
<pre>$ git log A..B C..D</pre>
</dl>
<p> does <code>not</code> specify two revision ranges for most commands. Instead it will name a single connected set of commits, i.e. those that are reachable from either B or D but are reachable from neither A or C. In a linear history like this: </p>
<dl>
<dd>
<pre>---A---B---o---o---C---D</pre>
</dl>
<p> because A and B are reachable from C, the revision range specified by these two dotted ranges is a single commit D.</p>
<h3>Other &lt;rev&gt;^ Parent Shorthand Notations</h3>
<p>Three other shorthands exist, particularly useful for merge commits, for naming a set that is formed by a commit and its parent commits. </p>
<p> The <i>r1^@</i> notation means all parents of <i>r1</i>. </p>
<p> The <i>r1^!</i> notation includes commit <i>r1</i> but excludes all of its parents. By itself, this notation denotes the single commit <i>r1</i>. </p>
<p> The <i>&lt;rev&gt;^-[&lt;n&gt;]</i> notation includes <i>&lt;rev&gt;</i> but excludes the &lt;n&gt;th parent (i.e. a shorthand for <i>&lt;rev&gt;^&lt;n&gt;..&lt;rev&gt;</i>), with <i>&lt;n&gt;</i> = 1 if not given. This is typically useful for merge commits where you can just pass <i>&lt;commit&gt;^-</i> to get all the commits in the branch that was merged in merge commit <i>&lt;commit&gt;</i> (including <i>&lt;commit&gt;</i> itself). </p>
<p> While <i>&lt;rev&gt;^&lt;n&gt;</i> was about specifying a single commit parent, these three notations also consider its parents. For example you can say <i>HEAD^2^@</i>, however you cannot say <i>HEAD^@^2</i>.</p>
<h2>Revision Range Summary</h2>
<p><i>&lt;rev&gt;</i></p>
<dl>
<dd>Include commits that are reachable from &lt;rev&gt; (i.e. &lt;rev&gt; and its ancestors).</dl>
<p> <i>^&lt;rev&gt;</i></p>
<dl>
<dd>Exclude commits that are reachable from &lt;rev&gt; (i.e. &lt;rev&gt; and its ancestors).</dl>
<p> <i>&lt;rev1&gt;..&lt;rev2&gt;</i></p>
<dl>
<dd>Include commits that are reachable from &lt;rev2&gt; but exclude those that are reachable from &lt;rev1&gt;. When either &lt;rev1&gt; or &lt;rev2&gt; is omitted, it defaults to <code>HEAD</code>.</dl>
<p> <i>&lt;rev1&gt;&#8230;&lt;rev2&gt;</i></p>
<dl>
<dd>Include commits that are reachable from either &lt;rev1&gt; or &lt;rev2&gt; but exclude those that are reachable from both. When either &lt;rev1&gt; or &lt;rev2&gt; is omitted, it defaults to <code>HEAD</code>.</dl>
<p> <i>&lt;rev&gt;^@</i>, e.g. <i>HEAD^@</i></p>
<dl>
<dd>A suffix <i>^</i> followed by an at sign is the same as listing all parents of <i>&lt;rev&gt;</i> (meaning, include anything reachable from its parents, but not the commit itself).</dl>
<p> <i>&lt;rev&gt;^!</i>, e.g. <i>HEAD^!</i></p>
<dl>
<dd>A suffix <i>^</i> followed by an exclamation mark is the same as giving commit <i>&lt;rev&gt;</i> and then all its parents prefixed with <i>^</i> to exclude them (and their ancestors).</dl>
<p> <i>&lt;rev&gt;^-&lt;n&gt;</i>, e.g. <i>HEAD^-, HEAD^-2</i></p>
<dl>
<dd>Equivalent to <i>&lt;rev&gt;^&lt;n&gt;..&lt;rev&gt;</i>, with <i>&lt;n&gt;</i> = 1 if not given.</dl>
<p> Here are a handful of examples using the Loeliger illustration above, with each step in the notation&#8217;s expansion and selection carefully spelt out: </p>
<dl>
<dd>
<pre> Args Expanded arguments Selected commits
 D G H D
 D F G H I J D F
 ^G D H D
 ^D B E I J F B
 ^D B C E I J F B C
 C I J F C
 B..C = ^B C C
 B...C = B ^F C G H D E B C
 B^- = B^..B
 = ^B^1 B E I J F B
 C^@ = C^1
 = F I J F
 B^@ = B^1 B^2 B^3
 = D E F D G H E F I J
 C^! = C ^C^@
 = C ^C^1
 = C ^F C
 B^! = B ^B^@
 = B ^B^1 ^B^2 ^B^3
 = B ^D ^E ^F B
 F^! D = F ^I ^J D G H D F</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-git-rev-parse/">git-rev-parse</a></code>(1)</p>
<h2>Git</h2>
<p>Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite</p>
