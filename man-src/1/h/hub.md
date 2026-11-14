---
title: "hub(1)"
name: "hub"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hub/"
description: "hub – git + hub = github"
---

<h2>NAME</h2>
<p> <code>hub</code> &#8211; git + hub = github</p>
<h2>SYNOPSIS</h2>
<p> <code>hub</code> [<code>&#8211;noop</code>] <i>COMMAND</i> <i>OPTIONS</i><br />
 <code>hub alias</code> [<code>-s</code>] [<i>SHELL</i>]</p>
<h3>Expanded git commands:</h3>
<p> <code>git init -g</code> <i>OPTIONS</i><br />
 <code>git clone</code> [<code>-p</code>] <i>OPTIONS</i> [<i>USER</i>/]<i>REPOSITORY</i> <i>DIRECTORY</i><br />
 <code>git remote add</code> [<code>-p</code>] <i>OPTIONS</i> <i>USER</i>[/<i>REPOSITORY</i>]<br />
 <code>git remote set-url</code> [<code>-p</code>] <i>OPTIONS</i> <i>REMOTE-NAME</i> <i>USER</i>[/<i>REPOSITORY</i>]<br />
 <code>git fetch</code> <i>USER-1</i>,[<i>USER-2</i>,&#8230;]<br />
 <code>git checkout</code> <i>PULLREQ-URL</i> [<i>BRANCH</i>]<br />
 <code>git merge</code> <i>PULLREQ-URL</i><br />
 <code>git cherry-pick</code> <i>GITHUB-REF</i><br />
 <code>git am</code> <i>GITHUB-URL</i><br />
 <code>git apply</code> <i>GITHUB-URL</i><br />
 <code>git push</code> <i>REMOTE-1</i>,<i>REMOTE-2</i>,&#8230;,<i>REMOTE-N</i> [<i>REF</i>]<br />
 <code>git submodule add</code> [<code>-p</code>] <i>OPTIONS</i> [<i>USER</i>/]<i>REPOSITORY</i> <i>DIRECTORY</i></p>
<h3>Custom git commands:</h3>
<p> <code>git create</code> [<i>NAME</i>] [<code>-p</code>] [<code>-d</code> <i>DESCRIPTION</i>] [<code>-h</code> <i>HOMEPAGE</i>]<br />
 <code>git browse</code> [<code>-u</code>] [[<i>USER</i><code>/</code>]<i>REPOSITORY</i>] [SUBPAGE]<br />
 <code>git compare</code> [<code>-u</code>] [<i>USER</i>] [[<i>START</i>&#8230;]<i>END</i>]<br />
 <code>git fork</code> [<code>&#8211;no-remote</code>]<br />
 <code>git pull-request</code> [<code>-o</code>|<code>&#8211;browse</code>] [<code>-f</code>] [<code>-m</code> <i>MESSAGE</i>|<code>-F</code> <i>FILE</i>|<code>-i</code> <i>ISSUE</i>|<i>ISSUE-URL</i>] [<code>-b</code> <i>BASE</i>] [<code>-h</code> <i>HEAD</i>]<br />
 <code>git ci-status</code> [<code>-v</code>] [<i>COMMIT</i>]</p>
<h2>DESCRIPTION</h2>
<p> hub enhances various git commands to ease most common workflows with GitHub.</p>
<dl>
<dt><code>hub &#8211;noop</code> <i>COMMAND</i></p>
<dd> Shows which command(s) would be run as a result of the current command. Doesn&#8217;t perform anything.</p>
<dt><code>hub alias</code> [<code>-s</code>] [<i>SHELL</i>]</p>
<dd> Shows shell instructions for wrapping git. If given, <i>SHELL</i> specifies the type of shell; otherwise defaults to the value of SHELL environment variable. With <code>-s</code>, outputs shell script suitable for <code>eval</code>.</p>
<dt><code>git init</code> <code>-g</code> <i>OPTIONS</i></p>
<dd> Create a git repository as with <a href="/docs/linux/man/1-git-init/">git-init</a>(1) and add remote <code>origin</code> at &quot;git [at] github.com:<i>USER</i>/<i>REPOSITORY</i>.git&quot;; <i>USER</i> is your GitHub username and <i>REPOSITORY</i> is the current working directory&#8217;s basename.</p>
<dt><code>git clone</code> [<code>-p</code>] <i>OPTIONS</i> [<i>USER</i><code>/</code>]<i>REPOSITORY</i> <i>DIRECTORY</i></p>
<dd> Clone repository &quot;<a href="git://github.com/">git://github.com/</a><i>USER</i>/<i>REPOSITORY</i>.git&quot; into <i>DIRECTORY</i> as with <a href="/docs/linux/man/1-git-clone/">git-clone</a>(1). When <i>USER</i>/ is omitted, assumes your GitHub login.</p>
<dt>
<dd> If the repository is private or the current user has push access to the repository, hub will use the ssh protocol for cloning. Use <code>-p</code> to select the ssh protocol unconditionally. HTTPS protocol can be used instead by setting &quot;hub.protocol&quot; (see <i>CONFIGURATION</i>).</p>
<dt><code>git remote add</code> [<code>-p</code>] <i>OPTIONS</i> <i>USER</i>[<code>/</code><i>REPOSITORY</i>]</p>
<dd> Add remote &quot;<a href="git://github.com/">git://github.com/</a><i>USER</i>/<i>REPOSITORY</i>.git&quot; as with <a href="/docs/linux/man/1-git-remote/">git-remote</a>(1). When /<i>REPOSITORY</i> is omitted, the basename of the current working directory is used. With <code>-p</code>, use private remote &quot;git [at] github.com:<i>USER</i>/<i>REPOSITORY</i>.git&quot;. If <i>USER</i> is &quot;origin&quot; then uses your GitHub login.</p>
<dt><code>git remote set-url</code> [<code>-p</code>] <i>OPTIONS</i> <i>REMOTE-NAME</i> <i>USER</i>[/<i>REPOSITORY</i>]</p>
<dd> Sets the url of remote <i>REMOTE-NAME</i> using the same rules as <code>git remote add</code>.</p>
<dt><code>git fetch</code> <i>USER-1</i>,[<i>USER-2</i>,&#8230;]</p>
<dd> Adds missing remote(s) with <code>git remote add</code> prior to fetching. New remotes are only added if they correspond to valid forks on GitHub.</p>
<dt><code>git checkout</code> <i>PULLREQ-URL</i> [<i>BRANCH</i>]</p>
<dd> Checks out the head of the pull request as a local branch, to allow for reviewing, rebasing and otherwise cleaning up the commits in the pull request before merging. The name of the local branch can explicitly be set with <i>BRANCH</i>.</p>
<dt><code>git merge</code> <i>PULLREQ-URL</i></p>
<dd> Merge the pull request with a commit message that includes the pull request ID and title, similar to the GitHub Merge Button.</p>
<dt><code>git cherry-pick</code> <i>GITHUB-REF</i></p>
<dd> Cherry-pick a commit from a fork using either full URL to the commit or GitHub-flavored Markdown notation, which is <code>user@sha</code>. If the remote doesn&#8217;t yet exist, it will be added. A <code>git fetch &lt;user&gt;</code> is issued prior to the cherry-pick attempt.</p>
<dt><code>git [am|apply]</code> <i>GITHUB-URL</i></p>
<dd> Downloads the patch file for the pull request or commit at the URL and applies that patch from disk with <code>git am</code> or <code>git apply</code>. Similar to <code>cherry-pick</code>, but doesn&#8217;t add new remotes. <code>git am</code> creates commits while preserving authorship info while <code>apply</code> only applies the patch to the working copy.</p>
<dt><code>git push</code> <i>REMOTE-1</i>,<i>REMOTE-2</i>,&#8230;,<i>REMOTE-N</i> [<i>REF</i>]</p>
<dd> Push <i>REF</i> to each of <i>REMOTE-1</i> through <i>REMOTE-N</i> by executing multiple <code>git push</code> commands.</p>
<dt><code>git submodule add</code> [<code>-p</code>] <i>OPTIONS</i> [<i>USER</i>/]<i>REPOSITORY</i> <i>DIRECTORY</i></p>
<dd> Submodule repository &quot;<a href="git://github.com/">git://github.com/</a><i>USER</i>/<i>REPOSITORY</i>.git&quot; into <i>DIRECTORY</i> as with <a href="/docs/linux/man/1-git-submodule/">git-submodule</a>(1). When <i>USER</i>/ is omitted, assumes your GitHub login. With <code>-p</code>, use private remote &quot;git [at] github.com:<i>USER</i>/<i>REPOSITORY</i>.git&quot;.</p>
<dt><code>git help</code></p>
<dd> Display enhanced <a href="/docs/linux/man/1-git-help/">git-help</a>(1).</dl>
<p> hub also adds some custom commands that are otherwise not present in git:</p>
<dl>
<dt><code>git create</code> [<i>NAME</i>] [<code>-p</code>] [<code>-d</code> <i>DESCRIPTION</i>] [<code>-h</code> <i>HOMEPAGE</i>]</p>
<dd> Create a new public GitHub repository from the current git repository and add remote <code>origin</code> at &quot;git [at] github.com:<i>USER</i>/<i>REPOSITORY</i>.git&quot;; <i>USER</i> is your GitHub username and <i>REPOSITORY</i> is the current working directory name. To explicitly name the new repository, pass in <i>NAME</i>, optionally in <i>ORGANIZATION</i>/<i>NAME</i> form to create under an organization you&#8217;re a member of. With <code>-p</code>, create a private repository, and with <code>-d</code> and <code>-h</code> set the repository&#8217;s description and homepage URL, respectively.</p>
<dt><code>git browse</code> [<code>-u</code>] [[<i>USER</i><code>/</code>]<i>REPOSITORY</i>] [SUBPAGE]</p>
<dd> Open repository&#8217;s GitHub page in the system&#8217;s default web browser using <code><a href="/docs/linux/man/1-open/">open</a>(1)</code> or the <code>BROWSER</code> env variable. If the repository isn&#8217;t specified, <code>browse</code> opens the page of the repository found in the current directory. If SUBPAGE is specified, the browser will open on the specified subpage: one of &quot;wiki&quot;, &quot;commits&quot;, &quot;issues&quot; or other (the default is &quot;tree&quot;). With <code>-u</code>, outputs the URL rather than opening the browser.</p>
<dt><code>git compare</code> [<code>-u</code>] [<i>USER</i>] [[<i>START</i>&#8230;]<i>END</i>]</p>
<dd> Open a GitHub compare view page in the system&#8217;s default web browser. <i>START</i> to <i>END</i> are branch names, tag names, or commit SHA1s specifying the range of history to compare. If a range with two dots (<code>a..b</code>) is given, it will be transformed into one with three dots. If <i>START</i> is omitted, GitHub will compare against the base branch (the default is &quot;master&quot;). If <i>END</i> is omitted, GitHub compare view is opened for the current branch. With <code>-u</code>, outputs the URL rather than opening the browser.</p>
<dt><code>git fork</code> [<code>&#8211;no-remote</code>]</p>
<dd> Forks the original project (referenced by &quot;origin&quot; remote) on GitHub and adds a new remote for it under your username.</p>
<dt><code>git pull-request</code> [<code>-o</code>|<code>&#8211;browse</code>] [<code>-f</code>] [<code>-m</code> <i>MESSAGE</i>|<code>-F</code> <i>FILE</i>|<code>-i</code> <i>ISSUE</i>|<i>ISSUE-URL</i>] [<code>-b</code> <i>BASE</i>] [<code>-h</code> <i>HEAD</i>]</p>
<dd> Opens a pull request on GitHub for the project that the &quot;origin&quot; remote points to. The default head of the pull request is the current branch. Both base and head of the pull request can be explicitly given in one of the following formats: &quot;branch&quot;, &quot;owner:branch&quot;, &quot;owner/repo:branch&quot;. This command will abort operation if it detects that the current topic branch has local commits that are not yet pushed to its upstream branch on the remote. To skip this check, use <code>-f</code>.</p>
<dt>
<dd> Without <i>MESSAGE</i> or <i>FILE</i>, a text editor will open in which title and body of the pull request can be entered in the same manner as git commit message. Pull request message can also be passed via stdin with <code>-F &#8211;</code>.</p>
<dt>
<dd> With <code>-o</code> or <code>&#8211;browse</code>, the new pull request will open in the web browser.</p>
<dt>
<dd> Issue to pull request conversion via <code>-i &lt;ISSUE&gt;</code> or <i>ISSUE-URL</i> arguments is deprecated and will likely be removed from the future versions of both hub and GitHub API.</p>
<dt><code>git ci-status</code> [<code>-v</code>] [<i>COMMIT</i>]</p>
<dd> Looks up the SHA for <i>COMMIT</i> in GitHub Status API and displays the latest status. Exits with one of:<br />
 success (0), error (1), failure (1), pending (2), no status (3)</p>
<dt>
<dd> If <code>-v</code> is given, additionally print the URL to CI build results.</dl>
<h2>CONFIGURATION</h2>
<p> Hub will prompt for GitHub username &amp; password the first time it needs to access the API and exchange it for an OAuth token, which it saves in &quot;~/.config/hub&quot;. </p>
<p> To avoid being prompted, use <i>GITHUB_USER</i> and <i>GITHUB_PASSWORD</i> environment variables. </p>
<p> If you prefer the HTTPS protocol for GitHub repositories, you can set &quot;hub.protocol&quot; to &quot;https&quot;. This will affect <code>clone</code>, <code>fork</code>, <code>remote add</code> and other operations that expand references to GitHub repositories as full URLs that otherwise use git and ssh protocols.</p>
<dl>
<dt>
<dd>
<pre>
$ git config --global hub.protocol https
</pre>
<dt>
<dd></dl>
<h3>GitHub Enterprise</h3>
<p> By default, hub will only work with repositories that have remotes which point to github.com. GitHub Enterprise hosts need to be whitelisted to configure hub to treat such remotes same as github.com:</p>
<dl>
<dt>
<dd>
<pre>
$ git config --global --add hub.host my.git.org
</pre>
<dt>
<dd></dl>
<p> The default host for commands like <code>init</code> and <code>clone</code> is still github.com, but this can be affected with the <i>GITHUB_HOST</i> environment variable:</p>
<dl>
<dt>
<dd>
<pre>
$ GITHUB_HOST=my.git.org git clone myproject
</pre>
<dt>
<dd></dl>
<h2>EXAMPLES</h2>
<h3>git clone</h3>
<pre><code>
$ git clone schacon / ticgit &gt; git clone git : // github.com/schacon/ticgit.git
                                               $ git clone -
                                               p schacon / ticgit &gt;
    git clone git[at] github.com : schacon / ticgit.git
                                                 $ git clone resque &gt;
    git clone git[at] github.com / YOUR_USER / resque.git
</code></pre>
<h3>git remote add</h3>
<pre>
$ git remote add rtomayko
&gt; git remote add rtomayko <a href="git://github.com/rtomayko/CURRENT_REPO.git">git://github.com/rtomayko/CURRENT_REPO.git</a>
$ git remote add -p rtomayko
&gt; git remote add rtomayko git [at] github.com:rtomayko/CURRENT_REPO.git
$ git remote add origin
&gt; git remote add origin <a href="git://github.com/YOUR_USER/CURRENT_REPO.git">git://github.com/YOUR_USER/CURRENT_REPO.git</a>
</pre>
<h3>git fetch</h3>
<pre>
$ git fetch mislav
&gt; git remote add mislav <a href="git://github.com/mislav/REPO.git">git://github.com/mislav/REPO.git</a>
&gt; git fetch mislav
$ git fetch mislav,xoebus
&gt; git remote add mislav ...
&gt; git remote add xoebus ...
&gt; git fetch --multiple mislav xoebus
</pre>
<h3>git cherry-pick</h3>
<pre>
$ git cherry-pick <a rel="nofollow" href="http://github.com/mislav/REPO/commit/SHA">http://github.com/mislav/REPO/commit/SHA</a>
&gt; git remote add -f mislav <a href="git://github.com/mislav/REPO.git">git://github.com/mislav/REPO.git</a>
&gt; git cherry-pick SHA
$ git cherry-pick mislav@SHA
&gt; git remote add -f mislav <a href="git://github.com/mislav/CURRENT_REPO.git">git://github.com/mislav/CURRENT_REPO.git</a>
&gt; git cherry-pick SHA
$ git cherry-pick mislav@SHA
&gt; git fetch mislav
&gt; git cherry-pick SHA
</pre>
<h3>git am, git apply</h3>
<p>$ git am https :                                                                                            // github.com/defunkt/hub/pull/55<br />
                 [downloads patch via API] &gt; git am / tmp / 55.patch $ git am&#8211; ignore &#8211; whitespace https : // github.com/davidbalbert/hub/commit/fdb9921<br />
                                                                                                            [downloads patch via API] &gt;<br />
                 git am&#8211; ignore &#8211; whitespace / tmp / fdb9921.patch $ git apply https : // gist.github.com/8da7fb575debd88c54cf<br />
                                                                                        [downloads patch via API] &gt;<br />
                 git apply / tmp / gist &#8211; 8da7fb575debd88c54cf.txt</p>
<h3>git fork</h3>
<p>$ git fork<br />
        [repo forked on GitHub] &gt; git remote add &#8211; f YOUR_USER git[at] github.com : YOUR_USER / CURRENT_REPO.git</p>
<h3>git pull-request</h3>
<p>#while on a topic branch called &#8220;feature&#8221;:<br />
$ git pull-request<br />
[ opens text editor to edit title &amp; body for the request ]<br />
[ opened pull request on GitHub for &#8220;YOUR_USER:feature&#8221; ]<br />
#explicit title, pull base &amp;head:<br />
$ git pull-request -m &#8220;Implemented feature X&#8221; -b defunkt:master -h mislav:feature</p>
<h3>git checkout</h3>
<pre>
$ git checkout <a rel="nofollow" href="https://github.com/defunkt/hub/pull/73">https://github.com/defunkt/hub/pull/73</a>
&gt; git remote add -f -t feature <a href="git://github:com/mislav/hub.git">git://github:com/mislav/hub.git</a>
&gt; git checkout --track -B mislav-feature mislav/feature
$ git checkout <a rel="nofollow" href="https://github.com/defunkt/hub/pull/73">https://github.com/defunkt/hub/pull/73</a> custom-branch-name
</pre>
<h3>git merge</h3>
<pre>
$ git merge <a rel="nofollow" href="https://github.com/defunkt/hub/pull/73">https://github.com/defunkt/hub/pull/73</a>
&gt; git fetch <a href="git://github.com/mislav/hub.git">git://github.com/mislav/hub.git</a> +refs/heads/feature:refs/remotes/mislav/feature
&gt; git merge mislav/feature --no-ff -m 'Merge pull request #73 from mislav/feature...'
</pre>
<h3>git create</h3>
<p>$ git create<br />
        [repo created on GitHub] &gt; git remote add origin git[at] github.com : YOUR_USER / CURRENT_REPO.git<br />
#with description:<br />
                                                                                              $ git create &#8211;<br />
                                       d &#8216;It shall be mine, all mine!&#8217; $ git create recipes<br />
                                           [repo created on GitHub] &gt;<br />
    git remote add origin git[at] github.com : YOUR_USER / recipes.git $ git create sinatra / recipes[repo created in GitHub organization] &gt; git remote add origin git[at] github.com : sinatra / recipes.git</p>
<h3>git init</h3>
<pre>
$ git init -g
&gt; git init
&gt; git remote add origin git [at] github.com:YOUR_USER/REPO.git
</pre>
<h3>git push</h3>
<pre>
$ git push origin,staging,qa bert_timeout
&gt; git push origin bert_timeout
&gt; git push staging bert_timeout
&gt; git push qa bert_timeout
</pre>
<h3>git browse</h3>
<pre>
$ git browse
&gt; open <a rel="nofollow" href="https://github.com/YOUR_USER/CURRENT_REPO">https://github.com/YOUR_USER/CURRENT_REPO</a>
$ git browse -- commit/SHA
&gt; open <a rel="nofollow" href="https://github.com/YOUR_USER/CURRENT_REPO/commit/SHA">https://github.com/YOUR_USER/CURRENT_REPO/commit/SHA</a>
$ git browse -- issues
&gt; open <a rel="nofollow" href="https://github.com/YOUR_USER/CURRENT_REPO/issues">https://github.com/YOUR_USER/CURRENT_REPO/issues</a>
$ git browse schacon/ticgit
&gt; open <a rel="nofollow" href="https://github.com/schacon/ticgit">https://github.com/schacon/ticgit</a>
$ git browse schacon/ticgit commit/SHA
&gt; open <a rel="nofollow" href="https://github.com/schacon/ticgit/commit/SHA">https://github.com/schacon/ticgit/commit/SHA</a>
$ git browse resque
&gt; open <a rel="nofollow" href="https://github.com/YOUR_USER/resque">https://github.com/YOUR_USER/resque</a>
$ git browse resque network
&gt; open <a rel="nofollow" href="https://github.com/YOUR_USER/resque/network">https://github.com/YOUR_USER/resque/network</a>
</pre>
<h3>git compare</h3>
<pre>
$ git compare refactor
&gt; open <a rel="nofollow" href="https://github.com/CURRENT_REPO/compare/refactor">https://github.com/CURRENT_REPO/compare/refactor</a>
$ git compare 1.0..1.1
&gt; open <a rel="nofollow" href="https://github.com/CURRENT_REPO/compare/1.0...1.1">https://github.com/CURRENT_REPO/compare/1.0...1.1</a>
$ git compare -u fix
&gt; (<a rel="nofollow" href="https://github.com/CURRENT_REPO/compare/fix)">https://github.com/CURRENT_REPO/compare/fix)</a>
$ git compare other-user patch
&gt; open <a rel="nofollow" href="https://github.com/other-user/REPO/compare/patch">https://github.com/other-user/REPO/compare/patch</a>
</pre>
<h3>git submodule</h3>
<pre><code>
$ git submodule add wycats / bundler vendor / bundler &gt; git submodule add git : // github.com/wycats/bundler.git vendor/bundler
                                                                                $ git submodule add -
                                                                                p wycats / bundler vendor / bundler &gt;
    git submodule add git[at] github.com : wycats / bundler.git vendor / bundler $ git submodule add - b ryppl-- name pip ryppl / pip vendor / pip &gt; git submodule add - b ryppl-- name pip git: // github.com/ryppl/pip.git vendor/pip
</code></pre>
<h3>git ci-status</h3>
<pre>
$ git ci-status [commit]
&gt; (prints CI state of commit and exits with appropriate code)
&gt; One of: success (0), error (1), failure (1), pending (2), no status (3)
</pre>
<h3>git help</h3>
<pre>
$ git help
&gt; (improved git help)
$ git help hub
&gt; (hub man page)
</pre>
<h2>BUGS</h2>
<p> <i><a rel="nofollow" href="https://github.com/github/hub/issues">https://github.com/github/hub/issues</a></i></p>
<h2>AUTHORS</h2>
<p> <i><a rel="nofollow" href="https://github.com/github/hub/contributors">https://github.com/github/hub/contributors</a></i></p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-git/">git</a>(1), <a href="/docs/linux/man/1-git-clone/">git-clone</a>(1), <a href="/docs/linux/man/1-git-remote/">git-remote</a>(1), <a href="/docs/linux/man/1-git-init/">git-init</a>(1), <i><a rel="nofollow" href="http://github.com">http://github.com</a></i>, <i><a href="https://github.com/github/hub">https://github.com/github/hub</a></i> </p>
<h2>Index</h2>
