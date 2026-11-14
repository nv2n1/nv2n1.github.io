---
title: "snmpconf(1)"
name: "snmpconf"
section: "1"
letter: "s"
url: "/docs/linux/man/1-snmpconf/"
description: "snmpconf – creates and modifies SNMP configuration files"
---

<h2>NAME</h2>
<p> snmpconf &#8211; creates and modifies SNMP configuration files</p>
<h2>SYNOPSIS</h2>
<p> <code>snmpconf</code> [OPTIONS] [fileToCreate]</p>
<dl>
<dt>Start with:</p>
<dd> <code>snmpconf</code> -g basic_setup</p>
<dt>Or even just:</p>
<dd> <code>snmpconf</code></dl>
<h2>DESCRIPTION</h2>
<p> <code>snmpconf</code> is a simple Perl script that walks you through setting up a configuration file step by step. It should be fairly straight forward to use. Merely run it and answer its questions. </p>
<p> In its default mode of operation, it prompts the user with menus showing sections of the various configuration files it knows about. When the user selects a section, a sub-menu is shown listing of the descriptions of the tokens that can be created in that section. When a description is selected, the user is prompted with questions that construct the configuration line in question. </p>
<p> Finally, when the user quits the program any configuration files that have been edited by the user are saved to the local directory, fully commented. </p>
<p> A particularly useful option is the <code>-g</code> switch, which walks a user through a specific set of configuration questions. Run:</p>
<dl>
<dt>
<dd>
<p> snmpconf -g basic_setup</dl>
<p> for an example.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f</code></p>
<dd> Force overwriting existing files in the current directory without prompting the user if this is a desired thing to do.</p>
<dt><code>-i</code></p>
<dd> When finished, install the files into the location where the global system commands expect to find them.</p>
<dt><code>-p</code></p>
<dd> When finished, install the files into the users home directory&#8217;s .snmp subdirectory (where the applications will also search for configuration files).</p>
<dt><code>-I</code><i> DIRECTORY</i></p>
<dd> When finished, install the files into the directory <i>DIRECTORY</i>.</p>
<dt><code>-a</code></p>
<dd> Don&#8217;t ask any questions. Simply read in the various known configuration files and write them back out again. This has the effect of &quot;auto-commenting&quot; the configuration files for you. See the <code>NEAT TRICKS</code> section below.</p>
<dt><code>-r</code><i>all|none</i></p>
<dd> Read in either all or none of the found configuration files. Normally <code>snmpconf</code> prompts you for which files you wish to read in. Reading in these configuration files will merge these files with the results of the questions that it asks of you.</p>
<dt><code>-R</code><i> FILE,&#8230;</i></p>
<dd> Read in a specific list of configuration files.</p>
<dt><code>-g</code><i> GROUPNAME</i></p>
<dd> Groups of configuration entries can be created that can be used to walk a user through a series of questions to create an initial configuration file. There are no menus to navigate, just a list of questions. Run:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> snmpconf -g basic_setup</dl>
<p> for a good example.</dl>
<dt><code>-G</code></p>
<dd> List all the known groups.</p>
<dt><code>-c</code><i> CONFIGDIR</i></p>
<dd> <code>snmpconf</code> uses a directory of configuration information to learn about the files and questions that it should be asking. This option tells <code>snmpconf</code> to use a different location for configuring itself.</p>
<dt><code>-q</code></p>
<dd> Run slightly more quietly. Since this is an interactive program, I don&#8217;t recommend this option since it only removes information from the output that is designed to help you.</p>
<dt><code>-d</code></p>
<dd> Turn on <code>lots</code> of debugging output.</p>
<dt><code>-D</code></p>
<dd> Add <code>even more</code> debugging output in the form of Perl variable dumps.</p>
<dt>
<dd></dl>
<h2>NEAT TRICKS</h2>
<dl>
<dt>snmpconf -g basic_setup</p>
<dd> Have I mentioned this command enough yet? It&#8217;s designed to walk someone through an initial setup for the <i><a href="/docs/linux/man/8-snmpd/">snmpd</a>(8)</i> daemon. Really, you should try it.</p>
<dt>snmpconf -R /usr/local/snmp/snmpd.conf -a -f snmpd.conf</p>
<dd> Automatically reads in an snmpd.conf file (for example) and adds comments to them describing what each token does. Try it. It&#8217;s cool.</dl>
<h2>NOTES</h2>
<p> <code>snmpconf</code> is actually a very generic utility that could be easily configured to help construct just about any kind of configuration file. Its default configuration set of files are SNMP based.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/8-snmpd/">snmpd</a>(8), <a href="/docs/linux/man/5-snmp_config/">snmp_config</a>(5), <a href="/docs/linux/man/5-snmp-conf/">snmp.conf</a>(5), <a href="/docs/linux/man/5-snmpd-conf/">snmpd.conf</a>(5) </p>
<h2>Index</h2>
