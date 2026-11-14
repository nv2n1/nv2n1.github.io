---
title: "elektra(5)"
name: "elektra"
section: "5"
letter: "e"
url: "/docs/linux/man/5-elektra/"
description: "elektra – A framework to store configuration atoms hierarchically"
---

<p>elektra &#8211; A framework to store configuration atoms hierarchically </p>
<p> Note </p>
<p> This section is provided for the sake of the openness of Elektra. You should not access the Elektra&#8217;s key files directly. You should use the API or the <code></p>
<p><a href="/docs/linux/man/1-kdb/">kdb</a></code>(1) command for that. </p>
<p> Elektra Key Storage Strategy.PP Elektra implements a very simple way to store the key-value pairs. The value (and some metainfo) for each key is stored in a single file. The key name (and some of its context) is sufficient to find the file name that stores the value. </p>
<p> The <i>system/*</i> keys are stored under <i>/etc/kdb/</i>, and the <i>user/*</i> keys can be found under each user&#8217;s <i>$HOME/.kdb/</i>. </p>
<p> Here are some examples of key names, and where Elektra goes to look for them in the disk. </p>
<p> <i>system/sw/XFree86/screen0/driver</i></p>
<dl>
<dd>Maps to: <i>/etc/kdb/system/sw/XFree86/screen0/driver</i></dl>
<p> <i>user/env/PATH</i></p>
<dl>
<dd>Maps to: <i>~$USER/.kdb/user/env/PATH</i></dl>
<p> <i>user:luciana/env/PATH</i></p>
<dl>
<dd>Maps to: <i>~luciana/.kdb/user/env/PATH</i></dl>
<p> <i>system/mime.types/some.mime</i></p>
<dl>
<dd>Maps to: <i>/etc/kdb/system/mime.types/some.mime</i></dl>
<p> Some may think that one file per key will consume many filesystem i-nodes. Actually, when not using Reiser4 filesystem, it may consume some more disk space, and it may also be not so efficient than reading one single text file, as KConfig does. But Elektra&#8217;s nature lets applications load their keys on demand; so it is possible to avoid the read-all-use-some approach. Writing updated keys back to disk is also more robust, because unchanged keys won&#8217;t be touched, different from a single file approach, that must be entirelly rewritten. </p>
<p> Besides that, big applications (like Mozilla, Konqueror, KDE, Gnome) key gathering time is a very small part of what they have to do to start up. And the benefits of an homogeneous key database to the entire system are much bigger then these issues. Think about a common integration between everything, flexibility, security granularity and openness. XML, Storage Backends and Elektra.PP This document you are just reading was written in DocBook XML. XML is a wonderfull technology, but brings no value to this software. Two main goals of the Elektra Project are to be lightweight, and to be accessible by early boot stage programs like <code>/sbin/init</code> and the <i>/etc/rc.d</i> scripts. </p>
<p> XML parsing libraries are memory eaters, not so fast as we can expect, and they are usualy located under <i>/usr/lib</i>, which may be unavailable to these early boot stage needs. </p>
<p> Some discussions asked for a sort of plugin architecture to let user decide the format to store keys content. Well, the info that goes into the key file is not big deal as you&#8217;ll see, and sometimes, too many options is bad business, and not the path for the Elektra Project. </p>
<p> So no XML, no plugin architecture, no sophistication. Lets keep it simple and generic. A very straight forward text based file format was defined to store a single key value. Key Files Format.PP Inside Elektra key database, each key is a file, and every file is a key. So most of the key&#8217;s metainformation are actually its file attributes, as you can see in a regular <code><a href="/docs/linux/man/1-ls/">ls</a></code>(1) command output. </p>
<p> So what needs to be stored inside the key file is the data type (binary or text), key comment and the actual data. The format of each key file is: </p>
<dl>
<dd>
<pre>File Format Version
Data Type
As many lines of
comments as we want (UTF-8 encoded)
&lt;DATA&gt;
The data encoded as text</pre>
</dl>
<p> So if we set the key <i>system/hw/eth0/driver</i> as type <code>String</code> and value &quot;<i>3com</i>&quot;, and comment &quot;<i>The driver for my network interface</i>&quot;, we&#8217;ll find the file <i>/etc/kdb/system/hw/eth0/driver</i> containing: </p>
<dl>
<dd>
<pre>RG002
40
The driver for my network interface
&lt;DATA&gt;
3com</pre>
</dl>
<p> Other example: setting <i>user/tmp/proprietary</i> as <code>Binary</code>, and value &quot;<i>A groovy data I want to hide</i>&quot;, and comment &quot;<i>Stay away from here</i>&quot;, you&#8217;ll get in <i>~$USER/.kdb/user/tmp/proprietary</i> the following: </p>
<dl>
<dd>
<pre>RG002
20
Stay away from here
&lt;DATA&gt;
41206772 6f6f7679 20646174 61204920 77616e74 20746f20 68696465</pre>
</dl>
<p> The current data types are: </p>
<p> Between 20 and 39</p>
<dl>
<dd>Binary value. The data will be encoded into a text format. Today only type 20 is used, and means a raw stream of bytes with no special semantics to Elektra. The other values are reserved for future use; being treated still as binary values but possibly with some semantics to Elektra or a higher level application.</dl>
<p> 40 up to 254</p>
<dl>
<dd>Text, UTF-8 encoded. Values higher then 40 are reserved for future or application specific implementations of more abstract data types, like time/date, color, font, etc. But always represented as pure text that can be edited in any text editor like <code><a href="/docs/linux/man/1-vi/">vi</a></code>(1).</dl>
<p> Types between 0 and 19 are used only internaly in the API, and will never appear into a key file. They are used to define meta keys as directory, link, etc.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-kdb/">kdb</a></code>(1), <code><a href="/docs/linux/man/7-elektra/">elektra</a></code>(7)</p>
<h2>Author</h2>
<p><code>Avi Alkalay</code> &lt;avi at unix.sh&gt;<br />
 Linux Market Developer, Senior IT and Software Architect, IBM Linux Impact Team :: <i>ibm.com/linux</i> </p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
<p>Copyright &#169; 2004 Avi Alkalay</p>
