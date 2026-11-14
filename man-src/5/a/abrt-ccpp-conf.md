---
title: "abrt-ccpp-conf(5)"
name: "abrt-ccpp-conf"
section: "5"
letter: "a"
url: "/docs/linux/man/5-abrt-ccpp-conf/"
description: "abrt-CCpp.conf – Configuration file for ABRT’s core dump crash hook"
---

<p>abrt-CCpp.conf &#8211; Configuration file for ABRT&#8217;s core dump crash hook</p>
<h2>Description</h2>
<p>The configuration file consists of items in the format &quot;Option = Value&quot;. Ithe following items are recognized: </p>
<p> MakeCompatCore = <i>yes</i> / <i>no</i> &#8230;</p>
<dl>
<dd>CCpp hook writes its template to the &quot;/proc/sys/kernel/core_pattern&quot; file and stores the original template in the &quot;/var/run/abrt/saved_core_pattern&quot; file. If you want CCpp hook to create a core dump file named according to the original template as well, set <i>MakeCompatCore</i> to <i>yes</i>. If the original template string starts with &quot;|&quot;, the string &quot;core&quot; is used instead of the template. For more information about naming core dump files see <i>man 5 core</i>.</dl>
<p> SaveBinaryImage = <i>yes</i> / <i>no</i> &#8230;</p>
<dl>
<dd>Do you want a copy of crashed binary be saved? Useful, for example, when <i>deleted binary</i> segfaults. Default is <i>no</i>.</dl>
<p> CreateCoreBacktrace = <i>yes</i> / <i>no</i> &#8230;</p>
<dl>
<dd>When this option is set to <i>yes</i>, core backtrace is generated from the memory image of the crashing process. Only the crash thread is present in the backtrace. Default is <i>no</i>.</dl>
<p> SaveFullCore = <i>yes</i> / <i>no</i> &#8230;</p>
<dl>
<dd>Save full coredump? If set to <i>no</i>, coredump won&#8217;t be saved and you won&#8217;t be able to report the crash to Bugzilla. Only useful with <i>CreateCoreBacktrace</i> set to <i>yes</i>. Please note that if this option is set to <i>no</i> and MakeCompatCore is set to <i>yes</i>, the core is still written to the current directory. Default is <i>yes</i>.</dl>
<p> IgnoredPaths = /path/to/ignore/<code>, */another/ignored/path</code> &#8230;</p>
<dl>
<dd>ABRT will ignore crashes in executables whose absolute path matches one of specified patterns.</dl>
<p> AllowedUsers = root, &#8230;</p>
<dl>
<dd>ABRT will process only crashes of either allowed users <i>AllowedUsers</i> or users who are members of allowed group <i>AllowedGroups</i>. If no allowed users nor allowed group are specified ABRT will process crashes of all users.</dl>
<p> AllowedGroups = root, &#8230;</p>
<dl>
<dd>ABRT will process only crashes of either allowed users <i>AllowedUsers</i> or users who are members of allowed group <i>AllowedGroups</i>. If no allowed users nor allowed group are specified ABRT will process crashes of all users.</dl>
<p> VerboseLog = NUM</p>
<dl>
<dd>Used to make the hook more verbose</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/5-abrt-conf/">abrt.conf</a>(5) <a href="/docs/linux/man/1-abrt-action-generate-core-backtrace/">abrt-action-generate-core-backtrace</a>(1)</p>
<h2>Authors</h2>
<dl>
<dd>&bull; ABRT team</dl>
