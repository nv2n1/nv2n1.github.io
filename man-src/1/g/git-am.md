---
title: "git-am(1)"
name: "git-am"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-am/"
description: "git-am – Apply a series of patches from a mailbox"
---

<h2 class="name">NAME</h2>
<p> git-am &#8211; Apply a series of patches from a mailbox </p>
<h2>SYNOPSIS</h2>
<pre><code>
git am[--signoff][--keep][--[no - ] keep - cr][--[no - ] utf8]
      [--[no - ] 3way][--interactive][--committer - date - is - author - date]
      [--ignore - date][--ignore - space - change | --ignore - whitespace]
      [--whitespace = &lt;option&gt;][-C&lt;n&gt;][-p&lt;n&gt;][--directory = &lt;dir&gt;]
      [--exclude = &lt;path&gt;][--include = &lt;path&gt;][--reject][-q | --quiet]
      [--[no - ] scissors][-S[&lt;keyid&gt;]][--patch - format = &lt;format&gt;]
      [--quoted - cr = &lt;action&gt;]
      [(&lt;mbox&gt; | &lt;Maildir&gt;)...] git am(--continue | --skip | --abort | --quit | --show - current - patch[=(diff | raw)])
</code></pre>
<h2>DESCRIPTION</h2>
<p> Splits mail messages in a mailbox into commit log message, authorship information and patches, and applies them to the current branch.</p>
<h2>OPTIONS</h2>
<p> (&lt;mbox&gt;|&lt;Maildir&gt;)&#8230;</p>
<dl>
<dt>
<dd> The list of mailbox files to read patches from. If you do not supply this argument, the command reads from the standard input. If you supply directories, they will be treated as Maildirs.</dl>
<p> -s, &#8211;signoff</p>
<dl>
<dt>
<dd> Add a <code>Signed-off-by</code> trailer to the commit message, using the committer identity of yourself. See the signoff option in <code><a href="/docs/linux/man/1-git-commit/">git-commit</a></code>(1) for more information.</dl>
<p> -k, &#8211;keep</p>
<dl>
<dt>
<dd> Pass <code>-k</code> flag to <i>git mailinfo</i> (see <code><a href="/docs/linux/man/1-git-mailinfo/">git-mailinfo</a></code>(1)).</dl>
<p> &#8211;keep-non-patch</p>
<dl>
<dt>
<dd> Pass <code>-b</code> flag to <i>git mailinfo</i> (see <code><a href="/docs/linux/man/1-git-mailinfo/">git-mailinfo</a></code>(1)).</dl>
<p> &#8211;[no-]keep-cr</p>
<dl>
<dt>
<dd> With <code>&#8211;keep-cr</code>, call <i>git mailsplit</i> (see <code><a href="/docs/linux/man/1-git-mailsplit/">git-mailsplit</a></code>(1)) with the same option, to prevent it from stripping CR at the end of lines. <code>am.keepcr</code> configuration variable can be used to specify the default behaviour. <code>&#8211;no-keep-cr</code> is useful to override <code>am.keepcr</code>.</dl>
<p> -c, &#8211;scissors</p>
<dl>
<dt>
<dd> Remove everything in body before a scissors line (see <code><a href="/docs/linux/man/1-git-mailinfo/">git-mailinfo</a></code>(1)). Can be activated by default using the <code>mailinfo.scissors</code> configuration variable.</dl>
<p> &#8211;no-scissors</p>
<dl>
<dt>
<dd> Ignore scissors lines (see <code><a href="/docs/linux/man/1-git-mailinfo/">git-mailinfo</a></code>(1)).</dl>
<p> &#8211;quoted-cr=&lt;action&gt;</p>
<dl>
<dt>
<dd> This flag will be passed down to <i>git mailinfo</i> (see <code><a href="/docs/linux/man/1-git-mailinfo/">git-mailinfo</a></code>(1)).</dl>
<p> -m, &#8211;message-id</p>
<dl>
<dt>
<dd> Pass the <code>-m</code> flag to <i>git mailinfo</i> (see <code><a href="/docs/linux/man/1-git-mailinfo/">git-mailinfo</a></code>(1)), so that the Message-ID header is added to the commit message. The <code>am.messageid</code> configuration variable can be used to specify the default behaviour.</dl>
<p> &#8211;no-message-id</p>
<dl>
<dt>
<dd> Do not add the Message-ID header to the commit message. <code>no-message-id</code> is useful to override <code>am.messageid</code>.</dl>
<p> -q, &#8211;quiet</p>
<dl>
<dt>
<dd> Be quiet. Only print error messages.</dl>
<p> -u, &#8211;utf8</p>
<dl>
<dt>
<dd> Pass <code>-u</code> flag to <i>git mailinfo</i> (see <code><a href="/docs/linux/man/1-git-mailinfo/">git-mailinfo</a></code>(1)). The proposed commit log message taken from the e-mail is re-coded into UTF-8 encoding (configuration variable <code>i18n.commitEncoding</code> can be used to specify project&#8217;s preferred encoding if it is not UTF-8). </p>
<p> This was optional in prior versions of git, but now it is the default. You can use <code>&#8211;no-utf8</code> to override this.</dl>
<p> &#8211;no-utf8</p>
<dl>
<dt>
<dd> Pass <code>-n</code> flag to <i>git mailinfo</i> (see <code><a href="/docs/linux/man/1-git-mailinfo/">git-mailinfo</a></code>(1)).</dl>
<p> -3, &#8211;3way, &#8211;no-3way</p>
<dl>
<dt>
<dd> When the patch does not apply cleanly, fall back on 3-way merge if the patch records the identity of blobs it is supposed to apply to and we have those blobs available locally. <code>&#8211;no-3way</code> can be used to override am.threeWay configuration variable. For more information, see am.threeWay in <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1).</dl>
<p> &#8211;rerere-autoupdate, &#8211;no-rerere-autoupdate</p>
<dl>
<dt>
<dd> Allow the rerere mechanism to update the index with the result of auto-conflict resolution if possible.</dl>
<p> &#8211;ignore-space-change, &#8211;ignore-whitespace, &#8211;whitespace=&lt;option&gt;, -C&lt;n&gt;, -p&lt;n&gt;, &#8211;directory=&lt;dir&gt;, &#8211;exclude=&lt;path&gt;, &#8211;include=&lt;path&gt;, &#8211;reject</p>
<dl>
<dt>
<dd> These flags are passed to the <i>git apply</i> (see <code><a href="/docs/linux/man/1-git-apply/">git-apply</a></code>(1)) program that applies the patch.</dl>
<p> &#8211;patch-format</p>
<dl>
<dt>
<dd> By default the command will try to detect the patch format automatically. This option allows the user to bypass the automatic detection and specify the patch format that the patch(es) should be interpreted as. Valid formats are mbox, mboxrd, stgit, stgit-series and hg.</dl>
<p> -i, &#8211;interactive</p>
<dl>
<dt>
<dd> Run interactively.</dl>
<p> &#8211;committer-date-is-author-date</p>
<dl>
<dt>
<dd> By default the command records the date from the e-mail message as the commit author date, and uses the time of commit creation as the committer date. This allows the user to lie about the committer date by using the same value as the author date.</dl>
<p> &#8211;ignore-date</p>
<dl>
<dt>
<dd> By default the command records the date from the e-mail message as the commit author date, and uses the time of commit creation as the committer date. This allows the user to lie about the author date by using the same value as the committer date.</dl>
<p> &#8211;skip</p>
<dl>
<dt>
<dd> Skip the current patch. This is only meaningful when restarting an aborted patch.</dl>
<p> -S[&lt;keyid&gt;], &#8211;gpg-sign[=&lt;keyid&gt;], &#8211;no-gpg-sign</p>
<dl>
<dt>
<dd> GPG-sign commits. The <code>keyid</code> argument is optional and defaults to the committer identity; if specified, it must be stuck to the option without a space. <code>&#8211;no-gpg-sign</code> is useful to countermand both <code>commit.gpgSign</code> configuration variable, and earlier <code>&#8211;gpg-sign</code>.</dl>
<p> &#8211;continue, -r, &#8211;resolved</p>
<dl>
<dt>
<dd> After a patch failure (e.g. attempting to apply conflicting patch), the user has applied it by hand and the index file stores the result of the application. Make a commit using the authorship and commit log extracted from the e-mail message and the current index file, and continue.</dl>
<p> &#8211;resolvemsg=&lt;msg&gt;</p>
<dl>
<dt>
<dd> When a patch failure occurs, &lt;msg&gt; will be printed to the screen before exiting. This overrides the standard message informing you to use <code>&#8211;continue</code> or <code>&#8211;skip</code> to handle the failure. This is solely for internal use between <i>git rebase</i> and <i>git am</i>.</dl>
<p> &#8211;abort</p>
<dl>
<dt>
<dd> Restore the original branch and abort the patching operation. Revert contents of files involved in the am operation to their pre-am state.</dl>
<p> &#8211;quit</p>
<dl>
<dt>
<dd> Abort the patching operation but keep HEAD and the index untouched.</dl>
<p> &#8211;show-current-patch[=(diff|raw)]</p>
<dl>
<dt>
<dd> Show the message at which <code>git am</code> has stopped due to conflicts. If <code>raw</code> is specified, show the raw contents of the e-mail message; if <code>diff</code>, show the diff portion only. Defaults to <code>raw</code>.</dl>
<h2>DISCUSSION</h2>
<p> The commit author name is taken from the &quot;From: &quot; line of the message, and commit author date is taken from the &quot;Date: &quot; line of the message. The &quot;Subject: &quot; line is used as the title of the commit, after stripping common prefix &quot;[PATCH &lt;anything&gt;]&quot;. The &quot;Subject: &quot; line is supposed to concisely describe what the commit is about in one line of text. </p>
<p> &quot;From: &quot;, &quot;Date: &quot;, and &quot;Subject: &quot; lines starting the body override the respective commit author name and title values taken from the headers. </p>
<p> The commit message is formed by the title taken from the &quot;Subject: &quot;, a blank line and the body of the message up to where the patch begins. Excess whitespace at the end of each line is automatically stripped. </p>
<p> The patch is expected to be inline, directly following the message. Any line that is of the form: </p>
<dl>
<dt>
<dd> &bull; three-dashes and end-of-line, or</dl>
<dl>
<dt>
<dd> &bull; a line that begins with &quot;diff -&quot;, or</dl>
<dl>
<dt>
<dd> &bull; a line that begins with &quot;Index: &quot;</dl>
<p> is taken as the beginning of a patch, and the commit log message is terminated before the first occurrence of such a line. </p>
<p> When initially invoking <code>git am</code>, you give it the names of the mailboxes to process. Upon seeing the first patch that does not apply, it aborts in the middle. You can recover from this in one of two ways: </p>
<dl>
<dt>
<dd> 1. skip the current patch by re-running the command with the <code>&#8211;skip</code> option.</dl>
<dl>
<dt>
<dd> 2. hand resolve the conflict in the working directory, and update the index file to bring it into a state that the patch should have produced. Then run the command with the <code>&#8211;continue</code> option.</dl>
<p> The command refuses to process new mailboxes until the current operation is finished, so if you decide to start over from scratch, run <code>git am &#8211;abort</code> before running the command with mailbox names. </p>
<p> Before any patches are applied, ORIG_HEAD is set to the tip of the current branch. This is useful if you have problems with multiple commits, like running <i>git am</i> on the wrong branch or an error in the commits that is more easily fixed by changing the mailbox (e.g. errors in the &quot;From:&quot; lines).</p>
<h2>HOOKS</h2>
<p> This command can run <code>applypatch-msg</code>, <code>pre-applypatch</code>, and <code>post-applypatch</code> hooks. See <code><a href="/docs/linux/man/5-githooks/">githooks</a></code>(5) for more information.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-git-apply/">git-apply</a></code>(1).</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
