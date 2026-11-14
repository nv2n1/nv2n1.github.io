---
title: "bt-obex(1)"
name: "bt-obex"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bt-obex/"
description: "bt-obex – a bluetooth OBEX client/server"
---

<h2 class="name">NAME</h2>
<p> bt-obex &#8211; a bluetooth OBEX client/server </p>
<h2>SYNOPSIS</h2>
<p> bt-obex [<font SIZE="-1">OPTION&#8230;</font>] </p>
<p> Help Options:<br />
&nbsp;<wbr>&nbsp;<wbr>-h, &#8211;help </p>
<p> Application Options:<br />
&nbsp;<wbr>&nbsp;<wbr>-a, &#8211;adapter=&lt;name|mac&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>-s, &#8211;server&nbsp;<wbr>[&lt;path&gt;]<br />
&nbsp;<wbr>&nbsp;<wbr>-p, &#8211;opp&nbsp;<wbr>&lt;name|mac&gt;&nbsp;<wbr>&lt;file&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>-f, &#8211;ftp=&lt;name|mac&gt;</p>
<h2>DESCRIPTION</h2>
<p> This utility implemented support of Object Push Profile (<font SIZE="-1">OPP</font>) and File Transfer Profile (<font SIZE="-1">FTP</font>). You can send and receive files to/from remote device using this tool.</p>
<h2>OPTIONS</h2>
<p> <code>-h, &#8211;help</code><br />
&nbsp;<wbr>Show help </p>
<p> <code>-a, &#8211;adapter &lt;name|mac&gt;</code><br />
&nbsp;<wbr>Specify adapter to use by his Name or&nbsp;<wbr><font SIZE="-1">MAC</font>&nbsp;<wbr>address<br />
&nbsp;<wbr>(if this option does not defined &#8211; default adapter used) </p>
<p> <code>-s, &#8211;server [&lt;path&gt;]</code><br />
&nbsp;<wbr>Register agent at&nbsp;<wbr><font SIZE="-1">OBEX</font>&nbsp;<wbr>server and set incoming/root directory to<br />
&nbsp;<wbr>`path`&nbsp;<wbr>or current folder will be used;&nbsp;<wbr>Agent is used to<br />
&nbsp;<wbr>accept/reject incoming bluetooth object push requests </p>
<p> <code>-p, &#8211;opp &lt;name|mac&gt; &lt;file&gt;</code><br />
&nbsp;<wbr>Send local file to the specified remote device using object push<br />
&nbsp;<wbr>profile </p>
<p> <code>-f, &#8211;ftp &lt;name|mac&gt;</code><br />
&nbsp;<wbr>Start&nbsp;<wbr><font SIZE="-1">FTP</font>&nbsp;<wbr>session with remote device;&nbsp;<wbr>If session opened<br />
&nbsp;<wbr>successfuly,&nbsp;<wbr><font SIZE="-1">FTP</font>&nbsp;<wbr>shell will be opened </p>
<pre>
    FTP commands:
        help                    Show help message
        exit                    Close FTP session
        cd &lt;folder&gt;             Change the current folder of the remote device
        mkdir &lt;folder&gt;          Create a new folder in the remote device
        ls                      List folder contents
        get &lt;src&gt; &lt;dst&gt;         Copy the src file (from remote device) to the dst file (on local filesystem)
        put &lt;src&gt; &lt;dst&gt;         Copy the src file (from local filesystem) to the dst file (on remote device)
        cp &lt;src&gt; &lt;dst&gt;          Copy a file within the remote device from src file to dst file
        mv &lt;src&gt; &lt;dst&gt;          Move a file within the remote device from src file to dst file
        rm &lt;target&gt;             Deletes the specified file/folder
</pre>
<h2>AUTHOR</h2>
<p> Alexander Orlenko &lt;zxteam [at] gmail.com&gt;.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-bt-adapter/">bt-adapter</a></i>(1) <i><a href="/docs/linux/man/1-bt-agent/">bt-agent</a></i>(1) <i><a href="/docs/linux/man/1-bt-device/">bt-device</a></i>(1) <i><a href="/docs/linux/man/1-bt-network/">bt-network</a></i>(1) </p>
<h2>Index</h2>
