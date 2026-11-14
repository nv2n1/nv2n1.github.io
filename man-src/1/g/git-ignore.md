---
title: "git-ignore(1)"
name: "git-ignore"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-ignore/"
description: "git-ignore – Add .gitignore patterns"
---

<h2>NAME</h2>
<p> <code>git-ignore</code> &#8211; Add .gitignore patterns</p>
<h2>SYNOPSIS</h2>
<p> <code>git-ignore</code> [&lt;context&gt;] [&lt;pattern&gt; [&lt;pattern&gt;]&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> Adds the given _pattern_s to a .gitignore file if it doesn&#8217;t already exist.</p>
<h2>OPTIONS</h2>
<p> &lt;context&gt; </p>
<p> -l, &#8211;local </p>
<p> Sets the context to the .gitignore file in the current working directory. (default) </p>
<p> -g, &#8211;global </p>
<p> Sets the context to the global gitignore file for the current user. </p>
<p> &lt;pattern&gt; </p>
<p> A space delimited list of patterns to append to the file in context.</p>
<h3>PATTERN FORMAT</h3>
<p> Pattern format as described in the git manual</p>
<dl>
<dt>&bull;</p>
<dd> A blank line matches no files, so it can serve as a separator for readability. To append a blank line use empty quotes &quot;&quot;.</p>
<dt>&bull;</p>
<dd> A line starting with # serves as a comment. For example, &quot;# This is a comment&quot;</p>
<dt>&bull;</p>
<dd> An optional prefix ! which negates the pattern; any matching file excluded by a previous pattern will become included again. If a negated pattern matches, this will override lower precedence patterns sources. To use an exclamation ! as command line argument it is best placed between single quotes &#8221;. For example, &#8216;!src&#8217;</p>
<dt>&bull;</p>
<dd> If the pattern ends with a slash, it is removed for the purpose of the following description, but it would only find a match with a directory. In other words, foo/ will match a directory foo and paths underneath it, but will not match a regular file or a symbolic link foo (this is consistent with the way how pathspec works in general in git).</p>
<dt>&bull;</p>
<dd> If the pattern does not contain a slash /, git treats it as a shell glob pattern and checks for a match against the pathname relative to the location of the .gitignore file (relative to the toplevel of the work tree if not from a .gitignore file).</p>
<dt>&bull;</p>
<dd> Otherwise, git treats the pattern as a shell glob suitable for consumption by <a href="/docs/linux/man/3-fnmatch/">fnmatch</a>(3) with the FNM_PATHNAME flag: wildcards in the pattern will not match a / in the pathname. For example, &quot;Documentation/*.html&quot; matches &quot;Documentation/git.html&quot; but not &quot;Documentation/ppc/ppc.html&quot; or &quot;tools/perf/Documentation/perf.html&quot;.</p>
<dt>&bull;</p>
<dd> A leading slash matches the beginning of the pathname. For example, &quot;/*.c&quot; matches &quot;cat-file.c&quot; but not &quot;mozilla-sha1/sha1.c&quot;.</p>
<dt>
<dd></dl>
<h2>EXAMPLES</h2>
<p> All arguments are optional so calling git-ignore alone will display first the global then the local gitignore files:</p>
<dl>
<dt>
<dd>
<pre><code>
$ git ignore
            Global gitignore : /
                               home / alice /.gitignore
#Numerous always - ignore extensions
                                                 *.diff *.err *.orig *.rej *.swo *.swp *.vi *
                               ~*.sass -
    cache
#OS or Editor folders
        .DS_Store
        .Trashes
        ._ *
            Thumbs.db-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -Local gitignore :.gitignore
        .cache
        .project
        .settings
        .tmproj
                                                                                           nbproject
</code></pre>
<dt>
<dd></dl>
<p> If you only want to see the global context use the &#8211;global argument (for local use &#8211;local):</p>
<dl>
<dt>
<dd>
<pre>
$ git ignore
Global gitignore: /home/alice/.gitignore
.DS_Store
.Trashes
._*
Thumbs.db
</pre>
<dt>
<dd></dl>
<p> To quickly append a new pattern to the default/local context simply:</p>
<dl>
<dt>
<dd>
<pre>
$ git ignore *.log
Adding pattern(s) to: .gitignore
... adding '*.log'
</pre>
<dt>
<dd></dl>
<p> You can now configure any patterns without ever using an editor, with a context and pattern arguments: The resulting configuration is also returned for your convenience.</p>
<dl>
<dt>
<dd>
<pre>
$ git ignore --local &quot;&quot; &quot;# Temporary files&quot; *.tmp &quot;*.log&quot; tmp/*  &quot;&quot; &quot;# Files I'd like to keep&quot; '!work'  &quot;&quot;
Adding pattern(s) to: .gitignore
... adding ''
... adding '# Temporary files'
... adding 'index.tmp'
... adding '*.log'
... adding 'tmp/*'
... adding ''
... adding '# Files I'd like to keep'
... adding '!work'
... adding ''
Local gitignore: .gitignore
# Temporary files
index.tmp
*.log
# Files I'd like to keep
!work
</pre>
<dt>
<dd></dl>
<h2>AUTHOR</h2>
<p> Written by Tj Holowaychuk &lt;<i>tj [at] vision-media.ca</i>&gt; and Tema Bolshakov &lt;<i>tweekane [at] gmail.com</i>&gt; and Nick Lombard &lt;<i>github [at] jigsoft.co.za</i>&gt;</p>
<h2>REPORTING BUGS</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras/issues">https://github.com/tj/git-extras/issues</a></i>&gt;</p>
<h2>SEE ALSO</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras">https://github.com/tj/git-extras</a></i>&gt; </p>
<h2>Index</h2>
