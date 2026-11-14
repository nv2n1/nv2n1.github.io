---
title: "repomapper(1)"
name: "repomapper"
section: "1"
letter: "r"
url: "/docs/linux/man/1-repomapper/"
description: "repomapper – update and manipulate contributor maps"
---

<h2 class="name">NAME</h2>
<p> repomapper &#8211; update and manipulate contributor maps </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>repomapper</code> [-i] [-p&nbsp;<wbr><i>passwordfile</i>] [-u&nbsp;<wbr><i>updatefile</i>] [-h&nbsp;<wbr><i>host</i>] <i>contribmap</i></dl>
<h2>DESCRIPTION</h2>
<dd>Older, centralized version-control systems such as CVS and SVN centralize a repository on one host and identify users by their account names on that host. Distributed version-control systems such as git and Mercurial identify users by a netwide-unique ID consisting of a name-among-humans followed by an email address. </p>
<p> When moving a repository from a centralized to a distributed system, therefore, one of the prerequisites is a contributor map that associates each account name on the old system to a DVCS-style ID on the new one. This tool automates parts of that process. </p>
<p> The main argument file must be a contributor map such as is read by the <code>authors read</code> subcommand of <code><a href="/docs/linux/man/1-reposurgeon/">reposurgeon</a></code>(1). It may be a fresh or stub map, produced by <code>authors write</code> before any human-name or email information has been added to the repository. Or it may have name-among-humans and email information filled in for some entries. </p>
<p> A stub map entry looks something like this: </p>
<dl>
<dt>
<dd>
<pre>
foonly = foonly &lt;foonly&gt;
</pre>
</dl>
<p> The same entry, fully filled in, might look something like this: </p>
<dl>
<dt>
<dd>
<pre>
foonly = Fred Foonly &lt;foonly [at] fubar.net&gt;
</pre>
</dl>
<p> The default behavior of the tool is to report all map entries, in effect a sorting copy of the file. </p>
<p> With -i, it reports only entries that are not yet in DVCS form &#8211; that is, either the fullname field on the right side of the equals sign is identical to the account name on the left, or the email field contains no @-sign, or both. </p>
<p> With the -p option, this tool fills in the full-name field using the password file given as the option&#8217;s argument. Only the username and the comment (or &#8216;gecos&#8217;) field containing the user&#8217;s name-among-humans are used. Other fields are ignored, including the password-hash field. (On modern Unixes this field does not contain the actual hash, which lives in a different file named /etc/shadow, so /etc/passwd can be shared without security risk.) </p>
<p> In the -p mode, for each entry in the contrib file the program looks for a username in the password file matching the name to the left of the equal sign. If a match is found, the user&#8217;s name-among-humans is extracted from the gecos field and replaces the text between the &#8220;=&#8221; and the &#8220;&lt;&#8220;. </p>
<p> Thus, the stub line above and the /etc/passwd line </p>
<dl>
<dt>
<dd>
<pre>
foonly:x:1000:1000:Fred Foonly,,,:/home/foonly:/bin/bash
</pre>
</dl>
<p> will combine to produce this on output: </p>
<dl>
<dt>
<dd>
<pre>
foonly = Fred Foonly &lt;foonly&gt;
</pre>
</dl>
<p> Note that the email-address part (and, if present, the optional trailing timezone field) are not normally modified. </p>
<p> However, if the -h option is given, the argument is taken to be a host name which should be appended (after a @) to every email field that does not already contain a @. The argument would typically be the fully-qualified domain name of the repository host. </p>
<p> Thus, if the passwd file still contains an entry for every committer (which might not be the case if inactive committer accounts were ever removed), -p mode combined with an -h option can produce an entire, valid contributor map. </p>
<p> In the -u mode of operation, the option argument must be a second contributor file, which is taken as a source of updates. Each contributor entry with a username not matching any in the first contributor map is copied into the first map, which is output. </p>
<p> Output from this tool is always a contrib map sorted by username.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-reposurgeon/">reposurgeon</a></code>(1).</p>
<h2>AUTHOR</h2>
<p> Eric S. Raymond &lt;esr [at] thyrsus.com&gt;. This tool is distributed with reposurgeon; see the project page at m[blue]<code><a rel="nofollow" href="http://www.catb.org/~esr/reposurgeon">http://www.catb.org/~esr/reposurgeon</a></code>m[]. </p>
<h2>Index</h2>
