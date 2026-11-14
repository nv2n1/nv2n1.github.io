---
title: "gappletviewer(1)"
name: "gappletviewer"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gappletviewer/"
description: "gappletviewer – Load and runs an applet"
---

<h2 class="name">NAME</h2>
<p> gappletviewer &#8211; Load and runs an applet </p>
<h2>SYNOPSIS</h2>
<p> appletviewer [<i></i><font SIZE="-1"><i>OPTION</i></font><i></i>]&#8230; <i></i><font SIZE="-1"><i>URL</i></font><i></i>&#8230; </p>
<p> appletviewer [<i></i><font SIZE="-1"><i>OPTION</i></font><i></i>]&#8230; <code>-code</code> <i></i><font SIZE="-1"><i>CODE</i></font><i></i> </p>
<p> appletviewer [<i></i><font SIZE="-1"><i>OPTION</i></font><i></i>]&#8230; <code>-plugin</code> <i></i><font SIZE="-1"><i>INPUT</i></font><i></i>,<i></i><font SIZE="-1"><i>OUTPUT</i></font><i></i></p>
<h2>DESCRIPTION</h2>
<p> The <code>appletviewer</code> tool loads and runs an applet. </p>
<p> Use the first form to test applets specified by tag. The <font SIZE="-1">URL</font> should resolve to an <font SIZE="-1">HTML</font> document from which the <code>appletviewer</code> will extract applet tags. The <font SIZE="-1">APPLET</font>, <font SIZE="-1">EMBED</font> and <font SIZE="-1">OBJECT</font> tags are supported. If a given document contains multiple applet tags, all the applets will be loaded, with each applet appearing in its own window. Likewise, when multiple URLs are specified, each applet tag instance is given its own window. If a given document contains no recognized tags the <code>appletviewer</code> does nothing. </p>
<pre>
        appletviewer <a rel="nofollow" href="http://www.gnu.org/software/classpath/">http://www.gnu.org/software/classpath/</a>
</pre>
<p> Use the second form to test an applet in development. This form allows applet tag attributes to be supplied on the command line. Only one applet may be specified using the <code>-code</code> option. The <code>-code</code> option overrides the <font SIZE="-1">URL</font> form &#8212; any URLs specified will be ignored. </p>
<pre>
        appletviewer -code Test.class -param datafile,data.txt
</pre>
<p> <code>gcjwebplugin</code> uses the third form to communicate with the <code>appletviewer</code> through named pipes.</p>
<h2>OPTIONS</h2>
<p> <font SIZE="-1">URL</font> <font SIZE="-1">OPTIONS</font></p>
<dl>
<dt><code>-debug</code></p>
<dd> This option is not yet implemented but is provided for compatibility.</p>
<dt><code>-encoding</code> <i></i><font SIZE="-1"><i>CHARSET</i></font><i></i></p>
<dd> Use this option to specify an alternate character encoding for the specified <font SIZE="-1">HTML</font> page.</dl>
<p> <font SIZE="-1">APPLET</font> <font SIZE="-1">TAG</font> <font SIZE="-1">OPTIONS</font></p>
<dl>
<dt><code>-code</code> <i></i><font SIZE="-1"><i>CODE</i></font><i></i></p>
<dd> Use the <code>-code</code> option to specify the value of the applet tag <i></i><font SIZE="-1"><i>CODE</i></font><i></i> attribute.</p>
<dt><code>-codebase</code> <i></i><font SIZE="-1"><i>CODEBASE</i></font><i></i></p>
<dd> Use the <code>-codebase</code> option to specify the value of the applet tag <i></i><font SIZE="-1"><i>CODEBASE</i></font><i></i> attribute.</p>
<dt><code>-archive</code> <i></i><font SIZE="-1"><i>ARCHIVE</i></font><i></i></p>
<dd> Use the <code>-archive</code> option to specify the value of the applet tag <i></i><font SIZE="-1"><i>ARCHIVE</i></font><i></i> attribute.</p>
<dt><code>-width</code> <i></i><font SIZE="-1"><i>WIDTH</i></font><i></i></p>
<dd> Use the <code>-width</code> option to specify the value of the applet tag <i></i><font SIZE="-1"><i>WIDTH</i></font><i></i> attribute.</p>
<dt><code>-height</code> <i></i><font SIZE="-1"><i>HEIGHT</i></font><i></i></p>
<dd> Use the <code>-height</code> option to specify the value of the applet tag <i></i><font SIZE="-1"><i>HEIGHT</i></font><i></i> attribute.</p>
<dt><code>-param</code> <i></i><font SIZE="-1"><i>NAME</i></font><i></i><code>,</code><i></i><font SIZE="-1"><i>VALUE</i></font><i></i></p>
<dd> Use the <code>-param</code> option to specify values for the <i></i><font SIZE="-1"><i>NAME</i></font><i></i> and <i></i><font SIZE="-1"><i>VALUE</i></font><i></i> attributes of an applet <font SIZE="-1">PARAM</font> tag.</dl>
<p> <font SIZE="-1">PLUGIN</font> <font SIZE="-1">OPTION</font></p>
<dl>
<dt><code>-plugin</code> <i></i><font SIZE="-1"><i>INPUT</i></font><i></i><code>,</code><i></i><font SIZE="-1"><i>OUTPUT</i></font><i></i></p>
<dd> <code>gcjwebplugin</code> uses the <code>-plugin</code> option to specify the named pipe the <code>appletviewer</code> should use for receiving commands (<i></i><font SIZE="-1"><i>INPUT</i></font><i></i>) and the one it should use for sending commands to <code>gcjwebplugin</code> (<i></i><font SIZE="-1"><i>OUTPUT</i></font><i></i>).</dl>
<p> <font SIZE="-1">DEBUGGING</font> <font SIZE="-1">OPTION</font></p>
<dl>
<dt><code>-verbose</code></p>
<dd> Use the <code>-verbose</code> option to have the <code>appletviewer</code> print debugging messages.</dl>
<p> <font SIZE="-1">STANDARD</font> <font SIZE="-1">OPTIONS</font></p>
<dl>
<dt><code>-help</code></p>
<dd> Use the <code>-help</code> option to have the <code>appletviewer</code> print a usage message, then exit.</p>
<dt><code>-version</code></p>
<dd> Use the <code>-version</code> option to have the <code>appletviewer</code> print its version, then exit.</p>
<dt><code>-J</code><i></i><font SIZE="-1"><i>OPTION</i></font><i></i></p>
<dd> Use the <code>-J</code> option to pass <i></i><font SIZE="-1"><i>OPTION</i></font><i></i> to the virtual machine that will run the <code>appletviewer</code>. Unlike other options, there must not be a space between the <code>-J</code> and <i></i><font SIZE="-1"><i>OPTION</i></font><i></i>.</dl>
<h2>BUGS</h2>
<h2>SEE ALSO</h2>
<h2>AUTHOR</h2>
<h2>Index</h2>
