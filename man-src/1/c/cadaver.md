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
<dt>-t, &#8211;tolerant</dt>
<dd> Allow cd/open into non-WebDAV enabled collection; use if the server or proxy server has WebDAV compliance problems.</dd>
<dt>-r, &#8211;rcfile=file</dt>
<dd> Use this rcfile rather than the default of <i>~/.cadaverrc</i></dd>
<dt>-p, &#8211;proxy=host[:port]</dt>
<dd> Connect using the proxy host &quot;host&quot; and optional proxy port &quot;port&quot;.</dd>
<dt>-V, &#8211;version</dt>
<dd> Display version information and exit.</dd>
<dt>-h, &#8211;help</dt>
<dd> Display this help message and exit.</dd></dl>
<h2>COMMAND REFERENCE</h2>
<dl>
<dt>ls [path]</dt>
<dd> List contents of current [or other] collection</dd>
<dt>cd path</dt>
<dd> Change to specified collection</dd>
<dt>pwd</dt>
<dd> Display name of current collection</dd>
<dt>put local [remote]</dt>
<dd> Upload local file</dd>
<dt>get remote [local]</dt>
<dd> Download remote resource</dd>
<dt>mget remote&#8230;</dt>
<dd> Download many remote resources</dd>
<dt>mput local&#8230;</dt>
<dd> Upload many local files</dd>
<dt>edit resource</dt>
<dd> Edit given resource</dd>
<dt>less remote&#8230;</dt>
<dd> Display remote resource through pager</dd>
<dt>mkcol remote&#8230;</dt>
<dd> Create remote collection(s)</dd>
<dt>cat remote&#8230;</dt>
<dd> Display remote resource(s)</dd>
<dt>delete remote&#8230;</dt>
<dd> Delete non-collection resource(s)</dd>
<dt>rmcol remote&#8230;</dt>
<dd> Delete remote collections and ALL contents</dd>
<dt>copy source&#8230; dest</dt>
<dd> Copy resource(s) from source to dest</dd>
<dt>move source&#8230; dest</dt>
<dd> Move resource(s) from source to dest</dd>
<dt>lock resource</dt>
<dd> Lock given resource</dd>
<dt>unlock resource</dt>
<dd> Unlock given resource</dd>
<dt>discover resource</dt>
<dd> Display lock information for resource</dd>
<dt>steal resource</dt>
<dd> Steal lock token for resource</dd>
<dt>showlocks</dt>
<dd> Display list of owned locks</dd>
<dt>propnames res</dt>
<dd> Names of properties defined on resource</dd>
<dt>chexec [+|-] remote</dt>
<dd> Change isexecutable property of resource</dd>
<dt>propget res [propname]</dt>
<dd> Retrieve properties of resource</dd>
<dt>propset res propname value</dt>
<dd> Set property on resource</dd>
<dt>set [option] [value]</dt>
<dd> Set an option, or display options</dd>
<dt>open URL</dt>
<dd> Open connection to given URL</dd>
<dt>close</dt>
<dd> Close current connection</dd>
<dt>quit</dt>
<dd> Exit program</dd>
<dt>unset [option] [value]</dt>
<dd> Unsets or clears value from option.</dd>
<dt>lcd [directory]</dt>
<dd> Change local working directory</dd>
<dt>lls [options]</dt>
<dd> Display local directory listing</dd>
<dt>lpwd</dt>
<dd> Print local working directory</dd>
<dt>logout</dt>
<dd> Logout of authentication session</dd>
<dt>help [command]</dt>
<dd> Display help message</dd></dl>
<h2>THE .netrc FILE</h2>
<p> The file <i>~/.netrc</i> may be used to automatically login to a server requiring authentication. The following tokens (separated by spaces, tabs or newlines) may be used: </p>
<p> <code>machine</code> <i>host</i></p>
<dl>
<dt>
</dt><dd> Identify a remote machine <i>host</i> which is compared with the hostname given on the command line or as an argument to the <code>open</code> command. Any subsequent tokens up to the end of file or the next <code>machine</code> or <code>default</code> token are associated with this entry.</dd></dl>
<p> <code>default</code></p>
<dl>
<dt>
</dt><dd> This is equivalent to the <code>machine</code> token but matches any hostname. Only one <code>default</code> token may be used and it must be after all <code>machine</code> tokens.</dd></dl>
<p> <code>login</code> <i>username</i></p>
<dl>
<dt>
</dt><dd> Specifies the username to use when logging in to the remote machine.</dd></dl>
<p> <code>password</code> <i>string</i><br />
 <code>passwd</code> <i>string</i></p>
<dl>
<dt>
</dt><dd> Specifies the password to use when logging in to the remote machine.</dd></dl>
<p> Any other tokens (as described in <a href="/docs/linux/man/1-ftp/">ftp</a>(1)) are ignored.</p>
<h2>EXAMPLES</h2>
<dl>
<dt>cadaver <a rel="nofollow" href="http://dav.example.com/">http://dav.example.com/</a></dt>
<dd> Connects to the server myserver.example.com, opening the root collection.</dd>
<dt>cadaver <a rel="nofollow" href="http://zope.example.com:8022/Users/fred/">http://zope.example.com:8022/Users/fred/</a></dt>
<dd> Connects to the server zope.example.com using port 8022, opening the collection &quot;/Users/fred/&quot;.</dd>
<dt>cadaver <a rel="nofollow" href="https://secure.example.com/">https://secure.example.com/</a></dt>
<dd> Connects to a server called secure.example.com using SSL.</dd>
</dl>
<h2>FILES</h2>
<dl>
<dt>~/.cadaverrc</dt>
<dd> Individual user settings that can override cadaver defaults and to script cadaver. Can be changed by the &quot;&#8211;rcfile&quot; option.</dd>
<dt>~/.netrc</dt>
<dd> Login and initialization information used by the auto-login process. See section &quot;THE .netrc FILE&quot; for details.</dd></dl>
<h2>AUTHOR</h2>
<p> Joe Orton &lt;cadaver [at] webdav.org&gt;</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-ftp/">ftp</a>(1), <a href="/docs/linux/man/1-smbclient/">smbclient</a>(1) </p>
