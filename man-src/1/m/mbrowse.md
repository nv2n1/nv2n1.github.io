---
title: "mbrowse(1)"
name: "mbrowse"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mbrowse/"
description: "mbrowse – SNMP MIB browser and query tool"
---

<h2 class="name">NAME</h2>
<p> mbrowse &#8211; SNMP MIB browser and query tool </p>
<h2>SYNOPSIS</h2>
<p> <code>mbrowse</code></p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>mbrowse</code> command. This manual page was written for the Debian distribution because the original program does not have a manual page. </p>
<p> <code>mbrowse</code> is a SNMP MIB browser tool. It relies on GTK+ and net-snmp. It is able to display as a tree view the content of a MIB, and to query MIB objects on any machine through get, set and walk methods. </p>
<p> It includes a search function, bookmarking of MIB entries, ability to support additional MIBs, &#8230; </p>
<p> Once mbrowse is open, it displays the MIB tree. You can browse this tree like any other one. Once you have selected a MIB object, you can get details about it by going in the <i>Details</i> page. Its SNMP identifier is also update on the fly in the <i>Object Identifier</i> field. You can also directly enter the object identifier, and the tree will be browsed to the right place. </p>
<p> To query a SNMP object, select it, enter the host name (IP address or DNS entry) of the machine you want to query in the right field. Also enter the read community to <i>get</i> or <i>walk</i> a value, and the write community to <i>set</i> it. Click on the right button and the objects and their values will be displayed. </p>
<p> By clicking the <i>Search</i> page, you can search MIb entries by MIB name or description. </p>
<p> In the <i>Options</i> page, you can set a few general options: whether to save the session on exit of the program, set the style of the tree view, the version of SNMP to use, and a few SNMP-related values. </p>
<p> You can also use bookmarks to quickly find SNMP objects. Select the object you want to save, and click on <i>Add Bookmark</i> in the <i>Bookmark</i> menu. You will be prompted a name and the bookmark will be added to the menu. You can now click it to be positioned on the object back. To delete a bookmark, click on <i>Delete Bookmark</i>, and then, click on the bookmark to delete. </p>
<p> You can also import MIBs at runtime, by clicking <i>Open MIB</i> in the <i>File</i> menu. Select the MIB file in the dialog box and the values contained in the file will be integrated in the tree view. For this MIB to be automatically opened at startup, you must put the MIB file in net-nsmp MIB files directory (usually <i>/usr/share/snmp/mibs</i> on Debian [and also on Fedora]). Mbrowse will open the MIB at its next startup. </p>
<h2>OPTIONS</h2>
<p> This program takes no options</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-snmpget/">snmpget</a></code>(1), <code><a href="/docs/linux/man/1-snmpwalk/">snmpwalk</a></code>(1). <code><a href="/docs/linux/man/1-snmpset/">snmpset</a></code>(1).</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Clément Stenac &lt;zorglub [at] via.ecp.fr&gt;, for the Debian GNU/Linux project (but may be used by others). </p>
<p> Added comment on MIB path for Fedora and removed two typos &#8212; Volker Fröhlich &lt;volker27 [at] gmx.at&gt; </p>
<p> mbrowse was written by Aaron Hodgen </p>
<h2>Index</h2>
