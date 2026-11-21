---

title: "megals(1)"
name: "megals"
section: "1"
letter: "m"
url: "/docs/linux/man/1-megals/"
description: "megals – List files stored in the cloud"
---

<p> megals &#8211; List files stored in the cloud </p>
<h2>SYNOPSIS</h2>
<pre><code>
megals[-e][-h][--header][-l][-R][-n][&lt;remotepaths&gt;...]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Lists files stored on Mega.co.nz, exports public download links.</p>
<h2>OPTIONS</h2>
<p> &#8211;export, -e</p>
<dl>
<dt>
</dt><dd> For all files that are going to be listed, also display public download link with file key. </dd>
<p> <code>NOTE</code>: Folders export doesn&#8217;t work yet.</dl>
<p> &#8211;human, -h</p>
<dl>
<dt>
</dt><dd> Display file sizes in a human readable format.</dd></dl>
<p> &#8211;header</p>
<dl>
<dt>
</dt><dd> For long list format, display header describing all listed columns.</dd></dl>
<p> &#8211;long, -l</p>
<dl>
<dt>
</dt><dd> List additional information about listed filesystem nodes. Node handle, owner, node type, file size, and the last modification date.</dd></dl>
<p> &#8211;recursive, -R</p>
<dl>
<dt>
</dt><dd> List directories recursively. This is the default if no paths are specified.</dd></dl>
<p> &#8211;names, -n</p>
<dl>
<dt>
</dt><dd> Show only names of nodes within the directory. This option has effect only if you specified a single path on a command line.</dd></dl>
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
<p> &lt;remotepaths&gt;</p>
<dl>
<dt>
</dt><dd> One or more remote filesystem paths to list. If path points to a directory, contents of the directory and the directory itself is listed. When &#8211;names is given, only the contents of the directory is listed. </dd>
<dl>
<dt>
</dt><dd>
<pre>
If path points to a file, the file itself is listed.
</pre>
</dd></dl>
<dl>
<dt>
</dt><dd>
<pre>
If ommited, the entire remote filesystem is listed recursively.
</pre>
</dd></dl>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>
</dt><dd> &bull; List all files: </dd>
<dl>
<dt>
</dt><dd>
<pre>
$ megals
/Contacts
/Inbox
/Root
/Root/README
/Root/bigfile
/Trash
</pre>
</dd></dl>
</dl>
<dl>
<dt>
</dt><dd> &bull; List all files in the /Root, recursively and with details: </dd>
<dl>
<dt>
</dt><dd>
<pre>
$ megals -l /Root
3RsS2QwJ                2             - 2013-01-22 12:31:06 /Root
2FFSiaKZ    Xz2tWWB5Dmo 0          2686 2013-04-15 08:33:47 /Root/README
udtDgR7I    Xz2tWWB5Dmo 0    4405067776 2013-04-10 19:16:02 /Root/bigfile
</pre>
</dd></dl>
</dl>
<dl>
<dt>
</dt><dd> &bull; List all files in the /Root, recursively and with details, show only file names: </dd>
<dl>
<dt>
</dt><dd>
<pre>
$ megals -ln /Root
2FFSiaKZ    Xz2tWWB5Dmo 0          2686 2013-04-15 08:33:47 README
udtDgR7I    Xz2tWWB5Dmo 0    4405067776 2013-04-10 19:16:02 bigfile
</pre>
</dd></dl>
</dl>
<dl>
<dt>
</dt><dd> &bull; Export download links: </dd>
<dl>
<dt>
</dt><dd>
<pre>
$ megals -e /Root/README
<a rel="nofollow" href="https://mega.co.nz/#!OFFRlbgR!k5rWmLp3mxB0gsq07Ii67PLd9L0wq4KondFLDlfH3Uw">https://mega.co.nz/#!OFFRlbgR!k5rWmLp3mxB0gsq07Ii67PLd9L0wq4KondFLDlfH3Uw</a> /Root/README
</pre>
</dd></dl>
</dl>
<dl>
<dt>
</dt><dd> &bull; List files in a more human readable format: </dd>
<dl>
<dt>
</dt><dd>
<pre><code>
$ megals - hnl-- header / Root / README == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
                                                                                                                                                                       Handle Owner T Size Mod.Date Filename == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
                                                                                                                                                                                                                                                                                                                                            2FFSiaKZ Xz2tWWB5Dmo 0 2.6 KiB 2013 - 04 - 15 08 : 33 : 47 README
</code></pre>
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
