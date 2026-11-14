---
title: "git-show(1)"
name: "git-show"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-show/"
description: "git-show – Show various types of objects"
---

<h2 class="name">NAME</h2>
<p> git-show &#8211; Show various types of objects </p>
<h2>SYNOPSIS</h2>
<pre><code>
git show[&lt;options&gt;][&lt;object&gt;...]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Shows one or more objects (blobs, trees, tags and commits). </p>
<p> For commits it shows the log message and textual diff. It also presents the merge commit in a special format as produced by <i>git diff-tree &#8211;cc</i>. </p>
<p> For tags, it shows the tag message and the referenced objects. </p>
<p> For trees, it shows the names (equivalent to <i>git ls-tree</i> with &#8211;name-only). </p>
<p> For plain blobs, it shows the plain contents. </p>
<p> The command takes options applicable to the <i>git diff-tree</i> command to control how the changes the commit introduces are shown. </p>
<p> This manual page describes only the most frequently used options.</p>
<h2>OPTIONS</h2>
<p> &lt;object&gt;&#8230;</p>
<dl>
<dt>
<dd> The names of objects to show (defaults to <i>HEAD</i>). For a more complete list of ways to spell object names, see &quot;SPECIFYING REVISIONS&quot; section in <code><a href="/docs/linux/man/7-gitrevisions/">gitrevisions</a></code>(7).</dl>
<p> &#8211;pretty[=&lt;format&gt;], &#8211;format=&lt;format&gt;</p>
<dl>
<dt>
<dd> Pretty-print the contents of the commit logs in a given format, where <i>&lt;format&gt;</i> can be one of <i>oneline</i>, <i>short</i>, <i>medium</i>, <i>full</i>, <i>fuller</i>, <i>reference</i>, <i>email</i>, <i>raw</i>, <i>format:&lt;string&gt;</i> and <i>tformat:&lt;string&gt;</i>. When <i>&lt;format&gt;</i> is none of the above, and has <i>%placeholder</i> in it, it acts as if <i>&#8211;pretty=tformat:&lt;format&gt;</i> were given. </p>
<p> See the &quot;PRETTY FORMATS&quot; section for some additional details for each format. When <i>=&lt;format&gt;</i> part is omitted, it defaults to <i>medium</i>. </p>
<p> Note: you can specify the default pretty format in the repository configuration (see <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)).</dl>
<p> &#8211;abbrev-commit</p>
<dl>
<dt>
<dd> Instead of showing the full 40-byte hexadecimal commit object name, show a prefix that names the object uniquely. &quot;&#8211;abbrev=&lt;n&gt;&quot; (which also modifies diff output, if it is displayed) option can be used to specify the minimum length of the prefix. </p>
<p> This should make &quot;&#8211;pretty=oneline&quot; a whole lot more readable for people using 80-column terminals.</dl>
<p> &#8211;no-abbrev-commit</p>
<dl>
<dt>
<dd> Show the full 40-byte hexadecimal commit object name. This negates <code>&#8211;abbrev-commit</code>, either explicit or implied by other options such as &quot;&#8211;oneline&quot;. It also overrides the <code>log.abbrevCommit</code> variable.</dl>
<p> &#8211;oneline</p>
<dl>
<dt>
<dd> This is a shorthand for &quot;&#8211;pretty=oneline &#8211;abbrev-commit&quot; used together.</dl>
<p> &#8211;encoding=&lt;encoding&gt;</p>
<dl>
<dt>
<dd> Commit objects record the character encoding used for the log message in their encoding header; this option can be used to tell the command to re-code the commit log message in the encoding preferred by the user. For non plumbing commands this defaults to UTF-8. Note that if an object claims to be encoded in <code>X</code> and we are outputting in <code>X</code>, we will output the object verbatim; this means that invalid sequences in the original commit may be copied to the output. Likewise, if <a href="/docs/linux/man/3-iconv/">iconv</a>(3) fails to convert the commit, we will quietly output the original object verbatim.</dl>
<p> &#8211;expand-tabs=&lt;n&gt;, &#8211;expand-tabs, &#8211;no-expand-tabs</p>
<dl>
<dt>
<dd> Perform a tab expansion (replace each tab with enough spaces to fill to the next display column that is multiple of <i>&lt;n&gt;</i>) in the log message before showing it in the output. <code>&#8211;expand-tabs</code> is a short-hand for <code>&#8211;expand-tabs=8</code>, and <code>&#8211;no-expand-tabs</code> is a short-hand for <code>&#8211;expand-tabs=0</code>, which disables tab expansion. </p>
<p> By default, tabs are expanded in pretty formats that indent the log message by 4 spaces (i.e. <i>medium</i>, which is the default, <i>full</i>, and <i>fuller</i>).</dl>
<p> &#8211;notes[=&lt;ref&gt;]</p>
<dl>
<dt>
<dd> Show the notes (see <code><a href="/docs/linux/man/1-git-notes/">git-notes</a></code>(1)) that annotate the commit, when showing the commit log message. This is the default for <code>git log</code>, <code>git show</code> and <code>git whatchanged</code> commands when there is no <code>&#8211;pretty</code>, <code>&#8211;format</code>, or <code>&#8211;oneline</code> option given on the command line. </p>
<p> By default, the notes shown are from the notes refs listed in the <code>core.notesRef</code> and <code>notes.displayRef</code> variables (or corresponding environment overrides). See <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1) for more details. </p>
<p> With an optional <i>&lt;ref&gt;</i> argument, use the ref to find the notes to display. The ref can specify the full refname when it begins with <code>refs/notes/</code>; when it begins with <code>notes/</code>, <code>refs/</code> and otherwise <code>refs/notes/</code> is prefixed to form a full name of the ref. </p>
<p> Multiple &#8211;notes options can be combined to control which notes are being displayed. Examples: &quot;&#8211;notes=foo&quot; will show only notes from &quot;refs/notes/foo&quot;; &quot;&#8211;notes=foo &#8211;notes&quot; will show both notes from &quot;refs/notes/foo&quot; and from the default notes ref(s).</dl>
<p> &#8211;no-notes</p>
<dl>
<dt>
<dd> Do not show notes. This negates the above <code>&#8211;notes</code> option, by resetting the list of notes refs from which notes are shown. Options are parsed in the order given on the command line, so e.g. &quot;&#8211;notes &#8211;notes=foo &#8211;no-notes &#8211;notes=bar&quot; will only show notes from &quot;refs/notes/bar&quot;.</dl>
<p> &#8211;show-notes[=&lt;ref&gt;], &#8211;[no-]standard-notes</p>
<dl>
<dt>
<dd> These options are deprecated. Use the above &#8211;notes/&#8211;no-notes options instead.</dl>
<p> &#8211;show-signature</p>
<dl>
<dt>
<dd> Check the validity of a signed commit object by passing the signature to <code>gpg &#8211;verify</code> and show the output.</dl>
<h2>PRETTY FORMATS</h2>
<p> If the commit is a merge, and if the pretty-format is not <i>oneline</i>, <i>email</i> or <i>raw</i>, an additional line is inserted before the <i>Author:</i> line. This line begins with &quot;Merge: &quot; and the hashes of ancestral commits are printed, separated by spaces. Note that the listed commits may not necessarily be the list of the <code>direct</code> parent commits if you have limited your view of history: for example, if you are only interested in changes related to a certain directory or file. </p>
<p> There are several built-in formats, and you can define additional formats by setting a pretty.&lt;name&gt; config option to either another format name, or a <i>format:</i> string, as described below (see <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)). Here are the details of the built-in formats: </p>
<dl>
<dt>
<dd> &bull; <i>oneline</i> </p>
<dl>
<dt>
<dd>
<pre>
&lt;hash&gt; &lt;title line&gt;
</pre>
</dl>
<p> This is designed to be as compact as possible.</dl>
<dl>
<dt>
<dd> &bull; <i>short</i> </p>
<dl>
<dt>
<dd>
<pre>
commit &lt;hash&gt;
Author: &lt;author&gt;
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
&lt;title line&gt;
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; <i>medium</i> </p>
<dl>
<dt>
<dd>
<pre>
commit &lt;hash&gt;
Author: &lt;author&gt;
Date:   &lt;author date&gt;
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
&lt;title line&gt;
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
&lt;full commit message&gt;
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; <i>full</i> </p>
<dl>
<dt>
<dd>
<pre>
commit &lt;hash&gt;
Author: &lt;author&gt;
Commit: &lt;committer&gt;
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
&lt;title line&gt;
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
&lt;full commit message&gt;
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; <i>fuller</i> </p>
<dl>
<dt>
<dd>
<pre>
commit &lt;hash&gt;
Author:     &lt;author&gt;
AuthorDate: &lt;author date&gt;
Commit:     &lt;committer&gt;
CommitDate: &lt;committer date&gt;
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
&lt;title line&gt;
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
&lt;full commit message&gt;
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; <i>reference</i> </p>
<dl>
<dt>
<dd>
<pre>
&lt;abbrev hash&gt; (&lt;title line&gt;, &lt;short author date&gt;)
</pre>
</dl>
<p> This format is used to refer to another commit in a commit message and is the same as <code>&#8211;pretty=&#8217;format:%C(auto)%h (%s, %ad)&#8217;</code>. By default, the date is formatted with <code>&#8211;date=short</code> unless another <code>&#8211;date</code> option is explicitly specified. As with any <code>format:</code> with format placeholders, its output is not affected by other options like <code>&#8211;decorate</code> and <code>&#8211;walk-reflogs</code>.</dl>
<dl>
<dt>
<dd> &bull; <i>email</i> </p>
<dl>
<dt>
<dd>
<pre>
From &lt;hash&gt; &lt;date&gt;
From: &lt;author&gt;
Date: &lt;author date&gt;
Subject: [PATCH] &lt;title line&gt;
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
&lt;full commit message&gt;
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; <i>mboxrd</i> </p>
<p> Like <i>email</i>, but lines in the commit message starting with &quot;From &quot; (preceded by zero or more &quot;&gt;&quot;) are quoted with &quot;&gt;&quot; so they aren&#8217;t confused as starting a new commit.</dl>
<dl>
<dt>
<dd> &bull; <i>raw</i> </p>
<p> The <i>raw</i> format shows the entire commit exactly as stored in the commit object. Notably, the hashes are displayed in full, regardless of whether &#8211;abbrev or &#8211;no-abbrev are used, and <i>parents</i> information show the true parent commits, without taking grafts or history simplification into account. Note that this format affects the way commits are displayed, but not the way the diff is shown e.g. with <code>git log &#8211;raw</code>. To get full object names in a raw diff format, use <code>&#8211;no-abbrev</code>.</dl>
<dl>
<dt>
<dd> &bull; <i>format:&lt;string&gt;</i> </p>
<p> The <i>format:&lt;string&gt;</i> format allows you to specify which information you want to show. It works a little bit like printf format, with the notable exception that you get a newline with <i>%n</i> instead of <i>
</i>. </p>
<p> E.g, <i>format:&quot;The author of %h was %an, %ar%nThe title was &gt;&gt;%s&lt;&lt;%n&quot;</i> would show something like this: </p>
<dl>
<dt>
<dd>
<pre>
The author of fe6e0ee was Junio C Hamano, 23 hours ago
The title was &gt;&gt;t4119: test autocomputing -p&lt;n&gt; for traditional diff input.&lt;&lt;
</pre>
</dl>
<p> The placeholders are: </p>
<dl>
<dt>
<dd> &bull; Placeholders that expand to a single literal character: </p>
<p> <i>%n</i></p>
<dl>
<dt>
<dd> newline</dl>
<p> <i>%%</i></p>
<dl>
<dt>
<dd> a raw <i>%</i></dl>
<p> <i>%x00</i></p>
<dl>
<dt>
<dd> print a byte from a hex code</dl>
</dl>
<dl>
<dt>
<dd> &bull; Placeholders that affect formatting of later placeholders: </p>
<p> <i>%Cred</i></p>
<dl>
<dt>
<dd> switch color to red</dl>
<p> <i>%Cgreen</i></p>
<dl>
<dt>
<dd> switch color to green</dl>
<p> <i>%Cblue</i></p>
<dl>
<dt>
<dd> switch color to blue</dl>
<p> <i>%Creset</i></p>
<dl>
<dt>
<dd> reset color</dl>
<p> <i>%C(&#8230;)</i></p>
<dl>
<dt>
<dd> color specification, as described under Values in the &quot;CONFIGURATION FILE&quot; section of <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1). By default, colors are shown only when enabled for log output (by <code>color.diff</code>, <code>color.ui</code>, or <code>&#8211;color</code>, and respecting the <code>auto</code> settings of the former if we are going to a terminal). <code>%C(auto,&#8230;)</code> is accepted as a historical synonym for the default (e.g., <code>%C(auto,red)</code>). Specifying <code>%C(always,&#8230;)</code> will show the colors even when color is not otherwise enabled (though consider just using <code>&#8211;color=always</code> to enable color for the whole output, including this format and anything else git might color). <code>auto</code> alone (i.e. <code>%C(auto)</code>) will turn on auto coloring on the next placeholders until the color is switched again.</dl>
<p> <i>%m</i></p>
<dl>
<dt>
<dd> left (<code>&lt;</code>), right (<code>&gt;</code>) or boundary (<code>&#8211;</code>) mark</dl>
<p> <i>%w([&lt;w&gt;[,&lt;i1&gt;[,&lt;i2&gt;]]])</i></p>
<dl>
<dt>
<dd> switch line wrapping, like the -w option of <code><a href="/docs/linux/man/1-git-shortlog/">git-shortlog</a></code>(1).</dl>
<p> <i>%&lt;(&lt;N&gt;[,trunc|ltrunc|mtrunc])</i></p>
<dl>
<dt>
<dd> make the next placeholder take at least N columns, padding spaces on the right if necessary. Optionally truncate at the beginning (ltrunc), the middle (mtrunc) or the end (trunc) if the output is longer than N columns. Note that truncating only works correctly with N &gt;= 2.</dl>
<p> <i>%&lt;|(&lt;N&gt;)</i></p>
<dl>
<dt>
<dd> make the next placeholder take at least until Nth columns, padding spaces on the right if necessary</dl>
<p> <i>%&gt;(&lt;N&gt;)</i>, <i>%&gt;|(&lt;N&gt;)</i></p>
<dl>
<dt>
<dd> similar to <i>%&lt;(&lt;N&gt;)</i>, <i>%&lt;|(&lt;N&gt;)</i> respectively, but padding spaces on the left</dl>
<p> <i>%&gt;&gt;(&lt;N&gt;)</i>, <i>%&gt;&gt;|(&lt;N&gt;)</i></p>
<dl>
<dt>
<dd> similar to <i>%&gt;(&lt;N&gt;)</i>, <i>%&gt;|(&lt;N&gt;)</i> respectively, except that if the next placeholder takes more spaces than given and there are spaces on its left, use those spaces</dl>
<p> <i>%&gt;&lt;(&lt;N&gt;)</i>, <i>%&gt;&lt;|(&lt;N&gt;)</i></p>
<dl>
<dt>
<dd> similar to <i>%&lt;(&lt;N&gt;)</i>, <i>%&lt;|(&lt;N&gt;)</i> respectively, but padding both sides (i.e. the text is centered)</dl>
</dl>
<dl>
<dt>
<dd> &bull; Placeholders that expand to information extracted from the commit: </p>
<p> <i>%H</i></p>
<dl>
<dt>
<dd> commit hash</dl>
<p> <i>%h</i></p>
<dl>
<dt>
<dd> abbreviated commit hash</dl>
<p> <i>%T</i></p>
<dl>
<dt>
<dd> tree hash</dl>
<p> <i>%t</i></p>
<dl>
<dt>
<dd> abbreviated tree hash</dl>
<p> <i>%P</i></p>
<dl>
<dt>
<dd> parent hashes</dl>
<p> <i>%p</i></p>
<dl>
<dt>
<dd> abbreviated parent hashes</dl>
<p> <i>%an</i></p>
<dl>
<dt>
<dd> author name</dl>
<p> <i>%aN</i></p>
<dl>
<dt>
<dd> author name (respecting .mailmap, see <code><a href="/docs/linux/man/1-git-shortlog/">git-shortlog</a></code>(1) or <code><a href="/docs/linux/man/1-git-blame/">git-blame</a></code>(1))</dl>
<p> <i>%ae</i></p>
<dl>
<dt>
<dd> author email</dl>
<p> <i>%aE</i></p>
<dl>
<dt>
<dd> author email (respecting .mailmap, see <code><a href="/docs/linux/man/1-git-shortlog/">git-shortlog</a></code>(1) or <code><a href="/docs/linux/man/1-git-blame/">git-blame</a></code>(1))</dl>
<p> <i>%al</i></p>
<dl>
<dt>
<dd> author email local-part (the part before the <i>@</i> sign)</dl>
<p> <i>%aL</i></p>
<dl>
<dt>
<dd> author local-part (see <i>%al</i>) respecting .mailmap, see <code><a href="/docs/linux/man/1-git-shortlog/">git-shortlog</a></code>(1) or <code><a href="/docs/linux/man/1-git-blame/">git-blame</a></code>(1))</dl>
<p> <i>%ad</i></p>
<dl>
<dt>
<dd> author date (format respects &#8211;date= option)</dl>
<p> <i>%aD</i></p>
<dl>
<dt>
<dd> author date, RFC2822 style</dl>
<p> <i>%ar</i></p>
<dl>
<dt>
<dd> author date, relative</dl>
<p> <i>%at</i></p>
<dl>
<dt>
<dd> author date, UNIX timestamp</dl>
<p> <i>%ai</i></p>
<dl>
<dt>
<dd> author date, ISO 8601-like format</dl>
<p> <i>%aI</i></p>
<dl>
<dt>
<dd> author date, strict ISO 8601 format</dl>
<p> <i>%as</i></p>
<dl>
<dt>
<dd> author date, short format (<code>YYYY-MM-DD</code>)</dl>
<p> <i>%ah</i></p>
<dl>
<dt>
<dd> author date, human style (like the <code>&#8211;date=human</code> option of <code><a href="/docs/linux/man/1-git-rev-list/">git-rev-list</a></code>(1))</dl>
<p> <i>%cn</i></p>
<dl>
<dt>
<dd> committer name</dl>
<p> <i>%cN</i></p>
<dl>
<dt>
<dd> committer name (respecting .mailmap, see <code><a href="/docs/linux/man/1-git-shortlog/">git-shortlog</a></code>(1) or <code><a href="/docs/linux/man/1-git-blame/">git-blame</a></code>(1))</dl>
<p> <i>%ce</i></p>
<dl>
<dt>
<dd> committer email</dl>
<p> <i>%cE</i></p>
<dl>
<dt>
<dd> committer email (respecting .mailmap, see <code><a href="/docs/linux/man/1-git-shortlog/">git-shortlog</a></code>(1) or <code><a href="/docs/linux/man/1-git-blame/">git-blame</a></code>(1))</dl>
<p> <i>%cl</i></p>
<dl>
<dt>
<dd> committer email local-part (the part before the <i>@</i> sign)</dl>
<p> <i>%cL</i></p>
<dl>
<dt>
<dd> committer local-part (see <i>%cl</i>) respecting .mailmap, see <code><a href="/docs/linux/man/1-git-shortlog/">git-shortlog</a></code>(1) or <code><a href="/docs/linux/man/1-git-blame/">git-blame</a></code>(1))</dl>
<p> <i>%cd</i></p>
<dl>
<dt>
<dd> committer date (format respects &#8211;date= option)</dl>
<p> <i>%cD</i></p>
<dl>
<dt>
<dd> committer date, RFC2822 style</dl>
<p> <i>%cr</i></p>
<dl>
<dt>
<dd> committer date, relative</dl>
<p> <i>%ct</i></p>
<dl>
<dt>
<dd> committer date, UNIX timestamp</dl>
<p> <i>%ci</i></p>
<dl>
<dt>
<dd> committer date, ISO 8601-like format</dl>
<p> <i>%cI</i></p>
<dl>
<dt>
<dd> committer date, strict ISO 8601 format</dl>
<p> <i>%cs</i></p>
<dl>
<dt>
<dd> committer date, short format (<code>YYYY-MM-DD</code>)</dl>
<p> <i>%ch</i></p>
<dl>
<dt>
<dd> committer date, human style (like the <code>&#8211;date=human</code> option of <code><a href="/docs/linux/man/1-git-rev-list/">git-rev-list</a></code>(1))</dl>
<p> <i>%d</i></p>
<dl>
<dt>
<dd> ref names, like the &#8211;decorate option of <code><a href="/docs/linux/man/1-git-log/">git-log</a></code>(1)</dl>
<p> <i>%D</i></p>
<dl>
<dt>
<dd> ref names without the &quot; (&quot;, &quot;)&quot; wrapping.</dl>
<p> <i>%(describe[:options])</i></p>
<dl>
<dt>
<dd> human-readable name, like <code><a href="/docs/linux/man/1-git-describe/">git-describe</a></code>(1); empty string for undescribable commits. The <code>describe</code> string may be followed by a colon and zero or more comma-separated options. Descriptions can be inconsistent when tags are added or removed at the same time. </p>
<dl>
<dt>
<dd> &bull; <i>match=&lt;pattern&gt;</i>: Only consider tags matching the given <code><a href="/docs/linux/man/7-glob/">glob</a>(7)</code> pattern, excluding the &quot;refs/tags/&quot; prefix.</dl>
<dl>
<dt>
<dd> &bull; <i>exclude=&lt;pattern&gt;</i>: Do not consider tags matching the given <code><a href="/docs/linux/man/7-glob/">glob</a>(7)</code> pattern, excluding the &quot;refs/tags/&quot; prefix.</dl>
</dl>
<p> <i>%S</i></p>
<dl>
<dt>
<dd> ref name given on the command line by which the commit was reached (like <code>git log &#8211;source</code>), only works with <code>git log</code></dl>
<p> <i>%e</i></p>
<dl>
<dt>
<dd> encoding</dl>
<p> <i>%s</i></p>
<dl>
<dt>
<dd> subject</dl>
<p> <i>%f</i></p>
<dl>
<dt>
<dd> sanitized subject line, suitable for a filename</dl>
<p> <i>%b</i></p>
<dl>
<dt>
<dd> body</dl>
<p> <i>%B</i></p>
<dl>
<dt>
<dd> raw body (unwrapped subject and body)</dl>
<p> <i>%N</i></p>
<dl>
<dt>
<dd> commit notes</dl>
<p> <i>%GG</i></p>
<dl>
<dt>
<dd> raw verification message from GPG for a signed commit</dl>
<p> <i>%G?</i></p>
<dl>
<dt>
<dd> show &quot;G&quot; for a good (valid) signature, &quot;B&quot; for a bad signature, &quot;U&quot; for a good signature with unknown validity, &quot;X&quot; for a good signature that has expired, &quot;Y&quot; for a good signature made by an expired key, &quot;R&quot; for a good signature made by a revoked key, &quot;E&quot; if the signature cannot be checked (e.g. missing key) and &quot;N&quot; for no signature</dl>
<p> <i>%GS</i></p>
<dl>
<dt>
<dd> show the name of the signer for a signed commit</dl>
<p> <i>%GK</i></p>
<dl>
<dt>
<dd> show the key used to sign a signed commit</dl>
<p> <i>%GF</i></p>
<dl>
<dt>
<dd> show the fingerprint of the key used to sign a signed commit</dl>
<p> <i>%GP</i></p>
<dl>
<dt>
<dd> show the fingerprint of the primary key whose subkey was used to sign a signed commit</dl>
<p> <i>%GT</i></p>
<dl>
<dt>
<dd> show the trust level for the key used to sign a signed commit</dl>
<p> <i>%gD</i></p>
<dl>
<dt>
<dd> reflog selector, e.g., <code>refs/stash@{1}</code> or <code>refs/stash@{2 minutes ago}</code>; the format follows the rules described for the <code>-g</code> option. The portion before the <code>@</code> is the refname as given on the command line (so <code>git log -g refs/heads/master</code> would yield <code>refs/heads/master@{0}</code>).</dl>
<p> <i>%gd</i></p>
<dl>
<dt>
<dd> shortened reflog selector; same as <code>%gD</code>, but the refname portion is shortened for human readability (so <code>refs/heads/master</code> becomes just <code>master</code>).</dl>
<p> <i>%gn</i></p>
<dl>
<dt>
<dd> reflog identity name</dl>
<p> <i>%gN</i></p>
<dl>
<dt>
<dd> reflog identity name (respecting .mailmap, see <code><a href="/docs/linux/man/1-git-shortlog/">git-shortlog</a></code>(1) or <code><a href="/docs/linux/man/1-git-blame/">git-blame</a></code>(1))</dl>
<p> <i>%ge</i></p>
<dl>
<dt>
<dd> reflog identity email</dl>
<p> <i>%gE</i></p>
<dl>
<dt>
<dd> reflog identity email (respecting .mailmap, see <code><a href="/docs/linux/man/1-git-shortlog/">git-shortlog</a></code>(1) or <code><a href="/docs/linux/man/1-git-blame/">git-blame</a></code>(1))</dl>
<p> <i>%gs</i></p>
<dl>
<dt>
<dd> reflog subject</dl>
<p> <i>%(trailers[:options])</i></p>
<dl>
<dt>
<dd> display the trailers of the body as interpreted by <code><a href="/docs/linux/man/1-git-interpret-trailers/">git-interpret-trailers</a></code>(1). The <code>trailers</code> string may be followed by a colon and zero or more comma-separated options. If any option is provided multiple times the last occurrence wins. </p>
<p> The boolean options accept an optional value <code>[=&lt;BOOL&gt;]</code>. The values <code>true</code>, <code>false</code>, <code>on</code>, <code>off</code> etc. are all accepted. See the &quot;boolean&quot; sub-section in &quot;EXAMPLES&quot; in <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1). If a boolean option is given with no value, it&#8217;s enabled. </p>
<dl>
<dt>
<dd> &bull; <i>key=&lt;K&gt;</i>: only show trailers with specified key. Matching is done case-insensitively and trailing colon is optional. If option is given multiple times trailer lines matching any of the keys are shown. This option automatically enables the <code>only</code> option so that non-trailer lines in the trailer block are hidden. If that is not desired it can be disabled with <code>only=false</code>. E.g., <code>%(trailers:key=Reviewed-by)</code> shows trailer lines with key <code>Reviewed-by</code>.</dl>
<dl>
<dt>
<dd> &bull; <i>only[=&lt;BOOL&gt;]</i>: select whether non-trailer lines from the trailer block should be included.</dl>
<dl>
<dt>
<dd> &bull; <i>separator=&lt;SEP&gt;</i>: specify a separator inserted between trailer lines. When this option is not given each trailer line is terminated with a line feed character. The string SEP may contain the literal formatting codes described above. To use comma as separator one must use <code>%x2C</code> as it would otherwise be parsed as next option. E.g., <code>%(trailers:key=Ticket,separator=%x2C )</code> shows all trailer lines whose key is &quot;Ticket&quot; separated by a comma and a space.</dl>
<dl>
<dt>
<dd> &bull; <i>unfold[=&lt;BOOL&gt;]</i>: make it behave as if interpret-trailer&#8217;s <code>&#8211;unfold</code> option was given. E.g., <code>%(trailers:only,unfold=true)</code> unfolds and shows all trailer lines.</dl>
<dl>
<dt>
<dd> &bull; <i>keyonly[=&lt;BOOL&gt;]</i>: only show the key part of the trailer.</dl>
<dl>
<dt>
<dd> &bull; <i>valueonly[=&lt;BOOL&gt;]</i>: only show the value part of the trailer.</dl>
<dl>
<dt>
<dd> &bull; <i>key_value_separator=&lt;SEP&gt;</i>: specify a separator inserted between trailer lines. When this option is not given each trailer key-value pair is separated by &quot;: &quot;. Otherwise it shares the same semantics as <i>separator=&lt;SEP&gt;</i> above.</dl>
</dl>
</dl>
</dl>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font> </p>
<p> Some placeholders may depend on other options given to the revision traversal engine. For example, the <code>%g*</code> reflog options will insert an empty string unless we are traversing reflog entries (e.g., by <code>git log -g</code>). The <code>%d</code> and <code>%D</code> placeholders will use the &quot;short&quot; decoration format if <code>&#8211;decorate</code> was not already provided on the command line. </p>
</dl>
<p> If you add a <code>+</code> (plus sign) after <i>%</i> of a placeholder, a line-feed is inserted immediately before the expansion if and only if the placeholder expands to a non-empty string. </p>
<p> If you add a <code>&#8211;</code> (minus sign) after <i>%</i> of a placeholder, all consecutive line-feeds immediately preceding the expansion are deleted if and only if the placeholder expands to an empty string. </p>
<p> If you add a ` ` (space) after <i>%</i> of a placeholder, a space is inserted immediately before the expansion if and only if the placeholder expands to a non-empty string. </p>
<dl>
<dt>
<dd> &bull; <i>tformat:</i> </p>
<p> The <i>tformat:</i> format works exactly like <i>format:</i>, except that it provides &quot;terminator&quot; semantics instead of &quot;separator&quot; semantics. In other words, each commit has the message terminator character (usually a newline) appended, rather than a separator placed between entries. This means that the final entry of a single-line format will be properly terminated with a new line, just as the &quot;oneline&quot; format does. For example: </p>
<dl>
<dt>
<dd>
$ git log &#8211; 2 &#8211;pretty = format : % h 4da45bef | perl &#8211; pe &#8216;$_ .= &#8221; &#8212; NO NEWLINE
&#8221; unless /
/&#8217; 4da45be 7134973 &#8211;NO NEWLINE $ git log &#8211; 2 &#8211;pretty = tformat : % h 4da45bef | perl &#8211; pe &#8216;$_ .= &#8221; &#8212; NO NEWLINE
&#8221; unless /
/&#8217; 4da45be 7134973
</dl>
<p> In addition, any unrecognized string that has a <code>%</code> in it is interpreted as if it has <code>tformat:</code> in front of it. For example, these two are equivalent: </p>
<dl>
<dt>
<dd>
<pre>
$ git log -2 --pretty=tformat:%h 4da45bef
$ git log -2 --pretty=%h 4da45bef
</pre>
</dl>
</dl>
<h2>DIFF FORMATTING</h2>
<p> The options below can be used to change the way <code>git show</code> generates diff output. </p>
<p> -p, -u, &#8211;patch</p>
<dl>
<dt>
<dd> Generate patch (see section on generating patches).</dl>
<p> -s, &#8211;no-patch</p>
<dl>
<dt>
<dd> Suppress diff output. Useful for commands like <code>git show</code> that show the patch by default, or to cancel the effect of <code>&#8211;patch</code>.</dl>
<p> &#8211;diff-merges=(off|none|on|first-parent|1|separate|m|combined|c|dense-combined|cc), &#8211;no-diff-merges</p>
<dl>
<dt>
<dd> Specify diff format to be used for merge commits. Default is <code>dense-combined</code> unless <code>&#8211;first-parent</code> is in use, in which case <code>first-parent</code> is the default. </p>
<p> &#8211;diff-merges=(off|none), &#8211;no-diff-merges</p>
<dl>
<dt>
<dd> Disable output of diffs for merge commits. Useful to override implied value.</dl>
<p> &#8211;diff-merges=on, &#8211;diff-merges=m, -m</p>
<dl>
<dt>
<dd> This option makes diff output for merge commits to be shown in the default format. <code>-m</code> will produce the output only if <code>-p</code> is given as well. The default format could be changed using <code>log.diffMerges</code> configuration parameter, which default value is <code>separate</code>.</dl>
<p> &#8211;diff-merges=first-parent, &#8211;diff-merges=1</p>
<dl>
<dt>
<dd> This option makes merge commits show the full diff with respect to the first parent only.</dl>
<p> &#8211;diff-merges=separate</p>
<dl>
<dt>
<dd> This makes merge commits show the full diff with respect to each of the parents. Separate log entry and diff is generated for each parent.</dl>
<p> &#8211;diff-merges=combined, &#8211;diff-merges=c, -c</p>
<dl>
<dt>
<dd> With this option, diff output for a merge commit shows the differences from each of the parents to the merge result simultaneously instead of showing pairwise diff between a parent and the result one at a time. Furthermore, it lists only files which were modified from all parents. <code>-c</code> implies <code>-p</code>.</dl>
<p> &#8211;diff-merges=dense-combined, &#8211;diff-merges=cc, &#8211;cc</p>
<dl>
<dt>
<dd> With this option the output produced by <code>&#8211;diff-merges=combined</code> is further compressed by omitting uninteresting hunks whose contents in the parents have only two variants and the merge result picks one of them without modification. <code>&#8211;cc</code> implies <code>-p</code>.</dl>
</dl>
<p> &#8211;combined-all-paths</p>
<dl>
<dt>
<dd> This flag causes combined diffs (used for merge commits) to list the name of the file from all parents. It thus only has effect when <code>&#8211;diff-merges=[dense-]combined</code> is in use, and is likely only useful if filename changes are detected (i.e. when either rename or copy detection have been requested).</dl>
<p> -U&lt;n&gt;, &#8211;unified=&lt;n&gt;</p>
<dl>
<dt>
<dd> Generate diffs with &lt;n&gt; lines of context instead of the usual three. Implies <code>&#8211;patch</code>.</dl>
<p> &#8211;output=&lt;file&gt;</p>
<dl>
<dt>
<dd> Output to a specific file instead of stdout.</dl>
<p> &#8211;output-indicator-new=&lt;char&gt;, &#8211;output-indicator-old=&lt;char&gt;, &#8211;output-indicator-context=&lt;char&gt;</p>
<dl>
<dt>
<dd> Specify the character used to indicate new, old or context lines in the generated patch. Normally they are <i>+</i>, <i>&#8211;</i> and &#8216; &#8216; respectively.</dl>
<p> &#8211;raw</p>
<dl>
<dt>
<dd> For each commit, show a summary of changes using the raw diff format. See the &quot;RAW OUTPUT FORMAT&quot; section of <code><a href="/docs/linux/man/1-git-diff/">git-diff</a></code>(1). This is different from showing the log itself in raw format, which you can achieve with <code>&#8211;format=raw</code>.</dl>
<p> &#8211;patch-with-raw</p>
<dl>
<dt>
<dd> Synonym for <code>-p &#8211;raw</code>.</dl>
<p> -t</p>
<dl>
<dt>
<dd> Show the tree objects in the diff output.</dl>
<p> &#8211;indent-heuristic</p>
<dl>
<dt>
<dd> Enable the heuristic that shifts diff hunk boundaries to make patches easier to read. This is the default.</dl>
<p> &#8211;no-indent-heuristic</p>
<dl>
<dt>
<dd> Disable the indent heuristic.</dl>
<p> &#8211;minimal</p>
<dl>
<dt>
<dd> Spend extra time to make sure the smallest possible diff is produced.</dl>
<p> &#8211;patience</p>
<dl>
<dt>
<dd> Generate a diff using the &quot;patience diff&quot; algorithm.</dl>
<p> &#8211;histogram</p>
<dl>
<dt>
<dd> Generate a diff using the &quot;histogram diff&quot; algorithm.</dl>
<p> &#8211;anchored=&lt;text&gt;</p>
<dl>
<dt>
<dd> Generate a diff using the &quot;anchored diff&quot; algorithm. </p>
<p> This option may be specified more than once. </p>
<p> If a line exists in both the source and destination, exists only once, and starts with this text, this algorithm attempts to prevent it from appearing as a deletion or addition in the output. It uses the &quot;patience diff&quot; algorithm internally.</dl>
<p> &#8211;diff-algorithm={patience|minimal|histogram|myers}</p>
<dl>
<dt>
<dd> Choose a diff algorithm. The variants are as follows: </p>
<p> <code>default</code>, <code>myers</code></p>
<dl>
<dt>
<dd> The basic greedy diff algorithm. Currently, this is the default.</dl>
<p> <code>minimal</code></p>
<dl>
<dt>
<dd> Spend extra time to make sure the smallest possible diff is produced.</dl>
<p> <code>patience</code></p>
<dl>
<dt>
<dd> Use &quot;patience diff&quot; algorithm when generating patches.</dl>
<p> <code>histogram</code></p>
<dl>
<dt>
<dd> This algorithm extends the patience algorithm to &quot;support low-occurrence common elements&quot;.</dl>
<p> For instance, if you configured the <code>diff.algorithm</code> variable to a non-default value and want to use the default one, then you have to use <code>&#8211;diff-algorithm=default</code> option.</dl>
<p> &#8211;stat[=&lt;width&gt;[,&lt;name-width&gt;[,&lt;count&gt;]]]</p>
<dl>
<dt>
<dd> Generate a diffstat. By default, as much space as necessary will be used for the filename part, and the rest for the graph part. Maximum width defaults to terminal width, or 80 columns if not connected to a terminal, and can be overridden by <code>&lt;width&gt;</code>. The width of the filename part can be limited by giving another width <code>&lt;name-width&gt;</code> after a comma. The width of the graph part can be limited by using <code>&#8211;stat-graph-width=&lt;width&gt;</code> (affects all commands generating a stat graph) or by setting <code>diff.statGraphWidth=&lt;width&gt;</code> (does not affect <code>git format-patch</code>). By giving a third parameter <code>&lt;count&gt;</code>, you can limit the output to the first <code>&lt;count&gt;</code> lines, followed by <code>&#8230;</code> if there are more. </p>
<p> These parameters can also be set individually with <code>&#8211;stat-width=&lt;width&gt;</code>, <code>&#8211;stat-name-width=&lt;name-width&gt;</code> and <code>&#8211;stat-count=&lt;count&gt;</code>.</dl>
<p> &#8211;compact-summary</p>
<dl>
<dt>
<dd> Output a condensed summary of extended header information such as file creations or deletions (&quot;new&quot; or &quot;gone&quot;, optionally &quot;+l&quot; if it&#8217;s a symlink) and mode changes (&quot;+x&quot; or &quot;-x&quot; for adding or removing executable bit respectively) in diffstat. The information is put between the filename part and the graph part. Implies <code>&#8211;stat</code>.</dl>
<p> &#8211;numstat</p>
<dl>
<dt>
<dd> Similar to <code>&#8211;stat</code>, but shows number of added and deleted lines in decimal notation and pathname without abbreviation, to make it more machine friendly. For binary files, outputs two <code>&#8211;</code> instead of saying <code>0 0</code>.</dl>
<p> &#8211;shortstat</p>
<dl>
<dt>
<dd> Output only the last line of the <code>&#8211;stat</code> format containing total number of modified files, as well as number of added and deleted lines.</dl>
<p> -X[&lt;param1,param2,&#8230;&gt;], &#8211;dirstat[=&lt;param1,param2,&#8230;&gt;]</p>
<dl>
<dt>
<dd> Output the distribution of relative amount of changes for each sub-directory. The behavior of <code>&#8211;dirstat</code> can be customized by passing it a comma separated list of parameters. The defaults are controlled by the <code>diff.dirstat</code> configuration variable (see <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)). The following parameters are available: </p>
<p> <code>changes</code></p>
<dl>
<dt>
<dd> Compute the dirstat numbers by counting the lines that have been removed from the source, or added to the destination. This ignores the amount of pure code movements within a file. In other words, rearranging lines in a file is not counted as much as other changes. This is the default behavior when no parameter is given.</dl>
<p> <code>lines</code></p>
<dl>
<dt>
<dd> Compute the dirstat numbers by doing the regular line-based diff analysis, and summing the removed/added line counts. (For binary files, count 64-byte chunks instead, since binary files have no natural concept of lines). This is a more expensive <code>&#8211;dirstat</code> behavior than the <code>changes</code> behavior, but it does count rearranged lines within a file as much as other changes. The resulting output is consistent with what you get from the other <code>&#8211;*stat</code> options.</dl>
<p> <code>files</code></p>
<dl>
<dt>
<dd> Compute the dirstat numbers by counting the number of files changed. Each changed file counts equally in the dirstat analysis. This is the computationally cheapest <code>&#8211;dirstat</code> behavior, since it does not have to look at the file contents at all.</dl>
<p> <code>cumulative</code></p>
<dl>
<dt>
<dd> Count changes in a child directory for the parent directory as well. Note that when using <code>cumulative</code>, the sum of the percentages reported may exceed 100%. The default (non-cumulative) behavior can be specified with the <code>noncumulative</code> parameter.</dl>
<p> &lt;limit&gt;</p>
<dl>
<dt>
<dd> An integer parameter specifies a cut-off percent (3% by default). Directories contributing less than this percentage of the changes are not shown in the output.</dl>
<p> Example: The following will count changed files, while ignoring directories with less than 10% of the total amount of changed files, and accumulating child directory counts in the parent directories: <code>&#8211;dirstat=files,10,cumulative</code>.</dl>
<p> &#8211;cumulative</p>
<dl>
<dt>
<dd> Synonym for &#8211;dirstat=cumulative</dl>
<p> &#8211;dirstat-by-file[=&lt;param1,param2&gt;&#8230;]</p>
<dl>
<dt>
<dd> Synonym for &#8211;dirstat=files,param1,param2&#8230;</dl>
<p> &#8211;summary</p>
<dl>
<dt>
<dd> Output a condensed summary of extended header information such as creations, renames and mode changes.</dl>
<p> &#8211;patch-with-stat</p>
<dl>
<dt>
<dd> Synonym for <code>-p &#8211;stat</code>.</dl>
<p> -z</p>
<dl>
<dt>
<dd> Separate the commits with NULs instead of with new newlines. </p>
<p> Also, when <code>&#8211;raw</code> or <code>&#8211;numstat</code> has been given, do not munge pathnames and use NULs as output field terminators. </p>
<p> Without this option, pathnames with &quot;unusual&quot; characters are quoted as explained for the configuration variable <code>core.quotePath</code> (see <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)).</dl>
<p> &#8211;name-only</p>
<dl>
<dt>
<dd> Show only names of changed files. The file names are often encoded in UTF-8. For more information see the discussion about encoding in the <code><a href="/docs/linux/man/1-git-log/">git-log</a></code>(1) manual page.</dl>
<p> &#8211;name-status</p>
<dl>
<dt>
<dd> Show only names and status of changed files. See the description of the <code>&#8211;diff-filter</code> option on what the status letters mean. Just like <code>&#8211;name-only</code> the file names are often encoded in UTF-8.</dl>
<p> &#8211;submodule[=&lt;format&gt;]</p>
<dl>
<dt>
<dd> Specify how differences in submodules are shown. When specifying <code>&#8211;submodule=short</code> the <i>short</i> format is used. This format just shows the names of the commits at the beginning and end of the range. When <code>&#8211;submodule</code> or <code>&#8211;submodule=log</code> is specified, the <i>log</i> format is used. This format lists the commits in the range like <code><a href="/docs/linux/man/1-git-submodule/">git-submodule</a></code>(1) <code>summary</code> does. When <code>&#8211;submodule=diff</code> is specified, the <i>diff</i> format is used. This format shows an inline diff of the changes in the submodule contents between the commit range. Defaults to <code>diff.submodule</code> or the <i>short</i> format if the config option is unset.</dl>
<p> &#8211;color[=&lt;when&gt;]</p>
<dl>
<dt>
<dd> Show colored diff. <code>&#8211;color</code> (i.e. without <i>=&lt;when&gt;</i>) is the same as <code>&#8211;color=always</code>. <i>&lt;when&gt;</i> can be one of <code>always</code>, <code>never</code>, or <code>auto</code>.</dl>
<p> &#8211;no-color</p>
<dl>
<dt>
<dd> Turn off colored diff. It is the same as <code>&#8211;color=never</code>.</dl>
<p> &#8211;color-moved[=&lt;mode&gt;]</p>
<dl>
<dt>
<dd> Moved lines of code are colored differently. The &lt;mode&gt; defaults to <i>no</i> if the option is not given and to <i>zebra</i> if the option with no mode is given. The mode must be one of: </p>
<p> no</p>
<dl>
<dt>
<dd> Moved lines are not highlighted.</dl>
<p> default</p>
<dl>
<dt>
<dd> Is a synonym for <code>zebra</code>. This may change to a more sensible mode in the future.</dl>
<p> plain</p>
<dl>
<dt>
<dd> Any line that is added in one location and was removed in another location will be colored with <i>color.diff.newMoved</i>. Similarly <i>color.diff.oldMoved</i> will be used for removed lines that are added somewhere else in the diff. This mode picks up any moved line, but it is not very useful in a review to determine if a block of code was moved without permutation.</dl>
<p> blocks</p>
<dl>
<dt>
<dd> Blocks of moved text of at least 20 alphanumeric characters are detected greedily. The detected blocks are painted using either the <i>color.diff.{old,new}Moved</i> color. Adjacent blocks cannot be told apart.</dl>
<p> zebra</p>
<dl>
<dt>
<dd> Blocks of moved text are detected as in <i>blocks</i> mode. The blocks are painted using either the <i>color.diff.{old,new}Moved</i> color or <i>color.diff.{old,new}MovedAlternative</i>. The change between the two colors indicates that a new block was detected.</dl>
<p> dimmed-zebra</p>
<dl>
<dt>
<dd> Similar to <i>zebra</i>, but additional dimming of uninteresting parts of moved code is performed. The bordering lines of two adjacent blocks are considered interesting, the rest is uninteresting. <code>dimmed_zebra</code> is a deprecated synonym.</dl>
</dl>
<p> &#8211;no-color-moved</p>
<dl>
<dt>
<dd> Turn off move detection. This can be used to override configuration settings. It is the same as <code>&#8211;color-moved=no</code>.</dl>
<p> &#8211;color-moved-ws=&lt;modes&gt;</p>
<dl>
<dt>
<dd> This configures how whitespace is ignored when performing the move detection for <code>&#8211;color-moved</code>. These modes can be given as a comma separated list: </p>
<p> no</p>
<dl>
<dt>
<dd> Do not ignore whitespace when performing move detection.</dl>
<p> ignore-space-at-eol</p>
<dl>
<dt>
<dd> Ignore changes in whitespace at EOL.</dl>
<p> ignore-space-change</p>
<dl>
<dt>
<dd> Ignore changes in amount of whitespace. This ignores whitespace at line end, and considers all other sequences of one or more whitespace characters to be equivalent.</dl>
<p> ignore-all-space</p>
<dl>
<dt>
<dd> Ignore whitespace when comparing lines. This ignores differences even if one line has whitespace where the other line has none.</dl>
<p> allow-indentation-change</p>
<dl>
<dt>
<dd> Initially ignore any whitespace in the move detection, then group the moved code blocks only into a block if the change in whitespace is the same per line. This is incompatible with the other modes.</dl>
</dl>
<p> &#8211;no-color-moved-ws</p>
<dl>
<dt>
<dd> Do not ignore whitespace when performing move detection. This can be used to override configuration settings. It is the same as <code>&#8211;color-moved-ws=no</code>.</dl>
<p> &#8211;word-diff[=&lt;mode&gt;]</p>
<dl>
<dt>
<dd> Show a word diff, using the &lt;mode&gt; to delimit changed words. By default, words are delimited by whitespace; see <code>&#8211;word-diff-regex</code> below. The &lt;mode&gt; defaults to <i>plain</i>, and must be one of: </p>
<p> color</p>
<dl>
<dt>
<dd> Highlight changed words using only colors. Implies <code>&#8211;color</code>.</dl>
<p> plain</p>
<dl>
<dt>
<dd> Show words as <code>[-removed-]</code> and <code>{+added+}</code>. Makes no attempts to escape the delimiters if they appear in the input, so the output may be ambiguous.</dl>
<p> porcelain</p>
<dl>
<dt>
<dd> Use a special line-based format intended for script consumption. Added/removed/unchanged runs are printed in the usual unified diff format, starting with a <code>+</code>/<code>&#8211;</code>/` ` character at the beginning of the line and extending to the end of the line. Newlines in the input are represented by a tilde <code>~</code> on a line of its own.</dl>
<p> none</p>
<dl>
<dt>
<dd> Disable word diff again.</dl>
<p> Note that despite the name of the first mode, color is used to highlight the changed parts in all modes if enabled.</dl>
<p> &#8211;word-diff-regex=&lt;regex&gt;</p>
<dl>
<dt>
<dd> Use &lt;regex&gt; to decide what a word is, instead of considering runs of non-whitespace to be a word. Also implies <code>&#8211;word-diff</code> unless it was already enabled. </p>
<p> Every non-overlapping match of the &lt;regex&gt; is considered a word. Anything between these matches is considered whitespace and ignored(!) for the purposes of finding differences. You may want to append <code>|[^[:space:]]</code> to your regular expression to make sure that it matches all non-whitespace characters. A match that contains a newline is silently truncated(!) at the newline. </p>
<p> For example, <code>&#8211;word-diff-regex=.</code> will treat each character as a word and, correspondingly, show differences character by character. </p>
<p> The regex can also be set via a diff driver or configuration option, see <code><a href="/docs/linux/man/5-gitattributes/">gitattributes</a></code>(5) or <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1). Giving it explicitly overrides any diff driver or configuration setting. Diff drivers override configuration settings.</dl>
<p> &#8211;color-words[=&lt;regex&gt;]</p>
<dl>
<dt>
<dd> Equivalent to <code>&#8211;word-diff=color</code> plus (if a regex was specified) <code>&#8211;word-diff-regex=&lt;regex&gt;</code>.</dl>
<p> &#8211;no-renames</p>
<dl>
<dt>
<dd> Turn off rename detection, even when the configuration file gives the default to do so.</dl>
<p> &#8211;[no-]rename-empty</p>
<dl>
<dt>
<dd> Whether to use empty blobs as rename source.</dl>
<p> &#8211;check</p>
<dl>
<dt>
<dd> Warn if changes introduce conflict markers or whitespace errors. What are considered whitespace errors is controlled by <code>core.whitespace</code> configuration. By default, trailing whitespaces (including lines that consist solely of whitespaces) and a space character that is immediately followed by a tab character inside the initial indent of the line are considered whitespace errors. Exits with non-zero status if problems are found. Not compatible with &#8211;exit-code.</dl>
<p> &#8211;ws-error-highlight=&lt;kind&gt;</p>
<dl>
<dt>
<dd> Highlight whitespace errors in the <code>context</code>, <code>old</code> or <code>new</code> lines of the diff. Multiple values are separated by comma, <code>none</code> resets previous values, <code>default</code> reset the list to <code>new</code> and <code>all</code> is a shorthand for <code>old,new,context</code>. When this option is not given, and the configuration variable <code>diff.wsErrorHighlight</code> is not set, only whitespace errors in <code>new</code> lines are highlighted. The whitespace errors are colored with <code>color.diff.whitespace</code>.</dl>
<p> &#8211;full-index</p>
<dl>
<dt>
<dd> Instead of the first handful of characters, show the full pre- and post-image blob object names on the &quot;index&quot; line when generating patch format output.</dl>
<p> &#8211;binary</p>
<dl>
<dt>
<dd> In addition to <code>&#8211;full-index</code>, output a binary diff that can be applied with <code>git-apply</code>. Implies <code>&#8211;patch</code>.</dl>
<p> &#8211;abbrev[=&lt;n&gt;]</p>
<dl>
<dt>
<dd> Instead of showing the full 40-byte hexadecimal object name in diff-raw format output and diff-tree header lines, show the shortest prefix that is at least <i>&lt;n&gt;</i> hexdigits long that uniquely refers the object. In diff-patch output format, <code>&#8211;full-index</code> takes higher precedence, i.e. if <code>&#8211;full-index</code> is specified, full blob names will be shown regardless of <code>&#8211;abbrev</code>. Non default number of digits can be specified with <code>&#8211;abbrev=&lt;n&gt;</code>.</dl>
<p> -B[&lt;n&gt;][/&lt;m&gt;], &#8211;break-rewrites[=[&lt;n&gt;][/&lt;m&gt;]]</p>
<dl>
<dt>
<dd> Break complete rewrite changes into pairs of delete and create. This serves two purposes: </p>
<p> It affects the way a change that amounts to a total rewrite of a file not as a series of deletion and insertion mixed together with a very few lines that happen to match textually as the context, but as a single deletion of everything old followed by a single insertion of everything new, and the number <code>m</code> controls this aspect of the -B option (defaults to 60%). <code>-B/70%</code> specifies that less than 30% of the original should remain in the result for Git to consider it a total rewrite (i.e. otherwise the resulting patch will be a series of deletion and insertion mixed together with context lines). </p>
<p> When used with -M, a totally-rewritten file is also considered as the source of a rename (usually -M only considers a file that disappeared as the source of a rename), and the number <code>n</code> controls this aspect of the -B option (defaults to 50%). <code>-B20%</code> specifies that a change with addition and deletion compared to 20% or more of the file&#8217;s size are eligible for being picked up as a possible source of a rename to another file.</dl>
<p> -M[&lt;n&gt;], &#8211;find-renames[=&lt;n&gt;]</p>
<dl>
<dt>
<dd> If generating diffs, detect and report renames for each commit. For following files across renames while traversing history, see <code>&#8211;follow</code>. If <code>n</code> is specified, it is a threshold on the similarity index (i.e. amount of addition/deletions compared to the file&#8217;s size). For example, <code>-M90%</code> means Git should consider a delete/add pair to be a rename if more than 90% of the file hasn&#8217;t changed. Without a <code>%</code> sign, the number is to be read as a fraction, with a decimal point before it. I.e., <code>-M5</code> becomes 0.5, and is thus the same as <code>-M50%</code>. Similarly, <code>-M05</code> is the same as <code>-M5%</code>. To limit detection to exact renames, use <code>-M100%</code>. The default similarity index is 50%.</dl>
<p> -C[&lt;n&gt;], &#8211;find-copies[=&lt;n&gt;]</p>
<dl>
<dt>
<dd> Detect copies as well as renames. See also <code>&#8211;find-copies-harder</code>. If <code>n</code> is specified, it has the same meaning as for <code>-M&lt;n&gt;</code>.</dl>
<p> &#8211;find-copies-harder</p>
<dl>
<dt>
<dd> For performance reasons, by default, <code>-C</code> option finds copies only if the original file of the copy was modified in the same changeset. This flag makes the command inspect unmodified files as candidates for the source of copy. This is a very expensive operation for large projects, so use it with caution. Giving more than one <code>-C</code> option has the same effect.</dl>
<p> -D, &#8211;irreversible-delete</p>
<dl>
<dt>
<dd> Omit the preimage for deletes, i.e. print only the header but not the diff between the preimage and <code>/dev/null</code>. The resulting patch is not meant to be applied with <code>patch</code> or <code>git apply</code>; this is solely for people who want to just concentrate on reviewing the text after the change. In addition, the output obviously lacks enough information to apply such a patch in reverse, even manually, hence the name of the option. </p>
<p> When used together with <code>-B</code>, omit also the preimage in the deletion part of a delete/create pair.</dl>
<p> -l&lt;num&gt;</p>
<dl>
<dt>
<dd> The <code>-M</code> and <code>-C</code> options involve some preliminary steps that can detect subsets of renames/copies cheaply, followed by an exhaustive fallback portion that compares all remaining unpaired destinations to all relevant sources. (For renames, only remaining unpaired sources are relevant; for copies, all original sources are relevant.) For N sources and destinations, this exhaustive check is O(N^2). This option prevents the exhaustive portion of rename/copy detection from running if the number of source/destination files involved exceeds the specified number. Defaults to diff.renameLimit. Note that a value of 0 is treated as unlimited.</dl>
<p> &#8211;diff-filter=[(A|C|D|M|R|T|U|X|B)&#8230;[*]]</p>
<dl>
<dt>
<dd> Select only files that are Added (<code>A</code>), Copied (<code>C</code>), Deleted (<code>D</code>), Modified (<code>M</code>), Renamed (<code>R</code>), have their type (i.e. regular file, symlink, submodule, &#8230;) changed (<code>T</code>), are Unmerged (<code>U</code>), are Unknown (<code>X</code>), or have had their pairing Broken (<code>B</code>). Any combination of the filter characters (including none) can be used. When <code>*</code> (All-or-none) is added to the combination, all paths are selected if there is any file that matches other criteria in the comparison; if there is no file that matches other criteria, nothing is selected. </p>
<p> Also, these upper-case letters can be downcased to exclude. E.g. <code>&#8211;diff-filter=ad</code> excludes added and deleted paths. </p>
<p> Note that not all diffs can feature all types. For instance, diffs from the index to the working tree can never have Added entries (because the set of paths included in the diff is limited by what is in the index). Similarly, copied and renamed entries cannot appear if detection for those types is disabled.</dl>
<p> -S&lt;string&gt;</p>
<dl>
<dt>
<dd> Look for differences that change the number of occurrences of the specified string (i.e. addition/deletion) in a file. Intended for the scripter&#8217;s use. </p>
<p> It is useful when you&#8217;re looking for an exact block of code (like a struct), and want to know the history of that block since it first came into being: use the feature iteratively to feed the interesting block in the preimage back into <code>-S</code>, and keep going until you get the very first version of the block. </p>
<p> Binary files are searched as well.</dl>
<p> -G&lt;regex&gt;</p>
<dl>
<dt>
<dd> Look for differences whose patch text contains added/removed lines that match &lt;regex&gt;. </p>
<p> To illustrate the difference between <code>-S&lt;regex&gt; &#8211;pickaxe-regex</code> and <code>-G&lt;regex&gt;</code>, consider a commit with the following diff in the same file: </p>
<dl>
<dt>
<dd>
+ return frotz(nitfol, two-&gt;ptr, 1, 0);<br />
&#8230; &#8211; hit = frotz(nitfol, mf2.ptr, 1, 0);
</dl>
<p> While <code>git log -G&quot;frotz\(nitfol&quot;</code> will show this commit, <code>git log -S&quot;frotz\(nitfol&quot; &#8211;pickaxe-regex</code> will not (because the number of occurrences of that string did not change). </p>
<p> Unless <code>&#8211;text</code> is supplied patches of binary files without a textconv filter will be ignored. </p>
<p> See the <i>pickaxe</i> entry in <code><a href="/docs/linux/man/7-gitdiffcore/">gitdiffcore</a></code>(7) for more information.</dl>
<p> &#8211;find-object=&lt;object-id&gt;</p>
<dl>
<dt>
<dd> Look for differences that change the number of occurrences of the specified object. Similar to <code>-S</code>, just the argument is different in that it doesn&#8217;t search for a specific string but for a specific object id. </p>
<p> The object can be a blob or a submodule commit. It implies the <code>-t</code> option in <code>git-log</code> to also find trees.</dl>
<p> &#8211;pickaxe-all</p>
<dl>
<dt>
<dd> When <code>-S</code> or <code>-G</code> finds a change, show all the changes in that changeset, not just the files that contain the change in &lt;string&gt;.</dl>
<p> &#8211;pickaxe-regex</p>
<dl>
<dt>
<dd> Treat the &lt;string&gt; given to <code>-S</code> as an extended POSIX regular expression to match.</dl>
<p> -O&lt;orderfile&gt;</p>
<dl>
<dt>
<dd> Control the order in which files appear in the output. This overrides the <code>diff.orderFile</code> configuration variable (see <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)). To cancel <code>diff.orderFile</code>, use <code>-O/dev/null</code>. </p>
<p> The output order is determined by the order of glob patterns in &lt;orderfile&gt;. All files with pathnames that match the first pattern are output first, all files with pathnames that match the second pattern (but not the first) are output next, and so on. All files with pathnames that do not match any pattern are output last, as if there was an implicit match-all pattern at the end of the file. If multiple pathnames have the same rank (they match the same pattern but no earlier patterns), their output order relative to each other is the normal order. </p>
<p> &lt;orderfile&gt; is parsed as follows: </p>
<dl>
<dt>
<dd> &bull; Blank lines are ignored, so they can be used as separators for readability.</dl>
<dl>
<dt>
<dd> &bull; Lines starting with a hash (&quot;<code>#</code>&quot;) are ignored, so they can be used for comments. Add a backslash (&quot;<code>\</code>&quot;) to the beginning of the pattern if it starts with a hash.</dl>
<dl>
<dt>
<dd> &bull; Each other line contains a single pattern.</dl>
<p> Patterns have the same syntax and semantics as patterns used for <a href="/docs/linux/man/3-fnmatch/">fnmatch</a>(3) without the FNM_PATHNAME flag, except a pathname also matches a pattern if removing any number of the final pathname components matches the pattern. For example, the pattern &quot;<code>foo*bar</code>&quot; matches &quot;<code>fooasdfbar</code>&quot; and &quot;<code>foo/bar/baz/asdf</code>&quot; but not &quot;<code>foobarx</code>&quot;.</dl>
<p> &#8211;skip-to=&lt;file&gt;, &#8211;rotate-to=&lt;file&gt;</p>
<dl>
<dt>
<dd> Discard the files before the named &lt;file&gt; from the output (i.e. <i>skip to</i>), or move them to the end of the output (i.e. <i>rotate to</i>). These were invented primarily for use of the <code>git difftool</code> command, and may not be very useful otherwise.</dl>
<p> -R</p>
<dl>
<dt>
<dd> Swap two inputs; that is, show differences from index or on-disk file to tree contents.</dl>
<p> &#8211;relative[=&lt;path&gt;], &#8211;no-relative</p>
<dl>
<dt>
<dd> When run from a subdirectory of the project, it can be told to exclude changes outside the directory and show pathnames relative to it with this option. When you are not in a subdirectory (e.g. in a bare repository), you can name which subdirectory to make the output relative to by giving a &lt;path&gt; as an argument. <code>&#8211;no-relative</code> can be used to countermand both <code>diff.relative</code> config option and previous <code>&#8211;relative</code>.</dl>
<p> -a, &#8211;text</p>
<dl>
<dt>
<dd> Treat all files as text.</dl>
<p> &#8211;ignore-cr-at-eol</p>
<dl>
<dt>
<dd> Ignore carriage-return at the end of line when doing a comparison.</dl>
<p> &#8211;ignore-space-at-eol</p>
<dl>
<dt>
<dd> Ignore changes in whitespace at EOL.</dl>
<p> -b, &#8211;ignore-space-change</p>
<dl>
<dt>
<dd> Ignore changes in amount of whitespace. This ignores whitespace at line end, and considers all other sequences of one or more whitespace characters to be equivalent.</dl>
<p> -w, &#8211;ignore-all-space</p>
<dl>
<dt>
<dd> Ignore whitespace when comparing lines. This ignores differences even if one line has whitespace where the other line has none.</dl>
<p> &#8211;ignore-blank-lines</p>
<dl>
<dt>
<dd> Ignore changes whose lines are all blank.</dl>
<p> -I&lt;regex&gt;, &#8211;ignore-matching-lines=&lt;regex&gt;</p>
<dl>
<dt>
<dd> Ignore changes whose all lines match &lt;regex&gt;. This option may be specified more than once.</dl>
<p> &#8211;inter-hunk-context=&lt;lines&gt;</p>
<dl>
<dt>
<dd> Show the context between diff hunks, up to the specified number of lines, thereby fusing hunks that are close to each other. Defaults to <code>diff.interHunkContext</code> or 0 if the config option is unset.</dl>
<p> -W, &#8211;function-context</p>
<dl>
<dt>
<dd> Show whole function as context lines for each change. The function names are determined in the same way as <code>git diff</code> works out patch hunk headers (see <i>Defining a custom hunk-header</i> in <code><a href="/docs/linux/man/5-gitattributes/">gitattributes</a></code>(5)).</dl>
<p> &#8211;ext-diff</p>
<dl>
<dt>
<dd> Allow an external diff helper to be executed. If you set an external diff driver with <code><a href="/docs/linux/man/5-gitattributes/">gitattributes</a></code>(5), you need to use this option with <code><a href="/docs/linux/man/1-git-log/">git-log</a></code>(1) and friends.</dl>
<p> &#8211;no-ext-diff</p>
<dl>
<dt>
<dd> Disallow external diff drivers.</dl>
<p> &#8211;textconv, &#8211;no-textconv</p>
<dl>
<dt>
<dd> Allow (or disallow) external text conversion filters to be run when comparing binary files. See <code><a href="/docs/linux/man/5-gitattributes/">gitattributes</a></code>(5) for details. Because textconv filters are typically a one-way conversion, the resulting diff is suitable for human consumption, but cannot be applied. For this reason, textconv filters are enabled by default only for <code><a href="/docs/linux/man/1-git-diff/">git-diff</a></code>(1) and <code><a href="/docs/linux/man/1-git-log/">git-log</a></code>(1), but not for <code><a href="/docs/linux/man/1-git-format-patch/">git-format-patch</a></code>(1) or diff plumbing commands.</dl>
<p> &#8211;ignore-submodules[=&lt;when&gt;]</p>
<dl>
<dt>
<dd> Ignore changes to submodules in the diff generation. &lt;when&gt; can be either &quot;none&quot;, &quot;untracked&quot;, &quot;dirty&quot; or &quot;all&quot;, which is the default. Using &quot;none&quot; will consider the submodule modified when it either contains untracked or modified files or its HEAD differs from the commit recorded in the superproject and can be used to override any settings of the <i>ignore</i> option in <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1) or <code><a href="/docs/linux/man/5-gitmodules/">gitmodules</a></code>(5). When &quot;untracked&quot; is used submodules are not considered dirty when they only contain untracked content (but they are still scanned for modified content). Using &quot;dirty&quot; ignores all changes to the work tree of submodules, only changes to the commits stored in the superproject are shown (this was the behavior until 1.7.0). Using &quot;all&quot; hides all changes to submodules.</dl>
<p> &#8211;src-prefix=&lt;prefix&gt;</p>
<dl>
<dt>
<dd> Show the given source prefix instead of &quot;a/&quot;.</dl>
<p> &#8211;dst-prefix=&lt;prefix&gt;</p>
<dl>
<dt>
<dd> Show the given destination prefix instead of &quot;b/&quot;.</dl>
<p> &#8211;no-prefix</p>
<dl>
<dt>
<dd> Do not show any source or destination prefix.</dl>
<p> &#8211;line-prefix=&lt;prefix&gt;</p>
<dl>
<dt>
<dd> Prepend an additional prefix to every line of output.</dl>
<p> &#8211;ita-invisible-in-index</p>
<dl>
<dt>
<dd> By default entries added by &quot;git add -N&quot; appear as an existing empty file in &quot;git diff&quot; and a new file in &quot;git diff &#8211;cached&quot;. This option makes the entry appear as a new file in &quot;git diff&quot; and non-existent in &quot;git diff &#8211;cached&quot;. This option could be reverted with <code>&#8211;ita-visible-in-index</code>. Both options are experimental and could be removed in future.</dl>
<p> For more detailed explanation on these common options, see also <code><a href="/docs/linux/man/7-gitdiffcore/">gitdiffcore</a></code>(7).</p>
<h2>GENERATING PATCH TEXT WITH -P</h2>
<p> Running <code><a href="/docs/linux/man/1-git-diff/">git-diff</a></code>(1), <code><a href="/docs/linux/man/1-git-log/">git-log</a></code>(1), <code><a href="/docs/linux/man/1-git-show/">git-show</a></code>(1), <code><a href="/docs/linux/man/1-git-diff-index/">git-diff-index</a></code>(1), <code><a href="/docs/linux/man/1-git-diff-tree/">git-diff-tree</a></code>(1), or <code><a href="/docs/linux/man/1-git-diff-files/">git-diff-files</a></code>(1) with the <code>-p</code> option produces patch text. You can customize the creation of patch text via the <code>GIT_EXTERNAL_DIFF</code> and the <code>GIT_DIFF_OPTS</code> environment variables (see <code><a href="/docs/linux/man/1-git/">git</a></code>(1)), and the <code>diff</code> attribute (see <code><a href="/docs/linux/man/5-gitattributes/">gitattributes</a></code>(5)). </p>
<p> What the -p option produces is slightly different from the traditional diff format: </p>
<dl>
<dt>
<dd> 1. It is preceded with a &quot;git diff&quot; header that looks like this: </p>
<dl>
<dt>
<dd>
<pre>
diff --git a/file1 b/file2
</pre>
</dl>
<p> The <code>a/</code> and <code>b/</code> filenames are the same unless rename/copy is involved. Especially, even for a creation or a deletion, <code>/dev/null</code> is <i>not</i> used in place of the <code>a/</code> or <code>b/</code> filenames. </p>
<p> When rename/copy is involved, <code>file1</code> and <code>file2</code> show the name of the source file of the rename/copy and the name of the file that rename/copy produces, respectively.</dl>
<dl>
<dt>
<dd> 2. It is followed by one or more extended header lines: </p>
<dl>
<dt>
<dd>
<pre>
old mode &lt;mode&gt;
new mode &lt;mode&gt;
deleted file mode &lt;mode&gt;
new file mode &lt;mode&gt;
copy from &lt;path&gt;
copy to &lt;path&gt;
rename from &lt;path&gt;
rename to &lt;path&gt;
similarity index &lt;number&gt;
dissimilarity index &lt;number&gt;
index &lt;hash&gt;..&lt;hash&gt; &lt;mode&gt;
</pre>
</dl>
<p> File modes are printed as 6-digit octal numbers including the file type and file permission bits. </p>
<p> Path names in extended headers do not include the <code>a/</code> and <code>b/</code> prefixes. </p>
<p> The similarity index is the percentage of unchanged lines, and the dissimilarity index is the percentage of changed lines. It is a rounded down integer, followed by a percent sign. The similarity index value of 100% is thus reserved for two equal files, while 100% dissimilarity means that no line from the old file made it into the new one. </p>
<p> The index line includes the blob object names before and after the change. The &lt;mode&gt; is included if the file mode does not change; otherwise, separate lines indicate the old and the new mode.</dl>
<dl>
<dt>
<dd> 3. Pathnames with &quot;unusual&quot; characters are quoted as explained for the configuration variable <code>core.quotePath</code> (see <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)).</dl>
<dl>
<dt>
<dd> 4. All the <code>file1</code> files in the output refer to files before the commit, and all the <code>file2</code> files refer to files after the commit. It is incorrect to apply each change to each file sequentially. For example, this patch will swap a and b: </p>
<dl>
<dt>
<dd>
<pre>
diff --git a/a b/b
rename from a
rename to b
diff --git a/b b/a
rename from b
rename to a
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> 5. Hunk headers mention the name of the function to which the hunk applies. See &quot;Defining a custom hunk-header&quot; in <code><a href="/docs/linux/man/5-gitattributes/">gitattributes</a></code>(5) for details of how to tailor to this to specific languages.</dl>
<h2>COMBINED DIFF FORMAT</h2>
<p> Any diff-generating command can take the <code>-c</code> or <code>&#8211;cc</code> option to produce a <i>combined diff</i> when showing a merge. This is the default format when showing merges with <code><a href="/docs/linux/man/1-git-diff/">git-diff</a></code>(1) or <code><a href="/docs/linux/man/1-git-show/">git-show</a></code>(1). Note also that you can give suitable <code>&#8211;diff-merges</code> option to any of these commands to force generation of diffs in specific format. </p>
<p> A &quot;combined diff&quot; format looks like this: </p>
<dl>
<dt>
<dd>
diff&#8211; combined describe.c<br />
    index fabadb8,<br />
    cc95eb0..4866510 &#8212; -a / describe.c++ + b / describe.c<br />
                                                @ @ @-98,<br />
    20 &#8211; 98, 12 + 98, 20 @ @ @ return (a_date &gt; b_date) ? -1 : (a_date == b_date) ? 0<br />
                                                                                  : 1;<br />
}<br />
&#8211; static void describe(char *arg) &#8211; static void describe(struct commit *cmit, int last_one)++ static void describe(char *arg, int last_one)<br />
{<br />
    +unsigned char sha1[20];<br />
    +struct commit *cmit;<br />
    struct commit_list *list;<br />
    static int initialized = 0;<br />
    struct commit_name *n;<br />
    +if (get_sha1(arg, sha1) &lt; 0) + usage(describe_usage);<br />
    +cmit = lookup_commit_reference(sha1);<br />
    +if (!cmit) + usage(describe_usage);<br />
    +if (!initialized)<br />
    {<br />
        initialized = 1;<br />
        for_each_ref(get_name);
</dl>
<dl>
<dt>
<dd> 1. It is preceded with a &quot;git diff&quot; header, that looks like this (when the <code>-c</code> option is used): </p>
<dl>
<dt>
<dd>
<pre>
diff --combined file
</pre>
</dl>
<p> or like this (when the <code>&#8211;cc</code> option is used): </p>
<dl>
<dt>
<dd>
<pre>
diff --cc file
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> 2. It is followed by one or more extended header lines (this example shows a merge with two parents): </p>
<dl>
<dt>
<dd>
<pre>
index &lt;hash&gt;,&lt;hash&gt;..&lt;hash&gt;
mode &lt;mode&gt;,&lt;mode&gt;..&lt;mode&gt;
new file mode &lt;mode&gt;
deleted file mode &lt;mode&gt;,&lt;mode&gt;
</pre>
</dl>
<p> The <code>mode &lt;mode&gt;,&lt;mode&gt;..&lt;mode&gt;</code> line appears only if at least one of the &lt;mode&gt; is different from the rest. Extended headers with information about detected contents movement (renames and copying detection) are designed to work with diff of two &lt;tree-ish&gt; and are not used by combined diff format.</dl>
<dl>
<dt>
<dd> 3. It is followed by two-line from-file/to-file header </p>
<dl>
<dt>
<dd>
<pre>
--- a/file
+++ b/file
</pre>
</dl>
<p> Similar to two-line header for traditional <i>unified</i> diff format, <code>/dev/null</code> is used to signal created or deleted files. </p>
<p> However, if the &#8211;combined-all-paths option is provided, instead of a two-line from-file/to-file you get a N+1 line from-file/to-file header, where N is the number of parents in the merge commit </p>
<dl>
<dt>
<dd>
<pre><code>
-- -a / file-- - a / file-- - a / file++ + b / file
</code></pre>
</dl>
<p> This extended format can be useful if rename or copy detection is active, to allow you to see the original name of the file in different parents.</dl>
<dl>
<dt>
<dd> 4. Chunk header format is modified to prevent people from accidentally feeding it to <code>patch -p1</code>. Combined diff format was created for review of merge commit changes, and was not meant to be applied. The change is similar to the change in the extended <i>index</i> header: </p>
<dl>
<dt>
<dd>
<pre>
@@@ &lt;from-file-range&gt; &lt;from-file-range&gt; &lt;to-file-range&gt; @@@
</pre>
</dl>
<p> There are (number of parents + 1) <code>@</code> characters in the chunk header for combined diff format.</dl>
<p> Unlike the traditional <i>unified</i> diff format, which shows two files A and B with a single column that has <code>&#8211;</code> (minus &#8212; appears in A but removed in B), <code>+</code> (plus &#8212; missing in A but added to B), or <code>&quot; &quot;</code> (space &#8212; unchanged) prefix, this format compares two or more files file1, file2,&#8230; with one file X, and shows how X differs from each of fileN. One column for each of fileN is prepended to the output line to note how X&#8217;s line is different from it. </p>
<p> A <code>&#8211;</code> character in the column N means that the line appears in fileN but it does not appear in the result. A <code>+</code> character in the column N means that the line appears in the result, and fileN does not have that line (in other words, the line was added, from the point of view of that parent). </p>
<p> In the above example output, the function signature was changed from both files (hence two <code>&#8211;</code> removals from both file1 and file2, plus <code>++</code> to mean one line that was added does not appear in either file1 or file2). Also eight other lines are the same from file1 but do not appear in file2 (hence prefixed with <code>+</code>). </p>
<p> When shown by <code>git diff-tree -c</code>, it compares the parents of a merge commit with the merge result (i.e. file1..fileN are the parents). When shown by <code>git diff-files -c</code>, it compares the two unresolved merge parents with the working tree file (i.e. file1 is stage 2 aka &quot;our version&quot;, file2 is stage 3 aka &quot;their version&quot;).</p>
<h2>EXAMPLES</h2>
<p> <code>git show v1.0.0</code></p>
<dl>
<dt>
<dd> Shows the tag <code>v1.0.0</code>, along with the object the tags points at.</dl>
<p> <code>git show v1.0.0^{tree}</code></p>
<dl>
<dt>
<dd> Shows the tree pointed to by the tag <code>v1.0.0</code>.</dl>
<p> <code>git show -s &#8211;format=%s v1.0.0^{commit}</code></p>
<dl>
<dt>
<dd> Shows the subject of the commit pointed to by the tag <code>v1.0.0</code>.</dl>
<p> <code>git show next~10:Documentation/README</code></p>
<dl>
<dt>
<dd> Shows the contents of the file <code>Documentation/README</code> as they were current in the 10th last commit of the branch <code>next</code>.</dl>
<p> <code>git show master:Makefile master:t/Makefile</code></p>
<dl>
<dt>
<dd> Concatenates the contents of said Makefiles in the head of the branch <code>master</code>.</dl>
<h2>DISCUSSION</h2>
<p> Git is to some extent character encoding agnostic. </p>
<dl>
<dt>
<dd> &bull; The contents of the blob objects are uninterpreted sequences of bytes. There is no encoding translation at the core level.</dl>
<dl>
<dt>
<dd> &bull; Path names are encoded in UTF-8 normalization form C. This applies to tree objects, the index file, ref names, as well as path names in command line arguments, environment variables and config files (<code>.git/config</code> (see <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)), <code><a href="/docs/linux/man/5-gitignore/">gitignore</a></code>(5), <code><a href="/docs/linux/man/5-gitattributes/">gitattributes</a></code>(5) and <code><a href="/docs/linux/man/5-gitmodules/">gitmodules</a></code>(5)). </p>
<p> Note that Git at the core level treats path names simply as sequences of non-NUL bytes, there are no path name encoding conversions (except on Mac and Windows). Therefore, using non-ASCII path names will mostly work even on platforms and file systems that use legacy extended ASCII encodings. However, repositories created on such systems will not work properly on UTF-8-based systems (e.g. Linux, Mac, Windows) and vice versa. Additionally, many Git-based tools simply assume path names to be UTF-8 and will fail to display other encodings correctly.</dl>
<dl>
<dt>
<dd> &bull; Commit log messages are typically encoded in UTF-8, but other extended ASCII encodings are also supported. This includes ISO-8859-x, CP125x and many others, but <i>not</i> UTF-16/32, EBCDIC and CJK multi-byte encodings (GBK, Shift-JIS, Big5, EUC-x, CP9xx etc.).</dl>
<p> Although we encourage that the commit log messages are encoded in UTF-8, both the core and Git Porcelain are designed not to force UTF-8 on projects. If all participants of a particular project find it more convenient to use legacy encodings, Git does not forbid it. However, there are a few things to keep in mind. </p>
<dl>
<dt>
<dd> 1. <i>git commit</i> and <i>git commit-tree</i> issues a warning if the commit log message given to it does not look like a valid UTF-8 string, unless you explicitly say your project uses a legacy encoding. The way to say this is to have <code>i18n.commitEncoding</code> in <code>.git/config</code> file, like this: </p>
<dl>
<dt>
<dd>
<pre>
[i18n]
        commitEncoding = ISO-8859-1
</pre>
</dl>
<p> Commit objects created with the above setting record the value of <code>i18n.commitEncoding</code> in its <code>encoding</code> header. This is to help other people who look at them later. Lack of this header implies that the commit log message is encoded in UTF-8.</dl>
<dl>
<dt>
<dd> 2. <i>git log</i>, <i>git show</i>, <i>git blame</i> and friends look at the <code>encoding</code> header of a commit object, and try to re-code the log message into UTF-8 unless otherwise specified. You can specify the desired output encoding with <code>i18n.logOutputEncoding</code> in <code>.git/config</code> file, like this: </p>
<dl>
<dt>
<dd>
<pre>
[i18n]
        logOutputEncoding = ISO-8859-1
</pre>
</dl>
<p> If you do not have this configuration variable, the value of <code>i18n.commitEncoding</code> is used instead.</dl>
<p> Note that we deliberately chose not to re-code the commit log message when a commit is made to force UTF-8 at the commit object level, because re-coding to UTF-8 is not necessarily a reversible operation.</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
