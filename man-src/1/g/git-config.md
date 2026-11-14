---
title: "git-config(1)"
name: "git-config"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-config/"
description: "git-config – Get and set repository or global options"
---

<h2 class="name">NAME</h2>
<p> git-config &#8211; Get and set repository or global options </p>
<h2>SYNOPSIS</h2>
<pre><code>
git config[&lt;file - option&gt;][--type = &lt;type&gt;][--fixed - value][--show - origin][--show - scope][-z | --null] name[value[value - pattern]] git config[&lt;file - option&gt;][--type = &lt;type&gt;]-- add name value
            git config[&lt;file - option&gt;][--type = &lt;type&gt;][--fixed - value]-- replace -
        all name value[value - pattern] git config[&lt;file - option&gt;][--type = &lt;type&gt;][--show - origin][--show - scope][-z | --null][--fixed - value]-- get name[value - pattern] git config[&lt;file - option&gt;][--type = &lt;type&gt;][--show - origin][--show - scope][-z | --null][--fixed - value]-- get - all name[value - pattern] git config[&lt;file - option&gt;][--type = &lt;type&gt;][--show - origin][--show - scope][-z | --null][--fixed - value][--name - only]-- get - regexp name_regex[value - pattern] git config[&lt;file - option&gt;][--type = &lt;type&gt;][-z | --null]-- get - urlmatch name URL git config[&lt;file - option&gt;][--fixed - value]-- unset name[value - pattern] git config[&lt;file - option&gt;][--fixed - value]-- unset - all name[value - pattern] git config[&lt;file - option&gt;]-- rename - section old_name new_name git config[&lt;file - option&gt;]-- remove - section name git config[&lt;file - option&gt;][--show - origin][--show - scope][-z | --null][--name - only] - l |
    --list
            git config[&lt;file - option&gt;]-- get -
        color name[default] git config[&lt;file - option&gt;]-- get - colorbool name[stdout - is - tty] git config[&lt;file - option&gt;] - e |
    --edit
</code></pre>
<h2>DESCRIPTION</h2>
<p> You can query/set/replace/unset options with this command. The name is actually the section and the key separated by a dot, and the value will be escaped. </p>
<p> Multiple lines can be added to an option by using the <code>&#8211;add</code> option. If you want to update or unset an option which can occur on multiple lines, a <code>value-pattern</code> (which is an extended regular expression, unless the <code>&#8211;fixed-value</code> option is given) needs to be given. Only the existing values that match the pattern are updated or unset. If you want to handle the lines that do <code>not</code> match the pattern, just prepend a single exclamation mark in front (see also the section called &#8220;EXAMPLES&#8221;), but note that this only works when the <code>&#8211;fixed-value</code> option is not in use. </p>
<p> The <code>&#8211;type=&lt;type&gt;</code> option instructs <i>git config</i> to ensure that incoming and outgoing values are canonicalize-able under the given &lt;type&gt;. If no <code>&#8211;type=&lt;type&gt;</code> is given, no canonicalization will be performed. Callers may unset an existing <code>&#8211;type</code> specifier with <code>&#8211;no-type</code>. </p>
<p> When reading, the values are read from the system, global and repository local configuration files by default, and options <code>&#8211;system</code>, <code>&#8211;global</code>, <code>&#8211;local</code>, <code>&#8211;worktree</code> and <code>&#8211;file &lt;filename&gt;</code> can be used to tell the command to read from only that location (see the section called &#8220;FILES&#8221;). </p>
<p> When writing, the new value is written to the repository local configuration file by default, and options <code>&#8211;system</code>, <code>&#8211;global</code>, <code>&#8211;worktree</code>, <code>&#8211;file &lt;filename&gt;</code> can be used to tell the command to write to that location (you can say <code>&#8211;local</code> but that is the default). </p>
<p> This command will fail with non-zero status upon error. Some exit codes are: </p>
<dl>
<dt>
<dd> &bull; The section or key is invalid (ret=1),</dl>
<dl>
<dt>
<dd> &bull; no section or name was provided (ret=2),</dl>
<dl>
<dt>
<dd> &bull; the config file is invalid (ret=3),</dl>
<dl>
<dt>
<dd> &bull; the config file cannot be written (ret=4),</dl>
<dl>
<dt>
<dd> &bull; you try to unset an option which does not exist (ret=5),</dl>
<dl>
<dt>
<dd> &bull; you try to unset/set an option for which multiple lines match (ret=5), or</dl>
<dl>
<dt>
<dd> &bull; you try to use an invalid regexp (ret=6).</dl>
<p> On success, the command returns the exit code 0. </p>
<p> A list of all available configuration variables can be obtained using the <code>git help &#8211;config</code> command.</p>
<h2>OPTIONS</h2>
<p> &#8211;replace-all</p>
<dl>
<dt>
<dd> Default behavior is to replace at most one line. This replaces all lines matching the key (and optionally the <code>value-pattern</code>).</dl>
<p> &#8211;add</p>
<dl>
<dt>
<dd> Adds a new line to the option without altering any existing values. This is the same as providing <i>^$</i> as the <code>value-pattern</code> in <code>&#8211;replace-all</code>.</dl>
<p> &#8211;get</p>
<dl>
<dt>
<dd> Get the value for a given key (optionally filtered by a regex matching the value). Returns error code 1 if the key was not found and the last value if multiple key values were found.</dl>
<p> &#8211;get-all</p>
<dl>
<dt>
<dd> Like get, but returns all values for a multi-valued key.</dl>
<p> &#8211;get-regexp</p>
<dl>
<dt>
<dd> Like &#8211;get-all, but interprets the name as a regular expression and writes out the key names. Regular expression matching is currently case-sensitive and done against a canonicalized version of the key in which section and variable names are lowercased, but subsection names are not.</dl>
<p> &#8211;get-urlmatch name URL</p>
<dl>
<dt>
<dd> When given a two-part name section.key, the value for section.&lt;url&gt;.key whose &lt;url&gt; part matches the best to the given URL is returned (if no such key exists, the value for section.key is used as a fallback). When given just the section as name, do so for all the keys in the section and list them. Returns error code 1 if no value is found.</dl>
<p> &#8211;global</p>
<dl>
<dt>
<dd> For writing options: write to global <code>~/.gitconfig</code> file rather than the repository <code>.git/config</code>, write to <code>$XDG_CONFIG_HOME/git/config</code> file if this file exists and the <code>~/.gitconfig</code> file doesn&#8217;t. </p>
<p> For reading options: read only from global <code>~/.gitconfig</code> and from <code>$XDG_CONFIG_HOME/git/config</code> rather than from all available files. </p>
<p> See also the section called &#8220;FILES&#8221;.</dl>
<p> &#8211;system</p>
<dl>
<dt>
<dd> For writing options: write to system-wide <code>$(prefix)/etc/gitconfig</code> rather than the repository <code>.git/config</code>. </p>
<p> For reading options: read only from system-wide <code>$(prefix)/etc/gitconfig</code> rather than from all available files. </p>
<p> See also the section called &#8220;FILES&#8221;.</dl>
<p> &#8211;local</p>
<dl>
<dt>
<dd> For writing options: write to the repository <code>.git/config</code> file. This is the default behavior. </p>
<p> For reading options: read only from the repository <code>.git/config</code> rather than from all available files. </p>
<p> See also the section called &#8220;FILES&#8221;.</dl>
<p> &#8211;worktree</p>
<dl>
<dt>
<dd> Similar to <code>&#8211;local</code> except that <code>.git/config.worktree</code> is read from or written to if <code>extensions.worktreeConfig</code> is present. If not it&#8217;s the same as <code>&#8211;local</code>.</dl>
<p> -f config-file, &#8211;file config-file</p>
<dl>
<dt>
<dd> For writing options: write to the specified file rather than the repository <code>.git/config</code>. </p>
<p> For reading options: read only from the specified file rather than from all available files. </p>
<p> See also the section called &#8220;FILES&#8221;.</dl>
<p> &#8211;blob blob</p>
<dl>
<dt>
<dd> Similar to <code>&#8211;file</code> but use the given blob instead of a file. E.g. you can use <i>master:.gitmodules</i> to read values from the file <i>.gitmodules</i> in the master branch. See &quot;SPECIFYING REVISIONS&quot; section in <code><a href="/docs/linux/man/7-gitrevisions/">gitrevisions</a></code>(7) for a more complete list of ways to spell blob names.</dl>
<p> &#8211;remove-section</p>
<dl>
<dt>
<dd> Remove the given section from the configuration file.</dl>
<p> &#8211;rename-section</p>
<dl>
<dt>
<dd> Rename the given section to a new name.</dl>
<p> &#8211;unset</p>
<dl>
<dt>
<dd> Remove the line matching the key from config file.</dl>
<p> &#8211;unset-all</p>
<dl>
<dt>
<dd> Remove all lines matching the key from config file.</dl>
<p> -l, &#8211;list</p>
<dl>
<dt>
<dd> List all variables set in config file, along with their values.</dl>
<p> &#8211;fixed-value</p>
<dl>
<dt>
<dd> When used with the <code>value-pattern</code> argument, treat <code>value-pattern</code> as an exact string instead of a regular expression. This will restrict the name/value pairs that are matched to only those where the value is exactly equal to the <code>value-pattern</code>.</dl>
<p> &#8211;type &lt;type&gt;</p>
<dl>
<dt>
<dd> <i>git config</i> will ensure that any input or output is valid under the given type constraint(s), and will canonicalize outgoing values in <code>&lt;type&gt;</code>&#8216;s canonical form. </p>
<p> Valid <code>&lt;type&gt;</code>&#8216;s include: </p>
<dl>
<dt>
<dd> &bull; <i>bool</i>: canonicalize values as either &quot;true&quot; or &quot;false&quot;.</dl>
<dl>
<dt>
<dd> &bull; <i>int</i>: canonicalize values as simple decimal numbers. An optional suffix of <i>k</i>, <i>m</i>, or <i>g</i> will cause the value to be multiplied by 1024, 1048576, or 1073741824 upon input.</dl>
<dl>
<dt>
<dd> &bull; <i>bool-or-int</i>: canonicalize according to either <i>bool</i> or <i>int</i>, as described above.</dl>
<dl>
<dt>
<dd> &bull; <i>path</i>: canonicalize by adding a leading <code>~</code> to the value of <code>$HOME</code> and <code>~user</code> to the home directory for the specified user. This specifier has no effect when setting the value (but you can use <code>git config section.variable ~/</code> from the command line to let your shell do the expansion.)</dl>
<dl>
<dt>
<dd> &bull; <i>expiry-date</i>: canonicalize by converting from a fixed or relative date-string to a timestamp. This specifier has no effect when setting the value.</dl>
<dl>
<dt>
<dd> &bull; <i>color</i>: When getting a value, canonicalize by converting to an ANSI color escape sequence. When setting a value, a sanity-check is performed to ensure that the given value is canonicalize-able as an ANSI color, but it is written as-is.</dl>
</dl>
<p> &#8211;bool, &#8211;int, &#8211;bool-or-int, &#8211;path, &#8211;expiry-date</p>
<dl>
<dt>
<dd> Historical options for selecting a type specifier. Prefer instead <code>&#8211;type</code> (see above).</dl>
<p> &#8211;no-type</p>
<dl>
<dt>
<dd> Un-sets the previously set type specifier (if one was previously set). This option requests that <i>git config</i> not canonicalize the retrieved variable. <code>&#8211;no-type</code> has no effect without <code>&#8211;type=&lt;type&gt;</code> or <code>&#8211;&lt;type&gt;</code>.</dl>
<p> -z, &#8211;null</p>
<dl>
<dt>
<dd> For all options that output values and/or keys, always end values with the null character (instead of a newline). Use newline instead as a delimiter between key and value. This allows for secure parsing of the output without getting confused e.g. by values that contain line breaks.</dl>
<p> &#8211;name-only</p>
<dl>
<dt>
<dd> Output only the names of config variables for <code>&#8211;list</code> or <code>&#8211;get-regexp</code>.</dl>
<p> &#8211;show-origin</p>
<dl>
<dt>
<dd> Augment the output of all queried config options with the origin type (file, standard input, blob, command line) and the actual origin (config file path, ref, or blob id if applicable).</dl>
<p> &#8211;show-scope</p>
<dl>
<dt>
<dd> Similar to <code>&#8211;show-origin</code> in that it augments the output of all queried config options with the scope of that value (local, global, system, command).</dl>
<p> &#8211;get-colorbool name [stdout-is-tty]</p>
<dl>
<dt>
<dd> Find the color setting for <code>name</code> (e.g. <code>color.diff</code>) and output &quot;true&quot; or &quot;false&quot;. <code>stdout-is-tty</code> should be either &quot;true&quot; or &quot;false&quot;, and is taken into account when configuration says &quot;auto&quot;. If <code>stdout-is-tty</code> is missing, then checks the standard output of the command itself, and exits with status 0 if color is to be used, or exits with status 1 otherwise. When the color setting for <code>name</code> is undefined, the command uses <code>color.ui</code> as fallback.</dl>
<p> &#8211;get-color name [default]</p>
<dl>
<dt>
<dd> Find the color configured for <code>name</code> (e.g. <code>color.diff.new</code>) and output it as the ANSI color escape sequence to the standard output. The optional <code>default</code> parameter is used instead, if there is no color configured for <code>name</code>. </p>
<p> <code>&#8211;type=color [&#8211;default=&lt;default&gt;]</code> is preferred over <code>&#8211;get-color</code> (but note that <code>&#8211;get-color</code> will omit the trailing newline printed by <code>&#8211;type=color</code>).</dl>
<p> -e, &#8211;edit</p>
<dl>
<dt>
<dd> Opens an editor to modify the specified config file; either <code>&#8211;system</code>, <code>&#8211;global</code>, or repository (default).</dl>
<p> &#8211;[no-]includes</p>
<dl>
<dt>
<dd> Respect <code>include.*</code> directives in config files when looking up values. Defaults to <code>off</code> when a specific file is given (e.g., using <code>&#8211;file</code>, <code>&#8211;global</code>, etc) and <code>on</code> when searching all config files.</dl>
<p> &#8211;default &lt;value&gt;</p>
<dl>
<dt>
<dd> When using <code>&#8211;get</code>, and the requested variable is not found, behave as if &lt;value&gt; were the value assigned to the that variable.</dl>
<h2>CONFIGURATION</h2>
<p> <code>pager.config</code> is only respected when listing configuration, i.e., when using <code>&#8211;list</code> or any of the <code>&#8211;get-*</code> which may return multiple results. The default is to use a pager.</p>
<h2>FILES</h2>
<p> If not set explicitly with <code>&#8211;file</code>, there are four files where <i>git config</i> will search for configuration options: </p>
<p> $(prefix)/etc/gitconfig</p>
<dl>
<dt>
<dd> System-wide configuration file.</dl>
<p> $XDG_CONFIG_HOME/git/config</p>
<dl>
<dt>
<dd> Second user-specific configuration file. If $XDG_CONFIG_HOME is not set or empty, <code>$HOME/.config/git/config</code> will be used. Any single-valued variable set in this file will be overwritten by whatever is in <code>~/.gitconfig</code>. It is a good idea not to create this file if you sometimes use older versions of Git, as support for this file was added fairly recently.</dl>
<p> ~/.gitconfig</p>
<dl>
<dt>
<dd> User-specific configuration file. Also called &quot;global&quot; configuration file.</dl>
<p> $GIT_DIR/config</p>
<dl>
<dt>
<dd> Repository specific configuration file.</dl>
<p> $GIT_DIR/config.worktree</p>
<dl>
<dt>
<dd> This is optional and is only searched when <code>extensions.worktreeConfig</code> is present in $GIT_DIR/config.</dl>
<p> If no further options are given, all reading options will read all of these files that are available. If the global or the system-wide configuration file are not available they will be ignored. If the repository configuration file is not available or readable, <i>git config</i> will exit with a non-zero error code. However, in neither case will an error message be issued. </p>
<p> The files are read in the order given above, with last value found taking precedence over values read earlier. When multiple values are taken then all values of a key from all files will be used. </p>
<p> You may override individual configuration parameters when running any git command by using the <code>-c</code> option. See <code><a href="/docs/linux/man/1-git/">git</a></code>(1) for details. </p>
<p> All writing options will per default write to the repository specific configuration file. Note that this also affects options like <code>&#8211;replace-all</code> and <code>&#8211;unset</code>. <i>git config</i><code> will only ever change one file at a time</code>. </p>
<p> You can override these rules using the <code>&#8211;global</code>, <code>&#8211;system</code>, <code>&#8211;local</code>, <code>&#8211;worktree</code>, and <code>&#8211;file</code> command-line options; see the section called &#8220;OPTIONS&#8221; above.</p>
<h2>ENVIRONMENT</h2>
<p> GIT_CONFIG_GLOBAL, GIT_CONFIG_SYSTEM</p>
<dl>
<dt>
<dd> Take the configuration from the given files instead from global or system-level configuration. See <code><a href="/docs/linux/man/1-git/">git</a></code>(1) for details.</dl>
<p> GIT_CONFIG_NOSYSTEM</p>
<dl>
<dt>
<dd> Whether to skip reading settings from the system-wide $(prefix)/etc/gitconfig file. See <code><a href="/docs/linux/man/1-git/">git</a></code>(1) for details.</dl>
<p> See also the section called &#8220;FILES&#8221;. </p>
<p> GIT_CONFIG_COUNT, GIT_CONFIG_KEY_&lt;n&gt;, GIT_CONFIG_VALUE_&lt;n&gt;</p>
<dl>
<dt>
<dd> If GIT_CONFIG_COUNT is set to a positive number, all environment pairs GIT_CONFIG_KEY_&lt;n&gt; and GIT_CONFIG_VALUE_&lt;n&gt; up to that number will be added to the process&#8217;s runtime configuration. The config pairs are zero-indexed. Any missing key or value is treated as an error. An empty GIT_CONFIG_COUNT is treated the same as GIT_CONFIG_COUNT=0, namely no pairs are processed. These environment variables will override values in configuration files, but will be overridden by any explicit options passed via <code>git -c</code>. </p>
<p> This is useful for cases where you want to spawn multiple git commands with a common configuration but cannot depend on a configuration file, for example when writing scripts.</dl>
<p> GIT_CONFIG</p>
<dl>
<dt>
<dd> If no <code>&#8211;file</code> option is provided to <code>git config</code>, use the file given by <code>GIT_CONFIG</code> as if it were provided via <code>&#8211;file</code>. This variable has no effect on other Git commands, and is mostly for historical compatibility; there is generally no reason to use it instead of the <code>&#8211;file</code> option.</dl>
<h2>EXAMPLES</h2>
<p> Given a .git/config like this: </p>
<dl>
<dt>
<dd>
#<br />
#This is the config file, and<br />
#a &#8216;#&#8217; or &#8216;;&#8217; character indicates<br />
#a comment<br />
#<br />
;<br />
core variables<br />
    [core];<br />
Don&#8217;t trust file modes filemode = false;<br />
Our diff algorithm<br />
    [diff] external = / usr / local / bin / diff &#8211; wrapper<br />
                                                       renames = true; Proxy settings<br />
[core]<br />
        gitproxy=proxy-command for kernel.org<br />
        gitproxy=default-proxy ; for<br />
    all the rest;<br />
HTTP<br />
    [http] sslVerify<br />
        [http &#8220;https://weak.example.com&#8221;] sslVerify = false cookieFile = / tmp / cookie.txt
</dl>
<p> you can set the filemode to true with </p>
<dl>
<dt>
<dd>
<pre>
% git config core.filemode true
</pre>
</dl>
<p> The hypothetical proxy command entries actually have a postfix to discern what URL they apply to. Here is how to change the entry for kernel.org to &quot;ssh&quot;. </p>
<dl>
<dt>
<dd>
<pre>
% git config core.gitproxy '&quot;ssh&quot; for kernel.org' 'for kernel.org$'
</pre>
</dl>
<p> This makes sure that only the key/value pair for kernel.org is replaced. </p>
<p> To delete the entry for renames, do </p>
<dl>
<dt>
<dd>
<pre>
% git config --unset diff.renames
</pre>
</dl>
<p> If you want to delete an entry for a multivar (like core.gitproxy above), you have to provide a regex matching the value of exactly one line. </p>
<p> To query the value for a given key, do </p>
<dl>
<dt>
<dd>
<pre>
% git config --get core.filemode
</pre>
</dl>
<p> or </p>
<dl>
<dt>
<dd>
<pre>
% git config core.filemode
</pre>
</dl>
<p> or, to query a multivar: </p>
<dl>
<dt>
<dd>
<pre>
% git config --get core.gitproxy &quot;for kernel.org$&quot;
</pre>
</dl>
<p> If you want to know all the values for a multivar, do: </p>
<dl>
<dt>
<dd>
<pre>
% git config --get-all core.gitproxy
</pre>
</dl>
<p> If you like to live dangerously, you can replace <code>all</code> core.gitproxy by a new one with </p>
<dl>
<dt>
<dd>
<pre>
% git config --replace-all core.gitproxy ssh
</pre>
</dl>
<p> However, if you really only want to replace the line for the default proxy, i.e. the one without a &quot;for &#8230;&quot; postfix, do something like this: </p>
<dl>
<dt>
<dd>
<pre>
% git config core.gitproxy ssh '! for '
</pre>
</dl>
<p> To actually match only values with an exclamation mark, you have to </p>
<dl>
<dt>
<dd>
<pre>
% git config section.key value '[!]'
</pre>
</dl>
<p> To add a new proxy, without altering any of the existing ones, use </p>
<dl>
<dt>
<dd>
<pre>
% git config --add core.gitproxy '&quot;proxy-command&quot; for example.com'
</pre>
</dl>
<p> An example to use customized color from the configuration in your script: </p>
<dl>
<dt>
<dd>
#!/ bin / sh<br />
WS = $(git config&#8211; get &#8211; color color.diff.whitespace &#8220;blue reverse&#8221;)<br />
    RESET = $(git config&#8211; get &#8211; color &#8220;&#8221;<br />
                                       &#8220;reset&#8221;)<br />
        echo &#8220;${WS}your whitespace color or blue reverse${RESET}&#8221;
</dl>
<p> For URLs in <code><a rel="nofollow" href="https://weak.example.com">https://weak.example.com</a></code>, <code>http.sslVerify</code> is set to false, while it is set to <code>true</code> for all others: </p>
<dl>
<dt>
<dd>
% git config&#8211; type = bool &#8211;get &#8211; urlmatch http.sslverify https : // good.example.com<br />
                                                                   true %<br />
                                       git config&#8211; type = bool &#8211;get &#8211; urlmatch http.sslverify https : // weak.example.com<br />
                                                                                                        false %<br />
                                                                            git config&#8211; get &#8211;<br />
                                                           urlmatch http https : // weak.example.com<br />
                                                                                 http.cookieFile /<br />
                                                               tmp / cookie.txt http.sslverify false
</dl>
<h2>CONFIGURATION FILE</h2>
<p> The Git configuration file contains a number of variables that affect the Git commands&#8217; behavior. The files <code>.git/config</code> and optionally <code>config.worktree</code> (see the &quot;CONFIGURATION FILE&quot; section of <code><a href="/docs/linux/man/1-git-worktree/">git-worktree</a></code>(1)) in each repository are used to store the configuration for that repository, and <code>$HOME/.gitconfig</code> is used to store a per-user configuration as fallback values for the <code>.git/config</code> file. The file <code>/etc/gitconfig</code> can be used to store a system-wide default configuration. </p>
<p> The configuration variables are used by both the Git plumbing and the porcelains. The variables are divided into sections, wherein the fully qualified variable name of the variable itself is the last dot-separated segment and the section name is everything before the last dot. The variable names are case-insensitive, allow only alphanumeric characters and <code>&#8211;</code>, and must start with an alphabetic character. Some variables may appear multiple times; we say then that the variable is multivalued.</p>
<h3>Syntax</h3>
<p> The syntax is fairly flexible and permissive; whitespaces are mostly ignored. The <i>#</i> and <i>;</i> characters begin comments to the end of line, blank lines are ignored. </p>
<p> The file consists of sections and variables. A section begins with the name of the section in square brackets and continues until the next section begins. Section names are case-insensitive. Only alphanumeric characters, <code>&#8211;</code> and <code>.</code> are allowed in section names. Each variable must belong to some section, which means that there must be a section header before the first setting of a variable. </p>
<p> Sections can be further divided into subsections. To begin a subsection put its name in double quotes, separated by space from the section name, in the section header, like in the example below: </p>
<dl>
<dt>
<dd>
<pre>
        [section &quot;subsection&quot;]
</pre>
</dl>
<p> Subsection names are case sensitive and can contain any characters except newline and the null byte. Doublequote <code>&quot;</code> and backslash can be included by escaping them as <code>\&quot;</code> and <code>\</code>, respectively. Backslashes preceding other characters are dropped when reading; for example, <code>	</code> is read as <code>t</code> and <code>
