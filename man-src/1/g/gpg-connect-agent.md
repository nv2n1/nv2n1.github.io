---
title: "gpg-connect-agent(1)"
name: "gpg-connect-agent"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gpg-connect-agent/"
description: "gpg-connect-agent – Communicate with a running agent"
---

<h2 class="name">NAME</h2>
<p> <code>gpg-connect-agent</code> &#8211; Communicate with a running agent </p>
<h2>SYNOPSIS</h2>
<p> <code>gpg-connect-agent</code> [<i>options</i>]<i>[commands]</i> </p>
<h2>DESCRIPTION</h2>
<p> The <code>gpg-connect-agent</code> is a utility to communicate with a running <code>gpg-agent</code>. It is useful to check out the commands <code>gpg-agent</code> provides using the Assuan interface. It might also be useful for scripting simple applications. Input is expected at stdin and output gets printed to stdout. </p>
<p> It is very similar to running <code>gpg-agent</code> in server mode; but here we connect to a running instance. </p>
<p> The following options may be used: </p>
<dl>
<dt><code>-v</code></p>
<dd> <code>&#8211;verbose</code> Output additional information while running. </p>
<dt><code>-q</code></p>
<dd>
<dt><code>&#8211;quiet</code></p>
<dd> Try to be as quiet as possible. </p>
<dt><code>&#8211;homedir </code><i>dir</i></p>
<dd> Set the name of the home directory to <i>dir</i>. If this option is not used, the home directory defaults to &#8216;<i>~/.gnupg</i>&#8216;. It is only recognized when given on the command line. It also overrides any home directory stated through the environment variable &#8216;<i>GNUPGHOME</i>&#8216; or (on Windows systems) by means of the Registry entry <i>HKCU\Software\GNU\GnuPG:HomeDir</i>. </p>
<p> On Windows systems it is possible to install GnuPG as a portable application. In this case only this command line option is considered, all other ways to set a home directory are ignored. </p>
<p> To install GnuPG as a portable application under Windows, create an empty file named &#8216;<i>gpgconf.ctl</i>&#8216; in the same directory as the tool &#8216;<i>gpgconf.exe</i>&#8216;. The root of the installation is then that directory; or, if &#8216;<i>gpgconf.exe</i>&#8216; has been installed directly below a directory named &#8216;<i>bin</i>&#8216;, its parent directory. You also need to make sure that the following directories exist and are writable: &#8216;<i>ROOT/home</i>&#8216; for the GnuPG home and &#8216;<i>ROOT/var/cache/gnupg</i>&#8216; for internal cache files. </p>
<dt><code>&#8211;agent-program </code><i>file</i></p>
<dd> Specify the agent program to be started if none is running. The default value is determined by running <code>gpgconf</code> with the option <code>&#8211;list-dirs</code>. Note that the pipe symbol (<code>|</code>) is used for a regression test suite hack and may thus not be used in the file name. </p>
<dt><code>&#8211;dirmngr-program </code><i>file</i></p>
<dd> Specify the directory manager (keyserver client) program to be started if none is running. This has only an effect if used together with the option <code>&#8211;dirmngr</code>. </p>
<dt><code>&#8211;dirmngr</code></p>
<dd> Connect to a running directory manager (keyserver client) instead of to the gpg-agent. If a dirmngr is not running, start it. </p>
<dt><code>-S</code></p>
<dd> <code>&#8211;raw-socket </code><i>name</i> Connect to socket <i>name</i> assuming this is an Assuan style server. Do not run any special initializations or environment checks. This may be used to directly connect to any Assuan style socket server. </p>
<dt><code>-E</code></p>
<dd> <code>&#8211;exec</code> Take the rest of the command line as a program and it&#8217;s arguments and execute it as an Assuan server. Here is how you would run <code>gpgsm</code>:</p>
<dl>
<dt>
<dd>
<pre>
 gpg-connect-agent --exec gpgsm --server
</pre>
</dl>
<p> Note that you may not use options on the command line in this case. </p>
<dt><code>&#8211;no-ext-connect</code></p>
<dd> When using <code>-S</code> or <code>&#8211;exec</code>, <code>gpg-connect-agent</code> connects to the Assuan server in extended mode to allow descriptor passing. This option makes it use the old mode. </p>
<dt><code>&#8211;no-autostart</code></p>
<dd> Do not start the gpg-agent or the dirmngr if it has not yet been started. </p>
<dt><code>-r </code><i>file</i></p>
<dd> <code>&#8211;run </code><i>file</i> Run the commands from <i>file</i> at startup and then continue with the regular input method. Note, that commands given on the command line are executed after this file. </p>
<dt><code>-s</code></p>
<dd> <code>&#8211;subst</code> Run the command <code>/subst</code> at startup. </p>
<dt><code>&#8211;hex</code></p>
<dd> Print data lines in a hex format and the ASCII representation of non-control characters. </p>
<dt><code>&#8211;decode</code></p>
<dd> Decode data lines. That is to remove percent escapes but make sure that a new line always starts with a D and a space. </p>
</dl>
<h2>CONTROL COMMANDS</h2>
<p> While reading Assuan commands, gpg-agent also allows a few special commands to control its operation. These control commands all start with a slash (<code>/</code>). </p>
<dl>
<dt><code>/echo </code><i>args</i></p>
<dd> Just print <i>args</i>. </p>
<dt><code>/let </code><i>name</i> <i>value</i></p>
<dd> Set the variable <i>name</i> to <i>value</i>. Variables are only substituted on the input if the <code>/subst</code> has been used. Variables are referenced by prefixing the name with a dollar sign and optionally include the name in curly braces. The rules for a valid name are identically to those of the standard bourne shell. This is not yet enforced but may be in the future. When used with curly braces no leading or trailing white space is allowed. </p>
<p> If a variable is not found, it is searched in the environment and if found copied to the table of variables. </p>
<p> Variable functions are available: The name of the function must be followed by at least one space and the at least one argument. The following functions are available: </p>
<dl>
<dt>
<dd>
<dl>
<dt><code>get</code></p>
<dd> Return a value described by the argument. Available arguments are: </p>
<dl>
<dt>
<dd>
<dl>
<dt><code>cwd</code></p>
<dd> The current working directory.</p>
<dt><code>homedir</code></p>
<dd> The gnupg homedir.</p>
<dt><code>sysconfdir</code></p>
<dd> GnuPG&#8217;s system configuration directory.</p>
<dt><code>bindir</code></p>
<dd> GnuPG&#8217;s binary directory.</p>
<dt><code>libdir</code></p>
<dd> GnuPG&#8217;s library directory.</p>
<dt><code>libexecdir</code></p>
<dd> GnuPG&#8217;s library directory for executable files.</p>
<dt><code>datadir</code></p>
<dd> GnuPG&#8217;s data directory.</p>
<dt><code>serverpid</code></p>
<dd> The PID of the current server. Command <code>/serverpid</code> must have been given to return a useful value.</dl>
</dl>
<dt><code>unescape </code><i>args</i></p>
<dd> Remove C-style escapes from <i>args</i>. Note that <code>
