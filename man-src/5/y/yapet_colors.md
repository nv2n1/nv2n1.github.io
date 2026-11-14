---
title: "yapet_colors(5)"
name: "yapet_colors"
section: "5"
letter: "y"
url: "/docs/linux/man/5-yapet_colors/"
description: "yapet_colors – format of YAPET color configuration"
---

<p>yapet_colors &#8211; format of YAPET color configuration</p>
<h2>Description</h2>
<p>The color scheme of YAPET can be customized by setting the <code>colors</code> option in <code>$HOME</code>/.yapet (see the section called &#8220;EXAMPLES&#8221; for examples). It has the following syntax:</p>
<dl>
<dd>
<pre><code>colors</code>=<i>OBJ1</i>:<i>&lt;fg1&gt;</i><i>&lt;bg1&gt;</i><i>&lt;attr1&gt;</i>;...;<i>OBJN</i>:<i>&lt;fgN&gt;</i><i>&lt;bgN&gt;</i><i>&lt;attrN&gt;</i></pre>
</dl>
<p> <i>OBJN</i></p>
<dl>
<dd>The UI object for which the color is set. See Table 1, &#8220;UI Objects&#8221; for possible values.</dl>
<p> <i>&lt;fgN&gt;</i></p>
<dl>
<dd>The foreground color of the UI object. See Table 2, &#8220;Colors&#8221; for possible values.</dl>
<p> <i>&lt;bgN&gt;</i></p>
<dl>
<dd>The background color of the UI object. See Table 2, &#8220;Colors&#8221; for possible values.</dl>
<p> <i>&lt;attrN&gt;</i></p>
<dl>
<dd>The attribute of the UI object. Attributes are used if the terminal does not support colors. See Table 3, &#8220;Attributes&#8221; for possible values.</dl>
<p> <code>Table 1. UI Objects</code> </p>
<table BORDER WIDTH=100%>
<tr VALIGN=top>
<td><code> UI Object </code></td>
<td><code> Abbreviation </code>
</td>
</tr>
<tr VALIGN=top>
<td> Default Color </td>
<td> DEF
</td>
</tr>
<tr VALIGN=top>
<td> Dialog </td>
<td> DIA
</td>
</tr>
<tr VALIGN=top>
<td> Dialog Title </td>
<td> DIT
</td>
</tr>
<tr VALIGN=top>
<td> Input Widget w/o focus </td>
<td> IWN
</td>
</tr>
<tr VALIGN=top>
<td> Input Widget w/ focus </td>
<td> IWF
</td>
</tr>
<tr VALIGN=top>
<td> Hidden text in Input Widget </td>
<td> IWH
</td>
</tr>
<tr VALIGN=top>
<td> Button w/o focus </td>
<td> BTN
</td>
</tr>
<tr VALIGN=top>
<td> Button w/ focus </td>
<td> BTF
</td>
</tr>
<tr VALIGN=top>
<td> List Box </td>
<td> LBX
</td>
</tr>
<tr VALIGN=top>
<td> Highlighted line in List Box </td>
<td> LBH
</td>
</tr>
<tr VALIGN=top>
<td> Check box group </td>
<td> CBG
</td>
</tr>
<tr VALIGN=top>
<td> Title Bar </td>
<td> TLB
</td>
</tr>
<tr VALIGN=top>
<td> Status Bar </td>
<td> STB
</td>
</tr>
</table>
<p> <code>Table 2. Colors</code> </p>
<table BORDER WIDTH=100%>
<tr VALIGN=top>
<td><code> Color </code></td>
<td><code> Abbreviation </code>
</td>
</tr>
<tr VALIGN=top>
<td> Black </td>
<td> k
</td>
</tr>
<tr VALIGN=top>
<td> Red </td>
<td> r
</td>
</tr>
<tr VALIGN=top>
<td> Green </td>
<td> g
</td>
</tr>
<tr VALIGN=top>
<td> Yellow </td>
<td> y
</td>
</tr>
<tr VALIGN=top>
<td> Blue </td>
<td> b
</td>
</tr>
<tr VALIGN=top>
<td> Magenta </td>
<td> m
</td>
</tr>
<tr VALIGN=top>
<td> Cyan </td>
<td> c
</td>
</tr>
<tr VALIGN=top>
<td> White </td>
<td> w
</td>
</tr>
</table>
<p> <code>Table 3. Attributes</code> </p>
<table BORDER WIDTH=100%>
<tr VALIGN=top>
<td><code> Attribute </code></td>
<td><code> Abbreviation </code>
</td>
</tr>
<tr VALIGN=top>
<td> Normal </td>
<td> 0
</td>
</tr>
<tr VALIGN=top>
<td> Standout </td>
<td> 1
</td>
</tr>
<tr VALIGN=top>
<td> Underline </td>
<td> 2
</td>
</tr>
<tr VALIGN=top>
<td> Reverse </td>
<td> 3
</td>
</tr>
<tr VALIGN=top>
<td> Blink </td>
<td> 4
</td>
</tr>
<tr VALIGN=top>
<td> Dim </td>
<td> 5
</td>
</tr>
<tr VALIGN=top>
<td> Protected </td>
<td> 6
</td>
</tr>
<tr VALIGN=top>
<td> Invisible </td>
<td> 7
</td>
</tr>
</table>
<h2>Examples</h2>
<p><code>Example 1. Default YAPET Colors</code> </p>
<p> Please note, the line has been wrapped for better readability. Line breaks are not allowed in <code>colors</code>. </p>
<dl>
<dd>
<pre>colors=DEF:wk0;DIA:wb0;DIT:bw3;IWN:kw3;IWF:kg3;IWH:yy7;
 BTN:wk0;BTF:kg3;LBX:wk0;LBH:kg3;CBG:yc0;TLB:bw0;STB:bw0</pre>
</dl>
<h2>Files</h2>
<p><code>$HOME</code>/.yapet</p>
<dl>
<dd>The per-user configuration file. If existing, options are read from this file but can be overridden by the command line options. </p>
<p> Processing of this file can be disabled by invoking <code>yapet</code> with the <code>-i</code> option. </p>
<p> Refer to the <code><a href="/docs/linux/man/5-yapet_config/">yapet_config</a></code>(5) for an explanation of the per-user configuration file.</dl>
<h2>Author</h2>
<p>Rafael Ostertag rafi [at] guengel.ch</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-yapet/">yapet</a></code>(1), <code><a href="/docs/linux/man/5-yapet_config/">yapet_config</a></code>(5)</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2008, 2009, 2010, 2011, 2013, 2014 Rafael Ostertag &lt;rafi [at] guengel.ch&gt;</p>
