---
title: "gresource(1)"
name: "gresource"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gresource/"
description: "gresource – GResource tool"
---

<h2 class="name">NAME</h2>
<p> gresource &#8211; GResource tool </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>gresource</code> [&#8211;section&nbsp;<i>SECTION</i>] list <i>FILE</i> [<i>PATH</i>]</dt>
<dt> <code>gresource</code> [&#8211;section&nbsp;<i>SECTION</i>] details <i>FILE</i> [<i>PATH</i>]</dt>
<dt> <code>gresource</code> [&#8211;section&nbsp;<i>SECTION</i>] extract <i>FILE</i> <i>PATH</i></dt>
<dt> <code>gresource</code> sections <i>FILE</i></dt>
<dt> <code>gresource</code> help [<i>COMMAND</i>]</dt></dl>
<h2>DESCRIPTION</h2>
<p> <code>gresource</code></p>
<dd>offers a simple commandline interface to <code>GResource</code>. It lets you list and extract resources that have been compiled into a resource file or included in an elf file (a binary or a shared library). </dd>
<p> The file to operate on is specified by the <i>FILE</i> argument. </p>
<p> If an elf file includes multiple sections with resources, it is possible to select which one to operate on with the &#8211;section option. Use the sections command to find available sections.</p>
<h2>COMMANDS</h2>
<p> <code>list</code></p>
<dl>
<dt>
</dt><dd> Lists resources. If <i>SECTION</i> is given, only list resources in this section. If <i>PATH</i> is given, only list matching resources.</dd></dl>
<p> <code>details</code></p>
<dl>
<dt>
</dt><dd> Lists resources with details. If <i>SECTION</i> is given, only list resources in this section. If <i>PATH</i> is given, only list matching resources. Details include the section, size and compression of each resource.</dd></dl>
<p> <code>extract</code></p>
<dl>
<dt>
</dt><dd> Extracts the resource named by <i>PATH</i> to stdout. Note that resources may contain binary data.</dd></dl>
<p> <code>sections</code></p>
<dl>
<dt>
</dt><dd> Lists sections containing resources. This is only interesting if <i>FILE</i> is an elf file.</dd></dl>
<p> <code>help</code></p>
<dl>
<dt>
</dt><dd> Prints help and exits.</dd></dl>
<h2>Index</h2>
