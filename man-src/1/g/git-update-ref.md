---
title: "git-update-ref(1)"
name: "git-update-ref"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-update-ref/"
description: "git-update-ref – Update the object name stored in a ref safely"
---

<h2 class="name">NAME</h2>
<p> git-update-ref &#8211; Update the object name stored in a ref safely </p>
<h2>SYNOPSIS</h2>
<pre><code>
git update - ref[-m&lt;reason&gt;][--no - deref](-d&lt;ref&gt;[&lt;oldvalue&gt;] | [--create - reflog]&lt;ref&gt;&lt;newvalue&gt;[&lt;oldvalue&gt;] | --stdin[-z])
</code></pre>
<h2>DESCRIPTION</h2>
<p> Given two arguments, stores the &lt;newvalue&gt; in the &lt;ref&gt;, possibly dereferencing the symbolic refs. E.g. <code>git update-ref HEAD &lt;newvalue&gt;</code> updates the current branch head to the new object. </p>
<p> Given three arguments, stores the &lt;newvalue&gt; in the &lt;ref&gt;, possibly dereferencing the symbolic refs, after verifying that the current value of the &lt;ref&gt; matches &lt;oldvalue&gt;. E.g. <code>git update-ref refs/heads/master &lt;newvalue&gt; &lt;oldvalue&gt;</code> updates the master branch head to &lt;newvalue&gt; only if its current value is &lt;oldvalue&gt;. You can specify 40 &quot;0&quot; or an empty string as &lt;oldvalue&gt; to make sure that the ref you are creating does not exist. </p>
<p> It also allows a &quot;ref&quot; file to be a symbolic pointer to another ref file by starting with the four-byte header sequence of &quot;ref:&quot;. </p>
<p> More importantly, it allows the update of a ref file to follow these symbolic pointers, whether they are symlinks or these &quot;regular file symbolic refs&quot;. It follows <code>real</code> symlinks only if they start with &quot;refs/&quot;: otherwise it will just try to read them and update them as a regular file (i.e. it will allow the filesystem to follow them, but will overwrite such a symlink to somewhere else with a regular filename). </p>
<p> If &#8211;no-deref is given, &lt;ref&gt; itself is overwritten, rather than the result of following the symbolic pointers. </p>
<p> In general, using </p>
<dl>
<dt>
<dd>
<pre>
git update-ref HEAD &quot;$head&quot;
</pre>
</dl>
<p> should be a <i>lot</i> safer than doing </p>
<dl>
<dt>
<dd>
<pre>
echo &quot;$head&quot; &gt; &quot;$GIT_DIR/HEAD&quot;
</pre>
</dl>
<p> both from a symlink following standpoint <code>and</code> an error checking standpoint. The &quot;refs/&quot; rule for symlinks means that symlinks that point to &quot;outside&quot; the tree are safe: they&#8217;ll be followed for reading but not for writing (so we&#8217;ll never write through a ref symlink to some other tree, if you have copied a whole archive by creating a symlink tree). </p>
<p> With <code>-d</code> flag, it deletes the named &lt;ref&gt; after verifying it still contains &lt;oldvalue&gt;. </p>
<p> With <code>&#8211;stdin</code>, update-ref reads instructions from standard input and performs all modifications together. Specify commands of the form: </p>
<dl>
<dt>
<dd>
update SP&lt;ref&gt; SP&lt;newvalue&gt;[SP&lt;oldvalue&gt;] LF<br />
    create SP&lt;ref&gt;<br />
        SP&lt;newvalue&gt; LF delete SP&lt;ref&gt;[SP&lt;oldvalue&gt;] LF<br />
            verify SP&lt;ref&gt;[SP&lt;oldvalue&gt;] LF<br />
                option SP&lt;opt&gt;<br />
                    LF<br />
                        start LF<br />
                            prepare LF<br />
                                commit LF<br />
                                    abort LF
</dl>
<p> With <code>&#8211;create-reflog</code>, update-ref will create a reflog for each ref even if one would not ordinarily be created. </p>
<p> Quote fields containing whitespace as if they were strings in C source code; i.e., surrounded by double-quotes and with backslash escapes. Use 40 &quot;0&quot; characters or the empty string to specify a zero value. To specify a missing value, omit the value and its preceding SP entirely. </p>
<p> Alternatively, use <code>-z</code> to specify in NUL-terminated format, without quoting: </p>
<dl>
<dt>
<dd>
<pre><code>
update SP&lt;ref&gt; NUL&lt;newvalue&gt; NUL[&lt;oldvalue&gt;] NUL
    create SP&lt;ref&gt;
        NUL&lt;newvalue&gt; NUL delete SP&lt;ref&gt; NUL[&lt;oldvalue&gt;] NUL
            verify SP&lt;ref&gt;
                NUL[&lt;oldvalue&gt;] NUL
                    option SP&lt;opt&gt;
                        NUL
                            start NUL
                                prepare NUL
                                    commit NUL
                                        abort NUL
</code></pre>
</dl>
<p> In this format, use 40 &quot;0&quot; to specify a zero value, and use the empty string to specify a missing value. </p>
<p> In either format, values can be specified in any form that Git recognizes as an object name. Commands in any other format or a repeated &lt;ref&gt; produce an error. Command meanings are: </p>
<p> update</p>
<dl>
<dt>
<dd> Set &lt;ref&gt; to &lt;newvalue&gt; after verifying &lt;oldvalue&gt;, if given. Specify a zero &lt;newvalue&gt; to ensure the ref does not exist after the update and/or a zero &lt;oldvalue&gt; to make sure the ref does not exist before the update.</dl>
<p> create</p>
<dl>
<dt>
<dd> Create &lt;ref&gt; with &lt;newvalue&gt; after verifying it does not exist. The given &lt;newvalue&gt; may not be zero.</dl>
<p> delete</p>
<dl>
<dt>
<dd> Delete &lt;ref&gt; after verifying it exists with &lt;oldvalue&gt;, if given. If given, &lt;oldvalue&gt; may not be zero.</dl>
<p> verify</p>
<dl>
<dt>
<dd> Verify &lt;ref&gt; against &lt;oldvalue&gt; but do not change it. If &lt;oldvalue&gt; is zero or missing, the ref must not exist.</dl>
<p> option</p>
<dl>
<dt>
<dd> Modify behavior of the next command naming a &lt;ref&gt;. The only valid option is <code>no-deref</code> to avoid dereferencing a symbolic ref.</dl>
<p> start</p>
<dl>
<dt>
<dd> Start a transaction. In contrast to a non-transactional session, a transaction will automatically abort if the session ends without an explicit commit. This command may create a new empty transaction when the current one has been committed or aborted already.</dl>
<p> prepare</p>
<dl>
<dt>
<dd> Prepare to commit the transaction. This will create lock files for all queued reference updates. If one reference could not be locked, the transaction will be aborted.</dl>
<p> commit</p>
<dl>
<dt>
<dd> Commit all reference updates queued for the transaction, ending the transaction.</dl>
<p> abort</p>
<dl>
<dt>
<dd> Abort the transaction, releasing all locks if the transaction is in prepared state.</dl>
<p> If all &lt;ref&gt;s can be locked with matching &lt;oldvalue&gt;s simultaneously, all modifications are performed. Otherwise, no modifications are performed. Note that while each individual &lt;ref&gt; is updated or deleted atomically, a concurrent reader may still see a subset of the modifications.</p>
<h2>LOGGING UPDATES</h2>
<p> If config parameter &quot;core.logAllRefUpdates&quot; is true and the ref is one under &quot;refs/heads/&quot;, &quot;refs/remotes/&quot;, &quot;refs/notes/&quot;, or a pseudoref like HEAD or ORIG_HEAD; or the file &quot;$GIT_DIR/logs/&lt;ref&gt;&quot; exists then <code>git update-ref</code> will append a line to the log file &quot;$GIT_DIR/logs/&lt;ref&gt;&quot; (dereferencing all symbolic refs before creating the log name) describing the change in ref value. Log lines are formatted as: </p>
<dl>
<dt>
<dd>
<pre>
oldsha1 SP newsha1 SP committer LF
</pre>
</dl>
<p> Where &quot;oldsha1&quot; is the 40 character hexadecimal value previously stored in &lt;ref&gt;, &quot;newsha1&quot; is the 40 character hexadecimal value of &lt;newvalue&gt; and &quot;committer&quot; is the committer&#8217;s name, email address and date in the standard Git committer ident format. </p>
<p> Optionally with -m: </p>
<dl>
<dt>
<dd>
<pre>
oldsha1 SP newsha1 SP committer TAB message LF
</pre>
</dl>
<p> Where all fields are as described above and &quot;message&quot; is the value supplied to the -m option. </p>
<p> An update will fail (without changing &lt;ref&gt;) if the current user is unable to create a new log file, append to the existing log file or does not have committer information available.</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
