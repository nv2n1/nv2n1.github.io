---

title: "fpaste(1)"
name: "fpaste"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fpaste/"
description: "fpaste – A cli frontend for the fpaste.org pastebin"
---

<h2>NAME</h2>
<p> fpaste &#8211; A cli frontend for the fpaste.org pastebin</p>
<p> <code>fpaste</code> [<i>OPTION</i>]&#8230; [<i>FILE</i>]&#8230;</p>
<p> It is often useful to be able to easily paste text to the Fedora Pastebin at <a rel="nofollow" href="http://fpaste.org">http://fpaste.org</a> and this simple utility will do that and return the resulting URL so that people may examine the output. This can hopefully help folks who are for some reason stuck without X, working remotely, or any other reason they may be unable to paste something into the pastebin using a web browser.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></dt>
<dd> show program&#8217;s version number and exit</dd>
<dt><code>-h, &#8211;help</code></dt>
<dd> show help message and exit</dd>
<dt><code>-n &quot;NICKNAME&quot;</code></dt>
<dd> your nickname; default is &quot;&quot;</dd>
<dt><code>-d &quot;PASSWORD&quot;, &#8211;password=&quot;PASSWORD&quot;</code></dt>
<dd> password for paste; default is &quot;&quot;</dd>
<dt><code>-l &quot;LANGUAGE&quot;</code></dt>
<dd> language of content for syntax highlighting; default is &quot;text&quot;; use &quot;list&quot; to show all 200+ supported langs</dd>
<dt><code>-x &quot;EXPIRES&quot;</code></dt>
<dd> time before paste is removed; default is 2592000 seconds; valid options: 1800, 21600, 86400, 604800, 2592000</dd>
<dt><code>-U, &#8211;URL &quot;URL&quot;</code></dt>
<dd> URL of fpaste server; default is <a rel="nofollow" href="http://fpaste.org">http://fpaste.org</a></dd>
<dt><code>-P, &#8211;private</code></dt>
<dd> make paste private; default is yes; valid options: yes, no </dd>
<dt><code>-i, &#8211;clipin</code></dt>
<dd> read paste text from current X clipboard selection</dd>
<dt><code>-o, &#8211;clipout</code></dt>
<dd> save returned paste URL to X clipboard</dd>
<dt><code>&#8211;selection=CLIPBOARD</code></dt>
<dd> specify which X clipboard to use. valid options: &quot;primary&quot; (default; middle-mouse-button paste), &quot;secondary&quot; (uncommon), or &quot;clipboard&quot; (ctrl-v paste)</dd>
<dt><code>&#8211;fullpath</code></dt>
<dd> use pathname VS basename for file description(s)</dd>
<dt><code>&#8211;pasteself</code></dt>
<dd> paste this script itself</dd>
<dt><code>&#8211;sysinfo</code></dt>
<dd> paste system information</dd>
<dt><code>&#8211;printonly</code></dt>
<dd> print paste, but do not send</dd>
<dt><code>&#8211;confirm</code></dt>
<dd> print paste, and prompt for confirmation before sending</dd></dl>
<h2>EXAMPLES</h2>
<dl>
<dt>Paste file foo.txt at fpaste.org</dt>
<dd>
</dd><dt>
</dt><dd> <code>fpaste foo.txt</code></dd>
<dt>Paste output of ifconfig to fpaste.org with description &quot;my network config&quot;</dt>
<dd>
</dd><dt>
</dt><dd> <code>ifconfig | fpaste </code></dd>
<dt>Paste mycode.py to fpaste.org with description as &quot;problem with foo&quot;, nickname &quot;codemonkey&quot;, and language &quot;python&quot;</dt>
<dd>
</dd><dt>
</dt><dd> <code>fpaste -n codemonkey -l python mycode.py</code></dd>
<dt>Paste mouse-selected text from the primary X selection clipboard, and then overwrite the same clipboard with the returned fpaste URL</dt>
<dd>
</dd><dt>
</dt><dd> <code>fpaste -io</code></dd>
<dt>To <i>manually paste clipboard</i> contents, run <code>fpaste</code> without file arguments so that it waits for input, then paste using mouse middle-click, &lt;Ctrl-V&gt;, or other, then press &lt;Enter&gt; followed by &lt;Ctrl-D&gt; to finish (EOF).</dt>
<dd>
</dd><dt>To paste the output of more than one program and/or file at a time, use the following example forms:</dt>
<dd>
</dd><dt>
</dt><dd> <code>(lsusb ; lspci) | fpaste</code><br />
 <code>fpaste &lt;(lsusb) &lt;(lspci)</code> </dd>
<p> <code>fpaste &lt;(fdisk -l) /etc/grub.conf </code><br />
 <code>(fdisk -l ; cat /etc/grub.conf) | fpaste </code> </p>
<p> <code>(uname -a ; yum repolist) | fpaste</code></p>
<dt>Gather and paste various information about the running system. The info collected should be practically anonymous, and you may use the &#8211;printonly or &#8211;confirm options to preview what would be sent. fpaste.org URLs are also practically anonymous ([a-zA-Z0-9]**4 == 14,776,336 combinations), so you may also preview it instead before giving the link out.</dt>
<dd>
</dd><dt>
</dt><dd> <code>fpaste &#8211;sysinfo</code><br />
 <code>fpaste &#8211;sysinfo &#8211;confirm</code><br />
 <code>fpaste &#8211;sysinfo &#8211;printonly | less</code></dd></dl>
<h2>BUGS</h2>
<p> Report bugs to: <a rel="nofollow" href="https://fedorahosted.org/fpaste/newticket">https://fedorahosted.org/fpaste/newticket</a><br />
 or to: Jason &#8216;zcat&#8217; Farrell &lt;farrellj AT gmail DOT com&gt;.</p>
<h2>AUTHOR</h2>
<p> Fedora Unity </p>
