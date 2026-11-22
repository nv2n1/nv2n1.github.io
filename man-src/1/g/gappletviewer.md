---

title: "gappletviewer(1)"
name: "gappletviewer"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gappletviewer/"
description: "gappletviewer – Load and runs an applet"
---

<p> gappletviewer &#8211; Load and runs an applet </p>
<h2>SYNOPSIS</h2>
<p> appletviewer [<i></i><i>OPTION</i><i></i>]&#8230; <i></i><i>URL</i><i></i>&#8230; </p>
<p> appletviewer [<i></i><i>OPTION</i><i></i>]&#8230; <code>-code</code> <i></i><i>CODE</i><i></i> </p>
<p> appletviewer [<i></i><i>OPTION</i><i></i>]&#8230; <code>-plugin</code> <i></i><i>INPUT</i><i></i>,<i></i><i>OUTPUT</i><i></i></p>
<h2>DESCRIPTION</h2>
<p> The <code>appletviewer</code> tool loads and runs an applet. </p>
<p> Use the first form to test applets specified by tag. The URL should resolve to an HTML document from which the <code>appletviewer</code> will extract applet tags. The APPLET, EMBED and OBJECT tags are supported. If a given document contains multiple applet tags, all the applets will be loaded, with each applet appearing in its own window. Likewise, when multiple URLs are specified, each applet tag instance is given its own window. If a given document contains no recognized tags the <code>appletviewer</code> does nothing. </p>
<pre>
        appletviewer <a rel="nofollow" href="http://www.gnu.org/software/classpath/">http://www.gnu.org/software/classpath/</a>
</pre>
<p> Use the second form to test an applet in development. This form allows applet tag attributes to be supplied on the command line. Only one applet may be specified using the <code>-code</code> option. The <code>-code</code> option overrides the URL form &#8212; any URLs specified will be ignored. </p>
<pre>
        appletviewer -code Test.class -param datafile,data.txt
</pre>
<p> <code>gcjwebplugin</code> uses the third form to communicate with the <code>appletviewer</code> through named pipes.</p>
<h2>OPTIONS</h2>
<p> URL OPTIONS</p>
<dl>
<dt><code>-debug</code></dt>
<dd> This option is not yet implemented but is provided for compatibility.</dd>
<dt><code>-encoding</code> <i></i><i>CHARSET</i><i></i></dt>
<dd> Use this option to specify an alternate character encoding for the specified HTML page.</dd></dl>
<p> APPLET TAG OPTIONS</p>
<dl>
<dt><code>-code</code> <i></i><i>CODE</i><i></i></dt>
<dd> Use the <code>-code</code> option to specify the value of the applet tag <i></i><i>CODE</i><i></i> attribute.</dd>
<dt><code>-codebase</code> <i></i><i>CODEBASE</i><i></i></dt>
<dd> Use the <code>-codebase</code> option to specify the value of the applet tag <i></i><i>CODEBASE</i><i></i> attribute.</dd>
<dt><code>-archive</code> <i></i><i>ARCHIVE</i><i></i></dt>
<dd> Use the <code>-archive</code> option to specify the value of the applet tag <i></i><i>ARCHIVE</i><i></i> attribute.</dd>
<dt><code>-width</code> <i></i><i>WIDTH</i><i></i></dt>
<dd> Use the <code>-width</code> option to specify the value of the applet tag <i></i><i>WIDTH</i><i></i> attribute.</dd>
<dt><code>-height</code> <i></i><i>HEIGHT</i><i></i></dt>
<dd> Use the <code>-height</code> option to specify the value of the applet tag <i></i><i>HEIGHT</i><i></i> attribute.</dd>
<dt><code>-param</code> <i></i><i>NAME</i><i></i><code>,</code><i></i><i>VALUE</i><i></i></dt>
<dd> Use the <code>-param</code> option to specify values for the <i></i><i>NAME</i><i></i> and <i></i><i>VALUE</i><i></i> attributes of an applet PARAM tag.</dd></dl>
<p> PLUGIN OPTION</p>
<dl>
<dt><code>-plugin</code> <i></i><i>INPUT</i><i></i><code>,</code><i></i><i>OUTPUT</i><i></i></dt>
<dd> <code>gcjwebplugin</code> uses the <code>-plugin</code> option to specify the named pipe the <code>appletviewer</code> should use for receiving commands (<i></i><i>INPUT</i><i></i>) and the one it should use for sending commands to <code>gcjwebplugin</code> (<i></i><i>OUTPUT</i><i></i>).</dd></dl>
<p> DEBUGGING OPTION</p>
<dl>
<dt><code>-verbose</code></dt>
<dd> Use the <code>-verbose</code> option to have the <code>appletviewer</code> print debugging messages.</dd></dl>
<p> STANDARD OPTIONS</p>
<dl>
<dt><code>-help</code></dt>
<dd> Use the <code>-help</code> option to have the <code>appletviewer</code> print a usage message, then exit.</dd>
<dt><code>-version</code></dt>
<dd> Use the <code>-version</code> option to have the <code>appletviewer</code> print its version, then exit.</dd>
<dt><code>-J</code><i></i><i>OPTION</i><i></i></dt>
<dd> Use the <code>-J</code> option to pass <i></i><i>OPTION</i><i></i> to the virtual machine that will run the <code>appletviewer</code>. Unlike other options, there must not be a space between the <code>-J</code> and <i></i><i>OPTION</i><i></i>.</dd></dl>
<h2>BUGS</h2>
<h2>SEE ALSO</h2>
<h2>AUTHOR</h2>
