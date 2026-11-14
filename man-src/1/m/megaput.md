---
title: "megaput(1)"
name: "megaput"
section: "1"
letter: "m"
url: "/docs/linux/man/1-megaput/"
description: "megaput – upload files to your Mega.co.nz account"
---

<h2 class="name">NAME</h2>
<p> megaput &#8211; upload files to your Mega.co.nz account </p>
<h2>SYNOPSIS</h2>
<pre><code>
megaput[--no - progress][--path&lt;remotepath&gt;]&lt;paths&gt;...
</code></pre>
<h2>DESCRIPTION</h2>
<p> Uploads files to your Mega.co.nz account. </p>
<p> <code>NOTE</code>: If you want to upload entire directories, use <code><a href="/docs/linux/man/1-megasync/">megasync</a></code>(1).</p>
<h2>OPTIONS</h2>
<p> &#8211;path &lt;remotepath&gt;</p>
<dl>
<dt>
<dd> Remote path to upload to. If this path is a directory, files are placed into the directory. If this path doesn&#8217;t exist, and it&#8217;s parent directory does, the file will be uploaded to a specified path (this only works if you specify exactly one file).</dl>
<p> &#8211;no-progress</p>
<dl>
<dt>
<dd> Disable upload progress reporting.</dl>
<p> -u &lt;email&gt;, &#8211;username &lt;email&gt;</p>
<dl>
<dt>
<dd> Account username (email)</dl>
<p> -p &lt;password&gt;, &#8211;password &lt;password&gt;</p>
<dl>
<dt>
<dd> Account password</dl>
<p> &#8211;config &lt;path&gt;</p>
<dl>
<dt>
<dd> Load configuration from a file</dl>
<p> &#8211;ignore-config-file</p>
<dl>
<dt>
<dd> Disable loading .megarc</dl>
<p> &#8211;no-ask-password</p>
<dl>
<dt>
<dd> Never ask interactively for a password</dl>
<p> &#8211;reload</p>
<dl>
<dt>
<dd> Reload filesystem cache</dl>
<p> &#8211;debug [&lt;options&gt;]</p>
<dl>
<dt>
<dd> Enable debugging of various aspects of the megatools operation. You may enable multiple debugging options separated by commas. (eg. &#8211;debug api,fs) </p>
<p> Available options are: </p>
<dl>
<dt>
<dd> &bull; </p>
<p> api: Dump Mega.co.nz API calls</dl>
<dl>
<dt>
<dd> &bull; </p>
<p> fs: Dump Mega.co.nz filesystem (may require &#8211;reload to actually print something)</dl>
<dl>
<dt>
<dd> &bull; </p>
<p> cache: Dump cache contents</dl>
</dl>
<p> &#8211;version</p>
<dl>
<dt>
<dd> Show version information</dl>
<p> &lt;paths&gt;</p>
<dl>
<dt>
<dd> One or more local files to upload.</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd> &bull; Upload file to the /Root: </p>
<dl>
<dt>
<dd>
<pre>
$ megaput README
$ megals /Root
/Root
/Root/README
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; Upload file, while naming it differently: </p>
<dl>
<dt>
<dd>
<pre>
$ megaput --path /Root/README.TXT README
$ megals /Root
/Root
/Root/README.TXT
</pre>
</dl>
</dl>
<h2>REMOTE FILESYSTEM</h2>
<p> Mega.co.nz filesystem is represented as a tree of nodes of various types. Nodes are identified by a 8 character node handles (eg. 7Fdi3ZjC). Structure of the filesystem is not encrypted. </p>
<p> Megatools maps node tree structure to a traditional filesystem paths (eg. /Root/SomeFile.DAT). </p>
<p> <code>NOTE</code>: By the nature of Mega.co.nz storage, several files in the directory can have the same name. To allow access to such files, the names of conflicting files are extended by appending dot and their node handle like this: </p>
<dl>
<dt>
<dd>
<pre>
/Root/conflictingfile
/Root/conflictingfile.7Fdi3ZjC
/Root/conflictingfile.mEU23aSD
</pre>
</dl>
<p> You need to be aware of several special folders: </p>
<p> /Root</p>
<dl>
<dt>
<dd> Writable directory representing the root of the filesystem.</dl>
<p> /Trash</p>
<dl>
<dt>
<dd> Trash directory where Mega.co.nz web client moves deleted files. This directory is not used by megatools when removing files.</dl>
<p> /Inbox</p>
<dl>
<dt>
<dd> Not sure.</dl>
<p> /Contacts</p>
<dl>
<dt>
<dd> Directory containing subdirectories representing your contacts list. If you want to add contacts to the list, simply create subdirectory named after the contact you want to add.</dl>
<p> /Contacts/&lt;email&gt;</p>
<dl>
<dt>
<dd> Directories representing individual contacts in your contacts list. These directories contain folders that others shared with you. All shared files are read-only, at the moment.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-megatools/">megatools</a></code>(7), <code><a href="/docs/linux/man/5-megarc/">megarc</a></code>(5), <code><a href="/docs/linux/man/1-megadf/">megadf</a></code>(1), <code><a href="/docs/linux/man/1-megadl/">megadl</a></code>(1), <code><a href="/docs/linux/man/1-megaget/">megaget</a></code>(1), <code><a href="/docs/linux/man/1-megals/">megals</a></code>(1), <code><a href="/docs/linux/man/1-megamkdir/">megamkdir</a></code>(1), <code><a href="/docs/linux/man/1-megaput/">megaput</a></code>(1), <code><a href="/docs/linux/man/1-megareg/">megareg</a></code>(1), <code><a href="/docs/linux/man/1-megarm/">megarm</a></code>(1), <code><a href="/docs/linux/man/1-megamv/">megamv</a></code>(1), <code><a href="/docs/linux/man/1-megasync/">megasync</a></code>(1), <code><a href="/docs/linux/man/1-megafs/">megafs</a></code>(1).</p>
<h2>MEGATOOLS</h2>
<p> Part of the <code><a href="/docs/linux/man/7-megatools/">megatools</a></code>(7) suite.</p>
<h2>BUGS</h2>
<p> Report bugs at <a rel="nofollow" href="https://github.com/megous/megatools">https://github.com/megous/megatools</a> or megous [at] megous.com.</p>
<h2>AUTHOR</h2>
<p> Megatools was written by Ondrej Jirman &lt;megous [at] megous.com&gt;, 2013. </p>
<p> Official website is <a rel="nofollow" href="http://megatools.megous.com.">http://megatools.megous.com.</a> </p>
<h2>Index</h2>
