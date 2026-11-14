---
title: "pwsafe(1)"
name: "pwsafe"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pwsafe/"
description: "pwsafe – commandline password database utility compatible with Counterpane’s Passwordsafe"
---

<h2>NAME</h2>
<p> pwsafe &#8211; commandline password database utility compatible with Counterpane&#8217;s Passwordsafe</p>
<h2>SYNOPSIS</h2>
<p> <code>pwsafe</code> [options] command [arg]</p>
<h2>DESCRIPTION</h2>
<p> <code>pwsafe</code> manipulates Counterpane Passwordsafe username/password databases. </p>
<p> It is compatible with Counterpane Passwordsafe 1.9.x and 2.0 databases.</p>
<h2>COMMANDS</h2>
<p> <code>pwsafe</code> accepts the following commands:</p>
<dl>
<dt><code>&#8211;createdb</code></p>
<dd> Create a new database.</p>
<dt><code>&#8211;exportdb</code></p>
<dd> Export database as text.</p>
<dt><code>&#8211;mergedb=DATABASE_FILE</code></p>
<dd> Merge DATABASE_FILE into database. Common entries are merged interactively.</p>
<dt><code>&#8211;passwd</code></p>
<dd> Change the database&#8217;s passphrase.</p>
<dt><code>&#8211;list[=REGEX]</code></p>
<dd> List all [matching] entries in database. If -u or -p is given then REGEX must match only one entry, and only the requested field(s) are emitted.</p>
<dt><code>-a, &#8211;add[=NAME]</code></p>
<dd> Add an entry to database.</p>
<dt><code>-e, &#8211;edit=REGEX</code></p>
<dd> Edit an entry.</p>
<dt><code>&#8211;delete=NAME</code></p>
<dd> Delete an entry from database.</p>
<dt>If no command is given, an interactive mode is entered.</p>
<dd></dl>
<h2>OPTIONS</h2>
<p> <code>pwsafe</code> accepts the following options:</p>
<dl>
<dt><code>-f, &#8211;file=DATABASE_FILE</code></p>
<dd> Specify the database to manipulate. Default is $HOME/.pwsafe.dat</p>
<dt><code>&#8211;dbversion=[1|2]</code></p>
<dd> Specify the database&#8217;s version. Default is 2.</p>
<dt><code>-I, &#8211;case</code></p>
<dd> REGEX is case-sensative. Any uppercase character in REGEX implies &#8211;case.</p>
<dt><code>-l</code></p>
<dd> Show login and notes in list output.</p>
<dt><code>-u, &#8211;username</code></p>
<dd> Show username of listed account(s).</p>
<dt><code>-p, &#8211;password</code></p>
<dd> Show password of listed accounts(s).</p>
<dt><code>-E, &#8211;echo</code></p>
<dd> Force echo&#8217;ing of entry to stdout. This is selected by default if $DISPLAY is not set.</p>
<dt><code>-o, &#8211;output=FILE</code></p>
<dd> Redirect username and password output to FILE. Implies &#8211;echo.</p>
<dt><code>-x, &#8211;xclip</code></p>
<dd> Force copying of username and password to X clipboard. This is selected by default if $DISPLAY is set.</p>
<dt><code>-d, &#8211;display=XDISPLAY</code></p>
<dd> Override $DISPLAY. Implies &#8211;xclip.</p>
<dt><code>-s, &#8211;selection={Primary,Secondary,Clipboard,Both}</code></p>
<dd> Select the X selection effected. Default is Both primary and clipboard. Implies &#8211;xclip.</p>
<dt><code>-G, &#8211;ignore=NAME [at] HOST</code></p>
<dd> Add NAME to windows or hosts that do not receive the selection. If just NAME is given it matches any host, and if just @HOST is given it matches any name.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd> Print more information.</p>
<dt><code>-q, &#8211;quiet</code></p>
<dd> Print less information. In fact, print only exactly what was requested.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Show summary of options.</p>
<dt><code>-V, &#8211;version</code></p>
<dd> Show version of program. </p>
</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt>PWSAFE_DATABASE</p>
<dd> Default database file. If this is a relative path it is assumed to be relative to $HOME. Defaults to &quot;.pwsafe.dat&quot;. Overridden by -f.</p>
<dt>PWSAFE_DEFAULT_USER</p>
<dd> Default user. Defaults to $USER or $LOGNAME.</p>
<dt>PWSAFE_IGNORE</p>
<dd> Overrides built-in &#8211;ignore list. &#8211;ignore overrides. Format is a list of &#8211;ignore arguments, seperated by colons (&#8216;:&#8217;).</p>
<dt>HOME</p>
<dd> Used to locate the default database &quot;~/.pwsafe.dat&quot; and default RANDFILE &quot;~/.rnd&quot;.</p>
<dt>RANDFILE</p>
<dd> Used to locate the random number generator entropy pool file. Defaults to &quot;$HOME/.rnd&quot;.</dl>
<h2>FILES</h2>
<dl>
<dt>~/.pwsafe.dat</p>
<dd> The password database.</p>
<dt>~/.pwsafe.dat~</p>
<dd> Backup of database.</p>
<dt>~/.rnd</p>
<dd> Random number generator&#8217;s entropy pool.</dl>
<h2>WARNINGS</h2>
<p> Use a good password for your database. </p>
<p> Don&#8217;t use pwsafe over telnet or from untrusted terminals. </p>
<p> To seed RANDFILE decently, do something like </p>
<p>md5sum&nbsp;<wbr>/var/log/*&nbsp;<wbr>&gt;~/.rnd</p>
<h2>EXAMPLES</h2>
<p> For those who can&#8217;t read the rest of this file:</p>
<dl>
<dt>Create $HOME/.pwsafe.dat.</p>
<dd>
<p> pwsafe &#8211;createdb</p>
<dt>Add an entry named &#8216;test&#8217;.</p>
<dd>
<p> pwsafe -a test</p>
<dt>Copy username and password of &#8216;test&#8217; to console or X clipboard &amp; primary selection.</p>
<dd>
<p> pwsafe -up test</p>
<dt>Upgrade a version passwordsafe version 1.7 database to version 2.0 (we do this by merging it with itself, but specifying version 2 output)</p>
<dd>
<p> pwsafe &#8211;mergedb $HOME/.pwsafe.dat &#8211;dbversion 2</dl>
<h2>AUTHOR</h2>
<p> Nicolas S. Dade &lt;ndade [at] nsd.dyndns.org&gt;.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;ndade [at] nsd.dyndns.org&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright © 2004-2005 Nicolas S. Dade. </p>
<p> This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>SEE ALSO</h2>
<p> <a rel="nofollow" href="http://nsd.dyndns.org/pwsafe/">http://nsd.dyndns.org/pwsafe/</a><br />
 <a rel="nofollow" href="http://passwordsafe.sourceforge.net/,">http://passwordsafe.sourceforge.net/,</a> <a rel="nofollow" href="http://www.counterpane.com/">http://www.counterpane.com/</a> </p>
<h2>Index</h2>
