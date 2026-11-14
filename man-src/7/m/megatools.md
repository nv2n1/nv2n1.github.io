---
title: "megatools(7)"
name: "megatools"
section: "7"
letter: "m"
url: "/docs/linux/man/7-megatools/"
description: "megatools – Mega.co.nz command line tools"
---

<p>megatools &#8211; Mega.co.nz command line tools</p>
<h2>Synopsis</h2>
<pre><i>megadf</i> [--free|--total|--used] [--mb|--gb|-h]
<i>megals</i> [-e] [-h] [--header] [-l] [-R] [-n] [&lt;remotepaths&gt;...]
<i>megaput</i> [--no-progress] [--path &lt;remotepath&gt;] &lt;paths&gt;...
<i>megamkdir</i> &lt;remotepaths&gt;...
<i>megamkdir</i> /Contacts/&lt;contactemail&gt;
<i>megaget</i> [--no-progress] [--path &lt;path&gt;] &lt;remotepaths&gt;...
<i>megaget</i> --path - &lt;remotefile&gt;
<i>megamv</i> &lt;srcpaths&gt;... &lt;destpath&gt;
<i>megarm</i> &lt;remotepaths&gt;...
<i>megarm</i> /Contacts/&lt;contactemail&gt;
<i>megadl</i> [--no-progress] [--path &lt;path&gt;] &lt;links&gt;...
<i>megadl</i> --path - &lt;filelink&gt;
<i>megareg</i> [--scripted] --register --email &lt;email&gt; --name &lt;realname&gt; --password &lt;password&gt;
<i>megareg</i> [--scripted] --verify &lt;state&gt; &lt;link&gt;
<i>megafs</i> [-o &lt;options&gt;...] [-d] [-f] &lt;mountpoint&gt;</pre>
<h2>Description</h2>
<p>Megatools is a collection of programs for accessing Mega service from a command line of your desktop or server. </p>
<p> Megatools allow you to copy individual files as well as entire directory trees to and from the cloud. You can also perform streaming downloads for example to preview videos and audio files, without needing to download the entire file. </p>
<p> Megatools are robust and optimized for fast operation &#8211; as fast as Mega servers allow. Memory requirements and CPU utilization are kept at minimum. </p>
<p> You can register account using a <code><a href="/docs/linux/man/1-megareg/">megareg</a></code>(1) tool, with the benefit of having true control of your encryption keys. </p>
<p> Mega website can be found at <a rel="nofollow" href="http://mega.co.nz.">http://mega.co.nz.</a> </p>
<p> Megatools can be downloaded at <a rel="nofollow" href="http://megatools.megous.com">http://megatools.megous.com</a></p>
<h2>Tools Overview</h2>
<p><code><a href="/docs/linux/man/1-megareg/">megareg</a></code>(1)</p>
<dl>
<dd>Register and verify a new mega account</dl>
<p> <code><a href="/docs/linux/man/1-megadf/">megadf</a></code>(1)</p>
<dl>
<dd>Show your cloud storage space usage/quota</dl>
<p> <code><a href="/docs/linux/man/1-megals/">megals</a></code>(1)</p>
<dl>
<dd>List all remote files</dl>
<p> <code><a href="/docs/linux/man/1-megamkdir/">megamkdir</a></code>(1)</p>
<dl>
<dd>Create remote directory</dl>
<p> <code><a href="/docs/linux/man/1-megarm/">megarm</a></code>(1)</p>
<dl>
<dd>Remove remote file or directory</dl>
<p> <code><a href="/docs/linux/man/1-megamv/">megamv</a></code>(1)</p>
<dl>
<dd>Move and rename remote files</dl>
<p> <code><a href="/docs/linux/man/1-megaput/">megaput</a></code>(1)</p>
<dl>
<dd>Upload individual files</dl>
<p> <code><a href="/docs/linux/man/1-megaget/">megaget</a></code>(1)</p>
<dl>
<dd>Download individual files</dl>
<p> <code><a href="/docs/linux/man/1-megadl/">megadl</a></code>(1)</p>
<dl>
<dd>Download file from a &quot;public&quot; Mega link (doesn&#8217;t require login)</dl>
<p> <code><a href="/docs/linux/man/1-megasync/">megasync</a></code>(1)</p>
<dl>
<dd>Upload or download a directory tree</dl>
<p> <code><a href="/docs/linux/man/1-megafs/">megafs</a></code>(1)</p>
<dl>
<dd>Mount remote filesystem locally.</dl>
<h2>Configuration Files</h2>
<p>See <code><a href="/docs/linux/man/5-megarc/">megarc</a></code>(5) for information about mega configuration file. </p>
<p> Each of the individual tools have help that can be accessed using &#8211;help parameter.</p>
<h2>Session Cache</h2>
<p>If you modify cloud filesystem from the Mega.co.nz website or from another computer, you&#8217;ll need to refresh your session cache. This can be done by using the &#8211;reload option to any tool, or by waiting for a cache timeout (default timeout is set to 10 minutes).</p>
<h2>Remote Filesystem</h2>
<p>Mega.co.nz filesystem is represented as a tree of nodes of various types. Nodes are identified by a 8 character node handles (eg. 7Fdi3ZjC). Structure of the filesystem is not encrypted. </p>
<p> Megatools maps node tree structure to a traditional filesystem paths (eg. /Root/SomeFile.DAT). </p>
<p> <code>NOTE</code>: By the nature of Mega.co.nz storage, several files in the directory can have the same name. To allow access to such files, the names of conflicting files are extended by appending dot and their node handle like this: </p>
<dl>
<dd>
<pre>/Root/conflictingfile
/Root/conflictingfile.7Fdi3ZjC
/Root/conflictingfile.mEU23aSD</pre>
</dl>
<p> You need to be aware of several special folders: </p>
<p> /Root</p>
<dl>
<dd>Writable directory representing the root of the filesystem.</dl>
<p> /Trash</p>
<dl>
<dd>Trash directory where Mega.co.nz web client moves deleted files. This directory is not used by megatools when removing files.</dl>
<p> /Inbox</p>
<dl>
<dd>Not sure.</dl>
<p> /Contacts</p>
<dl>
<dd>Directory containing subdirectories representing your contacts list. If you want to add contacts to the list, simply create subdirectory named after the contact you want to add.</dl>
<p> /Contacts/&lt;email&gt;</p>
<dl>
<dd>Directories representing individual contacts in your contacts list. These directories contain folders that others shared with you. All shared files are read-only, at the moment.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-megatools/">megatools</a></code>(7), <code><a href="/docs/linux/man/5-megarc/">megarc</a></code>(5), <code><a href="/docs/linux/man/1-megadf/">megadf</a></code>(1), <code><a href="/docs/linux/man/1-megadl/">megadl</a></code>(1), <code><a href="/docs/linux/man/1-megaget/">megaget</a></code>(1), <code><a href="/docs/linux/man/1-megals/">megals</a></code>(1), <code><a href="/docs/linux/man/1-megamkdir/">megamkdir</a></code>(1), <code><a href="/docs/linux/man/1-megaput/">megaput</a></code>(1), <code><a href="/docs/linux/man/1-megareg/">megareg</a></code>(1), <code><a href="/docs/linux/man/1-megarm/">megarm</a></code>(1), <code><a href="/docs/linux/man/1-megamv/">megamv</a></code>(1), <code><a href="/docs/linux/man/1-megasync/">megasync</a></code>(1), <code><a href="/docs/linux/man/1-megafs/">megafs</a></code>(1).</p>
<h2>Megatools</h2>
<p>Part of the <code><a href="/docs/linux/man/7-megatools/">megatools</a></code>(7) suite.</p>
<h2>Bugs</h2>
<p>Report bugs at <a rel="nofollow" href="https://github.com/megous/megatools">https://github.com/megous/megatools</a> or megous [at] megous.com.</p>
<h2>Author</h2>
<p>Megatools was written by Ondrej Jirman &lt;megous [at] megous.com&gt;, 2013. </p>
<p> Official website is <a rel="nofollow" href="http://megatools.megous.com.">http://megatools.megous.com.</a></p>
