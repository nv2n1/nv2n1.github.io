---
title: "megasync(1)"
name: "megasync"
section: "1"
letter: "m"
url: "/docs/linux/man/1-megasync/"
description: "megasync – Upload/download entire directories to/from your Mega.co.nz account"
---

<h2>SYNOPSIS</h2>
<pre><code>
megasync[-n][--no - progress]-- local&lt;path&gt; --remote&lt;remotepath&gt;
    megasync[-n][--no - progress]-- download-- local&lt;path&gt; --remote&lt;remotepath&gt;
</code></pre>
<h2>DESCRIPTION</h2>
<p> Sync remote and local directories. No files are ever overwritten or removed. </p>
<p> Default direction is to upload files to the cloud. If you want to download files, you have to add &#8211;download option.</p>
<h2>OPTIONS</h2>
<p> -r &lt;remotepath&gt;, &#8211;remote &lt;remotepath&gt;</p>
<dl>
<dt>
</dt><dd> Remote directory path.</dd></dl>
<p> -l &lt;path&gt;, &#8211;local &lt;path&gt;</p>
<dl>
<dt>
</dt><dd> Local directory path.</dd></dl>
<p> -d, &#8211;download</p>
<dl>
<dt>
</dt><dd> Download files from the Mega.co.nz. The default is to upload.</dd></dl>
<p> -n, &#8211;dryrun</p>
<dl>
<dt>
</dt><dd> Don&#8217;t perform any actual changes, just print what would be done.</dd></dl>
<p> &#8211;no-progress</p>
<dl>
<dt>
</dt><dd> Disable upload progress reporting.</dd></dl>
<p> -u &lt;email&gt;, &#8211;username &lt;email&gt;</p>
<dl>
<dt>
</dt><dd> Account username (email)</dd></dl>
<p> -p &lt;password&gt;, &#8211;password &lt;password&gt;</p>
<dl>
<dt>
</dt><dd> Account password</dd></dl>
<p> &#8211;config &lt;path&gt;</p>
<dl>
<dt>
</dt><dd> Load configuration from a file</dd></dl>
<p> &#8211;ignore-config-file</p>
<dl>
<dt>
</dt><dd> Disable loading .megarc</dd></dl>
<p> &#8211;no-ask-password</p>
<dl>
<dt>
</dt><dd> Never ask interactively for a password</dd></dl>
<p> &#8211;reload</p>
<dl>
<dt>
</dt><dd> Reload filesystem cache</dd></dl>
<p> &#8211;debug [&lt;options&gt;]</p>
<dl>
<dt>
</dt><dd> Enable debugging of various aspects of the megatools operation. You may enable multiple debugging options separated by commas. (eg. &#8211;debug api,fs) </dd>
<p> Available options are: </p>
<dl>
<dt>
</dt><dd> &bull; </dd>
<p> api: Dump Mega.co.nz API calls</dl>
<dl>
<dt>
</dt><dd> &bull; </dd>
<p> fs: Dump Mega.co.nz filesystem (may require &#8211;reload to actually print something)</dl>
<dl>
<dt>
</dt><dd> &bull; </dd>
<p> cache: Dump cache contents</dl>
</dl>
<p> &#8211;version</p>
<dl>
<dt>
</dt><dd> Show version information</dd></dl>
<h2>EXAMPLES</h2>
<dl>
<dt>
</dt><dd> &bull; Upload directory. </dd>
<dl>
<dt>
</dt><dd>
<pre>
$ megasync --local MyBackups --remote /Root/Backups
</pre>
</dd></dl>
</dl>
<dl>
<dt>
</dt><dd> &bull; Download directory. </dd>
<dl>
<dt>
</dt><dd>
<pre>
$ megasync --local MyBackups --remote /Root/Backups --download
</pre>
</dd></dl>
</dl>
<h2>REMOTE FILESYSTEM</h2>
<p> Mega.co.nz filesystem is represented as a tree of nodes of various types. Nodes are identified by a 8 character node handles (eg. 7Fdi3ZjC). Structure of the filesystem is not encrypted. </p>
<p> Megatools maps node tree structure to a traditional filesystem paths (eg. /Root/SomeFile.DAT). </p>
<p> <code>NOTE</code>: By the nature of Mega.co.nz storage, several files in the directory can have the same name. To allow access to such files, the names of conflicting files are extended by appending dot and their node handle like this: </p>
<dl>
<dt>
</dt><dd>
<pre>
/Root/conflictingfile
/Root/conflictingfile.7Fdi3ZjC
/Root/conflictingfile.mEU23aSD
</pre>
</dd></dl>
<p> You need to be aware of several special folders: </p>
<p> /Root</p>
<dl>
<dt>
</dt><dd> Writable directory representing the root of the filesystem.</dd></dl>
<p> /Trash</p>
<dl>
<dt>
</dt><dd> Trash directory where Mega.co.nz web client moves deleted files. This directory is not used by megatools when removing files.</dd></dl>
<p> /Inbox</p>
<dl>
<dt>
</dt><dd> Not sure.</dd></dl>
<p> /Contacts</p>
<dl>
<dt>
</dt><dd> Directory containing subdirectories representing your contacts list. If you want to add contacts to the list, simply create subdirectory named after the contact you want to add.</dd></dl>
<p> /Contacts/&lt;email&gt;</p>
<dl>
<dt>
</dt><dd> Directories representing individual contacts in your contacts list. These directories contain folders that others shared with you. All shared files are read-only, at the moment.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-megatools/">megatools</a></code>(7), <code><a href="/docs/linux/man/5-megarc/">megarc</a></code>(5), <code><a href="/docs/linux/man/1-megadf/">megadf</a></code>(1), <code><a href="/docs/linux/man/1-megadl/">megadl</a></code>(1), <code><a href="/docs/linux/man/1-megaget/">megaget</a></code>(1), <code><a href="/docs/linux/man/1-megals/">megals</a></code>(1), <code><a href="/docs/linux/man/1-megamkdir/">megamkdir</a></code>(1), <code><a href="/docs/linux/man/1-megaput/">megaput</a></code>(1), <code><a href="/docs/linux/man/1-megareg/">megareg</a></code>(1), <code><a href="/docs/linux/man/1-megarm/">megarm</a></code>(1), <code><a href="/docs/linux/man/1-megamv/">megamv</a></code>(1), <code><a href="/docs/linux/man/1-megasync/">megasync</a></code>(1), <code><a href="/docs/linux/man/1-megafs/">megafs</a></code>(1).</p>
<h2>MEGATOOLS</h2>
<p> Part of the <code><a href="/docs/linux/man/7-megatools/">megatools</a></code>(7) suite.</p>
<h2>BUGS</h2>
<p> Report bugs at <a rel="nofollow" href="https://github.com/megous/megatools">https://github.com/megous/megatools</a> or megous [at] megous.com.</p>
<h2>AUTHOR</h2>
<p> Megatools was written by Ondrej Jirman &lt;megous [at] megous.com&gt;, 2013. </p>
<p> Official website is <a rel="nofollow" href="http://megatools.megous.com.">http://megatools.megous.com.</a> </p>
