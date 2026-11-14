---
title: "git-http-backend(1)"
name: "git-http-backend"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-http-backend/"
description: "git-http-backend – Server side implementation of Git over HTTP"
---

<h2 class="name">NAME</h2>
<p> git-http-backend &#8211; Server side implementation of Git over HTTP </p>
<h2>SYNOPSIS</h2>
<pre>
<i>git http-backend</i>
</pre>
<h2>DESCRIPTION</h2>
<p> A simple CGI program to serve the contents of a Git repository to Git clients accessing the repository over http:// and https:// protocols. The program supports clients fetching using both the smart HTTP protocol and the backwards-compatible dumb HTTP protocol, as well as clients pushing using the smart HTTP protocol. It also supports Git&#8217;s more-efficient &quot;v2&quot; protocol if properly configured; see the discussion of <code>GIT_PROTOCOL</code> in the ENVIRONMENT section below. </p>
<p> It verifies that the directory has the magic file &quot;git-daemon-export-ok&quot;, and it will refuse to export any Git directory that hasn&#8217;t explicitly been marked for export this way (unless the <code>GIT_HTTP_EXPORT_ALL</code> environmental variable is set). </p>
<p> By default, only the <code>upload-pack</code> service is enabled, which serves <i>git fetch-pack</i> and <i>git ls-remote</i> clients, which are invoked from <i>git fetch</i>, <i>git pull</i>, and <i>git clone</i>. If the client is authenticated, the <code>receive-pack</code> service is enabled, which serves <i>git send-pack</i> clients, which is invoked from <i>git push</i>.</p>
<h2>SERVICES</h2>
<p> These services can be enabled/disabled using the per-repository configuration file: </p>
<p> http.getanyfile</p>
<dl>
<dt>
<dd> This serves Git clients older than version 1.6.6 that are unable to use the upload pack service. When enabled, clients are able to read any file within the repository, including objects that are no longer reachable from a branch but are still present. It is enabled by default, but a repository can disable it by setting this configuration item to <code>false</code>.</dl>
<p> http.uploadpack</p>
<dl>
<dt>
<dd> This serves <i>git fetch-pack</i> and <i>git ls-remote</i> clients. It is enabled by default, but a repository can disable it by setting this configuration item to <code>false</code>.</dl>
<p> http.receivepack</p>
<dl>
<dt>
<dd> This serves <i>git send-pack</i> clients, allowing push. It is disabled by default for anonymous users, and enabled by default for users authenticated by the web server. It can be disabled by setting this item to <code>false</code>, or enabled for all users, including anonymous users, by setting it to <code>true</code>.</dl>
<h2>URL TRANSLATION</h2>
<p> To determine the location of the repository on disk, <i>git http-backend</i> concatenates the environment variables PATH_INFO, which is set automatically by the web server, and GIT_PROJECT_ROOT, which must be set manually in the web server configuration. If GIT_PROJECT_ROOT is not set, <i>git http-backend</i> reads PATH_TRANSLATED, which is also set automatically by the web server.</p>
<h2>EXAMPLES</h2>
<p> All of the following examples map <code><a rel="nofollow" href="http://$hostname/git/foo/bar.git">http://$hostname/git/foo/bar.git</a></code> to <code>/var/www/git/foo/bar.git</code>. </p>
<p> Apache 2.x</p>
<dl>
<dt>
<dd> Ensure mod_cgi, mod_alias, and mod_env are enabled, set GIT_PROJECT_ROOT (or DocumentRoot) appropriately, and create a ScriptAlias to the CGI: </p>
<dl>
<dt>
<dd>
<pre>
SetEnv GIT_PROJECT_ROOT /var/www/git
SetEnv GIT_HTTP_EXPORT_ALL
ScriptAlias /git/ /usr/libexec/git-core/git-http-backend/
# This is not strictly necessary using Apache and a modern version of
# git-http-backend, as the webserver will pass along the header in the
# environment as HTTP_GIT_PROTOCOL, and http-backend will copy that into
# GIT_PROTOCOL. But you may need this line (or something similar if you
# are using a different webserver), or if you want to support older Git
# versions that did not do that copying.
#
# Having the webserver set up GIT_PROTOCOL is perfectly fine even with
# modern versions (and will take precedence over HTTP_GIT_PROTOCOL,
# which means it can be used to override the client's request).
SetEnvIf Git-Protocol &quot;.*&quot; GIT_PROTOCOL=$0
</pre>
</dl>
<p> To enable anonymous read access but authenticated write access, require authorization for both the initial ref advertisement (which we detect as a push via the service parameter in the query string), and the receive-pack invocation itself: </p>
<dl>
<dt>
<dd>
<pre><code>
RewriteCond % {QUERY_STRING} service = git - receive - pack[OR] RewriteCond % {REQUEST_URI} / git - receive - pack$ RewriteRule ^ / git / -[E = AUTHREQUIRED:yes]&lt;LocationMatch "^/git/"&gt; Order Deny, Allow
                                                                                                                                                                                                          Deny from env = AUTHREQUIRED
                                                                                                                                                                                                              AuthType Basic
                                                                                                                                                                                                                  AuthName "Git Access" Require group committers
                                                                                                                                                                                                                      Satisfy Any...&lt;/ LocationMatch&gt;
</code></pre>
</dl>
<p> If you do not have <code>mod_rewrite</code> available to match against the query string, it is sufficient to just protect <code>git-receive-pack</code> itself, like: </p>
<dl>
<dt>
<dd>
<pre>
&lt;LocationMatch &quot;^/git/.*/git-receive-pack$&quot;&gt;
        AuthType Basic
        AuthName &quot;Git Access&quot;
        Require group committers
        ...
&lt;/LocationMatch&gt;
</pre>
</dl>
<p> In this mode, the server will not request authentication until the client actually starts the object negotiation phase of the push, rather than during the initial contact. For this reason, you must also enable the <code>http.receivepack</code> config option in any repositories that should accept a push. The default behavior, if <code>http.receivepack</code> is not set, is to reject any pushes by unauthenticated users; the initial request will therefore report <code>403 Forbidden</code> to the client, without even giving an opportunity for authentication. </p>
<p> To require authentication for both reads and writes, use a Location directive around the repository, or one of its parent directories: </p>
<dl>
<dt>
<dd>
<pre>
&lt;Location /git/private&gt;
        AuthType Basic
        AuthName &quot;Private Git Access&quot;
        Require group committers
        ...
&lt;/Location&gt;
</pre>
</dl>
<p> To serve gitweb at the same url, use a ScriptAliasMatch to only those URLs that <i>git http-backend</i> can handle, and forward the rest to gitweb: </p>
<dl>
<dt>
<dd>
ScriptAliasMatch<br />
        &#8220;(?x)^/git/(.*/(HEAD | \<br />
                        info/refs | \<br />
                        objects/(info/[^/]+ | \<br />
                                 [0-9a-f]{2}/[0-9a-f]{38} | \<br />
                                 pack/pack-[0-9a-f]{40}\.(pack|idx)) | \<br />
                        git-(upload|receive)-pack))$&#8221; /<br />
        usr / libexec / git &#8211;<br />
    core / git &#8211; http &#8211; backend / $1 ScriptAlias / git / / var / www / cgi &#8211; bin / gitweb.cgi /
</dl>
<p> To serve multiple repositories from different <code><a href="/docs/linux/man/7-gitnamespaces/">gitnamespaces</a></code>(7) in a single repository: </p>
<dl>
<dt>
<dd>
SetEnvIf Request_URI &#8220;^/git/([^/]*)&#8221; GIT_NAMESPACE = $1<br />
                                                         ScriptAliasMatch ^<br />
                                                     / git / [^ / ] * (.*) / usr / libexec / git &#8211; core / git &#8211; http &#8211; backend / storage.git$1
</dl>
</dl>
<p> Accelerated static Apache 2.x</p>
<dl>
<dt>
<dd> Similar to the above, but Apache can be used to return static files that are stored on disk. On many systems this may be more efficient as Apache can ask the kernel to copy the file contents from the file system directly to the network: </p>
<dl>
<dt>
<dd>
SetEnv GIT_PROJECT_ROOT / var / www / git AliasMatch ^ / git / (<br />
                                                                   .*/ objects / [0 &#8211; 9a &#8211; f] { 2 } / [0 &#8211; 9a &#8211; f] { 38 }) $<br />
                                                           / var / www / git / $1 AliasMatch<br />
    ^ / git / (.*/ objects / pack / pack &#8211; [0 &#8211; 9a &#8211; f] { 40 }.(pack | idx)) $ / var / www / git / $1 ScriptAlias / git / / usr / libexec / git &#8211; core / git &#8211; http &#8211; backend /
</dl>
<p> This can be combined with the gitweb configuration: </p>
<dl>
<dt>
<dd>
SetEnv GIT_PROJECT_ROOT / var / www / git AliasMatch ^ / git / (<br />
                                                                   .*/ objects / [0 &#8211; 9a &#8211; f] { 2 } / [0 &#8211; 9a &#8211; f] { 38 }) $<br />
                                                           / var / www / git / $1 AliasMatch<br />
    ^ / git / (.*/ objects / pack / pack &#8211; [0 &#8211; 9a &#8211; f] { 40 }.(pack | idx)) $ / var / www / git / $1 ScriptAliasMatch &#8220;(?x)^/git/(.*/(HEAD | \<br />
                        info/refs | \<br />
                        objects/info/[^/]+ | \<br />
                        git-(upload|receive)-pack))$&#8221; /<br />
              usr / libexec / git<br />
          &#8211; core / git &#8211; http &#8211; backend / $1 ScriptAlias / git / / var / www / cgi &#8211; bin / gitweb.cgi /
</dl>
</dl>
<p> Lighttpd</p>
<dl>
<dt>
<dd> Ensure that <code>mod_cgi</code>, <code>mod_alias</code>, <code>mod_auth</code>, <code>mod_setenv</code> are loaded, then set <code>GIT_PROJECT_ROOT</code> appropriately and redirect all requests to the CGI: </p>
<dl>
<dt>
<dd>
alias.url += (&#8220;/git&#8221; = &gt; &#8220;/usr/lib/git-core/git-http-backend&#8221;)<br />
    $HTTP[&#8220;url&#8221;] = ~&#8221;^/git&#8221;<br />
{<br />
    cgi.assign = (&#8220;&#8221; = &gt; &#8220;&#8221;)<br />
                     setenv.add &#8211;<br />
                 environment = (&#8220;GIT_PROJECT_ROOT&#8221; = &gt; &#8220;/var/www/git&#8221;,<br />
                                &#8220;GIT_HTTP_EXPORT_ALL&#8221; = &gt; &#8220;&#8221;)<br />
}
</dl>
<p> To enable anonymous read access but authenticated write access: </p>
<dl>
<dt>
<dd>
$HTTP[&#8220;querystring&#8221;] = ~&#8221;service=git-receive-pack&#8221; {<br />
    include &#8220;git-auth.conf&#8221;} $HTTP[&#8220;url&#8221;] = ~&#8221;^/git/.*/git-receive-pack$&#8221;<br />
{<br />
    include &#8220;git-auth.conf&#8221;<br />
}
</dl>
<p> where <code>git-auth.conf</code> looks something like: </p>
<dl>
<dt>
<dd>
<pre>
auth.require = (
        &quot;/&quot; =&gt; (
                &quot;method&quot; =&gt; &quot;basic&quot;,
                &quot;realm&quot; =&gt; &quot;Git Access&quot;,
                &quot;require&quot; =&gt; &quot;valid-user&quot;
               )
)
# ...and set up auth.backend here
</pre>
</dl>
<p> To require authentication for both reads and writes: </p>
<dl>
<dt>
<dd>
<pre><code>
$HTTP["url"] = ~"^/git/private"
{
    include "git-auth.conf"
}
</code></pre>
</dl>
</dl>
<h2>ENVIRONMENT</h2>
<p> <i>git http-backend</i> relies upon the <code>CGI</code> environment variables set by the invoking web server, including: </p>
<dl>
<dt>
<dd> &bull; PATH_INFO (if GIT_PROJECT_ROOT is set, otherwise PATH_TRANSLATED)</dl>
<dl>
<dt>
<dd> &bull; REMOTE_USER</dl>
<dl>
<dt>
<dd> &bull; REMOTE_ADDR</dl>
<dl>
<dt>
<dd> &bull; CONTENT_TYPE</dl>
<dl>
<dt>
<dd> &bull; QUERY_STRING</dl>
<dl>
<dt>
<dd> &bull; REQUEST_METHOD</dl>
<p> The <code>GIT_HTTP_EXPORT_ALL</code> environmental variable may be passed to <i>git-http-backend</i> to bypass the check for the &quot;git-daemon-export-ok&quot; file in each repository before allowing export of that repository. </p>
<p> The <code>GIT_HTTP_MAX_REQUEST_BUFFER</code> environment variable (or the <code>http.maxRequestBuffer</code> config variable) may be set to change the largest ref negotiation request that git will handle during a fetch; any fetch requiring a larger buffer will not succeed. This value should not normally need to be changed, but may be helpful if you are fetching from a repository with an extremely large number of refs. The value can be specified with a unit (e.g., <code>100M</code> for 100 megabytes). The default is 10 megabytes. </p>
<p> Clients may probe for optional protocol capabilities (like the v2 protocol) using the <code>Git-Protocol</code> HTTP header. In order to support these, the contents of that header must appear in the <code>GIT_PROTOCOL</code> environment variable. Most webservers will pass this header to the CGI via the <code>HTTP_GIT_PROTOCOL</code> variable, and <code>git-http-backend</code> will automatically copy that to <code>GIT_PROTOCOL</code>. However, some webservers may be more selective about which headers they&#8217;ll pass, in which case they need to be configured explicitly (see the mention of <code>Git-Protocol</code> in the Apache config from the earlier EXAMPLES section). </p>
<p> The backend process sets GIT_COMMITTER_NAME to <i>$REMOTE_USER</i> and GIT_COMMITTER_EMAIL to <i>${REMOTE_USER}@http.${REMOTE_ADDR}</i>, ensuring that any reflogs created by <i>git-receive-pack</i> contain some identifying information of the remote user who performed the push. </p>
<p> All <code>CGI</code> environment variables are available to each of the hooks invoked by the <i>git-receive-pack</i>.</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
