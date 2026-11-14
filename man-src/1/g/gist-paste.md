---
title: "gist-paste(1)"
name: "gist-paste"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gist-paste/"
description: "gist – upload code to"
---

<h2 class="name">NAME</h2>
<p> <code>gist</code> &#8211; upload code to </p>
<p> <a rel="nofollow" href="https://gist.github.com">https://gist.github.com</a></p>
<h2>Synopsis</h2>
<p> The gist gem provides a <code>gist</code> command that you can use from your terminal to upload content to <a rel="nofollow" href="https://gist.github.com/.">https://gist.github.com/.</a></p>
<h2>Installation</h2>
<dl>
<dt>&bull;</p>
<dd> If you have ruby installed:</p>
<dt>
<dd> gem install gist</p>
<dt>&bull;</p>
<dd> If you&#8217;re using Bundler:</p>
<dt>
<dd> source :rubygems gem &#8216;gist&#8217;</p>
<dt>&bull;</p>
<dd> For OS X, gist lives in Homebrew</p>
<dt>
<dd> brew install gist</p>
<dt>
<dd></dl>
<h2>Command</h2>
<dl>
<dt>&bull;</p>
<dd> To upload the contents of <code>a.rb</code> just:</p>
<dt>
<dd> gist-paste a.rb</p>
<dt>&bull;</p>
<dd> Upload multiple files:</p>
<dt>
<dd> gist-paste a b c gist *.rb</p>
<dt>&bull;</p>
<dd> By default it reads from STDIN, and you can set a filename with <code>-f</code>.</p>
<dt>
<dd> gist-paste -f test.rb &lt;a.rb</p>
<dt>&bull;</p>
<dd> Alternatively, you can just paste from the clipboard:</p>
<dt>
<dd> gist-paste -P</p>
<dt>&bull;</p>
<dd> Use <code>-p</code> to make the gist private:</p>
<dt>
<dd> gist-paste -p a.rb</p>
<dt>&bull;</p>
<dd> Use <code>-d</code> to add a description:</p>
<dt>
<dd> gist-paste -d &quot;Random rbx bug&quot; a.rb</p>
<dt>&bull;</p>
<dd> You can update existing gists with <code>-u</code>:</p>
<dt>
<dd> gist-paste -u GIST_ID FILE_NAME gist -u 42f2c239d2eb57299408 test.txt</p>
<dt>&bull;</p>
<dd> If you&#8217;d like to copy the resulting URL to your clipboard, use <code>-c</code>.</p>
<dt>
<dd> gist-paste -c &lt;a.rb</p>
<dt>&bull;</p>
<dd> If you&#8217;d like to copy the resulting embeddable URL to your clipboard, use <code>-e</code>.</p>
<dt>
<dd> gist-paste -e &lt;a.rb</p>
<dt>&bull;</p>
<dd> And you can just ask gist to open a browser window directly with <code>-o</code>.</p>
<dt>
<dd> gist-paste -o &lt;a.rb</p>
<dt>&bull;</p>
<dd> To list (public gists or all gists for authed user) gists for user</p>
<dt>
<dd> gist-paste -l : all gists for authed user gist -l defunkt : list defunkt&#8217;s public gists</p>
<dt>
<dd></dl>
<p> To read a gist and print it to STDOUT</p>
<dl>
<dt>
<dd>
<pre>
gist -r GIST_ID
gist -r 374130
</pre>
<dt>
<dd>
<dt>&bull;</p>
<dd> See <code>gist &#8211;help</code> for more detail.</p>
<dt>
<dd></dl>
<h2>Login</h2>
<p> If you want to associate your gists with your GitHub account, you need to login with gist. It doesn&#8217;t store your username and password, it just uses them to get an OAuth2 token (with the &quot;gist&quot; permission).</p>
<dl>
<dt>
<dd>
<pre>
gist-paste --login
Obtaining OAuth2 access_token from github.
GitHub username: ConradIrwin
GitHub password:
2-factor auth code:
Success! <a rel="nofollow" href="https://github.com/settings/tokens">https://github.com/settings/tokens</a>
</pre>
<dt>
<dd></dl>
<p> This token is stored in <code>~/.gist</code> and used for all future gisting. If you need to you can revoke it from <a rel="nofollow" href="https://github.com/settings/tokens,">https://github.com/settings/tokens,</a> or just delete the file.</p>
<dl>
<dt>&bull;</p>
<dd> After you&#8217;ve done this, you can still upload gists anonymously with <code>-a</code>.</p>
<dt>
<dd> gist-paste -a a.rb</p>
<dt>
<dd></dl>
<p> If you have a complicated authorization requirement you can manually create a token file by pasting a Github token with only the <code>gist</code> permission into a file called <code>~/.gist</code>. You can create one from <a rel="nofollow" href="https://github.com/settings/tokens">https://github.com/settings/tokens</a> </p>
<p> This file should contain only the token (~40 hex characters), and to make it easier to edit, can optionally have a final newline (
 or 
). </p>
<p> For example, one way to create this file would be to run:</p>
<dl>
<dt>
<dd>
<pre>
echo MY_SECRET_TOKEN &gt; ~/.gist
</pre>
<dt>
<dd></dl>
<h3>GitHub Enterprise</h3>
<p> If you&#8217;d like <code>gist</code> to use your locally installed GitHub Enterprise <i><a rel="nofollow" href="https://enterprise.github.com/">https://enterprise.github.com/</a></i>, you need to export the <code>GITHUB_URL</code> environment variable (usually done in your <code>~/.bashrc</code>).</p>
<dl>
<dt>
<dd>
<pre>
export GITHUB_URL=<a rel="nofollow" href="http://github.internal.example.com/">http://github.internal.example.com/</a>
</pre>
<dt>
<dd></dl>
<p> Once you&#8217;ve done this and restarted your terminal (or run <code>source ~/.bashrc</code>), gist will automatically use github enterprise instead of the public github.com </p>
<p> Your token for GitHub Enterprise will be stored in <code>.gist.&lt;protocol&gt;.&lt;server.name&gt;[.&lt;port&gt;]</code> (e.g. <code>~/.gist.http.github.internal.example.com</code> for the GITHUB_URL example above) instead of <code>~/.gist</code>. </p>
<p> If you have multiple servers or use Enterprise and public GitHub often, you can work around this by creating scripts that set the env var and then run <code>gist</code>. Keep in mind that to use the public GitHub you must unset the env var. Just setting it to the public URL will not work. Use <code>unset GITHUB_URL</code></p>
<h3>Token file format</h3>
<p> If you cannot use passwords, as most Enterprise installations do, you can generate the token via the web interface and then simply save the string in the correct file. Avoid line breaks or you might see: <code>$ gist -l Error: Bad credentials</code></p>
<dl>
<dt>You can also use Gist as a library from inside your ruby code:</p>
<dd>
<dt>
<dd> Gist.gist(&quot;Look.at(:my =&gt; &#8216;awesome&#8217;).code&quot;)</dl>
<p> If you need more advanced features you can also pass:</p>
<dl>
<dt>&bull;</p>
<dd> <code>:access_token</code> to authenticate using OAuth2 (default is `File.read(&quot;~/.gist&quot;)).</p>
<dt>&bull;</p>
<dd> <code>:filename</code> to change the syntax highlighting (default is <code>a.rb</code>).</p>
<dt>&bull;</p>
<dd> <code>:public</code> if you want your gist to have a guessable url.</p>
<dt>&bull;</p>
<dd> <code>:description</code> to add a description to your gist.</p>
<dt>&bull;</p>
<dd> <code>:update</code> to update an existing gist (can be a URL or an id).</p>
<dt>&bull;</p>
<dd> <code>:anonymous</code> to submit an anonymous gist (default is false).</p>
<dt>&bull;</p>
<dd> <code>:copy</code> to copy the resulting URL to the clipboard (default is false).</p>
<dt>&bull;</p>
<dd> <code>:open</code> to open the resulting URL in a browser (default is false).</p>
<dt>
<dd></dl>
<p> NOTE: The access_token must have the &quot;gist&quot; scope.</p>
<dl>
<dt>&bull;</p>
<dd> If you want to upload multiple files in the same gist, you can:</p>
<dt>
<dd> Gist.multi_gist(&quot;a.rb&quot; =&gt; &quot;Foo.bar&quot;, &quot;a.py&quot; =&gt; &quot;Foo.bar&quot;)</p>
<dt>&bull;</p>
<dd> If you&#8217;d rather use gist&#8217;s builtin access_token, then you can force the user to obtain one by calling:</p>
<dt>
<dd> Gist.login!</p>
<dt>&bull;</p>
<dd> This will take them through the process of obtaining an OAuth2 token, and storing it in <code>~/.gist</code>, where it can later be read by <code>Gist.gist</code></p>
<dt>
<dd></dl>
<h2>Configuration</h2>
<dl>
<dt>&bull;</p>
<dd> If you&#8217;d like <code>-o</code> or <code>-c</code> to be the default when you use the gist executable, add an alias to your <code>~/.bashrc</code> (or equivalent). For example:</p>
<dt>
<dd> alias gist=&#8217;gist -c&#8217;</p>
<dt>&bull;</p>
<dd> If you&#8217;d prefer gist to open a different browser, then you can export the BROWSER environment variable:</p>
<dt>
<dd> export BROWSER=google-chrome</p>
<dt>
<dd></dl>
<p> If clipboard or browser integration don&#8217;t work on your platform, please file a bug or (more ideally) a pull request. </p>
<p> If you need to use an HTTP proxy to access the internet, export the <code>HTTP_PROXY</code> or <code>http_proxy</code> environment variable and gist will use it.</p>
<h2>Meta-fu</h2>
<p> Thanks to @defunkt and @indirect for writing and maintaining versions 1 through 3. Thanks to @rking and @ConradIrwin for maintaining version 4. </p>
<p> Licensed under the MIT license. Bug-reports, and pull requests are welcome. </p>
<h2>Index</h2>
