---
title: "megamkdir(1)"
name: "megamkdir"
section: "1"
letter: "m"
url: "/docs/linux/man/1-megamkdir/"
---

<h2 class="name">NAME</h2>
 

 megamkdir - Create remote folder under your Mega.co.nz account 

<h2>SYNOPSIS</h2>

 

 <pre>
<i>megamkdir</i> &lt;remotepaths&gt;...
<i>megamkdir</i> /Contacts/&lt;contactemail&gt;
</pre>

<h2>DESCRIPTION</h2>

 

 Creates folders on Mega.co.nz. 

 As a special case, by creating a new folder under /Contacts, you're adding a &lt;contactemail&gt; to your contacts list.

<h2>OPTIONS</h2>

 

 -u &lt;email&gt;, --username &lt;email&gt;
<dl>
<dt>
<dd> Account username (email)</dl>
 

 -p &lt;password&gt;, --password &lt;password&gt;
<dl>
<dt>
<dd> Account password</dl>
 

 --config &lt;path&gt;
<dl>
<dt>
<dd> Load configuration from a file</dl>
 

 --ignore-config-file
<dl>
<dt>
<dd> Disable loading .megarc</dl>
 

 --no-ask-password
<dl>
<dt>
<dd> Never ask interactively for a password</dl>
 

 --reload
<dl>
<dt>
<dd> Reload filesystem cache</dl>
 

 --debug [&lt;options&gt;]
<dl>
<dt>
<dd> Enable debugging of various aspects of the megatools operation. You may enable multiple debugging options separated by commas. (eg. --debug api,fs) 

 Available options are: 

<dl>
<dt>
<dd> &bull; 

 api: Dump Mega.co.nz API calls</dl>
 

<dl>
<dt>
<dd> &bull; 

 fs: Dump Mega.co.nz filesystem (may require --reload to actually print something)</dl>
 

<dl>
<dt>
<dd> &bull; 

 cache: Dump cache contents</dl>
</dl>
 

 --version
<dl>
<dt>
<dd> Show version information</dl>
 

 &lt;remotepaths&gt;
<dl>
<dt>
<dd> One or more remote directories to create.</dl>
 

 &lt;contactemail&gt;
<dl>
<dt>
<dd> Valid email address of a contact you want to add.</dl>

<h2>EXAMPLES</h2>

 

<dl>
<dt>
<dd> &bull; Create new folder: 

<dl>
<dt>
<dd> <pre>
$ megamkdir /Root/MyNewFolder
$ megals /Root
/Root
/Root/MyNewFolder
</pre></dl>
</dl>
 

<dl>
<dt>
<dd> &bull; Add new contact to your contacts list: 

<dl>
<dt>
<dd> <pre>
$ megamkdir /Contacts/some [at] email.com
</pre></dl>
</dl>

<h2>REMOTE FILESYSTEM</h2>

 

 Mega.co.nz filesystem is represented as a tree of nodes of various types. Nodes are identified by a 8 character node handles (eg. 7Fdi3ZjC). Structure of the filesystem is not encrypted. 

 Megatools maps node tree structure to a traditional filesystem paths (eg. /Root/SomeFile.DAT). 

 <b>NOTE</b>: By the nature of Mega.co.nz storage, several files in the directory can have the same name. To allow access to such files, the names of conflicting files are extended by appending dot and their node handle like this: 

<dl>
<dt>
<dd> <pre>
/Root/conflictingfile
/Root/conflictingfile.7Fdi3ZjC
/Root/conflictingfile.mEU23aSD
</pre></dl>
 

 You need to be aware of several special folders: 

 /Root
<dl>
<dt>
<dd> Writable directory representing the root of the filesystem.</dl>
 

 /Trash
<dl>
<dt>
<dd> Trash directory where Mega.co.nz web client moves deleted files. This directory is not used by megatools when removing files.</dl>
 

 /Inbox
<dl>
<dt>
<dd> Not sure.</dl>
 

 /Contacts
<dl>
<dt>
<dd> Directory containing subdirectories representing your contacts list. If you want to add contacts to the list, simply create subdirectory named after the contact you want to add.</dl>
 

 /Contacts/&lt;email&gt;
<dl>
<dt>
<dd> Directories representing individual contacts in your contacts list. These directories contain folders that others shared with you. All shared files are read-only, at the moment.</dl>

<h2>SEE ALSO</h2>

 

 <b><a HREF="/docs/linux/man/7-megatools/">megatools</a></b>(7), <b><a HREF="/docs/linux/man/5-megarc/">megarc</a></b>(5), <b><a HREF="/docs/linux/man/1-megadf/">megadf</a></b>(1), <b><a HREF="/docs/linux/man/1-megadl/">megadl</a></b>(1), <b><a HREF="/docs/linux/man/1-megaget/">megaget</a></b>(1), <b><a HREF="/docs/linux/man/1-megals/">megals</a></b>(1), <b><a HREF="/docs/linux/man/1-megamkdir/">megamkdir</a></b>(1), <b><a HREF="/docs/linux/man/1-megaput/">megaput</a></b>(1), <b><a HREF="/docs/linux/man/1-megareg/">megareg</a></b>(1), <b><a HREF="/docs/linux/man/1-megarm/">megarm</a></b>(1), <b><a HREF="/docs/linux/man/1-megamv/">megamv</a></b>(1), <b><a HREF="/docs/linux/man/1-megasync/">megasync</a></b>(1), <b><a HREF="/docs/linux/man/1-megafs/">megafs</a></b>(1).

<h2>MEGATOOLS</h2>

 

 Part of the <b><a HREF="/docs/linux/man/7-megatools/">megatools</a></b>(7) suite.

<h2>BUGS</h2>

 

 Report bugs at <a rel="nofollow" HREF="https://github.com/megous/megatools">https://github.com/megous/megatools</a> or megous [at] megous.com.

<h2>AUTHOR</h2>

 

 Megatools was written by Ondrej Jirman &lt;megous [at] megous.com&gt;, 2013. 

 Official website is <a rel="nofollow" HREF="http://megatools.megous.com.">http://megatools.megous.com.</a> 

<h2>Index</h2>


