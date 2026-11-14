---
title: "lshell(1)"
name: "lshell"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lshell/"
description: "lshell – Limited Shell"
---

<h2 class="name">NAME</h2>
<p> lshell &#8211; Limited Shell</p>
<h2>SYNOPSIS</h2>
<p> <code>lshell </code> [<i>OPTIONS</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>lshell</code> provides a limited shell configured per user. The configuration is done quite simply using a configuration file. Coupled with ssh&#8217;s <i>authorized_keys </i> or with <i>/etc/shells</i> and <i>/etc/passwd</i> , it becomes very easy to restrict user&#8217;s access to a limited set of command. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;config </code><i>&lt;FILE&gt;</i></p>
<dd> Specify config file</p>
<dt><code>&#8211;log </code><i>&lt;DIR&gt;</i></p>
<dd> Specify the log directory</p>
<dt><code>&#8211;&lt;param&gt; </code><i>&lt;value&gt;</i></p>
<dd> where &lt;param&gt; is *any* config file parameter</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Show help message</p>
<dt><code>&#8211;version</code></p>
<dd> Show version </p>
</dl>
<h2>CONFIGURATION</h2>
<p> You can configure lshell through its configuration file:</p>
<dl>
<dt>
<dd>
<pre><code>
On Linux-&gt;/ etc / lshell.conf On * BSD-&gt;/ usr / {pkg, local} / etc / lshell.conf
</code></pre>
<p> <code>lshell</code> configuration has 4 types of sections:</p>
<dl>
<dt>
<dd>
[global] -&gt; lshell system configuration(only 1)<br />
             [default] -&gt; lshell default user configuration(only 1)<br />
                              [foo]<br />
                                  -&gt;UNIX username &#8220;foo&#8221; specific configuration<br />
                          [grp:bar]<br />
                                  -&gt;UNIX groupname &#8220;bar&#8221; specific configuration<br />
 Order of priority when loading preferences is the following:</p>
<dl>
<dt>
<dd>
<pre>
1- User configuration
2- Group configuration
3- Default configuration
</dl>
</pre>
<h3>[global]</h3>
<dl>
<dt><i>logpath</i></p>
<dd> config path (default is /var/log/lshell/)</p>
<dt><i>loglevel</i></p>
<dd> 0, 1, 2, 3 or 4 (0: no logs -&gt; 4: logs everything)</p>
<dt><i>logfilename</i></p>
<dd> &#8211; set to <code>syslog</code> in order to log to syslog</p>
<dl>
<dt>
<dd> &#8211; set log file name, e.g. %u-%y%m%d (i.e foo-20091009.log): <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>%u</code> -&gt; username</dl>
<dl>
<dt>
<dd> <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>%d</code> -&gt; day [1..31]</dl>
<dl>
<dt>
<dd> <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>%m</code> -&gt; month [1..12]</dl>
<dl>
<dt>
<dd> <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>%y</code> -&gt; year [00..99]</dl>
<dl>
<dt>
<dd> <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>%h</code> -&gt; time [00:00..23:59]</dl>
<dt><i>syslogname</i></p>
<dd> in case you are using syslog, set your logname (default: lshell)</p>
<dl>
<dt>
<dd></dl>
</dl>
<h3>[default] and/or [username] and/or [grp:groupname]</h3>
<dl>
<dt>
<dt><i>aliases</i></p>
<dd>
<dd> command aliases list (similar to bash&#8217;s alias directive)</p>
<dt><i>allowed</i></p>
<dd> a list of the allowed commands or set to &#8216;all&#8217; to allow all commands in user&#8217;s PATH</p>
<dt><i>allowed_cmd_path</i></p>
<dd> a list of path; all executable files inside these path will be allowed</p>
<dt><i>env_path</i></p>
<dd> update the environment variable $PATH of the user (optional)</p>
<dt><i>env_vars</i></p>
<dd> set environment variables (optional)</p>
<dt><i>forbidden</i></p>
<dd> a list of forbidden characters or commands</p>
<dt><i>history_file</i></p>
<dd> set the history filename. A wildcard can be used:</p>
<dl>
<dt>
<dd> <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>%u</code> -&gt; username (e.g. &#8216;/home/%u/.lhistory&#8217;)</dl>
<dt><i>history_size</i></p>
<dd> set the maximum size (in lines) of the history file</p>
<dt><i>home_path (deprecated)</i></p>
<dd> set the home folder of your user. If not specified, the home directory is set to the $HOME environment variable. This variable will be removed in the next version of lshell, please use your system&#8217;s tools to set a user&#8217;s home directory. A wildcard can be used:</p>
<dl>
<dt>
<dd> <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>%u</code> -&gt; username (e.g. &#8216;/home/%u&#8217;)</dl>
<dt><i>intro</i></p>
<dd> set the introduction to print at login</p>
<dt><i>login_script</i></p>
<dd> define the script to run at user login</p>
<dt><i>passwd</i></p>
<dd> password of specific user (default is empty)</p>
<dt><i>path</i></p>
<dd> list of path to restrict the user geographically. It is possible to use wildcards (e.g. &#8216;/var/log/ap*&#8217;).</p>
<dt><i>prompt</i></p>
<dd> set the user&#8217;s prompt format (default: username)</p>
<dl>
<dt>
<dd> <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>%u</code> -&gt; username</dl>
<dl>
<dt>
<dd> <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>%h</code> -&gt; hostname</dl>
<dt><i>prompt_short</i></p>
<dd> set sort prompt current directory update &#8211; set to 1 or 0 <i>overssh</i> list of command allowed to execute over ssh (e.g. rsync, rdiff-backup, scp, etc.)</p>
<dt><i>scp</i></p>
<dd> allow or forbid the use of scp connection &#8211; set to 1 or 0</p>
<dt><i>scpforce</i></p>
<dd> force files sent through scp to a specific directory</p>
<dt><i>scp_download</i></p>
<dd> set to 0 to forbid scp downloads (default is 1)</p>
<dt><i>scp_upload</i></p>
<dd> set to 0 to forbid scp uploads (default is 1)</p>
<dt><i>sftp</i></p>
<dd> allow or forbid the use of sftp connection &#8211; set to 1 or 0</p>
<dt><i>sudo_commands</i></p>
<dd> a list of the allowed commands that can be used with <a href="/docs/linux/man/8-sudo/">sudo</a>(8)</p>
<dt><i>timer</i></p>
<dd> a value in seconds for the session timer</p>
<dt><i>strict</i></p>
<dd> logging strictness. If set to 1, any unknown command is considered as forbidden, and user&#8217;s warning counter is decreased. If set to 0, command is considered as unknown, and user is only warned (i.e. *** unknown synthax)</p>
<dt><i>warning_counter</i></p>
<dd> number of warnings when user enters a forbidden value before getting exited from lshell. Set to <code>-1</code> to disable the counter, and just warn the user. </p>
</dl>
<h2>SHELL BUILTIN COMMANDS</h2>
<p> Here is the set of commands that are always available with lshell:</p>
<dl>
<dt><i>clear</i></p>
<dd> clears the terminal</p>
<dt><i>help, ?</i></p>
<dd> print the list of allowed commands</p>
<dt><i>history</i></p>
<dd> print the commands history</p>
<dt><i>lpath</i></p>
<dd> lists all allowed and forbidden path</p>
<dt><i>lsudo</i></p>
<dd> lists all sudo allowed commands </p>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>$ lshell</code></p>
<dd>
<dl>
<dt>
<dd> Tries to run lshell using default ${PREFIX}/etc/lshell.conf as configuration file. If it fails a warning is printed and lshell is interrupted. lshell options are loaded from the configuration file</dl>
<dt><code>$ lshell &#8211;config /path/to/myconf.file &#8211;log /path/to/mylog.log</code></p>
<dd>
<dl>
<dt>
<dd> This will override the default options specified for configuration and/or log file</dl>
</dl>
<h2>USE CASE</h2>
<p> The primary goal of lshell, was to be able to create shell accounts with ssh access and restrict their environment to a couple a needed commands. In this example, User &#8216;foo&#8217; and user &#8216;bar&#8217; both belong to the &#8216;users&#8217; UNIX group:</p>
<dl>
<dt><code>User foo:</code></p>
<dd>
<dl>
<dt>
<dd>
&nbsp;<wbr>&#8211; must be able to access&nbsp;<wbr>/usr and&nbsp;<wbr>/var but not&nbsp;<wbr>/usr/local<br />
&nbsp;<wbr>&#8211; user all command in his PATH but&nbsp;<wbr>&#8216;su&#8217;<br />
&nbsp;<wbr>&#8211; has a warning counter set to 5<br />
&nbsp;<wbr>&#8211; has his home path set to&nbsp;<wbr>&#8216;/home/users&#8217;</dl>
<dt><code>User bar:</code></p>
<dd>
<dl>
<dt>
<dd>
&nbsp;<wbr>&#8211; must be able to access&nbsp;<wbr>/etc and&nbsp;<wbr>/usr but not&nbsp;<wbr>/usr/local<br />
&nbsp;<wbr>&#8211; is allowed default commands plus&nbsp;<wbr>&#8216;ping&#8217;&nbsp;<wbr>minus&nbsp;<wbr>&#8216;ls&#8217;<br />
&nbsp;<wbr>&#8211; strictness is set to 1&nbsp;<wbr>(meaning he is not allowed to type an unknown command)</dl>
<p> In this case, my configuration file will look something like this:</p>
<dl>
<dt>
<dd>
<pre><code>
#CONFIURATION START
[global] logpath : / var / log / lshell /
                   loglevel : 2
                       [default] allowed : [ 'ls', 'pwd' ] forbidden : [ ';', '&amp;', '|' ] warning_counter : 2 timer : 0 path : [ '/etc', '/usr' ] env_path : ':/sbin:/usr/bin/' scp : 1 # or
    0 sftp : 1 # or 0 overssh : [ 'rsync', 'ls' ] aliases : {'ls' : 'ls --color=auto', 'll' : 'ls -l'} [grp:users] warning_counter : 5 overssh : -['ls'][foo] allowed : 'all' - ['su'] path : [ '/var', '/usr' ] - ['/usr/local'] home_path : '/home/users'[bar] allowed : +['ping'] - ['ls'] path : -['/usr/local'] strict : 1 scpforce : '/home/bar/uploads/'
#CONFIURATION END
</code></pre>
</dl>
<h2>NOTES</h2>
<dl>
<dt>In order to log a user&#8217;s warnings into the logging directory (default <i>/var/log/lshell/</i>) , you must firt create the folder (if it doesn&#8217;t exist yet) and chown it to lshell group:</p>
<dd>
<dl>
<dt>
<dd>
<pre>
# addgroup --system lshell
# mkdir /var/log/lshell
# chown :lshell /var/log/lshell
# chmod 770 /var/log/lshell
</dl>
</pre>
<p> then add the user to the <i>lshell</i> group:</p>
<dl>
<dt>
<dd>
<pre>
# usermod -aG lshell user_name
</dl>
</pre>
<p> In order to set lshell as default shell for a user:</p>
<dl>
<dt>
<dd>
<pre>
On Linux:
# chsh -s /usr/bin/lshell user_name
On *BSD:
# chsh -s /usr/{pkg,local}/bin/lshell user_name
</dl>
</pre>
</dl>
<h2>AUTHOR</h2>
<p> Currently maintained by Ignace Mouzannar (ghantoos) </p>
<h2>EMAIL</h2>
<p> Feel free to send me your recommendations at &lt;ghantoos [at] ghantoos.org&gt; </p>
<h2>Index</h2>
