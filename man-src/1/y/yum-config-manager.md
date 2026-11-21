---

title: "yum-config-manager(1)"
name: "yum-config-manager"
section: "1"
letter: "y"
url: "/docs/linux/man/1-yum-config-manager/"
description: "yum-config-manager – manage yum configuration options and yum repositories"
---

<h2>NAME</h2>
<p> yum-config-manager &#8211; manage yum configuration options and yum repositories</p>
<p> <code>yum-config-manager</code> [options] [section &#8230;]</p>
<p> <code>yum-config-manager</code> is a program that can manage main yum configuration options, toggle which repositories are enabled or disabled, and add new repositories. </p>
<p> Unless &#8211;add-repo is used, the program will output the current configuration of the selected sections, and optionally save it back to the corresponding files. </p>
<p> By default, if no positional arguments are specified, the program will select the [main] section and each enabled repository. You can override this by specifying your own list of sections as arguments (these may also include disabled repositories). A section can either be main or a repoid. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></dt>
<dd> Display a help message, and then quit.</dd>
<dt><code>&#8211;setopt=option=value</code></dt>
<dd> Set any config option in yum config or repo files. For options in the global config just use: &#8211;setopt=option=value for repo options use: &#8211;setopt=repoid.option=value. The latter form accepts wildcards in repoid that will be expanded to the selected sections. If repoid contains no wildcard, it will automatically be selected; this is useful if you are addressing a disabled repo, in which case you don&#8217;t have to additionally pass it as an argument.</dd>
<dt><code>&#8211;save</code></dt>
<dd> Save the current options (useful with &#8211;setopt).</dd>
<dt><code>&#8211;enable</code></dt>
<dd> Enable the specified repos (automatically saves). To enable all repositories run &quot;yum-config-manager &#8211;enable \*&quot;.</dd>
<dt><code>&#8211;disable</code></dt>
<dd> Disable the specified repos (automatically saves). To disable all repositories run &quot;yum-config-manager &#8211;disable \*&quot;.</dd>
<dt><code>&#8211;add-repo=ADDREPO</code></dt>
<dd> Add (and enable) the repo from the specified file or url.</dd></dl>
<h2>ADDITIONAL OPTIONS</h2>
<p> Yum-config-manager inherits all other options from yum. See the <a href="/docs/linux/man/8-yum/">yum</a>(8) man page for more information. </p>
<h2>EXAMPLES</h2>
<p> Show the configuration of [main] and the repos foo and bar:</p>
<dl>
<dt>
</dt><dd> <code>yum-config-manager main foo bar</code></dd></dl>
<p> Enable the repos foo and bar:</p>
<dl>
<dt>
</dt><dd> <code>yum-config-manager &#8211;enable foo bar</code></dd></dl>
<p> Change a global option:</p>
<dl>
<dt>
</dt><dd> <code>yum-config-manager &#8211;setopt=installonly_limit=5 &#8211;save</code></dd></dl>
<p> Change a repo option of the repo foo (works even if foo is disabled):</p>
<dl>
<dt>
</dt><dd> <code>yum-config-manager &#8211;setopt=foo.skip_if_unavailable=1 &#8211;save</code></dd></dl>
<p> Change a repo option of more repos at once:</p>
<dl>
<dt>
</dt><dd> <code>yum-config-manager &#8211;setopt=\*.skip_if_unavailable=1 &#8211;save foo bar baz</code></dd></dl>
<p> Change a repo option of all the enabled repos:</p>
<dl>
<dt>
</dt><dd> <code>yum-config-manager &#8211;setopt=\*.skip_if_unavailable=1 &#8211;save</code></dd></dl>
<p> Change a repo option of all the configured (that is, enabled and disabled) repos:</p>
<dl>
<dt>
</dt><dd> <code>yum-config-manager &#8211;setopt=\*.skip_if_unavailable=1 &#8211;save \*</code> </dd>
</dl>
<h2>SEE ALSO</h2>
<pre>
<i>yum.conf (5)</i>
<a rel="nofollow" href="http://yum.baseurl.org/">http://yum.baseurl.org/</a>
</pre>
<h2>AUTHORS</h2>
<pre>
See the Authors file included with this program.
</pre>
