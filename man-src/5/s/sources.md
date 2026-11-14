---
title: "sources(5)"
name: "sources"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sources/"
description: "sources.list – List of configured APT data sources"
---

<p>sources.list &#8211; List of configured APT data sources</p>
<h2>Description</h2>
<p>The source list /etc/apt/sources.list is designed to support any number of active sources and a variety of source media. The file lists one source per line, with the most preferred source listed first. The information available from the configured sources is acquired by <code>apt-get update</code> (or by an equivalent command from another APT front-end). </p>
<p> Each line specifying a source starts with type (e.g. deb-src) followed by options and arguments for this type. Individual entries cannot be continued onto a following line. Empty lines are ignored, and a # character anywhere on a line marks the remainder of that line as a comment.</p>
<h2>Sources.List.D</h2>
<p>The /etc/apt/sources.list.d directory provides a way to add sources.list entries in separate files. The format is the same as for the regular sources.list file. File names need to end with .list and may only contain letters (a-z and A-Z), digits (0-9), underscore (_), hyphen (-) and period (.) characters. Otherwise APT will print a notice that it has ignored a file, unless that file matches a pattern in the Dir::Ignore-Files-Silently configuration list &#8211; in which case it will be silently ignored.</p>
<h2>The Deb And Deb-Src Types</h2>
<p>The deb type references a typical two-level Debian archive, distribution/component. The distribution is generally an archive name like stable or testing or a codename like wheezy or jessie while component is one of main, contrib or non-free. The deb-src type references a Debian distribution&#8217;s source code in the same form as the deb type. A deb-src line is required to fetch source indexes. </p>
<p> The format for a sources.list entry using the deb and deb-src types is: </p>
<dl>
<dd>
<pre>deb [ options ] uri suite [component1] [component2] [...]</pre>
</dl>
<p> Alternatively a rfc822 style format is also supported: </p>
<dl>
<dd>
<pre> Types: deb deb-src
 URIs: <a rel="nofollow" href="http://example.com">http://example.com</a>
 Suites: stable testing
 Sections: component1 component2
 Description: short
 long long long
 [option1]: [option1-value]
 Types: deb
 URIs: <a rel="nofollow" href="http://another.example.com">http://another.example.com</a>
 Suites: experimental
 Sections: component1 component2
 Enabled: no
 Description: short
 long long long
 [option1]: [option1-value]</pre>
</dl>
<p> The URI for the deb type must specify the base of the Debian distribution, from which APT will find the information it needs. suite can specify an exact path, in which case the components must be omitted and suite must end with a slash (/). This is useful for the case when only a particular sub-section of the archive denoted by the URI is of interest. If suite does not specify an exact path, at least one component must be present. </p>
<p> suite may also contain a variable, $(ARCH) which expands to the Debian architecture (such as amd64 or armel) used on the system. This permits architecture-independent sources.list files to be used. In general this is only of interest when specifying an exact path, APT will automatically generate a URI with the current architecture otherwise. </p>
<p> In the traditional style sources.list format since only one distribution can be specified per line it may be necessary to have multiple lines for the same URI, if a subset of all available distributions or components at that location is desired. APT will sort the URI list after it has generated a complete set internally, and will collapse multiple references to the same Internet host, for instance, into a single connection, so that it does not inefficiently establish an FTP connection, close it, do something else, and then re-establish a connection to that same host. This feature is useful for accessing busy FTP sites with limits on the number of simultaneous anonymous users. APT also parallelizes connections to different hosts to more effectively deal with sites with low bandwidth. </p>
<p> options is always optional and needs to be surrounded by square brackets. It can consist of multiple settings in the form <i>setting</i>=<i>value</i>. Multiple settings are separated by spaces. The following settings are supported by APT (note however that unsupported settings will be ignored silently): </p>
<dl>
<dd>&bull; arch=<i>arch1</i>,<i>arch2</i>,&#8230; can be used to specify for which architectures information should be downloaded. If this option is not set all architectures defined by the APT::Architectures option will be downloaded.</dl>
<dl>
<dd>&bull; arch+=<i>arch1</i>,<i>arch2</i>,&#8230; and arch-=<i>arch1</i>,<i>arch2</i>,&#8230; which can be used to add/remove architectures from the set which will be downloaded.</dl>
<dl>
<dd>&bull; trusted=yes can be set to indicate that packages from this source are always authenticated even if the Release file is not signed or the signature can&#8217;t be checked. This disables parts of <code><a href="/docs/linux/man/8-apt-secure/">apt-secure</a></code>(8) and should therefore only be used in a local and trusted context. trusted=no is the opposite which handles even correctly authenticated sources as not authenticated.</dl>
<p> It is important to list sources in order of preference, with the most preferred source listed first. Typically this will result in sorting by speed from fastest to slowest (CD-ROM followed by hosts on a local network, followed by distant Internet hosts, for example). </p>
<p> Some examples: </p>
<dl>
<dd>
<pre>deb <a rel="nofollow" href="http://ftp.debian.org/debian">http://ftp.debian.org/debian</a> wheezy main contrib non-free
deb <a rel="nofollow" href="http://security.debian.org/">http://security.debian.org/</a> wheezy/updates main contrib non-free</pre>
</dl>
<h2>Uri Specification</h2>
<p>The currently recognized URI types are: </p>
<p> <code>file</code></p>
<dl>
<dd>The file scheme allows an arbitrary directory in the file system to be considered an archive. This is useful for NFS mounts and local mirrors or archives.</dl>
<p> <code>cdrom</code></p>
<dl>
<dd>The cdrom scheme allows APT to use a local CD-ROM drive with media swapping. Use the <code><a href="/docs/linux/man/8-apt-cdrom/">apt-cdrom</a></code>(8) program to create cdrom entries in the source list.</dl>
<p> <code>http</code></p>
<dl>
<dd>The http scheme specifies an HTTP server for the archive. If an environment variable <code>http_proxy</code> is set with the format <a rel="nofollow" href="http://server:port/,">http://server:port/,</a> the proxy server specified in <code>http_proxy</code> will be used. Users of authenticated HTTP/1.1 proxies may use a string of the format <a rel="nofollow" href="http://user:pass@server:port/.">http://user:pass@server:port/.</a> Note that this is an insecure method of authentication.</dl>
<p> <code>ftp</code></p>
<dl>
<dd>The ftp scheme specifies an FTP server for the archive. APT&#8217;s FTP behavior is highly configurable; for more information see the <code><a href="/docs/linux/man/5-apt-conf/">apt.conf</a></code>(5) manual page. Please note that an FTP proxy can be specified by using the <code>ftp_proxy</code> environment variable. It is possible to specify an HTTP proxy (HTTP proxy servers often understand FTP URLs) using this environment variable and <i>only</i> this environment variable. Proxies using HTTP specified in the configuration file will be ignored.</dl>
<p> <code>copy</code></p>
<dl>
<dd>The copy scheme is identical to the file scheme except that packages are copied into the cache directory instead of used directly at their location. This is useful for people using removable media to copy files around with APT.</dl>
<p> <code>rsh</code>, <code>ssh</code></p>
<dl>
<dd>The rsh/ssh method invokes RSH/SSH to connect to a remote host and access the files as a given user. Prior configuration of rhosts or RSA keys is recommended. The standard <code>find</code> and <code>dd</code> commands are used to perform the file transfers from the remote host.</dl>
<p> adding more recognizable URI types</p>
<dl>
<dd>APT can be extended with more methods shipped in other optional packages, which should follow the naming scheme apt-transport-<i>method</i>. For instance, the APT team also maintains the package apt-transport-https, which provides access methods for HTTPS URIs with features similar to the http method. Methods for using e.g. debtorrent are also available &#8211; see <code><a href="/docs/linux/man/1-apt-transport-debtorrent/">apt-transport-debtorrent</a></code>(1).</dl>
<h2>Examples</h2>
<p>Uses the archive stored locally (or NFS mounted) at /home/jason/debian for stable/main, stable/contrib, and stable/non-free.</p>
<dl>
<dd>
<pre>deb file:/home/jason/debian stable main contrib non-free</pre>
</dl>
<p> As above, except this uses the unstable (development) distribution.</p>
<dl>
<dd>
<pre>deb file:/home/jason/debian unstable main contrib non-free</pre>
</dl>
<p> Source line for the above</p>
<dl>
<dd>
<pre>deb-src file:/home/jason/debian unstable main contrib non-free</pre>
</dl>
<p> The first line gets package information for the architectures in APT::Architectures while the second always retrieves amd64 and armel.</p>
<dl>
<dd>
<pre>deb <a rel="nofollow" href="http://ftp.debian.org/debian">http://ftp.debian.org/debian</a> wheezy main
deb [ arch=amd64,armel ] <a rel="nofollow" href="http://ftp.debian.org/debian">http://ftp.debian.org/debian</a> wheezy main</pre>
</dl>
<p> Uses HTTP to access the archive at archive.debian.org, and uses only the hamm/main area.</p>
<dl>
<dd>
<pre>deb <a rel="nofollow" href="http://archive.debian.org/debian-archive">http://archive.debian.org/debian-archive</a> hamm main</pre>
</dl>
<p> Uses FTP to access the archive at <a href="ftp://ftp.debian.org">ftp.debian.org</a>, under the debian directory, and uses only the wheezy/contrib area.</p>
<dl>
<dd>
<pre>deb <a href="ftp://ftp.debian.org/debian">ftp://ftp.debian.org/debian</a> wheezy contrib</pre>
</dl>
<p> Uses FTP to access the archive at <a href="ftp://ftp.debian.org">ftp.debian.org</a>, under the debian directory, and uses only the unstable/contrib area. If this line appears as well as the one in the previous example in sources.list a single FTP session will be used for both resource lines.</p>
<dl>
<dd>
<pre>deb <a href="ftp://ftp.debian.org/debian">ftp://ftp.debian.org/debian</a> unstable contrib</pre>
</dl>
<p> Uses HTTP to access the archive at <a href="ftp://ftp.tlh.debian.org">ftp.tlh.debian.org</a>, under the universe directory, and uses only files found under unstable/binary-i386 on i386 machines, unstable/binary-amd64 on amd64, and so forth for other supported architectures. [Note this example only illustrates how to use the substitution variable; official debian archives are not structured like this]</p>
<dl>
<dd>
<pre>deb <a rel="nofollow" href="http://ftp.tlh.debian.org/universe">http://ftp.tlh.debian.org/universe</a> unstable/binary-$(ARCH)/</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-apt-cache/">apt-cache</a></code>(8)<code><a href="/docs/linux/man/5-apt-conf/">apt.conf</a></code>(5)</p>
<h2>Bugs</h2>
<p>m[blue]<code>APT bug page</code>m[]<font SIZE="-2">[1]</font>. If you wish to report a bug in APT, please see /usr/share/doc/debian/bug-reporting.txt or the <code><a href="/docs/linux/man/1-reportbug/">reportbug</a></code>(1) command.</p>
<h2>Authors</h2>
<p><code>Jason Gunthorpe</code></p>
<dl>
<dd></dl>
<p> <code>APT team</code></p>
<dl>
<dd></dl>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>APT bug page</p>
<dl>
<dd><a rel="nofollow" href="http://bugs.debian.org/src:apt">http://bugs.debian.org/src:apt</a></dl>
