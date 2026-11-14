---
title: "vdpa(8)"
name: "vdpa"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vdpa/"
description: "vdpa – vdpa management tool"
---

<p>vdpa &#8211; vdpa management tool</p>
<h2>Synopsis</h2>
<pre><code>vdpa

[ OPTIONS ] { dev|mgmtdev } { COMMAND |

    help }

</code></pre>
<h2>Options</h2>
<dl>
<dt><code>-V</code>,<code> &#8211;Version</code></p>
<dd>Print the version of the <code>vdpa</code> utility and exit. </p>
<dt><code>-j</code>,<code> &#8211;json</code></p>
<dd>Generate JSON output. </p>
<dt><code>-p</code>,<code> &#8211;pretty</code></p>
<dd>When combined with -j generate a pretty JSON output. </p>
</dl>
<h3><i>OBJECT</i></h3>
<dl>
<dt><code>dev</code></p>
<dd>&#8211; vdpa device. </p>
<dt><code>mgmtdev</code></p>
<dd>&#8211; vdpa management device. </p>
</dl>
<h3><i>COMMAND</i></h3>
<p>Specifies the action to perform on the object. The set of possible actions depends on the object type. It is possible to <code>show</code> (or <code>list</code> ) objects. The <code>help</code> command is available for all objects. It prints out a list of available commands and argument syntax conventions. </p>
<p> If no command is given, some default command is assumed. Usually it is <code>show</code> or, if the objects of this class cannot be listed, <code>help</code>.</p>
<h2>Exit Status</h2>
<p>Exit status is 0 if command was successful or a positive integer upon failure.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-vdpa-dev/">vdpa-dev</a></code>(8), <code><a href="/docs/linux/man/8-vdpa-mgmtdev/">vdpa-mgmtdev</a></code>(8), </p>
<h2>Reporting Bugs</h2>
<p>Report any bugs to the Network Developers mailing list <code>&lt;netdev [at] vger.kernel.org&gt;</code> where the development and maintenance is primarily done. You do not have to be subscribed to the list to send a message there.</p>
<h2>Author</h2>
<p>Parav Pandit &lt;parav [at] nvidia.com&gt;</p>
