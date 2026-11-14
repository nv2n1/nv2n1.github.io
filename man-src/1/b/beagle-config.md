---
title: "beagle-config(1)"
name: "beagle-config"
section: "1"
letter: "b"
url: "/docs/linux/man/1-beagle-config/"
description: "beagle-config – command-line interface to Beagle configuration"
---

<h2>NAME</h2>
<p> beagle-config &#8211; command-line interface to Beagle configuration</p>
<h2>SYNOPSIS</h2>
<p> <code>beagle-config</code> <i>options</i><br />
 <code>beagle-config</code> <i>sections</i><br />
 <code>beagle-config</code> <i>sections</i> <i>section-options</i> [<i>params</i>]<br />
 <code>beagle-config</code> <i>xml-options</i></p>
<h2>DESCRIPTION</h2>
<p> <code>beagle-config</code> is a command line tool designed to manipulate the Beagle configuration. </p>
<p> The configuration is stored in a series of files usually located in the <code>~/.beagle/config</code> directory. The configuration is split up into <i>sections</i>, each section being represented by 1 file. </p>
<p> The format used is the result of serialized objects. Manually modifying the configuration files is not recommended, you should use this utility instead. You can also the graphical interfaces beagle-settings (Gtk) or beagle-settings-qt (Qt4). </p>
<p> Each <i>section</i> configures a different area of the Beagle system. Each section has a number of preset <i>section-options</i> (commands) which you can perform on it via this command-line application. </p>
<p> The available sections, and available options for each section, are discovered at runtime. This manual does not attempt to document the sections in detail. This manual demonstrates how you can retrieve a list of available sections and their options. </p>
<p> <i>beagle-config</i> can be used &quot;offline&quot;, it does not require a Beagle daemon to be running for most operations. If a Beagle daemon is running, it will immediately be notified of any configuration changes, and your new settings will come into effect almost immediately. Alternatively, you can force a re-load with the <code>&#8211;beagled-reload-config</code> argument.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help </code></p>
<dd> Print a brief copyright and usage message.</p>
<dt><code>&#8211;beagled-reload-config</code></p>
<dd> Asks the beagle daemon to reload the configuration files.</p>
<dt><code>&#8211;list-sections</code></p>
<dd> Lists all of the available sections for use as the <i>sections</i> parameter.</p>
<dt><code>&#8211;version</code></p>
<dd> Print version information.</dl>
<h2>SECTION OPTIONS</h2>
<p> Each section has its own unique set of options available. To see a list of supported options for a particular section, run <code>beagle-config section-name</code> with no additional parameters. Note that some of the options are strictly for internal usage by beagle and should not be modified by the user.</p>
<h2>PARAMS</h2>
<p> To read the value of section-option, you do not need to give any params. Of course you need to supply params if you want to set a section-option. There are 3 types of section options. The params depend on the type of the section-option.</p>
<dl>
<dt><i>boolean option</i></p>
<dd> PARAMS is &quot;true&quot; or &quot;false&quot;</p>
<dt><i>string option</i></p>
<dd> PARAMS is the value of the section-option.</p>
<dt><i>list option</i></p>
<dd> To add a list option, pass a comma separated list of options <i>value1,value2,&#8230;.</i> Run <code>beagle-config section-name section-option</code> for the number of items in the list and their explanations.<br />
 To remove a list option, pass <i>&#8211; value1,value2,&#8230;</i> where value1,value2,&#8230; are the exact values of the option that you want to remove.</dl>
<h2>XML OPTIONS</h2>
<p> Non-C# programs who want to get/set configuration values can use these options. If an error occurs, the return value can be checked to determine the kind of the error. The return value is</p>
<dl>
<dt>1: Bad section name</p>
<dd>
<dt>2: Invalid XML</p>
<dd>
<dt>3: XML does not correspond to the section name</p>
<dd></dl>
<h3>Options</h3>
<dl>
<dt><code>&#8211;read-xml SECTION</code></p>
<dd> Reads the xml of a section from stdin. Suitable for setting options by other programs.</p>
<dt><code>&#8211;write-xml SECTION</code></p>
<dd> Print the section in xml format. Suitable for parsing by other programs.</dl>
<h2>AUTHOR</h2>
<p> Originally written by Daniel Drake &lt;dsd [at] gentoo.org&gt;. Modified by D Bera &lt;dbera.web [at] gmail.com&gt;</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;dashboard-hackers [at] gnome.org&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2005 Novell, Inc., &#169; 2008 D Bera </p>
<p> This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-beagled/">beagled</a></code>(1) </p>
<h2>Index</h2>
