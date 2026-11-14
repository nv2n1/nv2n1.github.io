---
title: "mino(1)"
name: "mino"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mino/"
description: "Mino – a user friendly text editor for GNU/Linux console/xterm"
---

<h2>NAME</h2>
<p> Mino &#8211; a user friendly text editor for GNU/Linux console/xterm</p>
<h2>SYNOPSIS</h2>
<p> <code>mino [file-name] [&#8211;help, -h] [&#8211;reset-config]</code></p>
<h2>DESCRIPTION</h2>
<p> About The mino editor Mino is a GNU software, part of the GnuDOS package. Mino is a text file editor for use with the GNU/Linux console/xterm. The idea was to provide a text editor that is user friendly and easy to use for those who came from DOS land. Having accustomed to SHIFT selecting text, using CTRL-shortcut keys and so on makes it hard for a regular Joe to dive in head first into GNU syntax. Mino provides multi-level experience, the level of complexity can be adjusted by the user: you want to use DOS-keys with a few basic GNU ones? you want to go with the full power of the GNU system? All are options that are provided by the six levels of experience of Mino: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>1- Newbie: All DOS shortcut keys, no GNU keys yet<br />
&nbsp;<wbr>&nbsp;<wbr>2- Novice: DOS shortcut keys, some of which are replaced with GNU&#8217;s<br />
&nbsp;<wbr>&nbsp;<wbr>3- Intermediate: DOS keys with a few more replaced with GNU keys<br />
&nbsp;<wbr>&nbsp;<wbr>4-&nbsp;<wbr>ِAdvanced: &#8230; And more GNU keys in<br />
&nbsp;<wbr>&nbsp;<wbr>5-&nbsp;<wbr>ِExpert: Very few DOS keys, most are GNU keys<br />
&nbsp;<wbr>&nbsp;<wbr>6-&nbsp;<wbr>ِVeteran: Only GNU keys, no DOS-like keys<br />
&nbsp;<wbr>&nbsp;<wbr> You start with level 1 by default. To set your level, call the mino with &#8216;&#8211;levelX&#8217; or &#8216;-lX&#8217; options, </p>
<p> Which keys are defined for which level?<br />
 =======================================<br />
 There is a table showing the DOS-like key combinations along with their respective GNU key bindings in the README file installed with this package. To read more about the levels of experience and the keybindings, please refer to the README file, accessible from the Help menu in mino. </p>
<h2>OPTIONS</h2>
<dl>
<dt>&#8211;reset-config</p>
<dd> To reset the configuration file</p>
<dt>&#8211;help, -h</p>
<dd> Print command line help, including short instructions on the command line options, without starting the program</p>
<dt>&#8211;version, -v</p>
<dd> Show program version</p>
<dt>&#8211;levelX, -lX</p>
<dd> Set the level of experience, where X is a number in the range 1 to 6</p>
<dt>file-name</p>
<dd> If you want to load a file into mino on program startup</dl>
<h2>FILES</h2>
<p> <i>~/.mino.conf</i> The default file used to store mino&#8217;s configuration. It can be edited manually, but this is not advisable. Use mino Options menu to change program preferences</p>
<h2>TODO</h2>
<p> &#8211; Add mouse support<br />
 &#8211; Add printing functionality<br />
 &#8211; Add more syntax highlighting options</p>
<h2>SEE ALSO</h2>
<p> info mino, info gnudos</p>
<h2>AUTHOR</h2>
<p> Mohammed Isam &lt;mohammed_isam1984 [at] yahoo.com&gt; </p>
<h2>Index</h2>
