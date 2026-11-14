---
title: "abrt-action-save-package-data(5)"
name: "abrt-action-save-package-data"
section: "5"
letter: "a"
url: "/docs/linux/man/5-abrt-action-save-package-data/"
---

abrt-action-save-package-data.conf - Configuration file for abrt-action-save-package-data

<h2>Description</h2>

The <i>abrt-action-save-package-data</i> tool queries RPM database and saves package and component name to problem data. 

 The configuration file consists of items in the format &quot;Option = Value&quot;. A description of each item follows: 

 OpenGPGCheck = <i>yes</i> | <i>no</i>
<dl><dd>When set to <i>yes</i>, <i>abrt</i> will handle only crashes in executables which belong to an installed package with valid GPG signature. The default is <i>yes</i>. The files containing trusted GPG keys which are used to verify the signatures are listed in the gpg_keys.conf configuration file.</dl>
 

 BlackList = <i>packageName</i>, <i>packageName</i> ...
<dl><dd><i>abrt</i> will ignore packages in this list and will not handle their crashes.</dl>
 

 BlackListedPaths = <i>/path/to/ignore/*</i>, <i>*/another/ignored/path*</i> ...
<dl><dd><i>abrt</i> will ignore crashes in executables whose absolute path matches one of specified patterns.</dl>
 

 ProcessUnpackaged = <i>yes</i> | <i>no</i>
<dl><dd>When set to <i>yes</i>, <i>abrt</i> will catch all crashes in the system. When set to <i>no</i>, it will catch crashes only in executables which belong to an installed package. The default is <i>no</i>.</dl>

<h2>See Also</h2>

<a HREF="/docs/linux/man/5-abrt-conf/">abrt.conf</a>(5)

<h2>Authors</h2>

<dl><dd>&bull; ABRT team</dl>
