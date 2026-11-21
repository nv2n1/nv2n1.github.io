---
title: "git-config(1)"
name: "git-config"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-config/"
description: "git-config – Get and set repository or global options"
---
<h2 class="name">NAME</h2>
<p> git-config - Get and set repository or global options </p>
<h2>SYNOPSIS</h2>
<pre><code>
 git config  [&lt;file-option&gt;] [--type=&lt;type&gt;] [--fixed-value] [--show-origin] [--show-scope] [-z|--null] name [value [value-pattern]]
 git config  [&lt;file-option&gt;] [--type=&lt;type&gt;] --add name value
 git config  [&lt;file-option&gt;] [--type=&lt;type&gt;] [--fixed-value] --replace-all name value [value-pattern]
 git config  [&lt;file-option&gt;] [--type=&lt;type&gt;] [--show-origin] [--show-scope] [-z|--null] [--fixed-value] --get name [value-pattern]
 git config  [&lt;file-option&gt;] [--type=&lt;type&gt;] [--show-origin] [--show-scope] [-z|--null] [--fixed-value] --get-all name [value-pattern]
 git config  [&lt;file-option&gt;] [--type=&lt;type&gt;] [--show-origin] [--show-scope] [-z|--null] [--fixed-value] [--name-only] --get-regexp name_regex [value-pattern]
 git config  [&lt;file-option&gt;] [--type=&lt;type&gt;] [-z|--null] --get-urlmatch name URL
 git config  [&lt;file-option&gt;] [--fixed-value] --unset name [value-pattern]
 git config  [&lt;file-option&gt;] [--fixed-value] --unset-all name [value-pattern]
 git config  [&lt;file-option&gt;] --rename-section old_name new_name
 git config  [&lt;file-option&gt;] --remove-section name
 git config  [&lt;file-option&gt;] [--show-origin] [--show-scope] [-z|--null] [--name-only] -l | --list
 git config  [&lt;file-option&gt;] --get-color name [default]
 git config  [&lt;file-option&gt;] --get-colorbool name [stdout-is-tty]
 git config  [&lt;file-option&gt;] -e | --edit
</code></pre>
<h2>DESCRIPTION</h2>
<p> You can query/set/replace/unset options with this command. The name is actually the section and the key separated by a dot, and the value will be escaped. </p>
<p> Multiple lines can be added to an option by using the <code>--add</code> option. If you want to update or unset an option which can occur on multiple lines, a <code>value-pattern</code> (which is an extended regular expression, unless the <code>--fixed-value</code> option is given) needs to be given. Only the existing values that match the pattern are updated or unset. If you want to handle the lines that do <code>not</code> match the pattern, just prepend a single exclamation mark in front (see also the section called "EXAMPLES"), but note that this only works when the <code>--fixed-value</code> option is not in use. </p>
<p> The <code>--type=&lt;type&gt;</code> option instructs <i>git config</i> to ensure that incoming and outgoing values are canonicalize-able under the given &lt;type&gt;. If no <code>--type=&lt;type&gt;</code> is given, no canonicalization will be performed. Callers may unset an existing <code>--type</code> specifier with <code>--no-type</code>. </p>
<p> When reading, the values are read from the system, global and repository local configuration files by default, and options <code>--system</code>, <code>--global</code>, <code>--local</code>, <code>--worktree</code> and <code>--file &lt;filename&gt;</code> can be used to tell the command to read from only that location (see the section called "FILES"). </p>
<p> When writing, the new value is written to the repository local configuration file by default, and options <code>--system</code>, <code>--global</code>, <code>--worktree</code>, <code>--file &lt;filename&gt;</code> can be used to tell the command to write to that location (you can say <code>--local</code> but that is the default). </p>
<p> This command will fail with non-zero status upon error. Some exit codes are: </p>
<dl>
<dd> <p> &bull; The section or key is invalid (ret=1), </p>
 </dd></dl>
<dl>
<dd> <p> &bull; no section or name was provided (ret=2), </p>
 </dd></dl>
<dl>
<dd> <p> &bull; the config file is invalid (ret=3), </p>
 </dd></dl>
<dl>
<dd> <p> &bull; the config file cannot be written (ret=4), </p>
 </dd></dl>
<dl>
<dd> <p> &bull; you try to unset an option which does not exist (ret=5), </p>
 </dd></dl>
<dl>
<dd> <p> &bull; you try to unset/set an option for which multiple lines match (ret=5), or </p>
 </dd></dl>
<dl>
<dd> <p> &bull; you try to use an invalid regexp (ret=6). </p>
 </dd></dl>
<p> On success, the command returns the exit code 0. </p>
<p> A list of all available configuration variables can be obtained using the <code>git help --config</code> command.  </p>
<h2>OPTIONS</h2>
<p> --replace-all </p>
<dl>
<dd> <p> Default behavior is to replace at most one line. This replaces all lines matching the key (and optionally the <code>value-pattern</code>). </p>
 </dd></dl>
<p> --add </p>
<dl>
<dd> <p> Adds a new line to the option without altering any existing values. This is the same as providing <i>^$</i> as the <code>value-pattern</code> in <code>--replace-all</code>. </p>
 </dd></dl>
<p> --get </p>
<dl>
<dd> <p> Get the value for a given key (optionally filtered by a regex matching the value). Returns error code 1 if the key was not found and the last value if multiple key values were found. </p>
 </dd></dl>
<p> --get-all </p>
<dl>
<dd> <p> Like get, but returns all values for a multi-valued key. </p>
 </dd></dl>
<p> --get-regexp </p>
<dl>
<dd> <p> Like --get-all, but interprets the name as a regular expression and writes out the key names. Regular expression matching is currently case-sensitive and done against a canonicalized version of the key in which section and variable names are lowercased, but subsection names are not. </p>
 </dd></dl>
<p> --get-urlmatch name URL </p>
<dl>
<dd> <p> When given a two-part name section.key, the value for section.&lt;url&gt;.key whose &lt;url&gt; part matches the best to the given URL is returned (if no such key exists, the value for section.key is used as a fallback). When given just the section as name, do so for all the keys in the section and list them. Returns error code 1 if no value is found. </p>
 </dd></dl>
<p> --global </p>
<dl>
<dd> <p> For writing options: write to global <code>~/.gitconfig</code> file rather than the repository <code>.git/config</code>, write to <code>$XDG_CONFIG_HOME/git/config</code> file if this file exists and the <code>~/.gitconfig</code> file doesn&#8217;t. </p>
<p> For reading options: read only from global <code>~/.gitconfig</code> and from <code>$XDG_CONFIG_HOME/git/config</code> rather than from all available files. </p>
<p> See also the section called "FILES". </p>
 </dd></dl>
<p> --system </p>
<dl>
<dd> <p> For writing options: write to system-wide <code>$(prefix)/etc/gitconfig</code> rather than the repository <code>.git/config</code>. </p>
<p> For reading options: read only from system-wide <code>$(prefix)/etc/gitconfig</code> rather than from all available files. </p>
<p> See also the section called "FILES". </p>
 </dd></dl>
<p> --local </p>
<dl>
<dd> <p> For writing options: write to the repository <code>.git/config</code> file. This is the default behavior. </p>
<p> For reading options: read only from the repository <code>.git/config</code> rather than from all available files. </p>
<p> See also the section called "FILES". </p>
 </dd></dl>
<p> --worktree </p>
<dl>
<dd> <p> Similar to <code>--local</code> except that <code>.git/config.worktree</code> is read from or written to if <code>extensions.worktreeConfig</code> is present. If not it&#8217;s the same as <code>--local</code>. </p>
 </dd></dl>
<p> -f config-file, --file config-file </p>
<dl>
<dd> <p> For writing options: write to the specified file rather than the repository <code>.git/config</code>. </p>
<p> For reading options: read only from the specified file rather than from all available files. </p>
<p> See also the section called "FILES". </p>
 </dd></dl>
<p> --blob blob </p>
<dl>
<dd> <p> Similar to <code>--file</code> but use the given blob instead of a file. E.g. you can use <i>master:.gitmodules</i> to read values from the file <i>.gitmodules</i> in the master branch. See &quot;SPECIFYING REVISIONS&quot; section in <code><a href="/docs/linux/man/7-gitrevisions/">gitrevisions</a></code>(7) for a more complete list of ways to spell blob names. </p>
 </dd></dl>
<p> --remove-section </p>
<dl>
<dd> <p> Remove the given section from the configuration file. </p>
 </dd></dl>
<p> --rename-section </p>
<dl>
<dd> <p> Rename the given section to a new name. </p>
 </dd></dl>
<p> --unset </p>
<dl>
<dd> <p> Remove the line matching the key from config file. </p>
 </dd></dl>
<p> --unset-all </p>
<dl>
<dd> <p> Remove all lines matching the key from config file. </p>
 </dd></dl>
<p> -l, --list </p>
<dl>
<dd> <p> List all variables set in config file, along with their values. </p>
 </dd></dl>
<p> --fixed-value </p>
<dl>
<dd> <p> When used with the <code>value-pattern</code> argument, treat <code>value-pattern</code> as an exact string instead of a regular expression. This will restrict the name/value pairs that are matched to only those where the value is exactly equal to the <code>value-pattern</code>. </p>
 </dd></dl>
<p> --type &lt;type&gt; </p>
<dl>
<dd> <p> <i>git config</i> will ensure that any input or output is valid under the given type constraint(s), and will canonicalize outgoing values in <code>&lt;type&gt;</code>&#8216;s canonical form. </p>
<p> Valid <code>&lt;type&gt;</code>&#8216;s include: </p>
 </dd>
<dl>
<dd> <p> &bull; <i>bool</i>: canonicalize values as either &quot;true&quot; or &quot;false&quot;. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <i>int</i>: canonicalize values as simple decimal numbers. An optional suffix of <i>k</i>, <i>m</i>, or <i>g</i> will cause the value to be multiplied by 1024, 1048576, or 1073741824 upon input. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <i>bool-or-int</i>: canonicalize according to either <i>bool</i> or <i>int</i>, as described above. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <i>path</i>: canonicalize by adding a leading <code>~</code> to the value of <code>$HOME</code> and <code>~user</code> to the home directory for the specified user. This specifier has no effect when setting the value (but you can use <code>git config section.variable ~/</code> from the command line to let your shell do the expansion.) </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <i>expiry-date</i>: canonicalize by converting from a fixed or relative date-string to a timestamp. This specifier has no effect when setting the value. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <i>color</i>: When getting a value, canonicalize by converting to an ANSI color escape sequence. When setting a value, a sanity-check is performed to ensure that the given value is canonicalize-able as an ANSI color, but it is written as-is. </p>
 </dd></dl>
</dl>
<p> --bool, --int, --bool-or-int, --path, --expiry-date </p>
<dl>
<dd> <p> Historical options for selecting a type specifier. Prefer instead <code>--type</code> (see above). </p>
 </dd></dl>
<p> --no-type </p>
<dl>
<dd> <p> Un-sets the previously set type specifier (if one was previously set). This option requests that <i>git config</i> not canonicalize the retrieved variable. <code>--no-type</code> has no effect without <code>--type=&lt;type&gt;</code> or <code>--&lt;type&gt;</code>. </p>
 </dd></dl>
<p> -z, --null </p>
<dl>
<dd> <p> For all options that output values and/or keys, always end values with the null character (instead of a newline). Use newline instead as a delimiter between key and value. This allows for secure parsing of the output without getting confused e.g. by values that contain line breaks. </p>
 </dd></dl>
<p> --name-only </p>
<dl>
<dd> <p> Output only the names of config variables for <code>--list</code> or <code>--get-regexp</code>. </p>
 </dd></dl>
<p> --show-origin </p>
<dl>
<dd> <p> Augment the output of all queried config options with the origin type (file, standard input, blob, command line) and the actual origin (config file path, ref, or blob id if applicable). </p>
 </dd></dl>
<p> --show-scope </p>
<dl>
<dd> <p> Similar to <code>--show-origin</code> in that it augments the output of all queried config options with the scope of that value (local, global, system, command). </p>
 </dd></dl>
<p> --get-colorbool name [stdout-is-tty] </p>
<dl>
<dd> <p> Find the color setting for <code>name</code> (e.g. <code>color.diff</code>) and output &quot;true&quot; or &quot;false&quot;. <code>stdout-is-tty</code> should be either &quot;true&quot; or &quot;false&quot;, and is taken into account when configuration says &quot;auto&quot;. If <code>stdout-is-tty</code> is missing, then checks the standard output of the command itself, and exits with status 0 if color is to be used, or exits with status 1 otherwise. When the color setting for <code>name</code> is undefined, the command uses <code>color.ui</code> as fallback. </p>
 </dd></dl>
<p> --get-color name [default] </p>
<dl>
<dd> <p> Find the color configured for <code>name</code> (e.g. <code>color.diff.new</code>) and output it as the ANSI color escape sequence to the standard output. The optional <code>default</code> parameter is used instead, if there is no color configured for <code>name</code>. </p>
<p> <code>--type=color [--default=&lt;default&gt;]</code> is preferred over <code>--get-color</code> (but note that <code>--get-color</code> will omit the trailing newline printed by <code>--type=color</code>). </p>
 </dd></dl>
<p> -e, --edit </p>
<dl>
<dd> <p> Opens an editor to modify the specified config file; either <code>--system</code>, <code>--global</code>, or repository (default). </p>
 </dd></dl>
<p> --[no-]includes </p>
<dl>
<dd> <p> Respect <code>include.*</code> directives in config files when looking up values. Defaults to <code>off</code> when a specific file is given (e.g., using <code>--file</code>, <code>--global</code>, etc) and <code>on</code> when searching all config files. </p>
 </dd></dl>
<p> --default &lt;value&gt; </p>
<dl>
<dd> <p> When using <code>--get</code>, and the requested variable is not found, behave as if &lt;value&gt; were the value assigned to the that variable. </p>
 </dd></dl>
<h2>CONFIGURATION</h2>
<p> <code>pager.config</code> is only respected when listing configuration, i.e., when using <code>--list</code> or any of the <code>--get-*</code> which may return multiple results. The default is to use a pager.  </p>
<h2>FILES</h2>
<p> If not set explicitly with <code>--file</code>, there are four files where <i>git config</i> will search for configuration options: </p>
<p> $(prefix)/etc/gitconfig </p>
<dl>
<dd> <p> System-wide configuration file. </p>
 </dd></dl>
<p> $XDG_CONFIG_HOME/git/config </p>
<dl>
<dd> <p> Second user-specific configuration file. If $XDG_CONFIG_HOME is not set or empty, <code>$HOME/.config/git/config</code> will be used. Any single-valued variable set in this file will be overwritten by whatever is in <code>~/.gitconfig</code>. It is a good idea not to create this file if you sometimes use older versions of Git, as support for this file was added fairly recently. </p>
 </dd></dl>
<p> ~/.gitconfig </p>
<dl>
<dd> <p> User-specific configuration file. Also called &quot;global&quot; configuration file. </p>
 </dd></dl>
<p> $GIT_DIR/config </p>
<dl>
<dd> <p> Repository specific configuration file. </p>
 </dd></dl>
<p> $GIT_DIR/config.worktree </p>
<dl>
<dd> <p> This is optional and is only searched when <code>extensions.worktreeConfig</code> is present in $GIT_DIR/config. </p>
 </dd></dl>
<p> If no further options are given, all reading options will read all of these files that are available. If the global or the system-wide configuration file are not available they will be ignored. If the repository configuration file is not available or readable, <i>git config</i> will exit with a non-zero error code. However, in neither case will an error message be issued. </p>
<p> The files are read in the order given above, with last value found taking precedence over values read earlier. When multiple values are taken then all values of a key from all files will be used. </p>
<p> You may override individual configuration parameters when running any git command by using the <code>-c</code> option. See <code><a href="/docs/linux/man/1-git/">git</a></code>(1) for details. </p>
<p> All writing options will per default write to the repository specific configuration file. Note that this also affects options like <code>--replace-all</code> and <code>--unset</code>. <i>git config</i><code> will only ever change one file at a time</code>. </p>
<p> You can override these rules using the <code>--global</code>, <code>--system</code>, <code>--local</code>, <code>--worktree</code>, and <code>--file</code> command-line options; see the section called "OPTIONS" above.  </p>
<h2>ENVIRONMENT</h2>
<p> GIT_CONFIG_GLOBAL, GIT_CONFIG_SYSTEM </p>
<dl>
<dd> <p> Take the configuration from the given files instead from global or system-level configuration. See <code><a href="/docs/linux/man/1-git/">git</a></code>(1) for details. </p>
 </dd></dl>
<p> GIT_CONFIG_NOSYSTEM </p>
<dl>
<dd> <p> Whether to skip reading settings from the system-wide $(prefix)/etc/gitconfig file. See <code><a href="/docs/linux/man/1-git/">git</a></code>(1) for details. </p>
 </dd></dl>
<p> See also the section called "FILES". </p>
<p> GIT_CONFIG_COUNT, GIT_CONFIG_KEY_&lt;n&gt;, GIT_CONFIG_VALUE_&lt;n&gt; </p>
<dl>
<dd> <p> If GIT_CONFIG_COUNT is set to a positive number, all environment pairs GIT_CONFIG_KEY_&lt;n&gt; and GIT_CONFIG_VALUE_&lt;n&gt; up to that number will be added to the process&#8217;s runtime configuration. The config pairs are zero-indexed. Any missing key or value is treated as an error. An empty GIT_CONFIG_COUNT is treated the same as GIT_CONFIG_COUNT=0, namely no pairs are processed. These environment variables will override values in configuration files, but will be overridden by any explicit options passed via <code>git -c</code>. </p>
<p> This is useful for cases where you want to spawn multiple git commands with a common configuration but cannot depend on a configuration file, for example when writing scripts. </p>
 </dd></dl>
<p> GIT_CONFIG </p>
<dl>
<dd> <p> If no <code>--file</code> option is provided to <code>git config</code>, use the file given by <code>GIT_CONFIG</code> as if it were provided via <code>--file</code>. This variable has no effect on other Git commands, and is mostly for historical compatibility; there is generally no reason to use it instead of the <code>--file</code> option. </p>
 </dd></dl>
<h2>EXAMPLES</h2>
<p> Given a .git/config like this: </p>
<dl>
<dd> <pre><code>#
# This is the config file, and
# a '#' or ';' character indicates
# a comment
#
; core variables
[core]
        ; Don't trust file modes
        filemode = false
; Our diff algorithm
[diff]
        external = /usr/local/bin/diff-wrapper
        renames = true
; Proxy settings
[core]
        gitproxy=proxy-command for kernel.org
        gitproxy=default-proxy ; for all the rest
; HTTP
[http]
        sslVerify
[http &quot;https://weak.example.com&quot;]
        sslVerify = false
        cookieFile = /tmp/cookie.txt
</code></pre>
 </dd></dl>
<p> you can set the filemode to true with </p>
<dl>
<dd> <pre><code>% git config core.filemode true
</code></pre>
 </dd></dl>
<p> The hypothetical proxy command entries actually have a postfix to discern what URL they apply to. Here is how to change the entry for kernel.org to &quot;ssh&quot;. </p>
<dl>
<dd> <pre><code>% git config core.gitproxy '&quot;ssh&quot; for kernel.org' 'for kernel.org$'
</code></pre>
 </dd></dl>
<p> This makes sure that only the key/value pair for kernel.org is replaced. </p>
<p> To delete the entry for renames, do </p>
<dl>
<dd> <pre><code>% git config --unset diff.renames
</code></pre>
 </dd></dl>
<p> If you want to delete an entry for a multivar (like core.gitproxy above), you have to provide a regex matching the value of exactly one line. </p>
<p> To query the value for a given key, do </p>
<dl>
<dd> <pre><code>% git config --get core.filemode
</code></pre>
 </dd></dl>
<p> or </p>
<dl>
<dd> <pre><code>% git config core.filemode
</code></pre>
 </dd></dl>
<p> or, to query a multivar: </p>
<dl>
<dd> <pre><code>% git config --get core.gitproxy &quot;for kernel.org$&quot;
</code></pre>
 </dd></dl>
<p> If you want to know all the values for a multivar, do: </p>
<dl>
<dd> <pre><code>% git config --get-all core.gitproxy
</code></pre>
 </dd></dl>
<p> If you like to live dangerously, you can replace <code>all</code> core.gitproxy by a new one with </p>
<dl>
<dd> <pre><code>% git config --replace-all core.gitproxy ssh
</code></pre>
 </dd></dl>
<p> However, if you really only want to replace the line for the default proxy, i.e. the one without a &quot;for ...&quot; postfix, do something like this: </p>
<dl>
<dd> <pre><code>% git config core.gitproxy ssh '! for '
</code></pre>
 </dd></dl>
<p> To actually match only values with an exclamation mark, you have to </p>
<dl>
<dd> <pre><code>% git config section.key value '[!]'
</code></pre>
 </dd></dl>
<p> To add a new proxy, without altering any of the existing ones, use </p>
<dl>
<dd> <pre><code>% git config --add core.gitproxy '&quot;proxy-command&quot; for example.com'
</code></pre>
 </dd></dl>
<p> An example to use customized color from the configuration in your script: </p>
<dl>
<dd> <pre><code>#!/bin/sh
WS=$(git config --get-color color.diff.whitespace &quot;blue reverse&quot;)
RESET=$(git config --get-color &quot;&quot; &quot;reset&quot;)
echo &quot;${WS}your whitespace color or blue reverse${RESET}&quot;
</code></pre>
 </dd></dl>
<p> For URLs in <code><a rel="nofollow" href="https://weak.example.com">https://weak.example.com</a></code>, <code>http.sslVerify</code> is set to false, while it is set to <code>true</code> for all others: </p>
<dl>
<dd> <pre><code>% git config --type=bool --get-urlmatch http.sslverifyhttps://good.example.comtrue
% git config --type=bool --get-urlmatch http.sslverifyhttps://weak.example.comfalse
% git config --get-urlmatch httphttps://weak.example.comhttp.cookieFile /tmp/cookie.txt
http.sslverify false
</code></pre>
 </dd></dl>
<h2>CONFIGURATION FILE</h2>
<p> The Git configuration file contains a number of variables that affect the Git commands&#8217; behavior. The files <code>.git/config</code> and optionally <code>config.worktree</code> (see the &quot;CONFIGURATION FILE&quot; section of <code><a href="/docs/linux/man/1-git-worktree/">git-worktree</a></code>(1)) in each repository are used to store the configuration for that repository, and <code>$HOME/.gitconfig</code> is used to store a per-user configuration as fallback values for the <code>.git/config</code> file. The file <code>/etc/gitconfig</code> can be used to store a system-wide default configuration. </p>
<p> The configuration variables are used by both the Git plumbing and the porcelains. The variables are divided into sections, wherein the fully qualified variable name of the variable itself is the last dot-separated segment and the section name is everything before the last dot. The variable names are case-insensitive, allow only alphanumeric characters and <code>-</code>, and must start with an alphabetic character. Some variables may appear multiple times; we say then that the variable is multivalued.  </p>
<h3>Syntax</h3>
<p> The syntax is fairly flexible and permissive; whitespaces are mostly ignored. The <i>#</i> and <i>;</i> characters begin comments to the end of line, blank lines are ignored. </p>
<p> The file consists of sections and variables. A section begins with the name of the section in square brackets and continues until the next section begins. Section names are case-insensitive. Only alphanumeric characters, <code>-</code> and <code>.</code> are allowed in section names. Each variable must belong to some section, which means that there must be a section header before the first setting of a variable. </p>
<p> Sections can be further divided into subsections. To begin a subsection put its name in double quotes, separated by space from the section name, in the section header, like in the example below: </p>
<dl>
<dd> <pre><code>        [section &quot;subsection&quot;]
</code></pre>
 </dd></dl>
<p> Subsection names are case sensitive and can contain any characters except newline and the null byte. Doublequote <code>&quot;</code> and backslash can be included by escaping them as <code>\&quot;</code> and <code>\\</code>, respectively. Backslashes preceding other characters are dropped when reading; for example, <code>\t</code> is read as <code>t</code> and <code>\0</code> is read as <code>0</code>. Section headers cannot span multiple lines. Variables may belong directly to a section or to a given subsection. You can have <code>[section]</code> if you have <code>[section &quot;subsection&quot;]</code>, but you don&#8217;t need to. </p>
<p> There is also a deprecated <code>[section.subsection]</code> syntax. With this syntax, the subsection name is converted to lower-case and is also compared case sensitively. These subsection names follow the same restrictions as section names. </p>
<p> All the other lines (and the remainder of the line after the section header) are recognized as setting variables, in the form <i>name = value</i> (or just <i>name</i>, which is a short-hand to say that the variable is the boolean &quot;true&quot;). The variable names are case-insensitive, allow only alphanumeric characters and <code>-</code>, and must start with an alphabetic character. </p>
<p> A line that defines a value can be continued to the next line by ending it with a <code>\</code>; the backslash and the end-of-line are stripped. Leading whitespaces after <i>name =</i>, the remainder of the line after the first comment character <i>#</i> or <i>;</i>, and trailing whitespaces of the line are discarded unless they are enclosed in double quotes. Internal whitespaces within the value are retained verbatim. </p>
<p> Inside double quotes, double quote <code>&quot;</code> and backslash <code>\</code> characters must be escaped: use <code>\&quot;</code> for <code>&quot;</code> and <code>\\</code> for <code>\</code>. </p>
<p> The following escape sequences (beside <code>\&quot;</code> and <code>\\</code>) are recognized: <code>\n</code> for newline character (NL), <code>\t</code> for horizontal tabulation (HT, TAB) and <code>\b</code> for backspace (BS). Other char escape sequences (including octal escape sequences) are invalid.  </p>
<h3>Includes</h3>
<p> The <code>include</code> and <code>includeIf</code> sections allow you to include config directives from another source. These sections behave identically to each other with the exception that <code>includeIf</code> sections may be ignored if their condition does not evaluate to true; see &quot;Conditional includes&quot; below. </p>
<p> You can include a config file from another by setting the special <code>include.path</code> (or <code>includeIf.*.path</code>) variable to the name of the file to be included. The variable takes a pathname as its value, and is subject to tilde expansion. These variables can be given multiple times. </p>
<p> The contents of the included file are inserted immediately, as if they had been found at the location of the include directive. If the value of the variable is a relative path, the path is considered to be relative to the configuration file in which the include directive was found. See below for examples.  </p>
<h3>Conditional includes</h3>
<p> You can include a config file from another conditionally by setting a <code>includeIf.&lt;condition&gt;.path</code> variable to the name of the file to be included. </p>
<p> The condition starts with a keyword followed by a colon and some data whose format and meaning depends on the keyword. Supported keywords are: </p>
<p> <code>gitdir</code> </p>
<dl>
<dd> <p> The data that follows the keyword <code>gitdir:</code> is used as a glob pattern. If the location of the .git directory matches the pattern, the include condition is met. </p>
<p> The .git location may be auto-discovered, or come from <code>$GIT_DIR</code> environment variable. If the repository is auto discovered via a .git file (e.g. from submodules, or a linked worktree), the .git location would be the final location where the .git directory is, not where the .git file is. </p>
<p> The pattern can contain standard globbing wildcards and two additional ones, <code>**/</code> and <code>/**</code>, that can match multiple path components. Please refer to <code><a href="/docs/linux/man/5-gitignore/">gitignore</a></code>(5) for details. For convenience: </p>
 </dd>
<dl>
<dd> <p> &bull; If the pattern starts with <code>~/</code>, <code>~</code> will be substituted with the content of the environment variable <code>HOME</code>. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; If the pattern starts with <code>./</code>, it is replaced with the directory containing the current config file. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; If the pattern does not start with either <code>~/</code>, <code>./</code> or <code>/</code>, <code>**/</code> will be automatically prepended. For example, the pattern <code>foo/bar</code> becomes <code>**/foo/bar</code> and would match <code>/any/path/to/foo/bar</code>. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; If the pattern ends with <code>/</code>, <code>**</code> will be automatically added. For example, the pattern <code>foo/</code> becomes <code>foo/**</code>. In other words, it matches &quot;foo&quot; and everything inside, recursively. </p>
 </dd></dl>
</dl>
<p> <code>gitdir/i</code> </p>
<dl>
<dd> <p> This is the same as <code>gitdir</code> except that matching is done case-insensitively (e.g. on case-insensitive file systems) </p>
 </dd></dl>
<p> <code>onbranch</code> </p>
<dl>
<dd> <p> The data that follows the keyword <code>onbranch:</code> is taken to be a pattern with standard globbing wildcards and two additional ones, <code>**/</code> and <code>/**</code>, that can match multiple path components. If we are in a worktree where the name of the branch that is currently checked out matches the pattern, the include condition is met. </p>
<p> If the pattern ends with <code>/</code>, <code>**</code> will be automatically added. For example, the pattern <code>foo/</code> becomes <code>foo/**</code>. In other words, it matches all branches that begin with <code>foo/</code>. This is useful if your branches are organized hierarchically and you would like to apply a configuration to all the branches in that hierarchy. </p>
 </dd></dl>
<p> A few more notes on matching via <code>gitdir</code> and <code>gitdir/i</code>: </p>
<dl>
<dd> <p> &bull; Symlinks in <code>$GIT_DIR</code> are not resolved before matching. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; Both the symlink &amp; realpath versions of paths will be matched outside of <code>$GIT_DIR</code>. E.g. if ~/git is a symlink to /mnt/storage/git, both <code>gitdir:~/git</code> and <code>gitdir:/mnt/storage/git</code> will match. </p>
<p> This was not the case in the initial release of this feature in v2.13.0, which only matched the realpath version. Configuration that wants to be compatible with the initial release of this feature needs to either specify only the realpath version, or both versions. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; Note that &quot;../&quot; is not special and will match literally, which is unlikely what you want. </p>
 </dd></dl>
<h3>Example</h3>
<dl>
<dd> <pre><code># Core variables
[core]
        ; Don't trust file modes
        filemode = false
# Our diff algorithm
[diff]
        external = /usr/local/bin/diff-wrapper
        renames = true
[branch &quot;devel&quot;]
        remote = origin
        merge = refs/heads/devel
# Proxy settings
[core]
        gitProxy=&quot;ssh&quot; for &quot;kernel.org&quot;
        gitProxy=default-proxy ; for the rest
[include]
        path = /path/to/foo.inc ; include by absolute path
        path = foo.inc ; find &quot;foo.inc&quot; relative to the current file
        path = ~/foo.inc ; find &quot;foo.inc&quot; in your `$HOME` directory
; include if $GIT_DIR is /path/to/foo/.git
[includeIf &quot;gitdir:/path/to/foo/.git&quot;]
        path = /path/to/foo.inc
; include for all repositories inside /path/to/group
[includeIf &quot;gitdir:/path/to/group/&quot;]
        path = /path/to/foo.inc
; include for all repositories inside $HOME/to/group
[includeIf &quot;gitdir:~/to/group/&quot;]
        path = /path/to/foo.inc
; relative paths are always relative to the including
; file (if the condition is true); their location is not
; affected by the condition
[includeIf &quot;gitdir:/path/to/group/&quot;]
        path = foo.inc
; include only if we are in a worktree where foo-branch is
; currently checked out
[includeIf &quot;onbranch:foo-branch&quot;]
        path = foo.inc
</code></pre>
 </dd></dl>
<h3>Values</h3>
<p> Values of many variables are treated as a simple string, but there are variables that take values of specific types and there are rules as to how to spell them. </p>
<p> boolean </p>
<dl>
<dd> <p> When a variable is said to take a boolean value, many synonyms are accepted for <i>true</i> and <i>false</i>; these are all case-insensitive. </p>
<p> true </p>
 </dd>
<dl>
<dd> <p> Boolean true literals are <code>yes</code>, <code>on</code>, <code>true</code>, and <code>1</code>. Also, a variable defined without <code>= &lt;value&gt;</code> is taken as true. </p>
 </dd></dl>
<p> false </p>
<dl>
<dd> <p> Boolean false literals are <code>no</code>, <code>off</code>, <code>false</code>, <code>0</code> and the empty string. </p>
<p> When converting a value to its canonical form using the <code>--type=bool</code> type specifier, <i>git config</i> will ensure that the output is &quot;true&quot; or &quot;false&quot; (spelled in lowercase). </p>
 </dd></dl>
</dl>
<p> integer </p>
<dl>
<dd> <p> The value for many variables that specify various sizes can be suffixed with <code>k</code>, <code>M</code>,... to mean &quot;scale the number by 1024&quot;, &quot;by 1024x1024&quot;, etc. </p>
 </dd></dl>
<p> color </p>
<dl>
<dd> <p> The value for a variable that takes a color is a list of colors (at most two, one for foreground and one for background) and attributes (as many as you want), separated by spaces. </p>
<p> The basic colors accepted are <code>normal</code>, <code>black</code>, <code>red</code>, <code>green</code>, <code>yellow</code>, <code>blue</code>, <code>magenta</code>, <code>cyan</code> and <code>white</code>. The first color given is the foreground; the second is the background. All the basic colors except <code>normal</code> have a bright variant that can be specified by prefixing the color with <code>bright</code>, like <code>brightred</code>. </p>
<p> Colors may also be given as numbers between 0 and 255; these use ANSI 256-color mode (but note that not all terminals may support this). If your terminal supports it, you may also specify 24-bit RGB values as hex, like <code>#ff0ab3</code>. </p>
<p> The accepted attributes are <code>bold</code>, <code>dim</code>, <code>ul</code>, <code>blink</code>, <code>reverse</code>, <code>italic</code>, and <code>strike</code> (for crossed-out or &quot;strikethrough&quot; letters). The position of any attributes with respect to the colors (before, after, or in between), doesn&#8217;t matter. Specific attributes may be turned off by prefixing them with <code>no</code> or <code>no-</code> (e.g., <code>noreverse</code>, <code>no-ul</code>, etc). </p>
<p> An empty color string produces no color effect at all. This can be used to avoid coloring specific elements without disabling color entirely. </p>
<p> For git&#8217;s pre-defined color slots, the attributes are meant to be reset at the beginning of each item in the colored output. So setting <code>color.decorate.branch</code> to <code>black</code> will paint that branch name in a plain <code>black</code>, even if the previous thing on the same output line (e.g. opening parenthesis before the list of branch names in <code>log --decorate</code> output) is set to be painted with <code>bold</code> or some other attribute. However, custom log formats may do more complicated and layered coloring, and the negated forms may be useful there. </p>
 </dd></dl>
<p> pathname </p>
<dl>
<dd> <p> A variable that takes a pathname value can be given a string that begins with &quot;<code>~/</code>&quot; or &quot;<code>~user/</code>&quot;, and the usual tilde expansion happens to such a string: <code>~/</code> is expanded to the value of <code>$HOME</code>, and <code>~user/</code> to the specified user&#8217;s home directory. </p>
<p> If a path starts with <code>%(prefix)/</code>, the remainder is interpreted as a path relative to Git&#8217;s &quot;runtime prefix&quot;, i.e. relative to the location where Git itself was installed. For example, <code>%(prefix)/bin/</code> refers to the directory in which the Git executable itself lives. If Git was compiled without runtime prefix support, the compiled-in prefix will be substituted instead. In the unlikely event that a literal path needs to be specified that should <i>not</i> be expanded, it needs to be prefixed by <code>./</code>, like so: <code>./%(prefix)/bin</code>. </p>
 </dd></dl>
<h3>Variables</h3>
<p> Note that this list is non-comprehensive and not necessarily complete. For command-specific variables, you will find a more detailed description in the appropriate manual page. </p>
<p> Other git-related tools may and do use their own variables. When inventing new variables for use in your own tool, make sure their names do not conflict with those that are used by Git itself and other popular tools, and describe them in your documentation. </p>
<p> advice.* </p>
<dl>
<dd> <p> These variables control various optional help messages designed to aid new users. All <i>advice.*</i> variables default to <i>true</i>, and you can tell Git that you do not need help by setting these to <i>false</i>: </p>
<p> fetchShowForcedUpdates </p>
 </dd>
<dl>
<dd> <p> Advice shown when <code><a href="/docs/linux/man/1-git-fetch/">git-fetch</a></code>(1) takes a long time to calculate forced updates after ref updates, or to warn that the check is disabled. </p>
 </dd></dl>
<p> pushUpdateRejected </p>
<dl>
<dd> <p> Set this variable to <i>false</i> if you want to disable <i>pushNonFFCurrent</i>, <i>pushNonFFMatching</i>, <i>pushAlreadyExists</i>, <i>pushFetchFirst</i>, <i>pushNeedsForce</i>, and <i>pushRefNeedsUpdate</i> simultaneously. </p>
 </dd></dl>
<p> pushNonFFCurrent </p>
<dl>
<dd> <p> Advice shown when <code><a href="/docs/linux/man/1-git-push/">git-push</a></code>(1) fails due to a non-fast-forward update to the current branch. </p>
 </dd></dl>
<p> pushNonFFMatching </p>
<dl>
<dd> <p> Advice shown when you ran <code><a href="/docs/linux/man/1-git-push/">git-push</a></code>(1) and pushed <i>matching refs</i> explicitly (i.e. you used <i>:</i>, or specified a refspec that isn&#8217;t your current branch) and it resulted in a non-fast-forward error. </p>
 </dd></dl>
<p> pushAlreadyExists </p>
<dl>
<dd> <p> Shown when <code><a href="/docs/linux/man/1-git-push/">git-push</a></code>(1) rejects an update that does not qualify for fast-forwarding (e.g., a tag.) </p>
 </dd></dl>
<p> pushFetchFirst </p>
<dl>
<dd> <p> Shown when <code><a href="/docs/linux/man/1-git-push/">git-push</a></code>(1) rejects an update that tries to overwrite a remote ref that points at an object we do not have. </p>
 </dd></dl>
<p> pushNeedsForce </p>
<dl>
<dd> <p> Shown when <code><a href="/docs/linux/man/1-git-push/">git-push</a></code>(1) rejects an update that tries to overwrite a remote ref that points at an object that is not a commit-ish, or make the remote ref point at an object that is not a commit-ish. </p>
 </dd></dl>
<p> pushUnqualifiedRefname </p>
<dl>
<dd> <p> Shown when <code><a href="/docs/linux/man/1-git-push/">git-push</a></code>(1) gives up trying to guess based on the source and destination refs what remote ref namespace the source belongs in, but where we can still suggest that the user push to either refs/heads/* or refs/tags/* based on the type of the source object. </p>
 </dd></dl>
<p> pushRefNeedsUpdate </p>
<dl>
<dd> <p> Shown when <code><a href="/docs/linux/man/1-git-push/">git-push</a></code>(1) rejects a forced update of a branch when its remote-tracking ref has updates that we do not have locally. </p>
 </dd></dl>
<p> skippedCherryPicks </p>
<dl>
<dd> <p> Shown when <code><a href="/docs/linux/man/1-git-rebase/">git-rebase</a></code>(1) skips a commit that has already been cherry-picked onto the upstream branch. </p>
 </dd></dl>
<p> statusAheadBehind </p>
<dl>
<dd> <p> Shown when <code><a href="/docs/linux/man/1-git-status/">git-status</a></code>(1) computes the ahead/behind counts for a local ref compared to its remote tracking ref, and that calculation takes longer than expected. Will not appear if <code>status.aheadBehind</code> is false or the option <code>--no-ahead-behind</code> is given. </p>
 </dd></dl>
<p> statusHints </p>
<dl>
<dd> <p> Show directions on how to proceed from the current state in the output of <code><a href="/docs/linux/man/1-git-status/">git-status</a></code>(1), in the template shown when writing commit messages in <code><a href="/docs/linux/man/1-git-commit/">git-commit</a></code>(1), and in the help message shown by <code><a href="/docs/linux/man/1-git-switch/">git-switch</a></code>(1) or <code><a href="/docs/linux/man/1-git-checkout/">git-checkout</a></code>(1) when switching branch. </p>
 </dd></dl>
<p> statusUoption </p>
<dl>
<dd> <p> Advise to consider using the <code>-u</code> option to <code><a href="/docs/linux/man/1-git-status/">git-status</a></code>(1) when the command takes more than 2 seconds to enumerate untracked files. </p>
 </dd></dl>
<p> commitBeforeMerge </p>
<dl>
<dd> <p> Advice shown when <code><a href="/docs/linux/man/1-git-merge/">git-merge</a></code>(1) refuses to merge to avoid overwriting local changes. </p>
 </dd></dl>
<p> resetQuiet </p>
<dl>
<dd> <p> Advice to consider using the <code>--quiet</code> option to <code><a href="/docs/linux/man/1-git-reset/">git-reset</a></code>(1) when the command takes more than 2 seconds to enumerate unstaged changes after reset. </p>
 </dd></dl>
<p> resolveConflict </p>
<dl>
<dd> <p> Advice shown by various commands when conflicts prevent the operation from being performed. </p>
 </dd></dl>
<p> sequencerInUse </p>
<dl>
<dd> <p> Advice shown when a sequencer command is already in progress. </p>
 </dd></dl>
<p> implicitIdentity </p>
<dl>
<dd> <p> Advice on how to set your identity configuration when your information is guessed from the system username and domain name. </p>
 </dd></dl>
<p> detachedHead </p>
<dl>
<dd> <p> Advice shown when you used <code><a href="/docs/linux/man/1-git-switch/">git-switch</a></code>(1) or <code><a href="/docs/linux/man/1-git-checkout/">git-checkout</a></code>(1) to move to the detach HEAD state, to instruct how to create a local branch after the fact. </p>
 </dd></dl>
<p> checkoutAmbiguousRemoteBranchName </p>
<dl>
<dd> <p> Advice shown when the argument to <code><a href="/docs/linux/man/1-git-checkout/">git-checkout</a></code>(1) and <code><a href="/docs/linux/man/1-git-switch/">git-switch</a></code>(1) ambiguously resolves to a remote tracking branch on more than one remote in situations where an unambiguous argument would have otherwise caused a remote-tracking branch to be checked out. See the <code>checkout.defaultRemote</code> configuration variable for how to set a given remote to used by default in some situations where this advice would be printed. </p>
 </dd></dl>
<p> amWorkDir </p>
<dl>
<dd> <p> Advice that shows the location of the patch file when <code><a href="/docs/linux/man/1-git-am/">git-am</a></code>(1) fails to apply it. </p>
 </dd></dl>
<p> rmHints </p>
<dl>
<dd> <p> In case of failure in the output of <code><a href="/docs/linux/man/1-git-rm/">git-rm</a></code>(1), show directions on how to proceed from the current state. </p>
 </dd></dl>
<p> addEmbeddedRepo </p>
<dl>
<dd> <p> Advice on what to do when you&#8217;ve accidentally added one git repo inside of another. </p>
 </dd></dl>
<p> ignoredHook </p>
<dl>
<dd> <p> Advice shown if a hook is ignored because the hook is not set as executable. </p>
 </dd></dl>
<p> waitingForEditor </p>
<dl>
<dd> <p> Print a message to the terminal whenever Git is waiting for editor input from the user. </p>
 </dd></dl>
<p> nestedTag </p>
<dl>
<dd> <p> Advice shown if a user attempts to recursively tag a tag object. </p>
 </dd></dl>
<p> submoduleAlternateErrorStrategyDie </p>
<dl>
<dd> <p> Advice shown when a submodule.alternateErrorStrategy option configured to &quot;die&quot; causes a fatal error. </p>
 </dd></dl>
<p> addIgnoredFile </p>
<dl>
<dd> <p> Advice shown if a user attempts to add an ignored file to the index. </p>
 </dd></dl>
<p> addEmptyPathspec </p>
<dl>
<dd> <p> Advice shown if a user runs the add command without providing the pathspec parameter. </p>
 </dd></dl>
<p> updateSparsePath </p>
<dl>
<dd> <p> Advice shown when either <code><a href="/docs/linux/man/1-git-add/">git-add</a></code>(1) or <code><a href="/docs/linux/man/1-git-rm/">git-rm</a></code>(1) is asked to update index entries outside the current sparse checkout. </p>
 </dd></dl>
</dl>
<p> core.fileMode </p>
<dl>
<dd> <p> Tells Git if the executable bit of files in the working tree is to be honored. </p>
<p> Some filesystems lose the executable bit when a file that is marked as executable is checked out, or checks out a non-executable file with executable bit on. <code><a href="/docs/linux/man/1-git-clone/">git-clone</a></code>(1) or <code><a href="/docs/linux/man/1-git-init/">git-init</a></code>(1) probe the filesystem to see if it handles the executable bit correctly and this variable is automatically set as necessary. </p>
<p> A repository, however, may be on a filesystem that handles the filemode correctly, and this variable is set to <i>true</i> when created, but later may be made accessible from another environment that loses the filemode (e.g. exporting ext4 via CIFS mount, visiting a Cygwin created repository with Git for Windows or Eclipse). In such a case it may be necessary to set this variable to <i>false</i>. See <code><a href="/docs/linux/man/1-git-update-index/">git-update-index</a></code>(1). </p>
<p> The default is true (when core.filemode is not specified in the config file). </p>
 </dd></dl>
<p> core.hideDotFiles </p>
<dl>
<dd> <p> (Windows-only) If true, mark newly-created directories and files whose name starts with a dot as hidden. If <i>dotGitOnly</i>, only the <code>.git/</code> directory is hidden, but no other files starting with a dot. The default mode is <i>dotGitOnly</i>. </p>
 </dd></dl>
<p> core.ignoreCase </p>
<dl>
<dd> <p> Internal variable which enables various workarounds to enable Git to work better on filesystems that are not case sensitive, like APFS, HFS+, FAT, NTFS, etc. For example, if a directory listing finds &quot;makefile&quot; when Git expects &quot;Makefile&quot;, Git will assume it is really the same file, and continue to remember it as &quot;Makefile&quot;. </p>
<p> The default is false, except <code><a href="/docs/linux/man/1-git-clone/">git-clone</a></code>(1) or <code><a href="/docs/linux/man/1-git-init/">git-init</a></code>(1) will probe and set core.ignoreCase true if appropriate when the repository is created. </p>
<p> Git relies on the proper configuration of this variable for your operating and file system. Modifying this value may result in unexpected behavior. </p>
 </dd></dl>
<p> core.precomposeUnicode </p>
<dl>
<dd> <p> This option is only used by Mac OS implementation of Git. When core.precomposeUnicode=true, Git reverts the unicode decomposition of filenames done by Mac OS. This is useful when sharing a repository between Mac OS and Linux or Windows. (Git for Windows 1.7.10 or higher is needed, or Git under cygwin 1.7). When false, file names are handled fully transparent by Git, which is backward compatible with older versions of Git. </p>
 </dd></dl>
<p> core.protectHFS </p>
<dl>
<dd> <p> If set to true, do not allow checkout of paths that would be considered equivalent to <code>.git</code> on an HFS+ filesystem. Defaults to <code>true</code> on Mac OS, and <code>false</code> elsewhere. </p>
 </dd></dl>
<p> core.protectNTFS </p>
<dl>
<dd> <p> If set to true, do not allow checkout of paths that would cause problems with the NTFS filesystem, e.g. conflict with 8.3 &quot;short&quot; names. Defaults to <code>true</code> on Windows, and <code>false</code> elsewhere. </p>
 </dd></dl>
<p> core.fsmonitor </p>
<dl>
<dd> <p> If set, the value of this variable is used as a command which will identify all files that may have changed since the requested date/time. This information is used to speed up git by avoiding unnecessary processing of files that have not changed. See the &quot;fsmonitor-watchman&quot; section of <code><a href="/docs/linux/man/5-githooks/">githooks</a></code>(5). </p>
 </dd></dl>
<p> core.fsmonitorHookVersion </p>
<dl>
<dd> <p> Sets the version of hook that is to be used when calling fsmonitor. There are currently versions 1 and 2. When this is not set, version 2 will be tried first and if it fails then version 1 will be tried. Version 1 uses a timestamp as input to determine which files have changes since that time but some monitors like watchman have race conditions when used with a timestamp. Version 2 uses an opaque string so that the monitor can return something that can be used to determine what files have changed without race conditions. </p>
 </dd></dl>
<p> core.trustctime </p>
<dl>
<dd> <p> If false, the ctime differences between the index and the working tree are ignored; useful when the inode change time is regularly modified by something outside Git (file system crawlers and some backup systems). See <code><a href="/docs/linux/man/1-git-update-index/">git-update-index</a></code>(1). True by default. </p>
 </dd></dl>
<p> core.splitIndex </p>
<dl>
<dd> <p> If true, the split-index feature of the index will be used. See <code><a href="/docs/linux/man/1-git-update-index/">git-update-index</a></code>(1). False by default. </p>
 </dd></dl>
<p> core.untrackedCache </p>
<dl>
<dd> <p> Determines what to do about the untracked cache feature of the index. It will be kept, if this variable is unset or set to <code>keep</code>. It will automatically be added if set to <code>true</code>. And it will automatically be removed, if set to <code>false</code>. Before setting it to <code>true</code>, you should check that mtime is working properly on your system. See <code><a href="/docs/linux/man/1-git-update-index/">git-update-index</a></code>(1). <code>keep</code> by default, unless <code>feature.manyFiles</code> is enabled which sets this setting to <code>true</code> by default. </p>
 </dd></dl>
<p> core.checkStat </p>
<dl>
<dd> <p> When missing or is set to <code>default</code>, many fields in the stat structure are checked to detect if a file has been modified since Git looked at it. When this configuration variable is set to <code>minimal</code>, sub-second part of mtime and ctime, the uid and gid of the owner of the file, the inode number (and the device number, if Git was compiled to use it), are excluded from the check among these fields, leaving only the whole-second part of mtime (and ctime, if <code>core.trustCtime</code> is set) and the filesize to be checked. </p>
<p> There are implementations of Git that do not leave usable values in some fields (e.g. JGit); by excluding these fields from the comparison, the <code>minimal</code> mode may help interoperability when the same repository is used by these other systems at the same time. </p>
 </dd></dl>
<p> core.quotePath </p>
<dl>
<dd> <p> Commands that output paths (e.g. <i>ls-files</i>, <i>diff</i>), will quote &quot;unusual&quot; characters in the pathname by enclosing the pathname in double-quotes and escaping those characters with backslashes in the same way C escapes control characters (e.g. <code>\t</code> for TAB, <code>\n</code> for LF, <code>\\</code> for backslash) or bytes with values larger than 0x80 (e.g. octal <code>\302\265</code> for &quot;micro&quot; in UTF-8). If this variable is set to false, bytes higher than 0x80 are not considered &quot;unusual&quot; any more. Double-quotes, backslash and control characters are always escaped regardless of the setting of this variable. A simple space character is not considered &quot;unusual&quot;. Many commands can output pathnames completely verbatim using the <code>-z</code> option. The default value is true. </p>
 </dd></dl>
<p> core.eol </p>
<dl>
<dd> <p> Sets the line ending type to use in the working directory for files that are marked as text (either by having the <code>text</code> attribute set, or by having <code>text=auto</code> and Git auto-detecting the contents as text). Alternatives are <i>lf</i>, <i>crlf</i> and <i>native</i>, which uses the platform&#8217;s native line ending. The default value is <code>native</code>. See <code><a href="/docs/linux/man/5-gitattributes/">gitattributes</a></code>(5) for more information on end-of-line conversion. Note that this value is ignored if <code>core.autocrlf</code> is set to <code>true</code> or <code>input</code>. </p>
 </dd></dl>
<p> core.safecrlf </p>
<dl>
<dd> <p> If true, makes Git check if converting <code>CRLF</code> is reversible when end-of-line conversion is active. Git will verify if a command modifies a file in the work tree either directly or indirectly. For example, committing a file followed by checking out the same file should yield the original file in the work tree. If this is not the case for the current setting of <code>core.autocrlf</code>, Git will reject the file. The variable can be set to &quot;warn&quot;, in which case Git will only warn about an irreversible conversion but continue the operation. </p>
<p> CRLF conversion bears a slight chance of corrupting data. When it is enabled, Git will convert CRLF to LF during commit and LF to CRLF during checkout. A file that contains a mixture of LF and CRLF before the commit cannot be recreated by Git. For text files this is the right thing to do: it corrects line endings such that we have only LF line endings in the repository. But for binary files that are accidentally classified as text the conversion can corrupt data. </p>
<p> If you recognize such corruption early you can easily fix it by setting the conversion type explicitly in .gitattributes. Right after committing you still have the original file in your work tree and this file is not yet corrupted. You can explicitly tell Git that this file is binary and Git will handle the file appropriately. </p>
<p> Unfortunately, the desired effect of cleaning up text files with mixed line endings and the undesired effect of corrupting binary files cannot be distinguished. In both cases CRLFs are removed in an irreversible way. For text files this is the right thing to do because CRLFs are line endings, while for binary files converting CRLFs corrupts data. </p>
<p> Note, this safety check does not mean that a checkout will generate a file identical to the original file for a different setting of <code>core.eol</code> and <code>core.autocrlf</code>, but only for the current one. For example, a text file with <code>LF</code> would be accepted with <code>core.eol=lf</code> and could later be checked out with <code>core.eol=crlf</code>, in which case the resulting file would contain <code>CRLF</code>, although the original file contained <code>LF</code>. However, in both work trees the line endings would be consistent, that is either all <code>LF</code> or all <code>CRLF</code>, but never mixed. A file with mixed line endings would be reported by the <code>core.safecrlf</code> mechanism. </p>
 </dd></dl>
<p> core.autocrlf </p>
<dl>
<dd> <p> Setting this variable to &quot;true&quot; is the same as setting the <code>text</code> attribute to &quot;auto&quot; on all files and core.eol to &quot;crlf&quot;. Set to true if you want to have <code>CRLF</code> line endings in your working directory and the repository has LF line endings. This variable can be set to <i>input</i>, in which case no output conversion is performed. </p>
 </dd></dl>
<p> core.checkRoundtripEncoding </p>
<dl>
<dd> <p> A comma and/or whitespace separated list of encodings that Git performs UTF-8 round trip checks on if they are used in an <code>working-tree-encoding</code> attribute (see <code><a href="/docs/linux/man/5-gitattributes/">gitattributes</a></code>(5)). The default value is <code>SHIFT-JIS</code>. </p>
 </dd></dl>
<p> core.symlinks </p>
<dl>
<dd> <p> If false, symbolic links are checked out as small plain files that contain the link text. <code><a href="/docs/linux/man/1-git-update-index/">git-update-index</a></code>(1) and <code><a href="/docs/linux/man/1-git-add/">git-add</a></code>(1) will not change the recorded type to regular file. Useful on filesystems like FAT that do not support symbolic links. </p>
<p> The default is true, except <code><a href="/docs/linux/man/1-git-clone/">git-clone</a></code>(1) or <code><a href="/docs/linux/man/1-git-init/">git-init</a></code>(1) will probe and set core.symlinks false if appropriate when the repository is created. </p>
 </dd></dl>
<p> core.gitProxy </p>
<dl>
<dd> <p> A &quot;proxy command&quot; to execute (as <i>command host port</i>) instead of establishing direct connection to the remote server when using the Git protocol for fetching. If the variable value is in the &quot;COMMAND for DOMAIN&quot; format, the command is applied only on hostnames ending with the specified domain string. This variable may be set multiple times and is matched in the given order; the first match wins. </p>
<p> Can be overridden by the <code>GIT_PROXY_COMMAND</code> environment variable (which always applies universally, without the special &quot;for&quot; handling). </p>
<p> The special string <code>none</code> can be used as the proxy command to specify that no proxy be used for a given domain pattern. This is useful for excluding servers inside a firewall from proxy use, while defaulting to a common proxy for external domains. </p>
 </dd></dl>
<p> core.sshCommand </p>
<dl>
<dd> <p> If this variable is set, <code>git fetch</code> and <code>git push</code> will use the specified command instead of <code>ssh</code> when they need to connect to a remote system. The command is in the same form as the <code>GIT_SSH_COMMAND</code> environment variable and is overridden when the environment variable is set. </p>
 </dd></dl>
<p> core.ignoreStat </p>
<dl>
<dd> <p> If true, Git will avoid using lstat() calls to detect if files have changed by setting the &quot;assume-unchanged&quot; bit for those tracked files which it has updated identically in both the index and working tree. </p>
<p> When files are modified outside of Git, the user will need to stage the modified files explicitly (e.g. see <i>Examples</i> section in <code><a href="/docs/linux/man/1-git-update-index/">git-update-index</a></code>(1)). Git will not normally detect changes to those files. </p>
<p> This is useful on systems where lstat() calls are very slow, such as CIFS/Microsoft Windows. </p>
<p> False by default. </p>
 </dd></dl>
<p> core.preferSymlinkRefs </p>
<dl>
<dd> <p> Instead of the default &quot;symref&quot; format for HEAD and other symbolic reference files, use symbolic links. This is sometimes needed to work with old scripts that expect HEAD to be a symbolic link. </p>
 </dd></dl>
<p> core.alternateRefsCommand </p>
<dl>
<dd> <p> When advertising tips of available history from an alternate, use the shell to execute the specified command instead of <code><a href="/docs/linux/man/1-git-for-each-ref/">git-for-each-ref</a></code>(1). The first argument is the absolute path of the alternate. Output must contain one hex object id per line (i.e., the same as produced by <code>git for-each-ref --format=&#8216;%(objectname)&#8216;</code>). </p>
<p> Note that you cannot generally put <code>git for-each-ref</code> directly into the config value, as it does not take a repository path as an argument (but you can wrap the command above in a shell script). </p>
 </dd></dl>
<p> core.alternateRefsPrefixes </p>
<dl>
<dd> <p> When listing references from an alternate, list only references that begin with the given prefix. Prefixes match as if they were given as arguments to <code><a href="/docs/linux/man/1-git-for-each-ref/">git-for-each-ref</a></code>(1). To list multiple prefixes, separate them with whitespace. If <code>core.alternateRefsCommand</code> is set, setting <code>core.alternateRefsPrefixes</code> has no effect. </p>
 </dd></dl>
<p> core.bare </p>
<dl>
<dd> <p> If true this repository is assumed to be <i>bare</i> and has no working directory associated with it. If this is the case a number of commands that require a working directory will be disabled, such as <code><a href="/docs/linux/man/1-git-add/">git-add</a></code>(1) or <code><a href="/docs/linux/man/1-git-merge/">git-merge</a></code>(1). </p>
<p> This setting is automatically guessed by <code><a href="/docs/linux/man/1-git-clone/">git-clone</a></code>(1) or <code><a href="/docs/linux/man/1-git-init/">git-init</a></code>(1) when the repository was created. By default a repository that ends in &quot;/.git&quot; is assumed to be not bare (bare = false), while all other repositories are assumed to be bare (bare = true). </p>
 </dd></dl>
<p> core.worktree </p>
<dl>
<dd> <p> Set the path to the root of the working tree. If <code>GIT_COMMON_DIR</code> environment variable is set, core.worktree is ignored and not used for determining the root of working tree. This can be overridden by the <code>GIT_WORK_TREE</code> environment variable and the <code>--work-tree</code> command-line option. The value can be an absolute path or relative to the path to the .git directory, which is either specified by --git-dir or GIT_DIR, or automatically discovered. If --git-dir or GIT_DIR is specified but none of --work-tree, GIT_WORK_TREE and core.worktree is specified, the current working directory is regarded as the top level of your working tree. </p>
<p> Note that this variable is honored even when set in a configuration file in a &quot;.git&quot; subdirectory of a directory and its value differs from the latter directory (e.g. &quot;/path/to/.git/config&quot; has core.worktree set to &quot;/different/path&quot;), which is most likely a misconfiguration. Running Git commands in the &quot;/path/to&quot; directory will still use &quot;/different/path&quot; as the root of the work tree and can cause confusion unless you know what you are doing (e.g. you are creating a read-only snapshot of the same index to a location different from the repository&#8217;s usual working tree). </p>
 </dd></dl>
<p> core.logAllRefUpdates </p>
<dl>
<dd> <p> Enable the reflog. Updates to a ref &lt;ref&gt; is logged to the file &quot;<code>$GIT_DIR/logs/&lt;ref&gt;</code>&quot;, by appending the new and old SHA-1, the date/time and the reason of the update, but only when the file exists. If this configuration variable is set to <code>true</code>, missing &quot;<code>$GIT_DIR/logs/&lt;ref&gt;</code>&quot; file is automatically created for branch heads (i.e. under <code>refs/heads/</code>), remote refs (i.e. under <code>refs/remotes/</code>), note refs (i.e. under <code>refs/notes/</code>), and the symbolic ref <code>HEAD</code>. If it is set to <code>always</code>, then a missing reflog is automatically created for any ref under <code>refs/</code>. </p>
<p> This information can be used to determine what commit was the tip of a branch &quot;2 days ago&quot;. </p>
<p> This value is true by default in a repository that has a working directory associated with it, and false by default in a bare repository. </p>
 </dd></dl>
<p> core.repositoryFormatVersion </p>
<dl>
<dd> <p> Internal variable identifying the repository format and layout version. </p>
 </dd></dl>
<p> core.sharedRepository </p>
<dl>
<dd> <p> When <i>group</i> (or <i>true</i>), the repository is made shareable between several users in a group (making sure all the files and objects are group-writable). When <i>all</i> (or <i>world</i> or <i>everybody</i>), the repository will be readable by all users, additionally to being group-shareable. When <i>umask</i> (or <i>false</i>), Git will use permissions reported by <a href="/docs/linux/man/2-umask/">umask</a>(2). When <i>0xxx</i>, where <i>0xxx</i> is an octal number, files in the repository will have this mode value. <i>0xxx</i> will override user&#8217;s umask value (whereas the other options will only override requested parts of the user&#8217;s umask value). Examples: <i>0660</i> will make the repo read/write-able for the owner and group, but inaccessible to others (equivalent to <i>group</i> unless umask is e.g. <i>0022</i>). <i>0640</i> is a repository that is group-readable but not group-writable. See <code><a href="/docs/linux/man/1-git-init/">git-init</a></code>(1). False by default. </p>
 </dd></dl>
<p> core.warnAmbiguousRefs </p>
<dl>
<dd> <p> If true, Git will warn you if the ref name you passed it is ambiguous and might match multiple refs in the repository. True by default. </p>
 </dd></dl>
<p> core.compression </p>
<dl>
<dd> <p> An integer -1..9, indicating a default compression level. -1 is the zlib default. 0 means no compression, and 1..9 are various speed/size tradeoffs, 9 being slowest. If set, this provides a default to other compression variables, such as <code>core.looseCompression</code> and <code>pack.compression</code>. </p>
 </dd></dl>
<p> core.looseCompression </p>
<dl>
<dd> <p> An integer -1..9, indicating the compression level for objects that are not in a pack file. -1 is the zlib default. 0 means no compression, and 1..9 are various speed/size tradeoffs, 9 being slowest. If not set, defaults to core.compression. If that is not set, defaults to 1 (best speed). </p>
 </dd></dl>
<p> core.packedGitWindowSize </p>
<dl>
<dd> <p> Number of bytes of a pack file to map into memory in a single mapping operation. Larger window sizes may allow your system to process a smaller number of large pack files more quickly. Smaller window sizes will negatively affect performance due to increased calls to the operating system&#8217;s memory manager, but may improve performance when accessing a large number of large pack files. </p>
<p> Default is 1 MiB if NO_MMAP was set at compile time, otherwise 32 MiB on 32 bit platforms and 1 GiB on 64 bit platforms. This should be reasonable for all users/operating systems. You probably do not need to adjust this value. </p>
<p> Common unit suffixes of <i>k</i>, <i>m</i>, or <i>g</i> are supported. </p>
 </dd></dl>
<p> core.packedGitLimit </p>
<dl>
<dd> <p> Maximum number of bytes to map simultaneously into memory from pack files. If Git needs to access more than this many bytes at once to complete an operation it will unmap existing regions to reclaim virtual address space within the process. </p>
<p> Default is 256 MiB on 32 bit platforms and 32 TiB (effectively unlimited) on 64 bit platforms. This should be reasonable for all users/operating systems, except on the largest projects. You probably do not need to adjust this value. </p>
<p> Common unit suffixes of <i>k</i>, <i>m</i>, or <i>g</i> are supported. </p>
 </dd></dl>
<p> core.deltaBaseCacheLimit </p>
<dl>
<dd> <p> Maximum number of bytes per thread to reserve for caching base objects that may be referenced by multiple deltified objects. By storing the entire decompressed base objects in a cache Git is able to avoid unpacking and decompressing frequently used base objects multiple times. </p>
<p> Default is 96 MiB on all platforms. This should be reasonable for all users/operating systems, except on the largest projects. You probably do not need to adjust this value. </p>
<p> Common unit suffixes of <i>k</i>, <i>m</i>, or <i>g</i> are supported. </p>
 </dd></dl>
<p> core.bigFileThreshold </p>
<dl>
<dd> <p> Files larger than this size are stored deflated, without attempting delta compression. Storing large files without delta compression avoids excessive memory usage, at the slight expense of increased disk usage. Additionally files larger than this size are always treated as binary. </p>
<p> Default is 512 MiB on all platforms. This should be reasonable for most projects as source code and other text files can still be delta compressed, but larger binary media files won&#8217;t be. </p>
<p> Common unit suffixes of <i>k</i>, <i>m</i>, or <i>g</i> are supported. </p>
 </dd></dl>
<p> core.excludesFile </p>
<dl>
<dd> <p> Specifies the pathname to the file that contains patterns to describe paths that are not meant to be tracked, in addition to <code>.gitignore</code> (per-directory) and <code>.git/info/exclude</code>. Defaults to <code>$XDG_CONFIG_HOME/git/ignore</code>. If <code>$XDG_CONFIG_HOME</code> is either not set or empty, <code>$HOME/.config/git/ignore</code> is used instead. See <code><a href="/docs/linux/man/5-gitignore/">gitignore</a></code>(5). </p>
 </dd></dl>
<p> core.askPass </p>
<dl>
<dd> <p> Some commands (e.g. svn and http interfaces) that interactively ask for a password can be told to use an external program given via the value of this variable. Can be overridden by the <code>GIT_ASKPASS</code> environment variable. If not set, fall back to the value of the <code>SSH_ASKPASS</code> environment variable or, failing that, a simple password prompt. The external program shall be given a suitable prompt as command-line argument and write the password on its STDOUT. </p>
 </dd></dl>
<p> core.attributesFile </p>
<dl>
<dd> <p> In addition to <code>.gitattributes</code> (per-directory) and <code>.git/info/attributes</code>, Git looks into this file for attributes (see <code><a href="/docs/linux/man/5-gitattributes/">gitattributes</a></code>(5)). Path expansions are made the same way as for <code>core.excludesFile</code>. Its default value is <code>$XDG_CONFIG_HOME/git/attributes</code>. If <code>$XDG_CONFIG_HOME</code> is either not set or empty, <code>$HOME/.config/git/attributes</code> is used instead. </p>
 </dd></dl>
<p> core.hooksPath </p>
<dl>
<dd> <p> By default Git will look for your hooks in the <code>$GIT_DIR/hooks</code> directory. Set this to different path, e.g. <code>/etc/git/hooks</code>, and Git will try to find your hooks in that directory, e.g. <code>/etc/git/hooks/pre-receive</code> instead of in <code>$GIT_DIR/hooks/pre-receive</code>. </p>
<p> The path can be either absolute or relative. A relative path is taken as relative to the directory where the hooks are run (see the &quot;DESCRIPTION&quot; section of <code><a href="/docs/linux/man/5-githooks/">githooks</a></code>(5)). </p>
<p> This configuration variable is useful in cases where you&#8217;d like to centrally configure your Git hooks instead of configuring them on a per-repository basis, or as a more flexible and centralized alternative to having an <code>init.templateDir</code> where you&#8217;ve changed default hooks. </p>
 </dd></dl>
<p> core.editor </p>
<dl>
<dd> <p> Commands such as <code>commit</code> and <code>tag</code> that let you edit messages by launching an editor use the value of this variable when it is set, and the environment variable <code>GIT_EDITOR</code> is not set. See <code><a href="/docs/linux/man/1-git-var/">git-var</a></code>(1). </p>
 </dd></dl>
<p> core.commentChar </p>
<dl>
<dd> <p> Commands such as <code>commit</code> and <code>tag</code> that let you edit messages consider a line that begins with this character commented, and removes them after the editor returns (default <i>#</i>). </p>
<p> If set to &quot;auto&quot;, <code>git-commit</code> would select a character that is not the beginning character of any line in existing commit messages. </p>
 </dd></dl>
<p> core.filesRefLockTimeout </p>
<dl>
<dd> <p> The length of time, in milliseconds, to retry when trying to lock an individual reference. Value 0 means not to retry at all; -1 means to try indefinitely. Default is 100 (i.e., retry for 100ms). </p>
 </dd></dl>
<p> core.packedRefsTimeout </p>
<dl>
<dd> <p> The length of time, in milliseconds, to retry when trying to lock the <code>packed-refs</code> file. Value 0 means not to retry at all; -1 means to try indefinitely. Default is 1000 (i.e., retry for 1 second). </p>
 </dd></dl>
<p> core.pager </p>
<dl>
<dd> <p> Text viewer for use by Git commands (e.g., <i>less</i>). The value is meant to be interpreted by the shell. The order of preference is the <code>$GIT_PAGER</code> environment variable, then <code>core.pager</code> configuration, then <code>$PAGER</code>, and then the default chosen at compile time (usually <i>less</i>). </p>
<p> When the <code>LESS</code> environment variable is unset, Git sets it to <code>FRX</code> (if <code>LESS</code> environment variable is set, Git does not change it at all). If you want to selectively override Git&#8217;s default setting for <code>LESS</code>, you can set <code>core.pager</code> to e.g. <code>less -S</code>. This will be passed to the shell by Git, which will translate the final command to <code>LESS=FRX less -S</code>. The environment does not set the <code>S</code> option but the command line does, instructing less to truncate long lines. Similarly, setting <code>core.pager</code> to <code>less -+F</code> will deactivate the <code>F</code> option specified by the environment from the command-line, deactivating the &quot;quit if one screen&quot; behavior of <code>less</code>. One can specifically activate some flags for particular commands: for example, setting <code>pager.blame</code> to <code>less -S</code> enables line truncation only for <code>git blame</code>. </p>
<p> Likewise, when the <code>LV</code> environment variable is unset, Git sets it to <code>-c</code>. You can override this setting by exporting <code>LV</code> with another value or setting <code>core.pager</code> to <code>lv +c</code>. </p>
 </dd></dl>
<p> core.whitespace </p>
<dl>
<dd> <p> A comma separated list of common whitespace problems to notice. <i>git diff</i> will use <code>color.diff.whitespace</code> to highlight them, and <i>git apply --whitespace=error</i> will consider them as errors. You can prefix <code>-</code> to disable any of them (e.g. <code>-trailing-space</code>): </p>
 </dd>
<dl>
<dd> <p> &bull; <code>blank-at-eol</code> treats trailing whitespaces at the end of the line as an error (enabled by default). </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>space-before-tab</code> treats a space character that appears immediately before a tab character in the initial indent part of the line as an error (enabled by default). </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>indent-with-non-tab</code> treats a line that is indented with space characters instead of the equivalent tabs as an error (not enabled by default). </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>tab-in-indent</code> treats a tab character in the initial indent part of the line as an error (not enabled by default). </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>blank-at-eof</code> treats blank lines added at the end of file as an error (enabled by default). </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>trailing-space</code> is a short-hand to cover both <code>blank-at-eol</code> and <code>blank-at-eof</code>. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>cr-at-eol</code> treats a carriage-return at the end of line as part of the line terminator, i.e. with it, <code>trailing-space</code> does not trigger if the character before such a carriage-return is not a whitespace (not enabled by default). </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>tabwidth=&lt;n&gt;</code> tells how many character positions a tab occupies; this is relevant for <code>indent-with-non-tab</code> and when Git fixes <code>tab-in-indent</code> errors. The default tab width is 8. Allowed values are 1 to 63. </p>
 </dd></dl>
</dl>
<p> core.fsyncObjectFiles </p>
<dl>
<dd> <p> This boolean will enable <i>fsync()</i> when writing object files. </p>
<p> This is a total waste of time and effort on a filesystem that orders data writes properly, but can be useful for filesystems that do not use journalling (traditional UNIX filesystems) or that only journal metadata and not file contents (OS X&#8217;s HFS+, or Linux ext3 with &quot;data=writeback&quot;). </p>
 </dd></dl>
<p> core.preloadIndex </p>
<dl>
<dd> <p> Enable parallel index preload for operations like <i>git diff</i> </p>
<p> This can speed up operations like <i>git diff</i> and <i>git status</i> especially on filesystems like NFS that have weak caching semantics and thus relatively high IO latencies. When enabled, Git will do the index comparison to the filesystem data in parallel, allowing overlapping IO&#8217;s. Defaults to true. </p>
 </dd></dl>
<p> core.unsetenvvars </p>
<dl>
<dd> <p> Windows-only: comma-separated list of environment variables&#8217; names that need to be unset before spawning any other process. Defaults to <code>PERL5LIB</code> to account for the fact that Git for Windows insists on using its own Perl interpreter. </p>
 </dd></dl>
<p> core.restrictinheritedhandles </p>
<dl>
<dd> <p> Windows-only: override whether spawned processes inherit only standard file handles (<code>stdin</code>, <code>stdout</code> and <code>stderr</code>) or all handles. Can be <code>auto</code>, <code>true</code> or <code>false</code>. Defaults to <code>auto</code>, which means <code>true</code> on Windows 7 and later, and <code>false</code> on older Windows versions. </p>
 </dd></dl>
<p> core.createObject </p>
<dl>
<dd> <p> You can set this to <i>link</i>, in which case a hardlink followed by a delete of the source are used to make sure that object creation will not overwrite existing objects. </p>
<p> On some file system/operating system combinations, this is unreliable. Set this config setting to <i>rename</i> there; However, This will remove the check that makes sure that existing object files will not get overwritten. </p>
 </dd></dl>
<p> core.notesRef </p>
<dl>
<dd> <p> When showing commit messages, also show notes which are stored in the given ref. The ref must be fully qualified. If the given ref does not exist, it is not an error but means that no notes should be printed. </p>
<p> This setting defaults to &quot;refs/notes/commits&quot;, and it can be overridden by the <code>GIT_NOTES_REF</code> environment variable. See <code><a href="/docs/linux/man/1-git-notes/">git-notes</a></code>(1). </p>
 </dd></dl>
<p> core.commitGraph </p>
<dl>
<dd> <p> If true, then git will read the commit-graph file (if it exists) to parse the graph structure of commits. Defaults to true. See <code><a href="/docs/linux/man/1-git-commit-graph/">git-commit-graph</a></code>(1) for more information. </p>
 </dd></dl>
<p> core.useReplaceRefs </p>
<dl>
<dd> <p> If set to <code>false</code>, behave as if the <code>--no-replace-objects</code> option was given on the command line. See <code><a href="/docs/linux/man/1-git/">git</a></code>(1) and <code><a href="/docs/linux/man/1-git-replace/">git-replace</a></code>(1) for more information. </p>
 </dd></dl>
<p> core.multiPackIndex </p>
<dl>
<dd> <p> Use the multi-pack-index file to track multiple packfiles using a single index. See <code><a href="/docs/linux/man/1-git-multi-pack-index/">git-multi-pack-index</a></code>(1) for more information. Defaults to true. </p>
 </dd></dl>
<p> core.sparseCheckout </p>
<dl>
<dd> <p> Enable &quot;sparse checkout&quot; feature. See <code><a href="/docs/linux/man/1-git-sparse-checkout/">git-sparse-checkout</a></code>(1) for more information. </p>
 </dd></dl>
<p> core.sparseCheckoutCone </p>
<dl>
<dd> <p> Enables the &quot;cone mode&quot; of the sparse checkout feature. When the sparse-checkout file contains a limited set of patterns, then this mode provides significant performance advantages. See <code><a href="/docs/linux/man/1-git-sparse-checkout/">git-sparse-checkout</a></code>(1) for more information. </p>
 </dd></dl>
<p> core.abbrev </p>
<dl>
<dd> <p> Set the length object names are abbreviated to. If unspecified or set to &quot;auto&quot;, an appropriate value is computed based on the approximate number of packed objects in your repository, which hopefully is enough for abbreviated object names to stay unique for some time. If set to &quot;no&quot;, no abbreviation is made and the object names are shown in their full length. The minimum length is 4. </p>
 </dd></dl>
<p> add.ignoreErrors, add.ignore-errors (deprecated) </p>
<dl>
<dd> <p> Tells <i>git add</i> to continue adding files when some files cannot be added due to indexing errors. Equivalent to the <code>--ignore-errors</code> option of <code><a href="/docs/linux/man/1-git-add/">git-add</a></code>(1). <code>add.ignore-errors</code> is deprecated, as it does not follow the usual naming convention for configuration variables. </p>
 </dd></dl>
<p> add.interactive.useBuiltin </p>
<dl>
<dd> <p> [EXPERIMENTAL] Set to <code>true</code> to use the experimental built-in implementation of the interactive version of <code><a href="/docs/linux/man/1-git-add/">git-add</a></code>(1) instead of the Perl script version. Is <code>false</code> by default. </p>
 </dd></dl>
<p> alias.* </p>
<dl>
<dd> <p> Command aliases for the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) command wrapper - e.g. after defining <code>alias.last = cat-file commit HEAD</code>, the invocation <code>git last</code> is equivalent to <code>git cat-file commit HEAD</code>. To avoid confusion and troubles with script usage, aliases that hide existing Git commands are ignored. Arguments are split by spaces, the usual shell quoting and escaping is supported. A quote pair or a backslash can be used to quote them. </p>
<p> Note that the first word of an alias does not necessarily have to be a command. It can be a command-line option that will be passed into the invocation of <code>git</code>. In particular, this is useful when used with <code>-c</code> to pass in one-time configurations or <code>-p</code> to force pagination. For example, <code>loud-rebase = -c commit.verbose=true rebase</code> can be defined such that running <code>git loud-rebase</code> would be equivalent to <code>git -c commit.verbose=true rebase</code>. Also, <code>ps = -p status</code> would be a helpful alias since <code>git ps</code> would paginate the output of <code>git status</code> where the original command does not. </p>
<p> If the alias expansion is prefixed with an exclamation point, it will be treated as a shell command. For example, defining <code>alias.new = !gitk --all --not ORIG_HEAD</code>, the invocation <code>git new</code> is equivalent to running the shell command <code>gitk --all --not ORIG_HEAD</code>. Note that shell commands will be executed from the top-level directory of a repository, which may not necessarily be the current directory. <code>GIT_PREFIX</code> is set as returned by running <code>git rev-parse --show-prefix</code> from the original current directory. See <code><a href="/docs/linux/man/1-git-rev-parse/">git-rev-parse</a></code>(1). </p>
 </dd></dl>
<p> am.keepcr </p>
<dl>
<dd> <p> If true, git-am will call git-mailsplit for patches in mbox format with parameter <code>--keep-cr</code>. In this case git-mailsplit will not remove <code>\r</code> from lines ending with <code>\r\n</code>. Can be overridden by giving <code>--no-keep-cr</code> from the command line. See <code><a href="/docs/linux/man/1-git-am/">git-am</a></code>(1), <code><a href="/docs/linux/man/1-git-mailsplit/">git-mailsplit</a></code>(1). </p>
 </dd></dl>
<p> am.threeWay </p>
<dl>
<dd> <p> By default, <code>git am</code> will fail if the patch does not apply cleanly. When set to true, this setting tells <code>git am</code> to fall back on 3-way merge if the patch records the identity of blobs it is supposed to apply to and we have those blobs available locally (equivalent to giving the <code>--3way</code> option from the command line). Defaults to <code>false</code>. See <code><a href="/docs/linux/man/1-git-am/">git-am</a></code>(1). </p>
 </dd></dl>
<p> apply.ignoreWhitespace </p>
<dl>
<dd> <p> When set to <i>change</i>, tells <i>git apply</i> to ignore changes in whitespace, in the same way as the <code>--ignore-space-change</code> option. When set to one of: no, none, never, false tells <i>git apply</i> to respect all whitespace differences. See <code><a href="/docs/linux/man/1-git-apply/">git-apply</a></code>(1). </p>
 </dd></dl>
<p> apply.whitespace </p>
<dl>
<dd> <p> Tells <i>git apply</i> how to handle whitespaces, in the same way as the <code>--whitespace</code> option. See <code><a href="/docs/linux/man/1-git-apply/">git-apply</a></code>(1). </p>
 </dd></dl>
<p> blame.blankBoundary </p>
<dl>
<dd> <p> Show blank commit object name for boundary commits in <code><a href="/docs/linux/man/1-git-blame/">git-blame</a></code>(1). This option defaults to false. </p>
 </dd></dl>
<p> blame.coloring </p>
<dl>
<dd> <p> This determines the coloring scheme to be applied to blame output. It can be <i>repeatedLines</i>, <i>highlightRecent</i>, or <i>none</i> which is the default. </p>
 </dd></dl>
<p> blame.date </p>
<dl>
<dd> <p> Specifies the format used to output dates in <code><a href="/docs/linux/man/1-git-blame/">git-blame</a></code>(1). If unset the iso format is used. For supported values, see the discussion of the <code>--date</code> option at <code><a href="/docs/linux/man/1-git-log/">git-log</a></code>(1). </p>
 </dd></dl>
<p> blame.showEmail </p>
<dl>
<dd> <p> Show the author email instead of author name in <code><a href="/docs/linux/man/1-git-blame/">git-blame</a></code>(1). This option defaults to false. </p>
 </dd></dl>
<p> blame.showRoot </p>
<dl>
<dd> <p> Do not treat root commits as boundaries in <code><a href="/docs/linux/man/1-git-blame/">git-blame</a></code>(1). This option defaults to false. </p>
 </dd></dl>
<p> blame.ignoreRevsFile </p>
<dl>
<dd> <p> Ignore revisions listed in the file, one unabbreviated object name per line, in <code><a href="/docs/linux/man/1-git-blame/">git-blame</a></code>(1). Whitespace and comments beginning with <code>#</code> are ignored. This option may be repeated multiple times. Empty file names will reset the list of ignored revisions. This option will be handled before the command line option <code>--ignore-revs-file</code>. </p>
 </dd></dl>
<p> blame.markUnblamableLines </p>
<dl>
<dd> <p> Mark lines that were changed by an ignored revision that we could not attribute to another commit with a <i>*</i> in the output of <code><a href="/docs/linux/man/1-git-blame/">git-blame</a></code>(1). </p>
 </dd></dl>
<p> blame.markIgnoredLines </p>
<dl>
<dd> <p> Mark lines that were changed by an ignored revision that we attributed to another commit with a <i>?</i> in the output of <code><a href="/docs/linux/man/1-git-blame/">git-blame</a></code>(1). </p>
 </dd></dl>
<p> branch.autoSetupMerge </p>
<dl>
<dd> <p> Tells <i>git branch</i>, <i>git switch</i> and <i>git checkout</i> to set up new branches so that <code><a href="/docs/linux/man/1-git-pull/">git-pull</a></code>(1) will appropriately merge from the starting point branch. Note that even if this option is not set, this behavior can be chosen per-branch using the <code>--track</code> and <code>--no-track</code> options. The valid settings are: <code>false</code> --- no automatic setup is done; <code>true</code> --- automatic setup is done when the starting point is a remote-tracking branch; <code>always</code> --- automatic setup is done when the starting point is either a local branch or remote-tracking branch. This option defaults to true. </p>
 </dd></dl>
<p> branch.autoSetupRebase </p>
<dl>
<dd> <p> When a new branch is created with <i>git branch</i>, <i>git switch</i> or <i>git checkout</i> that tracks another branch, this variable tells Git to set up pull to rebase instead of merge (see &quot;branch.&lt;name&gt;.rebase&quot;). When <code>never</code>, rebase is never automatically set to true. When <code>local</code>, rebase is set to true for tracked branches of other local branches. When <code>remote</code>, rebase is set to true for tracked branches of remote-tracking branches. When <code>always</code>, rebase will be set to true for all tracking branches. See &quot;branch.autoSetupMerge&quot; for details on how to set up a branch to track another branch. This option defaults to never. </p>
 </dd></dl>
<p> branch.sort </p>
<dl>
<dd> <p> This variable controls the sort ordering of branches when displayed by <code><a href="/docs/linux/man/1-git-branch/">git-branch</a></code>(1). Without the &quot;--sort=&lt;value&gt;&quot; option provided, the value of this variable will be used as the default. See <code><a href="/docs/linux/man/1-git-for-each-ref/">git-for-each-ref</a></code>(1) field names for valid values. </p>
 </dd></dl>
<p> branch.&lt;name&gt;.remote </p>
<dl>
<dd> <p> When on branch &lt;name&gt;, it tells <i>git fetch</i> and <i>git push</i> which remote to fetch from/push to. The remote to push to may be overridden with <code>remote.pushDefault</code> (for all branches). The remote to push to, for the current branch, may be further overridden by <code>branch.&lt;name&gt;.pushRemote</code>. If no remote is configured, or if you are not on any branch, it defaults to <code>origin</code> for fetching and <code>remote.pushDefault</code> for pushing. Additionally, <code>.</code> (a period) is the current local repository (a dot-repository), see <code>branch.&lt;name&gt;.merge</code>&#8216;s final note below. </p>
 </dd></dl>
<p> branch.&lt;name&gt;.pushRemote </p>
<dl>
<dd> <p> When on branch &lt;name&gt;, it overrides <code>branch.&lt;name&gt;.remote</code> for pushing. It also overrides <code>remote.pushDefault</code> for pushing from branch &lt;name&gt;. When you pull from one place (e.g. your upstream) and push to another place (e.g. your own publishing repository), you would want to set <code>remote.pushDefault</code> to specify the remote to push to for all branches, and use this option to override it for a specific branch. </p>
 </dd></dl>
<p> branch.&lt;name&gt;.merge </p>
<dl>
<dd> <p> Defines, together with branch.&lt;name&gt;.remote, the upstream branch for the given branch. It tells <i>git fetch</i>/<i>git pull</i>/<i>git rebase</i> which branch to merge and can also affect <i>git push</i> (see push.default). When in branch &lt;name&gt;, it tells <i>git fetch</i> the default refspec to be marked for merging in FETCH_HEAD. The value is handled like the remote part of a refspec, and must match a ref which is fetched from the remote given by &quot;branch.&lt;name&gt;.remote&quot;. The merge information is used by <i>git pull</i> (which at first calls <i>git fetch</i>) to lookup the default branch for merging. Without this option, <i>git pull</i> defaults to merge the first refspec fetched. Specify multiple values to get an octopus merge. If you wish to setup <i>git pull</i> so that it merges into &lt;name&gt; from another branch in the local repository, you can point branch.&lt;name&gt;.merge to the desired branch, and use the relative path setting <code>.</code> (a period) for branch.&lt;name&gt;.remote. </p>
 </dd></dl>
<p> branch.&lt;name&gt;.mergeOptions </p>
<dl>
<dd> <p> Sets default options for merging into branch &lt;name&gt;. The syntax and supported options are the same as those of <code><a href="/docs/linux/man/1-git-merge/">git-merge</a></code>(1), but option values containing whitespace characters are currently not supported. </p>
 </dd></dl>
<p> branch.&lt;name&gt;.rebase </p>
<dl>
<dd> <p> When true, rebase the branch &lt;name&gt; on top of the fetched branch, instead of merging the default branch from the default remote when &quot;git pull&quot; is run. See &quot;pull.rebase&quot; for doing this in a non branch-specific manner. </p>
<p> When <code>merges</code> (or just <i>m</i>), pass the <code>--rebase-merges</code> option to <i>git rebase</i> so that the local merge commits are included in the rebase (see <code><a href="/docs/linux/man/1-git-rebase/">git-rebase</a></code>(1) for details). </p>
<p> When the value is <code>interactive</code> (or just <i>i</i>), the rebase is run in interactive mode. </p>
<p> <code>NOTE</code>: this is a possibly dangerous operation; do <code>not</code> use it unless you understand the implications (see <code><a href="/docs/linux/man/1-git-rebase/">git-rebase</a></code>(1) for details). </p>
 </dd></dl>
<p> branch.&lt;name&gt;.description </p>
<dl>
<dd> <p> Branch description, can be edited with <code>git branch --edit-description</code>. Branch description is automatically added in the format-patch cover letter or request-pull summary. </p>
 </dd></dl>
<p> browser.&lt;tool&gt;.cmd </p>
<dl>
<dd> <p> Specify the command to invoke the specified browser. The specified command is evaluated in shell with the URLs passed as arguments. (See <code>git-web--browse</code>(1).) </p>
 </dd></dl>
<p> browser.&lt;tool&gt;.path </p>
<dl>
<dd> <p> Override the path for the given tool that may be used to browse HTML help (see <code>-w</code> option in <code><a href="/docs/linux/man/1-git-help/">git-help</a></code>(1)) or a working repository in gitweb (see <code><a href="/docs/linux/man/1-git-instaweb/">git-instaweb</a></code>(1)). </p>
 </dd></dl>
<p> checkout.defaultRemote </p>
<dl>
<dd> <p> When you run <code>git checkout &lt;something&gt;</code> or <code>git switch &lt;something&gt;</code> and only have one remote, it may implicitly fall back on checking out and tracking e.g. <code>origin/&lt;something&gt;</code>. This stops working as soon as you have more than one remote with a <code>&lt;something&gt;</code> reference. This setting allows for setting the name of a preferred remote that should always win when it comes to disambiguation. The typical use-case is to set this to <code>origin</code>. </p>
<p> Currently this is used by <code><a href="/docs/linux/man/1-git-switch/">git-switch</a></code>(1) and <code><a href="/docs/linux/man/1-git-checkout/">git-checkout</a></code>(1) when <code>git checkout &lt;something&gt;</code> or <code>git switch &lt;something&gt;</code> will checkout the <code>&lt;something&gt;</code> branch on another remote, and by <code><a href="/docs/linux/man/1-git-worktree/">git-worktree</a></code>(1) when <code>git worktree add</code> refers to a remote branch. This setting might be used for other checkout-like commands or functionality in the future. </p>
 </dd></dl>
<p> checkout.guess </p>
<dl>
<dd> <p> Provides the default value for the <code>--guess</code> or <code>--no-guess</code> option in <code>git checkout</code> and <code>git switch</code>. See <code><a href="/docs/linux/man/1-git-switch/">git-switch</a></code>(1) and <code><a href="/docs/linux/man/1-git-checkout/">git-checkout</a></code>(1). </p>
 </dd></dl>
<p> checkout.workers </p>
<dl>
<dd> <p> The number of parallel workers to use when updating the working tree. The default is one, i.e. sequential execution. If set to a value less than one, Git will use as many workers as the number of logical cores available. This setting and <code>checkout.thresholdForParallelism</code> affect all commands that perform checkout. E.g. checkout, clone, reset, sparse-checkout, etc. </p>
<p> Note: parallel checkout usually delivers better performance for repositories located on SSDs or over NFS. For repositories on spinning disks and/or machines with a small number of cores, the default sequential checkout often performs better. The size and compression level of a repository might also influence how well the parallel version performs. </p>
 </dd></dl>
<p> checkout.thresholdForParallelism </p>
<dl>
<dd> <p> When running parallel checkout with a small number of files, the cost of subprocess spawning and inter-process communication might outweigh the parallelization gains. This setting allows to define the minimum number of files for which parallel checkout should be attempted. The default is 100. </p>
 </dd></dl>
<p> clean.requireForce </p>
<dl>
<dd> <p> A boolean to make git-clean do nothing unless given -f, -i or -n. Defaults to true. </p>
 </dd></dl>
<p> clone.defaultRemoteName </p>
<dl>
<dd> <p> The name of the remote to create when cloning a repository. Defaults to <code>origin</code>, and can be overridden by passing the <code>--origin</code> command-line option to <code><a href="/docs/linux/man/1-git-clone/">git-clone</a></code>(1). </p>
 </dd></dl>
<p> clone.rejectShallow </p>
<dl>
<dd> <p> Reject to clone a repository if it is a shallow one, can be overridden by passing option <code>--reject-shallow</code> in command line. See <code><a href="/docs/linux/man/1-git-clone/">git-clone</a></code>(1) </p>
 </dd></dl>
<p> color.advice </p>
<dl>
<dd> <p> A boolean to enable/disable color in hints (e.g. when a push failed, see <code>advice.*</code> for a list). May be set to <code>always</code>, <code>false</code> (or <code>never</code>) or <code>auto</code> (or <code>true</code>), in which case colors are used only when the error output goes to a terminal. If unset, then the value of <code>color.ui</code> is used (<code>auto</code> by default). </p>
 </dd></dl>
<p> color.advice.hint </p>
<dl>
<dd> <p> Use customized color for hints. </p>
 </dd></dl>
<p> color.blame.highlightRecent </p>
<dl>
<dd> <p> Specify the line annotation color for <code>git blame --color-by-age</code> depending upon the age of the line. </p>
<p> This setting should be set to a comma-separated list of color and date settings, starting and ending with a color, the dates should be set from oldest to newest. The metadata will be colored with the specified colors if the line was introduced before the given timestamp, overwriting older timestamped colors. </p>
<p> Instead of an absolute timestamp relative timestamps work as well, e.g. <code>2.weeks.ago</code> is valid to address anything older than 2 weeks. </p>
<p> It defaults to <code>blue,12 month ago,white,1 month ago,red</code>, which colors everything older than one year blue, recent changes between one month and one year old are kept white, and lines introduced within the last month are colored red. </p>
 </dd></dl>
<p> color.blame.repeatedLines </p>
<dl>
<dd> <p> Use the specified color to colorize line annotations for <code>git blame --color-lines</code>, if they come from the same commit as the preceding line. Defaults to cyan. </p>
 </dd></dl>
<p> color.branch </p>
<dl>
<dd> <p> A boolean to enable/disable color in the output of <code><a href="/docs/linux/man/1-git-branch/">git-branch</a></code>(1). May be set to <code>always</code>, <code>false</code> (or <code>never</code>) or <code>auto</code> (or <code>true</code>), in which case colors are used only when the output is to a terminal. If unset, then the value of <code>color.ui</code> is used (<code>auto</code> by default). </p>
 </dd></dl>
<p> color.branch.&lt;slot&gt; </p>
<dl>
<dd> <p> Use customized color for branch coloration. <code>&lt;slot&gt;</code> is one of <code>current</code> (the current branch), <code>local</code> (a local branch), <code>remote</code> (a remote-tracking branch in refs/remotes/), <code>upstream</code> (upstream tracking branch), <code>plain</code> (other refs). </p>
 </dd></dl>
<p> color.diff </p>
<dl>
<dd> <p> Whether to use ANSI escape sequences to add color to patches. If this is set to <code>always</code>, <code><a href="/docs/linux/man/1-git-diff/">git-diff</a></code>(1), <code><a href="/docs/linux/man/1-git-log/">git-log</a></code>(1), and <code><a href="/docs/linux/man/1-git-show/">git-show</a></code>(1) will use color for all patches. If it is set to <code>true</code> or <code>auto</code>, those commands will only use color when output is to the terminal. If unset, then the value of <code>color.ui</code> is used (<code>auto</code> by default). </p>
<p> This does not affect <code><a href="/docs/linux/man/1-git-format-patch/">git-format-patch</a></code>(1) or the <i>git-diff-*</i> plumbing commands. Can be overridden on the command line with the <code>--color[=&lt;when&gt;]</code> option. </p>
 </dd></dl>
<p> color.diff.&lt;slot&gt; </p>
<dl>
<dd> <p> Use customized color for diff colorization. <code>&lt;slot&gt;</code> specifies which part of the patch to use the specified color, and is one of <code>context</code> (context text - <code>plain</code> is a historical synonym), <code>meta</code> (metainformation), <code>frag</code> (hunk header), <i>func</i> (function in hunk header), <code>old</code> (removed lines), <code>new</code> (added lines), <code>commit</code> (commit headers), <code>whitespace</code> (highlighting whitespace errors), <code>oldMoved</code> (deleted lines), <code>newMoved</code> (added lines), <code>oldMovedDimmed</code>, <code>oldMovedAlternative</code>, <code>oldMovedAlternativeDimmed</code>, <code>newMovedDimmed</code>, <code>newMovedAlternative</code> <code>newMovedAlternativeDimmed</code> (See the <i>&lt;mode&gt;</i> setting of <i>--color-moved</i> in <code><a href="/docs/linux/man/1-git-diff/">git-diff</a></code>(1) for details), <code>contextDimmed</code>, <code>oldDimmed</code>, <code>newDimmed</code>, <code>contextBold</code>, <code>oldBold</code>, and <code>newBold</code> (see <code><a href="/docs/linux/man/1-git-range-diff/">git-range-diff</a></code>(1) for details). </p>
 </dd></dl>
<p> color.decorate.&lt;slot&gt; </p>
<dl>
<dd> <p> Use customized color for <i>git log --decorate</i> output. <code>&lt;slot&gt;</code> is one of <code>branch</code>, <code>remoteBranch</code>, <code>tag</code>, <code>stash</code> or <code>HEAD</code> for local branches, remote-tracking branches, tags, stash and HEAD, respectively and <code>grafted</code> for grafted commits. </p>
 </dd></dl>
<p> color.grep </p>
<dl>
<dd> <p> When set to <code>always</code>, always highlight matches. When <code>false</code> (or <code>never</code>), never. When set to <code>true</code> or <code>auto</code>, use color only when the output is written to the terminal. If unset, then the value of <code>color.ui</code> is used (<code>auto</code> by default). </p>
 </dd></dl>
<p> color.grep.&lt;slot&gt; </p>
<dl>
<dd> <p> Use customized color for grep colorization. <code>&lt;slot&gt;</code> specifies which part of the line to use the specified color, and is one of </p>
<p> <code>context</code> </p>
 </dd>
<dl>
<dd> <p> non-matching text in context lines (when using <code>-A</code>, <code>-B</code>, or <code>-C</code>) </p>
 </dd></dl>
<p> <code>filename</code> </p>
<dl>
<dd> <p> filename prefix (when not using <code>-h</code>) </p>
 </dd></dl>
<p> <code>function</code> </p>
<dl>
<dd> <p> function name lines (when using <code>-p</code>) </p>
 </dd></dl>
<p> <code>lineNumber</code> </p>
<dl>
<dd> <p> line number prefix (when using <code>-n</code>) </p>
 </dd></dl>
<p> <code>column</code> </p>
<dl>
<dd> <p> column number prefix (when using <code>--column</code>) </p>
 </dd></dl>
<p> <code>match</code> </p>
<dl>
<dd> <p> matching text (same as setting <code>matchContext</code> and <code>matchSelected</code>) </p>
 </dd></dl>
<p> <code>matchContext</code> </p>
<dl>
<dd> <p> matching text in context lines </p>
 </dd></dl>
<p> <code>matchSelected</code> </p>
<dl>
<dd> <p> matching text in selected lines. Also, used to customize the following <code><a href="/docs/linux/man/1-git-log/">git-log</a></code>(1) subcommands: <code>--grep</code>, <code>--author</code> and <code>--committer</code>. </p>
 </dd></dl>
<p> <code>selected</code> </p>
<dl>
<dd> <p> non-matching text in selected lines. Also, used to customize the following <code><a href="/docs/linux/man/1-git-log/">git-log</a></code>(1) subcommands: <code>--grep</code>, <code>--author</code> and <code>--committer</code>. </p>
 </dd></dl>
<p> <code>separator</code> </p>
<dl>
<dd> <p> separators between fields on a line (<code>:</code>, <code>-</code>, and <code>=</code>) and between hunks (<code>--</code>) </p>
 </dd></dl>
</dl>
<p> color.interactive </p>
<dl>
<dd> <p> When set to <code>always</code>, always use colors for interactive prompts and displays (such as those used by &quot;git-add --interactive&quot; and &quot;git-clean --interactive&quot;). When false (or <code>never</code>), never. When set to <code>true</code> or <code>auto</code>, use colors only when the output is to the terminal. If unset, then the value of <code>color.ui</code> is used (<code>auto</code> by default). </p>
 </dd></dl>
<p> color.interactive.&lt;slot&gt; </p>
<dl>
<dd> <p> Use customized color for <i>git add --interactive</i> and <i>git clean --interactive</i> output. <code>&lt;slot&gt;</code> may be <code>prompt</code>, <code>header</code>, <code>help</code> or <code>error</code>, for four distinct types of normal output from interactive commands. </p>
 </dd></dl>
<p> color.pager </p>
<dl>
<dd> <p> A boolean to specify whether <code>auto</code> color modes should colorize output going to the pager. Defaults to true; set this to false if your pager does not understand ANSI color codes. </p>
 </dd></dl>
<p> color.push </p>
<dl>
<dd> <p> A boolean to enable/disable color in push errors. May be set to <code>always</code>, <code>false</code> (or <code>never</code>) or <code>auto</code> (or <code>true</code>), in which case colors are used only when the error output goes to a terminal. If unset, then the value of <code>color.ui</code> is used (<code>auto</code> by default). </p>
 </dd></dl>
<p> color.push.error </p>
<dl>
<dd> <p> Use customized color for push errors. </p>
 </dd></dl>
<p> color.remote </p>
<dl>
<dd> <p> If set, keywords at the start of the line are highlighted. The keywords are &quot;error&quot;, &quot;warning&quot;, &quot;hint&quot; and &quot;success&quot;, and are matched case-insensitively. May be set to <code>always</code>, <code>false</code> (or <code>never</code>) or <code>auto</code> (or <code>true</code>). If unset, then the value of <code>color.ui</code> is used (<code>auto</code> by default). </p>
 </dd></dl>
<p> color.remote.&lt;slot&gt; </p>
<dl>
<dd> <p> Use customized color for each remote keyword. <code>&lt;slot&gt;</code> may be <code>hint</code>, <code>warning</code>, <code>success</code> or <code>error</code> which match the corresponding keyword. </p>
 </dd></dl>
<p> color.showBranch </p>
<dl>
<dd> <p> A boolean to enable/disable color in the output of <code><a href="/docs/linux/man/1-git-show-branch/">git-show-branch</a></code>(1). May be set to <code>always</code>, <code>false</code> (or <code>never</code>) or <code>auto</code> (or <code>true</code>), in which case colors are used only when the output is to a terminal. If unset, then the value of <code>color.ui</code> is used (<code>auto</code> by default). </p>
 </dd></dl>
<p> color.status </p>
<dl>
<dd> <p> A boolean to enable/disable color in the output of <code><a href="/docs/linux/man/1-git-status/">git-status</a></code>(1). May be set to <code>always</code>, <code>false</code> (or <code>never</code>) or <code>auto</code> (or <code>true</code>), in which case colors are used only when the output is to a terminal. If unset, then the value of <code>color.ui</code> is used (<code>auto</code> by default). </p>
 </dd></dl>
<p> color.status.&lt;slot&gt; </p>
<dl>
<dd> <p> Use customized color for status colorization. <code>&lt;slot&gt;</code> is one of <code>header</code> (the header text of the status message), <code>added</code> or <code>updated</code> (files which are added but not committed), <code>changed</code> (files which are changed but not added in the index), <code>untracked</code> (files which are not tracked by Git), <code>branch</code> (the current branch), <code>nobranch</code> (the color the <i>no branch</i> warning is shown in, defaulting to red), <code>localBranch</code> or <code>remoteBranch</code> (the local and remote branch names, respectively, when branch and tracking information is displayed in the status short-format), or <code>unmerged</code> (files which have unmerged changes). </p>
 </dd></dl>
<p> color.transport </p>
<dl>
<dd> <p> A boolean to enable/disable color when pushes are rejected. May be set to <code>always</code>, <code>false</code> (or <code>never</code>) or <code>auto</code> (or <code>true</code>), in which case colors are used only when the error output goes to a terminal. If unset, then the value of <code>color.ui</code> is used (<code>auto</code> by default). </p>
 </dd></dl>
<p> color.transport.rejected </p>
<dl>
<dd> <p> Use customized color when a push was rejected. </p>
 </dd></dl>
<p> color.ui </p>
<dl>
<dd> <p> This variable determines the default value for variables such as <code>color.diff</code> and <code>color.grep</code> that control the use of color per command family. Its scope will expand as more commands learn configuration to set a default for the <code>--color</code> option. Set it to <code>false</code> or <code>never</code> if you prefer Git commands not to use color unless enabled explicitly with some other configuration or the <code>--color</code> option. Set it to <code>always</code> if you want all output not intended for machine consumption to use color, to <code>true</code> or <code>auto</code> (this is the default since Git 1.8.4) if you want such output to use color when written to the terminal. </p>
 </dd></dl>
<p> column.ui </p>
<dl>
<dd> <p> Specify whether supported commands should output in columns. This variable consists of a list of tokens separated by spaces or commas: </p>
<p> These options control when the feature should be enabled (defaults to <i>never</i>): </p>
<p> <code>always</code> </p>
 </dd>
<dl>
<dd> <p> always show in columns </p>
 </dd></dl>
<p> <code>never</code> </p>
<dl>
<dd> <p> never show in columns </p>
 </dd></dl>
<p> <code>auto</code> </p>
<dl>
<dd> <p> show in columns if the output is to the terminal </p>
 </dd></dl>
<p> These options control layout (defaults to <i>column</i>). Setting any of these implies <i>always</i> if none of <i>always</i>, <i>never</i>, or <i>auto</i> are specified. </p>
<p> <code>column</code> </p>
<dl>
<dd> <p> fill columns before rows </p>
 </dd></dl>
<p> <code>row</code> </p>
<dl>
<dd> <p> fill rows before columns </p>
 </dd></dl>
<p> <code>plain</code> </p>
<dl>
<dd> <p> show in one column </p>
 </dd></dl>
<p> Finally, these options can be combined with a layout option (defaults to <i>nodense</i>): </p>
<p> <code>dense</code> </p>
<dl>
<dd> <p> make unequal size columns to utilize more space </p>
 </dd></dl>
<p> <code>nodense</code> </p>
<dl>
<dd> <p> make equal size columns </p>
 </dd></dl>
</dl>
<p> column.branch </p>
<dl>
<dd> <p> Specify whether to output branch listing in <code>git branch</code> in columns. See <code>column.ui</code> for details. </p>
 </dd></dl>
<p> column.clean </p>
<dl>
<dd> <p> Specify the layout when list items in <code>git clean -i</code>, which always shows files and directories in columns. See <code>column.ui</code> for details. </p>
 </dd></dl>
<p> column.status </p>
<dl>
<dd> <p> Specify whether to output untracked files in <code>git status</code> in columns. See <code>column.ui</code> for details. </p>
 </dd></dl>
<p> column.tag </p>
<dl>
<dd> <p> Specify whether to output tag listing in <code>git tag</code> in columns. See <code>column.ui</code> for details. </p>
 </dd></dl>
<p> commit.cleanup </p>
<dl>
<dd> <p> This setting overrides the default of the <code>--cleanup</code> option in <code>git commit</code>. See <code><a href="/docs/linux/man/1-git-commit/">git-commit</a></code>(1) for details. Changing the default can be useful when you always want to keep lines that begin with comment character <code>#</code> in your log message, in which case you would do <code>git config commit.cleanup whitespace</code> (note that you will have to remove the help lines that begin with <code>#</code> in the commit log template yourself, if you do this). </p>
 </dd></dl>
<p> commit.gpgSign </p>
<dl>
<dd> <p> A boolean to specify whether all commits should be GPG signed. Use of this option when doing operations such as rebase can result in a large number of commits being signed. It may be convenient to use an agent to avoid typing your GPG passphrase several times. </p>
 </dd></dl>
<p> commit.status </p>
<dl>
<dd> <p> A boolean to enable/disable inclusion of status information in the commit message template when using an editor to prepare the commit message. Defaults to true. </p>
 </dd></dl>
<p> commit.template </p>
<dl>
<dd> <p> Specify the pathname of a file to use as the template for new commit messages. </p>
 </dd></dl>
<p> commit.verbose </p>
<dl>
<dd> <p> A boolean or int to specify the level of verbose with <code>git commit</code>. See <code><a href="/docs/linux/man/1-git-commit/">git-commit</a></code>(1). </p>
 </dd></dl>
<p> commitGraph.generationVersion </p>
<dl>
<dd> <p> Specifies the type of generation number version to use when writing or reading the commit-graph file. If version 1 is specified, then the corrected commit dates will not be written or read. Defaults to 2. </p>
 </dd></dl>
<p> commitGraph.maxNewFilters </p>
<dl>
<dd> <p> Specifies the default value for the <code>--max-new-filters</code> option of <code>git commit-graph write</code> (c.f., <code><a href="/docs/linux/man/1-git-commit-graph/">git-commit-graph</a></code>(1)). </p>
 </dd></dl>
<p> commitGraph.readChangedPaths </p>
<dl>
<dd> <p> If true, then git will use the changed-path Bloom filters in the commit-graph file (if it exists, and they are present). Defaults to true. See <code><a href="/docs/linux/man/1-git-commit-graph/">git-commit-graph</a></code>(1) for more information. </p>
 </dd></dl>
<p> credential.helper </p>
<dl>
<dd> <p> Specify an external helper to be called when a username or password credential is needed; the helper may consult external storage to avoid prompting the user for the credentials. This is normally the name of a credential helper with possible arguments, but may also be an absolute path with arguments or, if preceded by <code>!</code>, shell commands. </p>
<p> Note that multiple helpers may be defined. See <code><a href="/docs/linux/man/7-gitcredentials/">gitcredentials</a></code>(7) for details and examples. </p>
 </dd></dl>
<p> credential.useHttpPath </p>
<dl>
<dd> <p> When acquiring credentials, consider the &quot;path&quot; component of an http or https URL to be important. Defaults to false. See <code><a href="/docs/linux/man/7-gitcredentials/">gitcredentials</a></code>(7) for more information. </p>
 </dd></dl>
<p> credential.username </p>
<dl>
<dd> <p> If no username is set for a network authentication, use this username by default. See credential.&lt;context&gt;.* below, and <code><a href="/docs/linux/man/7-gitcredentials/">gitcredentials</a></code>(7). </p>
 </dd></dl>
<p> credential.&lt;url&gt;.* </p>
<dl>
<dd> <p> Any of the credential.* options above can be applied selectively to some credentials. For example &quot;credential.<a rel="nofollow" href="https://example.com.username">https://example.com.username</a>&quot; would set the default username only for https connections to example.com. See <code><a href="/docs/linux/man/7-gitcredentials/">gitcredentials</a></code>(7) for details on how URLs are matched. </p>
 </dd></dl>
<p> credentialCache.ignoreSIGHUP </p>
<dl>
<dd> <p> Tell git-credential-cache---daemon to ignore SIGHUP, instead of quitting. </p>
 </dd></dl>
<p> credentialStore.lockTimeoutMS </p>
<dl>
<dd> <p> The length of time, in milliseconds, for git-credential-store to retry when trying to lock the credentials file. Value 0 means not to retry at all; -1 means to try indefinitely. Default is 1000 (i.e., retry for 1s). </p>
 </dd></dl>
<p> completion.commands </p>
<dl>
<dd> <p> This is only used by git-completion.bash to add or remove commands from the list of completed commands. Normally only porcelain commands and a few select others are completed. You can add more commands, separated by space, in this variable. Prefixing the command with <i>-</i> will remove it from the existing list. </p>
 </dd></dl>
<p> diff.autoRefreshIndex </p>
<dl>
<dd> <p> When using <i>git diff</i> to compare with work tree files, do not consider stat-only change as changed. Instead, silently run <code>git update-index --refresh</code> to update the cached stat information for paths whose contents in the work tree match the contents in the index. This option defaults to true. Note that this affects only <i>git diff</i> Porcelain, and not lower level <i>diff</i> commands such as <i>git diff-files</i>. </p>
 </dd></dl>
<p> diff.dirstat </p>
<dl>
<dd> <p> A comma separated list of <code>--dirstat</code> parameters specifying the default behavior of the <code>--dirstat</code> option to <code><a href="/docs/linux/man/1-git-diff/">git-diff</a></code>(1) and friends. The defaults can be overridden on the command line (using <code>--dirstat=&lt;param1,param2,...&gt;</code>). The fallback defaults (when not changed by <code>diff.dirstat</code>) are <code>changes,noncumulative,3</code>. The following parameters are available: </p>
<p> <code>changes</code> </p>
 </dd>
<dl>
<dd> <p> Compute the dirstat numbers by counting the lines that have been removed from the source, or added to the destination. This ignores the amount of pure code movements within a file. In other words, rearranging lines in a file is not counted as much as other changes. This is the default behavior when no parameter is given. </p>
 </dd></dl>
<p> <code>lines</code> </p>
<dl>
<dd> <p> Compute the dirstat numbers by doing the regular line-based diff analysis, and summing the removed/added line counts. (For binary files, count 64-byte chunks instead, since binary files have no natural concept of lines). This is a more expensive <code>--dirstat</code> behavior than the <code>changes</code> behavior, but it does count rearranged lines within a file as much as other changes. The resulting output is consistent with what you get from the other <code>--*stat</code> options. </p>
 </dd></dl>
<p> <code>files</code> </p>
<dl>
<dd> <p> Compute the dirstat numbers by counting the number of files changed. Each changed file counts equally in the dirstat analysis. This is the computationally cheapest <code>--dirstat</code> behavior, since it does not have to look at the file contents at all. </p>
 </dd></dl>
<p> <code>cumulative</code> </p>
<dl>
<dd> <p> Count changes in a child directory for the parent directory as well. Note that when using <code>cumulative</code>, the sum of the percentages reported may exceed 100%. The default (non-cumulative) behavior can be specified with the <code>noncumulative</code> parameter. </p>
 </dd></dl>
<p> &lt;limit&gt; </p>
<dl>
<dd> <p> An integer parameter specifies a cut-off percent (3% by default). Directories contributing less than this percentage of the changes are not shown in the output. </p>
 </dd></dl>
<p> Example: The following will count changed files, while ignoring directories with less than 10% of the total amount of changed files, and accumulating child directory counts in the parent directories: <code>files,10,cumulative</code>. </dl>
 </p>
<p> diff.statGraphWidth </p>
<dl>
<dd> <p> Limit the width of the graph part in --stat output. If set, applies to all commands generating --stat output except format-patch. </p>
 </dd></dl>
<p> diff.context </p>
<dl>
<dd> <p> Generate diffs with &lt;n&gt; lines of context instead of the default of 3. This value is overridden by the -U option. </p>
 </dd></dl>
<p> diff.interHunkContext </p>
<dl>
<dd> <p> Show the context between diff hunks, up to the specified number of lines, thereby fusing the hunks that are close to each other. This value serves as the default for the <code>--inter-hunk-context</code> command line option. </p>
 </dd></dl>
<p> diff.external </p>
<dl>
<dd> <p> If this config variable is set, diff generation is not performed using the internal diff machinery, but using the given command. Can be overridden with the &#8216;GIT_EXTERNAL_DIFF&#8217; environment variable. The command is called with parameters as described under &quot;git Diffs&quot; in <code><a href="/docs/linux/man/1-git/">git</a></code>(1). Note: if you want to use an external diff program only on a subset of your files, you might want to use <code><a href="/docs/linux/man/5-gitattributes/">gitattributes</a></code>(5) instead. </p>
 </dd></dl>
<p> diff.ignoreSubmodules </p>
<dl>
<dd> <p> Sets the default value of --ignore-submodules. Note that this affects only <i>git diff</i> Porcelain, and not lower level <i>diff</i> commands such as <i>git diff-files</i>. <i>git checkout</i> and <i>git switch</i> also honor this setting when reporting uncommitted changes. Setting it to <i>all</i> disables the submodule summary normally shown by <i>git commit</i> and <i>git status</i> when <code>status.submoduleSummary</code> is set unless it is overridden by using the --ignore-submodules command-line option. The <i>git submodule</i> commands are not affected by this setting. By default this is set to untracked so that any untracked submodules are ignored. </p>
 </dd></dl>
<p> diff.mnemonicPrefix </p>
<dl>
<dd> <p> If set, <i>git diff</i> uses a prefix pair that is different from the standard &quot;a/&quot; and &quot;b/&quot; depending on what is being compared. When this configuration is in effect, reverse diff output also swaps the order of the prefixes: </p>
<p> <code>git diff</code> </p>
 </dd>
<dl>
<dd> <p> compares the (i)ndex and the (w)ork tree; </p>
 </dd></dl>
<p> <code>git diff HEAD</code> </p>
<dl>
<dd> <p> compares a (c)ommit and the (w)ork tree; </p>
 </dd></dl>
<p> <code>git diff --cached</code> </p>
<dl>
<dd> <p> compares a (c)ommit and the (i)ndex; </p>
 </dd></dl>
<p> <code>git diff HEAD:file1 file2</code> </p>
<dl>
<dd> <p> compares an (o)bject and a (w)ork tree entity; </p>
 </dd></dl>
<p> <code>git diff --no-index a b</code> </p>
<dl>
<dd> <p> compares two non-git things (1) and (2). </p>
 </dd></dl>
</dl>
<p> diff.noprefix </p>
<dl>
<dd> <p> If set, <i>git diff</i> does not show any source or destination prefix. </p>
 </dd></dl>
<p> diff.relative </p>
<dl>
<dd> <p> If set to <i>true</i>, <i>git diff</i> does not show changes outside of the directory and show pathnames relative to the current directory. </p>
 </dd></dl>
<p> diff.orderFile </p>
<dl>
<dd> <p> File indicating how to order files within a diff. See the <i>-O</i> option to <code><a href="/docs/linux/man/1-git-diff/">git-diff</a></code>(1) for details. If <code>diff.orderFile</code> is a relative pathname, it is treated as relative to the top of the working tree. </p>
 </dd></dl>
<p> diff.renameLimit </p>
<dl>
<dd> <p> The number of files to consider in the exhaustive portion of copy/rename detection; equivalent to the <i>git diff</i> option <code>-l</code>. If not set, the default value is currently 1000. This setting has no effect if rename detection is turned off. </p>
 </dd></dl>
<p> diff.renames </p>
<dl>
<dd> <p> Whether and how Git detects renames. If set to &quot;false&quot;, rename detection is disabled. If set to &quot;true&quot;, basic rename detection is enabled. If set to &quot;copies&quot; or &quot;copy&quot;, Git will detect copies, as well. Defaults to true. Note that this affects only <i>git diff</i> Porcelain like <code><a href="/docs/linux/man/1-git-diff/">git-diff</a></code>(1) and <code><a href="/docs/linux/man/1-git-log/">git-log</a></code>(1), and not lower level commands such as <code><a href="/docs/linux/man/1-git-diff-files/">git-diff-files</a></code>(1). </p>
 </dd></dl>
<p> diff.suppressBlankEmpty </p>
<dl>
<dd> <p> A boolean to inhibit the standard behavior of printing a space before each empty output line. Defaults to false. </p>
 </dd></dl>
<p> diff.submodule </p>
<dl>
<dd> <p> Specify the format in which differences in submodules are shown. The &quot;short&quot; format just shows the names of the commits at the beginning and end of the range. The &quot;log&quot; format lists the commits in the range like <code><a href="/docs/linux/man/1-git-submodule/">git-submodule</a></code>(1) <code>summary</code> does. The &quot;diff&quot; format shows an inline diff of the changed contents of the submodule. Defaults to &quot;short&quot;. </p>
 </dd></dl>
<p> diff.wordRegex </p>
<dl>
<dd> <p> A POSIX Extended Regular Expression used to determine what is a &quot;word&quot; when performing word-by-word difference calculations. Character sequences that match the regular expression are &quot;words&quot;, all other characters are <code>ignorable</code> whitespace. </p>
 </dd></dl>
<p> diff.&lt;driver&gt;.command </p>
<dl>
<dd> <p> The custom diff driver command. See <code><a href="/docs/linux/man/5-gitattributes/">gitattributes</a></code>(5) for details. </p>
 </dd></dl>
<p> diff.&lt;driver&gt;.xfuncname </p>
<dl>
<dd> <p> The regular expression that the diff driver should use to recognize the hunk header. A built-in pattern may also be used. See <code><a href="/docs/linux/man/5-gitattributes/">gitattributes</a></code>(5) for details. </p>
 </dd></dl>
<p> diff.&lt;driver&gt;.binary </p>
<dl>
<dd> <p> Set this option to true to make the diff driver treat files as binary. See <code><a href="/docs/linux/man/5-gitattributes/">gitattributes</a></code>(5) for details. </p>
 </dd></dl>
<p> diff.&lt;driver&gt;.textconv </p>
<dl>
<dd> <p> The command that the diff driver should call to generate the text-converted version of a file. The result of the conversion is used to generate a human-readable diff. See <code><a href="/docs/linux/man/5-gitattributes/">gitattributes</a></code>(5) for details. </p>
 </dd></dl>
<p> diff.&lt;driver&gt;.wordRegex </p>
<dl>
<dd> <p> The regular expression that the diff driver should use to split words in a line. See <code><a href="/docs/linux/man/5-gitattributes/">gitattributes</a></code>(5) for details. </p>
 </dd></dl>
<p> diff.&lt;driver&gt;.cachetextconv </p>
<dl>
<dd> <p> Set this option to true to make the diff driver cache the text conversion outputs. See <code><a href="/docs/linux/man/5-gitattributes/">gitattributes</a></code>(5) for details. </p>
 </dd></dl>
<p> diff.tool </p>
<dl>
<dd> <p> Controls which diff tool is used by <code><a href="/docs/linux/man/1-git-difftool/">git-difftool</a></code>(1). This variable overrides the value configured in <code>merge.tool</code>. The list below shows the valid built-in values. Any other value is treated as a custom diff tool and requires that a corresponding difftool.&lt;tool&gt;.cmd variable is defined. </p>
 </dd></dl>
<p> diff.guitool </p>
<dl>
<dd> <p> Controls which diff tool is used by <code><a href="/docs/linux/man/1-git-difftool/">git-difftool</a></code>(1) when the -g/--gui flag is specified. This variable overrides the value configured in <code>merge.guitool</code>. The list below shows the valid built-in values. Any other value is treated as a custom diff tool and requires that a corresponding difftool.&lt;guitool&gt;.cmd variable is defined. </p>
 </dd>
<dl>
<dd> <p> &bull; araxis </p>
 </dd></dl>
<dl>
<dd> <p> &bull; bc </p>
 </dd></dl>
<dl>
<dd> <p> &bull; bc3 </p>
 </dd></dl>
<dl>
<dd> <p> &bull; bc4 </p>
 </dd></dl>
<dl>
<dd> <p> &bull; codecompare </p>
 </dd></dl>
<dl>
<dd> <p> &bull; deltawalker </p>
 </dd></dl>
<dl>
<dd> <p> &bull; diffmerge </p>
 </dd></dl>
<dl>
<dd> <p> &bull; diffuse </p>
 </dd></dl>
<dl>
<dd> <p> &bull; ecmerge </p>
 </dd></dl>
<dl>
<dd> <p> &bull; emerge </p>
 </dd></dl>
<dl>
<dd> <p> &bull; examdiff </p>
 </dd></dl>
<dl>
<dd> <p> &bull; guiffy </p>
 </dd></dl>
<dl>
<dd> <p> &bull; gvimdiff </p>
 </dd></dl>
<dl>
<dd> <p> &bull; gvimdiff1 </p>
 </dd></dl>
<dl>
<dd> <p> &bull; gvimdiff2 </p>
 </dd></dl>
<dl>
<dd> <p> &bull; gvimdiff3 </p>
 </dd></dl>
<dl>
<dd> <p> &bull; kdiff3 </p>
 </dd></dl>
<dl>
<dd> <p> &bull; kompare </p>
 </dd></dl>
<dl>
<dd> <p> &bull; meld </p>
 </dd></dl>
<dl>
<dd> <p> &bull; nvimdiff </p>
 </dd></dl>
<dl>
<dd> <p> &bull; nvimdiff1 </p>
 </dd></dl>
<dl>
<dd> <p> &bull; nvimdiff2 </p>
 </dd></dl>
<dl>
<dd> <p> &bull; nvimdiff3 </p>
 </dd></dl>
<dl>
<dd> <p> &bull; opendiff </p>
 </dd></dl>
<dl>
<dd> <p> &bull; p4merge </p>
 </dd></dl>
<dl>
<dd> <p> &bull; smerge </p>
 </dd></dl>
<dl>
<dd> <p> &bull; tkdiff </p>
 </dd></dl>
<dl>
<dd> <p> &bull; vimdiff </p>
 </dd></dl>
<dl>
<dd> <p> &bull; vimdiff1 </p>
 </dd></dl>
<dl>
<dd> <p> &bull; vimdiff2 </p>
 </dd></dl>
<dl>
<dd> <p> &bull; vimdiff3 </p>
 </dd></dl>
<dl>
<dd> <p> &bull; winmerge </p>
 </dd></dl>
<dl>
<dd> <p> &bull; xxdiff </p>
 </dd></dl>
</dl>
<p> diff.indentHeuristic </p>
<dl>
<dd> <p> Set this option to <code>false</code> to disable the default heuristics that shift diff hunk boundaries to make patches easier to read. </p>
 </dd></dl>
<p> diff.algorithm </p>
<dl>
<dd> <p> Choose a diff algorithm. The variants are as follows: </p>
<p> <code>default</code>, <code>myers</code> </p>
 </dd>
<dl>
<dd> <p> The basic greedy diff algorithm. Currently, this is the default. </p>
 </dd></dl>
<p> <code>minimal</code> </p>
<dl>
<dd> <p> Spend extra time to make sure the smallest possible diff is produced. </p>
 </dd></dl>
<p> <code>patience</code> </p>
<dl>
<dd> <p> Use &quot;patience diff&quot; algorithm when generating patches. </p>
 </dd></dl>
<p> <code>histogram</code> </p>
<dl>
<dd> <p> This algorithm extends the patience algorithm to &quot;support low-occurrence common elements&quot;. </p>
 </dd></dl>
</dl>
<p> diff.wsErrorHighlight </p>
<dl>
<dd> <p> Highlight whitespace errors in the <code>context</code>, <code>old</code> or <code>new</code> lines of the diff. Multiple values are separated by comma, <code>none</code> resets previous values, <code>default</code> reset the list to <code>new</code> and <code>all</code> is a shorthand for <code>old,new,context</code>. The whitespace errors are colored with <code>color.diff.whitespace</code>. The command line option <code>--ws-error-highlight=&lt;kind&gt;</code> overrides this setting. </p>
 </dd></dl>
<p> diff.colorMoved </p>
<dl>
<dd> <p> If set to either a valid <code>&lt;mode&gt;</code> or a true value, moved lines in a diff are colored differently, for details of valid modes see <i>--color-moved</i> in <code><a href="/docs/linux/man/1-git-diff/">git-diff</a></code>(1). If simply set to true the default color mode will be used. When set to false, moved lines are not colored. </p>
 </dd></dl>
<p> diff.colorMovedWS </p>
<dl>
<dd> <p> When moved lines are colored using e.g. the <code>diff.colorMoved</code> setting, this option controls the <code>&lt;mode&gt;</code> how spaces are treated for details of valid modes see <i>--color-moved-ws</i> in <code><a href="/docs/linux/man/1-git-diff/">git-diff</a></code>(1). </p>
 </dd></dl>
<p> difftool.&lt;tool&gt;.path </p>
<dl>
<dd> <p> Override the path for the given tool. This is useful in case your tool is not in the PATH. </p>
 </dd></dl>
<p> difftool.&lt;tool&gt;.cmd </p>
<dl>
<dd> <p> Specify the command to invoke the specified diff tool. The specified command is evaluated in shell with the following variables available: <i>LOCAL</i> is set to the name of the temporary file containing the contents of the diff pre-image and <i>REMOTE</i> is set to the name of the temporary file containing the contents of the diff post-image. </p>
 </dd></dl>
<p> difftool.prompt </p>
<dl>
<dd> <p> Prompt before each invocation of the diff tool. </p>
 </dd></dl>
<p> extensions.objectFormat </p>
<dl>
<dd> <p> Specify the hash algorithm to use. The acceptable values are <code>sha1</code> and <code>sha256</code>. If not specified, <code>sha1</code> is assumed. It is an error to specify this key unless <code>core.repositoryFormatVersion</code> is 1. </p>
<p> Note that this setting should only be set by <code><a href="/docs/linux/man/1-git-init/">git-init</a></code>(1) or <code><a href="/docs/linux/man/1-git-clone/">git-clone</a></code>(1). Trying to change it after initialization will not work and will produce hard-to-diagnose issues. </p>
 </dd></dl>
<p> fastimport.unpackLimit </p>
<dl>
<dd> <p> If the number of objects imported by <code><a href="/docs/linux/man/1-git-fast-import/">git-fast-import</a></code>(1) is below this limit, then the objects will be unpacked into loose object files. However if the number of imported objects equals or exceeds this limit then the pack will be stored as a pack. Storing the pack from a fast-import can make the import operation complete faster, especially on slow filesystems. If not set, the value of <code>transfer.unpackLimit</code> is used instead. </p>
 </dd></dl>
<p> feature.* </p>
<dl>
<dd> <p> The config settings that start with <code>feature.</code> modify the defaults of a group of other config settings. These groups are created by the Git developer community as recommended defaults and are subject to change. In particular, new config options may be added with different defaults. </p>
 </dd></dl>
<p> feature.experimental </p>
<dl>
<dd> <p> Enable config options that are new to Git, and are being considered for future defaults. Config settings included here may be added or removed with each release, including minor version updates. These settings may have unintended interactions since they are so new. Please enable this setting if you are interested in providing feedback on experimental features. The new default values are: </p>
 </dd>
<dl>
<dd> <p> &bull; <code>fetch.negotiationAlgorithm=skipping</code> may improve fetch negotiation times by skipping more commits at a time, reducing the number of round trips. </p>
 </dd></dl>
</dl>
<p> feature.manyFiles </p>
<dl>
<dd> <p> Enable config options that optimize for repos with many files in the working directory. With many files, commands such as <code>git status</code> and <code>git checkout</code> may be slow and these new defaults improve performance: </p>
 </dd>
<dl>
<dd> <p> &bull; <code>index.version=4</code> enables path-prefix compression in the index. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>core.untrackedCache=true</code> enables the untracked cache. This setting assumes that mtime is working on your machine. </p>
 </dd></dl>
</dl>
<p> fetch.recurseSubmodules </p>
<dl>
<dd> <p> This option controls whether <code>git fetch</code> (and the underlying fetch in <code>git pull</code>) will recursively fetch into populated submodules. This option can be set either to a boolean value or to <i>on-demand</i>. Setting it to a boolean changes the behavior of fetch and pull to recurse unconditionally into submodules when set to true or to not recurse at all when set to false. When set to <i>on-demand</i>, fetch and pull will only recurse into a populated submodule when its superproject retrieves a commit that updates the submodule&#8217;s reference. Defaults to <i>on-demand</i>, or to the value of <i>submodule.recurse</i> if set. </p>
 </dd></dl>
<p> fetch.fsckObjects </p>
<dl>
<dd> <p> If it is set to true, git-fetch-pack will check all fetched objects. See <code>transfer.fsckObjects</code> for what&#8217;s checked. Defaults to false. If not set, the value of <code>transfer.fsckObjects</code> is used instead. </p>
 </dd></dl>
<p> fetch.fsck.&lt;msg-id&gt; </p>
<dl>
<dd> <p> Acts like <code>fsck.&lt;msg-id&gt;</code>, but is used by <code><a href="/docs/linux/man/1-git-fetch-pack/">git-fetch-pack</a></code>(1) instead of <code><a href="/docs/linux/man/1-git-fsck/">git-fsck</a></code>(1). See the <code>fsck.&lt;msg-id&gt;</code> documentation for details. </p>
 </dd></dl>
<p> fetch.fsck.skipList </p>
<dl>
<dd> <p> Acts like <code>fsck.skipList</code>, but is used by <code><a href="/docs/linux/man/1-git-fetch-pack/">git-fetch-pack</a></code>(1) instead of <code><a href="/docs/linux/man/1-git-fsck/">git-fsck</a></code>(1). See the <code>fsck.skipList</code> documentation for details. </p>
 </dd></dl>
<p> fetch.unpackLimit </p>
<dl>
<dd> <p> If the number of objects fetched over the Git native transfer is below this limit, then the objects will be unpacked into loose object files. However if the number of received objects equals or exceeds this limit then the received pack will be stored as a pack, after adding any missing delta bases. Storing the pack from a push can make the push operation complete faster, especially on slow filesystems. If not set, the value of <code>transfer.unpackLimit</code> is used instead. </p>
 </dd></dl>
<p> fetch.prune </p>
<dl>
<dd> <p> If true, fetch will automatically behave as if the <code>--prune</code> option was given on the command line. See also <code>remote.&lt;name&gt;.prune</code> and the PRUNING section of <code><a href="/docs/linux/man/1-git-fetch/">git-fetch</a></code>(1). </p>
 </dd></dl>
<p> fetch.pruneTags </p>
<dl>
<dd> <p> If true, fetch will automatically behave as if the <code>refs/tags/*:refs/tags/*</code> refspec was provided when pruning, if not set already. This allows for setting both this option and <code>fetch.prune</code> to maintain a 1=1 mapping to upstream refs. See also <code>remote.&lt;name&gt;.pruneTags</code> and the PRUNING section of <code><a href="/docs/linux/man/1-git-fetch/">git-fetch</a></code>(1). </p>
 </dd></dl>
<p> fetch.output </p>
<dl>
<dd> <p> Control how ref update status is printed. Valid values are <code>full</code> and <code>compact</code>. Default value is <code>full</code>. See section OUTPUT in <code><a href="/docs/linux/man/1-git-fetch/">git-fetch</a></code>(1) for detail. </p>
 </dd></dl>
<p> fetch.negotiationAlgorithm </p>
<dl>
<dd> <p> Control how information about the commits in the local repository is sent when negotiating the contents of the packfile to be sent by the server. Set to &quot;skipping&quot; to use an algorithm that skips commits in an effort to converge faster, but may result in a larger-than-necessary packfile; or set to &quot;noop&quot; to not send any information at all, which will almost certainly result in a larger-than-necessary packfile, but will skip the negotiation step. The default is &quot;default&quot; which instructs Git to use the default algorithm that never skips commits (unless the server has acknowledged it or one of its descendants). If <code>feature.experimental</code> is enabled, then this setting defaults to &quot;skipping&quot;. Unknown values will cause <i>git fetch</i> to error out. </p>
<p> See also the <code>--negotiate-only</code> and <code>--negotiation-tip</code> options to <code><a href="/docs/linux/man/1-git-fetch/">git-fetch</a></code>(1). </p>
 </dd></dl>
<p> fetch.showForcedUpdates </p>
<dl>
<dd> <p> Set to false to enable <code>--no-show-forced-updates</code> in <code><a href="/docs/linux/man/1-git-fetch/">git-fetch</a></code>(1) and <code><a href="/docs/linux/man/1-git-pull/">git-pull</a></code>(1) commands. Defaults to true. </p>
 </dd></dl>
<p> fetch.parallel </p>
<dl>
<dd> <p> Specifies the maximal number of fetch operations to be run in parallel at a time (submodules, or remotes when the <code>--multiple</code> option of <code><a href="/docs/linux/man/1-git-fetch/">git-fetch</a></code>(1) is in effect). </p>
<p> A value of 0 will give some reasonable default. If unset, it defaults to 1. </p>
<p> For submodules, this setting can be overridden using the <code>submodule.fetchJobs</code> config setting. </p>
 </dd></dl>
<p> fetch.writeCommitGraph </p>
<dl>
<dd> <p> Set to true to write a commit-graph after every <code>git fetch</code> command that downloads a pack-file from a remote. Using the <code>--split</code> option, most executions will create a very small commit-graph file on top of the existing commit-graph file(s). Occasionally, these files will merge and the write may take longer. Having an updated commit-graph file helps performance of many Git commands, including <code>git merge-base</code>, <code>git push -f</code>, and <code>git log --graph</code>. Defaults to false. </p>
 </dd></dl>
<p> format.attach </p>
<dl>
<dd> <p> Enable multipart/mixed attachments as the default for <i>format-patch</i>. The value can also be a double quoted string which will enable attachments as the default and set the value as the boundary. See the --attach option in <code><a href="/docs/linux/man/1-git-format-patch/">git-format-patch</a></code>(1). </p>
 </dd></dl>
<p> format.from </p>
<dl>
<dd> <p> Provides the default value for the <code>--from</code> option to format-patch. Accepts a boolean value, or a name and email address. If false, format-patch defaults to <code>--no-from</code>, using commit authors directly in the &quot;From:&quot; field of patch mails. If true, format-patch defaults to <code>--from</code>, using your committer identity in the &quot;From:&quot; field of patch mails and including a &quot;From:&quot; field in the body of the patch mail if different. If set to a non-boolean value, format-patch uses that value instead of your committer identity. Defaults to false. </p>
 </dd></dl>
<p> format.numbered </p>
<dl>
<dd> <p> A boolean which can enable or disable sequence numbers in patch subjects. It defaults to &quot;auto&quot; which enables it only if there is more than one patch. It can be enabled or disabled for all messages by setting it to &quot;true&quot; or &quot;false&quot;. See --numbered option in <code><a href="/docs/linux/man/1-git-format-patch/">git-format-patch</a></code>(1). </p>
 </dd></dl>
<p> format.headers </p>
<dl>
<dd> <p> Additional email headers to include in a patch to be submitted by mail. See <code><a href="/docs/linux/man/1-git-format-patch/">git-format-patch</a></code>(1). </p>
 </dd></dl>
<p> format.to, format.cc </p>
<dl>
<dd> <p> Additional recipients to include in a patch to be submitted by mail. See the --to and --cc options in <code><a href="/docs/linux/man/1-git-format-patch/">git-format-patch</a></code>(1). </p>
 </dd></dl>
<p> format.subjectPrefix </p>
<dl>
<dd> <p> The default for format-patch is to output files with the <i>[PATCH]</i> subject prefix. Use this variable to change that prefix. </p>
 </dd></dl>
<p> format.coverFromDescription </p>
<dl>
<dd> <p> The default mode for format-patch to determine which parts of the cover letter will be populated using the branch&#8217;s description. See the <code>--cover-from-description</code> option in <code><a href="/docs/linux/man/1-git-format-patch/">git-format-patch</a></code>(1). </p>
 </dd></dl>
<p> format.signature </p>
<dl>
<dd> <p> The default for format-patch is to output a signature containing the Git version number. Use this variable to change that default. Set this variable to the empty string (&quot;&quot;) to suppress signature generation. </p>
 </dd></dl>
<p> format.signatureFile </p>
<dl>
<dd> <p> Works just like format.signature except the contents of the file specified by this variable will be used as the signature. </p>
 </dd></dl>
<p> format.suffix </p>
<dl>
<dd> <p> The default for format-patch is to output files with the suffix <code>.patch</code>. Use this variable to change that suffix (make sure to include the dot if you want it). </p>
 </dd></dl>
<p> format.encodeEmailHeaders </p>
<dl>
<dd> <p> Encode email headers that have non-ASCII characters with &quot;Q-encoding&quot; (described in RFC 2047) for email transmission. Defaults to true. </p>
 </dd></dl>
<p> format.pretty </p>
<dl>
<dd> <p> The default pretty format for log/show/whatchanged command, See <code><a href="/docs/linux/man/1-git-log/">git-log</a></code>(1), <code><a href="/docs/linux/man/1-git-show/">git-show</a></code>(1), <code><a href="/docs/linux/man/1-git-whatchanged/">git-whatchanged</a></code>(1). </p>
 </dd></dl>
<p> format.thread </p>
<dl>
<dd> <p> The default threading style for <i>git format-patch</i>. Can be a boolean value, or <code>shallow</code> or <code>deep</code>. <code>shallow</code> threading makes every mail a reply to the head of the series, where the head is chosen from the cover letter, the <code>--in-reply-to</code>, and the first patch mail, in this order. <code>deep</code> threading makes every mail a reply to the previous one. A true boolean value is the same as <code>shallow</code>, and a false value disables threading. </p>
 </dd></dl>
<p> format.signOff </p>
<dl>
<dd> <p> A boolean value which lets you enable the <code>-s/--signoff</code> option of format-patch by default. <code>Note:</code> Adding the <code>Signed-off-by</code> trailer to a patch should be a conscious act and means that you certify you have the rights to submit this work under the same open source license. Please see the <i>SubmittingPatches</i> document for further discussion. </p>
 </dd></dl>
<p> format.coverLetter </p>
<dl>
<dd> <p> A boolean that controls whether to generate a cover-letter when format-patch is invoked, but in addition can be set to &quot;auto&quot;, to generate a cover-letter only when there&#8217;s more than one patch. Default is false. </p>
 </dd></dl>
<p> format.outputDirectory </p>
<dl>
<dd> <p> Set a custom directory to store the resulting files instead of the current working directory. All directory components will be created. </p>
 </dd></dl>
<p> format.filenameMaxLength </p>
<dl>
<dd> <p> The maximum length of the output filenames generated by the <code>format-patch</code> command; defaults to 64. Can be overridden by the <code>--filename-max-length=&lt;n&gt;</code> command line option. </p>
 </dd></dl>
<p> format.useAutoBase </p>
<dl>
<dd> <p> A boolean value which lets you enable the <code>--base=auto</code> option of format-patch by default. Can also be set to &quot;whenAble&quot; to allow enabling <code>--base=auto</code> if a suitable base is available, but to skip adding base info otherwise without the format dying. </p>
 </dd></dl>
<p> format.notes </p>
<dl>
<dd> <p> Provides the default value for the <code>--notes</code> option to format-patch. Accepts a boolean value, or a ref which specifies where to get notes. If false, format-patch defaults to <code>--no-notes</code>. If true, format-patch defaults to <code>--notes</code>. If set to a non-boolean value, format-patch defaults to <code>--notes=&lt;ref&gt;</code>, where <code>ref</code> is the non-boolean value. Defaults to false. </p>
<p> If one wishes to use the ref <code>ref/notes/true</code>, please use that literal instead. </p>
<p> This configuration can be specified multiple times in order to allow multiple notes refs to be included. In that case, it will behave similarly to multiple <code>--[no-]notes[=]</code> options passed in. That is, a value of <code>true</code> will show the default notes, a value of <code>&lt;ref&gt;</code> will also show notes from that notes ref and a value of <code>false</code> will negate previous configurations and not show notes. </p>
<p> For example, </p>
 </dd>
<dl>
<dd> <pre><code>[format]
        notes = true
        notes = foo
        notes = false
        notes = bar
</code></pre>
 </dd></dl>
<p> will only show notes from <code>refs/notes/bar</code>. </dl>
 </p>
<p> filter.&lt;driver&gt;.clean </p>
<dl>
<dd> <p> The command which is used to convert the content of a worktree file to a blob upon checkin. See <code><a href="/docs/linux/man/5-gitattributes/">gitattributes</a></code>(5) for details. </p>
 </dd></dl>
<p> filter.&lt;driver&gt;.smudge </p>
<dl>
<dd> <p> The command which is used to convert the content of a blob object to a worktree file upon checkout. See <code><a href="/docs/linux/man/5-gitattributes/">gitattributes</a></code>(5) for details. </p>
 </dd></dl>
<p> fsck.&lt;msg-id&gt; </p>
<dl>
<dd> <p> During fsck git may find issues with legacy data which wouldn&#8217;t be generated by current versions of git, and which wouldn&#8217;t be sent over the wire if <code>transfer.fsckObjects</code> was set. This feature is intended to support working with legacy repositories containing such data. </p>
<p> Setting <code>fsck.&lt;msg-id&gt;</code> will be picked up by <code><a href="/docs/linux/man/1-git-fsck/">git-fsck</a></code>(1), but to accept pushes of such data set <code>receive.fsck.&lt;msg-id&gt;</code> instead, or to clone or fetch it set <code>fetch.fsck.&lt;msg-id&gt;</code>. </p>
<p> The rest of the documentation discusses <code>fsck.*</code> for brevity, but the same applies for the corresponding <code>receive.fsck.*</code> and <code>fetch.&lt;msg-id&gt;.*</code>. variables. </p>
<p> Unlike variables like <code>color.ui</code> and <code>core.editor</code> the <code>receive.fsck.&lt;msg-id&gt;</code> and <code>fetch.fsck.&lt;msg-id&gt;</code> variables will not fall back on the <code>fsck.&lt;msg-id&gt;</code> configuration if they aren&#8217;t set. To uniformly configure the same fsck settings in different circumstances all three of them they must all set to the same values. </p>
<p> When <code>fsck.&lt;msg-id&gt;</code> is set, errors can be switched to warnings and vice versa by configuring the <code>fsck.&lt;msg-id&gt;</code> setting where the <code>&lt;msg-id&gt;</code> is the fsck message ID and the value is one of <code>error</code>, <code>warn</code> or <code>ignore</code>. For convenience, fsck prefixes the error/warning with the message ID, e.g. &quot;missingEmail: invalid author/committer line - missing email&quot; means that setting <code>fsck.missingEmail = ignore</code> will hide that issue. </p>
<p> In general, it is better to enumerate existing objects with problems with <code>fsck.skipList</code>, instead of listing the kind of breakages these problematic objects share to be ignored, as doing the latter will allow new instances of the same breakages go unnoticed. </p>
<p> Setting an unknown <code>fsck.&lt;msg-id&gt;</code> value will cause fsck to die, but doing the same for <code>receive.fsck.&lt;msg-id&gt;</code> and <code>fetch.fsck.&lt;msg-id&gt;</code> will only cause git to warn. </p>
 </dd></dl>
<p> fsck.skipList </p>
<dl>
<dd> <p> The path to a list of object names (i.e. one unabbreviated SHA-1 per line) that are known to be broken in a non-fatal way and should be ignored. On versions of Git 2.20 and later comments (<i>#</i>), empty lines, and any leading and trailing whitespace is ignored. Everything but a SHA-1 per line will error out on older versions. </p>
<p> This feature is useful when an established project should be accepted despite early commits containing errors that can be safely ignored such as invalid committer email addresses. Note: corrupt objects cannot be skipped with this setting. </p>
<p> Like <code>fsck.&lt;msg-id&gt;</code> this variable has corresponding <code>receive.fsck.skipList</code> and <code>fetch.fsck.skipList</code> variants. </p>
<p> Unlike variables like <code>color.ui</code> and <code>core.editor</code> the <code>receive.fsck.skipList</code> and <code>fetch.fsck.skipList</code> variables will not fall back on the <code>fsck.skipList</code> configuration if they aren&#8217;t set. To uniformly configure the same fsck settings in different circumstances all three of them they must all set to the same values. </p>
<p> Older versions of Git (before 2.20) documented that the object names list should be sorted. This was never a requirement, the object names could appear in any order, but when reading the list we tracked whether the list was sorted for the purposes of an internal binary search implementation, which could save itself some work with an already sorted list. Unless you had a humongous list there was no reason to go out of your way to pre-sort the list. After Git version 2.20 a hash implementation is used instead, so there&#8217;s now no reason to pre-sort the list. </p>
 </dd></dl>
<p> gc.aggressiveDepth </p>
<dl>
<dd> <p> The depth parameter used in the delta compression algorithm used by <i>git gc --aggressive</i>. This defaults to 50, which is the default for the <code>--depth</code> option when <code>--aggressive</code> isn&#8217;t in use. </p>
<p> See the documentation for the <code>--depth</code> option in <code><a href="/docs/linux/man/1-git-repack/">git-repack</a></code>(1) for more details. </p>
 </dd></dl>
<p> gc.aggressiveWindow </p>
<dl>
<dd> <p> The window size parameter used in the delta compression algorithm used by <i>git gc --aggressive</i>. This defaults to 250, which is a much more aggressive window size than the default <code>--window</code> of 10. </p>
<p> See the documentation for the <code>--window</code> option in <code><a href="/docs/linux/man/1-git-repack/">git-repack</a></code>(1) for more details. </p>
 </dd></dl>
<p> gc.auto </p>
<dl>
<dd> <p> When there are approximately more than this many loose objects in the repository, <code>git gc --auto</code> will pack them. Some Porcelain commands use this command to perform a light-weight garbage collection from time to time. The default value is 6700. </p>
<p> Setting this to 0 disables not only automatic packing based on the number of loose objects, but any other heuristic <code>git gc --auto</code> will otherwise use to determine if there&#8217;s work to do, such as <code>gc.autoPackLimit</code>. </p>
 </dd></dl>
<p> gc.autoPackLimit </p>
<dl>
<dd> <p> When there are more than this many packs that are not marked with <code>*.keep</code> file in the repository, <code>git gc --auto</code> consolidates them into one larger pack. The default value is 50. Setting this to 0 disables it. Setting <code>gc.auto</code> to 0 will also disable this. </p>
<p> See the <code>gc.bigPackThreshold</code> configuration variable below. When in use, it&#8217;ll affect how the auto pack limit works. </p>
 </dd></dl>
<p> gc.autoDetach </p>
<dl>
<dd> <p> Make <code>git gc --auto</code> return immediately and run in background if the system supports it. Default is true. </p>
 </dd></dl>
<p> gc.bigPackThreshold </p>
<dl>
<dd> <p> If non-zero, all packs larger than this limit are kept when <code>git gc</code> is run. This is very similar to <code>--keep-largest-pack</code> except that all packs that meet the threshold are kept, not just the largest pack. Defaults to zero. Common unit suffixes of <i>k</i>, <i>m</i>, or <i>g</i> are supported. </p>
<p> Note that if the number of kept packs is more than gc.autoPackLimit, this configuration variable is ignored, all packs except the base pack will be repacked. After this the number of packs should go below gc.autoPackLimit and gc.bigPackThreshold should be respected again. </p>
<p> If the amount of memory estimated for <code>git repack</code> to run smoothly is not available and <code>gc.bigPackThreshold</code> is not set, the largest pack will also be excluded (this is the equivalent of running <code>git gc</code> with <code>--keep-largest-pack</code>). </p>
 </dd></dl>
<p> gc.writeCommitGraph </p>
<dl>
<dd> <p> If true, then gc will rewrite the commit-graph file when <code><a href="/docs/linux/man/1-git-gc/">git-gc</a></code>(1) is run. When using <code>git gc --auto</code> the commit-graph will be updated if housekeeping is required. Default is true. See <code><a href="/docs/linux/man/1-git-commit-graph/">git-commit-graph</a></code>(1) for details. </p>
 </dd></dl>
<p> gc.logExpiry </p>
<dl>
<dd> <p> If the file gc.log exists, then <code>git gc --auto</code> will print its content and exit with status zero instead of running unless that file is more than <i>gc.logExpiry</i> old. Default is &quot;1.day&quot;. See <code>gc.pruneExpire</code> for more ways to specify its value. </p>
 </dd></dl>
<p> gc.packRefs </p>
<dl>
<dd> <p> Running <code>git pack-refs</code> in a repository renders it unclonable by Git versions prior to 1.5.1.2 over dumb transports such as HTTP. This variable determines whether <i>git gc</i> runs <code>git pack-refs</code>. This can be set to <code>notbare</code> to enable it within all non-bare repos or it can be set to a boolean value. The default is <code>true</code>. </p>
 </dd></dl>
<p> gc.pruneExpire </p>
<dl>
<dd> <p> When <i>git gc</i> is run, it will call <i>prune --expire 2.weeks.ago</i>. Override the grace period with this config variable. The value &quot;now&quot; may be used to disable this grace period and always prune unreachable objects immediately, or &quot;never&quot; may be used to suppress pruning. This feature helps prevent corruption when <i>git gc</i> runs concurrently with another process writing to the repository; see the &quot;NOTES&quot; section of <code><a href="/docs/linux/man/1-git-gc/">git-gc</a></code>(1). </p>
 </dd></dl>
<p> gc.worktreePruneExpire </p>
<dl>
<dd> <p> When <i>git gc</i> is run, it calls <i>git worktree prune --expire 3.months.ago</i>. This config variable can be used to set a different grace period. The value &quot;now&quot; may be used to disable the grace period and prune <code>$GIT_DIR/worktrees</code> immediately, or &quot;never&quot; may be used to suppress pruning. </p>
 </dd></dl>
<p> gc.reflogExpire, gc.&lt;pattern&gt;.reflogExpire </p>
<dl>
<dd> <p> <i>git reflog expire</i> removes reflog entries older than this time; defaults to 90 days. The value &quot;now&quot; expires all entries immediately, and &quot;never&quot; suppresses expiration altogether. With &quot;&lt;pattern&gt;&quot; (e.g. &quot;refs/stash&quot;) in the middle the setting applies only to the refs that match the &lt;pattern&gt;. </p>
 </dd></dl>
<p> gc.reflogExpireUnreachable, gc.&lt;pattern&gt;.reflogExpireUnreachable </p>
<dl>
<dd> <p> <i>git reflog expire</i> removes reflog entries older than this time and are not reachable from the current tip; defaults to 30 days. The value &quot;now&quot; expires all entries immediately, and &quot;never&quot; suppresses expiration altogether. With &quot;&lt;pattern&gt;&quot; (e.g. &quot;refs/stash&quot;) in the middle, the setting applies only to the refs that match the &lt;pattern&gt;. </p>
<p> These types of entries are generally created as a result of using <code>git commit --amend</code> or <code>git rebase</code> and are the commits prior to the amend or rebase occurring. Since these changes are not part of the current project most users will want to expire them sooner, which is why the default is more aggressive than <code>gc.reflogExpire</code>. </p>
 </dd></dl>
<p> gc.rerereResolved </p>
<dl>
<dd> <p> Records of conflicted merge you resolved earlier are kept for this many days when <i>git rerere gc</i> is run. You can also use more human-readable &quot;1.month.ago&quot;, etc. The default is 60 days. See <code><a href="/docs/linux/man/1-git-rerere/">git-rerere</a></code>(1). </p>
 </dd></dl>
<p> gc.rerereUnresolved </p>
<dl>
<dd> <p> Records of conflicted merge you have not resolved are kept for this many days when <i>git rerere gc</i> is run. You can also use more human-readable &quot;1.month.ago&quot;, etc. The default is 15 days. See <code><a href="/docs/linux/man/1-git-rerere/">git-rerere</a></code>(1). </p>
 </dd></dl>
<p> gitcvs.commitMsgAnnotation </p>
<dl>
<dd> <p> Append this string to each commit message. Set to empty string to disable this feature. Defaults to &quot;via git-CVS emulator&quot;. </p>
 </dd></dl>
<p> gitcvs.enabled </p>
<dl>
<dd> <p> Whether the CVS server interface is enabled for this repository. See <code><a href="/docs/linux/man/1-git-cvsserver/">git-cvsserver</a></code>(1). </p>
 </dd></dl>
<p> gitcvs.logFile </p>
<dl>
<dd> <p> Path to a log file where the CVS server interface well... logs various stuff. See <code><a href="/docs/linux/man/1-git-cvsserver/">git-cvsserver</a></code>(1). </p>
 </dd></dl>
<p> gitcvs.usecrlfattr </p>
<dl>
<dd> <p> If true, the server will look up the end-of-line conversion attributes for files to determine the <code>-k</code> modes to use. If the attributes force Git to treat a file as text, the <code>-k</code> mode will be left blank so CVS clients will treat it as text. If they suppress text conversion, the file will be set with <i>-kb</i> mode, which suppresses any newline munging the client might otherwise do. If the attributes do not allow the file type to be determined, then <code>gitcvs.allBinary</code> is used. See <code><a href="/docs/linux/man/5-gitattributes/">gitattributes</a></code>(5). </p>
 </dd></dl>
<p> gitcvs.allBinary </p>
<dl>
<dd> <p> This is used if <code>gitcvs.usecrlfattr</code> does not resolve the correct <i>-kb</i> mode to use. If true, all unresolved files are sent to the client in mode <i>-kb</i>. This causes the client to treat them as binary files, which suppresses any newline munging it otherwise might do. Alternatively, if it is set to &quot;guess&quot;, then the contents of the file are examined to decide if it is binary, similar to <code>core.autocrlf</code>. </p>
 </dd></dl>
<p> gitcvs.dbName </p>
<dl>
<dd> <p> Database used by git-cvsserver to cache revision information derived from the Git repository. The exact meaning depends on the used database driver, for SQLite (which is the default driver) this is a filename. Supports variable substitution (see <code><a href="/docs/linux/man/1-git-cvsserver/">git-cvsserver</a></code>(1) for details). May not contain semicolons (<code>;</code>). Default: <i>%Ggitcvs.%m.sqlite</i> </p>
 </dd></dl>
<p> gitcvs.dbDriver </p>
<dl>
<dd> <p> Used Perl DBI driver. You can specify any available driver for this here, but it might not work. git-cvsserver is tested with <i>DBD::SQLite</i>, reported to work with <i>DBD::Pg</i>, and reported <code>not</code> to work with <i>DBD::mysql</i>. Experimental feature. May not contain double colons (<code>:</code>). Default: <i>SQLite</i>. See <code><a href="/docs/linux/man/1-git-cvsserver/">git-cvsserver</a></code>(1). </p>
 </dd></dl>
<p> gitcvs.dbUser, gitcvs.dbPass </p>
<dl>
<dd> <p> Database user and password. Only useful if setting <code>gitcvs.dbDriver</code>, since SQLite has no concept of database users and/or passwords. <i>gitcvs.dbUser</i> supports variable substitution (see <code><a href="/docs/linux/man/1-git-cvsserver/">git-cvsserver</a></code>(1) for details). </p>
 </dd></dl>
<p> gitcvs.dbTableNamePrefix </p>
<dl>
<dd> <p> Database table name prefix. Prepended to the names of any database tables used, allowing a single database to be used for several repositories. Supports variable substitution (see <code><a href="/docs/linux/man/1-git-cvsserver/">git-cvsserver</a></code>(1) for details). Any non-alphabetic characters will be replaced with underscores. </p>
 </dd></dl>
<p> All gitcvs variables except for <code>gitcvs.usecrlfattr</code> and <code>gitcvs.allBinary</code> can also be specified as <i>gitcvs.&lt;access_method&gt;.&lt;varname&gt;</i> (where <i>access_method</i> is one of &quot;ext&quot; and &quot;pserver&quot;) to make them apply only for the given access method. </p>
<p> gitweb.category, gitweb.description, gitweb.owner, gitweb.url </p>
<dl>
<dd> <p> See <code><a href="/docs/linux/man/1-gitweb/">gitweb</a></code>(1) for description. </p>
 </dd></dl>
<p> gitweb.avatar, gitweb.blame, gitweb.grep, gitweb.highlight, gitweb.patches, gitweb.pickaxe, gitweb.remote_heads, gitweb.showSizes, gitweb.snapshot </p>
<dl>
<dd> <p> See <code>gitweb.conf</code>(5) for description. </p>
 </dd></dl>
<p> grep.lineNumber </p>
<dl>
<dd> <p> If set to true, enable <code>-n</code> option by default. </p>
 </dd></dl>
<p> grep.column </p>
<dl>
<dd> <p> If set to true, enable the <code>--column</code> option by default. </p>
 </dd></dl>
<p> grep.patternType </p>
<dl>
<dd> <p> Set the default matching behavior. Using a value of <i>basic</i>, <i>extended</i>, <i>fixed</i>, or <i>perl</i> will enable the <code>--basic-regexp</code>, <code>--extended-regexp</code>, <code>--fixed-strings</code>, or <code>--perl-regexp</code> option accordingly, while the value <i>default</i> will return to the default matching behavior. </p>
 </dd></dl>
<p> grep.extendedRegexp </p>
<dl>
<dd> <p> If set to true, enable <code>--extended-regexp</code> option by default. This option is ignored when the <code>grep.patternType</code> option is set to a value other than <i>default</i>. </p>
 </dd></dl>
<p> grep.threads </p>
<dl>
<dd> <p> Number of grep worker threads to use. See <code>grep.threads</code> in <code><a href="/docs/linux/man/1-git-grep/">git-grep</a></code>(1) for more information. </p>
 </dd></dl>
<p> grep.fallbackToNoIndex </p>
<dl>
<dd> <p> If set to true, fall back to git grep --no-index if git grep is executed outside of a git repository. Defaults to false. </p>
 </dd></dl>
<p> gpg.program </p>
<dl>
<dd> <p> Use this custom program instead of &quot;<code>gpg</code>&quot; found on <code>$PATH</code> when making or verifying a PGP signature. The program must support the same command-line interface as GPG, namely, to verify a detached signature, &quot;<code>gpg --verify $signature - &lt;$file</code>&quot; is run, and the program is expected to signal a good signature by exiting with code 0, and to generate an ASCII-armored detached signature, the standard input of &quot;<code>gpg -bsau $key</code>&quot; is fed with the contents to be signed, and the program is expected to send the result to its standard output. </p>
 </dd></dl>
<p> gpg.format </p>
<dl>
<dd> <p> Specifies which key format to use when signing with <code>--gpg-sign</code>. Default is &quot;openpgp&quot;. Other possible values are &quot;x509&quot;, &quot;ssh&quot;. </p>
 </dd></dl>
<p> gpg.&lt;format&gt;.program </p>
<dl>
<dd> <p> Use this to customize the program used for the signing format you chose. (see <code>gpg.program</code> and <code>gpg.format</code>) <code>gpg.program</code> can still be used as a legacy synonym for <code>gpg.openpgp.program</code>. The default value for <code>gpg.x509.program</code> is &quot;gpgsm&quot; and <code>gpg.ssh.program</code> is &quot;ssh-keygen&quot;. </p>
 </dd></dl>
<p> gpg.minTrustLevel </p>
<dl>
<dd> <p> Specifies a minimum trust level for signature verification. If this option is unset, then signature verification for merge operations require a key with at least <code>marginal</code> trust. Other operations that perform signature verification require a key with at least <code>undefined</code> trust. Setting this option overrides the required trust-level for all operations. Supported values, in increasing order of significance: </p>
 </dd>
<dl>
<dd> <p> &bull; <code>undefined</code> </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>never</code> </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>marginal</code> </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>fully</code> </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>ultimate</code> </p>
 </dd></dl>
</dl>
<p> gpg.ssh.defaultKeyCommand: This command that will be run when user.signingkey is not set and a ssh signature is requested. On successful exit a valid ssh public key is expected in the first line of its output. To automatically use the first available key from your ssh-agent set this to &quot;ssh-add -L&quot;. </p>
<p> gpg.ssh.allowedSignersFile </p>
<dl>
<dd> <p> A file containing ssh public keys which you are willing to trust. The file consists of one or more lines of principals followed by an ssh public key. e.g.: m[blue]<code>user1 [at] example.com</code>m[]<font SIZE="-2">[1]</font>,m[blue]<code>user2 [at] example.com</code>m[]<font SIZE="-2">[2]</font> ssh-rsa AAAAX1... See <a href="/docs/linux/man/1-ssh-keygen/">ssh-keygen</a>(1) &quot;ALLOWED SIGNERS&quot; for details. The principal is only used to identify the key and is available when verifying a signature. </p>
<p> SSH has no concept of trust levels like gpg does. To be able to differentiate between valid signatures and trusted signatures the trust level of a signature verification is set to <code>fully</code> when the public key is present in the allowedSignersFile. Otherwise the trust level is <code>undefined</code> and git verify-commit/tag will fail. </p>
<p> This file can be set to a location outside of the repository and every developer maintains their own trust store. A central repository server could generate this file automatically from ssh keys with push access to verify the code against. In a corporate setting this file is probably generated at a global location from automation that already handles developer ssh keys. </p>
<p> A repository that only allows signed commits can store the file in the repository itself using a path relative to the top-level of the working tree. This way only committers with an already valid key can add or change keys in the keyring. </p>
<p> Using a SSH CA key with the cert-authority option (see <a href="/docs/linux/man/1-ssh-keygen/">ssh-keygen</a>(1) &quot;CERTIFICATES&quot;) is also valid. </p>
 </dd></dl>
<p> gpg.ssh.revocationFile </p>
<dl>
<dd> <p> Either a SSH KRL or a list of revoked public keys (without the principal prefix). See <a href="/docs/linux/man/1-ssh-keygen/">ssh-keygen</a>(1) for details. If a public key is found in this file then it will always be treated as having trust level &quot;never&quot; and signatures will show as invalid. </p>
 </dd></dl>
<p> gui.commitMsgWidth </p>
<dl>
<dd> <p> Defines how wide the commit message window is in the <code><a href="/docs/linux/man/1-git-gui/">git-gui</a></code>(1). &quot;75&quot; is the default. </p>
 </dd></dl>
<p> gui.diffContext </p>
<dl>
<dd> <p> Specifies how many context lines should be used in calls to diff made by the <code><a href="/docs/linux/man/1-git-gui/">git-gui</a></code>(1). The default is &quot;5&quot;. </p>
 </dd></dl>
<p> gui.displayUntracked </p>
<dl>
<dd> <p> Determines if <code><a href="/docs/linux/man/1-git-gui/">git-gui</a></code>(1) shows untracked files in the file list. The default is &quot;true&quot;. </p>
 </dd></dl>
<p> gui.encoding </p>
<dl>
<dd> <p> Specifies the default character encoding to use for displaying of file contents in <code><a href="/docs/linux/man/1-git-gui/">git-gui</a></code>(1) and <code><a href="/docs/linux/man/1-gitk/">gitk</a></code>(1). It can be overridden by setting the <i>encoding</i> attribute for relevant files (see <code><a href="/docs/linux/man/5-gitattributes/">gitattributes</a></code>(5)). If this option is not set, the tools default to the locale encoding. </p>
 </dd></dl>
<p> gui.matchTrackingBranch </p>
<dl>
<dd> <p> Determines if new branches created with <code><a href="/docs/linux/man/1-git-gui/">git-gui</a></code>(1) should default to tracking remote branches with matching names or not. Default: &quot;false&quot;. </p>
 </dd></dl>
<p> gui.newBranchTemplate </p>
<dl>
<dd> <p> Is used as suggested name when creating new branches using the <code><a href="/docs/linux/man/1-git-gui/">git-gui</a></code>(1). </p>
 </dd></dl>
<p> gui.pruneDuringFetch </p>
<dl>
<dd> <p> &quot;true&quot; if <code><a href="/docs/linux/man/1-git-gui/">git-gui</a></code>(1) should prune remote-tracking branches when performing a fetch. The default value is &quot;false&quot;. </p>
 </dd></dl>
<p> gui.trustmtime </p>
<dl>
<dd> <p> Determines if <code><a href="/docs/linux/man/1-git-gui/">git-gui</a></code>(1) should trust the file modification timestamp or not. By default the timestamps are not trusted. </p>
 </dd></dl>
<p> gui.spellingDictionary </p>
<dl>
<dd> <p> Specifies the dictionary used for spell checking commit messages in the <code><a href="/docs/linux/man/1-git-gui/">git-gui</a></code>(1). When set to &quot;none&quot; spell checking is turned off. </p>
 </dd></dl>
<p> gui.fastCopyBlame </p>
<dl>
<dd> <p> If true, <i>git gui blame</i> uses <code>-C</code> instead of <code>-C -C</code> for original location detection. It makes blame significantly faster on huge repositories at the expense of less thorough copy detection. </p>
 </dd></dl>
<p> gui.copyBlameThreshold </p>
<dl>
<dd> <p> Specifies the threshold to use in <i>git gui blame</i> original location detection, measured in alphanumeric characters. See the <code><a href="/docs/linux/man/1-git-blame/">git-blame</a></code>(1) manual for more information on copy detection. </p>
 </dd></dl>
<p> gui.blamehistoryctx </p>
<dl>
<dd> <p> Specifies the radius of history context in days to show in <code><a href="/docs/linux/man/1-gitk/">gitk</a></code>(1) for the selected commit, when the <code>Show History Context</code> menu item is invoked from <i>git gui blame</i>. If this variable is set to zero, the whole history is shown. </p>
 </dd></dl>
<p> guitool.&lt;name&gt;.cmd </p>
<dl>
<dd> <p> Specifies the shell command line to execute when the corresponding item of the <code><a href="/docs/linux/man/1-git-gui/">git-gui</a></code>(1) <code>Tools</code> menu is invoked. This option is mandatory for every tool. The command is executed from the root of the working directory, and in the environment it receives the name of the tool as <code>GIT_GUITOOL</code>, the name of the currently selected file as <i>FILENAME</i>, and the name of the current branch as <i>CUR_BRANCH</i> (if the head is detached, <i>CUR_BRANCH</i> is empty). </p>
 </dd></dl>
<p> guitool.&lt;name&gt;.needsFile </p>
<dl>
<dd> <p> Run the tool only if a diff is selected in the GUI. It guarantees that <i>FILENAME</i> is not empty. </p>
 </dd></dl>
<p> guitool.&lt;name&gt;.noConsole </p>
<dl>
<dd> <p> Run the command silently, without creating a window to display its output. </p>
 </dd></dl>
<p> guitool.&lt;name&gt;.noRescan </p>
<dl>
<dd> <p> Don&#8217;t rescan the working directory for changes after the tool finishes execution. </p>
 </dd></dl>
<p> guitool.&lt;name&gt;.confirm </p>
<dl>
<dd> <p> Show a confirmation dialog before actually running the tool. </p>
 </dd></dl>
<p> guitool.&lt;name&gt;.argPrompt </p>
<dl>
<dd> <p> Request a string argument from the user, and pass it to the tool through the <code>ARGS</code> environment variable. Since requesting an argument implies confirmation, the <i>confirm</i> option has no effect if this is enabled. If the option is set to <i>true</i>, <i>yes</i>, or <i>1</i>, the dialog uses a built-in generic prompt; otherwise the exact value of the variable is used. </p>
 </dd></dl>
<p> guitool.&lt;name&gt;.revPrompt </p>
<dl>
<dd> <p> Request a single valid revision from the user, and set the <code>REVISION</code> environment variable. In other aspects this option is similar to <i>argPrompt</i>, and can be used together with it. </p>
 </dd></dl>
<p> guitool.&lt;name&gt;.revUnmerged </p>
<dl>
<dd> <p> Show only unmerged branches in the <i>revPrompt</i> subdialog. This is useful for tools similar to merge or rebase, but not for things like checkout or reset. </p>
 </dd></dl>
<p> guitool.&lt;name&gt;.title </p>
<dl>
<dd> <p> Specifies the title to use for the prompt dialog. The default is the tool name. </p>
 </dd></dl>
<p> guitool.&lt;name&gt;.prompt </p>
<dl>
<dd> <p> Specifies the general prompt string to display at the top of the dialog, before subsections for <i>argPrompt</i> and <i>revPrompt</i>. The default value includes the actual command. </p>
 </dd></dl>
<p> help.browser </p>
<dl>
<dd> <p> Specify the browser that will be used to display help in the <i>web</i> format. See <code><a href="/docs/linux/man/1-git-help/">git-help</a></code>(1). </p>
 </dd></dl>
<p> help.format </p>
<dl>
<dd> <p> Override the default help format used by <code><a href="/docs/linux/man/1-git-help/">git-help</a></code>(1). Values <i>man</i>, <i>info</i>, <i>web</i> and <i>html</i> are supported. <i>man</i> is the default. <i>web</i> and <i>html</i> are the same. </p>
 </dd></dl>
<p> help.autoCorrect </p>
<dl>
<dd> <p> If git detects typos and can identify exactly one valid command similar to the error, git will try to suggest the correct command or even run the suggestion automatically. Possible config values are: </p>
 </dd>
<dl>
<dd> <p> &bull; 0 (default): show the suggested command. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; positive number: run the suggested command after specified deciseconds (0.1 sec). </p>
 </dd></dl>
<dl>
<dd> <p> &bull; &quot;immediate&quot;: run the suggested command immediately. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; &quot;prompt&quot;: show the suggestion and prompt for confirmation to run the command. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; &quot;never&quot;: don&#8217;t run or show any suggested command. </p>
 </dd></dl>
</dl>
<p> help.htmlPath </p>
<dl>
<dd> <p> Specify the path where the HTML documentation resides. File system paths and URLs are supported. HTML pages will be prefixed with this path when help is displayed in the <i>web</i> format. This defaults to the documentation path of your Git installation. </p>
 </dd></dl>
<p> http.proxy </p>
<dl>
<dd> <p> Override the HTTP proxy, normally configured using the <i>http_proxy</i>, <i>https_proxy</i>, and <i>all_proxy</i> environment variables (see <code><a href="/docs/linux/man/1-curl/">curl</a>(1)</code>). In addition to the syntax understood by curl, it is possible to specify a proxy string with a user name but no password, in which case git will attempt to acquire one in the same way it does for other credentials. See <code><a href="/docs/linux/man/7-gitcredentials/">gitcredentials</a></code>(7) for more information. The syntax thus is <i>[protocol://][user[:password]@]proxyhost[:port]</i>. This can be overridden on a per-remote basis; see remote.&lt;name&gt;.proxy </p>
 </dd></dl>
<p> http.proxyAuthMethod </p>
<dl>
<dd> <p> Set the method with which to authenticate against the HTTP proxy. This only takes effect if the configured proxy string contains a user name part (i.e. is of the form <i>user [at] host</i> or <i>user [at] host:port</i>). This can be overridden on a per-remote basis; see <code>remote.&lt;name&gt;.proxyAuthMethod</code>. Both can be overridden by the <code>GIT_HTTP_PROXY_AUTHMETHOD</code> environment variable. Possible values are: </p>
 </dd>
<dl>
<dd> <p> &bull; <code>anyauth</code> - Automatically pick a suitable authentication method. It is assumed that the proxy answers an unauthenticated request with a 407 status code and one or more Proxy-authenticate headers with supported authentication methods. This is the default. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>basic</code> - HTTP Basic authentication </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>digest</code> - HTTP Digest authentication; this prevents the password from being transmitted to the proxy in clear text </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>negotiate</code> - GSS-Negotiate authentication (compare the --negotiate option of <code><a href="/docs/linux/man/1-curl/">curl</a>(1)</code>) </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>ntlm</code> - NTLM authentication (compare the --ntlm option of <code><a href="/docs/linux/man/1-curl/">curl</a>(1)</code>) </p>
 </dd></dl>
</dl>
<p> http.proxySSLCert </p>
<dl>
<dd> <p> The pathname of a file that stores a client certificate to use to authenticate with an HTTPS proxy. Can be overridden by the <code>GIT_PROXY_SSL_CERT</code> environment variable. </p>
 </dd></dl>
<p> http.proxySSLKey </p>
<dl>
<dd> <p> The pathname of a file that stores a private key to use to authenticate with an HTTPS proxy. Can be overridden by the <code>GIT_PROXY_SSL_KEY</code> environment variable. </p>
 </dd></dl>
<p> http.proxySSLCertPasswordProtected </p>
<dl>
<dd> <p> Enable Git&#8217;s password prompt for the proxy SSL certificate. Otherwise OpenSSL will prompt the user, possibly many times, if the certificate or private key is encrypted. Can be overridden by the <code>GIT_PROXY_SSL_CERT_PASSWORD_PROTECTED</code> environment variable. </p>
 </dd></dl>
<p> http.proxySSLCAInfo </p>
<dl>
<dd> <p> Pathname to the file containing the certificate bundle that should be used to verify the proxy with when using an HTTPS proxy. Can be overridden by the <code>GIT_PROXY_SSL_CAINFO</code> environment variable. </p>
 </dd></dl>
<p> http.emptyAuth </p>
<dl>
<dd> <p> Attempt authentication without seeking a username or password. This can be used to attempt GSS-Negotiate authentication without specifying a username in the URL, as libcurl normally requires a username for authentication. </p>
 </dd></dl>
<p> http.delegation </p>
<dl>
<dd> <p> Control GSSAPI credential delegation. The delegation is disabled by default in libcurl since version 7.21.7. Set parameter to tell the server what it is allowed to delegate when it comes to user credentials. Used with GSS/kerberos. Possible values are: </p>
 </dd>
<dl>
<dd> <p> &bull; <code>none</code> - Don&#8217;t allow any delegation. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>policy</code> - Delegates if and only if the OK-AS-DELEGATE flag is set in the Kerberos service ticket, which is a matter of realm policy. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>always</code> - Unconditionally allow the server to delegate. </p>
 </dd></dl>
</dl>
<p> http.extraHeader </p>
<dl>
<dd> <p> Pass an additional HTTP header when communicating with a server. If more than one such entry exists, all of them are added as extra headers. To allow overriding the settings inherited from the system config, an empty value will reset the extra headers to the empty list. </p>
 </dd></dl>
<p> http.cookieFile </p>
<dl>
<dd> <p> The pathname of a file containing previously stored cookie lines, which should be used in the Git http session, if they match the server. The file format of the file to read cookies from should be plain HTTP headers or the Netscape/Mozilla cookie file format (see <code><a href="/docs/linux/man/1-curl/">curl</a>(1)</code>). NOTE that the file specified with http.cookieFile is used only as input unless http.saveCookies is set. </p>
 </dd></dl>
<p> http.saveCookies </p>
<dl>
<dd> <p> If set, store cookies received during requests to the file specified by http.cookieFile. Has no effect if http.cookieFile is unset. </p>
 </dd></dl>
<p> http.version </p>
<dl>
<dd> <p> Use the specified HTTP protocol version when communicating with a server. If you want to force the default. The available and default version depend on libcurl. Currently the possible values of this option are: </p>
 </dd>
<dl>
<dd> <p> &bull; HTTP/2 </p>
 </dd></dl>
<dl>
<dd> <p> &bull; HTTP/1.1 </p>
 </dd></dl>
</dl>
<p> http.sslVersion </p>
<dl>
<dd> <p> The SSL version to use when negotiating an SSL connection, if you want to force the default. The available and default version depend on whether libcurl was built against NSS or OpenSSL and the particular configuration of the crypto library in use. Internally this sets the <i>CURLOPT_SSL_VERSION</i> option; see the libcurl documentation for more details on the format of this option and for the ssl version supported. Currently the possible values of this option are: </p>
 </dd>
<dl>
<dd> <p> &bull; sslv2 </p>
 </dd></dl>
<dl>
<dd> <p> &bull; sslv3 </p>
 </dd></dl>
<dl>
<dd> <p> &bull; tlsv1 </p>
 </dd></dl>
<dl>
<dd> <p> &bull; tlsv1.0 </p>
 </dd></dl>
<dl>
<dd> <p> &bull; tlsv1.1 </p>
 </dd></dl>
<dl>
<dd> <p> &bull; tlsv1.2 </p>
 </dd></dl>
<dl>
<dd> <p> &bull; tlsv1.3 </p>
 </dd></dl>
<p> Can be overridden by the <code>GIT_SSL_VERSION</code> environment variable. To force git to use libcurl&#8217;s default ssl version and ignore any explicit http.sslversion option, set <code>GIT_SSL_VERSION</code> to the empty string. </dl>
 </p>
<p> http.sslCipherList </p>
<dl>
<dd> <p> A list of SSL ciphers to use when negotiating an SSL connection. The available ciphers depend on whether libcurl was built against NSS or OpenSSL and the particular configuration of the crypto library in use. Internally this sets the <i>CURLOPT_SSL_CIPHER_LIST</i> option; see the libcurl documentation for more details on the format of this list. </p>
<p> Can be overridden by the <code>GIT_SSL_CIPHER_LIST</code> environment variable. To force git to use libcurl&#8217;s default cipher list and ignore any explicit http.sslCipherList option, set <code>GIT_SSL_CIPHER_LIST</code> to the empty string. </p>
 </dd></dl>
<p> http.sslVerify </p>
<dl>
<dd> <p> Whether to verify the SSL certificate when fetching or pushing over HTTPS. Defaults to true. Can be overridden by the <code>GIT_SSL_NO_VERIFY</code> environment variable. </p>
 </dd></dl>
<p> http.sslCert </p>
<dl>
<dd> <p> File containing the SSL certificate when fetching or pushing over HTTPS. Can be overridden by the <code>GIT_SSL_CERT</code> environment variable. </p>
 </dd></dl>
<p> http.sslKey </p>
<dl>
<dd> <p> File containing the SSL private key when fetching or pushing over HTTPS. Can be overridden by the <code>GIT_SSL_KEY</code> environment variable. </p>
 </dd></dl>
<p> http.sslCertPasswordProtected </p>
<dl>
<dd> <p> Enable Git&#8217;s password prompt for the SSL certificate. Otherwise OpenSSL will prompt the user, possibly many times, if the certificate or private key is encrypted. Can be overridden by the <code>GIT_SSL_CERT_PASSWORD_PROTECTED</code> environment variable. </p>
 </dd></dl>
<p> http.sslCAInfo </p>
<dl>
<dd> <p> File containing the certificates to verify the peer with when fetching or pushing over HTTPS. Can be overridden by the <code>GIT_SSL_CAINFO</code> environment variable. </p>
 </dd></dl>
<p> http.sslCAPath </p>
<dl>
<dd> <p> Path containing files with the CA certificates to verify the peer with when fetching or pushing over HTTPS. Can be overridden by the <code>GIT_SSL_CAPATH</code> environment variable. </p>
 </dd></dl>
<p> http.sslBackend </p>
<dl>
<dd> <p> Name of the SSL backend to use (e.g. &quot;openssl&quot; or &quot;schannel&quot;). This option is ignored if cURL lacks support for choosing the SSL backend at runtime. </p>
 </dd></dl>
<p> http.schannelCheckRevoke </p>
<dl>
<dd> <p> Used to enforce or disable certificate revocation checks in cURL when http.sslBackend is set to &quot;schannel&quot;. Defaults to <code>true</code> if unset. Only necessary to disable this if Git consistently errors and the message is about checking the revocation status of a certificate. This option is ignored if cURL lacks support for setting the relevant SSL option at runtime. </p>
 </dd></dl>
<p> http.schannelUseSSLCAInfo </p>
<dl>
<dd> <p> As of cURL v7.60.0, the Secure Channel backend can use the certificate bundle provided via <code>http.sslCAInfo</code>, but that would override the Windows Certificate Store. Since this is not desirable by default, Git will tell cURL not to use that bundle by default when the <code>schannel</code> backend was configured via <code>http.sslBackend</code>, unless <code>http.schannelUseSSLCAInfo</code> overrides this behavior. </p>
 </dd></dl>
<p> http.pinnedpubkey </p>
<dl>
<dd> <p> Public key of the https service. It may either be the filename of a PEM or DER encoded public key file or a string starting with <i>sha256//</i> followed by the base64 encoded sha256 hash of the public key. See also libcurl <i>CURLOPT_PINNEDPUBLICKEY</i>. git will exit with an error if this option is set but not supported by cURL. </p>
 </dd></dl>
<p> http.sslTry </p>
<dl>
<dd> <p> Attempt to use AUTH SSL/TLS and encrypted data transfers when connecting via regular FTP protocol. This might be needed if the FTP server requires it for security reasons or you wish to connect securely whenever remote FTP server supports it. Default is false since it might trigger certificate verification errors on misconfigured servers. </p>
 </dd></dl>
<p> http.maxRequests </p>
<dl>
<dd> <p> How many HTTP requests to launch in parallel. Can be overridden by the <code>GIT_HTTP_MAX_REQUESTS</code> environment variable. Default is 5. </p>
 </dd></dl>
<p> http.minSessions </p>
<dl>
<dd> <p> The number of curl sessions (counted across slots) to be kept across requests. They will not be ended with curl_easy_cleanup() until http_cleanup() is invoked. If USE_CURL_MULTI is not defined, this value will be capped at 1. Defaults to 1. </p>
 </dd></dl>
<p> http.postBuffer </p>
<dl>
<dd> <p> Maximum size in bytes of the buffer used by smart HTTP transports when POSTing data to the remote system. For requests larger than this buffer size, HTTP/1.1 and Transfer-Encoding: chunked is used to avoid creating a massive pack file locally. Default is 1 MiB, which is sufficient for most requests. </p>
<p> Note that raising this limit is only effective for disabling chunked transfer encoding and therefore should be used only where the remote server or a proxy only supports HTTP/1.0 or is noncompliant with the HTTP standard. Raising this is not, in general, an effective solution for most push problems, but can increase memory consumption significantly since the entire buffer is allocated even for small pushes. </p>
 </dd></dl>
<p> http.lowSpeedLimit, http.lowSpeedTime </p>
<dl>
<dd> <p> If the HTTP transfer speed is less than <i>http.lowSpeedLimit</i> for longer than <i>http.lowSpeedTime</i> seconds, the transfer is aborted. Can be overridden by the <code>GIT_HTTP_LOW_SPEED_LIMIT</code> and <code>GIT_HTTP_LOW_SPEED_TIME</code> environment variables. </p>
 </dd></dl>
<p> http.noEPSV </p>
<dl>
<dd> <p> A boolean which disables using of EPSV ftp command by curl. This can helpful with some &quot;poor&quot; ftp servers which don&#8217;t support EPSV mode. Can be overridden by the <code>GIT_CURL_FTP_NO_EPSV</code> environment variable. Default is false (curl will use EPSV). </p>
 </dd></dl>
<p> http.userAgent </p>
<dl>
<dd> <p> The HTTP USER_AGENT string presented to an HTTP server. The default value represents the version of the client Git such as git/1.7.1. This option allows you to override this value to a more common value such as Mozilla/4.0. This may be necessary, for instance, if connecting through a firewall that restricts HTTP connections to a set of common USER_AGENT strings (but not including those like git/1.7.1). Can be overridden by the <code>GIT_HTTP_USER_AGENT</code> environment variable. </p>
 </dd></dl>
<p> http.followRedirects </p>
<dl>
<dd> <p> Whether git should follow HTTP redirects. If set to <code>true</code>, git will transparently follow any redirect issued by a server it encounters. If set to <code>false</code>, git will treat all redirects as errors. If set to <code>initial</code>, git will follow redirects only for the initial request to a remote, but not for subsequent follow-up HTTP requests. Since git uses the redirected URL as the base for the follow-up requests, this is generally sufficient. The default is <code>initial</code>. </p>
 </dd></dl>
<p> http.&lt;url&gt;.* </p>
<dl>
<dd> <p> Any of the http.* options above can be applied selectively to some URLs. For a config key to match a URL, each element of the config key is compared to that of the URL, in the following order: </p>
 </dd>
<dl>
<dd> <p> 1. Scheme (e.g., <code>https</code> in <code><a rel="nofollow" href="https://example.com/">https://example.com/</a></code>). This field must match exactly between the config key and the URL. </p>
 </dd></dl>
<dl>
<dd> <p> 2. Host/domain name (e.g., <code>example.com</code> in <code><a rel="nofollow" href="https://example.com/">https://example.com/</a></code>). This field must match between the config key and the URL. It is possible to specify a <code>*</code> as part of the host name to match all subdomains at this level. <code><a rel="nofollow" href="https://*.example.com/">https://*.example.com/</a></code> for example would match <code><a rel="nofollow" href="https://foo.example.com/">https://foo.example.com/</a></code>, but not <code><a rel="nofollow" href="https://foo.bar.example.com/">https://foo.bar.example.com/</a></code>. </p>
 </dd></dl>
<dl>
<dd> <p> 3. Port number (e.g., <code>8080</code> in <code><a rel="nofollow" href="http://example.com:8080/">http://example.com:8080/</a></code>). This field must match exactly between the config key and the URL. Omitted port numbers are automatically converted to the correct default for the scheme before matching. </p>
 </dd></dl>
<dl>
<dd> <p> 4. Path (e.g., <code>repo.git</code> in <code><a rel="nofollow" href="https://example.com/repo.git">https://example.com/repo.git</a></code>). The path field of the config key must match the path field of the URL either exactly or as a prefix of slash-delimited path elements. This means a config key with path <code>foo/</code> matches URL path <code>foo/bar</code>. A prefix can only match on a slash (<code>/</code>) boundary. Longer matches take precedence (so a config key with path <code>foo/bar</code> is a better match to URL path <code>foo/bar</code> than a config key with just path <code>foo/</code>). </p>
 </dd></dl>
<dl>
<dd> <p> 5. User name (e.g., <code>user</code> in <code><a rel="nofollow" href="https://user@example.com/repo.git">https://user@example.com/repo.git</a></code>). If the config key has a user name it must match the user name in the URL exactly. If the config key does not have a user name, that config key will match a URL with any user name (including none), but at a lower precedence than a config key with a user name. </p>
 </dd></dl>
<p> The list above is ordered by decreasing precedence; a URL that matches a config key&#8217;s path is preferred to one that matches its user name. For example, if the URL is <code><a rel="nofollow" href="https://user@example.com/foo/bar">https://user@example.com/foo/bar</a></code> a config key match of <code><a rel="nofollow" href="https://example.com/foo">https://example.com/foo</a></code> will be preferred over a config key match of <code><a rel="nofollow" href="https://user@example.com">https://user@example.com</a></code>. </p>
<p> All URLs are normalized before attempting any matching (the password part, if embedded in the URL, is always ignored for matching purposes) so that equivalent URLs that are simply spelled differently will match properly. Environment variable settings always override any matches. The URLs that are matched against are those given directly to Git commands. This means any URLs visited as a result of a redirection do not participate in matching. </dl>
 </p>
<p> i18n.commitEncoding </p>
<dl>
<dd> <p> Character encoding the commit messages are stored in; Git itself does not care per se, but this information is necessary e.g. when importing commits from emails or in the gitk graphical history browser (and possibly at other places in the future or in other porcelains). See e.g. <code><a href="/docs/linux/man/1-git-mailinfo/">git-mailinfo</a></code>(1). Defaults to <i>utf-8</i>. </p>
 </dd></dl>
<p> i18n.logOutputEncoding </p>
<dl>
<dd> <p> Character encoding the commit messages are converted to when running <i>git log</i> and friends. </p>
 </dd></dl>
<p> imap.folder </p>
<dl>
<dd> <p> The folder to drop the mails into, which is typically the Drafts folder. For example: &quot;INBOX.Drafts&quot;, &quot;INBOX/Drafts&quot; or &quot;[Gmail]/Drafts&quot;. Required. </p>
 </dd></dl>
<p> imap.tunnel </p>
<dl>
<dd> <p> Command used to setup a tunnel to the IMAP server through which commands will be piped instead of using a direct network connection to the server. Required when imap.host is not set. </p>
 </dd></dl>
<p> imap.host </p>
<dl>
<dd> <p> A URL identifying the server. Use an <code>imap://</code> prefix for non-secure connections and an <code>imaps://</code> prefix for secure connections. Ignored when imap.tunnel is set, but required otherwise. </p>
 </dd></dl>
<p> imap.user </p>
<dl>
<dd> <p> The username to use when logging in to the server. </p>
 </dd></dl>
<p> imap.pass </p>
<dl>
<dd> <p> The password to use when logging in to the server. </p>
 </dd></dl>
<p> imap.port </p>
<dl>
<dd> <p> An integer port number to connect to on the server. Defaults to 143 for imap:// hosts and 993 for imaps:// hosts. Ignored when imap.tunnel is set. </p>
 </dd></dl>
<p> imap.sslverify </p>
<dl>
<dd> <p> A boolean to enable/disable verification of the server certificate used by the SSL/TLS connection. Default is <code>true</code>. Ignored when imap.tunnel is set. </p>
 </dd></dl>
<p> imap.preformattedHTML </p>
<dl>
<dd> <p> A boolean to enable/disable the use of html encoding when sending a patch. An html encoded patch will be bracketed with &lt;pre&gt; and have a content type of text/html. Ironically, enabling this option causes Thunderbird to send the patch as a plain/text, format=fixed email. Default is <code>false</code>. </p>
 </dd></dl>
<p> imap.authMethod </p>
<dl>
<dd> <p> Specify authenticate method for authentication with IMAP server. If Git was built with the NO_CURL option, or if your curl version is older than 7.34.0, or if you&#8217;re running git-imap-send with the <code>--no-curl</code> option, the only supported method is <i>CRAM-MD5</i>. If this is not set then <i>git imap-send</i> uses the basic IMAP plaintext LOGIN command. </p>
 </dd></dl>
<p> index.recordEndOfIndexEntries </p>
<dl>
<dd> <p> Specifies whether the index file should include an &quot;End Of Index Entry&quot; section. This reduces index load time on multiprocessor machines but produces a message &quot;ignoring EOIE extension&quot; when reading the index using Git versions before 2.20. Defaults to <i>true</i> if index.threads has been explicitly enabled, <i>false</i> otherwise. </p>
 </dd></dl>
<p> index.recordOffsetTable </p>
<dl>
<dd> <p> Specifies whether the index file should include an &quot;Index Entry Offset Table&quot; section. This reduces index load time on multiprocessor machines but produces a message &quot;ignoring IEOT extension&quot; when reading the index using Git versions before 2.20. Defaults to <i>true</i> if index.threads has been explicitly enabled, <i>false</i> otherwise. </p>
 </dd></dl>
<p> index.sparse </p>
<dl>
<dd> <p> When enabled, write the index using sparse-directory entries. This has no effect unless <code>core.sparseCheckout</code> and <code>core.sparseCheckoutCone</code> are both enabled. Defaults to <i>false</i>. </p>
 </dd></dl>
<p> index.threads </p>
<dl>
<dd> <p> Specifies the number of threads to spawn when loading the index. This is meant to reduce index load time on multiprocessor machines. Specifying 0 or <i>true</i> will cause Git to auto-detect the number of CPU&#8217;s and set the number of threads accordingly. Specifying 1 or <i>false</i> will disable multithreading. Defaults to <i>true</i>. </p>
 </dd></dl>
<p> index.version </p>
<dl>
<dd> <p> Specify the version with which new index files should be initialized. This does not affect existing repositories. If <code>feature.manyFiles</code> is enabled, then the default is 4. </p>
 </dd></dl>
<p> init.templateDir </p>
<dl>
<dd> <p> Specify the directory from which templates will be copied. (See the &quot;TEMPLATE DIRECTORY&quot; section of <code><a href="/docs/linux/man/1-git-init/">git-init</a></code>(1).) </p>
 </dd></dl>
<p> init.defaultBranch </p>
<dl>
<dd> <p> Allows overriding the default branch name e.g. when initializing a new repository. </p>
 </dd></dl>
<p> instaweb.browser </p>
<dl>
<dd> <p> Specify the program that will be used to browse your working repository in gitweb. See <code><a href="/docs/linux/man/1-git-instaweb/">git-instaweb</a></code>(1). </p>
 </dd></dl>
<p> instaweb.httpd </p>
<dl>
<dd> <p> The HTTP daemon command-line to start gitweb on your working repository. See <code><a href="/docs/linux/man/1-git-instaweb/">git-instaweb</a></code>(1). </p>
 </dd></dl>
<p> instaweb.local </p>
<dl>
<dd> <p> If true the web server started by <code><a href="/docs/linux/man/1-git-instaweb/">git-instaweb</a></code>(1) will be bound to the local IP (127.0.0.1). </p>
 </dd></dl>
<p> instaweb.modulePath </p>
<dl>
<dd> <p> The default module path for <code><a href="/docs/linux/man/1-git-instaweb/">git-instaweb</a></code>(1) to use instead of /usr/lib/apache2/modules. Only used if httpd is Apache. </p>
 </dd></dl>
<p> instaweb.port </p>
<dl>
<dd> <p> The port number to bind the gitweb httpd to. See <code><a href="/docs/linux/man/1-git-instaweb/">git-instaweb</a></code>(1). </p>
 </dd></dl>
<p> interactive.singleKey </p>
<dl>
<dd> <p> In interactive commands, allow the user to provide one-letter input with a single key (i.e., without hitting enter). Currently this is used by the <code>--patch</code> mode of <code><a href="/docs/linux/man/1-git-add/">git-add</a></code>(1), <code><a href="/docs/linux/man/1-git-checkout/">git-checkout</a></code>(1), <code><a href="/docs/linux/man/1-git-restore/">git-restore</a></code>(1), <code><a href="/docs/linux/man/1-git-commit/">git-commit</a></code>(1), <code><a href="/docs/linux/man/1-git-reset/">git-reset</a></code>(1), and <code><a href="/docs/linux/man/1-git-stash/">git-stash</a></code>(1). Note that this setting is silently ignored if portable keystroke input is not available; requires the Perl module Term::ReadKey. </p>
 </dd></dl>
<p> interactive.diffFilter </p>
<dl>
<dd> <p> When an interactive command (such as <code>git add --patch</code>) shows a colorized diff, git will pipe the diff through the shell command defined by this configuration variable. The command may mark up the diff further for human consumption, provided that it retains a one-to-one correspondence with the lines in the original diff. Defaults to disabled (no filtering). </p>
 </dd></dl>
<p> log.abbrevCommit </p>
<dl>
<dd> <p> If true, makes <code><a href="/docs/linux/man/1-git-log/">git-log</a></code>(1), <code><a href="/docs/linux/man/1-git-show/">git-show</a></code>(1), and <code><a href="/docs/linux/man/1-git-whatchanged/">git-whatchanged</a></code>(1) assume <code>--abbrev-commit</code>. You may override this option with <code>--no-abbrev-commit</code>. </p>
 </dd></dl>
<p> log.date </p>
<dl>
<dd> <p> Set the default date-time mode for the <i>log</i> command. Setting a value for log.date is similar to using <i>git log</i>&#8216;s <code>--date</code> option. See <code><a href="/docs/linux/man/1-git-log/">git-log</a></code>(1) for details. </p>
 </dd></dl>
<p> log.decorate </p>
<dl>
<dd> <p> Print out the ref names of any commits that are shown by the log command. If <i>short</i> is specified, the ref name prefixes <i>refs/heads/</i>, <i>refs/tags/</i> and <i>refs/remotes/</i> will not be printed. If <i>full</i> is specified, the full ref name (including prefix) will be printed. If <i>auto</i> is specified, then if the output is going to a terminal, the ref names are shown as if <i>short</i> were given, otherwise no ref names are shown. This is the same as the <code>--decorate</code> option of the <code>git log</code>. </p>
 </dd></dl>
<p> log.excludeDecoration </p>
<dl>
<dd> <p> Exclude the specified patterns from the log decorations. This is similar to the <code>--decorate-refs-exclude</code> command-line option, but the config option can be overridden by the <code>--decorate-refs</code> option. </p>
 </dd></dl>
<p> log.diffMerges </p>
<dl>
<dd> <p> Set default diff format to be used for merge commits. See <code>--diff-merges</code> in <code><a href="/docs/linux/man/1-git-log/">git-log</a></code>(1) for details. Defaults to <code>separate</code>. </p>
 </dd></dl>
<p> log.follow </p>
<dl>
<dd> <p> If <code>true</code>, <code>git log</code> will act as if the <code>--follow</code> option was used when a single &lt;path&gt; is given. This has the same limitations as <code>--follow</code>, i.e. it cannot be used to follow multiple files and does not work well on non-linear history. </p>
 </dd></dl>
<p> log.graphColors </p>
<dl>
<dd> <p> A list of colors, separated by commas, that can be used to draw history lines in <code>git log --graph</code>. </p>
 </dd></dl>
<p> log.showRoot </p>
<dl>
<dd> <p> If true, the initial commit will be shown as a big creation event. This is equivalent to a diff against an empty tree. Tools like <code><a href="/docs/linux/man/1-git-log/">git-log</a></code>(1) or <code><a href="/docs/linux/man/1-git-whatchanged/">git-whatchanged</a></code>(1), which normally hide the root commit will now show it. True by default. </p>
 </dd></dl>
<p> log.showSignature </p>
<dl>
<dd> <p> If true, makes <code><a href="/docs/linux/man/1-git-log/">git-log</a></code>(1), <code><a href="/docs/linux/man/1-git-show/">git-show</a></code>(1), and <code><a href="/docs/linux/man/1-git-whatchanged/">git-whatchanged</a></code>(1) assume <code>--show-signature</code>. </p>
 </dd></dl>
<p> log.mailmap </p>
<dl>
<dd> <p> If true, makes <code><a href="/docs/linux/man/1-git-log/">git-log</a></code>(1), <code><a href="/docs/linux/man/1-git-show/">git-show</a></code>(1), and <code><a href="/docs/linux/man/1-git-whatchanged/">git-whatchanged</a></code>(1) assume <code>--use-mailmap</code>, otherwise assume <code>--no-use-mailmap</code>. True by default. </p>
 </dd></dl>
<p> lsrefs.unborn </p>
<dl>
<dd> <p> May be &quot;advertise&quot; (the default), &quot;allow&quot;, or &quot;ignore&quot;. If &quot;advertise&quot;, the server will respond to the client sending &quot;unborn&quot; (as described in protocol-v2.txt) and will advertise support for this feature during the protocol v2 capability advertisement. &quot;allow&quot; is the same as &quot;advertise&quot; except that the server will not advertise support for this feature; this is useful for load-balanced servers that cannot be updated atomically (for example), since the administrator could configure &quot;allow&quot;, then after a delay, configure &quot;advertise&quot;. </p>
 </dd></dl>
<p> mailinfo.scissors </p>
<dl>
<dd> <p> If true, makes <code><a href="/docs/linux/man/1-git-mailinfo/">git-mailinfo</a></code>(1) (and therefore <code><a href="/docs/linux/man/1-git-am/">git-am</a></code>(1)) act by default as if the --scissors option was provided on the command-line. When active, this features removes everything from the message body before a scissors line (i.e. consisting mainly of &quot;&gt;8&quot;, &quot;8&lt;&quot; and &quot;-&quot;). </p>
 </dd></dl>
<p> mailmap.file </p>
<dl>
<dd> <p> The location of an augmenting mailmap file. The default mailmap, located in the root of the repository, is loaded first, then the mailmap file pointed to by this variable. The location of the mailmap file may be in a repository subdirectory, or somewhere outside of the repository itself. See <code><a href="/docs/linux/man/1-git-shortlog/">git-shortlog</a></code>(1) and <code><a href="/docs/linux/man/1-git-blame/">git-blame</a></code>(1). </p>
 </dd></dl>
<p> mailmap.blob </p>
<dl>
<dd> <p> Like <code>mailmap.file</code>, but consider the value as a reference to a blob in the repository. If both <code>mailmap.file</code> and <code>mailmap.blob</code> are given, both are parsed, with entries from <code>mailmap.file</code> taking precedence. In a bare repository, this defaults to <code>HEAD:.mailmap</code>. In a non-bare repository, it defaults to empty. </p>
 </dd></dl>
<p> maintenance.auto </p>
<dl>
<dd> <p> This boolean config option controls whether some commands run <code>git maintenance run --auto</code> after doing their normal work. Defaults to true. </p>
 </dd></dl>
<p> maintenance.strategy </p>
<dl>
<dd> <p> This string config option provides a way to specify one of a few recommended schedules for background maintenance. This only affects which tasks are run during <code>git maintenance run --schedule=X</code> commands, provided no <code>--task=&lt;task&gt;</code> arguments are provided. Further, if a <code>maintenance.&lt;task&gt;.schedule</code> config value is set, then that value is used instead of the one provided by <code>maintenance.strategy</code>. The possible strategy strings are: </p>
 </dd>
<dl>
<dd> <p> &bull; <code>none</code>: This default setting implies no task are run at any schedule. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>incremental</code>: This setting optimizes for performing small maintenance activities that do not delete any data. This does not schedule the <code>gc</code> task, but runs the <code>prefetch</code> and <code>commit-graph</code> tasks hourly, the <code>loose-objects</code> and <code>incremental-repack</code> tasks daily, and the <code>pack-refs</code> task weekly. </p>
 </dd></dl>
</dl>
<p> maintenance.&lt;task&gt;.enabled </p>
<dl>
<dd> <p> This boolean config option controls whether the maintenance task with name <code>&lt;task&gt;</code> is run when no <code>--task</code> option is specified to <code>git maintenance run</code>. These config values are ignored if a <code>--task</code> option exists. By default, only <code>maintenance.gc.enabled</code> is true. </p>
 </dd></dl>
<p> maintenance.&lt;task&gt;.schedule </p>
<dl>
<dd> <p> This config option controls whether or not the given <code>&lt;task&gt;</code> runs during a <code>git maintenance run --schedule=&lt;frequency&gt;</code> command. The value must be one of &quot;hourly&quot;, &quot;daily&quot;, or &quot;weekly&quot;. </p>
 </dd></dl>
<p> maintenance.commit-graph.auto </p>
<dl>
<dd> <p> This integer config option controls how often the <code>commit-graph</code> task should be run as part of <code>git maintenance run --auto</code>. If zero, then the <code>commit-graph</code> task will not run with the <code>--auto</code> option. A negative value will force the task to run every time. Otherwise, a positive value implies the command should run when the number of reachable commits that are not in the commit-graph file is at least the value of <code>maintenance.commit-graph.auto</code>. The default value is 100. </p>
 </dd></dl>
<p> maintenance.loose-objects.auto </p>
<dl>
<dd> <p> This integer config option controls how often the <code>loose-objects</code> task should be run as part of <code>git maintenance run --auto</code>. If zero, then the <code>loose-objects</code> task will not run with the <code>--auto</code> option. A negative value will force the task to run every time. Otherwise, a positive value implies the command should run when the number of loose objects is at least the value of <code>maintenance.loose-objects.auto</code>. The default value is 100. </p>
 </dd></dl>
<p> maintenance.incremental-repack.auto </p>
<dl>
<dd> <p> This integer config option controls how often the <code>incremental-repack</code> task should be run as part of <code>git maintenance run --auto</code>. If zero, then the <code>incremental-repack</code> task will not run with the <code>--auto</code> option. A negative value will force the task to run every time. Otherwise, a positive value implies the command should run when the number of pack-files not in the multi-pack-index is at least the value of <code>maintenance.incremental-repack.auto</code>. The default value is 10. </p>
 </dd></dl>
<p> man.viewer </p>
<dl>
<dd> <p> Specify the programs that may be used to display help in the <i>man</i> format. See <code><a href="/docs/linux/man/1-git-help/">git-help</a></code>(1). </p>
 </dd></dl>
<p> man.&lt;tool&gt;.cmd </p>
<dl>
<dd> <p> Specify the command to invoke the specified man viewer. The specified command is evaluated in shell with the man page passed as argument. (See <code><a href="/docs/linux/man/1-git-help/">git-help</a></code>(1).) </p>
 </dd></dl>
<p> man.&lt;tool&gt;.path </p>
<dl>
<dd> <p> Override the path for the given tool that may be used to display help in the <i>man</i> format. See <code><a href="/docs/linux/man/1-git-help/">git-help</a></code>(1). </p>
 </dd></dl>
<p> merge.conflictStyle </p>
<dl>
<dd> <p> Specify the style in which conflicted hunks are written out to working tree files upon merge. The default is &quot;merge&quot;, which shows a <code>&lt;&lt;&lt;&lt;&lt;&lt;&lt;</code> conflict marker, changes made by one side, a <code>=======</code> marker, changes made by the other side, and then a <code>&gt;&gt;&gt;&gt;&gt;&gt;&gt;</code> marker. An alternate style, &quot;diff3&quot;, adds a <code>|||||||</code> marker and the original text before the <code>=======</code> marker. </p>
 </dd></dl>
<p> merge.defaultToUpstream </p>
<dl>
<dd> <p> If merge is called without any commit argument, merge the upstream branches configured for the current branch by using their last observed values stored in their remote-tracking branches. The values of the <code>branch.&lt;current branch&gt;.merge</code> that name the branches at the remote named by <code>branch.&lt;current branch&gt;.remote</code> are consulted, and then they are mapped via <code>remote.&lt;remote&gt;.fetch</code> to their corresponding remote-tracking branches, and the tips of these tracking branches are merged. Defaults to true. </p>
 </dd></dl>
<p> merge.ff </p>
<dl>
<dd> <p> By default, Git does not create an extra merge commit when merging a commit that is a descendant of the current commit. Instead, the tip of the current branch is fast-forwarded. When set to <code>false</code>, this variable tells Git to create an extra merge commit in such a case (equivalent to giving the <code>--no-ff</code> option from the command line). When set to <code>only</code>, only such fast-forward merges are allowed (equivalent to giving the <code>--ff-only</code> option from the command line). </p>
 </dd></dl>
<p> merge.verifySignatures </p>
<dl>
<dd> <p> If true, this is equivalent to the --verify-signatures command line option. See <code><a href="/docs/linux/man/1-git-merge/">git-merge</a></code>(1) for details. </p>
 </dd></dl>
<p> merge.branchdesc </p>
<dl>
<dd> <p> In addition to branch names, populate the log message with the branch description text associated with them. Defaults to false. </p>
 </dd></dl>
<p> merge.log </p>
<dl>
<dd> <p> In addition to branch names, populate the log message with at most the specified number of one-line descriptions from the actual commits that are being merged. Defaults to false, and true is a synonym for 20. </p>
 </dd></dl>
<p> merge.suppressDest </p>
<dl>
<dd> <p> By adding a glob that matches the names of integration branches to this multi-valued configuration variable, the default merge message computed for merges into these integration branches will omit &quot;into &lt;branch name&gt;&quot; from its title. </p>
<p> An element with an empty value can be used to clear the list of globs accumulated from previous configuration entries. When there is no <code>merge.suppressDest</code> variable defined, the default value of <code>master</code> is used for backward compatibility. </p>
 </dd></dl>
<p> merge.renameLimit </p>
<dl>
<dd> <p> The number of files to consider in the exhaustive portion of rename detection during a merge. If not specified, defaults to the value of diff.renameLimit. If neither merge.renameLimit nor diff.renameLimit are specified, currently defaults to 7000. This setting has no effect if rename detection is turned off. </p>
 </dd></dl>
<p> merge.renames </p>
<dl>
<dd> <p> Whether Git detects renames. If set to &quot;false&quot;, rename detection is disabled. If set to &quot;true&quot;, basic rename detection is enabled. Defaults to the value of diff.renames. </p>
 </dd></dl>
<p> merge.directoryRenames </p>
<dl>
<dd> <p> Whether Git detects directory renames, affecting what happens at merge time to new files added to a directory on one side of history when that directory was renamed on the other side of history. If merge.directoryRenames is set to &quot;false&quot;, directory rename detection is disabled, meaning that such new files will be left behind in the old directory. If set to &quot;true&quot;, directory rename detection is enabled, meaning that such new files will be moved into the new directory. If set to &quot;conflict&quot;, a conflict will be reported for such paths. If merge.renames is false, merge.directoryRenames is ignored and treated as false. Defaults to &quot;conflict&quot;. </p>
 </dd></dl>
<p> merge.renormalize </p>
<dl>
<dd> <p> Tell Git that canonical representation of files in the repository has changed over time (e.g. earlier commits record text files with CRLF line endings, but recent ones use LF line endings). In such a repository, Git can convert the data recorded in commits to a canonical form before performing a merge to reduce unnecessary conflicts. For more information, see section &quot;Merging branches with differing checkin/checkout attributes&quot; in <code><a href="/docs/linux/man/5-gitattributes/">gitattributes</a></code>(5). </p>
 </dd></dl>
<p> merge.stat </p>
<dl>
<dd> <p> Whether to print the diffstat between ORIG_HEAD and the merge result at the end of the merge. True by default. </p>
 </dd></dl>
<p> merge.autoStash </p>
<dl>
<dd> <p> When set to true, automatically create a temporary stash entry before the operation begins, and apply it after the operation ends. This means that you can run merge on a dirty worktree. However, use with care: the final stash application after a successful merge might result in non-trivial conflicts. This option can be overridden by the <code>--no-autostash</code> and <code>--autostash</code> options of <code><a href="/docs/linux/man/1-git-merge/">git-merge</a></code>(1). Defaults to false. </p>
 </dd></dl>
<p> merge.tool </p>
<dl>
<dd> <p> Controls which merge tool is used by <code><a href="/docs/linux/man/1-git-mergetool/">git-mergetool</a></code>(1). The list below shows the valid built-in values. Any other value is treated as a custom merge tool and requires that a corresponding mergetool.&lt;tool&gt;.cmd variable is defined. </p>
 </dd></dl>
<p> merge.guitool </p>
<dl>
<dd> <p> Controls which merge tool is used by <code><a href="/docs/linux/man/1-git-mergetool/">git-mergetool</a></code>(1) when the -g/--gui flag is specified. The list below shows the valid built-in values. Any other value is treated as a custom merge tool and requires that a corresponding mergetool.&lt;guitool&gt;.cmd variable is defined. </p>
 </dd>
<dl>
<dd> <p> &bull; araxis </p>
 </dd></dl>
<dl>
<dd> <p> &bull; bc </p>
 </dd></dl>
<dl>
<dd> <p> &bull; bc3 </p>
 </dd></dl>
<dl>
<dd> <p> &bull; bc4 </p>
 </dd></dl>
<dl>
<dd> <p> &bull; codecompare </p>
 </dd></dl>
<dl>
<dd> <p> &bull; deltawalker </p>
 </dd></dl>
<dl>
<dd> <p> &bull; diffmerge </p>
 </dd></dl>
<dl>
<dd> <p> &bull; diffuse </p>
 </dd></dl>
<dl>
<dd> <p> &bull; ecmerge </p>
 </dd></dl>
<dl>
<dd> <p> &bull; emerge </p>
 </dd></dl>
<dl>
<dd> <p> &bull; examdiff </p>
 </dd></dl>
<dl>
<dd> <p> &bull; guiffy </p>
 </dd></dl>
<dl>
<dd> <p> &bull; gvimdiff </p>
 </dd></dl>
<dl>
<dd> <p> &bull; gvimdiff1 </p>
 </dd></dl>
<dl>
<dd> <p> &bull; gvimdiff2 </p>
 </dd></dl>
<dl>
<dd> <p> &bull; gvimdiff3 </p>
 </dd></dl>
<dl>
<dd> <p> &bull; kdiff3 </p>
 </dd></dl>
<dl>
<dd> <p> &bull; meld </p>
 </dd></dl>
<dl>
<dd> <p> &bull; nvimdiff </p>
 </dd></dl>
<dl>
<dd> <p> &bull; nvimdiff1 </p>
 </dd></dl>
<dl>
<dd> <p> &bull; nvimdiff2 </p>
 </dd></dl>
<dl>
<dd> <p> &bull; nvimdiff3 </p>
 </dd></dl>
<dl>
<dd> <p> &bull; opendiff </p>
 </dd></dl>
<dl>
<dd> <p> &bull; p4merge </p>
 </dd></dl>
<dl>
<dd> <p> &bull; smerge </p>
 </dd></dl>
<dl>
<dd> <p> &bull; tkdiff </p>
 </dd></dl>
<dl>
<dd> <p> &bull; tortoisemerge </p>
 </dd></dl>
<dl>
<dd> <p> &bull; vimdiff </p>
 </dd></dl>
<dl>
<dd> <p> &bull; vimdiff1 </p>
 </dd></dl>
<dl>
<dd> <p> &bull; vimdiff2 </p>
 </dd></dl>
<dl>
<dd> <p> &bull; vimdiff3 </p>
 </dd></dl>
<dl>
<dd> <p> &bull; winmerge </p>
 </dd></dl>
<dl>
<dd> <p> &bull; xxdiff </p>
 </dd></dl>
</dl>
<p> merge.verbosity </p>
<dl>
<dd> <p> Controls the amount of output shown by the recursive merge strategy. Level 0 outputs nothing except a final error message if conflicts were detected. Level 1 outputs only conflicts, 2 outputs conflicts and file changes. Level 5 and above outputs debugging information. The default is level 2. Can be overridden by the <code>GIT_MERGE_VERBOSITY</code> environment variable. </p>
 </dd></dl>
<p> merge.&lt;driver&gt;.name </p>
<dl>
<dd> <p> Defines a human-readable name for a custom low-level merge driver. See <code><a href="/docs/linux/man/5-gitattributes/">gitattributes</a></code>(5) for details. </p>
 </dd></dl>
<p> merge.&lt;driver&gt;.driver </p>
<dl>
<dd> <p> Defines the command that implements a custom low-level merge driver. See <code><a href="/docs/linux/man/5-gitattributes/">gitattributes</a></code>(5) for details. </p>
 </dd></dl>
<p> merge.&lt;driver&gt;.recursive </p>
<dl>
<dd> <p> Names a low-level merge driver to be used when performing an internal merge between common ancestors. See <code><a href="/docs/linux/man/5-gitattributes/">gitattributes</a></code>(5) for details. </p>
 </dd></dl>
<p> mergetool.&lt;tool&gt;.path </p>
<dl>
<dd> <p> Override the path for the given tool. This is useful in case your tool is not in the PATH. </p>
 </dd></dl>
<p> mergetool.&lt;tool&gt;.cmd </p>
<dl>
<dd> <p> Specify the command to invoke the specified merge tool. The specified command is evaluated in shell with the following variables available: <i>BASE</i> is the name of a temporary file containing the common base of the files to be merged, if available; <i>LOCAL</i> is the name of a temporary file containing the contents of the file on the current branch; <i>REMOTE</i> is the name of a temporary file containing the contents of the file from the branch being merged; <i>MERGED</i> contains the name of the file to which the merge tool should write the results of a successful merge. </p>
 </dd></dl>
<p> mergetool.&lt;tool&gt;.hideResolved </p>
<dl>
<dd> <p> Allows the user to override the global <code>mergetool.hideResolved</code> value for a specific tool. See <code>mergetool.hideResolved</code> for the full description. </p>
 </dd></dl>
<p> mergetool.&lt;tool&gt;.trustExitCode </p>
<dl>
<dd> <p> For a custom merge command, specify whether the exit code of the merge command can be used to determine whether the merge was successful. If this is not set to true then the merge target file timestamp is checked and the merge assumed to have been successful if the file has been updated, otherwise the user is prompted to indicate the success of the merge. </p>
 </dd></dl>
<p> mergetool.meld.hasOutput </p>
<dl>
<dd> <p> Older versions of <code>meld</code> do not support the <code>--output</code> option. Git will attempt to detect whether <code>meld</code> supports <code>--output</code> by inspecting the output of <code>meld --help</code>. Configuring <code>mergetool.meld.hasOutput</code> will make Git skip these checks and use the configured value instead. Setting <code>mergetool.meld.hasOutput</code> to <code>true</code> tells Git to unconditionally use the <code>--output</code> option, and <code>false</code> avoids using <code>--output</code>. </p>
 </dd></dl>
<p> mergetool.meld.useAutoMerge </p>
<dl>
<dd> <p> When the <code>--auto-merge</code> is given, meld will merge all non-conflicting parts automatically, highlight the conflicting parts and wait for user decision. Setting <code>mergetool.meld.useAutoMerge</code> to <code>true</code> tells Git to unconditionally use the <code>--auto-merge</code> option with <code>meld</code>. Setting this value to <code>auto</code> makes git detect whether <code>--auto-merge</code> is supported and will only use <code>--auto-merge</code> when available. A value of <code>false</code> avoids using <code>--auto-merge</code> altogether, and is the default value. </p>
 </dd></dl>
<p> mergetool.hideResolved </p>
<dl>
<dd> <p> During a merge Git will automatically resolve as many conflicts as possible and write the <i>MERGED</i> file containing conflict markers around any conflicts that it cannot resolve; <i>LOCAL</i> and <i>REMOTE</i> normally represent the versions of the file from before Git&#8217;s conflict resolution. This flag causes <i>LOCAL</i> and <i>REMOTE</i> to be overwriten so that only the unresolved conflicts are presented to the merge tool. Can be configured per-tool via the <code>mergetool.&lt;tool&gt;.hideResolved</code> configuration variable. Defaults to <code>false</code>. </p>
 </dd></dl>
<p> mergetool.keepBackup </p>
<dl>
<dd> <p> After performing a merge, the original file with conflict markers can be saved as a file with a <code>.orig</code> extension. If this variable is set to <code>false</code> then this file is not preserved. Defaults to <code>true</code> (i.e. keep the backup files). </p>
 </dd></dl>
<p> mergetool.keepTemporaries </p>
<dl>
<dd> <p> When invoking a custom merge tool, Git uses a set of temporary files to pass to the tool. If the tool returns an error and this variable is set to <code>true</code>, then these temporary files will be preserved, otherwise they will be removed after the tool has exited. Defaults to <code>false</code>. </p>
 </dd></dl>
<p> mergetool.writeToTemp </p>
<dl>
<dd> <p> Git writes temporary <i>BASE</i>, <i>LOCAL</i>, and <i>REMOTE</i> versions of conflicting files in the worktree by default. Git will attempt to use a temporary directory for these files when set <code>true</code>. Defaults to <code>false</code>. </p>
 </dd></dl>
<p> mergetool.prompt </p>
<dl>
<dd> <p> Prompt before each invocation of the merge resolution program. </p>
 </dd></dl>
<p> notes.mergeStrategy </p>
<dl>
<dd> <p> Which merge strategy to choose by default when resolving notes conflicts. Must be one of <code>manual</code>, <code>ours</code>, <code>theirs</code>, <code>union</code>, or <code>cat_sort_uniq</code>. Defaults to <code>manual</code>. See &quot;NOTES MERGE STRATEGIES&quot; section of <code><a href="/docs/linux/man/1-git-notes/">git-notes</a></code>(1) for more information on each strategy. </p>
 </dd></dl>
<p> notes.&lt;name&gt;.mergeStrategy </p>
<dl>
<dd> <p> Which merge strategy to choose when doing a notes merge into refs/notes/&lt;name&gt;. This overrides the more general &quot;notes.mergeStrategy&quot;. See the &quot;NOTES MERGE STRATEGIES&quot; section in <code><a href="/docs/linux/man/1-git-notes/">git-notes</a></code>(1) for more information on the available strategies. </p>
 </dd></dl>
<p> notes.displayRef </p>
<dl>
<dd> <p> The (fully qualified) refname from which to show notes when showing commit messages. The value of this variable can be set to a glob, in which case notes from all matching refs will be shown. You may also specify this configuration variable several times. A warning will be issued for refs that do not exist, but a glob that does not match any refs is silently ignored. </p>
<p> This setting can be overridden with the <code>GIT_NOTES_DISPLAY_REF</code> environment variable, which must be a colon separated list of refs or globs. </p>
<p> The effective value of &quot;core.notesRef&quot; (possibly overridden by GIT_NOTES_REF) is also implicitly added to the list of refs to be displayed. </p>
 </dd></dl>
<p> notes.rewrite.&lt;command&gt; </p>
<dl>
<dd> <p> When rewriting commits with &lt;command&gt; (currently <code>amend</code> or <code>rebase</code>) and this variable is set to <code>true</code>, Git automatically copies your notes from the original to the rewritten commit. Defaults to <code>true</code>, but see &quot;notes.rewriteRef&quot; below. </p>
 </dd></dl>
<p> notes.rewriteMode </p>
<dl>
<dd> <p> When copying notes during a rewrite (see the &quot;notes.rewrite.&lt;command&gt;&quot; option), determines what to do if the target commit already has a note. Must be one of <code>overwrite</code>, <code>concatenate</code>, <code>cat_sort_uniq</code>, or <code>ignore</code>. Defaults to <code>concatenate</code>. </p>
<p> This setting can be overridden with the <code>GIT_NOTES_REWRITE_MODE</code> environment variable. </p>
 </dd></dl>
<p> notes.rewriteRef </p>
<dl>
<dd> <p> When copying notes during a rewrite, specifies the (fully qualified) ref whose notes should be copied. The ref may be a glob, in which case notes in all matching refs will be copied. You may also specify this configuration several times. </p>
<p> Does not have a default value; you must configure this variable to enable note rewriting. Set it to <code>refs/notes/commits</code> to enable rewriting for the default commit notes. </p>
<p> This setting can be overridden with the <code>GIT_NOTES_REWRITE_REF</code> environment variable, which must be a colon separated list of refs or globs. </p>
 </dd></dl>
<p> pack.window </p>
<dl>
<dd> <p> The size of the window used by <code><a href="/docs/linux/man/1-git-pack-objects/">git-pack-objects</a></code>(1) when no window size is given on the command line. Defaults to 10. </p>
 </dd></dl>
<p> pack.depth </p>
<dl>
<dd> <p> The maximum delta depth used by <code><a href="/docs/linux/man/1-git-pack-objects/">git-pack-objects</a></code>(1) when no maximum depth is given on the command line. Defaults to 50. Maximum value is 4095. </p>
 </dd></dl>
<p> pack.windowMemory </p>
<dl>
<dd> <p> The maximum size of memory that is consumed by each thread in <code><a href="/docs/linux/man/1-git-pack-objects/">git-pack-objects</a></code>(1) for pack window memory when no limit is given on the command line. The value can be suffixed with &quot;k&quot;, &quot;m&quot;, or &quot;g&quot;. When left unconfigured (or set explicitly to 0), there will be no limit. </p>
 </dd></dl>
<p> pack.compression </p>
<dl>
<dd> <p> An integer -1..9, indicating the compression level for objects in a pack file. -1 is the zlib default. 0 means no compression, and 1..9 are various speed/size tradeoffs, 9 being slowest. If not set, defaults to core.compression. If that is not set, defaults to -1, the zlib default, which is &quot;a default compromise between speed and compression (currently equivalent to level 6).&quot; </p>
<p> Note that changing the compression level will not automatically recompress all existing objects. You can force recompression by passing the -F option to <code><a href="/docs/linux/man/1-git-repack/">git-repack</a></code>(1). </p>
 </dd></dl>
<p> pack.allowPackReuse </p>
<dl>
<dd> <p> When true, and when reachability bitmaps are enabled, pack-objects will try to send parts of the bitmapped packfile verbatim. This can reduce memory and CPU usage to serve fetches, but might result in sending a slightly larger pack. Defaults to true. </p>
 </dd></dl>
<p> pack.island </p>
<dl>
<dd> <p> An extended regular expression configuring a set of delta islands. See &quot;DELTA ISLANDS&quot; in <code><a href="/docs/linux/man/1-git-pack-objects/">git-pack-objects</a></code>(1) for details. </p>
 </dd></dl>
<p> pack.islandCore </p>
<dl>
<dd> <p> Specify an island name which gets to have its objects be packed first. This creates a kind of pseudo-pack at the front of one pack, so that the objects from the specified island are hopefully faster to copy into any pack that should be served to a user requesting these objects. In practice this means that the island specified should likely correspond to what is the most commonly cloned in the repo. See also &quot;DELTA ISLANDS&quot; in <code><a href="/docs/linux/man/1-git-pack-objects/">git-pack-objects</a></code>(1). </p>
 </dd></dl>
<p> pack.deltaCacheSize </p>
<dl>
<dd> <p> The maximum memory in bytes used for caching deltas in <code><a href="/docs/linux/man/1-git-pack-objects/">git-pack-objects</a></code>(1) before writing them out to a pack. This cache is used to speed up the writing object phase by not having to recompute the final delta result once the best match for all objects is found. Repacking large repositories on machines which are tight with memory might be badly impacted by this though, especially if this cache pushes the system into swapping. A value of 0 means no limit. The smallest size of 1 byte may be used to virtually disable this cache. Defaults to 256 MiB. </p>
 </dd></dl>
<p> pack.deltaCacheLimit </p>
<dl>
<dd> <p> The maximum size of a delta, that is cached in <code><a href="/docs/linux/man/1-git-pack-objects/">git-pack-objects</a></code>(1). This cache is used to speed up the writing object phase by not having to recompute the final delta result once the best match for all objects is found. Defaults to 1000. Maximum value is 65535. </p>
 </dd></dl>
<p> pack.threads </p>
<dl>
<dd> <p> Specifies the number of threads to spawn when searching for best delta matches. This requires that <code><a href="/docs/linux/man/1-git-pack-objects/">git-pack-objects</a></code>(1) be compiled with pthreads otherwise this option is ignored with a warning. This is meant to reduce packing time on multiprocessor machines. The required amount of memory for the delta search window is however multiplied by the number of threads. Specifying 0 will cause Git to auto-detect the number of CPU&#8217;s and set the number of threads accordingly. </p>
 </dd></dl>
<p> pack.indexVersion </p>
<dl>
<dd> <p> Specify the default pack index version. Valid values are 1 for legacy pack index used by Git versions prior to 1.5.2, and 2 for the new pack index with capabilities for packs larger than 4 GB as well as proper protection against the repacking of corrupted packs. Version 2 is the default. Note that version 2 is enforced and this config option ignored whenever the corresponding pack is larger than 2 GB. </p>
<p> If you have an old Git that does not understand the version 2 <code>*.idx</code> file, cloning or fetching over a non native protocol (e.g. &quot;http&quot;) that will copy both <code>*.pack</code> file and corresponding <code>*.idx</code> file from the other side may give you a repository that cannot be accessed with your older version of Git. If the <code>*.pack</code> file is smaller than 2 GB, however, you can use <code><a href="/docs/linux/man/1-git-index-pack/">git-index-pack</a></code>(1) on the *.pack file to regenerate the <code>*.idx</code> file. </p>
 </dd></dl>
<p> pack.packSizeLimit </p>
<dl>
<dd> <p> The maximum size of a pack. This setting only affects packing to a file when repacking, i.e. the git:// protocol is unaffected. It can be overridden by the <code>--max-pack-size</code> option of <code><a href="/docs/linux/man/1-git-repack/">git-repack</a></code>(1). Reaching this limit results in the creation of multiple packfiles. </p>
<p> Note that this option is rarely useful, and may result in a larger total on-disk size (because Git will not store deltas between packs), as well as worse runtime performance (object lookup within multiple packs is slower than a single pack, and optimizations like reachability bitmaps cannot cope with multiple packs). </p>
<p> If you need to actively run Git using smaller packfiles (e.g., because your filesystem does not support large files), this option may help. But if your goal is to transmit a packfile over a medium that supports limited sizes (e.g., removable media that cannot store the whole repository), you are likely better off creating a single large packfile and splitting it using a generic multi-volume archive tool (e.g., Unix <code>split</code>). </p>
<p> The minimum size allowed is limited to 1 MiB. The default is unlimited. Common unit suffixes of <i>k</i>, <i>m</i>, or <i>g</i> are supported. </p>
 </dd></dl>
<p> pack.useBitmaps </p>
<dl>
<dd> <p> When true, git will use pack bitmaps (if available) when packing to stdout (e.g., during the server side of a fetch). Defaults to true. You should not generally need to turn this off unless you are debugging pack bitmaps. </p>
 </dd></dl>
<p> pack.useSparse </p>
<dl>
<dd> <p> When true, git will default to using the <i>--sparse</i> option in <i>git pack-objects</i> when the <i>--revs</i> option is present. This algorithm only walks trees that appear in paths that introduce new objects. This can have significant performance benefits when computing a pack to send a small change. However, it is possible that extra objects are added to the pack-file if the included commits contain certain types of direct renames. Default is <code>true</code>. </p>
 </dd></dl>
<p> pack.preferBitmapTips </p>
<dl>
<dd> <p> When selecting which commits will receive bitmaps, prefer a commit at the tip of any reference that is a suffix of any value of this configuration over any other commits in the &quot;selection window&quot;. </p>
<p> Note that setting this configuration to <code>refs/foo</code> does not mean that the commits at the tips of <code>refs/foo/bar</code> and <code>refs/foo/baz</code> will necessarily be selected. This is because commits are selected for bitmaps from within a series of windows of variable length. </p>
<p> If a commit at the tip of any reference which is a suffix of any value of this configuration is seen in a window, it is immediately given preference over any other commit in that window. </p>
 </dd></dl>
<p> pack.writeBitmaps (deprecated) </p>
<dl>
<dd> <p> This is a deprecated synonym for <code>repack.writeBitmaps</code>. </p>
 </dd></dl>
<p> pack.writeBitmapHashCache </p>
<dl>
<dd> <p> When true, git will include a &quot;hash cache&quot; section in the bitmap index (if one is written). This cache can be used to feed git&#8217;s delta heuristics, potentially leading to better deltas between bitmapped and non-bitmapped objects (e.g., when serving a fetch between an older, bitmapped pack and objects that have been pushed since the last gc). The downside is that it consumes 4 bytes per object of disk space. Defaults to true. </p>
<p> When writing a multi-pack reachability bitmap, no new namehashes are computed; instead, any namehashes stored in an existing bitmap are permuted into their appropriate location when writing a new bitmap. </p>
 </dd></dl>
<p> pack.writeReverseIndex </p>
<dl>
<dd> <p> When true, git will write a corresponding .rev file (see: m[blue]<code>Documentation/technical/pack-format.txt</code>m[]<font SIZE="-2">[3]</font>) for each new packfile that it writes in all places except for <code><a href="/docs/linux/man/1-git-fast-import/">git-fast-import</a></code>(1) and in the bulk checkin mechanism. Defaults to false. </p>
 </dd></dl>
<p> pager.&lt;cmd&gt; </p>
<dl>
<dd> <p> If the value is boolean, turns on or off pagination of the output of a particular Git subcommand when writing to a tty. Otherwise, turns on pagination for the subcommand using the pager specified by the value of <code>pager.&lt;cmd&gt;</code>. If <code>--paginate</code> or <code>--no-pager</code> is specified on the command line, it takes precedence over this option. To disable pagination for all commands, set <code>core.pager</code> or <code>GIT_PAGER</code> to <code>cat</code>. </p>
 </dd></dl>
<p> pretty.&lt;name&gt; </p>
<dl>
<dd> <p> Alias for a --pretty= format string, as specified in <code><a href="/docs/linux/man/1-git-log/">git-log</a></code>(1). Any aliases defined here can be used just as the built-in pretty formats could. For example, running <code>git config pretty.changelog &quot;format:* %H %s&quot;</code> would cause the invocation <code>git log --pretty=changelog</code> to be equivalent to running <code>git log &quot;--pretty=format:* %H %s&quot;</code>. Note that an alias with the same name as a built-in format will be silently ignored. </p>
 </dd></dl>
<p> protocol.allow </p>
<dl>
<dd> <p> If set, provide a user defined default policy for all protocols which don&#8217;t explicitly have a policy (<code>protocol.&lt;name&gt;.allow</code>). By default, if unset, known-safe protocols (http, https, git, ssh) have a default policy of <code>always</code>, known-dangerous protocols (ext) have a default policy of <code>never</code>, and all other protocols (including file) have a default policy of <code>user</code>. Supported policies: </p>
 </dd>
<dl>
<dd> <p> &bull; <code>always</code> - protocol is always able to be used. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>never</code> - protocol is never able to be used. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>user</code> - protocol is only able to be used when <code>GIT_PROTOCOL_FROM_USER</code> is either unset or has a value of 1. This policy should be used when you want a protocol to be directly usable by the user but don&#8217;t want it used by commands which execute clone/fetch/push commands without user input, e.g. recursive submodule initialization. </p>
 </dd></dl>
</dl>
<p> protocol.&lt;name&gt;.allow </p>
<dl>
<dd> <p> Set a policy to be used by protocol <code>&lt;name&gt;</code> with clone/fetch/push commands. See <code>protocol.allow</code> above for the available policies. </p>
<p> The protocol names currently used by git are: </p>
 </dd>
<dl>
<dd> <p> &bull; <code>file</code>: any local file-based path (including <code>file://</code> URLs, or local paths) </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>git</code>: the anonymous git protocol over a direct TCP connection (or proxy, if configured) </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>ssh</code>: git over ssh (including <code>host:path</code> syntax, <code>ssh://</code>, etc). </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>http</code>: git over http, both &quot;smart http&quot; and &quot;dumb http&quot;. Note that this does <i>not</i> include <code>https</code>; if you want to configure both, you must do so individually. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; any external helpers are named by their protocol (e.g., use <code>hg</code> to allow the <code>git-remote-hg</code> helper) </p>
 </dd></dl>
</dl>
<p> protocol.version </p>
<dl>
<dd> <p> If set, clients will attempt to communicate with a server using the specified protocol version. If the server does not support it, communication falls back to version 0. If unset, the default is <code>2</code>. Supported versions: </p>
 </dd>
<dl>
<dd> <p> &bull; <code>0</code> - the original wire protocol. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>1</code> - the original wire protocol with the addition of a version string in the initial response from the server. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>2</code> - m[blue]<code>wire protocol version 2</code>m[]<font SIZE="-2">[4]</font>. </p>
 </dd></dl>
</dl>
<p> pull.ff </p>
<dl>
<dd> <p> By default, Git does not create an extra merge commit when merging a commit that is a descendant of the current commit. Instead, the tip of the current branch is fast-forwarded. When set to <code>false</code>, this variable tells Git to create an extra merge commit in such a case (equivalent to giving the <code>--no-ff</code> option from the command line). When set to <code>only</code>, only such fast-forward merges are allowed (equivalent to giving the <code>--ff-only</code> option from the command line). This setting overrides <code>merge.ff</code> when pulling. </p>
 </dd></dl>
<p> pull.rebase </p>
<dl>
<dd> <p> When true, rebase branches on top of the fetched branch, instead of merging the default branch from the default remote when &quot;git pull&quot; is run. See &quot;branch.&lt;name&gt;.rebase&quot; for setting this on a per-branch basis. </p>
<p> When <code>merges</code> (or just <i>m</i>), pass the <code>--rebase-merges</code> option to <i>git rebase</i> so that the local merge commits are included in the rebase (see <code><a href="/docs/linux/man/1-git-rebase/">git-rebase</a></code>(1) for details). </p>
<p> When the value is <code>interactive</code> (or just <i>i</i>), the rebase is run in interactive mode. </p>
<p> <code>NOTE</code>: this is a possibly dangerous operation; do <code>not</code> use it unless you understand the implications (see <code><a href="/docs/linux/man/1-git-rebase/">git-rebase</a></code>(1) for details). </p>
 </dd></dl>
<p> pull.octopus </p>
<dl>
<dd> <p> The default merge strategy to use when pulling multiple branches at once. </p>
 </dd></dl>
<p> pull.twohead </p>
<dl>
<dd> <p> The default merge strategy to use when pulling a single branch. </p>
 </dd></dl>
<p> push.default </p>
<dl>
<dd> <p> Defines the action <code>git push</code> should take if no refspec is given (whether from the command-line, config, or elsewhere). Different values are well-suited for specific workflows; for instance, in a purely central workflow (i.e. the fetch source is equal to the push destination), <code>upstream</code> is probably what you want. Possible values are: </p>
 </dd>
<dl>
<dd> <p> &bull; <code>nothing</code> - do not push anything (error out) unless a refspec is given. This is primarily meant for people who want to avoid mistakes by always being explicit. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>current</code> - push the current branch to update a branch with the same name on the receiving end. Works in both central and non-central workflows. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>upstream</code> - push the current branch back to the branch whose changes are usually integrated into the current branch (which is called <code>@{upstream}</code>). This mode only makes sense if you are pushing to the same repository you would normally pull from (i.e. central workflow). </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>tracking</code> - This is a deprecated synonym for <code>upstream</code>. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>simple</code> - pushes the current branch with the same name on the remote. </p>
<p> If you are working on a centralized workflow (pushing to the same repository you pull from, which is typically <code>origin</code>), then you need to configure an upstream branch with the same name. </p>
<p> This mode is the default since Git 2.0, and is the safest option suited for beginners. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>matching</code> - push all branches having the same name on both ends. This makes the repository you are pushing to remember the set of branches that will be pushed out (e.g. if you always push <i>maint</i> and <i>master</i> there and no other branches, the repository you push to will have these two branches, and your local <i>maint</i> and <i>master</i> will be pushed there). </p>
<p> To use this mode effectively, you have to make sure <i>all</i> the branches you would push out are ready to be pushed out before running <i>git push</i>, as the whole point of this mode is to allow you to push all of the branches in one go. If you usually finish work on only one branch and push out the result, while other branches are unfinished, this mode is not for you. Also this mode is not suitable for pushing into a shared central repository, as other people may add new branches there, or update the tip of existing branches outside your control. </p>
<p> This used to be the default, but not since Git 2.0 (<code>simple</code> is the new default). </p>
 </dd></dl>
</dl>
<p> push.followTags </p>
<dl>
<dd> <p> If set to true enable <code>--follow-tags</code> option by default. You may override this configuration at time of push by specifying <code>--no-follow-tags</code>. </p>
 </dd></dl>
<p> push.gpgSign </p>
<dl>
<dd> <p> May be set to a boolean value, or the string <i>if-asked</i>. A true value causes all pushes to be GPG signed, as if <code>--signed</code> is passed to <code><a href="/docs/linux/man/1-git-push/">git-push</a></code>(1). The string <i>if-asked</i> causes pushes to be signed if the server supports it, as if <code>--signed=if-asked</code> is passed to <i>git push</i>. A false value may override a value from a lower-priority config file. An explicit command-line flag always overrides this config option. </p>
 </dd></dl>
<p> push.pushOption </p>
<dl>
<dd> <p> When no <code>--push-option=&lt;option&gt;</code> argument is given from the command line, <code>git push</code> behaves as if each &lt;value&gt; of this variable is given as <code>--push-option=&lt;value&gt;</code>. </p>
<p> This is a multi-valued variable, and an empty value can be used in a higher priority configuration file (e.g. <code>.git/config</code> in a repository) to clear the values inherited from a lower priority configuration files (e.g. <code>$HOME/.gitconfig</code>). </p>
 </dd>
<dl>
<dd> <pre><code>Example:
/etc/gitconfig
  push.pushoption = a
  push.pushoption = b
~/.gitconfig
  push.pushoption = c
repo/.git/config
  push.pushoption =
  push.pushoption = b
This will result in only b (a and c are cleared).
</code></pre>
 </dd></dl>
<p> push.recurseSubmodules </p>
<dl>
<dd> <p> Make sure all submodule commits used by the revisions to be pushed are available on a remote-tracking branch. If the value is <i>check</i> then Git will verify that all submodule commits that changed in the revisions to be pushed are available on at least one remote of the submodule. If any commits are missing, the push will be aborted and exit with non-zero status. If the value is <i>on-demand</i> then all submodules that changed in the revisions to be pushed will be pushed. If on-demand was not able to push all necessary revisions it will also be aborted and exit with non-zero status. If the value is <i>no</i> then default behavior of ignoring submodules when pushing is retained. You may override this configuration at time of push by specifying <i>--recurse-submodules=check|on-demand|no</i>. If not set, <i>no</i> is used by default, unless <i>submodule.recurse</i> is set (in which case a <i>true</i> value means <i>on-demand</i>). </p>
 </dd></dl>
<p> push.useForceIfIncludes </p>
<dl>
<dd> <p> If set to &quot;true&quot;, it is equivalent to specifying <code>--force-if-includes</code> as an option to <code><a href="/docs/linux/man/1-git-push/">git-push</a></code>(1) in the command line. Adding <code>--no-force-if-includes</code> at the time of push overrides this configuration setting. </p>
 </dd></dl>
<p> push.negotiate </p>
<dl>
<dd> <p> If set to &quot;true&quot;, attempt to reduce the size of the packfile sent by rounds of negotiation in which the client and the server attempt to find commits in common. If &quot;false&quot;, Git will rely solely on the server&#8217;s ref advertisement to find commits in common. </p>
 </dd></dl>
<p> rebase.backend </p>
<dl>
<dd> <p> Default backend to use for rebasing. Possible choices are <i>apply</i> or <i>merge</i>. In the future, if the merge backend gains all remaining capabilities of the apply backend, this setting may become unused. </p>
 </dd></dl>
<p> rebase.stat </p>
<dl>
<dd> <p> Whether to show a diffstat of what changed upstream since the last rebase. False by default. </p>
 </dd></dl>
<p> rebase.autoSquash </p>
<dl>
<dd> <p> If set to true enable <code>--autosquash</code> option by default. </p>
 </dd></dl>
<p> rebase.autoStash </p>
<dl>
<dd> <p> When set to true, automatically create a temporary stash entry before the operation begins, and apply it after the operation ends. This means that you can run rebase on a dirty worktree. However, use with care: the final stash application after a successful rebase might result in non-trivial conflicts. This option can be overridden by the <code>--no-autostash</code> and <code>--autostash</code> options of <code><a href="/docs/linux/man/1-git-rebase/">git-rebase</a></code>(1). Defaults to false. </p>
 </dd></dl>
<p> rebase.missingCommitsCheck </p>
<dl>
<dd> <p> If set to &quot;warn&quot;, git rebase -i will print a warning if some commits are removed (e.g. a line was deleted), however the rebase will still proceed. If set to &quot;error&quot;, it will print the previous warning and stop the rebase, <i>git rebase --edit-todo</i> can then be used to correct the error. If set to &quot;ignore&quot;, no checking is done. To drop a commit without warning or error, use the <code>drop</code> command in the todo list. Defaults to &quot;ignore&quot;. </p>
 </dd></dl>
<p> rebase.instructionFormat </p>
<dl>
<dd> <p> A format string, as specified in <code><a href="/docs/linux/man/1-git-log/">git-log</a></code>(1), to be used for the todo list during an interactive rebase. The format will automatically have the long commit hash prepended to the format. </p>
 </dd></dl>
<p> rebase.abbreviateCommands </p>
<dl>
<dd> <p> If set to true, <code>git rebase</code> will use abbreviated command names in the todo list resulting in something like this: </p>
 </dd>
<dl>
<dd> <pre><code>        p deadbee The oneline of the commit
        p fa1afe1 The oneline of the next commit
        ...
</code></pre>
 </dd></dl>
<p> instead of: </p>
<dl>
<dd> <pre><code>        pick deadbee The oneline of the commit
        pick fa1afe1 The oneline of the next commit
        ...
</code></pre>
 </dd></dl>
<p> Defaults to false. </dl>
 </p>
<p> rebase.rescheduleFailedExec </p>
<dl>
<dd> <p> Automatically reschedule <code>exec</code> commands that failed. This only makes sense in interactive mode (or when an <code>--exec</code> option was provided). This is the same as specifying the <code>--reschedule-failed-exec</code> option. </p>
 </dd></dl>
<p> rebase.forkPoint </p>
<dl>
<dd> <p> If set to false set <code>--no-fork-point</code> option by default. </p>
 </dd></dl>
<p> receive.advertiseAtomic </p>
<dl>
<dd> <p> By default, git-receive-pack will advertise the atomic push capability to its clients. If you don&#8217;t want to advertise this capability, set this variable to false. </p>
 </dd></dl>
<p> receive.advertisePushOptions </p>
<dl>
<dd> <p> When set to true, git-receive-pack will advertise the push options capability to its clients. False by default. </p>
 </dd></dl>
<p> receive.autogc </p>
<dl>
<dd> <p> By default, git-receive-pack will run &quot;git-gc --auto&quot; after receiving data from git-push and updating refs. You can stop it by setting this variable to false. </p>
 </dd></dl>
<p> receive.certNonceSeed </p>
<dl>
<dd> <p> By setting this variable to a string, <code>git receive-pack</code> will accept a <code>git push --signed</code> and verifies it by using a &quot;nonce&quot; protected by HMAC using this string as a secret key. </p>
 </dd></dl>
<p> receive.certNonceSlop </p>
<dl>
<dd> <p> When a <code>git push --signed</code> sent a push certificate with a &quot;nonce&quot; that was issued by a receive-pack serving the same repository within this many seconds, export the &quot;nonce&quot; found in the certificate to <code>GIT_PUSH_CERT_NONCE</code> to the hooks (instead of what the receive-pack asked the sending side to include). This may allow writing checks in <code>pre-receive</code> and <code>post-receive</code> a bit easier. Instead of checking <code>GIT_PUSH_CERT_NONCE_SLOP</code> environment variable that records by how many seconds the nonce is stale to decide if they want to accept the certificate, they only can check <code>GIT_PUSH_CERT_NONCE_STATUS</code> is <code>OK</code>. </p>
 </dd></dl>
<p> receive.fsckObjects </p>
<dl>
<dd> <p> If it is set to true, git-receive-pack will check all received objects. See <code>transfer.fsckObjects</code> for what&#8217;s checked. Defaults to false. If not set, the value of <code>transfer.fsckObjects</code> is used instead. </p>
 </dd></dl>
<p> receive.fsck.&lt;msg-id&gt; </p>
<dl>
<dd> <p> Acts like <code>fsck.&lt;msg-id&gt;</code>, but is used by <code><a href="/docs/linux/man/1-git-receive-pack/">git-receive-pack</a></code>(1) instead of <code><a href="/docs/linux/man/1-git-fsck/">git-fsck</a></code>(1). See the <code>fsck.&lt;msg-id&gt;</code> documentation for details. </p>
 </dd></dl>
<p> receive.fsck.skipList </p>
<dl>
<dd> <p> Acts like <code>fsck.skipList</code>, but is used by <code><a href="/docs/linux/man/1-git-receive-pack/">git-receive-pack</a></code>(1) instead of <code><a href="/docs/linux/man/1-git-fsck/">git-fsck</a></code>(1). See the <code>fsck.skipList</code> documentation for details. </p>
 </dd></dl>
<p> receive.keepAlive </p>
<dl>
<dd> <p> After receiving the pack from the client, <code>receive-pack</code> may produce no output (if <code>--quiet</code> was specified) while processing the pack, causing some networks to drop the TCP connection. With this option set, if <code>receive-pack</code> does not transmit any data in this phase for <code>receive.keepAlive</code> seconds, it will send a short keepalive packet. The default is 5 seconds; set to 0 to disable keepalives entirely. </p>
 </dd></dl>
<p> receive.unpackLimit </p>
<dl>
<dd> <p> If the number of objects received in a push is below this limit then the objects will be unpacked into loose object files. However if the number of received objects equals or exceeds this limit then the received pack will be stored as a pack, after adding any missing delta bases. Storing the pack from a push can make the push operation complete faster, especially on slow filesystems. If not set, the value of <code>transfer.unpackLimit</code> is used instead. </p>
 </dd></dl>
<p> receive.maxInputSize </p>
<dl>
<dd> <p> If the size of the incoming pack stream is larger than this limit, then git-receive-pack will error out, instead of accepting the pack file. If not set or set to 0, then the size is unlimited. </p>
 </dd></dl>
<p> receive.denyDeletes </p>
<dl>
<dd> <p> If set to true, git-receive-pack will deny a ref update that deletes the ref. Use this to prevent such a ref deletion via a push. </p>
 </dd></dl>
<p> receive.denyDeleteCurrent </p>
<dl>
<dd> <p> If set to true, git-receive-pack will deny a ref update that deletes the currently checked out branch of a non-bare repository. </p>
 </dd></dl>
<p> receive.denyCurrentBranch </p>
<dl>
<dd> <p> If set to true or &quot;refuse&quot;, git-receive-pack will deny a ref update to the currently checked out branch of a non-bare repository. Such a push is potentially dangerous because it brings the HEAD out of sync with the index and working tree. If set to &quot;warn&quot;, print a warning of such a push to stderr, but allow the push to proceed. If set to false or &quot;ignore&quot;, allow such pushes with no message. Defaults to &quot;refuse&quot;. </p>
<p> Another option is &quot;updateInstead&quot; which will update the working tree if pushing into the current branch. This option is intended for synchronizing working directories when one side is not easily accessible via interactive ssh (e.g. a live web site, hence the requirement that the working directory be clean). This mode also comes in handy when developing inside a VM to test and fix code on different Operating Systems. </p>
<p> By default, &quot;updateInstead&quot; will refuse the push if the working tree or the index have any difference from the HEAD, but the <code>push-to-checkout</code> hook can be used to customize this. See <code><a href="/docs/linux/man/5-githooks/">githooks</a></code>(5). </p>
 </dd></dl>
<p> receive.denyNonFastForwards </p>
<dl>
<dd> <p> If set to true, git-receive-pack will deny a ref update which is not a fast-forward. Use this to prevent such an update via a push, even if that push is forced. This configuration variable is set when initializing a shared repository. </p>
 </dd></dl>
<p> receive.hideRefs </p>
<dl>
<dd> <p> This variable is the same as <code>transfer.hideRefs</code>, but applies only to <code>receive-pack</code> (and so affects pushes, but not fetches). An attempt to update or delete a hidden ref by <code>git push</code> is rejected. </p>
 </dd></dl>
<p> receive.procReceiveRefs </p>
<dl>
<dd> <p> This is a multi-valued variable that defines reference prefixes to match the commands in <code>receive-pack</code>. Commands matching the prefixes will be executed by an external hook &quot;proc-receive&quot;, instead of the internal <code>execute_commands</code> function. If this variable is not defined, the &quot;proc-receive&quot; hook will never be used, and all commands will be executed by the internal <code>execute_commands</code> function. </p>
<p> For example, if this variable is set to &quot;refs/for&quot;, pushing to reference such as &quot;refs/for/master&quot; will not create or update a reference named &quot;refs/for/master&quot;, but may create or update a pull request directly by running the hook &quot;proc-receive&quot;. </p>
<p> Optional modifiers can be provided in the beginning of the value to filter commands for specific actions: create (a), modify (m), delete (d). A <code>!</code> can be included in the modifiers to negate the reference prefix entry. E.g.: </p>
 </dd>
<dl>
<dd> <pre><code>git config --system --add receive.procReceiveRefs ad:refs/heads
git config --system --add receive.procReceiveRefs !:refs/heads
</code></pre>
 </dd></dl>
</dl>
<p> receive.updateServerInfo </p>
<dl>
<dd> <p> If set to true, git-receive-pack will run git-update-server-info after receiving data from git-push and updating refs. </p>
 </dd></dl>
<p> receive.shallowUpdate </p>
<dl>
<dd> <p> If set to true, .git/shallow can be updated when new refs require new shallow roots. Otherwise those refs are rejected. </p>
 </dd></dl>
<p> remote.pushDefault </p>
<dl>
<dd> <p> The remote to push to by default. Overrides <code>branch.&lt;name&gt;.remote</code> for all branches, and is overridden by <code>branch.&lt;name&gt;.pushRemote</code> for specific branches. </p>
 </dd></dl>
<p> remote.&lt;name&gt;.url </p>
<dl>
<dd> <p> The URL of a remote repository. See <code><a href="/docs/linux/man/1-git-fetch/">git-fetch</a></code>(1) or <code><a href="/docs/linux/man/1-git-push/">git-push</a></code>(1). </p>
 </dd></dl>
<p> remote.&lt;name&gt;.pushurl </p>
<dl>
<dd> <p> The push URL of a remote repository. See <code><a href="/docs/linux/man/1-git-push/">git-push</a></code>(1). </p>
 </dd></dl>
<p> remote.&lt;name&gt;.proxy </p>
<dl>
<dd> <p> For remotes that require curl (http, https and ftp), the URL to the proxy to use for that remote. Set to the empty string to disable proxying for that remote. </p>
 </dd></dl>
<p> remote.&lt;name&gt;.proxyAuthMethod </p>
<dl>
<dd> <p> For remotes that require curl (http, https and ftp), the method to use for authenticating against the proxy in use (probably set in <code>remote.&lt;name&gt;.proxy</code>). See <code>http.proxyAuthMethod</code>. </p>
 </dd></dl>
<p> remote.&lt;name&gt;.fetch </p>
<dl>
<dd> <p> The default set of &quot;refspec&quot; for <code><a href="/docs/linux/man/1-git-fetch/">git-fetch</a></code>(1). See <code><a href="/docs/linux/man/1-git-fetch/">git-fetch</a></code>(1). </p>
 </dd></dl>
<p> remote.&lt;name&gt;.push </p>
<dl>
<dd> <p> The default set of &quot;refspec&quot; for <code><a href="/docs/linux/man/1-git-push/">git-push</a></code>(1). See <code><a href="/docs/linux/man/1-git-push/">git-push</a></code>(1). </p>
 </dd></dl>
<p> remote.&lt;name&gt;.mirror </p>
<dl>
<dd> <p> If true, pushing to this remote will automatically behave as if the <code>--mirror</code> option was given on the command line. </p>
 </dd></dl>
<p> remote.&lt;name&gt;.skipDefaultUpdate </p>
<dl>
<dd> <p> If true, this remote will be skipped by default when updating using <code><a href="/docs/linux/man/1-git-fetch/">git-fetch</a></code>(1) or the <code>update</code> subcommand of <code><a href="/docs/linux/man/1-git-remote/">git-remote</a></code>(1). </p>
 </dd></dl>
<p> remote.&lt;name&gt;.skipFetchAll </p>
<dl>
<dd> <p> If true, this remote will be skipped by default when updating using <code><a href="/docs/linux/man/1-git-fetch/">git-fetch</a></code>(1) or the <code>update</code> subcommand of <code><a href="/docs/linux/man/1-git-remote/">git-remote</a></code>(1). </p>
 </dd></dl>
<p> remote.&lt;name&gt;.receivepack </p>
<dl>
<dd> <p> The default program to execute on the remote side when pushing. See option --receive-pack of <code><a href="/docs/linux/man/1-git-push/">git-push</a></code>(1). </p>
 </dd></dl>
<p> remote.&lt;name&gt;.uploadpack </p>
<dl>
<dd> <p> The default program to execute on the remote side when fetching. See option --upload-pack of <code><a href="/docs/linux/man/1-git-fetch-pack/">git-fetch-pack</a></code>(1). </p>
 </dd></dl>
<p> remote.&lt;name&gt;.tagOpt </p>
<dl>
<dd> <p> Setting this value to --no-tags disables automatic tag following when fetching from remote &lt;name&gt;. Setting it to --tags will fetch every tag from remote &lt;name&gt;, even if they are not reachable from remote branch heads. Passing these flags directly to <code><a href="/docs/linux/man/1-git-fetch/">git-fetch</a></code>(1) can override this setting. See options --tags and --no-tags of <code><a href="/docs/linux/man/1-git-fetch/">git-fetch</a></code>(1). </p>
 </dd></dl>
<p> remote.&lt;name&gt;.vcs </p>
<dl>
<dd> <p> Setting this to a value &lt;vcs&gt; will cause Git to interact with the remote with the git-remote-&lt;vcs&gt; helper. </p>
 </dd></dl>
<p> remote.&lt;name&gt;.prune </p>
<dl>
<dd> <p> When set to true, fetching from this remote by default will also remove any remote-tracking references that no longer exist on the remote (as if the <code>--prune</code> option was given on the command line). Overrides <code>fetch.prune</code> settings, if any. </p>
 </dd></dl>
<p> remote.&lt;name&gt;.pruneTags </p>
<dl>
<dd> <p> When set to true, fetching from this remote by default will also remove any local tags that no longer exist on the remote if pruning is activated in general via <code>remote.&lt;name&gt;.prune</code>, <code>fetch.prune</code> or <code>--prune</code>. Overrides <code>fetch.pruneTags</code> settings, if any. </p>
<p> See also <code>remote.&lt;name&gt;.prune</code> and the PRUNING section of <code><a href="/docs/linux/man/1-git-fetch/">git-fetch</a></code>(1). </p>
 </dd></dl>
<p> remote.&lt;name&gt;.promisor </p>
<dl>
<dd> <p> When set to true, this remote will be used to fetch promisor objects. </p>
 </dd></dl>
<p> remote.&lt;name&gt;.partialclonefilter </p>
<dl>
<dd> <p> The filter that will be applied when fetching from this promisor remote. </p>
 </dd></dl>
<p> remotes.&lt;group&gt; </p>
<dl>
<dd> <p> The list of remotes which are fetched by &quot;git remote update &lt;group&gt;&quot;. See <code><a href="/docs/linux/man/1-git-remote/">git-remote</a></code>(1). </p>
 </dd></dl>
<p> repack.useDeltaBaseOffset </p>
<dl>
<dd> <p> By default, <code><a href="/docs/linux/man/1-git-repack/">git-repack</a></code>(1) creates packs that use delta-base offset. If you need to share your repository with Git older than version 1.4.4, either directly or via a dumb protocol such as http, then you need to set this option to &quot;false&quot; and repack. Access from old Git versions over the native protocol are unaffected by this option. </p>
 </dd></dl>
<p> repack.packKeptObjects </p>
<dl>
<dd> <p> If set to true, makes <code>git repack</code> act as if <code>--pack-kept-objects</code> was passed. See <code><a href="/docs/linux/man/1-git-repack/">git-repack</a></code>(1) for details. Defaults to <code>false</code> normally, but <code>true</code> if a bitmap index is being written (either via <code>--write-bitmap-index</code> or <code>repack.writeBitmaps</code>). </p>
 </dd></dl>
<p> repack.useDeltaIslands </p>
<dl>
<dd> <p> If set to true, makes <code>git repack</code> act as if <code>--delta-islands</code> was passed. Defaults to <code>false</code>. </p>
 </dd></dl>
<p> repack.writeBitmaps </p>
<dl>
<dd> <p> When true, git will write a bitmap index when packing all objects to disk (e.g., when <code>git repack -a</code> is run). This index can speed up the &quot;counting objects&quot; phase of subsequent packs created for clones and fetches, at the cost of some disk space and extra time spent on the initial repack. This has no effect if multiple packfiles are created. Defaults to true on bare repos, false otherwise. </p>
 </dd></dl>
<p> rerere.autoUpdate </p>
<dl>
<dd> <p> When set to true, <code>git-rerere</code> updates the index with the resulting contents after it cleanly resolves conflicts using previously recorded resolution. Defaults to false. </p>
 </dd></dl>
<p> rerere.enabled </p>
<dl>
<dd> <p> Activate recording of resolved conflicts, so that identical conflict hunks can be resolved automatically, should they be encountered again. By default, <code><a href="/docs/linux/man/1-git-rerere/">git-rerere</a></code>(1) is enabled if there is an <code>rr-cache</code> directory under the <code>$GIT_DIR</code>, e.g. if &quot;rerere&quot; was previously used in the repository. </p>
 </dd></dl>
<p> reset.quiet </p>
<dl>
<dd> <p> When set to true, <i>git reset</i> will default to the <i>--quiet</i> option. </p>
 </dd></dl>
<p> safe.directory </p>
<dl>
<dd> <p> These config entries specify Git-tracked directories that are considered safe even if they are owned by someone other than the current user. By default, Git will refuse to even parse a Git config of a repository owned by someone else, let alone run its hooks, and this config setting allows users to specify exceptions, e.g. for intentionally shared repositories (see the <code>--shared</code> option in <code><a href="/docs/linux/man/1-git-init/">git-init</a></code>(1)). </p>
<p> This is a multi-valued setting, i.e. you can add more than one directory via <code>git config --add</code>. To reset the list of safe directories (e.g. to override any such directories specified in the system config), add a <code>safe.directory</code> entry with an empty value. </p>
<p> This config setting is only respected when specified in a system or global config, not when it is specified in a repository config or via the command line option <code>-c safe.directory=&lt;path&gt;</code>. </p>
<p> The value of this setting is interpolated, i.e. <code>~/&lt;path&gt;</code> expands to a path relative to the home directory and <code>%(prefix)/&lt;path&gt;</code> expands to a path relative to Git&#8217;s (runtime) prefix. </p>
<p> To completely opt-out of this security check, set <code>safe.directory</code> to the string <code>*</code>. This will allow all repositories to be treated as if their directory was listed in the <code>safe.directory</code> list. If <code>safe.directory=*</code> is set in system config and you want to re-enable this protection, then initialize your list with an empty value before listing the repositories that you deem safe. </p>
<p> As explained, Git only allows you to access repositories owned by yourself, i.e. the user who is running Git, by default. When Git is running as <i>root</i> in a non Windows platform that provides sudo, however, git checks the SUDO_UID environment variable that sudo creates and will allow access to the uid recorded as its value in addition to the id from <i>root</i>. This is to make it easy to perform a common sequence during installation &quot;make &amp;&amp; sudo make install&quot;. A git process running under <i>sudo</i> runs as <i>root</i> but the <i>sudo</i> command exports the environment variable to record which id the original user has. If that is not what you would prefer and want git to only trust repositories that are owned by root instead, then you can remove the <code>SUDO_UID</code> variable from root&#8217;s environment before invoking git. </p>
 </dd></dl>
<p> sendemail.identity </p>
<dl>
<dd> <p> A configuration identity. When given, causes values in the <i>sendemail.&lt;identity&gt;</i> subsection to take precedence over values in the <i>sendemail</i> section. The default identity is the value of <code>sendemail.identity</code>. </p>
 </dd></dl>
<p> sendemail.smtpEncryption </p>
<dl>
<dd> <p> See <code><a href="/docs/linux/man/1-git-send-email/">git-send-email</a></code>(1) for description. Note that this setting is not subject to the <i>identity</i> mechanism. </p>
 </dd></dl>
<p> sendemail.smtpsslcertpath </p>
<dl>
<dd> <p> Path to ca-certificates (either a directory or a single file). Set it to an empty string to disable certificate verification. </p>
 </dd></dl>
<p> sendemail.&lt;identity&gt;.* </p>
<dl>
<dd> <p> Identity-specific versions of the <i>sendemail.*</i> parameters found below, taking precedence over those when this identity is selected, through either the command-line or <code>sendemail.identity</code>. </p>
 </dd></dl>
<p> sendemail.aliasesFile, sendemail.aliasFileType, sendemail.annotate, sendemail.bcc, sendemail.cc, sendemail.ccCmd, sendemail.chainReplyTo, sendemail.confirm, sendemail.envelopeSender, sendemail.from, sendemail.multiEdit, sendemail.signedoffbycc, sendemail.smtpPass, sendemail.suppresscc, sendemail.suppressFrom, sendemail.to, sendemail.tocmd, sendemail.smtpDomain, sendemail.smtpServer, sendemail.smtpServerPort, sendemail.smtpServerOption, sendemail.smtpUser, sendemail.thread, sendemail.transferEncoding, sendemail.validate, sendemail.xmailer </p>
<dl>
<dd> <p> See <code><a href="/docs/linux/man/1-git-send-email/">git-send-email</a></code>(1) for description. </p>
 </dd></dl>
<p> sendemail.signedoffcc (deprecated) </p>
<dl>
<dd> <p> Deprecated alias for <code>sendemail.signedoffbycc</code>. </p>
 </dd></dl>
<p> sendemail.smtpBatchSize </p>
<dl>
<dd> <p> Number of messages to be sent per connection, after that a relogin will happen. If the value is 0 or undefined, send all messages in one connection. See also the <code>--batch-size</code> option of <code><a href="/docs/linux/man/1-git-send-email/">git-send-email</a></code>(1). </p>
 </dd></dl>
<p> sendemail.smtpReloginDelay </p>
<dl>
<dd> <p> Seconds wait before reconnecting to smtp server. See also the <code>--relogin-delay</code> option of <code><a href="/docs/linux/man/1-git-send-email/">git-send-email</a></code>(1). </p>
 </dd></dl>
<p> sendemail.forbidSendmailVariables </p>
<dl>
<dd> <p> To avoid common misconfiguration mistakes, <code><a href="/docs/linux/man/1-git-send-email/">git-send-email</a></code>(1) will abort with a warning if any configuration options for &quot;sendmail&quot; exist. Set this variable to bypass the check. </p>
 </dd></dl>
<p> sequence.editor </p>
<dl>
<dd> <p> Text editor used by <code>git rebase -i</code> for editing the rebase instruction file. The value is meant to be interpreted by the shell when it is used. It can be overridden by the <code>GIT_SEQUENCE_EDITOR</code> environment variable. When not configured the default commit message editor is used instead. </p>
 </dd></dl>
<p> showBranch.default </p>
<dl>
<dd> <p> The default set of branches for <code><a href="/docs/linux/man/1-git-show-branch/">git-show-branch</a></code>(1). See <code><a href="/docs/linux/man/1-git-show-branch/">git-show-branch</a></code>(1). </p>
 </dd></dl>
<p> splitIndex.maxPercentChange </p>
<dl>
<dd> <p> When the split index feature is used, this specifies the percent of entries the split index can contain compared to the total number of entries in both the split index and the shared index before a new shared index is written. The value should be between 0 and 100. If the value is 0 then a new shared index is always written, if it is 100 a new shared index is never written. By default the value is 20, so a new shared index is written if the number of entries in the split index would be greater than 20 percent of the total number of entries. See <code><a href="/docs/linux/man/1-git-update-index/">git-update-index</a></code>(1). </p>
 </dd></dl>
<p> splitIndex.sharedIndexExpire </p>
<dl>
<dd> <p> When the split index feature is used, shared index files that were not modified since the time this variable specifies will be removed when a new shared index file is created. The value &quot;now&quot; expires all entries immediately, and &quot;never&quot; suppresses expiration altogether. The default value is &quot;2.weeks.ago&quot;. Note that a shared index file is considered modified (for the purpose of expiration) each time a new split-index file is either created based on it or read from it. See <code><a href="/docs/linux/man/1-git-update-index/">git-update-index</a></code>(1). </p>
 </dd></dl>
<p> ssh.variant </p>
<dl>
<dd> <p> By default, Git determines the command line arguments to use based on the basename of the configured SSH command (configured using the environment variable <code>GIT_SSH</code> or <code>GIT_SSH_COMMAND</code> or the config setting <code>core.sshCommand</code>). If the basename is unrecognized, Git will attempt to detect support of OpenSSH options by first invoking the configured SSH command with the <code>-G</code> (print configuration) option and will subsequently use OpenSSH options (if that is successful) or no options besides the host and remote command (if it fails). </p>
<p> The config variable <code>ssh.variant</code> can be set to override this detection. Valid values are <code>ssh</code> (to use OpenSSH options), <code>plink</code>, <code>putty</code>, <code>tortoiseplink</code>, <code>simple</code> (no options except the host and remote command). The default auto-detection can be explicitly requested using the value <code>auto</code>. Any other value is treated as <code>ssh</code>. This setting can also be overridden via the environment variable <code>GIT_SSH_VARIANT</code>. </p>
<p> The current command-line parameters used for each variant are as follows: </p>
 </dd>
<dl>
<dd> <p> &bull; <code>ssh</code> - [-p port] [-4] [-6] [-o option] [username@]host command </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>simple</code> - [username@]host command </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>plink</code> or <code>putty</code> - [-P port] [-4] [-6] [username@]host command </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>tortoiseplink</code> - [-P port] [-4] [-6] -batch [username@]host command </p>
 </dd></dl>
<p> Except for the <code>simple</code> variant, command-line parameters are likely to change as git gains new features. </dl>
 </p>
<p> status.relativePaths </p>
<dl>
<dd> <p> By default, <code><a href="/docs/linux/man/1-git-status/">git-status</a></code>(1) shows paths relative to the current directory. Setting this variable to <code>false</code> shows paths relative to the repository root (this was the default for Git prior to v1.5.4). </p>
 </dd></dl>
<p> status.short </p>
<dl>
<dd> <p> Set to true to enable --short by default in <code><a href="/docs/linux/man/1-git-status/">git-status</a></code>(1). The option --no-short takes precedence over this variable. </p>
 </dd></dl>
<p> status.branch </p>
<dl>
<dd> <p> Set to true to enable --branch by default in <code><a href="/docs/linux/man/1-git-status/">git-status</a></code>(1). The option --no-branch takes precedence over this variable. </p>
 </dd></dl>
<p> status.aheadBehind </p>
<dl>
<dd> <p> Set to true to enable <code>--ahead-behind</code> and false to enable <code>--no-ahead-behind</code> by default in <code><a href="/docs/linux/man/1-git-status/">git-status</a></code>(1) for non-porcelain status formats. Defaults to true. </p>
 </dd></dl>
<p> status.displayCommentPrefix </p>
<dl>
<dd> <p> If set to true, <code><a href="/docs/linux/man/1-git-status/">git-status</a></code>(1) will insert a comment prefix before each output line (starting with <code>core.commentChar</code>, i.e. <code>#</code> by default). This was the behavior of <code><a href="/docs/linux/man/1-git-status/">git-status</a></code>(1) in Git 1.8.4 and previous. Defaults to false. </p>
 </dd></dl>
<p> status.renameLimit </p>
<dl>
<dd> <p> The number of files to consider when performing rename detection in <code><a href="/docs/linux/man/1-git-status/">git-status</a></code>(1) and <code><a href="/docs/linux/man/1-git-commit/">git-commit</a></code>(1). Defaults to the value of diff.renameLimit. </p>
 </dd></dl>
<p> status.renames </p>
<dl>
<dd> <p> Whether and how Git detects renames in <code><a href="/docs/linux/man/1-git-status/">git-status</a></code>(1) and <code><a href="/docs/linux/man/1-git-commit/">git-commit</a></code>(1) . If set to &quot;false&quot;, rename detection is disabled. If set to &quot;true&quot;, basic rename detection is enabled. If set to &quot;copies&quot; or &quot;copy&quot;, Git will detect copies, as well. Defaults to the value of diff.renames. </p>
 </dd></dl>
<p> status.showStash </p>
<dl>
<dd> <p> If set to true, <code><a href="/docs/linux/man/1-git-status/">git-status</a></code>(1) will display the number of entries currently stashed away. Defaults to false. </p>
 </dd></dl>
<p> status.showUntrackedFiles </p>
<dl>
<dd> <p> By default, <code><a href="/docs/linux/man/1-git-status/">git-status</a></code>(1) and <code><a href="/docs/linux/man/1-git-commit/">git-commit</a></code>(1) show files which are not currently tracked by Git. Directories which contain only untracked files, are shown with the directory name only. Showing untracked files means that Git needs to lstat() all the files in the whole repository, which might be slow on some systems. So, this variable controls how the commands displays the untracked files. Possible values are: </p>
 </dd>
<dl>
<dd> <p> &bull; <code>no</code> - Show no untracked files. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>normal</code> - Show untracked files and directories. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>all</code> - Show also individual files in untracked directories. </p>
 </dd></dl>
<p> If this variable is not specified, it defaults to <i>normal</i>. This variable can be overridden with the -u|--untracked-files option of <code><a href="/docs/linux/man/1-git-status/">git-status</a></code>(1) and <code><a href="/docs/linux/man/1-git-commit/">git-commit</a></code>(1). </dl>
 </p>
<p> status.submoduleSummary </p>
<dl>
<dd> <p> Defaults to false. If this is set to a non zero number or true (identical to -1 or an unlimited number), the submodule summary will be enabled and a summary of commits for modified submodules will be shown (see --summary-limit option of <code><a href="/docs/linux/man/1-git-submodule/">git-submodule</a></code>(1)). Please note that the summary output command will be suppressed for all submodules when <code>diff.ignoreSubmodules</code> is set to <i>all</i> or only for those submodules where <code>submodule.&lt;name&gt;.ignore=all</code>. The only exception to that rule is that status and commit will show staged submodule changes. To also view the summary for ignored submodules you can either use the --ignore-submodules=dirty command-line option or the <i>git submodule summary</i> command, which shows a similar output but does not honor these settings. </p>
 </dd></dl>
<p> stash.useBuiltin </p>
<dl>
<dd> <p> Unused configuration variable. Used in Git versions 2.22 to 2.26 as an escape hatch to enable the legacy shellscript implementation of stash. Now the built-in rewrite of it in C is always used. Setting this will emit a warning, to alert any remaining users that setting this now does nothing. </p>
 </dd></dl>
<p> stash.showIncludeUntracked </p>
<dl>
<dd> <p> If this is set to true, the <code>git stash show</code> command will show the untracked files of a stash entry. Defaults to false. See description of <i>show</i> command in <code><a href="/docs/linux/man/1-git-stash/">git-stash</a></code>(1). </p>
 </dd></dl>
<p> stash.showPatch </p>
<dl>
<dd> <p> If this is set to true, the <code>git stash show</code> command without an option will show the stash entry in patch form. Defaults to false. See description of <i>show</i> command in <code><a href="/docs/linux/man/1-git-stash/">git-stash</a></code>(1). </p>
 </dd></dl>
<p> stash.showStat </p>
<dl>
<dd> <p> If this is set to true, the <code>git stash show</code> command without an option will show diffstat of the stash entry. Defaults to true. See description of <i>show</i> command in <code><a href="/docs/linux/man/1-git-stash/">git-stash</a></code>(1). </p>
 </dd></dl>
<p> submodule.&lt;name&gt;.url </p>
<dl>
<dd> <p> The URL for a submodule. This variable is copied from the .gitmodules file to the git config via <i>git submodule init</i>. The user can change the configured URL before obtaining the submodule via <i>git submodule update</i>. If neither submodule.&lt;name&gt;.active or submodule.active are set, the presence of this variable is used as a fallback to indicate whether the submodule is of interest to git commands. See <code><a href="/docs/linux/man/1-git-submodule/">git-submodule</a></code>(1) and <code><a href="/docs/linux/man/5-gitmodules/">gitmodules</a></code>(5) for details. </p>
 </dd></dl>
<p> submodule.&lt;name&gt;.update </p>
<dl>
<dd> <p> The method by which a submodule is updated by <i>git submodule update</i>, which is the only affected command, others such as <i>git checkout --recurse-submodules</i> are unaffected. It exists for historical reasons, when <i>git submodule</i> was the only command to interact with submodules; settings like <code>submodule.active</code> and <code>pull.rebase</code> are more specific. It is populated by <code>git submodule init</code> from the <code><a href="/docs/linux/man/5-gitmodules/">gitmodules</a></code>(5) file. See description of <i>update</i> command in <code><a href="/docs/linux/man/1-git-submodule/">git-submodule</a></code>(1). </p>
 </dd></dl>
<p> submodule.&lt;name&gt;.branch </p>
<dl>
<dd> <p> The remote branch name for a submodule, used by <code>git submodule update --remote</code>. Set this option to override the value found in the <code>.gitmodules</code> file. See <code><a href="/docs/linux/man/1-git-submodule/">git-submodule</a></code>(1) and <code><a href="/docs/linux/man/5-gitmodules/">gitmodules</a></code>(5) for details. </p>
 </dd></dl>
<p> submodule.&lt;name&gt;.fetchRecurseSubmodules </p>
<dl>
<dd> <p> This option can be used to control recursive fetching of this submodule. It can be overridden by using the --[no-]recurse-submodules command-line option to &quot;git fetch&quot; and &quot;git pull&quot;. This setting will override that from in the <code><a href="/docs/linux/man/5-gitmodules/">gitmodules</a></code>(5) file. </p>
 </dd></dl>
<p> submodule.&lt;name&gt;.ignore </p>
<dl>
<dd> <p> Defines under what circumstances &quot;git status&quot; and the diff family show a submodule as modified. When set to &quot;all&quot;, it will never be considered modified (but it will nonetheless show up in the output of status and commit when it has been staged), &quot;dirty&quot; will ignore all changes to the submodules work tree and takes only differences between the HEAD of the submodule and the commit recorded in the superproject into account. &quot;untracked&quot; will additionally let submodules with modified tracked files in their work tree show up. Using &quot;none&quot; (the default when this option is not set) also shows submodules that have untracked files in their work tree as changed. This setting overrides any setting made in .gitmodules for this submodule, both settings can be overridden on the command line by using the &quot;--ignore-submodules&quot; option. The <i>git submodule</i> commands are not affected by this setting. </p>
 </dd></dl>
<p> submodule.&lt;name&gt;.active </p>
<dl>
<dd> <p> Boolean value indicating if the submodule is of interest to git commands. This config option takes precedence over the submodule.active config option. See <code><a href="/docs/linux/man/7-gitsubmodules/">gitsubmodules</a></code>(7) for details. </p>
 </dd></dl>
<p> submodule.active </p>
<dl>
<dd> <p> A repeated field which contains a pathspec used to match against a submodule&#8217;s path to determine if the submodule is of interest to git commands. See <code><a href="/docs/linux/man/7-gitsubmodules/">gitsubmodules</a></code>(7) for details. </p>
 </dd></dl>
<p> submodule.recurse </p>
<dl>
<dd> <p> A boolean indicating if commands should enable the <code>--recurse-submodules</code> option by default. Applies to all commands that support this option (<code>checkout</code>, <code>fetch</code>, <code>grep</code>, <code>pull</code>, <code>push</code>, <code>read-tree</code>, <code>reset</code>, <code>restore</code> and <code>switch</code>) except <code>clone</code> and <code>ls-files</code>. Defaults to false. When set to true, it can be deactivated via the <code>--no-recurse-submodules</code> option. Note that some Git commands lacking this option may call some of the above commands affected by <code>submodule.recurse</code>; for instance <code>git remote update</code> will call <code>git fetch</code> but does not have a <code>--no-recurse-submodules</code> option. For these commands a workaround is to temporarily change the configuration value by using <code>git -c submodule.recurse=0</code>. </p>
 </dd></dl>
<p> submodule.fetchJobs </p>
<dl>
<dd> <p> Specifies how many submodules are fetched/cloned at the same time. A positive integer allows up to that number of submodules fetched in parallel. A value of 0 will give some reasonable default. If unset, it defaults to 1. </p>
 </dd></dl>
<p> submodule.alternateLocation </p>
<dl>
<dd> <p> Specifies how the submodules obtain alternates when submodules are cloned. Possible values are <code>no</code>, <code>superproject</code>. By default <code>no</code> is assumed, which doesn&#8217;t add references. When the value is set to <code>superproject</code> the submodule to be cloned computes its alternates location relative to the superprojects alternate. </p>
 </dd></dl>
<p> submodule.alternateErrorStrategy </p>
<dl>
<dd> <p> Specifies how to treat errors with the alternates for a submodule as computed via <code>submodule.alternateLocation</code>. Possible values are <code>ignore</code>, <code>info</code>, <code>die</code>. Default is <code>die</code>. Note that if set to <code>ignore</code> or <code>info</code>, and if there is an error with the computed alternate, the clone proceeds as if no alternate was specified. </p>
 </dd></dl>
<p> tag.forceSignAnnotated </p>
<dl>
<dd> <p> A boolean to specify whether annotated tags created should be GPG signed. If <code>--annotate</code> is specified on the command line, it takes precedence over this option. </p>
 </dd></dl>
<p> tag.sort </p>
<dl>
<dd> <p> This variable controls the sort ordering of tags when displayed by <code><a href="/docs/linux/man/1-git-tag/">git-tag</a></code>(1). Without the &quot;--sort=&lt;value&gt;&quot; option provided, the value of this variable will be used as the default. </p>
 </dd></dl>
<p> tag.gpgSign </p>
<dl>
<dd> <p> A boolean to specify whether all tags should be GPG signed. Use of this option when running in an automated script can result in a large number of tags being signed. It is therefore convenient to use an agent to avoid typing your gpg passphrase several times. Note that this option doesn&#8217;t affect tag signing behavior enabled by &quot;-u &lt;keyid&gt;&quot; or &quot;--local-user=&lt;keyid&gt;&quot; options. </p>
 </dd></dl>
<p> tar.umask </p>
<dl>
<dd> <p> This variable can be used to restrict the permission bits of tar archive entries. The default is 0002, which turns off the world write bit. The special value &quot;user&quot; indicates that the archiving user&#8217;s umask will be used instead. See <a href="/docs/linux/man/2-umask/">umask</a>(2) and <code><a href="/docs/linux/man/1-git-archive/">git-archive</a></code>(1). </p>
 </dd></dl>
<p> Trace2 config settings are only read from the system and global config files; repository local and worktree config files and <code>-c</code> command line arguments are not respected. </p>
<p> trace2.normalTarget </p>
<dl>
<dd> <p> This variable controls the normal target destination. It may be overridden by the <code>GIT_TRACE2</code> environment variable. The following table shows possible values. </p>
 </dd></dl>
<p> trace2.perfTarget </p>
<dl>
<dd> <p> This variable controls the performance target destination. It may be overridden by the <code>GIT_TRACE2_PERF</code> environment variable. The following table shows possible values. </p>
 </dd></dl>
<p> trace2.eventTarget </p>
<dl>
<dd> <p> This variable controls the event target destination. It may be overridden by the <code>GIT_TRACE2_EVENT</code> environment variable. The following table shows possible values. </p>
 </dd>
<dl>
<dd> <p> &bull; <code>0</code> or <code>false</code> - Disables the target. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>1</code> or <code>true</code> - Writes to <code>STDERR</code>. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>[2-9]</code> - Writes to the already opened file descriptor. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>&lt;absolute-pathname&gt;</code> - Writes to the file in append mode. If the target already exists and is a directory, the traces will be written to files (one per process) underneath the given directory. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>af_unix:[&lt;socket_type&gt;:]&lt;absolute-pathname&gt;</code> - Write to a Unix DomainSocket (on platforms that support them). Socket type can be either <code>stream</code> or <code>dgram</code>; if omitted Git will try both. </p>
 </dd></dl>
</dl>
<p> trace2.normalBrief </p>
<dl>
<dd> <p> Boolean. When true <code>time</code>, <code>filename</code>, and <code>line</code> fields are omitted from normal output. May be overridden by the <code>GIT_TRACE2_BRIEF</code> environment variable. Defaults to false. </p>
 </dd></dl>
<p> trace2.perfBrief </p>
<dl>
<dd> <p> Boolean. When true <code>time</code>, <code>filename</code>, and <code>line</code> fields are omitted from PERF output. May be overridden by the <code>GIT_TRACE2_PERF_BRIEF</code> environment variable. Defaults to false. </p>
 </dd></dl>
<p> trace2.eventBrief </p>
<dl>
<dd> <p> Boolean. When true <code>time</code>, <code>filename</code>, and <code>line</code> fields are omitted from event output. May be overridden by the <code>GIT_TRACE2_EVENT_BRIEF</code> environment variable. Defaults to false. </p>
 </dd></dl>
<p> trace2.eventNesting </p>
<dl>
<dd> <p> Integer. Specifies desired depth of nested regions in the event output. Regions deeper than this value will be omitted. May be overridden by the <code>GIT_TRACE2_EVENT_NESTING</code> environment variable. Defaults to 2. </p>
 </dd></dl>
<p> trace2.configParams </p>
<dl>
<dd> <p> A comma-separated list of patterns of &quot;important&quot; config settings that should be recorded in the trace2 output. For example, <code>core.*,remote.*.url</code> would cause the trace2 output to contain events listing each configured remote. May be overridden by the <code>GIT_TRACE2_CONFIG_PARAMS</code> environment variable. Unset by default. </p>
 </dd></dl>
<p> trace2.envVars </p>
<dl>
<dd> <p> A comma-separated list of &quot;important&quot; environment variables that should be recorded in the trace2 output. For example, <code>GIT_HTTP_USER_AGENT,GIT_CONFIG</code> would cause the trace2 output to contain events listing the overrides for HTTP user agent and the location of the Git configuration file (assuming any are set). May be overridden by the <code>GIT_TRACE2_ENV_VARS</code> environment variable. Unset by default. </p>
 </dd></dl>
<p> trace2.destinationDebug </p>
<dl>
<dd> <p> Boolean. When true Git will print error messages when a trace target destination cannot be opened for writing. By default, these errors are suppressed and tracing is silently disabled. May be overridden by the <code>GIT_TRACE2_DST_DEBUG</code> environment variable. </p>
 </dd></dl>
<p> trace2.maxFiles </p>
<dl>
<dd> <p> Integer. When writing trace files to a target directory, do not write additional traces if we would exceed this many files. Instead, write a sentinel file that will block further tracing to this directory. Defaults to 0, which disables this check. </p>
 </dd></dl>
<p> transfer.fsckObjects </p>
<dl>
<dd> <p> When <code>fetch.fsckObjects</code> or <code>receive.fsckObjects</code> are not set, the value of this variable is used instead. Defaults to false. </p>
<p> When set, the fetch or receive will abort in the case of a malformed object or a link to a nonexistent object. In addition, various other issues are checked for, including legacy issues (see <code>fsck.&lt;msg-id&gt;</code>), and potential security issues like the existence of a <code>.GIT</code> directory or a malicious <code>.gitmodules</code> file (see the release notes for v2.2.1 and v2.17.1 for details). Other sanity and security checks may be added in future releases. </p>
<p> On the receiving side, failing fsckObjects will make those objects unreachable, see &quot;QUARANTINE ENVIRONMENT&quot; in <code><a href="/docs/linux/man/1-git-receive-pack/">git-receive-pack</a></code>(1). On the fetch side, malformed objects will instead be left unreferenced in the repository. </p>
<p> Due to the non-quarantine nature of the <code>fetch.fsckObjects</code> implementation it cannot be relied upon to leave the object store clean like <code>receive.fsckObjects</code> can. </p>
<p> As objects are unpacked they&#8217;re written to the object store, so there can be cases where malicious objects get introduced even though the &quot;fetch&quot; failed, only to have a subsequent &quot;fetch&quot; succeed because only new incoming objects are checked, not those that have already been written to the object store. That difference in behavior should not be relied upon. In the future, such objects may be quarantined for &quot;fetch&quot; as well. </p>
<p> For now, the paranoid need to find some way to emulate the quarantine environment if they&#8217;d like the same protection as &quot;push&quot;. E.g. in the case of an internal mirror do the mirroring in two steps, one to fetch the untrusted objects, and then do a second &quot;push&quot; (which will use the quarantine) to another internal repo, and have internal clients consume this pushed-to repository, or embargo internal fetches and only allow them once a full &quot;fsck&quot; has run (and no new fetches have happened in the meantime). </p>
 </dd></dl>
<p> transfer.hideRefs </p>
<dl>
<dd> <p> String(s) <code>receive-pack</code> and <code>upload-pack</code> use to decide which refs to omit from their initial advertisements. Use more than one definition to specify multiple prefix strings. A ref that is under the hierarchies listed in the value of this variable is excluded, and is hidden when responding to <code>git push</code> or <code>git fetch</code>. See <code>receive.hideRefs</code> and <code>uploadpack.hideRefs</code> for program-specific versions of this config. </p>
<p> You may also include a <code>!</code> in front of the ref name to negate the entry, explicitly exposing it, even if an earlier entry marked it as hidden. If you have multiple hideRefs values, later entries override earlier ones (and entries in more-specific config files override less-specific ones). </p>
<p> If a namespace is in use, the namespace prefix is stripped from each reference before it is matched against <code>transfer.hiderefs</code> patterns. In order to match refs before stripping, add a <code>^</code> in front of the ref name. If you combine <code>!</code> and <code>^</code>, <code>!</code> must be specified first. </p>
<p> For example, if <code>refs/heads/master</code> is specified in <code>transfer.hideRefs</code> and the current namespace is <code>foo</code>, then <code>refs/namespaces/foo/refs/heads/master</code> is omitted from the advertisements. If <code>uploadpack.allowRefInWant</code> is set, <code>upload-pack</code> will treat <code>want-ref refs/heads/master</code> in a protocol v2 <code>fetch</code> command as if <code>refs/namespaces/foo/refs/heads/master</code> did not exist. <code>receive-pack</code>, on the other hand, will still advertise the object id the ref is pointing to without mentioning its name (a so-called &quot;.have&quot; line). </p>
<p> Even if you hide refs, a client may still be able to steal the target objects via the techniques described in the &quot;SECURITY&quot; section of the <code><a href="/docs/linux/man/7-gitnamespaces/">gitnamespaces</a></code>(7) man page; it&#8217;s best to keep private data in a separate repository. </p>
 </dd></dl>
<p> transfer.unpackLimit </p>
<dl>
<dd> <p> When <code>fetch.unpackLimit</code> or <code>receive.unpackLimit</code> are not set, the value of this variable is used instead. The default value is 100. </p>
 </dd></dl>
<p> transfer.advertiseSID </p>
<dl>
<dd> <p> Boolean. When true, client and server processes will advertise their unique session IDs to their remote counterpart. Defaults to false. </p>
 </dd></dl>
<p> uploadarchive.allowUnreachable </p>
<dl>
<dd> <p> If true, allow clients to use <code>git archive --remote</code> to request any tree, whether reachable from the ref tips or not. See the discussion in the &quot;SECURITY&quot; section of <code><a href="/docs/linux/man/1-git-upload-archive/">git-upload-archive</a></code>(1) for more details. Defaults to <code>false</code>. </p>
 </dd></dl>
<p> uploadpack.hideRefs </p>
<dl>
<dd> <p> This variable is the same as <code>transfer.hideRefs</code>, but applies only to <code>upload-pack</code> (and so affects only fetches, not pushes). An attempt to fetch a hidden ref by <code>git fetch</code> will fail. See also <code>uploadpack.allowTipSHA1InWant</code>. </p>
 </dd></dl>
<p> uploadpack.allowTipSHA1InWant </p>
<dl>
<dd> <p> When <code>uploadpack.hideRefs</code> is in effect, allow <code>upload-pack</code> to accept a fetch request that asks for an object at the tip of a hidden ref (by default, such a request is rejected). See also <code>uploadpack.hideRefs</code>. Even if this is false, a client may be able to steal objects via the techniques described in the &quot;SECURITY&quot; section of the <code><a href="/docs/linux/man/7-gitnamespaces/">gitnamespaces</a></code>(7) man page; it&#8217;s best to keep private data in a separate repository. </p>
 </dd></dl>
<p> uploadpack.allowReachableSHA1InWant </p>
<dl>
<dd> <p> Allow <code>upload-pack</code> to accept a fetch request that asks for an object that is reachable from any ref tip. However, note that calculating object reachability is computationally expensive. Defaults to <code>false</code>. Even if this is false, a client may be able to steal objects via the techniques described in the &quot;SECURITY&quot; section of the <code><a href="/docs/linux/man/7-gitnamespaces/">gitnamespaces</a></code>(7) man page; it&#8217;s best to keep private data in a separate repository. </p>
 </dd></dl>
<p> uploadpack.allowAnySHA1InWant </p>
<dl>
<dd> <p> Allow <code>upload-pack</code> to accept a fetch request that asks for any object at all. Defaults to <code>false</code>. </p>
 </dd></dl>
<p> uploadpack.keepAlive </p>
<dl>
<dd> <p> When <code>upload-pack</code> has started <code>pack-objects</code>, there may be a quiet period while <code>pack-objects</code> prepares the pack. Normally it would output progress information, but if <code>--quiet</code> was used for the fetch, <code>pack-objects</code> will output nothing at all until the pack data begins. Some clients and networks may consider the server to be hung and give up. Setting this option instructs <code>upload-pack</code> to send an empty keepalive packet every <code>uploadpack.keepAlive</code> seconds. Setting this option to 0 disables keepalive packets entirely. The default is 5 seconds. </p>
 </dd></dl>
<p> uploadpack.packObjectsHook </p>
<dl>
<dd> <p> If this option is set, when <code>upload-pack</code> would run <code>git pack-objects</code> to create a packfile for a client, it will run this shell command instead. The <code>pack-objects</code> command and arguments it <i>would</i> have run (including the <code>git pack-objects</code> at the beginning) are appended to the shell command. The stdin and stdout of the hook are treated as if <code>pack-objects</code> itself was run. I.e., <code>upload-pack</code> will feed input intended for <code>pack-objects</code> to the hook, and expects a completed packfile on stdout. </p>
<p> Note that this configuration variable is ignored if it is seen in the repository-level config (this is a safety measure against fetching from untrusted repositories). </p>
 </dd></dl>
<p> uploadpack.allowFilter </p>
<dl>
<dd> <p> If this option is set, <code>upload-pack</code> will support partial clone and partial fetch object filtering. </p>
 </dd></dl>
<p> uploadpackfilter.allow </p>
<dl>
<dd> <p> Provides a default value for unspecified object filters (see: the below configuration variable). If set to <code>true</code>, this will also enable all filters which get added in the future. Defaults to <code>true</code>. </p>
 </dd></dl>
<p> uploadpackfilter.&lt;filter&gt;.allow </p>
<dl>
<dd> <p> Explicitly allow or ban the object filter corresponding to <code>&lt;filter&gt;</code>, where <code>&lt;filter&gt;</code> may be one of: <code>blob:none</code>, <code>blob:limit</code>, <code>object:type</code>, <code>tree</code>, <code>sparse:oid</code>, or <code>combine</code>. If using combined filters, both <code>combine</code> and all of the nested filter kinds must be allowed. Defaults to <code>uploadpackfilter.allow</code>. </p>
 </dd></dl>
<p> uploadpackfilter.tree.maxDepth </p>
<dl>
<dd> <p> Only allow <code>--filter=tree:&lt;n&gt;</code> when <code>&lt;n&gt;</code> is no more than the value of <code>uploadpackfilter.tree.maxDepth</code>. If set, this also implies <code>uploadpackfilter.tree.allow=true</code>, unless this configuration variable had already been set. Has no effect if unset. </p>
 </dd></dl>
<p> uploadpack.allowRefInWant </p>
<dl>
<dd> <p> If this option is set, <code>upload-pack</code> will support the <code>ref-in-want</code> feature of the protocol version 2 <code>fetch</code> command. This feature is intended for the benefit of load-balanced servers which may not have the same view of what OIDs their refs point to due to replication delay. </p>
 </dd></dl>
<p> url.&lt;base&gt;.insteadOf </p>
<dl>
<dd> <p> Any URL that starts with this value will be rewritten to start, instead, with &lt;base&gt;. In cases where some site serves a large number of repositories, and serves them with multiple access methods, and some users need to use different access methods, this feature allows people to specify any of the equivalent URLs and have Git automatically rewrite the URL to the best alternative for the particular user, even for a never-before-seen repository on the site. When more than one insteadOf strings match a given URL, the longest match is used. </p>
<p> Note that any protocol restrictions will be applied to the rewritten URL. If the rewrite changes the URL to use a custom protocol or remote helper, you may need to adjust the <code>protocol.*.allow</code> config to permit the request. In particular, protocols you expect to use for submodules must be set to <code>always</code> rather than the default of <code>user</code>. See the description of <code>protocol.allow</code> above. </p>
 </dd></dl>
<p> url.&lt;base&gt;.pushInsteadOf </p>
<dl>
<dd> <p> Any URL that starts with this value will not be pushed to; instead, it will be rewritten to start with &lt;base&gt;, and the resulting URL will be pushed to. In cases where some site serves a large number of repositories, and serves them with multiple access methods, some of which do not allow push, this feature allows people to specify a pull-only URL and have Git automatically use an appropriate URL to push, even for a never-before-seen repository on the site. When more than one pushInsteadOf strings match a given URL, the longest match is used. If a remote has an explicit pushurl, Git will ignore this setting for that remote. </p>
 </dd></dl>
<p> user.name, user.email, author.name, author.email, committer.name, committer.email </p>
<dl>
<dd> <p> The <code>user.name</code> and <code>user.email</code> variables determine what ends up in the <code>author</code> and <code>committer</code> field of commit objects. If you need the <code>author</code> or <code>committer</code> to be different, the <code>author.name</code>, <code>author.email</code>, <code>committer.name</code> or <code>committer.email</code> variables can be set. Also, all of these can be overridden by the <code>GIT_AUTHOR_NAME</code>, <code>GIT_AUTHOR_EMAIL</code>, <code>GIT_COMMITTER_NAME</code>, <code>GIT_COMMITTER_EMAIL</code> and <code>EMAIL</code> environment variables. </p>
<p> Note that the <code>name</code> forms of these variables conventionally refer to some form of a personal name. See <code><a href="/docs/linux/man/1-git-commit/">git-commit</a></code>(1) and the environment variables section of <code><a href="/docs/linux/man/1-git/">git</a></code>(1) for more information on these settings and the <code>credential.username</code> option if you&#8217;re looking for authentication credentials instead. </p>
 </dd></dl>
<p> user.useConfigOnly </p>
<dl>
<dd> <p> Instruct Git to avoid trying to guess defaults for <code>user.email</code> and <code>user.name</code>, and instead retrieve the values only from the configuration. For example, if you have multiple email addresses and would like to use a different one for each repository, then with this configuration option set to <code>true</code> in the global config along with a name, Git will prompt you to set up an email before making new commits in a newly cloned repository. Defaults to <code>false</code>. </p>
 </dd></dl>
<p> user.signingKey </p>
<dl>
<dd> <p> If <code><a href="/docs/linux/man/1-git-tag/">git-tag</a></code>(1) or <code><a href="/docs/linux/man/1-git-commit/">git-commit</a></code>(1) is not selecting the key you want it to automatically when creating a signed tag or commit, you can override the default selection with this variable. This option is passed unchanged to gpg&#8217;s --local-user parameter, so you may specify a key using any method that gpg supports. If gpg.format is set to &quot;ssh&quot; this can contain the literal ssh public key (e.g.: &quot;ssh-rsa XXXXXX identifier&quot;) or a file which contains it and corresponds to the private key used for signing. The private key needs to be available via ssh-agent. Alternatively it can be set to a file containing a private key directly. If not set git will call gpg.ssh.defaultKeyCommand (e.g.: &quot;ssh-add -L&quot;) and try to use the first key available. </p>
 </dd></dl>
<p> versionsort.prereleaseSuffix (deprecated) </p>
<dl>
<dd> <p> Deprecated alias for <code>versionsort.suffix</code>. Ignored if <code>versionsort.suffix</code> is set. </p>
 </dd></dl>
<p> versionsort.suffix </p>
<dl>
<dd> <p> Even when version sort is used in <code><a href="/docs/linux/man/1-git-tag/">git-tag</a></code>(1), tagnames with the same base version but different suffixes are still sorted lexicographically, resulting e.g. in prerelease tags appearing after the main release (e.g. &quot;1.0-rc1&quot; after &quot;1.0&quot;). This variable can be specified to determine the sorting order of tags with different suffixes. </p>
<p> By specifying a single suffix in this variable, any tagname containing that suffix will appear before the corresponding main release. E.g. if the variable is set to &quot;-rc&quot;, then all &quot;1.0-rcX&quot; tags will appear before &quot;1.0&quot;. If specified multiple times, once per suffix, then the order of suffixes in the configuration will determine the sorting order of tagnames with those suffixes. E.g. if &quot;-pre&quot; appears before &quot;-rc&quot; in the configuration, then all &quot;1.0-preX&quot; tags will be listed before any &quot;1.0-rcX&quot; tags. The placement of the main release tag relative to tags with various suffixes can be determined by specifying the empty suffix among those other suffixes. E.g. if the suffixes &quot;-rc&quot;, &quot;&quot;, &quot;-ck&quot; and &quot;-bfs&quot; appear in the configuration in this order, then all &quot;v4.8-rcX&quot; tags are listed first, followed by &quot;v4.8&quot;, then &quot;v4.8-ckX&quot; and finally &quot;v4.8-bfsX&quot;. </p>
<p> If more than one suffixes match the same tagname, then that tagname will be sorted according to the suffix which starts at the earliest position in the tagname. If more than one different matching suffixes start at that earliest position, then that tagname will be sorted according to the longest of those suffixes. The sorting order between different suffixes is undefined if they are in multiple config files. </p>
 </dd></dl>
<p> web.browser </p>
<dl>
<dd> <p> Specify a web browser that may be used by some commands. Currently only <code><a href="/docs/linux/man/1-git-instaweb/">git-instaweb</a></code>(1) and <code><a href="/docs/linux/man/1-git-help/">git-help</a></code>(1) may use it. </p>
 </dd></dl>
<p> worktree.guessRemote </p>
<dl>
<dd> <p> If no branch is specified and neither <code>-b</code> nor <code>-B</code> nor <code>--detach</code> is used, then <code>git worktree add</code> defaults to creating a new branch from HEAD. If <code>worktree.guessRemote</code> is set to true, <code>worktree add</code> tries to find a remote-tracking branch whose name uniquely matches the new branch name. If such a branch exists, it is checked out and set as &quot;upstream&quot; for the new branch. If no such match can be found, it falls back to creating a new branch from the current HEAD. </p>
 </dd></dl>
<h2>BUGS</h2>
<p> When using the deprecated <code>[section.subsection]</code> syntax, changing a value will result in adding a multi-line key instead of a change, if the subsection is given with at least one uppercase character. For example when the config looks like </p>
<dl>
<dd> <pre><code>  [section.subsection]
    key = value1
</code></pre>
 </dd></dl>
<p> and running <code>git config section.Subsection.key value2</code> will result in </p>
<dl>
<dd> <pre><code>  [section.subsection]
    key = value1
    key = value2
</code></pre>
 </dd></dl>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite  </p>
<h2>NOTES</h2>
<dl>
<dt> 1.</dt>
<dd> <p> user1 [at] example.com </p>
 </dd>
<dl>
<dd> <p> mailto:user1 [at] example.com </p>
 </dd></dl>
<dt> 2.</dt>
<dd> <p> user2 [at] example.com </p>
 </dd>
<dl>
<dd> <p> mailto:user2 [at] example.com </p>
 </dd></dl>
<dt> 3.</dt>
<dd> <p> Documentation/technical/pack-format.txt </p>
 </dd>
<dl>
<dd> <p> file:///usr/share/doc/git/html/../technical/pack-format.html </p>
 </dd></dl>
<dt> 4.</dt>
<dd> <p> wire protocol version 2 </p>
 </dd>
<dl>
<dd> <p> file:///usr/share/doc/git/html/technical/protocol-v2.html </p>
 </dd></dl>
