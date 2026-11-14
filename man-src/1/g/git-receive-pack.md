---
title: "git-receive-pack(1)"
name: "git-receive-pack"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-receive-pack/"
description: "git-receive-pack – Receive what is pushed into the repository"
---

<h2 class="name">NAME</h2>
<p> git-receive-pack &#8211; Receive what is pushed into the repository </p>
<h2>SYNOPSIS</h2>
<pre>
<i>git-receive-pack</i> &lt;directory&gt;
</pre>
<h2>DESCRIPTION</h2>
<p> Invoked by <i>git send-pack</i> and updates the repository with the information fed from the remote end. </p>
<p> This command is usually not invoked directly by the end user. The UI for the protocol is on the <i>git send-pack</i> side, and the program pair is meant to be used to push updates to remote repository. For pull operations, see <code><a href="/docs/linux/man/1-git-fetch-pack/">git-fetch-pack</a></code>(1). </p>
<p> The command allows for creation and fast-forwarding of sha1 refs (heads/tags) on the remote end (strictly speaking, it is the local end <i>git-receive-pack</i> runs, but to the user who is sitting at the send-pack end, it is updating the remote. Confused?) </p>
<p> There are other real-world examples of using update and post-update hooks found in the Documentation/howto directory. </p>
<p> <i>git-receive-pack</i> honours the receive.denyNonFastForwards config option, which tells it if updates to a ref should be denied if they are not fast-forwards. </p>
<p> A number of other receive.* config options are available to tweak its behavior, see <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1).</p>
<h2>OPTIONS</h2>
<p> &lt;directory&gt;</p>
<dl>
<dt>
<dd> The repository to sync into.</dl>
<p> &#8211;http-backend-info-refs</p>
<dl>
<dt>
<dd> Used by <code><a href="/docs/linux/man/1-git-http-backend/">git-http-backend</a></code>(1) to serve up <code>$GIT_URL/info/refs?service=git-receive-pack</code> requests. See <code>&#8211;http-backend-info-refs</code> in <code><a href="/docs/linux/man/1-git-upload-pack/">git-upload-pack</a></code>(1).</dl>
<h2>PRE-RECEIVE HOOK</h2>
<p> Before any ref is updated, if $GIT_DIR/hooks/pre-receive file exists and is executable, it will be invoked once with no parameters. The standard input of the hook will be one line per ref to be updated: </p>
<dl>
<dt>
<dd>
<pre>
sha1-old SP sha1-new SP refname LF
</pre>
</dl>
<p> The refname value is relative to $GIT_DIR; e.g. for the master head this is &quot;refs/heads/master&quot;. The two sha1 values before each refname are the object names for the refname before and after the update. Refs to be created will have sha1-old equal to 0{40}, while refs to be deleted will have sha1-new equal to 0{40}, otherwise sha1-old and sha1-new should be valid objects in the repository. </p>
<p> When accepting a signed push (see <code><a href="/docs/linux/man/1-git-push/">git-push</a></code>(1)), the signed push certificate is stored in a blob and an environment variable <code>GIT_PUSH_CERT</code> can be consulted for its object name. See the description of <code>post-receive</code> hook for an example. In addition, the certificate is verified using GPG and the result is exported with the following environment variables: </p>
<p> <code>GIT_PUSH_CERT_SIGNER</code></p>
<dl>
<dt>
<dd> The name and the e-mail address of the owner of the key that signed the push certificate.</dl>
<p> <code>GIT_PUSH_CERT_KEY</code></p>
<dl>
<dt>
<dd> The GPG key ID of the key that signed the push certificate.</dl>
<p> <code>GIT_PUSH_CERT_STATUS</code></p>
<dl>
<dt>
<dd> The status of GPG verification of the push certificate, using the same mnemonic as used in <code>%G?</code> format of <code>git log</code> family of commands (see <code><a href="/docs/linux/man/1-git-log/">git-log</a></code>(1)).</dl>
<p> <code>GIT_PUSH_CERT_NONCE</code></p>
<dl>
<dt>
<dd> The nonce string the process asked the signer to include in the push certificate. If this does not match the value recorded on the &quot;nonce&quot; header in the push certificate, it may indicate that the certificate is a valid one that is being replayed from a separate &quot;git push&quot; session.</dl>
<p> <code>GIT_PUSH_CERT_NONCE_STATUS</code></p>
<dl>
<dt>
<dd>
<p> <code>UNSOLICITED</code></p>
<dl>
<dt>
<dd> &quot;git push &#8211;signed&quot; sent a nonce when we did not ask it to send one.</dl>
<p> <code>MISSING</code></p>
<dl>
<dt>
<dd> &quot;git push &#8211;signed&quot; did not send any nonce header.</dl>
<p> <code>BAD</code></p>
<dl>
<dt>
<dd> &quot;git push &#8211;signed&quot; sent a bogus nonce.</dl>
<p> <code>OK</code></p>
<dl>
<dt>
<dd> &quot;git push &#8211;signed&quot; sent the nonce we asked it to send.</dl>
<p> <code>SLOP</code></p>
<dl>
<dt>
<dd> &quot;git push &#8211;signed&quot; sent a nonce different from what we asked it to send now, but in a previous session. See <code>GIT_PUSH_CERT_NONCE_SLOP</code> environment variable.</dl>
</dl>
<p> <code>GIT_PUSH_CERT_NONCE_SLOP</code></p>
<dl>
<dt>
<dd> &quot;git push &#8211;signed&quot; sent a nonce different from what we asked it to send now, but in a different session whose starting time is different by this many seconds from the current session. Only meaningful when <code>GIT_PUSH_CERT_NONCE_STATUS</code> says <code>SLOP</code>. Also read about <code>receive.certNonceSlop</code> variable in <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1).</dl>
<p> This hook is called before any refname is updated and before any fast-forward checks are performed. </p>
<p> If the pre-receive hook exits with a non-zero exit status no updates will be performed, and the update, post-receive and post-update hooks will not be invoked either. This can be useful to quickly bail out if the update is not to be supported. </p>
<p> See the notes on the quarantine environment below.</p>
<h2>UPDATE HOOK</h2>
<p> Before each ref is updated, if $GIT_DIR/hooks/update file exists and is executable, it is invoked once per ref, with three parameters: </p>
<dl>
<dt>
<dd>
<pre>
$GIT_DIR/hooks/update refname sha1-old sha1-new
</pre>
</dl>
<p> The refname parameter is relative to $GIT_DIR; e.g. for the master head this is &quot;refs/heads/master&quot;. The two sha1 arguments are the object names for the refname before and after the update. Note that the hook is called before the refname is updated, so either sha1-old is 0{40} (meaning there is no such ref yet), or it should match what is recorded in refname. </p>
<p> The hook should exit with non-zero status if it wants to disallow updating the named ref. Otherwise it should exit with zero. </p>
<p> Successful execution (a zero exit status) of this hook does not ensure the ref will actually be updated, it is only a prerequisite. As such it is not a good idea to send notices (e.g. email) from this hook. Consider using the post-receive hook instead.</p>
<h2>POST-RECEIVE HOOK</h2>
<p> After all refs were updated (or attempted to be updated), if any ref update was successful, and if $GIT_DIR/hooks/post-receive file exists and is executable, it will be invoked once with no parameters. The standard input of the hook will be one line for each successfully updated ref: </p>
<dl>
<dt>
<dd>
<pre>
sha1-old SP sha1-new SP refname LF
</pre>
</dl>
<p> The refname value is relative to $GIT_DIR; e.g. for the master head this is &quot;refs/heads/master&quot;. The two sha1 values before each refname are the object names for the refname before and after the update. Refs that were created will have sha1-old equal to 0{40}, while refs that were deleted will have sha1-new equal to 0{40}, otherwise sha1-old and sha1-new should be valid objects in the repository. </p>
<p> The <code>GIT_PUSH_CERT*</code> environment variables can be inspected, just as in <code>pre-receive</code> hook, after accepting a signed push. </p>
<p> Using this hook, it is easy to generate mails describing the updates to the repository. This example script sends one mail message per ref listing the commits pushed to the repository, and logs the push certificates of signed pushes with good signatures to a logger service: </p>
<dl>
<dt>
<dd>
<pre><code>
#!/ bin / sh
#mail out commit update information.
while
read oval nval ref do if expr "$oval" : '0*$' &gt; / dev / null then echo "Created a new ref, with the following commits:" git rev - list-- pretty "$nval" else echo "New commits:" git rev - list-- pretty "$nval"
                                                                                                                                                                                                         "^$oval" fi |
        mail - s "Changes to ref $ref" commit - list[at] mydomain done
#log signed push certificate, if any
            if test -
            n "${GIT_PUSH_CERT-}" &amp;&amp;
    test ${GIT_PUSH_CERT_STATUS} = G
                                   then(
                                       echo expected nonce is ${GIT_PUSH_NONCE} git cat - file blob ${GIT_PUSH_CERT}) |
                                   mail - s "push certificate from $GIT_PUSH_CERT_SIGNER" push - log[at] mydomain fi exit 0
</code></pre>
</dl>
<p> The exit code from this hook invocation is ignored, however a non-zero exit code will generate an error message. </p>
<p> Note that it is possible for refname to not have sha1-new when this hook runs. This can easily occur if another user modifies the ref after it was updated by <i>git-receive-pack</i>, but before the hook was able to evaluate it. It is recommended that hooks rely on sha1-new rather than the current value of refname.</p>
<h2>POST-UPDATE HOOK</h2>
<p> After all other processing, if at least one ref was updated, and if $GIT_DIR/hooks/post-update file exists and is executable, then post-update will be called with the list of refs that have been updated. This can be used to implement any repository wide cleanup tasks. </p>
<p> The exit code from this hook invocation is ignored; the only thing left for <i>git-receive-pack</i> to do at that point is to exit itself anyway. </p>
<p> This hook can be used, for example, to run <code>git update-server-info</code> if the repository is packed and is served via a dumb transport. </p>
<dl>
<dt>
<dd>
<pre>
#!/bin/sh
exec git update-server-info
</pre>
</dl>
<h2>QUARANTINE ENVIRONMENT</h2>
<p> When <code>receive-pack</code> takes in objects, they are placed into a temporary &quot;quarantine&quot; directory within the <code>$GIT_DIR/objects</code> directory and migrated into the main object store only after the <code>pre-receive</code> hook has completed. If the push fails before then, the temporary directory is removed entirely. </p>
<p> This has a few user-visible effects and caveats: </p>
<dl>
<dt>
<dd> 1. Pushes which fail due to problems with the incoming pack, missing objects, or due to the <code>pre-receive</code> hook will not leave any on-disk data. This is usually helpful to prevent repeated failed pushes from filling up your disk, but can make debugging more challenging.</dl>
<dl>
<dt>
<dd> 2. Any objects created by the <code>pre-receive</code> hook will be created in the quarantine directory (and migrated only if it succeeds).</dl>
<dl>
<dt>
<dd> 3. The <code>pre-receive</code> hook MUST NOT update any refs to point to quarantined objects. Other programs accessing the repository will not be able to see the objects (and if the pre-receive hook fails, those refs would become corrupted). For safety, any ref updates from within <code>pre-receive</code> are automatically rejected.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-git-send-pack/">git-send-pack</a></code>(1), <code><a href="/docs/linux/man/7-gitnamespaces/">gitnamespaces</a></code>(7)</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
