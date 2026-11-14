---
title: "mr(1)"
name: "mr"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mr/"
description: "mr – a tool to manage all your version control repos"
---

<h2 class="name">NAME</h2>
<p> mr &#8211; a tool to manage all your version control repos </p>
<h2>SYNOPSIS</h2>
<p> <code>mr</code> [options] checkout </p>
<p> <code>mr</code> [options] update </p>
<p> <code>mr</code> [options] status </p>
<p> <code>mr</code> [options] clean [-f] </p>
<p> <code>mr</code> [options] commit [-m &#8220;message&#8221;] </p>
<p> <code>mr</code> [options] record [-m &#8220;message&#8221;] </p>
<p> <code>mr</code> [options] fetch </p>
<p> <code>mr</code> [options] push </p>
<p> <code>mr</code> [options] diff </p>
<p> <code>mr</code> [options] log </p>
<p> <code>mr</code> [options] grep pattern </p>
<p> <code>mr</code> [options] run command [param &#8230;] </p>
<p> <code>mr</code> [options] bootstrap src [directory] </p>
<p> <code>mr</code> [options] register [repository] </p>
<p> <code>mr</code> [options] config section [&#8220;setting=[value]&#8221; &#8230;] </p>
<p> <code>mr</code> [options] action [params &#8230;] </p>
<p> <code>mr</code> [options] [online|offline] </p>
<p> <code>mr</code> [options] remember action [params &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>mr</code> is a tool to manage all your version control repos. It can checkout, update, or perform other actions on a set of repositories as if they were one combined repository. It supports any combination of subversion, git, cvs, mercurial, bzr, darcs, fossil and veracity repositories, and support for other version control systems can easily be added. </p>
<p> <code>mr</code> cds into and operates on all registered repositories at or below your working directory. Or, if you are in a subdirectory of a repository that contains no other registered repositories, it will stay in that directory, and work on only that repository, </p>
<p> <code>mr</code> is configured by .mrconfig files, which list the repositories. It starts by reading the .mrconfig file in your home directory, and this can in turn chain load .mrconfig files from repositories. It also automatically looks for a .mrconfig file in the current directory, or in one of its parent directories. </p>
<p> These predefined commands should be fairly familiar to users of any version control system:</p>
<dl>
<dt>checkout (or co)</p>
<dd> Checks out any repositories that are not already checked out.</p>
<dt>update</p>
<dd> Updates each repository from its configured remote repository. </p>
<p> If a repository isn&#8217;t checked out yet, it will first check it out.</p>
<dt>status</p>
<dd> Displays a status report for each repository, showing what uncommitted changes are present in the repository. For distributed version control systems, also shows unpushed local branches.</p>
<dt>clean</p>
<dd> Print ignored files, untracked files and other cruft in the working directory. </p>
<p> The optional -f parameter allows removing the files as well as printing them.</p>
<dt>commit (or ci)</p>
<dd> Commits changes to each repository. (By default, changes are pushed to the remote repository too, when using distributed systems like git. If you don&#8217;t like this default, you can change it in your .mrconfig, or use record instead.) </p>
<p> The optional -m parameter allows specifying a commit message.</p>
<dt>record</p>
<dd> Records changes to the local repository, but does not push them to the remote repository. Only supported for distributed version control systems. </p>
<p> The optional -m parameter allows specifying a commit message.</p>
<dt>fetch</p>
<dd> Fetches from each repository&#8217;s remote repository, but does not update the working copy. Only supported for some distributed version control systems.</p>
<dt>push</p>
<dd> Pushes committed local changes to the remote repository. A no-op for centralized version control systems.</p>
<dt>diff</p>
<dd> Show a diff of uncommitted changes.</p>
<dt>log</p>
<dd> Show the commit log.</p>
<dt>grep pattern</p>
<dd> Searches for a pattern in each repository using the grep subcommand. Uses ack-grep on <font SIZE="-1">VCS</font> that do not have their own.</p>
<dt>run command [param &#8230;]</p>
<dd> Runs the specified command in each repository.</dl>
<p> These commands are also available:</p>
<dl>
<dt>bootstrap src [directory]</p>
<dd> Causes mr to retrieve the source <tt>&quot;src&quot;</tt> and use it as a .mrconfig file to checkout the repositories listed in it, into the specified directory. </p>
<p> <code>mr</code> understands several types of sources:</p>
<dl>
<dt>
<dd>
<dl>
<dt><font SIZE="-1">URL</font> for curl</p>
<dd> <tt>&quot;src&quot;</tt> may be an <font SIZE="-1">URL</font> understood by <code>curl</code>.</p>
<dt>copy via ssh</p>
<dd> To use <code>scp</code> to download, the <tt>&quot;src&quot;</tt> may have the form <tt>&quot;<a href="ssh://[user@]host:file">ssh://[user@]host:file</a>&quot;</tt>.</p>
<dt>local file</p>
<dd> You can retrieve the config file by other means and pass its <code>path</code> as <tt>&quot;src&quot;</tt>.</p>
<dt>standard input</p>
<dd> If source <tt>&quot;src&quot;</tt> consists in a single dash <tt>&quot;-&quot;</tt>, config file is read from standard input.</dl>
</dl>
<dl>
<dt>
<dd>
<p> The directory will be created if it does not exist. If no directory is specified, the current directory will be used. </p>
<p> As a special case, if source <tt>&quot;src&quot;</tt> includes a repository named &#8220;.&#8221;, that is checked out into the top of the specified directory.</dl>
<dt>list (or ls)</p>
<dd> List the repositories that mr will act on.</p>
<dt>register</p>
<dd> Register an existing repository in a mrconfig file. By default, the repository in the current directory is registered, or you can specify a directory to register. </p>
<p> The mrconfig file that is modified is chosen by either the -c option, or by looking for the closest known one at or in a parent of the current directory.</p>
<dt>config</p>
<dd> Adds, modifies, removes, or prints a value from a mrconfig file. The next parameter is the name of the section the value is in. To add or modify values, use one or more instances of &#8220;setting=value&#8221;. Use &#8220;setting=&#8221; to remove a setting. Use just &#8220;setting&#8221; to get the value of a that setting. </p>
<p> For example, to add (or edit) a repository in src/foo: </p>
<pre>
  mr config src/foo checkout=&quot;svn co <a href="svn://example.com/foo/trunk">svn://example.com/foo/trunk</a> foo&quot;
</pre>
<p> To show the command that mr uses to update the repository in src/foo: </p>
<pre>
  mr config src/foo update
</pre>
<p> To see the built-in library of shell functions contained in mr: </p>
<pre>
  mr config DEFAULT lib
</pre>
<p> The mrconfig file that is used is chosen by either the -c option, or by looking for the closest known one at or in a parent of the current directory.</p>
<dt>offline</p>
<dd> Advises mr that it is in offline mode. Any commands that fail in offline mode will be remembered, and retried when mr is told it&#8217;s online.</p>
<dt>online</p>
<dd> Advices mr that it is in online mode again. Commands that failed while in offline mode will be re-run.</p>
<dt>remember</p>
<dd> Remember a command, to be run later when mr re-enters online mode. This implicitly puts mr into offline mode. The command can be any regular mr command. This is useful when you know that a command will fail due to being offline, and so don&#8217;t want to run it right now at all, but just remember to run it when you go back online.</p>
<dt>help</p>
<dd> Displays this help.</dl>
<p> Actions can be abbreviated to any unambiguous substring, so &#8220;mr st&#8221; is equivalent to &#8220;mr status&#8221;, and &#8220;mr up&#8221; is equivalent to &#8220;mr update&#8221; </p>
<p> Additional parameters can be passed to most commands, and are passed on unchanged to the underlying version control system. This is mostly useful if the repositories mr will act on all use the same version control system.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-d directory</p>
<dd>
<dt>&#8211;directory directory</p>
<dd> Specifies the topmost directory that <code>mr</code> should work in. The default is the current working directory.</p>
<dt>-c mrconfig</p>
<dd>
<dt>&#8211;config mrconfig</p>
<dd> Use the specified mrconfig file. The default is to use both <i>~/.mrconfig</i> as well as look for a <i>.mrconfig</i> file in the current directory, or in one of its parent directories.</p>
<dt>-f</p>
<dd>
<dt>&#8211;force</p>
<dd> Force mr to act on repositories that would normally be skipped due to their configuration.</p>
<dt>-v</p>
<dd>
<dt>&#8211;verbose</p>
<dd> Be verbose.</p>
<dt>-m</p>
<dd>
<dt>&#8211;minimal</p>
<dd> Minimise output. If a command fails or there is any output then the usual output will be shown.</p>
<dt>-q</p>
<dd>
<dt>&#8211;quiet</p>
<dd> Be quiet. This suppresses mr&#8217;s usual output, as well as any output from commands that are run (including stderr output). If a command fails, the output will be shown.</p>
<dt>-k</p>
<dd>
<dt>&#8211;insecure</p>
<dd> Accept untrusted <font SIZE="-1">SSL</font> certificates when bootstrapping.</p>
<dt>-s</p>
<dd>
<dt>&#8211;stats</p>
<dd> Expand the statistics line displayed at the end to include information about exactly which repositories failed and were skipped, if any.</p>
<dt>-i</p>
<dd>
<dt>&#8211;interactive</p>
<dd> Interactive mode. If a repository fails to be processed, a subshell will be started which you can use to resolve or investigate the problem. Exit the subshell to continue the mr run.</p>
<dt>-n [number]</p>
<dd>
<dt>&#8211;no-recurse [number]</p>
<dd> If no number if specified, just operate on the repository for the current directory, do not recurse into deeper repositories. </p>
<p> If a number is specified, will recurse into repositories at most that many subdirectories deep. For example, with -n 2 it would recurse into ./src/foo, but not ./src/packages/bar.</p>
<dt>-j [number]</p>
<dd>
<dt>&#8211;jobs [number]</p>
<dd> Run the specified number of jobs in parallel, or an unlimited number of jobs with no number specified. This can greatly speed up operations such as updates. It is not recommended for interactive operations. </p>
<p> Note that running more than 10 jobs at a time is likely to run afoul of ssh connection limits. Running between 3 and 5 jobs at a time will yield a good speedup in updates without loading the machine too much.</p>
<dt>-t</p>
<dd>
<dt>&#8211;trust-all</p>
<dd> Trust all mrconfig files even if they are not listed in <i>~/.mrtrust</i>. Use with caution.</p>
<dt>-p</p>
<dd>
<dt>&#8211;path</p>
<dd> This obsolete flag is ignored.</dl>
<h2>MRCONFIG FILES</h2>
<p> Here is an example <i>.mrconfig</i> file: </p>
<pre><code>
[src] checkout = svn checkout svn : // svn.example.com/src/trunk src
                                    chain = true
                                        [src / linux - 2.6] checkout = git clone git : // git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux-2.6.git &amp;&amp;
                                                                                       cd linux -
                                                                                       2.6 &amp;&amp;
                                                                       git checkout - b mybranch origin / master
</code></pre>
<p> The <i>.mrconfig</i> file uses a variant of the <font SIZE="-1">INI</font> file format. Lines starting with &#8220;#&#8221; are comments. Values can be continued to the following line by indenting the line with whitespace. </p>
<p> The <tt>&quot;DEFAULT&quot;</tt> section allows setting default values for the sections that come after it. </p>
<p> The <tt>&quot;ALIAS&quot;</tt> section allows adding aliases for actions. Each setting is an alias, and its value is the action to use. </p>
<p> All other sections add repositories. The section header specifies the directory where the repository is located. This is relative to the directory that contains the mrconfig file, but you can also choose to use absolute paths. (Note that you can use environment variables in section names; they will be passed through the shell for expansion. For example, <tt>&quot;[$HOSTNAME]&quot;</tt>, or <tt>&quot;[${HOSTNAME}foo]&quot;</tt>). </p>
<p> Within a section, each setting defines a shell command to run to handle a given action. mr contains default handlers for &#8220;update&#8221;, &#8220;status&#8221;, &#8220;commit&#8221;, and other standard actions. </p>
<p> Normally you only need to specify what to do for &#8220;checkout&#8221;. Here you specify the command to run in order to create a checkout of the repository. The command will be run in the parent directory, and must create the repository&#8217;s directory. So use <tt>&quot;git clone&quot;</tt>, <tt>&quot;svn checkout&quot;</tt>, <tt>&quot;bzr branch&quot;</tt> or <tt>&quot;bzr checkout&quot;</tt> (for a bound branch), etc. </p>
<p> Note that these shell commands are run in a <tt>&quot;set -e&quot;</tt> shell environment, where any additional parameters you pass are available in <tt>$@</tt>. All commands other than &#8220;checkout&#8221; are run inside the repository, though not necessarily at the top of it. </p>
<p> The <tt>&quot;MR_REPO&quot;</tt> environment variable is set to the path to the top of the repository. (For the &#8220;register&#8221; action, &#8220;<font SIZE="-1">MR_REPO&#8221;</font> is instead set to the basename of the directory that should be created when checking the repository out.) </p>
<p> The <tt>&quot;MR_CONFIG&quot;</tt> environment variable is set to the .mrconfig file that defines the repo being acted on, or, if the repo is not yet in a config file, the <i>.mrconfig</i> file that should be modified to register the repo. </p>
<p> The <tt>&quot;MR_ACTION&quot;</tt> environment variable is set to the command being run (update, checkout, etc). </p>
<p> A few settings have special meanings:</p>
<dl>
<dt>skip</p>
<dd> If &#8220;skip&#8221; is set and its command returns true, then <code>mr</code> will skip acting on that repository. The command is passed the action name in <tt>$1</tt>. </p>
<p> Here are two examples. The first skips the repo unless mr is run by joey. The second uses the hours_since function (included in mr&#8217;s built-in library) to skip updating the repo unless it&#8217;s been at least 12 hours since the last update. </p>
<pre><code>
[mystuff] checkout = ... skip = test `whoami` != joey
                                                     [linux] checkout = ... skip = ["$1" = update] &amp;&amp; !hours_since "$1" 12
</code></pre>
<p> Another way to use skip is for a lazy checkout. This makes mr skip operating on a repo unless it already exists. To enable the repo, you have to explicitly check it out (using &#8220;mr &#8211;force -d foo checkout&#8221;). </p>
<pre>
  [foo]
  checkout = ...
  skip = lazy
</pre>
<dt>order</p>
<dd> The &#8220;order&#8221; setting can be used to override the default ordering of repositories. The default order value is 10. Use smaller values to make repositories be processed earlier, and larger values to make repositories be processed later. </p>
<p> Note that if a repository is located in a subdirectory of another repository, ordering it to be processed earlier is not recommended.</p>
<dt>chain</p>
<dd> If &#8220;chain&#8221; is set and its command returns true, then <code>mr</code> will try to load a <i>.mrconfig</i> file from the root of the repository.</p>
<dt>include</p>
<dd> If &#8220;include&#8221; is set, its command is ran, and should output additional mrconfig file content. The content is included as if it were part of the including file. </p>
<p> Unlike everything else, &#8220;include&#8221; does not need to be placed within a section. </p>
<p> <code>mr</code> ships several libraries that can be included to add support for additional version control type things (unison, git-svn, git-fake-bare, git-subtree). To include them all, you could use: </p>
<pre>
  include = cat /usr/share/mr/*
</pre>
<p> See the individual files for details.</p>
<dt>deleted</p>
<dd> If &#8220;deleted&#8221; is set and its command returns true, then <code>mr</code> will treat the repository as deleted. It won&#8217;t ever actually delete the repository, but it will warn if it sees the repository&#8217;s directory. This is useful when one mrconfig file is shared among multiple machines, to keep track of and remember to delete old repositories.</p>
<dt>lib</p>
<dd> The &#8220;lib&#8221; setting can contain some shell code that will be run before each command, this can be a useful way to define shell functions for other commands to use. </p>
<p> Unlike most other settings, this can be specified multiple times, in which case the chunks of shell code are accumulatively concatenated together.</p>
<dt>fixups</p>
<dd> If &#8220;fixups&#8221; is set, its command is run whenever a repository is checked out, or updated. This provides an easy way to do things like permissions fixups, or other tweaks to the repository content, whenever the repository is changed.</p>
<dt>jobs</p>
<dd> If &#8220;jobs&#8221; is set, run the specified number of jobs in parallel. This can greatly speed up operations such as updates. </p>
<p> Note that running more than 10 jobs at a time is likely to run afoul of ssh connection limits. Running between 3 and 5 jobs at a time will yield a good speedup in updates without loading the machine too much.</p>
<dt>VCS_action</p>
<dd> When looking for a command to run for a given action, mr first looks for a setting with the same name as the action. If that is not found, it looks for a setting named &#8220;VCS_action&#8221; (substituting in the name of the version control system and the action). </p>
<p> Internally, mr has settings for &#8220;git_update&#8221;, &#8220;svn_update&#8221;, etc. To change the action that is performed for a given version control system, you can override these <font SIZE="-1">VCS</font> specific actions. To add a new version control system, you can just add <font SIZE="-1">VCS</font> specific actions for it.</p>
<dt>pre_ and post_</p>
<dd> If &#8220;pre_action&#8221; is set, its command is run before mr performs the specified action. Similarly, &#8220;post_action&#8221; commands are run after mr successfully performs the specified action. For example, &#8220;pre_commit&#8221; is run before committing; &#8220;post_update&#8221; is run after updating.</p>
<dt>_append</p>
<dd> Any setting can be suffixed with <tt>&quot;_append&quot;</tt>, to add an additional value to the existing value of the setting. In this way, actions can be constructed accumulatively.</p>
<dt>VCS_test</p>
<dd> The name of the version control system is itself determined by running each defined &#8220;VCS_test&#8221; action, until one succeeds.</dl>
<h2>UNTRUSTED MRCONFIG FILES</h2>
<p> Since mrconfig files can contain arbitrary shell commands, they can do anything. This flexibility is good, but it also allows a malicious mrconfig file to delete your whole home directory. Such a file might be contained inside a repository that your main <i>~/.mrconfig</i> checks out. To avoid worries about evil commands in a mrconfig file, mr defaults to reading all mrconfig files other than the main <i>~/.mrconfig</i> in untrusted mode. In untrusted mode, mrconfig files are limited to running only known safe commands (like &#8220;git clone&#8221;) in a carefully checked manner. </p>
<p> To configure mr to trust other mrconfig files, list them in <i>~/.mrtrust</i>. One mrconfig file should be listed per line. Either the full pathname should be listed, or the pathname can start with <i>~/</i> to specify a file relative to your home directory.</p>
<h2>OFFLINE LOG FILE</h2>
<p> The <i>~/.mrlog</i> file contains commands that mr has remembered to run later, due to being offline. You can delete or edit this file to remove commands, or even to add other commands for &#8216;mr online&#8217; to run. If the file is present, mr assumes it is in offline mode.</p>
<h2>EXTENSIONS</h2>
<p> mr can be extended to support things such as unison and git-svn. Some files providing such extensions are available in <i>/usr/share/mr/</i>. See the documentation in the files for details about using them.</p>
<h2>EXIT STATUS</h2>
<p> mr returns nonzero if a command failed in any of the repositories.</p>
<h2>AUTHOR</h2>
<p> Copyright 2007-2011 Joey Hess &lt;joey [at] kitenet.net&gt; </p>
<p> Licensed under the <font SIZE="-1">GNU GPL</font> version 2 or higher. </p>
<p> <a rel="nofollow" href="http://myrepos.branchable.com/">http://myrepos.branchable.com/</a> </p>
<h2>Index</h2>
