---

title: "git-annex-shell(1)"
name: "git-annex-shell"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-annex-shell/"
description: "git-annex-shell – Restricted login shell for git-annex only SSH access"
---

<h2>NAME</h2>
<p> git-annex-shell &#8211; Restricted login shell for git-annex only SSH access </p>
<p> git-annex-shell [-c] command [params &#8230;] </p>
<p> git-annex-shell is a restricted shell, similar to git-shell, which can be used as a login shell for SSH accounts. </p>
<p> Since its syntax is identical to git-shell&#8217;s, it can be used as a drop-in replacement anywhere git-shell is used. For example it can be used as a user&#8217;s restricted login shell. </p>
<h2>COMMANDS</h2>
<p> Any command not listed below is passed through to git-shell. </p>
<p> Note that the directory parameter should be an absolute path, otherwise it is assumed to be relative to the user&#8217;s home directory. Also the first &quot;/~/&quot; or &quot;/~user/&quot; is expanded to the specified home directory. </p>
<dl>
<dt>configlist directory</dt>
<dd> This outputs a subset of the git configuration, in the same form as <code>git config &#8211;list</code></dd>
<dt>inannex directory [key &#8230;]</dt>
<dd> This checks if all specified keys are present in the annex, and exits zero if so.</dd>
<dt>dropkey directory [key &#8230;]</dt>
<dd> This drops the annexed data for the specified keys.</dd>
<dt>recvkey directory key</dt>
<dd> This runs rsync in server mode to receive the content of a key, and stores the content in the annex.</dd>
<dt>sendkey directory key</dt>
<dd> This runs rsync in server mode to transfer out the content of a key.</dd>
<dt>transferinfo directory key</dt>
<dd> This is typically run at the same time as sendkey is sending a key to the remote. Using it is optional, but is used to update progress information for the transfer of the key.</dd>
<dt>
</dt><dd> It reads lines from standard input, each giving the number of bytes that have been received so far.</dd>
<dt>commit directory</dt>
<dd> This commits any staged changes to the git-annex branch. It also runs the annex-content hook.</dd>
<dt>gcryptsetup gcryptid</dt>
<dd> Sets up a repository as a gcrypt repository.</dd>
</dl>
<h2>OPTIONS</h2>
<p> Most options are the same as in git-annex. The ones specific to git-annex-shell are: </p>
<dl>
<dt>&#8211;uuid=UUID</dt>
<dd> git-annex uses this to specify the UUID of the repository it was expecting git-annex-shell to access, as a sanity check.</dd>
<dt>&#8212; fields=val fields=val.. &#8212;</dt>
<dd> Additional fields may be specified this way, to retain compatability with past versions of git-annex-shell (that ignore these, but would choke on new dashed options).</dd>
<dt>
</dt><dd> Currently used fields include remoteuuid=, associatedfile=, and direct=</dd>
</dl>
<h2>HOOK</h2>
<p> After content is received or dropped from the repository by git-annex-shell, it runs a hook, <code>.git/hooks/annex-content</code> (or <code>hooks/annex-content</code> on a bare repository). The hook is not currently passed any information about what changed. </p>
<h2>ENVIRONMENT</h2>
<dl>
<dt>GIT_ANNEX_SHELL_READONLY</dt>
<dd>
</dd><dt>
</dt><dd> If set, disallows any command that could modify the repository.</dd>
<dt>GIT_ANNEX_SHELL_LIMITED</dt>
<dd> If set, disallows running git-shell to handle unknown commands.</dd>
<dt>GIT_ANNEX_SHELL_DIRECTORY</dt>
<dd> If set, git-annex-shell will refuse to run commands that do not operate on the specified directory.</dd>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-git-annex/">git-annex</a>(1) </p>
<p> <a href="/docs/linux/man/1-git-shell/">git-shell</a>(1) </p>
<h2>AUTHOR</h2>
<p> Joey Hess &lt;joey [at] kitenet.net&gt; </p>
<p> &lt;<a rel="nofollow" href="http://git-annex.branchable.com/">http://git-annex.branchable.com/</a>&gt; </p>
