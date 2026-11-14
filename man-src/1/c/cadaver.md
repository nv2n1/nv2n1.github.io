---
title: "cadaver(1)"
name: "cadaver"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cadaver/"
description: "cadaver – A command-line WebDAV client for Unix."
---

<h2>NAME</h2>
<p> cadaver &#8211; A command-line WebDAV client for Unix.</p>
<h2>SYNOPSIS</h2>
<p> cadaver [-trp[-r file][-p host[:port]]][-V][-h] <a rel="nofollow" href="http://hostname[:port]/path">http://hostname[:port]/path</a></p>
<h2>DESCRIPTION</h2>
<p> <code>cadaver </code> supports file upload, download, on-screen display, namespace operations (move and copy), collection creation and deletion, and locking operations. </p>
<p> Its operation is similar to the standard BSD <code><a href="/docs/linux/man/1-ftp/">ftp</a></code>(1) client and the Samba Project&#8217;s <code><a href="/docs/linux/man/1-smbclient/">smbclient</a></code>(1). A user familiar with these tools should be quite comfortable with cadaver. </p>
<p> <code>cadaver</code> supports automatically logging in to servers requiring authentication via a .netrc file (similar to <code><a href="/docs/linux/man/1-ftp/">ftp</a></code>(1) &#8211; see section &quot;THE .netrc FILE&quot; below).</p>
<h2>OPTIONS</h2>
<dl>
<dt>-t, &#8211;tolerant</p>
<dd> Allow cd/open into non-WebDAV enabled collection; use if the server or proxy server has WebDAV compliance problems.</p>
<dt>-r, &#8211;rcfile=file</p>
<dd> Use this rcfile rather than the default of <i>~/.cadaverrc</i></p>
<dt>-p, &#8211;proxy=host[:port]</p>
<dd> Connect using the proxy host &quot;host&quot; and optional proxy port &quot;port&quot;.</p>
<dt>-V, &#8211;version</p>
<dd> Display version information and exit.</p>
<dt>-h, &#8211;help</p>
<dd> Display this help message and exit.</dl>
<h2>COMMAND REFERENCE</h2>
<dl>
<dt>ls [path]</p>
<dd> List contents of current [or other] collection</p>
<dt>cd path</p>
<dd> Change to specified collection</p>
<dt>pwd</p>
<dd> Display name of current collection</p>
<dt>put local [remote]</p>
<dd> Upload local file</p>
<dt>get remote [local]</p>
<dd> Download remote resource</p>
<dt>mget remote&#8230;</p>
<dd> Download many remote resources</p>
<dt>mput local&#8230;</p>
<dd> Upload many local files</p>
<dt>edit resource</p>
<dd> Edit given resource</p>
<dt>less remote&#8230;</p>
<dd> Display remote resource through pager</p>
<dt>mkcol remote&#8230;</p>
<dd> Create remote collection(s)</p>
<dt>cat remote&#8230;</p>
<dd> Display remote resource(s)</p>
<dt>delete remote&#8230;</p>
<dd> Delete non-collection resource(s)</p>
<dt>rmcol remote&#8230;</p>
<dd> Delete remote collections and ALL contents</p>
<dt>copy source&#8230; dest</p>
<dd> Copy resource(s) from source to dest</p>
<dt>move source&#8230; dest</p>
<dd> Move resource(s) from source to dest</p>
<dt>lock resource</p>
<dd> Lock given resource</p>
<dt>unlock resource</p>
<dd> Unlock given resource</p>
<dt>discover resource</p>
<dd> Display lock information for resource</p>
<dt>steal resource</p>
<dd> Steal lock token for resource</p>
<dt>showlocks</p>
<dd> Display list of owned locks</p>
<dt>propnames res</p>
<dd> Names of properties defined on resource</p>
<dt>chexec [+|-] remote</p>
<dd> Change isexecutable property of resource</p>
<dt>propget res [propname]</p>
<dd> Retrieve properties of resource</p>
<dt>propset res propname value</p>
<dd> Set property on resource</p>
<dt>set [option] [value]</p>
<dd> Set an option, or display options</p>
<dt>open URL</p>
<dd> Open connection to given URL</p>
<dt>close</p>
<dd> Close current connection</p>
<dt>quit</p>
<dd> Exit program</p>
<dt>unset [option] [value]</p>
<dd> Unsets or clears value from option.</p>
<dt>lcd [directory]</p>
<dd> Change local working directory</p>
<dt>lls [options]</p>
<dd> Display local directory listing</p>
<dt>lpwd</p>
<dd> Print local working directory</p>
<dt>logout</p>
<dd> Logout of authentication session</p>
<dt>help [command]</p>
<dd> Display help message</dl>
<h2>THE .netrc FILE</h2>
<p> The file <i>~/.netrc</i> may be used to automatically login to a server requiring authentication. The following tokens (separated by spaces, tabs or newlines) may be used: </p>
<p> <code>machine</code> <i>host</i></p>
<dl>
<dt>
<dd> Identify a remote machine <i>host</i> which is compared with the hostname given on the command line or as an argument to the <code>open</code> command. Any subsequent tokens up to the end of file or the next <code>machine</code> or <code>default</code> token are associated with this entry.</dl>
<p> <code>default</code></p>
<dl>
<dt>
<dd> This is equivalent to the <code>machine</code> token but matches any hostname. Only one <code>default</code> token may be used and it must be after all <code>machine</code> tokens.</dl>
<p> <code>login</code> <i>username</i></p>
<dl>
<dt>
<dd> Specifies the username to use when logging in to the remote machine.</dl>
<p> <code>password</code> <i>string</i><br />
 <code>passwd</code> <i>string</i></p>
<dl>
<dt>
<dd> Specifies the password to use when logging in to the remote machine.</dl>
<p> Any other tokens (as described in <a href="/docs/linux/man/1-ftp/">ftp</a>(1)) are ignored.</p>
<h2>EXAMPLES</h2>
<dl>
<dt>cadaver <a rel="nofollow" href="http://dav.example.com/">http://dav.example.com/</a></p>
<dd> Connects to the server myserver.example.com, opening the root collection.</p>
<dt>cadaver <a rel="nofollow" href="http://zope.example.com:8022/Users/fred/">http://zope.example.com:8022/Users/fred/</a></p>
<dd> Connects to the server zope.example.com using port 8022, opening the collection &quot;/Users/fred/&quot;.</p>
<dt>cadaver <a rel="nofollow" href="https://secure.example.com/">https://secure.example.com/</a></p>
<dd> Connects to a server called secure.example.com using SSL.</p>
<dt>
<dd></dl>
<h2>FILES</h2>
<dl>
<dt>~/.cadaverrc</p>
<dd> Individual user settings that can override cadaver defaults and to script cadaver. Can be changed by the &quot;&#8211;rcfile&quot; option.</p>
<dt>~/.netrc</p>
<dd> Login and initialization information used by the auto-login process. See section &quot;THE .netrc FILE&quot; for details.</dl>
<h2>AUTHOR</h2>
<p> Joe Orton &lt;cadaver [at] webdav.org&gt;</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-ftp/">ftp</a>(1), <a href="/docs/linux/man/1-smbclient/">smbclient</a>(1) </p>
<h2>Index</h2>
