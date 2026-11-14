---
title: "selinux_raw_context_to_color(3)"
name: "selinux_raw_context_to_color"
section: "3"
letter: "s"
url: "/docs/linux/man/3-selinux_raw_context_to_color/"
description: "selinux_raw_context_to_color – Return RGB color string for an SELinux security context"
---

<p>selinux_raw_context_to_color &#8211; Return RGB color string for an SELinux security context</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;selinux/selinux.h&gt;
int selinux_raw_context_to_color(char *raw,

                                 char **color_str);</code></pre>
<h2>Description</h2>
<p><code>selinux_raw_context_to_color</code>() returns a <i>color_str</i> associated to the raw context <i>raw</i> provided that the <code><a href="/docs/linux/man/8-mcstransd/">mcstransd</a></code>(8) daemon is running, the policy is an MLS type policy (MCS or MLS) and there is a color configuration file <code><a href="/docs/linux/man/5-secolor-conf/">secolor.conf</a></code>(5) (see the <code>FILES</code> section). The <i>color_str</i> string is a space separated list of eight hexadecimal RGB triples, each prefixed by a hash character (#). These represent the user:role:type:range components of the foreground and background colors. An example string is shown in the <code>EXAMPLE</code> section. The returned <i>color_str</i> string must be freed with <code><a href="/docs/linux/man/3-free/">free</a></code>(3). If a color has not been configured for a specific user, role, type and/or range component of context <i>raw</i>, then <code>selinux_raw_context_to_color</code>() will select the color returned in <i>color_str</i> in order of precedence as follows:</p>
<dl>
<dd>role, type, range<br />
 user, type, range<br />
 user, role, range<br />
 user, role, type
</dl>
<p> If there are no entries in the <code><a href="/docs/linux/man/5-secolor-conf/">secolor.conf</a></code>(5) file for any of the components of context <i>raw</i> (or the file is not present), then the default string returned in <i>color_str</i> is:</p>
<dl>
<dd>&#8212;&#8211; user &#8212;- &#8212;- role &#8212;- &#8212;- type &#8212;- &#8212;- range &#8212;-<br />
 #000000 #ffffff #000000 #ffffff #000000 #ffffff #000000 #ffffff </p>
<h2>Return Value</h2>
<p>On success, zero is returned.<br />
 On failure, -1 is returned with <i>errno</i> set appropriately.</p>
<h2>Errors</h2>
<p><code>ENOENT</code> If the <code><a href="/docs/linux/man/8-mcstransd/">mcstransd</a></code>(8) daemon is not running.</p>
<h2>Files</h2>
<p><code>selinux_raw_context_to_color</code>() obtains the translated entry from the active policy <code><a href="/docs/linux/man/5-secolor-conf/">secolor.conf</a></code>(5) file as returned by <code><a href="/docs/linux/man/3-selinux_colors_path/">selinux_colors_path</a></code>(3). The file format is described in <code><a href="/docs/linux/man/5-secolor-conf/">secolor.conf</a></code>(5).</p>
<h2>Notes</h2>
<p>1. The primary use of <code>selinux_raw_context_to_color</code>() is to return a color that corresponds to a range, that can then be used to highlight information at different MLS levels. </p>
<p> 2. The <code><a href="/docs/linux/man/8-mcstransd/">mcstransd</a></code>(8) daemon process security level must dominate the <i>raw</i> security level passed to it by the <code>selinux_raw_context_to_color</code>() function. If not, the range color selected will be as defined by the order of precedence.</p>
<h2>Example</h2>
<p><code>selinux_raw_context_to_color</code>() returns the foreground and background colors of the context string components (user:role:type:range) as RGB triples as follows: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;user&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;role&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;type&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;range </p>
<p>&nbsp;<wbr>&nbsp;fg&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;bg&nbsp;<wbr>&nbsp;:&nbsp;<wbr>&nbsp;<wbr>&nbsp;fg&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;bg&nbsp;<wbr>&nbsp;<wbr>&nbsp;:&nbsp;<wbr>&nbsp;fg&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;bg&nbsp;<wbr>&nbsp;<wbr>&nbsp;:&nbsp;<wbr>&nbsp;fg&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;bg&nbsp;<wbr>&nbsp;<br />
 #000000 #ffffff #ffffff #000000 #d2b48c #ffa500 #000000 #008000 </p>
<p>&nbsp;black&nbsp;<wbr>&nbsp;<wbr>&nbsp;white :&nbsp;<wbr>&nbsp;white&nbsp;<wbr>&nbsp;<wbr>&nbsp;black&nbsp;<wbr>&nbsp;: tan&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;orange&nbsp;<wbr>&nbsp;: black&nbsp;<wbr>&nbsp;<wbr>&nbsp;green&nbsp;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8), <code><a href="/docs/linux/man/3-selinux_colors_path/">selinux_colors_path</a></code>(3), <code><a href="/docs/linux/man/8-mcstransd/">mcstransd</a></code>(8), <code><a href="/docs/linux/man/5-secolor-conf/">secolor.conf</a></code>(5), <code><a href="/docs/linux/man/3-selinux_raw_to_trans_context/">selinux_raw_to_trans_context</a></code>(3), <code><a href="/docs/linux/man/3-selinux_trans_to_raw_context/">selinux_trans_to_raw_context</a></code>(3), <code><a href="/docs/linux/man/3-free/">free</a></code>(3) </p>
