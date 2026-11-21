---
title: "scpr(1)"
name: "scpr"
section: "1"
letter: "s"
url: "/docs/linux/man/1-scpr/"
---

<h2 class="name">NAME</h2>
 

 scpr - The scpr program is used to print out objects in checkpoint files.

<h2>Running scpr</h2>

 

 

 scpr takes the following command line options followed by a list of files. 

<dl>
<dt>-o <i>val</i>
</dt><dd> Print the object with the name val. Object names take the form '&lt;classname&gt;:&lt;ordinal_number&gt;'. At least one file and object name must be given.
</dd><dt>-memorygrp <i>val</i>
</dt><dd> Which memory group to use.
</dd><dt>-threadgrp <i>val</i>
</dt><dd> Which thread group to use.
</dd><dt>-messagegrp <i>val</i>
</dt><dd> Which message group to use.
</dd><dt>-W <i>val</i>
</dt><dd> Set the working directory.
</dd><dt>-d
</dt><dd> Turn on debugging.
</dd><dt>-v
</dt><dd> Print the version.
</dd><dt>-w
</dt><dd> Print the warranty.
</dd><dt>-L
</dt><dd> Print the license.
</dd><dt>-h
</dt><dd> Print this help.</dd></dl>
 

 

<h2>License</h2>

 

 

 scpr is open-source software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. 

<h2>Warranty</h2>

 

 

 scpr is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
