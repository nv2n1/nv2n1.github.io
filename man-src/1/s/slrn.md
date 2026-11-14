---
title: "slrn(1)"
name: "slrn"
section: "1"
letter: "s"
url: "/docs/linux/man/1-slrn/"
description: "slrn – An easy to use NNTP / spool based newsreader."
---

<h2 class="name">NAME</h2>
<p> slrn &#8211; An easy to use NNTP / spool based newsreader. </p>
<h2>SYNOPSIS</h2>
<p> <code>slrn</code> [-aCdknmw] [-C-] [-D<i>name</i>] [-f&nbsp;<wbr><i>newsrc-file</i>] [-i&nbsp;<wbr><i>config-file</i>] [-k0] [&#8211;create] [&#8211;debug&nbsp;<wbr><i>file</i>] [&#8211;help] [&#8211;inews] [&#8211;kill-log <i>file</i>] [&#8211;nntp [-h&nbsp;<wbr><i>server</i>] [-p&nbsp;<wbr><i>port</i>]] [&#8211;show-config] [&#8211;spool] [&#8211;version]</p>
<h2>DESCRIPTION</h2>
<p> <i>slrn</i> is an easy to use but powerful NNTP / spool based newsreader. </p>
<p> It is highly customizable, supports scoring, free key bindings and can be extended using the embedded S-Lang interpreter. </p>
<p> To use slrn, you either need to set the <i>NNTPSERVER</i> environment variable to the server you want to read news from or specify a server on the command line. A <i>newsrc</i> file is needed, too. In case you do not yet have one, you can create it using &#8220;slrn -f ~/.jnewsrc &#8211;create&#8221;. </p>
<p> Inside slrn, online help is available via the &#8216;?&#8217; key.</p>
<h2>OPTIONS</h2>
<p> The following options can be used when calling slrn from the command line. They override both environment variables and settings in private and global configuration files.</p>
<dl>
<dt>-a</p>
<dd> Read active file when checking for new news.</p>
<dt>-C</p>
<dd> Use colors without checking if the terminal supports it.</p>
<dt>-C-</p>
<dd> Don&#8217;t use colors, even if the terminal supports it.</p>
<dt>-d</p>
<dd> Get group descriptions (taglines) from the news server. Please note that this may cause a download of several hundred kilobytes and thus can take a long time. The output is saved to a local file, so you only need to do this once. May not be specified in combination with <i>&#8211;create</i>.</p>
<dt>-D<i>name</i></p>
<dd> Add name to the list of predefined preprocessing tokens, which can be used in your slrnrc file to have conditionally interpreted lines. See the slrn reference manual for details.</p>
<dt>-f <i>newsrc-file</i></p>
<dd> Use file as the newsrc file for this session. This is permanently set via the <i>server</i> configuration command.</p>
<dt>-h <i>host[:port]</i></p>
<dd> Connect to the NNTP server on <i>host</i>, overriding the <i>$NNTPSERVER</i> environment variable. If no <i>port</i> is given, the default NNTP port (119) will be used. This option is only accepted after <i>&#8211;nntp</i> or when NNTP is the default mode.</p>
<dt>-i <i>config-file</i></p>
<dd> Read file as the initialization (slrnrc) file. The default is to use .slrnrc (or slrn.rc on VMS, OS/2 and Windows) in your home directory.</p>
<dt>-k</p>
<dd> Don&#8217;t read the <i>score file</i>.</p>
<dt>-k0</p>
<dd> Read the score file, but inhibit <i>expensive</i> scoring. A scoring rule is <i>expensive</i> if it contains header lines that are not included in the server&#8217;s overview files. This makes applying them slow.</p>
<dt>-m</p>
<dd> Force mouse support (without checking if it works on the current terminal).</p>
<dt>-n</p>
<dd> Do not check for new groups (usually resulting in a faster startup).</p>
<dt>-p <i>N</i></p>
<dd> Use port N to connect to the NNTP server.</p>
<dt>-w</p>
<dd> Wait for a key before switching to full screen mode, allowing the user to read startup messages.</p>
<dt>&#8211;create</p>
<dd> Read the active file (the list of all groups) from the news server to create an initial newsrc file.</p>
<dt>&#8211;debug <i>file</i></p>
<dd> Write debugging output to <i>file</i>.</p>
<dt>&#8211;help</p>
<dd> Show help for command line switches.</p>
<dt>&#8211;inews</p>
<dd> Use an external <i>inews program</i> to post articles.</p>
<dt>&#8211;kill-log <i>file</i></p>
<dd> Keep a log of all articles that were killed by the scorefile in <i>file</i>.</p>
<dt>&#8211;nntp</p>
<dd> Use builtin NNTP support for reading and posting (an external program is used to post if slrn was compiled with &#8211;enable-force-inews).</p>
<dt>&#8211;pull</p>
<dd> Spool outgoing articles locally for slrnpull to send.</p>
<dt>&#8211;show-config</p>
<dd> Print detailed information about slrn configuration.</p>
<dt>&#8211;spool</p>
<dd> Read directly from spool.</p>
<dt>&#8211;version</p>
<dd> Print version and some compile time settings.</dl>
<h2>ENVIRONMENT</h2>
<p> <i>slrn</i> uses the following list of environment variables. Note: environment variables can be overridden by configuration files or command line switches.</p>
<dl>
<dt><code>COLORTERM</code></p>
<dd> If this variable is set, slrn will assume that your terminal supports <i>ANSI color sequences</i>. It also enables a workaround for a problem with the <i>mouse reporting</i> when running slrn inside of an rxvt.</p>
<dt><code>DISPLAY</code></p>
<dd> If set, slrn assumes that X11 is running.</p>
<dt><code>EDITOR</code></p>
<dd> See <i>$SLRN_EDITOR</i>.</p>
<dt><code>HOME</code></p>
<dd> See <i>$SLRNHOME</i>.</p>
<dt><code>HOSTNAME</code></p>
<dd> If no <i>hostname</i> is given, the value of this environment variable is used.</p>
<dt><code>LOGNAME</code></p>
<dd> See <i>$USER</i>.</p>
<dt><code>NAME</code></p>
<dd> Set it to your realname, if slrn can&#8217;t determine it otherwise.</p>
<dt><code>NNTPSERVER</code></p>
<dd> You can use this variable to tell slrn which NNTP server to connect to. It can be overridden by the command line option -h.</p>
<dt><code>ORGANIZATION</code></p>
<dd> The name of your organization.</p>
<dt><code>PRINTER</code></p>
<dd> On unix systems, slrn pipes the current article to &#8220;lpr -P <i>$PRINTER</i>&#8221; to print it.</p>
<dt><code>PWD</code></p>
<dd> This variable is only used on unix systems that don&#8217;t support <a href="/docs/linux/man/3-getcwd/">getcwd</a>(3). In these cases, it should be set to the current directory at the time slrn is invoked. This is usually done by the shell and nothing the user has to worry about.</p>
<dt><code>REPLYTO</code></p>
<dd> The value of this variable is used as the default if you do not set <i>replyto</i> in your slrnrc file.</p>
<dt><code>SLANG_EDITOR</code></p>
<dd> See <i>$SLRN_EDITOR</i>.</p>
<dt><code>SLRNHELP</code></p>
<dd> You can set this variable to a file slrn should read its online help from. This is only needed when the default key bindings have been changed and you want the help function to reflect this. If unset, slrn looks for help.txt in the configuration directory.</p>
<dt><code>SLRNHOME</code></p>
<dd> When interpreting filenames as relative to your home directory, slrn uses this variable to find out what your home directory is. If <i>$SLRNHOME</i> is unset, <i>$HOME</i> is used instead.</p>
<dt><code>SLRN_EDITOR</code></p>
<dd> The editor to start for editing articles. If this variable is unset, slrn subsequently looks at <i>$SLANG_EDITOR</i>, <i>$EDITOR</i> and <i>$VISUAL</i>.</p>
<dt><code>SLRN_SLANG_DIR</code></p>
<dd> If set, slrn will search for slang macros here. If not set slrn will search in the default path, which is defined at compile time (usually share_dir/slang).</p>
<dt><code>TMP</code></p>
<dd> Indicates the directory in which slrn should save temporary files.</p>
<dt><code>TMPDIR</code></p>
<dd> See <i>$TMP</i>.</p>
<dt><code>USER</code></p>
<dd> Your username, if slrn can&#8217;t get it from the system by other means.</p>
<dt><code>VISUAL</code></p>
<dd> See <i>$SLRN_EDITOR</i>.</dl>
<h2>FILES</h2>
<dl>
<dt>$HOME/.slrnrc</p>
<dd> User-specific configuration file.</p>
<dt>config_dir/slrn.rc</p>
<dd> System-wide configuration file. config_dir is set at compile time (/usr/local/etc by default).</p>
<dt>$HOME/.jnewsrc</p>
<dd> default newsrc file for <i>slrn.</i></p>
<dt>$HOME/.jnewsrc.dsc</p>
<dd> Per user newsgroups descriptions.</p>
<dt>share_dir/newsgroups.dsc</p>
<dd> Global newsgroup descriptions. share_dir is set at compile time (/usr/local/share/slrn by default).</dl>
<h2>SEE ALSO</h2>
<p> The documentation that comes with <i>slrn</i>, especially FIRST_STEPS, manual.txt, FAQ and score.txt. If you consider writing S-Lang macros, also look at README.macros and slrnfuns.txt. </p>
<p> Recent versions of the slrn manual and the FAQ as well as additional information can also be found on slrn&#8217;s official home page: <a rel="nofollow" href="http://slrn.sourceforge.net/">http://slrn.sourceforge.net/</a> </p>
<p> Questions about <i>slrn</i> that are not covered by existing documentation may be posted to the newsgroup <i>news.software.readers</i> where they will be answered by knowledgeable users or the author of the program. In addition, announcements of new versions of <i>slrn</i> are posted there. </p>
<p> The latest version of <i>slrn</i> is available from <a rel="nofollow" href="http://prdownloads.sourceforge.net/slrn/">http://prdownloads.sourceforge.net/slrn/</a></p>
<h2>AUTHOR</h2>
<p> John E. Davis &lt;jed [at] jedsoft.org&gt; </p>
<h2>Index</h2>
