---
title: "hgrc(5)"
name: "hgrc"
section: "5"
letter: "h"
url: "/docs/linux/man/5-hgrc/"
description: "hgrc – configuration files for Mercurial"
---

<p>hgrc &#8211; configuration files for Mercurial</p>
<h2>Synopsis</h2>
<p>The Mercurial system uses a set of configuration files to control aspects of its behavior. </p>
<p> The configuration files use a simple ini-file format. A configuration file consists of sections, led by a <code>[section]</code> header and followed by <code>name = value</code> entries: </p>
<pre>[ui]
username = Firstname Lastname &lt;firstname.lastname [at] example.net&gt;
verbose = True</pre>
<p>The above entries will be referred to as <code>ui.username</code> and <code>ui.verbose</code>, respectively. See the Syntax section below.</p>
<h2>Files</h2>
<p>Mercurial reads configuration data from several files, if they exist. These files do not exist by default and you will have to create the appropriate configuration files yourself: global configuration like the username setting is typically put into <code>%USERPROFILE%\mercurial.ini</code> or <code>$HOME/.hgrc</code> and local configuration is put into the per-repository <code>&lt;repo&gt;/.hg/hgrc</code> file. </p>
<p> The names of these files depend on the system on which Mercurial is installed. <code>*.rc</code> files from a single directory are read in alphabetical order, later ones overriding earlier ones. Where multiple paths are given below, settings from earlier paths override later ones. </p>
<pre>(All) <code>&lt;repo&gt;/.hg/hgrc</code></pre>
<p>Per-repository configuration options that only apply in a particular repository. This file is not version-controlled, and will not get transferred during a &quot;clone&quot; operation. Options in this file override options in all other configuration files. On Plan 9 and Unix, most of this file will be ignored if it doesn&#8217;t belong to a trusted user or to a trusted group. See the documentation for the <code>[trusted]</code> section below for more details. </p>
<pre>(Plan 9) <code>$home/lib/hgrc</code>
(Unix) <code>$HOME/.hgrc</code>
(Windows) <code>%USERPROFILE%\.hgrc</code>
(Windows) <code>%USERPROFILE%\Mercurial.ini</code>
(Windows) <code>%HOME%\.hgrc</code>
(Windows) <code>%HOME%\Mercurial.ini</code></pre>
<p>Per-user configuration file(s), for the user running Mercurial. On Windows 9x, <code>%HOME%</code> is replaced by <code>%APPDATA%</code>. Options in these files apply to all Mercurial commands executed by this user in any directory. Options in these files override per-system and per-installation options. </p>
<pre>(Plan 9) <code>/lib/mercurial/hgrc</code>
(Plan 9) <code>/lib/mercurial/hgrc.d/*.rc</code>
(Unix) <code>/etc/mercurial/hgrc</code>
(Unix) <code>/etc/mercurial/hgrc.d/*.rc</code></pre>
<p>Per-system configuration files, for the system on which Mercurial is running. Options in these files apply to all Mercurial commands executed by any user in any directory. Options in these files override per-installation options. </p>
<pre>(Plan 9) <code>&lt;install-root&gt;/lib/mercurial/hgrc</code>
(Plan 9) <code>&lt;install-root&gt;/lib/mercurial/hgrc.d/*.rc</code>
(Unix) <code>&lt;install-root&gt;/etc/mercurial/hgrc</code>
(Unix) <code>&lt;install-root&gt;/etc/mercurial/hgrc.d/*.rc</code></pre>
<p>Per-installation configuration files, searched for in the directory where Mercurial is installed. <code>&lt;install-root&gt;</code> is the parent directory of the <code>hg</code> executable (or symlink) being run. For example, if installed in <code>/shared/tools/bin/hg</code>, Mercurial will look in <code>/shared/tools/etc/mercurial/hgrc</code>. Options in these files apply to all Mercurial commands executed by any user in any directory. </p>
<pre>(Windows) <code>&lt;install-dir&gt;\Mercurial.ini</code> <code>or</code>
(Windows) <code>&lt;install-dir&gt;\hgrc.d\*.rc</code> <code>or</code>
(Windows) <code>HKEY_LOCAL_MACHINE\SOFTWARE\Mercurial</code></pre>
<p>Per-installation/system configuration files, for the system on which Mercurial is running. Options in these files apply to all Mercurial commands executed by any user in any directory. Registry keys contain PATH-like strings, every part of which must reference a <code>Mercurial.ini</code> file or be a directory where <code>*.rc</code> files will be read. Mercurial checks each of these locations in the specified order until one or more configuration files are detected.</p>
<dl>
<dt>Note</p>
<dd>The registry key <code>HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Mercurial</code> is used when running 32-bit Python on 64-bit Windows.</dl>
<h2>Syntax</h2>
<p>A configuration file consists of sections, led by a <code>[section]</code> header and followed by <code>name = value</code> entries (sometimes called <code>configuration keys</code>): </p>
<pre>[spam]
eggs=ham
green=
 eggs</pre>
<p>Each line contains one entry. If the lines that follow are indented, they are treated as continuations of that entry. Leading whitespace is removed from values. Empty lines are skipped. Lines beginning with <code>#</code> or <code>;</code> are ignored and may be used to provide comments. </p>
<p> Configuration keys can be set multiple times, in which case Mercurial will use the value that was configured last. As an example: </p>
<pre>[spam]
eggs=large
ham=serrano
eggs=small</pre>
<p>This would set the configuration key named <code>eggs</code> to <code>small</code>. </p>
<p> It is also possible to define a section multiple times. A section can be redefined on the same and/or on different configuration files. For example: </p>
<pre>[foo]
eggs=large
ham=serrano
eggs=small
[bar]
eggs=ham
green=
 eggs
[foo]
ham=prosciutto
eggs=medium
bread=toasted</pre>
<p>This would set the <code>eggs</code>, <code>ham</code>, and <code>bread</code> configuration keys of the <code>foo</code> section to <code>medium</code>, <code>prosciutto</code>, and <code>toasted</code>, respectively. As you can see there only thing that matters is the last value that was set for each of the configuration keys. </p>
<p> If a configuration key is set multiple times in different configuration files the final value will depend on the order in which the different configuration files are read, with settings from earlier paths overriding later ones as described on the <code>Files</code> section above. </p>
<p> A line of the form <code>%include file</code> will include <code>file</code> into the current configuration file. The inclusion is recursive, which means that included files can include other files. Filenames are relative to the configuration file in which the <code>%include</code> directive is found. Environment variables and <code>~user</code> constructs are expanded in <code>file</code>. This lets you do something like: </p>
<pre>%include ~/.hgrc.d/$HOST.rc</pre>
<p>to include a different configuration file on each computer you use. </p>
<p> A line with <code>%unset name</code> will remove <code>name</code> from the current section, if it has been set previously. </p>
<p> The values are either free-form text strings, lists of text strings, or Boolean values. Boolean values can be set to true using any of &quot;1&quot;, &quot;yes&quot;, &quot;true&quot;, or &quot;on&quot; and to false using &quot;0&quot;, &quot;no&quot;, &quot;false&quot;, or &quot;off&quot; (all case insensitive). </p>
<p> List values are separated by whitespace or comma, except when values are placed in double quotation marks: </p>
<pre>allow_read = &quot;John Doe, PhD&quot;, brian, betty</pre>
<p>Quotation marks can be escaped by prefixing them with a backslash. Only quotation marks at the beginning of a word is counted as a quotation (e.g., <code>foo&quot;bar baz</code> is the list of <code>foo&quot;bar</code> and <code>baz</code>).</p>
<h2>Sections</h2>
<p>This section describes the different sections that may appear in a Mercurial configuration file, the purpose of each section, its possible keys, and their possible values.</p>
<h3><code>alias</code></h3>
<p>Defines command aliases. Aliases allow you to define your own commands in terms of other commands (or aliases), optionally including arguments. Positional arguments in the form of <code>$1</code>, <code>$2</code>, etc in the alias definition are expanded by Mercurial before execution. Positional arguments not already used by <code>$N</code> in the definition are put at the end of the command to be executed. </p>
<p> Alias definitions consist of lines of the form: </p>
<pre>&lt;alias&gt; = &lt;command&gt; [&lt;argument&gt;]...</pre>
<p>For example, this definition: </p>
<pre>latest = log --limit 5</pre>
<p>creates a new command <code>latest</code> that shows only the five most recent changesets. You can define subsequent aliases using earlier ones: </p>
<pre>stable5 = latest -b stable</pre>
<dl>
<dt>Note</p>
<dd>It is possible to create aliases with the same names as existing commands, which will then override the original definitions. This is almost always a bad idea! </p>
<p> An alias can start with an exclamation point (<code>!</code>) to make it a shell alias. A shell alias is executed with the shell and will let you run arbitrary commands. As an example, </p>
<pre>echo = !echo $@</pre>
<p>will let you do <code>hg echo foo</code> to have <code>foo</code> printed in your terminal. A better example might be: </p>
<pre>purge = !$HG status --no-status --unknown -0 | xargs -0 rm</pre>
<p>which will make <code>hg purge</code> delete all unknown files in the repository in the same manner as the purge extension. </p>
<p> Positional arguments like <code>$1</code>, <code>$2</code>, etc. in the alias definition expand to the command arguments. Unmatched arguments are removed. <code>$0</code> expands to the alias name and <code>$@</code> expands to all arguments separated by a space. These expansions happen before the command is passed to the shell. </p>
<p> Shell aliases are executed in an environment where <code>$HG</code> expands to the path of the Mercurial that was used to execute the alias. This is useful when you want to call further Mercurial commands in a shell alias, as was done above for the purge alias. In addition, <code>$HG_ARGS</code> expands to the arguments given to Mercurial. In the <code>hg echo foo</code> call above, <code>$HG_ARGS</code> would expand to <code>echo foo</code>.</p>
<dt>Note</p>
<dd>Some global configuration options such as <code>-R</code> are processed before shell aliases and will thus not be passed to aliases.</dl>
<h3><code>annotate</code></h3>
<p>Settings used when displaying file annotations. All values are Booleans and default to False. See <code>diff</code> section for related options for the diff command.</p>
<dl>
<dt><code>ignorews</code></p>
<dd>Ignore white space when comparing lines.</p>
<dt><code>ignorewsamount</code></p>
<dd>Ignore changes in the amount of white space.</p>
<dt><code>ignoreblanklines</code></p>
<dd>Ignore changes whose lines are all blank.</dl>
<h3><code>auth</code></h3>
<p>Authentication credentials for HTTP authentication. This section allows you to store usernames and passwords for use when logging <i>into</i> HTTP servers. See the <code>[web]</code> configuration section if you want to configure <i>who</i> can login to your HTTP server. </p>
<p> Each line has the following format: </p>
<pre>&lt;name&gt;.&lt;argument&gt; = &lt;value&gt;</pre>
<p>where <code>&lt;name&gt;</code> is used to group arguments into authentication entries. Example: </p>
<pre>foo.prefix = hg.intevation.org/mercurial
foo.username = foo
foo.password = bar
foo.schemes = http https
bar.prefix = secure.example.org
bar.key = path/to/file.key
bar.cert = path/to/file.cert
bar.schemes = https</pre>
<p>Supported arguments:</p>
<dl>
<dt><code>prefix</code></p>
<dd>Either <code>*</code> or a URI prefix with or without the scheme part. The authentication entry with the longest matching prefix is used (where <code>*</code> matches everything and counts as a match of length 1). If the prefix doesn&#8217;t include a scheme, the match is performed against the URI with its scheme stripped as well, and the schemes argument, q.v., is then subsequently consulted.</p>
<dt><code>username</code></p>
<dd>Optional. Username to authenticate with. If not given, and the remote site requires basic or digest authentication, the user will be prompted for it. Environment variables are expanded in the username letting you do <code>foo.username = $USER</code>. If the URI includes a username, only <code>[auth]</code> entries with a matching username or without a username will be considered.</p>
<dt><code>password</code></p>
<dd>Optional. Password to authenticate with. If not given, and the remote site requires basic or digest authentication, the user will be prompted for it.</p>
<dt><code>key</code></p>
<dd>Optional. PEM encoded client certificate key file. Environment variables are expanded in the filename.</p>
<dt><code>cert</code></p>
<dd>Optional. PEM encoded client certificate chain file. Environment variables are expanded in the filename.</p>
<dt><code>schemes</code></p>
<dd>Optional. Space separated list of URI schemes to use this authentication entry with. Only used if the prefix doesn&#8217;t include a scheme. Supported schemes are http and https. They will match static-http and static-https respectively, as well. Default: https. </p>
<p> If no suitable authentication entry is found, the user is prompted for credentials as usual if required by the remote.</dl>
<h3><code>decode/encode</code></h3>
<p>Filters for transforming files on checkout/checkin. This would typically be used for newline processing or other localization/canonicalization of files. </p>
<p> Filters consist of a filter pattern followed by a filter command. Filter patterns are globs by default, rooted at the repository root. For example, to match any file ending in <code>.txt</code> in the root directory only, use the pattern <code>*.txt</code>. To match any file ending in <code>.c</code> anywhere in the repository, use the pattern <code>**.c</code>. For each file only the first matching filter applies. </p>
<p> The filter command can start with a specifier, either <code>pipe:</code> or <code>tempfile:</code>. If no specifier is given, <code>pipe:</code> is used by default. </p>
<p> A <code>pipe:</code> command must accept data on stdin and return the transformed data on stdout. </p>
<p> Pipe example: </p>
<pre>[encode]
# uncompress gzip files on checkin to improve delta compression
# note: not necessarily a good idea, just an example
*.gz = pipe: gunzip
[decode]
# recompress gzip files when writing them to the working dir (we
# can safely omit &quot;pipe:&quot;, because it's the default)
*.gz = gzip</pre>
<p>A <code>tempfile:</code> command is a template. The string <code>INFILE</code> is replaced with the name of a temporary file that contains the data to be filtered by the command. The string <code>OUTFILE</code> is replaced with the name of an empty temporary file, where the filtered data must be written by the command.</p>
<dl>
<dt>Note</p>
<dd>The tempfile mechanism is recommended for Windows systems, where the standard shell I/O redirection operators often have strange effects and may corrupt the contents of your files. </p>
<p> This filter mechanism is used internally by the <code>eol</code> extension to translate line ending characters between Windows (CRLF) and Unix (LF) format. We suggest you use the <code>eol</code> extension for convenience.</dl>
<h3><code>defaults</code></h3>
<p>(defaults are deprecated. Don&#8217;t use them. Use aliases instead) </p>
<p> Use the <code>[defaults]</code> section to define command defaults, i.e. the default options/arguments to pass to the specified commands. </p>
<p> The following example makes <code>hg log</code>: run in verbose mode, and <code>hg status</code>: show only the modified files, by default: </p>
<pre>[defaults]
log = -v
status = -m</pre>
<p>The actual commands, instead of their aliases, must be used when defining command defaults. The command defaults will also be applied to the aliases of the commands defined.</p>
<h3><code>diff</code></h3>
<p>Settings used when displaying diffs. Everything except for <code>unified</code> is a Boolean and defaults to False. See <code>annotate</code> section for related options for the annotate command.</p>
<dl>
<dt><code>git</code></p>
<dd>Use git extended diff format.</p>
<dt><code>nodates</code></p>
<dd>Don&#8217;t include dates in diff headers.</p>
<dt><code>showfunc</code></p>
<dd>Show which function each change is in.</p>
<dt><code>ignorews</code></p>
<dd>Ignore white space when comparing lines.</p>
<dt><code>ignorewsamount</code></p>
<dd>Ignore changes in the amount of white space.</p>
<dt><code>ignoreblanklines</code></p>
<dd>Ignore changes whose lines are all blank.</p>
<dt><code>unified</code></p>
<dd>Number of lines of context to show.</dl>
<h3><code>email</code></h3>
<p>Settings for extensions that send email messages.</p>
<dl>
<dt><code>from</code></p>
<dd>Optional. Email address to use in &quot;From&quot; header and SMTP envelope of outgoing messages.</p>
<dt><code>to</code></p>
<dd>Optional. Comma-separated list of recipients&#8217; email addresses.</p>
<dt><code>cc</code></p>
<dd>Optional. Comma-separated list of carbon copy recipients&#8217; email addresses.</p>
<dt><code>bcc</code></p>
<dd>Optional. Comma-separated list of blind carbon copy recipients&#8217; email addresses.</p>
<dt><code>method</code></p>
<dd>Optional. Method to use to send email messages. If value is <code>smtp</code> (default), use SMTP (see the <code>[smtp]</code> section for configuration). Otherwise, use as name of program to run that acts like sendmail (takes <code>-f</code> option for sender, list of recipients on command line, message on stdin). Normally, setting this to <code>sendmail</code> or <code>/usr/sbin/sendmail</code> is enough to use sendmail to send messages.</p>
<dt><code>charsets</code></p>
<dd>Optional. Comma-separated list of character sets considered convenient for recipients. Addresses, headers, and parts not containing patches of outgoing messages will be encoded in the first character set to which conversion from local encoding (<code>$HGENCODING</code>, <code>ui.fallbackencoding</code>) succeeds. If correct conversion fails, the text in question is sent as is. Defaults to empty (explicit) list. </p>
<p> Order of outgoing email character sets:</p>
<dt>1.</p>
<dd><code>us-ascii</code>: always first, regardless of settings</p>
<dt>2.</p>
<dd><code>email.charsets</code>: in order given by user</p>
<dt>3.</p>
<dd><code>ui.fallbackencoding</code>: if not in email.charsets</p>
<dt>4.</p>
<dd><code>$HGENCODING</code>: if not in email.charsets</p>
<dt>5.</p>
<dd><code>utf-8</code>: always last, regardless of settings </p>
<p> Email example: </p>
<pre>[email]
from = Joseph User &lt;joe.user [at] example.com&gt;
method = /usr/sbin/sendmail
# charsets for western Europeans
# us-ascii, utf-8 omitted, as they are tried first and last
charsets = iso-8859-1, iso-8859-15, windows-1252</pre>
</dl>
<h3><code>extensions</code></h3>
<p>Mercurial has an extension mechanism for adding new features. To enable an extension, create an entry for it in this section. </p>
<p> If you know that the extension is already in Python&#8217;s search path, you can give the name of the module, followed by <code>=</code>, with nothing after the <code>=</code>. </p>
<p> Otherwise, give a name that you choose, followed by <code>=</code>, followed by the path to the <code>.py</code> file (including the file name extension) that defines the extension. </p>
<p> To explicitly disable an extension that is enabled in an hgrc of broader scope, prepend its path with <code>!</code>, as in <code>foo = !/ext/path</code> or <code>foo = !</code> when path is not supplied. </p>
<p> Example for <code>~/.hgrc</code>: </p>
<pre>[extensions]
# (the mq extension will get loaded from Mercurial's path)
mq =
# (this extension will get loaded from the file specified)
myfeature = ~/.hgext/myfeature.py</pre>
<h3><code>format</code></h3>
<dl>
<dt><code>usestore</code></p>
<dd>Enable or disable the &quot;store&quot; repository format which improves compatibility with systems that fold case or otherwise mangle filenames. Enabled by default. Disabling this option will allow you to store longer filenames in some situations at the expense of compatibility and ensures that the on-disk format of newly created repositories will be compatible with Mercurial before version 0.9.4.</p>
<dt><code>usefncache</code></p>
<dd>Enable or disable the &quot;fncache&quot; repository format which enhances the &quot;store&quot; repository format (which has to be enabled to use fncache) to allow longer filenames and avoids using Windows reserved names, e.g. &quot;nul&quot;. Enabled by default. Disabling this option ensures that the on-disk format of newly created repositories will be compatible with Mercurial before version 1.1.</p>
<dt><code>dotencode</code></p>
<dd>Enable or disable the &quot;dotencode&quot; repository format which enhances the &quot;fncache&quot; repository format (which has to be enabled to use dotencode) to avoid issues with filenames starting with ._ on Mac OS X and spaces on Windows. Enabled by default. Disabling this option ensures that the on-disk format of newly created repositories will be compatible with Mercurial before version 1.7.</dl>
<h3><code>graph</code></h3>
<p>Web graph view configuration. This section let you change graph elements display properties by branches, for instance to make the <code>default</code> branch stand out. </p>
<p> Each line has the following format: </p>
<pre>&lt;branch&gt;.&lt;argument&gt; = &lt;value&gt;</pre>
<p>where <code>&lt;branch&gt;</code> is the name of the branch being customized. Example: </p>
<pre>[graph]
# 2px width
default.width = 2
# red color
default.color = FF0000</pre>
<p>Supported arguments:</p>
<dl>
<dt><code>width</code></p>
<dd>Set branch edges width in pixels.</p>
<dt><code>color</code></p>
<dd>Set branch edges color in hexadecimal RGB notation.</dl>
<h3><code>hooks</code></h3>
<p>Commands or Python functions that get automatically executed by various actions such as starting or finishing a commit. Multiple hooks can be run for the same action by appending a suffix to the action. Overriding a site-wide hook can be done by changing its value or setting it to an empty string. Hooks can be prioritized by adding a prefix of <code>priority</code> to the hook name on a new line and setting the priority. The default priority is 0 if not specified. </p>
<p> Example <code>.hg/hgrc</code>: </p>
<pre>[hooks]
# update working directory after adding changesets
changegroup.update = hg update
# do not use the site-wide hook
incoming =
incoming.email = /my/email/hook
incoming.autobuild = /my/build/hook
# force autobuild hook to run before other incoming hooks
priority.incoming.autobuild = 1</pre>
<p>Most hooks are run with environment variables set that give useful additional information. For each hook below, the environment variables it is passed are listed with names of the form <code>$HG_foo</code>.</p>
<dl>
<dt><code>changegroup</code></p>
<dd>Run after a changegroup has been added via push, pull or unbundle. ID of the first new changeset is in <code>$HG_NODE</code>. URL from which changes came is in <code>$HG_URL</code>.</p>
<dt><code>commit</code></p>
<dd>Run after a changeset has been created in the local repository. ID of the newly created changeset is in <code>$HG_NODE</code>. Parent changeset IDs are in <code>$HG_PARENT1</code> and <code>$HG_PARENT2</code>.</p>
<dt><code>incoming</code></p>
<dd>Run after a changeset has been pulled, pushed, or unbundled into the local repository. The ID of the newly arrived changeset is in <code>$HG_NODE</code>. URL that was source of changes came is in <code>$HG_URL</code>.</p>
<dt><code>outgoing</code></p>
<dd>Run after sending changes from local repository to another. ID of first changeset sent is in <code>$HG_NODE</code>. Source of operation is in <code>$HG_SOURCE</code>; see &quot;preoutgoing&quot; hook for description.</p>
<dt><code>post-&lt;command&gt;</code></p>
<dd>Run after successful invocations of the associated command. The contents of the command line are passed as <code>$HG_ARGS</code> and the result code in <code>$HG_RESULT</code>. Parsed command line arguments are passed as <code>$HG_PATS</code> and <code>$HG_OPTS</code>. These contain string representations of the python data internally passed to &lt;command&gt;. <code>$HG_OPTS</code> is a dictionary of options (with unspecified options set to their defaults). <code>$HG_PATS</code> is a list of arguments. Hook failure is ignored.</p>
<dt><code>pre-&lt;command&gt;</code></p>
<dd>Run before executing the associated command. The contents of the command line are passed as <code>$HG_ARGS</code>. Parsed command line arguments are passed as <code>$HG_PATS</code> and <code>$HG_OPTS</code>. These contain string representations of the data internally passed to &lt;command&gt;. <code>$HG_OPTS</code> is a dictionary of options (with unspecified options set to their defaults). <code>$HG_PATS</code> is a list of arguments. If the hook returns failure, the command doesn&#8217;t execute and Mercurial returns the failure code.</p>
<dt><code>prechangegroup</code></p>
<dd>Run before a changegroup is added via push, pull or unbundle. Exit status 0 allows the changegroup to proceed. Non-zero status will cause the push, pull or unbundle to fail. URL from which changes will come is in <code>$HG_URL</code>.</p>
<dt><code>precommit</code></p>
<dd>Run before starting a local commit. Exit status 0 allows the commit to proceed. Non-zero status will cause the commit to fail. Parent changeset IDs are in <code>$HG_PARENT1</code> and <code>$HG_PARENT2</code>.</p>
<dt><code>prelistkeys</code></p>
<dd>Run before listing pushkeys (like bookmarks) in the repository. Non-zero status will cause failure. The key namespace is in <code>$HG_NAMESPACE</code>.</p>
<dt><code>preoutgoing</code></p>
<dd>Run before collecting changes to send from the local repository to another. Non-zero status will cause failure. This lets you prevent pull over HTTP or SSH. Also prevents against local pull, push (outbound) or bundle commands, but not effective, since you can just copy files instead then. Source of operation is in <code>$HG_SOURCE</code>. If &quot;serve&quot;, operation is happening on behalf of remote SSH or HTTP repository. If &quot;push&quot;, &quot;pull&quot; or &quot;bundle&quot;, operation is happening on behalf of repository on same system.</p>
<dt><code>prepushkey</code></p>
<dd>Run before a pushkey (like a bookmark) is added to the repository. Non-zero status will cause the key to be rejected. The key namespace is in <code>$HG_NAMESPACE</code>, the key is in <code>$HG_KEY</code>, the old value (if any) is in <code>$HG_OLD</code>, and the new value is in <code>$HG_NEW</code>.</p>
<dt><code>pretag</code></p>
<dd>Run before creating a tag. Exit status 0 allows the tag to be created. Non-zero status will cause the tag to fail. ID of changeset to tag is in <code>$HG_NODE</code>. Name of tag is in <code>$HG_TAG</code>. Tag is local if <code>$HG_LOCAL=1</code>, in repository if <code>$HG_LOCAL=0</code>.</p>
<dt><code>pretxnchangegroup</code></p>
<dd>Run after a changegroup has been added via push, pull or unbundle, but before the transaction has been committed. Changegroup is visible to hook program. This lets you validate incoming changes before accepting them. Passed the ID of the first new changeset in <code>$HG_NODE</code>. Exit status 0 allows the transaction to commit. Non-zero status will cause the transaction to be rolled back and the push, pull or unbundle will fail. URL that was source of changes is in <code>$HG_URL</code>.</p>
<dt><code>pretxncommit</code></p>
<dd>Run after a changeset has been created but the transaction not yet committed. Changeset is visible to hook program. This lets you validate commit message and changes. Exit status 0 allows the commit to proceed. Non-zero status will cause the transaction to be rolled back. ID of changeset is in <code>$HG_NODE</code>. Parent changeset IDs are in <code>$HG_PARENT1</code> and <code>$HG_PARENT2</code>.</p>
<dt><code>preupdate</code></p>
<dd>Run before updating the working directory. Exit status 0 allows the update to proceed. Non-zero status will prevent the update. Changeset ID of first new parent is in <code>$HG_PARENT1</code>. If merge, ID of second new parent is in <code>$HG_PARENT2</code>.</p>
<dt><code>listkeys</code></p>
<dd>Run after listing pushkeys (like bookmarks) in the repository. The key namespace is in <code>$HG_NAMESPACE</code>. <code>$HG_VALUES</code> is a dictionary containing the keys and values.</p>
<dt><code>pushkey</code></p>
<dd>Run after a pushkey (like a bookmark) is added to the repository. The key namespace is in <code>$HG_NAMESPACE</code>, the key is in <code>$HG_KEY</code>, the old value (if any) is in <code>$HG_OLD</code>, and the new value is in <code>$HG_NEW</code>.</p>
<dt><code>tag</code></p>
<dd>Run after a tag is created. ID of tagged changeset is in <code>$HG_NODE</code>. Name of tag is in <code>$HG_TAG</code>. Tag is local if <code>$HG_LOCAL=1</code>, in repository if <code>$HG_LOCAL=0</code>.</p>
<dt><code>update</code></p>
<dd>Run after updating the working directory. Changeset ID of first new parent is in <code>$HG_PARENT1</code>. If merge, ID of second new parent is in <code>$HG_PARENT2</code>. If the update succeeded, <code>$HG_ERROR=0</code>. If the update failed (e.g. because conflicts not resolved), <code>$HG_ERROR=1</code>.</p>
<dt>Note</p>
<dd>It is generally better to use standard hooks rather than the generic pre- and post- command hooks as they are guaranteed to be called in the appropriate contexts for influencing transactions. Also, hooks like &quot;commit&quot; will be called in all contexts that generate a commit (e.g. tag) and not just the commit command.</p>
<dt>Note</p>
<dd>Environment variables with empty values may not be passed to hooks on platforms such as Windows. As an example, <code>$HG_PARENT2</code> will have an empty value under Unix-like platforms for non-merge changesets, while it will not be available at all under Windows. </p>
<p> The syntax for Python hooks is as follows: </p>
<pre>hookname = python:modulename.submodule.callable
hookname = python:/path/to/python/module.py:callable</pre>
<p>Python hooks are run within the Mercurial process. Each hook is called with at least three keyword arguments: a ui object (keyword <code>ui</code>), a repository object (keyword <code>repo</code>), and a <code>hooktype</code> keyword that tells what kind of hook is used. Arguments listed as environment variables above are passed as keyword arguments, with no <code>HG_</code> prefix, and names in lower case. </p>
<p> If a Python hook returns a &quot;true&quot; value or raises an exception, this is treated as a failure.</dl>
<h3><code>hostfingerprints</code></h3>
<p>Fingerprints of the certificates of known HTTPS servers. A HTTPS connection to a server with a fingerprint configured here will only succeed if the servers certificate matches the fingerprint. This is very similar to how ssh known hosts works. The fingerprint is the SHA-1 hash value of the DER encoded certificate. The CA chain and web.cacerts is not used for servers with a fingerprint. </p>
<p> For example: </p>
<pre>[hostfingerprints]
hg.intevation.org = 44:ed:af:1f:97:11:b6:01:7a:48:45:fc:10:3c:b7:f9:d4:89:2a:9d</pre>
<p>This feature is only supported when using Python 2.6 or later.</p>
<h3><code>http_proxy</code></h3>
<p>Used to access web-based Mercurial repositories through a HTTP proxy.</p>
<dl>
<dt><code>host</code></p>
<dd>Host name and (optional) port of the proxy server, for example &quot;myproxy:8000&quot;.</p>
<dt><code>no</code></p>
<dd>Optional. Comma-separated list of host names that should bypass the proxy.</p>
<dt><code>passwd</code></p>
<dd>Optional. Password to authenticate with at the proxy server.</p>
<dt><code>user</code></p>
<dd>Optional. User name to authenticate with at the proxy server.</p>
<dt><code>always</code></p>
<dd>Optional. Always use the proxy, even for localhost and any entries in <code>http_proxy.no</code>. True or False. Default: False.</dl>
<h3><code>merge-patterns</code></h3>
<p>This section specifies merge tools to associate with particular file patterns. Tools matched here will take precedence over the default merge tool. Patterns are globs by default, rooted at the repository root. </p>
<p> Example: </p>
<pre>[merge-patterns]
**.c = kdiff3
**.jpg = myimgmerge</pre>
<h3><code>merge-tools</code></h3>
<p>This section configures external merge tools to use for file-level merges. </p>
<p> Example <code>~/.hgrc</code>: </p>
<pre>[merge-tools]
# Override stock tool location
kdiff3.executable = ~/bin/kdiff3
# Specify command line
kdiff3.args = $base $local $other -o $output
# Give higher priority
kdiff3.priority = 1
# Define new tool
myHtmlTool.args = -m $local $other $base $output
myHtmlTool.regkey = Software\FooSoftware\HtmlMerge
myHtmlTool.priority = 1</pre>
<p>Supported arguments:</p>
<dl>
<dt><code>priority</code></p>
<dd>The priority in which to evaluate this tool. Default: 0.</p>
<dt><code>executable</code></p>
<dd>Either just the name of the executable or its pathname. On Windows, the path can use environment variables with ${ProgramFiles} syntax. Default: the tool name.</p>
<dt><code>args</code></p>
<dd>The arguments to pass to the tool executable. You can refer to the files being merged as well as the output file through these variables: <code>$base</code>, <code>$local</code>, <code>$other</code>, <code>$output</code>. Default: <code>$local $base $other</code></p>
<dt><code>premerge</code></p>
<dd>Attempt to run internal non-interactive 3-way merge tool before launching external tool. Options are <code>true</code>, <code>false</code>, or <code>keep</code> to leave markers in the file if the premerge fails. Default: True</p>
<dt><code>binary</code></p>
<dd>This tool can merge binary files. Defaults to False, unless tool was selected by file pattern match.</p>
<dt><code>symlink</code></p>
<dd>This tool can merge symlinks. Defaults to False, even if tool was selected by file pattern match.</p>
<dt><code>check</code></p>
<dd>A list of merge success-checking options:</p>
<dt><code>changed</code></p>
<dd>Ask whether merge was successful when the merged file shows no changes.</p>
<dt><code>conflicts</code></p>
<dd>Check whether there are conflicts even though the tool reported success.</p>
<dt><code>prompt</code></p>
<dd>Always prompt for merge success, regardless of success reported by tool.</p>
<dt><code>fixeol</code></p>
<dd>Attempt to fix up EOL changes caused by the merge tool. Default: False</p>
<dt><code>gui</code></p>
<dd>This tool requires a graphical interface to run. Default: False</p>
<dt><code>regkey</code></p>
<dd>Windows registry key which describes install location of this tool. Mercurial will search for this key first under <code>HKEY_CURRENT_USER</code> and then under <code>HKEY_LOCAL_MACHINE</code>. Default: None</p>
<dt><code>regkeyalt</code></p>
<dd>An alternate Windows registry key to try if the first key is not found. The alternate key uses the same <code>regname</code> and <code>regappend</code> semantics of the primary key. The most common use for this key is to search for 32bit applications on 64bit operating systems. Default: None</p>
<dt><code>regname</code></p>
<dd>Name of value to read from specified registry key. Defaults to the unnamed (default) value.</p>
<dt><code>regappend</code></p>
<dd>String to append to the value read from the registry, typically the executable name of the tool. Default: None</dl>
<h3><code>patch</code></h3>
<p>Settings used when applying patches, for instance through the &#8216;import&#8217; command or with Mercurial Queues extension.</p>
<dl>
<dt><code>eol</code></p>
<dd>When set to &#8216;strict&#8217; patch content and patched files end of lines are preserved. When set to <code>lf</code> or <code>crlf</code>, both files end of lines are ignored when patching and the result line endings are normalized to either LF (Unix) or CRLF (Windows). When set to <code>auto</code>, end of lines are again ignored while patching but line endings in patched files are normalized to their original setting on a per-file basis. If target file does not exist or has no end of line, patch line endings are preserved. Default: strict.</dl>
<h3><code>paths</code></h3>
<p>Assigns symbolic names to repositories. The left side is the symbolic name, and the right gives the directory or URL that is the location of the repository. Default paths can be declared by setting the following entries.</p>
<dl>
<dt><code>default</code></p>
<dd>Directory or URL to use when pulling if no source is specified. Default is set to repository from which the current repository was cloned.</p>
<dt><code>default-push</code></p>
<dd>Optional. Directory or URL to use when pushing if no destination is specified. </p>
<p> Custom paths can be defined by assigning the path to a name that later can be used from the command line. Example: </p>
<pre>[paths]
my_path = <a rel="nofollow" href="http://example.com/path">http://example.com/path</a></pre>
<p>To push to the path defined in <code>my_path</code> run the command: </p>
<pre>hg push my_path</pre>
</dl>
<h3><code>phases</code></h3>
<p>Specifies default handling of phases. See <code>hg help phases</code>: for more information about working with phases.</p>
<dl>
<dt><code>publish</code></p>
<dd>Controls draft phase behavior when working as a server. When true, pushed changesets are set to public in both client and server and pulled or cloned changesets are set to public in the client. Default: True</p>
<dt><code>new-commit</code></p>
<dd>Phase of newly-created commits. Default: draft</dl>
<h3><code>profiling</code></h3>
<p>Specifies profiling type, format, and file output. Two profilers are supported: an instrumenting profiler (named <code>ls</code>), and a sampling profiler (named <code>stat</code>). </p>
<p> In this section description, &#8216;profiling data&#8217; stands for the raw data collected during profiling, while &#8216;profiling report&#8217; stands for a statistical text report generated from the profiling data. The profiling is done using lsprof.</p>
<dl>
<dt><code>type</code></p>
<dd>The type of profiler to use. Default: ls.</p>
<dt><code>ls</code></p>
<dd>Use Python&#8217;s built-in instrumenting profiler. This profiler works on all platforms, but each line number it reports is the first line of a function. This restriction makes it difficult to identify the expensive parts of a non-trivial function.</p>
<dt><code>stat</code></p>
<dd>Use a third-party statistical profiler, statprof. This profiler currently runs only on Unix systems, and is most useful for profiling commands that run for longer than about 0.1 seconds.</p>
<dt><code>format</code></p>
<dd>Profiling format. Specific to the <code>ls</code> instrumenting profiler. Default: text.</p>
<dt><code>text</code></p>
<dd>Generate a profiling report. When saving to a file, it should be noted that only the report is saved, and the profiling data is not kept.</p>
<dt><code>kcachegrind</code></p>
<dd>Format profiling data for kcachegrind use: when saving to a file, the generated file can directly be loaded into kcachegrind.</p>
<dt><code>frequency</code></p>
<dd>Sampling frequency. Specific to the <code>stat</code> sampling profiler. Default: 1000.</p>
<dt><code>output</code></p>
<dd>File path where profiling data or report should be saved. If the file exists, it is replaced. Default: None, data is printed on stderr</p>
<dt><code>sort</code></p>
<dd>Sort field. Specific to the <code>ls</code> instrumenting profiler. One of <code>callcount</code>, <code>reccallcount</code>, <code>totaltime</code> and <code>inlinetime</code>. Default: inlinetime.</p>
<dt><code>limit</code></p>
<dd>Number of lines to show. Specific to the <code>ls</code> instrumenting profiler. Default: 30.</p>
<dt><code>nested</code></p>
<dd>Show at most this number of lines of drill-down info after each main entry. This can help explain the difference between Total and Inline. Specific to the <code>ls</code> instrumenting profiler. Default: 5.</dl>
<h3><code>revsetalias</code></h3>
<p>Alias definitions for revsets. See <code>hg help revsets</code>: for details.</p>
<h3><code>server</code></h3>
<p>Controls generic server settings.</p>
<dl>
<dt><code>uncompressed</code></p>
<dd>Whether to allow clients to clone a repository using the uncompressed streaming protocol. This transfers about 40% more data than a regular clone, but uses less memory and CPU on both server and client. Over a LAN (100 Mbps or better) or a very fast WAN, an uncompressed streaming clone is a lot faster (~10x) than a regular clone. Over most WAN connections (anything slower than about 6 Mbps), uncompressed streaming is slower, because of the extra data transfer overhead. This mode will also temporarily hold the write lock while determining what data to transfer. Default is True.</p>
<dt><code>preferuncompressed</code></p>
<dd>When set, clients will try to use the uncompressed streaming protocol. Default is False.</p>
<dt><code>validate</code></p>
<dd>Whether to validate the completeness of pushed changesets by checking that all new file revisions specified in manifests are present. Default is False.</dl>
<h3><code>smtp</code></h3>
<p>Configuration for extensions that need to send email messages.</p>
<dl>
<dt><code>host</code></p>
<dd>Host name of mail server, e.g. &quot;mail.example.com&quot;.</p>
<dt><code>port</code></p>
<dd>Optional. Port to connect to on mail server. Default: 465 (if <code>tls</code> is smtps) or 25 (otherwise).</p>
<dt><code>tls</code></p>
<dd>Optional. Method to enable TLS when connecting to mail server: starttls, smtps or none. Default: none.</p>
<dt><code>verifycert</code></p>
<dd>Optional. Verification for the certificate of mail server, when <code>tls</code> is starttls or smtps. &quot;strict&quot;, &quot;loose&quot; or False. For &quot;strict&quot; or &quot;loose&quot;, the certificate is verified as same as the verification for HTTPS connections (see <code>[hostfingerprints]</code> and <code>[web] cacerts</code> also). For &quot;strict&quot;, sending email is also aborted, if there is no configuration for mail server in <code>[hostfingerprints]</code> and <code>[web] cacerts</code>. &#8211;insecure for <code>hg email</code>: overwrites this as &quot;loose&quot;. Default: &quot;strict&quot;.</p>
<dt><code>username</code></p>
<dd>Optional. User name for authenticating with the SMTP server. Default: none.</p>
<dt><code>password</code></p>
<dd>Optional. Password for authenticating with the SMTP server. If not specified, interactive sessions will prompt the user for a password; non-interactive sessions will fail. Default: none.</p>
<dt><code>local_hostname</code></p>
<dd>Optional. It&#8217;s the hostname that the sender can use to identify itself to the MTA.</dl>
<h3><code>subpaths</code></h3>
<p>Subrepository source URLs can go stale if a remote server changes name or becomes temporarily unavailable. This section lets you define rewrite rules of the form: </p>
<pre>&lt;pattern&gt; = &lt;replacement&gt;</pre>
<p>where <code>pattern</code> is a regular expression matching a subrepository source URL and <code>replacement</code> is the replacement string used to rewrite it. Groups can be matched in <code>pattern</code> and referenced in <code>replacements</code>. For instance: </p>
<pre><a rel="nofollow" href="http://server/(.*)-hg/">http://server/(.*)-hg/</a> = <a href="http://hg.server/\1/">http://hg.server/\1/</a></pre>
<p>rewrites <code><a rel="nofollow" href="http://server/foo-hg/">http://server/foo-hg/</a></code> into <code><a href="http://hg.server/foo/">http://hg.server/foo/</a></code>. </p>
<p> Relative subrepository paths are first made absolute, and the rewrite rules are then applied on the full (absolute) path. The rules are applied in definition order.</p>
<h3><code>trusted</code></h3>
<p>Mercurial will not use the settings in the <code>.hg/hgrc</code> file from a repository if it doesn&#8217;t belong to a trusted user or to a trusted group, as various hgrc features allow arbitrary commands to be run. This issue is often encountered when configuring hooks or extensions for shared repositories or servers. However, the web interface will use some safe settings from the <code>[web]</code> section. </p>
<p> This section specifies what users and groups are trusted. The current user is always trusted. To trust everybody, list a user or a group with name <code>*</code>. These settings must be placed in an <i>already-trusted file</i> to take effect, such as <code>$HOME/.hgrc</code> of the user or service running Mercurial.</p>
<dl>
<dt><code>users</code></p>
<dd>Comma-separated list of trusted users.</p>
<dt><code>groups</code></p>
<dd>Comma-separated list of trusted groups.</dl>
<h3><code>ui</code></h3>
<p>User interface controls.</p>
<dl>
<dt><code>archivemeta</code></p>
<dd>Whether to include the .hg_archival.txt file containing meta data (hashes for the repository base and for tip) in archives created by the <code>hg archive</code>: command or downloaded via hgweb. Default is True.</p>
<dt><code>askusername</code></p>
<dd>Whether to prompt for a username when committing. If True, and neither <code>$HGUSER</code> nor <code>$EMAIL</code> has been specified, then the user will be prompted to enter a username. If no username is entered, the default <code>USER [at] HOST</code> is used instead. Default is False.</p>
<dt><code>commitsubrepos</code></p>
<dd>Whether to commit modified subrepositories when committing the parent repository. If False and one subrepository has uncommitted changes, abort the commit. Default is False.</p>
<dt><code>debug</code></p>
<dd>Print debugging information. True or False. Default is False.</p>
<dt><code>editor</code></p>
<dd>The editor to use during a commit. Default is <code>$EDITOR</code> or <code>vi</code>.</p>
<dt><code>fallbackencoding</code></p>
<dd>Encoding to try if it&#8217;s not possible to decode the changelog using UTF-8. Default is ISO-8859-1.</p>
<dt><code>ignore</code></p>
<dd>A file to read per-user ignore patterns from. This file should be in the same format as a repository-wide .hgignore file. This option supports hook syntax, so if you want to specify multiple ignore files, you can do so by setting something like <code>ignore.other = ~/.hgignore2</code>. For details of the ignore file format, see the <code><a href="/docs/linux/man/5-hgignore/">hgignore</a>(5)</code> man page.</p>
<dt><code>interactive</code></p>
<dd>Allow to prompt the user. True or False. Default is True.</p>
<dt><code>logtemplate</code></p>
<dd>Template string for commands that print changesets.</p>
<dt><code>merge</code></p>
<dd>The conflict resolution program to use during a manual merge. For more information on merge tools see <code>hg help merge-tools</code>:. For configuring merge tools see the <code>[merge-tools]</code> section.</p>
<dt><code>portablefilenames</code></p>
<dd>Check for portable filenames. Can be <code>warn</code>, <code>ignore</code> or <code>abort</code>. Default is <code>warn</code>. If set to <code>warn</code> (or <code>true</code>), a warning message is printed on POSIX platforms, if a file with a non-portable filename is added (e.g. a file with a name that can&#8217;t be created on Windows because it contains reserved parts like <code>AUX</code>, reserved characters like <code>:</code>, or would cause a case collision with an existing file). If set to <code>ignore</code> (or <code>false</code>), no warning is printed. If set to <code>abort</code>, the command is aborted. On Windows, this configuration option is ignored and the command aborted.</p>
<dt><code>quiet</code></p>
<dd>Reduce the amount of output printed. True or False. Default is False.</p>
<dt><code>remotecmd</code></p>
<dd>remote command to use for clone/push/pull operations. Default is <code>hg</code>.</p>
<dt><code>reportoldssl</code></p>
<dd>Warn if an SSL certificate is unable to be due to using Python 2.5 or earlier. True or False. Default is True.</p>
<dt><code>report_untrusted</code></p>
<dd>Warn if a <code>.hg/hgrc</code> file is ignored due to not being owned by a trusted user or group. True or False. Default is True.</p>
<dt><code>slash</code></p>
<dd>Display paths using a slash (<code>/</code>) as the path separator. This only makes a difference on systems where the default path separator is not the slash character (e.g. Windows uses the backslash character (<code>\</code>)). Default is False.</p>
<dt><code>ssh</code></p>
<dd>command to use for SSH connections. Default is <code>ssh</code>.</p>
<dt><code>strict</code></p>
<dd>Require exact command names, instead of allowing unambiguous abbreviations. True or False. Default is False.</p>
<dt><code>style</code></p>
<dd>Name of style to use for command output.</p>
<dt><code>timeout</code></p>
<dd>The timeout used when a lock is held (in seconds), a negative value means no timeout. Default is 600.</p>
<dt><code>traceback</code></p>
<dd>Mercurial always prints a traceback when an unknown exception occurs. Setting this to True will make Mercurial print a traceback on all exceptions, even those recognized by Mercurial (such as IOError or MemoryError). Default is False.</p>
<dt><code>username</code></p>
<dd>The committer of a changeset created when running &quot;commit&quot;. Typically a person&#8217;s name and email address, e.g. <code>Fred Widget &lt;fred [at] example.com&gt;</code>. Default is <code>$EMAIL</code> or <code>username [at] hostname</code>. If the username in hgrc is empty, it has to be specified manually or in a different hgrc file (e.g. <code>$HOME/.hgrc</code>, if the admin set <code>username =</code> in the system hgrc). Environment variables in the username are expanded.</p>
<dt><code>verbose</code></p>
<dd>Increase the amount of output printed. True or False. Default is False.</dl>
<h3><code>web</code></h3>
<p>Web interface configuration. The settings in this section apply to both the builtin webserver (started by <code>hg serve</code>:) and the script you run through a webserver (<code>hgweb.cgi</code> and the derivatives for FastCGI and WSGI). </p>
<p> The Mercurial webserver does no authentication (it does not prompt for usernames and passwords to validate <i>who</i> users are), but it does do authorization (it grants or denies access for <i>authenticated users</i> based on settings in this section). You must either configure your webserver to do authentication for you, or disable the authorization checks. </p>
<p> For a quick setup in a trusted environment, e.g., a private LAN, where you want it to accept pushes from anybody, you can use the following command line: </p>
<pre>$ hg --config web.allow_push=* --config web.push_ssl=False serve</pre>
<p>Note that this will allow anybody to push anything to the server and that this should not be used for public servers. </p>
<p> The full set of options is:</p>
<dl>
<dt><code>accesslog</code></p>
<dd>Where to output the access log. Default is stdout.</p>
<dt><code>address</code></p>
<dd>Interface address to bind to. Default is all.</p>
<dt><code>allow_archive</code></p>
<dd>List of archive format (bz2, gz, zip) allowed for downloading. Default is empty.</p>
<dt><code>allowbz2</code></p>
<dd>(DEPRECATED) Whether to allow .tar.bz2 downloading of repository revisions. Default is False.</p>
<dt><code>allowgz</code></p>
<dd>(DEPRECATED) Whether to allow .tar.gz downloading of repository revisions. Default is False.</p>
<dt><code>allowpull</code></p>
<dd>Whether to allow pulling from the repository. Default is True.</p>
<dt><code>allow_push</code></p>
<dd>Whether to allow pushing to the repository. If empty or not set, push is not allowed. If the special value <code>*</code>, any remote user can push, including unauthenticated users. Otherwise, the remote user must have been authenticated, and the authenticated user name must be present in this list. The contents of the allow_push list are examined after the deny_push list.</p>
<dt><code>allow_read</code></p>
<dd>If the user has not already been denied repository access due to the contents of deny_read, this list determines whether to grant repository access to the user. If this list is not empty, and the user is unauthenticated or not present in the list, then access is denied for the user. If the list is empty or not set, then access is permitted to all users by default. Setting allow_read to the special value <code>*</code> is equivalent to it not being set (i.e. access is permitted to all users). The contents of the allow_read list are examined after the deny_read list.</p>
<dt><code>allowzip</code></p>
<dd>(DEPRECATED) Whether to allow .zip downloading of repository revisions. Default is False. This feature creates temporary files.</p>
<dt><code>archivesubrepos</code></p>
<dd>Whether to recurse into subrepositories when archiving. Default is False.</p>
<dt><code>baseurl</code></p>
<dd>Base URL to use when publishing URLs in other locations, so third-party tools like email notification hooks can construct URLs. Example: <code><a rel="nofollow" href="http://hgserver/repos/">http://hgserver/repos/</a></code>.</p>
<dt><code>cacerts</code></p>
<dd>Path to file containing a list of PEM encoded certificate authority certificates. Environment variables and <code>~user</code> constructs are expanded in the filename. If specified on the client, then it will verify the identity of remote HTTPS servers with these certificates. </p>
<p> This feature is only supported when using Python 2.6 or later. If you wish to use it with earlier versions of Python, install the backported version of the ssl library that is available from <code><a rel="nofollow" href="http://pypi.python.org">http://pypi.python.org</a></code>. </p>
<p> To disable SSL verification temporarily, specify <code>&#8211;insecure</code> from command line. </p>
<p> You can use OpenSSL&#8217;s CA certificate file if your platform has one. On most Linux systems this will be <code>/etc/ssl/certs/ca-certificates.crt</code>. Otherwise you will have to generate this file manually. The form must be as follows: </p>
<pre>-----BEGIN CERTIFICATE-----
... (certificate in base64 PEM encoding) ...
-----END CERTIFICATE-----
-----BEGIN CERTIFICATE-----
... (certificate in base64 PEM encoding) ...
-----END CERTIFICATE-----</pre>
<dt><code>cache</code></p>
<dd>Whether to support caching in hgweb. Defaults to True.</p>
<dt><code>collapse</code></p>
<dd>With <code>descend</code> enabled, repositories in subdirectories are shown at a single level alongside repositories in the current path. With <code>collapse</code> also enabled, repositories residing at a deeper level than the current path are grouped behind navigable directory entries that lead to the locations of these repositories. In effect, this setting collapses each collection of repositories found within a subdirectory into a single entry for that subdirectory. Default is False.</p>
<dt><code>comparisoncontext</code></p>
<dd>Number of lines of context to show in side-by-side file comparison. If negative or the value <code>full</code>, whole files are shown. Default is 5. This setting can be overridden by a <code>context</code> request parameter to the <code>comparison</code> command, taking the same values.</p>
<dt><code>contact</code></p>
<dd>Name or email address of the person in charge of the repository. Defaults to ui.username or <code>$EMAIL</code> or &quot;unknown&quot; if unset or empty.</p>
<dt><code>deny_push</code></p>
<dd>Whether to deny pushing to the repository. If empty or not set, push is not denied. If the special value <code>*</code>, all remote users are denied push. Otherwise, unauthenticated users are all denied, and any authenticated user name present in this list is also denied. The contents of the deny_push list are examined before the allow_push list.</p>
<dt><code>deny_read</code></p>
<dd>Whether to deny reading/viewing of the repository. If this list is not empty, unauthenticated users are all denied, and any authenticated user name present in this list is also denied access to the repository. If set to the special value <code>*</code>, all remote users are denied access (rarely needed ;). If deny_read is empty or not set, the determination of repository access depends on the presence and content of the allow_read list (see description). If both deny_read and allow_read are empty or not set, then access is permitted to all users by default. If the repository is being served via hgwebdir, denied users will not be able to see it in the list of repositories. The contents of the deny_read list have priority over (are examined before) the contents of the allow_read list.</p>
<dt><code>descend</code></p>
<dd>hgwebdir indexes will not descend into subdirectories. Only repositories directly in the current path will be shown (other repositories are still available from the index corresponding to their containing path).</p>
<dt><code>description</code></p>
<dd>Textual description of the repository&#8217;s purpose or contents. Default is &quot;unknown&quot;.</p>
<dt><code>encoding</code></p>
<dd>Character encoding name. Default is the current locale charset. Example: &quot;UTF-8&quot;</p>
<dt><code>errorlog</code></p>
<dd>Where to output the error log. Default is stderr.</p>
<dt><code>guessmime</code></p>
<dd>Control MIME types for raw download of file content. Set to True to let hgweb guess the content type from the file extension. This will serve HTML files as <code>text/html</code> and might allow cross-site scripting attacks when serving untrusted repositories. Default is False.</p>
<dt><code>hidden</code></p>
<dd>Whether to hide the repository in the hgwebdir index. Default is False.</p>
<dt><code>ipv6</code></p>
<dd>Whether to use IPv6. Default is False.</p>
<dt><code>logoimg</code></p>
<dd>File name of the logo image that some templates display on each page. The file name is relative to <code>staticurl</code>. That is, the full path to the logo image is &quot;staticurl/logoimg&quot;. If unset, <code>hglogo.png</code> will be used.</p>
<dt><code>logourl</code></p>
<dd>Base URL to use for logos. If unset, <code><a rel="nofollow" href="http://mercurial.selenic.com/">http://mercurial.selenic.com/</a></code> will be used.</p>
<dt><code>maxchanges</code></p>
<dd>Maximum number of changes to list on the changelog. Default is 10.</p>
<dt><code>maxfiles</code></p>
<dd>Maximum number of files to list per changeset. Default is 10.</p>
<dt><code>maxshortchanges</code></p>
<dd>Maximum number of changes to list on the shortlog, graph or filelog pages. Default is 60.</p>
<dt><code>name</code></p>
<dd>Repository name to use in the web interface. Default is current working directory.</p>
<dt><code>port</code></p>
<dd>Port to listen on. Default is 8000.</p>
<dt><code>prefix</code></p>
<dd>Prefix path to serve from. Default is &#8221; (server root).</p>
<dt><code>push_ssl</code></p>
<dd>Whether to require that inbound pushes be transported over SSL to prevent password sniffing. Default is True.</p>
<dt><code>staticurl</code></p>
<dd>Base URL to use for static files. If unset, static files (e.g. the hgicon.png favicon) will be served by the CGI script itself. Use this setting to serve them directly with the HTTP server. Example: <code><a rel="nofollow" href="http://hgserver/static/">http://hgserver/static/</a></code>.</p>
<dt><code>stripes</code></p>
<dd>How many lines a &quot;zebra stripe&quot; should span in multi-line output. Default is 1; set to 0 to disable.</p>
<dt><code>style</code></p>
<dd>Which template map style to use.</p>
<dt><code>templates</code></p>
<dd>Where to find the HTML templates. Default is install path.</dl>
<h3><code>websub</code></h3>
<p>Web substitution filter definition. You can use this section to define a set of regular expression substitution patterns which let you automatically modify the hgweb server output. </p>
<p> The default hgweb templates only apply these substitution patterns on the revision description fields. You can apply them anywhere you want when you create your own templates by adding calls to the &quot;websub&quot; filter (usually after calling the &quot;escape&quot; filter). </p>
<p> This can be used, for example, to convert issue references to links to your issue tracker, or to convert &quot;markdown-like&quot; syntax into HTML (see the examples below). </p>
<p> Each entry in this section names a substitution filter. The value of each entry defines the substitution expression itself. The websub expressions follow the old interhg extension syntax, which in turn imitates the Unix sed replacement syntax: </p>
<pre>patternname = s/SEARCH_REGEX/REPLACE_EXPRESSION/[i]</pre>
<p>You can use any separator other than &quot;/&quot;. The final &quot;i&quot; is optional and indicates that the search must be case insensitive. </p>
<p> Examples: </p>
<pre>[websub]
issues = s|issue(\d+)|&lt;a href=&quot;<a rel="nofollow" href="http://bts.example.org/issue\1">http://bts.example.org/issue\1</a>&quot;&gt;issue\1&lt;/a&gt;|i
italic = s/_(\S+)_/&lt;i&gt;\1&lt;\/i&gt;/
bold = s/\*(\S+)\*/&lt;b&gt;\1&lt;\/b&gt;/</pre>
<h3><code>worker</code></h3>
<p>Parallel master/worker configuration. We currently perform working directory updates in parallel on Unix-like systems, which greatly helps performance.</p>
<dl>
<dt><code>numcpus</code></p>
<dd>Number of CPUs to use for parallel operations. Default is 4 or the number of CPUs on the system, whichever is larger. A zero or negative value is treated as <code>use the default</code>.</dl>
<h2>Author</h2>
<p>Bryan O&#8217;Sullivan &lt;bos [at] serpentine.com:&gt;. </p>
<p> Mercurial was written by Matt Mackall &lt;mpm [at] selenic.com:&gt;.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-hg/">hg</a></code>(1):, <code><a href="/docs/linux/man/5-hgignore/">hgignore</a></code>(5):</p>
<h2>Copying</h2>
<p>This manual page is copyright 2005 Bryan O&#8217;Sullivan. Mercurial is copyright 2005-2012 Matt Mackall. Free use of this software is granted under the terms of the GNU General Public License version 2 or any later version.</p>
<h2>Author</h2>
<p>Bryan O&#8217;Sullivan &lt;bos [at] serpentine.com&gt; </p>
<p> Organization: Mercurial</p>
