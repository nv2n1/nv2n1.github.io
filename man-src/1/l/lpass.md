---
title: "lpass(1)"
name: "lpass"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lpass/"
description: "lpass – command line interface for LastPass"
---

<h2 class="name">NAME</h2>
<p> lpass &#8211; command line interface for LastPass </p>
<h2>SYNOPSIS</h2>
<pre><code>
lpass[--version, -v | --help, -h] lpass&lt;subcommand&gt;[&lt;args&gt;]
</code></pre>
<h2>DESCRIPTION</h2>
<p> <i>lpass</i> is a simple command line interface to LastPass. It is comprised of several subcommands: </p>
<dl>
<dt>
<dd>
<pre><code>
lpass login[--trust][--plaintext - key[--force, -f]][--color = auto | never | always] USERNAME
        lpass logout[--force, -f][--color = auto | never | always] lpass passwd
            lpass show[--sync = auto | now | no][--clip, -c][--expand - multi, -x][--all | --username | --password | --url | --notes | --field = FIELD | --id | --name][--basic - regexp, -G | --fixed - strings, -F][--color = auto | never | always]{NAME | UNIQUEID} *
    lpass ls[--sync = auto | now | no][--long, -l][-m][-u][--color = auto | never | always][GROUP] lpass mv[--sync = auto | now | no][--color = auto | never | always]{UNIQUENAME | UNIQUEID} GROUP
        lpass edit[--sync = auto | now | no][--non - interactive]{--name | --username, -u | --password, -p | --url | --notes | --field = FIELD}[--color = auto | never | always]{NAME | UNIQUEID} lpass generate[--sync = auto | now | no][--clip, -c][--username = USERNAME][--url = URL][--no - symbols][--color = auto | never | always]{NAME | UNIQUEID} LENGTH
            lpass duplicate[--sync = auto | now | no][--color = auto | never | always]{UNIQUENAME | UNIQUEID} lpass rm[--sync = auto | now | no][--color = auto | never | always]{UNIQUENAME | UNIQUEID} lpass sync[--background, -b][--color = auto | never | always] lpass export[--sync = auto | now | no][--color = auto | never | always] lpass share userls SHARE
                lpass share useradd[--read - only = [true | false]][--hidden = [true | false]][--admin = [true | false]] SHARE USERNAME
                    lpass share usermod[--read - only = [true | false]][--hidden = [true | false]][--admin = [true | false]] SHARE USERNAME
                        lpass share userdel SHARE USERNAME
                            lpass share create SHARE
                                lpass share rm SHARE
</code></pre>
</dl>
<h3>Synchronization</h3>
<p> The <i>&#8211;sync</i> options control when the current operation involves a synchronization with the server. If <i>now</i> is set, and the command makes a change, the change is synchronized before the command exits. If <i>now</i> is set, and the command displays a value, the local cache is synchronized before the value is shown. If <i>now</i> is set, and the command is otherwise successful, but synchronization fails, the command will return an error. If <i>auto</i> is set, and the command makes a change, the change is synchronized to the server in the background. If <i>auto</i> is set, and the command displays a value, the local cache is synchronized before the value is shown only if the local cache is more than 5 seconds (or <i>LPASS_AUTO_SYNC_TIME</i> seconds, if set) old. If <i>no</i> is set, the command will not interact with the server, unless there is a current upload queue being processed. Any local changes that are not synchronized with the server will exist in a queue of timestamped requests which will be synchronized on the next occurring synchronization. </p>
<p> The <i>sync</i> command forces a synchronization of the local cache with the LastPass servers, and does not exit until the local cache is synchronized or until an error occurs. Alternatively, if <i>&#8211;background</i> is specified, the synchronization occurs in a daemonized process.</p>
<h3>Agent</h3>
<p> An agent process will be spawned in the background on a first successful command, and all subsequent commands will use the agent for decryption, instead of asking a user for a password. The agent will quit after one hour, unless the <i>LPASS_AGENT_TIMEOUT</i> environment variable is set to an alternative number of seconds in which to quit, or 0 to never quit. If the environment variable <i>LPASS_AGENT_DISABLE</i> is set to 1, the agent will not be used.</p>
<h3>Password Entry</h3>
<p> If available, the <code>pinentry</code> program, part of <code><a href="/docs/linux/man/1-gpg2/">gpg2</a></code>(1), may be used for inputting passwords if it is installed. If unavailable, or if the <i>LPASS_DISABLE_PINENTRY</i> environment variable is set to 1, passwords will be read from standard input and a prompt will be displayed on standard error. </p>
<p> The program used for inputting passwords may also be configured by setting the <i>LPASS_ASKPASS` environment variable. &#8216;LPASS_ASKPASS</i> is expected to be a binary that produces a prompt using its first command-line argument, and outputs the entered password to standard out. ssh-askpass implements this protocol, as does the following shell script: </p>
<dl>
<dt>
<dd>
<pre>
#!/bin/bash
echo -n &quot;$*: &quot; &gt;/dev/stderr
stty -echo
read answer
stty echo
echo $answer
</pre>
</dl>
<h3>Entry Specification</h3>
<p> Commands that take a <i>UNIQUENAME</i> will fail if the provided name is used multiple times, and return an error. Commands may alternatively take a <i>UNIQUEID</i>, which will be the integer <i>ID</i> provided by LastPass for identifying entries uniquely. Commands that take either a <i>NAME</i> or a <i>UNIQUEID</i> will create a new entry if a <i>NAME</i> is specified and otherwise overwrite an existing entry if <i>UNIQUEID</i> is specified.</p>
<h3>Logging In</h3>
<p> The <i>login</i> subcommand will initialize a cache and configuration folder inside the current user&#8217;s home directory &#8211; <i>~/.lpass</i> &#8211; or in the directory specified by the environment variable <i>LPASS_HOME</i>. It will then attempt to authenticate itself with the LastPass servers, using the provided command line credentials or by interactively prompting (in the case of multifactor or an unprovided password). The <i>&#8211;trust</i> option will cause subsequent logins to not require multifactor authentication. If the <i>&#8211;plaintext-key</i> option is specified, the decryption key will be saved to the hard disk in plaintext. Please note that use of this option is discouraged except in limited situations, as it greatly decreases the security of data. </p>
<p> The <i>logout</i> subcommand will remove the local cache and stored encryption keys. It will prompt the user to confirm, unless <i>&#8211;force</i> is specified.</p>
<h3>Viewing</h3>
<p> The <i>show</i> subcommand will display a password or selected field. </p>
<p> The <i>ls</i> subcommand will list names in groups in a tree structure. If the <i>&#8211;long</i> or <i>-l</i> option is set, then also list the last modification time. The <i>-u</i> option may be passed to show the last use (last touch) time instead, if available. Both times are in GMT. </p>
<p> The <i>export</i> subcommand will dump all account information including passwords to stdout (unencrypted).</p>
<h3>Modifying</h3>
<p> The <i>edit</i> subcommand will edit the selected field. If <i>&#8211;non-interactive</i> is not set, the selected field will be edited using <i>EDITOR</i>; otherwise the command will accept data until EOF or, unless the notes field is being edited, the first new line. Please note that when editing interactively, the contents of the field may be saved on disk in tmp files or in editor swap files, depending on your system configuration. </p>
<p> The <i>generate</i> subcommand will create a randomly generated password for the chosen key name, and optionally add a url and username while inserting the generated password. </p>
<p> The <i>rm</i> command will remove the specified entry, and the <i>duplicate</i> command will create a duplicate entry of the one specified, but with a different <i>ID</i>.</p>
<h3>Shared Folder Commands</h3>
<p> The <i>share</i> command and its accompanying subcommands can be used to manipulate shared folders, if available to the (enterprise or premium) user. The <i>userls</i>, <i>useradd</i>, <i>usermod</i>, and <i>userdel</i> subcommands may be used to query and modify membership of the shared folder, while the <i>create</i> and <i>rm</i> share subcommands may be used to add new, or delete existing shared folders. The normal <i>generate</i> and <i>edit</i> commands may be used to edit accounts within the shared folder.</p>
<h3>Clipboard</h3>
<p> Commands that take a <i>-c</i> or <i>&#8211;clip</i> option will copy the output to the clipboard, using <code><a href="/docs/linux/man/1-xclip/">xclip</a></code>(1) or <code><a href="/docs/linux/man/1-xsel/">xsel</a></code>(1) on X11-based systems, <code><a href="/docs/linux/man/1-pbcopy/">pbcopy</a></code>(1) on OSX, or <code>putclip</code> on Cygwin. The command to be used can be overridden by specifying the LPASS_CLIPBOARD_COMMAND environment variable.</p>
<h3>Color Output</h3>
<p> The <i>&#8211;color</i> option controls colored output to the terminal. By default, commands will use <i>&#8211;color=auto</i>, in which color output is used unless the output is not a tty (for example, when passed to a pipe or file). If <i>always</i> is used, colors are produced regardless of the output detection. If <i>never</i> is used, no color escape sequences are emitted.</p>
<h3>Configuration</h3>
<p> All configuration may be specified via environment variables. Alternatively, a set of environment variable overrides may be specified in <i>~/.lpass/env</i> in the form of: </p>
<dl>
<dt>
<dd>
<pre>
VARIABLE1=VALUE1
VARIABLE2=VALUE2
...
</pre>
</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<p> The following environment variables may be used for configuration as described in the section above: </p>
<dl>
<dt>
<dd> &bull; <i>LPASS_HOME</i></dl>
<dl>
<dt>
<dd> &bull; <i>LPASS_AUTO_SYNC_TIME</i></dl>
<dl>
<dt>
<dd> &bull; <i>LPASS_AGENT_TIMEOUT</i></dl>
<dl>
<dt>
<dd> &bull; <i>LPASS_AGENT_DISABLE</i></dl>
<dl>
<dt>
<dd> &bull; <i>LPASS_DISABLE_PINENTRY</i></dl>
<dl>
<dt>
<dd> &bull; <i>LPASS_ASKPASS</i></dl>
<dl>
<dt>
<dd> &bull; <i>LPASS_CLIPBOARD_COMMAND</i></dl>
<h2>Index</h2>
