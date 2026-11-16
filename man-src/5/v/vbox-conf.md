---
title: "vbox-conf(5)"
name: "vbox-conf"
section: "5"
letter: "v"
url: "/docs/linux/man/5-vbox-conf/"
description: "vbox.conf – config file for vbox"
---

<p>vbox.conf &#8211; config file for vbox</p>
<h2>Description</h2>
<p>This file is used to configure when and on what conditions calls are taken. It can also be used to define which CALLERID is used with which person. Everything after the &quot;#&quot; is ignored, as are empty lines. All arguments must be separated by whitespace (spaces, tabs). Arguments may not contain whitespace. This file consists of several sections. A section begins with &quot;[&quot; NAME &quot;]&quot;. The section name is case insensitive. A section ends at the end of the file or at the end of a new section. These sections exist:</p>
<dl>
<dt><code>[CALLERIDS]</code></dt>
<dd>This section maps CALLERID to persons and what settings to use. On an incoming call the CALLERID of the caller is detected and compared with this section. The SECTION of the first match is used. <code>Format : PATTERN SECTION REALNAME</code></dd>
<dl>
<dd>
</dd><dl>
<dt><code>PATTERN</code></dt>
<dd>UN*X Pattern of a CALLERID. You may not use whitespace.</dd>
<dt><code>SECTION</code></dt>
<dd>Name of a user section to use. You many not use whitespace. With a &quot;-&quot; STANDARD will be used, with a &quot;*&quot; the REALNAME will be used.</dd>
<dt><code>REALNAME</code></dt>
<dd>Full name of the person that should be mapped to the CALLERID. Here you may use spaces.</dd></dl>
</dl>
<dt>&nbsp;<wbr></dt>
<dd>At the end of the [CALLERIDS] Section, you should have the entry &quot;* &#8211; *** Unknown ***&quot;, so that also calls with no or unknown CALLERID can be processed.</dd>
<dt><code>[RINGS]</code></dt>
<dd>In this section you set when and after how many RINGs a call is taken. This section is the first to be examined when a call is incoming to determine if the call should be taken. The number of RINGs can be overruled in the user section. <code>Format : TIME DAYS RINGS</code></dd>
<dl>
<dd>
</dd><dl>
<dt><code>TIME</code></dt>
<dd>time when the call should be taken. Read the isdntime(5) man page for details.</dd>
<dt><code>DAYS</code></dt>
<dd>days when the call should be takes. Read the isdntime(5) man page for details.</dd>
<dt><code>RINGS</code></dt>
<dd>Number of rings to wait before taking the call. With version 2.0 of the hisax isdn device driver the interval between two rings is longer (now it&#8217;s nearly like a telephone; 4 &#8211; 5 seconds between rings).</dd></dl>
</dl>
<dt><code>user defined sections</code></dt>
<dd>Here you can make individual settings for some people. The section name has the same format as the other sections. The names CALLERIDS and RINGS are reserved. <code>Format : TIME DAYS MESSAGE RECTIME [FLAG] [&#8230;]</code></dd>
<dl>
<dd>
</dd><dl>
<dt><code>TIME</code></dt>
<dd>time when the call should be taken. Read the isdntime(5) man page for details.</dd>
<dt><code>DAYS</code></dt>
<dd>days when the call should be taken. Read the isdntime(5) man page for details.</dd>
<dt><code>MESSAGE</code></dt>
<dd>Standard message to play for this call. You must either give the filename with full path, or a filename relative to /var/spool/vbox/&lt;user&gt;/messages. Default is &quot;standard.msg&quot;. You may not use spaces or tabs.</dd>
<dt><code>RECTIME</code></dt>
<dd>Time in seconds: how long should vboxgetty record? Default is 60 seconds.</dd>
<dt><code>FLAGS</code></dt>
<dd>You can additionally give these flags:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>NOANSWER</code></dt>
<dd>Don&#8217;t answer this call. Default is to answer.</dd>
<dt><code>NORECORD</code></dt>
<dd>Don&#8217;t record a message. Default is to record.</dd>
<dt><code>NOTIMEOUTMSG</code></dt>
<dd>Don&#8217;t play timeout message. Default is to play.</dd>
<dt><code>NOBEEPMSG</code></dt>
<dd>Don&#8217;t play beep message. Default is to play.</dd>
<dt><code>NOSTDMSG</code></dt>
<dd>Don&#8217;t play std message. Default is to play.</dd>
<dt><code>RINGS=</code></dt>
<dd>Number of rings to wait before taking the call. Here you can override the [RINGS] section.</dd>
<dt><code>TOLLRINGS=</code></dt>
<dd>Number of rings to wait before answering the call, if new messages are available. This flag overrides the section [RINGS] and the flag RINGS= if there are new messages. The directory to search for new messages must be given with TOLLCHECK (or you can use the default).</dd>
<dt><code>TOLLCHECK=</code></dt>
<dd>Directory to search for new messages. Default is /var/spool/vbox/&lt;user&gt;/incoming.</dd>
<dt><code>SCRIPT=</code></dt>
<dd>TCL-Script to start after taking the call. This must be the full path or a filename relative to /var/spool/vbox/&lt;user&gt;. The default is standard.tcl.</dd></dl>
</dl>
</dl>
</dl>
<h2>Files</h2>
<dl>
<dt><code>/var/spool/vbox/&lt;user&gt;/vbox.conf</code></dt>
<dd>this configuration file. </dd>
<dt>/usr/doc/isdnutils/examples/vbox.conf</dt>
<dd>an example. </dd>
</dl>
<h2>See Also</h2>
<p><code>isdntime(5)</code> </p>
<h2>Author</h2>
<p>This manual page was written by Andreas Jellinghaus &lt;aj [at] dungeon.inka.de&gt;, for Debian GNU/Linux and isdn4linux.</p>
</dl>