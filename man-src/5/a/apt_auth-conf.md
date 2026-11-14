---
title: "apt_auth-conf(5)"
name: "apt_auth-conf"
section: "5"
letter: "a"
url: "/docs/linux/man/5-apt_auth-conf/"
description: "apt_auth.conf – Login configuration file for APT sources and proxies"
---

<p>apt_auth.conf &#8211; Login configuration file for APT sources and proxies</p>
<h2>Description</h2>
<p>APT configuration files like <code><a href="/docs/linux/man/5-sources-list/">sources.list</a></code>(5) or <code><a href="/docs/linux/man/5-apt-conf/">apt.conf</a></code>(5) need to be accessible for everyone using apt tools on the system to have access to all package-related information like the available packages in a repository. Login information needed to connect to a proxy or to download data from a repository on the other hand shouldn&#8217;t always be accessible by everyone and can hence not be placed in a file with world-readable file permissions. </p>
<p> The APT auth.conf file /etc/apt/auth.conf, and .conf files inside /etc/apt/auth.conf.d can be used to store login information in a netrc-like format with restrictive file permissions.</p>
<h2>Netrc-Like Format</h2>
<p>The format defined here is similar to the format of the ~/.netrc file used by <code><a href="/docs/linux/man/1-ftp/">ftp</a></code>(1) and similar programs interacting with servers. It is a simple token-based format with the following tokens being recognized; Unknown tokens will be ignored. Tokens may be separated by spaces, tabs or newlines. </p>
<p> machine <i>[protocol://]</i><i>hostname</i>[:<i>port</i>][/<i>path</i>]</p>
<dl>
<dd>Entries are looked up by searching for the <i>machine</i> token matching the hostname of the URI apt needs login information for. Extending the netrc-format a portnumber can be specified. If no port is given the token matches for all ports. Similar the path is optional and only needed and useful if multiple repositories with different login information reside on the same server. A machine token with a path matches if the path in the URI starts with the path given in the token. Once a match is made, the subsequent tokens are processed, stopping when the end of file is reached or another <i>machine</i> token is encountered. </p>
<p> If protocol is not specified, the entry only matches https and tor+https.</dl>
<p> login <i>name</i></p>
<dl>
<dd>The username to be used.</dl>
<p> password <i>string</i></p>
<dl>
<dd>The password to be used.</dl>
<h2>Example</h2>
<p>Supplying login information for a user named apt with the password debian for the <code><a href="/docs/linux/man/5-sources-list/">sources.list</a></code>(5) entry</p>
<dl>
<dd>
<pre>deb <a rel="nofollow" href="https://example.org/debian">https://example.org/debian</a> bullseye main</pre>
</dl>
<p> could be done in the entry directly:</p>
<dl>
<dd>
<pre>deb <a rel="nofollow" href="https://apt:debian@example.org/debian">https://apt:debian@example.org/debian</a> bullseye main</pre>
</dl>
<p> Alternatively an entry like the following in the auth.conf file could be used:</p>
<dl>
<dd>
<pre>machine example.org
login apt
password debian</pre>
</dl>
<p> Or alternatively within a single line:</p>
<dl>
<dd>
<pre>machine example.org login apt password debian</pre>
</dl>
<p> If you need to be more specific all of these lines will also apply to the example entry:</p>
<dl>
<dd>
<pre>machine example.org/deb login apt password debian
machine example.org/debian login apt password debian
machine example.org/debian/ login apt password debian</pre>
</dl>
<p> On the other hand neither of the following lines apply:</p>
<dl>
<dd>
<pre>machine example.org:443 login apt password debian
machine example.org/deb/ login apt password debian
machine example.org/ubuntu login apt password debian
machine example.orga login apt password debian
machine example.net login apt password debian</pre>
</dl>
<h2>Notes</h2>
<p>Basic support for this feature is present since version 0.7.25, but was undocumented for years. The documentation was added in version 1.5 changing also the implementation slightly. For maximum backward compatibility you should avoid multiple machine tokens with the same hostname, but if you need multiple they should all have a path specified in the machine token. </p>
<p> Login information in auth.conf are more flexible than those in sources.list. For example, login information can be specified for parts of a repository only, or if the sources.list entry redirects elsewhere, login information for the redirect destination can be supplied.</p>
<h2>Files</h2>
<p>/etc/apt/auth.conf</p>
<dl>
<dd>Login information for APT sources and proxies in a netrc-like format. Configuration Item: Dir::Etc::netrc.</dl>
<p> /etc/apt/auth.conf.d/*.conf</p>
<dl>
<dd>Login information for APT sources and proxies in a netrc-like format. Configuration Item: Dir::Etc::netrcparts.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-apt-conf/">apt.conf</a></code>(5) <code><a href="/docs/linux/man/5-sources-list/">sources.list</a></code>(5)</p>
<h2>Bugs</h2>
<p>m[blue]<code>APT bug page</code>m[]<font SIZE="-2">[1]</font>. If you wish to report a bug in APT, please see /usr/share/doc/debian/bug-reporting.txt or the <code><a href="/docs/linux/man/1-reportbug/">reportbug</a></code>(1) command.</p>
<h2>Author</h2>
<p><code>APT team</code></p>
<dl>
<dd></dl>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>APT bug page</p>
<dl>
<dd><a rel="nofollow" href="http://bugs.debian.org/src:apt">http://bugs.debian.org/src:apt</a></dl>
