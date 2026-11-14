---
title: "flatpak-document-export(1)"
name: "flatpak-document-export"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flatpak-document-export/"
description: "flatpak-document-export – Export a file to a sandboxed application"
---

<h2 class="name">NAME</h2>
<p> flatpak-document-export &#8211; Export a file to a sandboxed application </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>flatpak document-export</code> [OPTION&#8230;] FILE</dl>
<h2>DESCRIPTION</h2>
<dd>Creates a document id for a local file that can be exposed to sandboxed applications, allowing them access to files that they would not otherwise see. The exported files are exposed in a fuse filesystem at /run/user/$UID/doc/. </p>
<p> This command also lets you modify the per-application permissions of the documents, granting or revoking access to the file on a per-application basis.</p>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show help options and exit.</dl>
<p> <code>-u</code>, <code>&#8211;unique</code></p>
<dl>
<dt>
<dd> Don&#8217;t reuse an existing document id for the file. This makes it safe to later remove the document when you&#8217;re finished with it.</dl>
<p> <code>-t</code>, <code>&#8211;transient</code></p>
<dl>
<dt>
<dd> The document will only exist for the length of the session. This is useful for temporary grants.</dl>
<p> <code>-n</code>, <code>&#8211;noexist</code></p>
<dl>
<dt>
<dd> Don&#8217;t require the file to exist already.</dl>
<p> <code>-a</code>, <code>&#8211;app=APPID</code></p>
<dl>
<dt>
<dd> Grant read access to the specified application. The <code>&#8211;allow</code> and <code>&#8211;forbid</code> options can be used to grant or remove additional privileges. This option can be used multiple times.</dl>
<p> <code>-r</code>, <code>&#8211;allow-read</code></p>
<dl>
<dt>
<dd> Grant read access to the applications specified with <code>&#8211;app</code>. This defaults to TRUE.</dl>
<p> <code>&#8211;forbid-read</code></p>
<dl>
<dt>
<dd> Revoke read access for the applications specified with <code>&#8211;app</code>.</dl>
<p> <code>-w</code>, <code>&#8211;allow-write</code></p>
<dl>
<dt>
<dd> Grant write access to the applications specified with <code>&#8211;app</code>.</dl>
<p> <code>&#8211;forbid-write</code></p>
<dl>
<dt>
<dd> Revoke write access for the applications specified with <code>&#8211;app</code>.</dl>
<p> <code>-d</code>, <code>&#8211;allow-delete</code></p>
<dl>
<dt>
<dd> Grant the ability to remove the document from the document portal to the applications specified with <code>&#8211;app</code>.</dl>
<p> <code>&#8211;forbid-delete</code></p>
<dl>
<dt>
<dd> Revoke the ability to remove the document from the document portal from the applications specified with <code>&#8211;app</code>.</dl>
<p> <code>-g</code>, <code>&#8211;allow-grant-permission</code></p>
<dl>
<dt>
<dd> Grant the ability to grant further permissions to the applications specified with <code>&#8211;app</code>.</dl>
<p> <code>&#8211;forbid-grant-permission</code></p>
<dl>
<dt>
<dd> Revoke the ability to grant further permissions for the applications specified with <code>&#8211;app</code>.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Print debug information during command processing.</dl>
<p> <code>&#8211;ostree-verbose</code></p>
<dl>
<dt>
<dd> Print OSTree debug information during command processing.</dl>
<h2>EXAMPLES</h2>
<p> <code>$ flatpak document-export &#8211;app=org.gnome.gedit ~/test.txt</code> </p>
<dl>
<dt>
<dd>
<pre>
/run/user/1000/doc/e52f9c6a/test.txt
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flatpak/">flatpak</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-document-unexport/">flatpak-document-unexport</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-document-info/">flatpak-document-info</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-documents/">flatpak-documents</a></code>(1) </p>
<h2>Index</h2>
