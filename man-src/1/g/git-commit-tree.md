---
title: "git-commit-tree(1)"
name: "git-commit-tree"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-commit-tree/"
description: "git-commit-tree – Create a new commit object"
---

<h2 class="name">NAME</h2>
<p> git-commit-tree &#8211; Create a new commit object </p>
<h2>SYNOPSIS</h2>
<pre><code>
git commit - tree&lt;tree&gt;[(-p&lt;parent&gt;)...] git commit - tree[(-p&lt;parent&gt;)...][-S[&lt;keyid&gt;]][(-m&lt;message&gt;)...][(-F&lt;file&gt;)...]&lt;tree&gt;
</code></pre>
<h2>DESCRIPTION</h2>
<p> This is usually not what an end user wants to run directly. See <code><a href="/docs/linux/man/1-git-commit/">git-commit</a></code>(1) instead. </p>
<p> Creates a new commit object based on the provided tree object and emits the new commit object id on stdout. The log message is read from the standard input, unless <code>-m</code> or <code>-F</code> options are given. </p>
<p> The <code>-m</code> and <code>-F</code> options can be given any number of times, in any order. The commit log message will be composed in the order in which the options are given. </p>
<p> A commit object may have any number of parents. With exactly one parent, it is an ordinary commit. Having more than one parent makes the commit a merge between several lines of history. Initial (root) commits have no parents. </p>
<p> While a tree represents a particular directory state of a working directory, a commit represents that state in &quot;time&quot;, and explains how to get there. </p>
<p> Normally a commit would identify a new &quot;HEAD&quot; state, and while Git doesn&#8217;t care where you save the note about that state, in practice we tend to just write the result to the file that is pointed at by <code>.git/HEAD</code>, so that we can always see what the last committed state was.</p>
<h2>OPTIONS</h2>
<p> &lt;tree&gt;</p>
<dl>
<dt>
<dd> An existing tree object.</dl>
<p> -p &lt;parent&gt;</p>
<dl>
<dt>
<dd> Each <code>-p</code> indicates the id of a parent commit object.</dl>
<p> -m &lt;message&gt;</p>
<dl>
<dt>
<dd> A paragraph in the commit log message. This can be given more than once and each &lt;message&gt; becomes its own paragraph.</dl>
<p> -F &lt;file&gt;</p>
<dl>
<dt>
<dd> Read the commit log message from the given file. Use <code>&#8211;</code> to read from the standard input. This can be given more than once and the content of each file becomes its own paragraph.</dl>
<p> -S[&lt;keyid&gt;], &#8211;gpg-sign[=&lt;keyid&gt;], &#8211;no-gpg-sign</p>
<dl>
<dt>
<dd> GPG-sign commits. The <code>keyid</code> argument is optional and defaults to the committer identity; if specified, it must be stuck to the option without a space. <code>&#8211;no-gpg-sign</code> is useful to countermand a <code>&#8211;gpg-sign</code> option given earlier on the command line.</dl>
<h2>COMMIT INFORMATION</h2>
<p> A commit encapsulates: </p>
<dl>
<dt>
<dd> &bull; all parent object ids</dl>
<dl>
<dt>
<dd> &bull; author name, email and date</dl>
<dl>
<dt>
<dd> &bull; committer name and email and the commit time.</dl>
<p> A commit comment is read from stdin. If a changelog entry is not provided via &quot;&lt;&quot; redirection, <i>git commit-tree</i> will just wait for one to be entered and terminated with ^D.</p>
<h2>DATE FORMATS</h2>
<p> The <code>GIT_AUTHOR_DATE</code> and <code>GIT_COMMITTER_DATE</code> environment variables support the following date formats: </p>
<p> Git internal format</p>
<dl>
<dt>
<dd> It is <code>&lt;unix timestamp&gt; &lt;time zone offset&gt;</code>, where <code>&lt;unix timestamp&gt;</code> is the number of seconds since the UNIX epoch. <code>&lt;time zone offset&gt;</code> is a positive or negative offset from UTC. For example CET (which is 1 hour ahead of UTC) is <code>+0100</code>.</dl>
<p> RFC 2822</p>
<dl>
<dt>
<dd> The standard email format as described by RFC 2822, for example <code>Thu, 07 Apr 2005 22:13:13 +0200</code>.</dl>
<p> ISO 8601</p>
<dl>
<dt>
<dd> Time and date specified by the ISO 8601 standard, for example <code>2005-04-07T22:13:13</code>. The parser accepts a space instead of the <code>T</code> character as well. Fractional parts of a second will be ignored, for example <code>2005-04-07T22:13:13.019</code> will be treated as <code>2005-04-07T22:13:13</code>. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font><br />
 In addition, the date part is accepted in the following formats: <code>YYYY.MM.DD</code>, <code>MM/DD/YYYY</code> and <code>DD.MM.YYYY</code>. </p>
</dl>
</dl>
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
<h2>FILES</h2>
<p> /etc/mailname</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-git-write-tree/">git-write-tree</a></code>(1) <code><a href="/docs/linux/man/1-git-commit/">git-commit</a></code>(1)</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
