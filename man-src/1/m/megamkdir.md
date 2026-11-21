---

title: "megamkdir(1)"
name: "megamkdir"
section: "1"
letter: "m"
url: "/docs/linux/man/1-megamkdir/"
---

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
</dt><dd> Account username (email)</dd></dl>
 

 -p &lt;password&gt;, --password &lt;password&gt;
<dl>
<dt>
</dt><dd> Account password</dd></dl>
 

 --config &lt;path&gt;
<dl>
<dt>
</dt><dd> Load configuration from a file</dd></dl>
 

 --ignore-config-file
<dl>
<dt>
</dt><dd> Disable loading .megarc</dd></dl>
 

 --no-ask-password
<dl>
<dt>
</dt><dd> Never ask interactively for a password</dd></dl>
 

 --reload
<dl>
<dt>
</dt><dd> Reload filesystem cache</dd></dl>
 

 --debug [&lt;options&gt;]
<dl>
<dt>
</dt><dd> Enable debugging of various aspects of the megatools operation. You may enable multiple debugging options separated by commas. (eg. --debug api,fs) 
 Available options are: 
</dd><dl>
<dt>
</dt><dd> &bull; 
 api: Dump Mega.co.nz API calls</dd></dl>
 

<dl>
<dt>
</dt><dd> &bull; 
 fs: Dump Mega.co.nz filesystem (may require --reload to actually print something)</dd></dl>
 

<dl>
<dt>
</dt><dd> &bull; 
 cache: Dump cache contents</dd></dl>
</dl>
 

 --version
<dl>
<dt>
</dt><dd> Show version information</dd></dl>
 

 &lt;remotepaths&gt;
<dl>
<dt>
</dt><dd> One or more remote directories to create.</dd></dl>
 

 &lt;contactemail&gt;
<dl>
<dt>
</dt><dd> Valid email address of a contact you want to add.</dd></dl>

<h2>EXAMPLES</h2>

 

<dl>
<dt>
</dt><dd> &bull; Create new folder: 
</dd><dl>
<dt>
</dt><dd> <pre>
$ megamkdir /Root/MyNewFolder
$ megals /Root
/Root
/Root/MyNewFolder
</pre></dd></dl>
</dl>
 

<dl>
<dt>
</dt><dd> &bull; Add new contact to your contacts list: 
</dd><dl>
<dt>
</dt><dd> <pre>
$ megamkdir /Contacts/some [at] email.com
</pre></dd></dl>
</dl>

<h2>REMOTE FILESYSTEM</h2>

 

 Mega.co.nz filesystem is represented as a tree of nodes of various types. Nodes are identified by a 8 character node handles (eg. 7Fdi3ZjC). Structure of the filesystem is not encrypted. 

 Megatools maps node tree structure to a traditional filesystem paths (eg. /Root/SomeFile.DAT). 

 <b>NOTE</b>: By the nature of Mega.co.nz storage, several files in the directory can have the same name. To allow access to such files, the names of conflicting files are extended by appending dot and their node handle like this: 

<dl>
<dt>
</dt><dd> <pre>
/Root/conflictingfile
/Root/conflictingfile.7Fdi3ZjC
/Root/conflictingfile.mEU23aSD
</pre></dd></dl>
 

 You need to be aware of several special folders: 

 /Root
<dl>
<dt>
</dt><dd> Writable directory representing the root of the filesystem.</dd></dl>
 

 /Trash
<dl>
<dt>
</dt><dd> Trash directory where Mega.co.nz web client moves deleted files. This directory is not used by megatools when removing files.</dd></dl>
 

 /Inbox
<dl>
<dt>
</dt><dd> Not sure.</dd></dl>
 

 /Contacts
<dl>
<dt>
</dt><dd> Directory containing subdirectories representing your contacts list. If you want to add contacts to the list, simply create subdirectory named after the contact you want to add.</dd></dl>
 

 /Contacts/&lt;email&gt;
<dl>
<dt>
</dt><dd> Directories representing individual contacts in your contacts list. These directories contain folders that others shared with you. All shared files are read-only, at the moment.</dd></dl>

<h2>SEE ALSO</h2>

 

 <b><a HREF="/docs/linux/man/7-megatools/">megatools</a></b>(7), <b><a HREF="/docs/linux/man/5-megarc/">megarc</a></b>(5), <b><a HREF="/docs/linux/man/1-megadf/">megadf</a></b>(1), <b><a HREF="/docs/linux/man/1-megadl/">megadl</a></b>(1), <b><a HREF="/docs/linux/man/1-megaget/">megaget</a></b>(1), <b><a HREF="/docs/linux/man/1-megals/">megals</a></b>(1), <b><a HREF="/docs/linux/man/1-megamkdir/">megamkdir</a></b>(1), <b><a HREF="/docs/linux/man/1-megaput/">megaput</a></b>(1), <b><a HREF="/docs/linux/man/1-megareg/">megareg</a></b>(1), <b><a HREF="/docs/linux/man/1-megarm/">megarm</a></b>(1), <b><a HREF="/docs/linux/man/1-megamv/">megamv</a></b>(1), <b><a HREF="/docs/linux/man/1-megasync/">megasync</a></b>(1), <b><a HREF="/docs/linux/man/1-megafs/">megafs</a></b>(1).

<h2>MEGATOOLS</h2>

 

 Part of the <b><a HREF="/docs/linux/man/7-megatools/">megatools</a></b>(7) suite.

<h2>BUGS</h2>

 

 Report bugs at <a rel="nofollow" HREF="https://github.com/megous/megatools">https://github.com/megous/megatools</a> or megous [at] megous.com.

<h2>AUTHOR</h2>

 

 Megatools was written by Ondrej Jirman &lt;megous [at] megous.com&gt;, 2013. 

 Official website is <a rel="nofollow" HREF="http://megatools.megous.com.">http://megatools.megous.com.</a>
