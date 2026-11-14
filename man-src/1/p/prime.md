---
title: "prime(1)"
name: "prime"
section: "1"
letter: "p"
url: "/docs/linux/man/1-prime/"
description: "Prime – a file manager for GNU/Linux console/xterm"
---

<h2>NAME</h2>
<p> Prime &#8211; a file manager for GNU/Linux console/xterm</p>
<h2>SYNOPSIS</h2>
<p> <code>Prime [log-file-name] [OPTIONS]</code></p>
<h2>DESCRIPTION</h2>
<p> About The Prime<br />
 ===============<br />
 Prime is a GNU software, part of the GnuDOS package. Prime is a file manager which works under the GNU/Linux console. It was influenced by other file managers (like the well known XTree Gold which was popular under MS-DOS). It provides a user friendly interface with menus, shortcuts, and key navigation. It is distributed as part of the GnuDOS package which was developed to help users coming from DOS-like environments feel ease when dealing with the GNU system. Prime provides multi-level experience, the level of complexity can be adjusted by the user: you want to use DOS-keys with a few basic GNU ones? you want to go with the full power of the GNU system? All are options that are provided by the six levels of experience of Prime: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>1- Newbie: All DOS shortcut keys, no GNU keys yet<br />
&nbsp;<wbr>&nbsp;<wbr>2- Novice: DOS shortcut keys, some of which are replaced with GNU&#8217;s<br />
&nbsp;<wbr>&nbsp;<wbr>3- Intermediate: DOS keys with a few more replaced with GNU keys<br />
&nbsp;<wbr>&nbsp;<wbr>4-&nbsp;<wbr>ِAdvanced: &#8230; And more GNU keys in<br />
&nbsp;<wbr>&nbsp;<wbr>5-&nbsp;<wbr>ِExpert: Very few DOS keys, most are GNU keys<br />
&nbsp;<wbr>&nbsp;<wbr>6-&nbsp;<wbr>ِVeteran: Only GNU keys, no DOS-like keys<br />
&nbsp;<wbr>&nbsp;<wbr> You start with level 1 by default. To set your level, call the mino with &#8216;&#8211;levelX&#8217; or &#8216;-lX&#8217; options, </p>
<p> Which keys are defined for which level?<br />
 =======================================<br />
 There is a table showing the DOS-like key combinations along with their respective GNU key bindings in the README file installed with this package. To read more about the levels of experience and the keybindings, please refer to the README file under prime&#8217;s help menu. </p>
<h2>OPTIONS</h2>
<dl>
<dt>&#8211;export, -e dirname filename</p>
<dd> Export directory tree of &#8216;dirname&#8217; into text file named &#8216;filename&#8217; without starting the file manager </p>
<dt>&#8211;log, -g log-file-name</p>
<dd> Provide a file to use for writing log information. The program uses ~/prime.log by default </p>
<dt>&#8211;level X, -l X</p>
<dd> The GNU DOS experience level to be used. Can be 1-6, defaults to 1. See above text for details </p>
<dt>&#8211;no-log, -n</p>
<dd> Do not output log information </p>
<dt>&#8211;reset-config, -r</p>
<dd> Reset the configuration file to its defaults </p>
<dt>&#8211;help, -h</p>
<dd> Print command line help, including short instructions on the command line options, without starting the program </p>
<dt>&#8211;version, -v</p>
<dd> Show program version </p>
<dt>dirname</p>
<dd> Load the directory tree of &#8216;dirname&#8217; into Prime on startup </p>
</dl>
<h2>FILES</h2>
<p> <i>~/prime.log</i> The default file used for log. User can override this by providing another file name as an argument to the program</p>
<h2>TODO</h2>
<p> &#8211; Add mouse support<br />
 &#8211; Add printing functionality</p>
<h2>SEE ALSO</h2>
<p> info prime, info gnudos</p>
<h2>AUTHOR</h2>
<p> Mohammed Isam &lt;mohammed_isam1984 [at] yahoo.com&gt; </p>
<h2>Index</h2>
