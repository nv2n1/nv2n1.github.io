---
title: "apt-transport-mirror(1)"
name: "apt-transport-mirror"
section: "1"
letter: "a"
url: "/docs/linux/man/1-apt-transport-mirror/"
description: "apt-transport-mirror – APT transport for more automated mirror selection"
---

<h2 class="name">NAME</h2>
<p> apt-transport-mirror &#8211; APT transport for more automated mirror selection </p>
<h2>DESCRIPTION</h2>
<p> This APT transport isn&#8217;t implementing a protocol to access local or remote repositories on its own, but acquires a mirrorlist and redirects all requests to the mirror(s) picked from this list, accessing them via other transports like <code><a href="/docs/linux/man/1-apt-transport-http/">apt-transport-http</a></code>(1). The basic functionality has been available since apt 0.7.24, but was undocumented until apt 1.6 which contained a complete rework of the transport and its supported features. Note that a transport is never called directly by a user but used by APT tools based on user configuration. </p>
<p> If the acquisition of a file via a mirror fails, the method ensures that another possible mirror from the list is automatically tried until either the file is retrieved or no mirror is left in the list, transparently handling server downtimes and similar problems. </p>
<p> The security implications of the transport depend on the security considerations associated with the transport used to acquire the mirrorlist and the transports involved in accessing the chosen mirror(s) by the transport.</p>
<h2>OPTIONS</h2>
<p> This transport has no configuration options at present. The mirror selection is based entirely on the mirrors offered in the mirrorlist and the files APT needs to acquire.</p>
<h3>Mirrorlist format</h3>
<p> A mirrorlist contains one or more lines each specifying a URI for a mirror. Empty lines and those starting with a hash character (#) are ignored. A URI always starts with a URI scheme which defines the transport used for this mirror. If for example the URI starts with http:, the responsible transport is <code><a href="/docs/linux/man/1-apt-transport-http/">apt-transport-http</a></code>(1) which might have specific requirements for the format of the remaining part of the URI. </p>
<p> Metadata about a mirror can be given on the same line, separated from the URI by a tab. Multiple items of metadata can themselves be separated by either tabs or spaces. (This is an advanced feature only available with apt &gt;= 1.6. Earlier apt versions will fail to parse mirrorlists using this feature.) </p>
<p> Since apt 1.6 the use of compressed mirrorlists is also supported. Note that the filename of the mirrorlist must specify the compression algorithm used; there is no auto-detection based on file contents.</p>
<h3>Mirror selection by metadata</h3>
<p> As specified in the format, a mirror can have additional metadata attached to prevent a mirror from being selected for acquiring a file not matching this metadata. This way the mirrorlist can e.g. contain partial mirrors serving only certain architectures and APT will automatically choose a different mirror for files requiring an unlisted architecture. Supported are limits for the architecture (arch), codename of the release (codename), component of the repository the file is in (component), language the file applies to (lang), suite name of the release (suite) and type of the file (type).</p>
<h3>Fallback order for mirrors</h3>
<p> If no priority is given for a mirror via the metadata key priority, the order in which mirrors are contacted is random. If a certain set of mirrors should be tried first before any of another set is tried, a priority can be explicitly set. The mirrors with the lowest number are tried first. Mirrors which have no explicit priority set default to the highest possible number and are therefore tried last. The choice between mirrors with the same priority is again random.</p>
<h3>Allowed transports in a mirrorlist</h3>
<p> The availability and choice of transports in a mirrorlist is limited by how the APT client is accessing the mirrorlist. If a local transport like file or copy is used, the mirrorlist can also include local sources, while a mirrorlist accessed via http can not. Additionally, a mirrorlist can not contain a mirrorlist or other wrapping transports (like apt-transport-tor). See the documentation of these transports on how to use them with the mirror method. </p>
<p> Note that apt versions before 1.6 do not support any other transport than http.</p>
<h2>EXAMPLES</h2>
<h3>Basic example</h3>
<p> A basic mirrorlist example supported by all apt versions with a mirror method (&gt;= 0.7.24) in which the client will pick any of the three mirrors: </p>
<dl>
<dt>
<dd>
<pre>
<a rel="nofollow" href="http://ftp.de.debian.org/debian/">http://ftp.de.debian.org/debian/</a>
<a rel="nofollow" href="http://ftp.us.debian.org/debian/">http://ftp.us.debian.org/debian/</a>
<a rel="nofollow" href="http://deb.debian.org/debian/">http://deb.debian.org/debian/</a>
</pre>
</dl>
<p> Assuming a file with this content is stored as /etc/apt/mirrorlist.txt on your machine it can be used like this in <code><a href="/docs/linux/man/5-sources-list/">sources.list</a></code>(5) (since apt 1.6): </p>
<dl>
<dt>
<dd>
<pre>
deb mirror+file:/etc/apt/mirrorlist.txt bullseye main
</pre>
</dl>
<p> All versions of the mirror method support a mirrorlist accessible via HTTP, so assuming it is available at <a rel="nofollow" href="http://apt.example.org/mirror.lst">http://apt.example.org/mirror.lst</a> the sources.list entry from above could instead be written as: </p>
<dl>
<dt>
<dd>
<pre>
deb <a href="mirror://apt.example.org/mirror.lst">mirror://apt.example.org/mirror.lst</a> bullseye main
</pre>
</dl>
<p> Note that since apt 1.6 the use of mirror+http should be preferred over mirror for uniformity. The functionality is the same.</p>
<h3>Example with metadata-enhanced mirror selection</h3>
<p> As explained in the format definition apt versions before 1.6 do not support this and will fail parsing the mirrorlist. The example mirrorlist is intentionally complicated to show some aspects of the selection. The following setup is assumed: The first mirror is a local mirror accessible via the file method, but potentially incomplete. The second mirror has a great connection, but is a partial mirror insofar as it only contains files related to the architectures amd64 and all. The remaining mirrors are average mirrors which should be contacted only if the earlier ones didn&#8217;t work. </p>
<dl>
<dt>
<dd>
<pre>
file:/srv/local/debian/mirror/  priority:1 type:index
<a rel="nofollow" href="http://partial.example.org/mirror/">http://partial.example.org/mirror/</a>      priority:2 arch:amd64 arch:all type:deb
<a rel="nofollow" href="http://ftp.us.debian.org/debian/">http://ftp.us.debian.org/debian/</a>        type:deb
<a rel="nofollow" href="http://ftp.de.debian.org/debian/">http://ftp.de.debian.org/debian/</a>        type:deb
<a rel="nofollow" href="https://deb.debian.org/debian/">https://deb.debian.org/debian/</a>
</pre>
</dl>
<p> In this setup with this mirrorlist the first mirror will be used to download all index files assuming the mirrorlist itself is accessed via a local transport like file. If it isn&#8217;t, if the mirror is otherwise inaccessible or if it does not contain the requested file another mirror will be used to acquire the file, chosen depending on the type of the file: An index file will be served by the last mirror in the list, while a package of architecture amd64 is served by the second and those of e.g. architecture i386 by one of the last three.</p>
<h2>BUGS</h2>
<p> m[blue]<code>APT bug page</code>m[]<font SIZE="-2">[1]</font>. If you wish to report a bug in APT, please see /usr/share/doc/debian/bug-reporting.txt or the <code><a href="/docs/linux/man/1-reportbug/">reportbug</a></code>(1) command.</p>
<h2>AUTHOR</h2>
<p> <code>APT team</code></p>
<dl>
<dt>
<dd></dl>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> APT bug page</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://bugs.debian.org/src:apt">http://bugs.debian.org/src:apt</a></dl>
</dl>
<h2>Index</h2>
