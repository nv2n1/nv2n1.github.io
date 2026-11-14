---
title: "stdexperimentalfilesystemfile_statuspermissions(3)"
name: "stdexperimentalfilesystemfile_statuspermissions"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalfilesystemfile_statuspermissions/"
description: "std::experimental::filesystem::file_status::permissions – std::experimental::filesystem::file_status::permissions"
---

<p>std::experimental::filesystem::file_status::permissions &#8211; std::experimental::filesystem::file_status::permissions</p>
<h2>Synopsis</h2>
<p>perms permissions() const; <code>(1)</code> (filesystem TS)<br />
void permissions( perms perm ); <code>(2)</code> (filesystem TS)<br />
Accesses the file permissions information.<br />
1) Returns file permissions information.<br />
2) Sets file type to perm. </p>
<h2>Parameters</h2>
<p>perm &#8211; file permissions to set to</p>
<h2>Return value</h2>
<p>1) File permissions information.<br />
2) <i>(none)</i> </p>
<h2>Exceptions</h2>
<p>noexcept specification:<br />
noexcept</p>
