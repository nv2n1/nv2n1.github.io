---
title: "megadl(1)"
name: "megadl"
section: "1"
letter: "m"
url: "/docs/linux/man/1-megadl/"
description: "megadl – download exported files and directories from Mega.co.nz"
---

<h2 class="name">NAME</h2>
<p> megadl &#8211; download exported files and directories from Mega.co.nz </p>
<h2>SYNOPSIS</h2>
<pre><code>
megadl[--no - progress][--path&lt;path&gt;]&lt;links&gt;... megadl-- path - &lt;filelink&gt;
</code></pre>
<h2>DESCRIPTION</h2>
<p> Downloads exported files and folders from Mega.co.nz. Handles links like: </p>
<dl>
<dt>
<dd> &bull; </p>
<p> <a rel="nofollow" href="https://mega.co.nz/#!7YVWhCzZ!bauBlAkKKvv8hIm-8-qFmGOYS289ToQWN7rGFPzXB_w">https://mega.co.nz/#!7YVWhCzZ!bauBlAkKKvv8hIm-8-qFmGOYS289ToQWN7rGFPzXB_w</a></dl>
<dl>
<dt>
<dd> &bull; </p>
<p> <a rel="nofollow" href="https://mega.co.nz/#F!HIlFDajT!HLiVvQQkSe1d0ogxZuaOJg">https://mega.co.nz/#F!HIlFDajT!HLiVvQQkSe1d0ogxZuaOJg</a></dl>
<p> When downloading individual files, these are placed into &lt;path&gt;. When downloading folders, the contents of the folder are placed into directory specified by &lt;path&gt;. </p>
<p> To export files, you can use Mega.co.nz web application, or <code><a href="/docs/linux/man/1-megals/">megals</a></code>(1)&#8217;s &#8211;export option.</p>
<h2>OPTIONS</h2>
<p> &#8211;path &lt;path&gt;</p>
<dl>
<dt>
<dd> Local directory to download to. Defaults to the current working directory. </p>
<p> If &lt;path&gt; is -, remote file will be streamed to stdout.</dl>
<p> &#8211;no-progress</p>
<dl>
<dt>
<dd> Disable download progress reporting. This is implied when streaming.</dl>
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
<p> &lt;links&gt;</p>
<dl>
<dt>
<dd> File and folder links to download from.</dl>
<p> &lt;filelink&gt;</p>
<dl>
<dt>
<dd> Link to exported file to stream.</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd> &bull; Download exported file: </p>
<dl>
<dt>
<dd>
<pre>
$ megadl '<a rel="nofollow" href="https://mega.co.nz/#!7YVWhCzZ!bauBlAkKKvv8hIm-8-qFmGOYS289ToQWN7rGFPzXB_w'">https://mega.co.nz/#!7YVWhCzZ!bauBlAkKKvv8hIm-8-qFmGOYS289ToQWN7rGFPzXB_w'</a>
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; Download exported folder: </p>
<dl>
<dt>
<dd>
<pre>
$ megadl '<a rel="nofollow" href="https://mega.co.nz/#F!HIlFDajT!HLiVvQQkSe1d0ogxZuaOJg'">https://mega.co.nz/#F!HIlFDajT!HLiVvQQkSe1d0ogxZuaOJg'</a>
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
