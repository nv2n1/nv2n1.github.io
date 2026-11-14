---
title: "apparmor-d(5)"
name: "apparmor-d"
section: "5"
letter: "a"
url: "/docs/linux/man/5-apparmor-d/"
description: "apparmor.d – syntax of security profiles for AppArmor."
---

<p>apparmor.d &#8211; syntax of security profiles for AppArmor.</p>
<h2>Description</h2>
<p>AppArmor profiles describe mandatory access rights granted to given programs and are fed to the AppArmor policy enforcement module using <code><a href="/docs/linux/man/8-apparmor_parser/">apparmor_parser</a></code>(8). This man page describes the format of the AppArmor configuration files; see <code><a href="/docs/linux/man/7-apparmor/">apparmor</a></code>(7) for an overview of AppArmor.</p>
<h2>Format</h2>
<p>AppArmor policy is written in a declarative language, in which the order of rules within a given section or block does not matter. Policy is by convention written so that it is contained in multiple files, but this is not a requirement. It could just as easily be written in a single file. The policy language is compiled to a architecture independent binary format that is loaded into the kernel for enforcement. </p>
<p> The base unit of AppArmor confinement is the profile. It contains a set of rules which are enforced when the profile is associated with a running program. The rules within the profile provide a whitelist of different permission that are allowed, along with a few other special rules. </p>
<p> The text in AppArmor policy is split into two sections, the preamble and the profile definitions. The preamble must occur at the head of the file and once profile definitions begin, no more preamble rules are allowed (even in files that are included into the profile). When AppArmor policy (set of profiles) is split across multiple files, each file can have its own preamble section, which may be the same or different from other files preamble. Files included within a profile section can not have a preamble section. </p>
<p> The following is a BNF-style description of AppArmor policy configuration files; see below for an example AppArmor policy file. AppArmor configuration files are line-oriented; <code>#</code> introduces a comment, similar to shell scripting languages. The exception to this rule is that <code>#include</code> will <i>include</i> the contents of a file inline to the policy; this behaviour is modelled after <code><a href="/docs/linux/man/1-cpp/">cpp</a></code>(1). </p>
<dl>
<dd><font SIZE="-1"><code>PROFILE FILE</code></font> = ( [ <i></i><font SIZE="-1"><i>PREAMBLE</i></font><i></i> ] [ <i></i><font SIZE="-1"><i>PROFILE</i></font><i></i> ] )* </p>
<p> <font SIZE="-1"><code>PREAMBLE</code></font> = ( <i></i><font SIZE="-1"><i>COMMENT</i></font><i></i> | <i></i><font SIZE="-1"><i>VARIABLE ASSIGNMENT</i></font><i></i> | <i></i><font SIZE="-1"><i>ALIAS RULE</i></font><i></i> | <i></i><font SIZE="-1"><i>INCLUDE</i></font><i></i> | <i></i><font SIZE="-1"><i>ABI</i></font><i></i> )*<br />
&nbsp;<wbr>&nbsp;Variable assignment and alias rules must come before the profile. </p>
<p> <font SIZE="-1"><code>VARIABLE ASSIGNMENT</code></font> = <i></i><font SIZE="-1"><i>VARIABLE</i></font><i></i> (&#8216;=&#8217; | &#8216;+=&#8217;) (space separated values) </p>
<p> <font SIZE="-1"><code>VARIABLE</code></font> = &#8216;@{&#8216; <i></i><font SIZE="-1"><i>ALPHA</i></font><i></i> [ ( <i></i><font SIZE="-1"><i>ALPHANUMERIC</i></font><i></i> | &#8216;_&#8217; ) &#8230; ] &#8216;}&#8217; </p>
<p> <font SIZE="-1"><code>ALIAS RULE</code></font> = &#8216;alias&#8217; <i></i><font SIZE="-1"><i>ABS PATH</i></font><i></i> &#8216;-&gt;&#8217; <i></i><font SIZE="-1"><i>REWRITTEN ABS PATH</i></font><i></i> &#8216;,&#8217; </p>
<p> <font SIZE="-1"><code>INCLUDE</code></font> = ( &#8216;#include&#8217; | &#8216;include&#8217; ) [ &#8216;if exists&#8217; ] ( <i></i><font SIZE="-1"><i>ABS PATH</i></font><i></i> | <i></i><font SIZE="-1"><i>MAGIC PATH</i></font><i></i> ) </p>
<p> <font SIZE="-1"><code>ABI</code></font> = ( &#8216;abi&#8217; ) ( <i></i><font SIZE="-1"><i>ABS PATH</i></font><i></i> | <i></i><font SIZE="-1"><i>MAGIC PATH</i></font><i></i> ) &#8216;,&#8217; </p>
<p> <font SIZE="-1"><code>ABS PATH</code></font> = &#8216;&#8220;&#8217; path &#8221;&#8221; (the path is passed to <code><a href="/docs/linux/man/2-open/">open</a></code>(2)) </p>
<p> <font SIZE="-1"><code>MAGIC PATH</code></font> = &#8216;&lt;&#8216; relative path &#8216;&gt;&#8217;<br />
&nbsp;<wbr>&nbsp;The path is relative to&nbsp;<i>/etc/apparmor.d/</i>. </p>
<p> <font SIZE="-1"><code>COMMENT</code></font> = &#8216;#&#8217; <i></i><font SIZE="-1"><i>TEXT</i></font><i></i> [ &#8216;&#8217; ] &#8216;
&#8217; </p>
<p> <font SIZE="-1"><code>TEXT</code></font> = any characters </p>
<p> <font SIZE="-1"><code>PROFILE</code></font> = ( <i></i><font SIZE="-1"><i>PROFILE HEAD</i></font><i></i> ) [ <i></i><font SIZE="-1"><i>ATTACHMENT SPECIFICATION</i></font><i></i> ] [ <i></i><font SIZE="-1"><i>PROFILE FLAG CONDS</i></font><i></i> ] &#8216;{&#8216; ( <i></i><font SIZE="-1"><i>RULES</i></font><i></i> )* &#8216;}&#8217; </p>
<p> <font SIZE="-1"><code>PROFILE HEAD</code></font> = [ &#8216;profile&#8217; ] <i></i><font SIZE="-1"><i>FILEGLOB</i></font><i></i> | &#8216;profile&#8217; <i></i><font SIZE="-1"><i>PROFILE NAME</i></font><i></i> </p>
<p> <font SIZE="-1"><code>PROFILE NAME</code></font> ( <i></i><font SIZE="-1"><i>UNQUOTED PROFILE NAME</i></font><i></i> | <i></i><font SIZE="-1"><i>QUOTED PROFILE NAME</i></font><i></i> ) </p>
<p> <font SIZE="-1"><code>QUOTED PROFILE NAME</code></font> = &#8216;&quot;&#8217; <i></i><font SIZE="-1"><i>UNQUOTED PROFILE NAME</i></font><i></i> &#8216;&quot;&#8217; </p>
<p> <font SIZE="-1"><code>UNQUOTED PROFILE NAME</code></font> = (must start with alphanumeric character (after variable expansion), or &#8216;/&#8217; <font SIZE="-1"><code>AARE</code></font> have special meanings; see below. May include <i></i><font SIZE="-1"><i>VARIABLE</i></font><i></i>. Rules with embedded spaces or tabs must be quoted.) </p>
<p> <font SIZE="-1"><code>ATTACHMENT SPECIFICATION</code></font> = [ <i></i><font SIZE="-1"><i>PROFILE_EXEC_COND</i></font><i></i> ] [ <i></i><font SIZE="-1"><i>PROFILE XATTR CONDS</i></font><i></i> ] </p>
<p> <font SIZE="-1"><code>PROFILE_EXEC_COND</code></font> = <i></i><font SIZE="-1"><i>FILEGLOB</i></font><i></i> </p>
<p> <font SIZE="-1"><code>PROFILE XATTR CONDS</code></font> = [ &#8216;xattrs=&#8217; ] &#8216;(&#8216; comma or white space separated list of <i></i><font SIZE="-1"><i>PROFILE XATTR</i></font><i></i> &#8216;)&#8217; </p>
<p> <font SIZE="-1"><code>PROFILE XATTR</code></font> = extended attribute name &#8216;=&#8217; <i></i><font SIZE="-1"><i>XATTR VALUE FILEGLOB</i></font><i></i> </p>
<p> <font SIZE="-1"><code>XATTR VALUE FILEGLOB</code></font> = <i></i><font SIZE="-1"><i>FILEGLOB</i></font><i></i> </p>
<p> <font SIZE="-1"><code>PROFILE FLAG CONDS</code></font> = [ &#8216;flags=&#8217; ] &#8216;(&#8216; comma or white space separated list of <i></i><font SIZE="-1"><i>PROFILE FLAGS</i></font><i></i> &#8216;)&#8217; </p>
<p> <font SIZE="-1"><code>PROFILE FLAGS</code></font> = <i></i><font SIZE="-1"><i>PROFILE MODE</i></font><i></i> | <i></i><font SIZE="-1"><i>AUDIT_MODE</i></font><i></i> | &#8216;mediate_deleted&#8217; | &#8216;attach_disconnected&#8217; | &#8216;chroot_relative&#8217; </p>
<p> <font SIZE="-1"><code>PROFILE MODE</code></font> = &#8216;enforce&#8217; | &#8216;complain&#8217; | &#8216;kill&#8217; | &#8216;unconfined&#8217; </p>
<p> <font SIZE="-1"><code>AUDIT MODE</code></font> = &#8216;audit&#8217; </p>
<p> <font SIZE="-1"><code>RULES</code></font> = [ ( <i></i><font SIZE="-1"><i>LINE RULES</i></font><i></i> | <i></i><font SIZE="-1"><i>COMMA RULES</i></font><i></i> &#8216;,&#8217; | <i></i><font SIZE="-1"><i>BLOCK RULES</i></font><i></i> ) </p>
<p> <font SIZE="-1"><code>LINE RULES</code></font> = ( <i></i><font SIZE="-1"><i>COMMENT</i></font><i></i> | <i></i><font SIZE="-1"><i>INCLUDE</i></font><i></i> ) [ &#8216;&#8217; ] &#8216;
&#8217; </p>
<p> <font SIZE="-1"><code>COMMA RULES</code></font> = ( <i></i><font SIZE="-1"><i>CAPABILITY RULE</i></font><i></i> | <i></i><font SIZE="-1"><i>NETWORK RULE</i></font><i></i> | <i></i><font SIZE="-1"><i>MOUNT RULE</i></font><i></i> | <i></i><font SIZE="-1"><i>PIVOT ROOT RULE</i></font><i></i> | <i></i><font SIZE="-1"><i>UNIX RULE</i></font><i></i> | <i></i><font SIZE="-1"><i>FILE RULE</i></font><i></i> | <i></i><font SIZE="-1"><i>LINK RULE</i></font><i></i> | <i></i><font SIZE="-1"><i>CHANGE_PROFILE RULE</i></font><i></i> | <i></i><font SIZE="-1"><i>RLIMIT RULE</i></font><i></i> | <i></i><font SIZE="-1"><i>DBUS RULE</i></font><i></i> | <i></i><font SIZE="-1"><i>MQUEUE RULE</i></font><i></i> ) </p>
<p> <font SIZE="-1"><code>BLOCK RULES</code></font> = ( <i></i><font SIZE="-1"><i>SUBPROFILE</i></font><i></i> | <i></i><font SIZE="-1"><i>HAT</i></font><i></i> | <i></i><font SIZE="-1"><i>QUALIFIER BLOCK</i></font><i></i> ) </p>
<p> <font SIZE="-1"><code>SUBPROFILE</code></font> = &#8216;profile&#8217; <i></i><font SIZE="-1"><i>PROFILE NAME</i></font><i></i> [ <i></i><font SIZE="-1"><i>ATTACHMENT SPECIFICATION</i></font><i></i> ] [ <i></i><font SIZE="-1"><i>PROFILE FLAG CONDS</i></font><i></i> ] &#8216;{&#8216; ( <i></i><font SIZE="-1"><i>RULES</i></font><i></i> )* &#8216;}&#8217; </p>
<p> <font SIZE="-1"><code>HAT</code></font> = (&#8216;hat&#8217; | &#8216;^&#8217;) <i></i><font SIZE="-1"><i>HATNAME</i></font><i></i> [ <i></i><font SIZE="-1"><i>PROFILE FLAG CONDS</i></font><i></i> ] &#8216;{&#8216; ( <i></i><font SIZE="-1"><i>RULES</i></font><i></i> )* &#8216;}&#8217; </p>
<p> <font SIZE="-1"><code>HATNAME</code></font> = (must start with alphanumeric character. See <code><a href="/docs/linux/man/2-aa_change_hat/">aa_change_hat</a></code>(2) for a description of how this &#8220;hat&#8221; is used. If &#8216;^&#8217; is used to start a hat then there is no space between the &#8216;^&#8217; and <i></i><font SIZE="-1"><i>HATNAME</i></font><i></i>) </p>
<p> <font SIZE="-1"><code>QUALIFIER BLOCK</code></font> = <i></i><font SIZE="-1"><i>QUALIFIERS</i></font><i></i> <i></i><font SIZE="-1"><i>BLOCK</i></font><i></i> </p>
<p> <font SIZE="-1"><code>ACCESS TYPE</code></font> = ( &#8216;allow&#8217; | &#8216;deny&#8217; ) </p>
<p> <font SIZE="-1"><code>QUALIFIERS</code></font> = [ &#8216;audit&#8217; ] [ <i></i><font SIZE="-1"><i>ACCESS TYPE</i></font><i></i> ] </p>
<p> <font SIZE="-1"><code>CAPABILITY RULE</code></font> = [ <i></i><font SIZE="-1"><i>QUALIFIERS</i></font><i></i> ] &#8216;capability&#8217; [ <i></i><font SIZE="-1"><i>CAPABILITY LIST</i></font><i></i> ] </p>
<p> <font SIZE="-1"><code>CAPABILITY LIST</code></font> = ( <i></i><font SIZE="-1"><i>CAPABILITY</i></font><i></i> )+ </p>
<p> <font SIZE="-1"><code>CAPABILITY</code></font> = (lowercase capability name without &#8216;<font SIZE="-1">CAP_</font>&#8216; prefix; see <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7)) </p>
<p> <font SIZE="-1"><code>NETWORK RULE</code></font> = [ <i></i><font SIZE="-1"><i>QUALIFIERS</i></font><i></i> ] &#8216;network&#8217; [ <i></i><font SIZE="-1"><i>DOMAIN</i></font><i></i> ] [ <i></i><font SIZE="-1"><i>TYPE</i></font><i></i> | <i></i><font SIZE="-1"><i>PROTOCOL</i></font><i></i> ] </p>
<p> <font SIZE="-1"><code>DOMAIN</code></font> = ( &#8216;unix&#8217; | &#8216;inet&#8217; | &#8216;ax25&#8217; | &#8216;ipx&#8217; | &#8216;appletalk&#8217; | &#8216;netrom&#8217; | &#8216;bridge&#8217; | &#8216;atmpvc&#8217; | &#8216;x25&#8217; | &#8216;inet6&#8217; | &#8216;rose&#8217; | &#8216;netbeui&#8217; | &#8216;security&#8217; | &#8216;key&#8217; | &#8216;netlink&#8217; | &#8216;packet&#8217; | &#8216;ash&#8217; | &#8216;econet&#8217; | &#8216;atmsvc&#8217; | &#8216;rds&#8217; | &#8216;sna&#8217; | &#8216;irda&#8217; | &#8216;pppox&#8217; | &#8216;wanpipe&#8217; | &#8216;llc&#8217; | &#8216;ib&#8217; | &#8216;mpls&#8217; | &#8216;can&#8217; | &#8216;tipc&#8217; | &#8216;bluetooth&#8217; | &#8216;iucv&#8217; | &#8216;rxrpc&#8217; | &#8216;isdn&#8217; | &#8216;phonet&#8217; | &#8216;ieee802154&#8217; | &#8216;caif&#8217; | &#8216;alg&#8217; | &#8216;nfc&#8217; | &#8216;vsock&#8217; | &#8216;kcm&#8217; | &#8216;qipcrtr&#8217; | &#8216;smc&#8217; | &#8216;xdp&#8217; | &#8216;mctp&#8217; ) &#8216;,&#8217; </p>
<p> <font SIZE="-1"><code>TYPE</code></font> = ( &#8216;stream&#8217; | &#8216;dgram&#8217; | &#8216;seqpacket&#8217; | &#8216;rdm&#8217; | &#8216;raw&#8217; | &#8216;packet&#8217; ) </p>
<p> <font SIZE="-1"><code>PROTOCOL</code></font> = ( &#8216;tcp&#8217; | &#8216;udp&#8217; | &#8216;icmp&#8217; ) </p>
<p> <font SIZE="-1"><code>MOUNT RULE</code></font> = ( <i></i><font SIZE="-1"><i>MOUNT</i></font><i></i> | <i></i><font SIZE="-1"><i>REMOUNT</i></font><i></i> | <i></i><font SIZE="-1"><i>UMOUNT</i></font><i></i> ) </p>
<p> <font SIZE="-1"><code>MOUNT</code></font> = [ <i></i><font SIZE="-1"><i>QUALIFIERS</i></font><i></i> ] &#8216;mount&#8217; [ <i></i><font SIZE="-1"><i>MOUNT CONDITIONS</i></font><i></i> ] [ <i></i><font SIZE="-1"><i>SOURCE FILEGLOB</i></font><i></i> ] [ &#8216;-&gt;&#8217; [ <i></i><font SIZE="-1"><i>MOUNTPOINT FILEGLOB</i></font><i></i> ] </p>
<p> <font SIZE="-1"><code>REMOUNT</code></font> = [ <i></i><font SIZE="-1"><i>QUALIFIERS</i></font><i></i> ] &#8216;remount&#8217; [ <i></i><font SIZE="-1"><i>MOUNT CONDITIONS</i></font><i></i> ] <i></i><font SIZE="-1"><i>MOUNTPOINT FILEGLOB</i></font><i></i> </p>
<p> <font SIZE="-1"><code>UMOUNT</code></font> = [ <i></i><font SIZE="-1"><i>QUALIFIERS</i></font><i></i> ] &#8216;umount&#8217; [ <i></i><font SIZE="-1"><i>MOUNT CONDITIONS</i></font><i></i> ] <i></i><font SIZE="-1"><i>MOUNTPOINT FILEGLOB</i></font><i></i> </p>
<p> <font SIZE="-1"><code>MOUNT CONDITIONS</code></font> = [ ( &#8216;fstype&#8217; | &#8216;vfstype&#8217; ) ( &#8216;=&#8217; | &#8216;in&#8217; ) <i></i><font SIZE="-1"><i>MOUNT FSTYPE EXPRESSION</i></font><i></i> ] [ &#8216;options&#8217; ( &#8216;=&#8217; | &#8216;in&#8217; ) <i></i><font SIZE="-1"><i>MOUNT FLAGS EXPRESSION</i></font><i></i> ] </p>
<p> <font SIZE="-1"><code>MOUNT FSTYPE EXPRESSION</code></font> = ( <i></i><font SIZE="-1"><i>MOUNT FSTYPE LIST</i></font><i></i> | <i></i><font SIZE="-1"><i>MOUNT EXPRESSION</i></font><i></i> ) </p>
<p> <font SIZE="-1"><code>MOUNT FSTYPE LIST</code></font> = Comma separated list of valid filesystem and virtual filesystem types (eg ext4, debugfs, devfs, etc) </p>
<p> <font SIZE="-1"><code>MOUNT FLAGS EXPRESSION</code></font> = ( <i></i><font SIZE="-1"><i>MOUNT FLAGS LIST</i></font><i></i> | <i></i><font SIZE="-1"><i>MOUNT EXPRESSION</i></font><i></i> ) </p>
<p> <font SIZE="-1"><code>MOUNT FLAGS LIST</code></font> = Comma separated list of <i></i><font SIZE="-1"><i>MOUNT FLAGS</i></font><i></i>. </p>
<p> <font SIZE="-1"><code>MOUNT FLAGS</code></font> = ( &#8216;ro&#8217; | &#8216;rw&#8217; | &#8216;nosuid&#8217; | &#8216;suid&#8217; | &#8216;nodev&#8217; | &#8216;dev&#8217; | &#8216;noexec&#8217; | &#8216;exec&#8217; | &#8216;sync&#8217; | &#8216;async&#8217; | &#8216;remount&#8217; | &#8216;mand&#8217; | &#8216;nomand&#8217; | &#8216;dirsync&#8217; | &#8216;noatime&#8217; | &#8216;atime&#8217; | &#8216;nodiratime&#8217; | &#8216;diratime&#8217; | &#8216;bind&#8217; | &#8216;rbind&#8217; | &#8216;move&#8217; | &#8216;verbose&#8217; | &#8216;silent&#8217; | &#8216;loud&#8217; | &#8216;acl&#8217; | &#8216;noacl&#8217; | &#8216;unbindable&#8217; | &#8216;runbindable&#8217; | &#8216;private&#8217; | &#8216;rprivate&#8217; | &#8216;slave&#8217; | &#8216;rslave&#8217; | &#8216;shared&#8217; | &#8216;rshared&#8217; | &#8216;relatime&#8217; | &#8216;norelatime&#8217; | &#8216;iversion&#8217; | &#8216;noiversion&#8217; | &#8216;strictatime&#8217; | &#8216;nouser&#8217; | &#8216;user&#8217; ) </p>
<p> <font SIZE="-1"><code>MOUNT EXPRESSION</code></font> = ( <i></i><font SIZE="-1"><i>ALPHANUMERIC</i></font><i></i> | <i></i><font SIZE="-1"><i>AARE</i></font><i></i> ) &#8230; </p>
<p> <font SIZE="-1"><code>MQUEUE_RULE</code></font> = [ <i></i><font SIZE="-1"><i>QUALIFIERS</i></font><i></i> ] &#8216;mqueue&#8217; [ <i></i><font SIZE="-1"><i>MQUEUE ACCESS PERMISSIONS</i></font><i></i> ] [ <i></i><font SIZE="-1"><i>MQUEUE TYPE</i></font><i></i> ] [ <i></i><font SIZE="-1"><i>MQUEUE LABEL</i></font><i></i> ] [ <i></i><font SIZE="-1"><i>MQUEUE NAME</i></font><i></i> ] </p>
<p> <font SIZE="-1"><code>MQUEUE ACCESS PERMISSIONS</code></font> = <i></i><font SIZE="-1"><i>MQUEUE ACCESS</i></font><i></i> | <i></i><font SIZE="-1"><i>MQUEUE ACCESS LIST</i></font><i></i> </p>
<p> <font SIZE="-1"><code>MQUEUE ACCESS LIST</code></font> = &#8216;(&#8216; Comma or space separated list of <i></i><font SIZE="-1"><i>MQUEUE ACCESS</i></font><i></i> &#8216;)&#8217; </p>
<p> <font SIZE="-1"><code>MQUEUE ACCESS</code></font> = ( &#8216;r&#8217; | &#8216;w&#8217; | &#8216;rw&#8217; | &#8216;read&#8217; | &#8216;write&#8217; | &#8216;create&#8217; | &#8216;open&#8217; | &#8216;delete&#8217; | &#8216;getattr&#8217; | &#8216;setattr&#8217; ) </p>
<p> <font SIZE="-1"><code>MQUEUE TYPE</code></font> = &#8216;type&#8217; &#8216;=&#8217; ( &#8216;posix&#8217; | &#8216;sysv&#8217; ) </p>
<p> <font SIZE="-1"><code>MQUEUE LABEL</code></font> = &#8216;label&#8217; &#8216;=&#8217; &#8216;(&#8216; &#8216;&quot;&#8217; <i></i><font SIZE="-1"><i>AARE</i></font><i></i> &#8216;&quot;&#8217; | <i></i><font SIZE="-1"><i>AARE</i></font><i></i> &#8216;)&#8217; </p>
<p> <font SIZE="-1"><code>MQUEUE NAME</code></font> = <i></i><font SIZE="-1"><i>AARE</i></font><i></i> </p>
<p> <font SIZE="-1"><code>PIVOT ROOT RULE</code></font> = [ <i></i><font SIZE="-1"><i>QUALIFIERS</i></font><i></i> ] pivot_root [ oldroot=<i></i><font SIZE="-1"><i>OLD PUT FILEGLOB</i></font><i></i> ] [ <i></i><font SIZE="-1"><i>NEW ROOT FILEGLOB</i></font><i></i> ] [ &#8216;-&gt;&#8217; <i></i><font SIZE="-1"><i>PROFILE NAME</i></font><i></i> ] </p>
<p> <font SIZE="-1"><code>SOURCE FILEGLOB</code></font> = <i></i><font SIZE="-1"><i>FILEGLOB</i></font><i></i> </p>
<p> <font SIZE="-1"><code>MOUNTPOINT FILEGLOB</code></font> = <i></i><font SIZE="-1"><i>FILEGLOB</i></font><i></i> </p>
<p> <font SIZE="-1"><code>OLD PUT FILEGLOB</code></font> = <i></i><font SIZE="-1"><i>FILEGLOB</i></font><i></i> </p>
<p> <font SIZE="-1"><code>PTRACE_RULE</code></font> = [ <i></i><font SIZE="-1"><i>QUALIFIERS</i></font><i></i> ] &#8216;ptrace&#8217; [ <i></i><font SIZE="-1"><i>PTRACE ACCESS PERMISSIONS</i></font><i></i> ] [ <i></i><font SIZE="-1"><i>PTRACE PEER</i></font><i></i> ] </p>
<p> <font SIZE="-1"><code>PTRACE ACCESS PERMISSIONS</code></font> = <i></i><font SIZE="-1"><i>PTRACE ACCESS</i></font><i></i> | <i></i><font SIZE="-1"><i>PTRACE ACCESS LIST</i></font><i></i> </p>
<p> <font SIZE="-1"><code>PTRACE ACCESS LIST</code></font> = &#8216;(&#8216; Comma or space separated list of <i></i><font SIZE="-1"><i>PTRACE ACCESS</i></font><i></i> &#8216;)&#8217; </p>
<p> <font SIZE="-1"><code>PTRACE ACCESS</code></font> = ( &#8216;r&#8217; | &#8216;w&#8217; | &#8216;rw&#8217; | &#8216;read&#8217; | &#8216;readby&#8217; | &#8216;trace&#8217; | &#8216;tracedby&#8217; ) </p>
<p> <font SIZE="-1"><code>PTRACE PEER</code></font> = &#8216;peer&#8217; &#8216;=&#8217; <i></i><font SIZE="-1"><i>AARE</i></font><i></i> </p>
<p> <font SIZE="-1"><code>SIGNAL_RULE</code></font> = [ <i></i><font SIZE="-1"><i>QUALIFIERS</i></font><i></i> ] &#8216;signal&#8217; [ <i></i><font SIZE="-1"><i>SIGNAL ACCESS PERMISSIONS</i></font><i></i> ] [ <i></i><font SIZE="-1"><i>SIGNAL SET</i></font><i></i> ] [ <i></i><font SIZE="-1"><i>SIGNAL PEER</i></font><i></i> ] </p>
<p> <font SIZE="-1"><code>SIGNAL ACCESS PERMISSIONS</code></font> = <i></i><font SIZE="-1"><i>SIGNAL ACCESS</i></font><i></i> | <i></i><font SIZE="-1"><i>SIGNAL ACCESS LIST</i></font><i></i> </p>
<p> <font SIZE="-1"><code>SIGNAL ACCESS LIST</code></font> = &#8216;(&#8216; Comma or space separated list of <i></i><font SIZE="-1"><i>SIGNAL ACCESS</i></font><i></i> &#8216;)&#8217; </p>
<p> <font SIZE="-1"><code>SIGNAL ACCESS</code></font> = ( &#8216;r&#8217; | &#8216;w&#8217; | &#8216;rw&#8217; | &#8216;read&#8217; | &#8216;write&#8217; | &#8216;send&#8217; | &#8216;receive&#8217; ) </p>
<p> <font SIZE="-1"><code>SIGNAL SET</code></font> = &#8216;set&#8217; &#8216;=&#8217; &#8216;(&#8216; <i></i><font SIZE="-1"><i>SIGNAL LIST</i></font><i></i> &#8216;)&#8217; </p>
<p> <font SIZE="-1"><code>SIGNAL LIST</code></font> = Comma or space separated list of <i></i><font SIZE="-1"><i>SIGNALS</i></font><i></i> </p>
<p> <font SIZE="-1"><code>SIGNALS</code></font> = ( &#8216;hup&#8217; | &#8216;int&#8217; | &#8216;quit&#8217; | &#8216;ill&#8217; | &#8216;trap&#8217; | &#8216;abrt&#8217; | &#8216;bus&#8217; | &#8216;fpe&#8217; | &#8216;kill&#8217; | &#8216;usr1&#8217; | &#8216;segv&#8217; | &#8216;usr2&#8217; | &#8216;pipe&#8217; | &#8216;alrm&#8217; | &#8216;term&#8217; | &#8216;stkflt&#8217; | &#8216;chld&#8217; | &#8216;cont&#8217; | &#8216;stop&#8217; | &#8216;stp&#8217; | &#8216;ttin&#8217; | &#8216;ttou&#8217; | &#8216;urg&#8217; | &#8216;xcpu&#8217; | &#8216;xfsz&#8217; | &#8216;vtalrm&#8217; | &#8216;prof&#8217; | &#8216;winch&#8217; | &#8216;io&#8217; | &#8216;pwr&#8217; | &#8216;sys&#8217; | &#8217;emt&#8217; | &#8216;exists&#8217; | &#8216;rtmin+0&#8217; &#8230; &#8216;rtmin+32&#8217; ) </p>
<p> <font SIZE="-1"><code>SIGNAL PEER</code></font> = &#8216;peer&#8217; &#8216;=&#8217; <i></i><font SIZE="-1"><i>AARE</i></font><i></i> </p>
<p> <font SIZE="-1"><code>DBUS RULE</code></font> = ( <i></i><font SIZE="-1"><i>DBUS MESSAGE RULE</i></font><i></i> | <i></i><font SIZE="-1"><i>DBUS SERVICE RULE</i></font><i></i> | <i></i><font SIZE="-1"><i>DBUS EAVESDROP RULE</i></font><i></i> | <i></i><font SIZE="-1"><i>DBUS COMBINED RULE</i></font><i></i> ) </p>
<p> <font SIZE="-1"><code>DBUS MESSAGE RULE</code></font> = [ <i></i><font SIZE="-1"><i>QUALIFIERS</i></font><i></i> ] &#8216;dbus&#8217; [ <i></i><font SIZE="-1"><i>DBUS ACCESS EXPRESSION</i></font><i></i> ] [ <i></i><font SIZE="-1"><i>DBUS BUS</i></font><i></i> ] [ <i></i><font SIZE="-1"><i>DBUS PATH</i></font><i></i> ] [ <i></i><font SIZE="-1"><i>DBUS INTERFACE</i></font><i></i> ] [ <i></i><font SIZE="-1"><i>DBUS MEMBER</i></font><i></i> ] [ <i></i><font SIZE="-1"><i>DBUS PEER</i></font><i></i> ] </p>
<p> <font SIZE="-1"><code>DBUS SERVICE RULE</code></font> = [ <i></i><font SIZE="-1"><i>QUALIFIERS</i></font><i></i> ] &#8216;dbus&#8217; [ <i></i><font SIZE="-1"><i>DBUS ACCESS EXPRESSION</i></font><i></i> ] [ <i></i><font SIZE="-1"><i>DBUS BUS</i></font><i></i> ] [ <i></i><font SIZE="-1"><i>DBUS NAME</i></font><i></i> ] </p>
<p> <font SIZE="-1"><code>DBUS EAVESDROP RULE</code></font> = [ <i></i><font SIZE="-1"><i>QUALIFIERS</i></font><i></i> ] &#8216;dbus&#8217; [ <i></i><font SIZE="-1"><i>DBUS ACCESS EXPRESSION</i></font><i></i> ] [ <i></i><font SIZE="-1"><i>DBUS BUS</i></font><i></i> ] </p>
<p> <font SIZE="-1"><code>DBUS COMBINED RULE</code></font> = [ <i></i><font SIZE="-1"><i>QUALIFIERS</i></font><i></i> ] &#8216;dbus&#8217; [ <i></i><font SIZE="-1"><i>DBUS ACCESS EXPRESSION</i></font><i></i> ] [ <i></i><font SIZE="-1"><i>DBUS BUS</i></font><i></i> ] </p>
<p> <font SIZE="-1"><code>DBUS ACCESS EXPRESSION</code></font> = ( <i></i><font SIZE="-1"><i>DBUS ACCESS</i></font><i></i> | &#8216;(&#8216; <i></i><font SIZE="-1"><i>DBUS ACCESS LIST</i></font><i></i> &#8216;)&#8217; ) </p>
<p> <font SIZE="-1"><code>DBUS BUS</code></font> = &#8216;bus&#8217; &#8216;=&#8217; &#8216;(&#8216; &#8216;system&#8217; | &#8216;session&#8217; | &#8216;&quot;&#8217; <i></i><font SIZE="-1"><i>AARE</i></font><i></i> &#8216;&quot;&#8217; | <i></i><font SIZE="-1"><i>AARE</i></font><i></i> &#8216;)&#8217; </p>
<p> <font SIZE="-1"><code>DBUS PATH</code></font> = &#8216;path&#8217; &#8216;=&#8217; &#8216;(&#8216; &#8216;&quot;&#8217; <i></i><font SIZE="-1"><i>AARE</i></font><i></i> &#8216;&quot;&#8217; | <i></i><font SIZE="-1"><i>AARE</i></font><i></i> &#8216;)&#8217; </p>
<p> <font SIZE="-1"><code>DBUS INTERFACE</code></font> = &#8216;interface&#8217; &#8216;=&#8217; &#8216;(&#8216; &#8216;&quot;&#8217; <i></i><font SIZE="-1"><i>AARE</i></font><i></i> &#8216;&quot;&#8217; | <i></i><font SIZE="-1"><i>AARE</i></font><i></i> &#8216;)&#8217; </p>
<p> <font SIZE="-1"><code>DBUS MEMBER</code></font> = &#8216;member&#8217; &#8216;=&#8217; &#8216;(&#8216; &#8216;&quot;&#8217; <i></i><font SIZE="-1"><i>AARE</i></font><i></i> &#8216;&quot;&#8217; | <i></i><font SIZE="-1"><i>AARE</i></font><i></i> &#8216;)&#8217; </p>
<p> <font SIZE="-1"><code>DBUS PEER</code></font> = &#8216;peer&#8217; &#8216;=&#8217; &#8216;(&#8216; [ <i></i><font SIZE="-1"><i>DBUS NAME</i></font><i></i> ] [ <i></i><font SIZE="-1"><i>DBUS LABEL</i></font><i></i> ] &#8216;)&#8217; </p>
<p> <font SIZE="-1"><code>DBUS NAME</code></font> = &#8216;name&#8217; &#8216;=&#8217; &#8216;(&#8216; &#8216;&quot;&#8217; <i></i><font SIZE="-1"><i>AARE</i></font><i></i> &#8216;&quot;&#8217; | <i></i><font SIZE="-1"><i>AARE</i></font><i></i> &#8216;)&#8217; </p>
<p> <font SIZE="-1"><code>DBUS LABEL</code></font> = &#8216;label&#8217; &#8216;=&#8217; &#8216;(&#8216; &#8216;&quot;&#8217; <i></i><font SIZE="-1"><i>AARE</i></font><i></i> &#8216;&quot;&#8217; | <i></i><font SIZE="-1"><i>AARE</i></font><i></i> &#8216;)&#8217; </p>
<p> <font SIZE="-1"><code>DBUS ACCESS LIST</code></font> = Comma separated list of <i></i><font SIZE="-1"><i>DBUS ACCESS</i></font><i></i> </p>
<p> <font SIZE="-1"><code>DBUS ACCESS</code></font> = ( &#8216;send&#8217; | &#8216;receive&#8217; | &#8216;bind&#8217; | &#8216;eavesdrop&#8217; | &#8216;r&#8217; | &#8216;read&#8217; | &#8216;w&#8217; | &#8216;write&#8217; | &#8216;rw&#8217; )<br />
&nbsp;<wbr>&nbsp;Some accesses are incompatible with some rules;&nbsp;see below. </p>
<p> <font SIZE="-1"><code>AARE</code></font> = <code>?*[]{}^</code><br />
&nbsp;<wbr>&nbsp;See below for meanings. </p>
<p> <font SIZE="-1"><code>UNIX RULE</code></font> = [ <i></i><font SIZE="-1"><i>QUALIFIERS</i></font><i></i> ] &#8216;unix&#8217; [ <i></i><font SIZE="-1"><i>UNIX ACCESS EXPR</i></font><i></i> ] [ <i></i><font SIZE="-1"><i>UNIX RULE CONDS</i></font><i></i> ] [ <i></i><font SIZE="-1"><i>UNIX LOCAL EXPR</i></font><i></i> ] [ <i></i><font SIZE="-1"><i>UNIX PEER EXPR</i></font><i></i> ] </p>
<p> <font SIZE="-1"><code>UNIX ACCESS EXPR</code></font> = ( <i></i><font SIZE="-1"><i>UNIX ACCESS</i></font><i></i> | <i></i><font SIZE="-1"><i>UNIX ACCESS LIST</i></font><i></i> ) </p>
<p> <font SIZE="-1"><code>UNIX ACCESS</code></font> = ( &#8216;create&#8217; | &#8216;bind&#8217; | &#8216;listen&#8217; | &#8216;accept&#8217; | &#8216;connect&#8217; | &#8216;shutdown&#8217; | &#8216;getattr&#8217; | &#8216;setattr&#8217; | &#8216;getopt&#8217; | &#8216;setopt&#8217; | &#8216;send&#8217; | &#8216;receive&#8217; | &#8216;r&#8217; | &#8216;w&#8217; | &#8216;rw&#8217; )<br />
&nbsp;<wbr>&nbsp;Some access modes are incompatible with some rules or require additional parameters. </p>
<p> <font SIZE="-1"><code>UNIX ACCESS LIST</code></font> = &#8216;(&#8216; <i></i><font SIZE="-1"><i>UNIX ACCESS</i></font><i></i> ( [&#8216;,&#8217;] <i></i><font SIZE="-1"><i>UNIX ACCESS</i></font><i></i> )* &#8216;)&#8217; </p>
<p> <font SIZE="-1"><code>UNIX RULE CONDS</code></font> = ( <i></i><font SIZE="-1"><i>TYPE COND</i></font><i></i> | <i></i><font SIZE="-1"><i>PROTO COND</i></font><i></i> )<br />
&nbsp;<wbr>&nbsp;Each cond can appear at most once. </p>
<p> <font SIZE="-1"><code>TYPE COND</code></font> = &#8216;type&#8217; &#8216;=&#8217; ( <i></i><font SIZE="-1"><i>AARE</i></font><i></i> | &#8216;(&#8216; ( &#8216;&quot;&#8217; <i></i><font SIZE="-1"><i>AARE</i></font><i></i> &#8216;&quot;&#8217; | <i></i><font SIZE="-1"><i>AARE</i></font><i></i> )+ &#8216;)&#8217; ) </p>
<p> <font SIZE="-1"><code>PROTO COND</code></font> = &#8216;protocol&#8217; &#8216;=&#8217; ( <i></i><font SIZE="-1"><i>AARE</i></font><i></i> | &#8216;(&#8216; ( &#8216;&quot;&#8217; <i></i><font SIZE="-1"><i>AARE</i></font><i></i> &#8216;&quot;&#8217; | <i></i><font SIZE="-1"><i>AARE</i></font><i></i> )+ &#8216;)&#8217; ) </p>
<p> <font SIZE="-1"><code>UNIX LOCAL EXPR</code></font> = ( <i></i><font SIZE="-1"><i>UNIX ADDRESS COND</i></font><i></i> | <i></i><font SIZE="-1"><i>UNIX LABEL COND</i></font><i></i> | <i></i><font SIZE="-1"><i>UNIX ATTR COND</i></font><i></i> | <i></i><font SIZE="-1"><i>UNIX OPT COND</i></font><i></i> )*<br />
&nbsp;<wbr>&nbsp;Each cond can appear at most once. </p>
<p> <font SIZE="-1"><code>UNIX PEER EXPR</code></font> = &#8216;peer&#8217; &#8216;=&#8217; ( <i></i><font SIZE="-1"><i>UNIX ADDRESS COND</i></font><i></i> | <i></i><font SIZE="-1"><i>UNIX LABEL COND</i></font><i></i> )+<br />
&nbsp;<wbr>&nbsp;Each cond can appear at most once. </p>
<p> <font SIZE="-1"><code>UNIX ADDRESS COND</code></font> &#8216;addr&#8217; &#8216;=&#8217; ( <i></i><font SIZE="-1"><i>AARE</i></font><i></i> | &#8216;(&#8216; &#8216;&quot;&#8217; <i></i><font SIZE="-1"><i>AARE</i></font><i></i> &#8216;&quot;&#8217; | <i></i><font SIZE="-1"><i>AARE</i></font><i></i> &#8216;)&#8217; ) </p>
<p> <font SIZE="-1"><code>UNIX LABEL COND</code></font> &#8216;label&#8217; &#8216;=&#8217; ( <i></i><font SIZE="-1"><i>AARE</i></font><i></i> | &#8216;(&#8216; &#8216;&quot;&#8217; <i></i><font SIZE="-1"><i>AARE</i></font><i></i> &#8216;&quot;&#8217; | <i></i><font SIZE="-1"><i>AARE</i></font><i></i> &#8216;)&#8217; ) </p>
<p> <font SIZE="-1"><code>UNIX ATTR COND</code></font> &#8216;attr&#8217; &#8216;=&#8217; ( <i></i><font SIZE="-1"><i>AARE</i></font><i></i> | &#8216;(&#8216; &#8216;&quot;&#8217; <i></i><font SIZE="-1"><i>AARE</i></font><i></i> &#8216;&quot;&#8217; | <i></i><font SIZE="-1"><i>AARE</i></font><i></i> &#8216;)&#8217; ) </p>
<p> <font SIZE="-1"><code>UNIX OPT COND</code></font> &#8216;opt&#8217; &#8216;=&#8217; ( <i></i><font SIZE="-1"><i>AARE</i></font><i></i> | &#8216;(&#8216; &#8216;&quot;&#8217; <i></i><font SIZE="-1"><i>AARE</i></font><i></i> &#8216;&quot;&#8217; | <i></i><font SIZE="-1"><i>AARE</i></font><i></i> &#8216;)&#8217; ) </p>
<p> <font SIZE="-1"><code>RLIMIT RULE</code></font> = &#8216;set&#8217; &#8216;rlimit&#8217; [<i></i><font SIZE="-1"><i>RLIMIT</i></font><i></i> &#8216;&lt;=&#8217; <i></i><font SIZE="-1"><i>RLIMIT VALUE</i></font><i></i> ] </p>
<p> <font SIZE="-1"><code>RLIMIT</code></font> = ( &#8216;cpu&#8217; | &#8216;fsize&#8217; | &#8216;data&#8217; | &#8216;stack&#8217; | &#8216;core&#8217; | &#8216;rss&#8217; | &#8216;nofile&#8217; | &#8216;ofile&#8217; | &#8216;as&#8217; | &#8216;nproc&#8217; | &#8216;memlock&#8217; | &#8216;locks&#8217; | &#8216;sigpending&#8217; | &#8216;msgqueue&#8217; | &#8216;nice&#8217; | &#8216;rtprio&#8217; | &#8216;rttime&#8217; ) </p>
<p> <font SIZE="-1"><code>RLIMIT VALUE</code></font> = ( <i></i><font SIZE="-1"><i>RLIMIT SIZE</i></font><i></i> | <i></i><font SIZE="-1"><i>RLIMIT NUMBER</i></font><i></i> | <i></i><font SIZE="-1"><i>RLIMIT TIME</i></font><i></i> | <i></i><font SIZE="-1"><i>RLIMIT NICE</i></font><i></i> ) </p>
<p> <font SIZE="-1"><code>RLIMIT SIZE</code></font> = <i></i><font SIZE="-1"><i>NUMBER</i></font><i></i> ( &#8216;K&#8217; | &#8216;M&#8217; | &#8216;G&#8217; )<br />
&nbsp;<wbr>&nbsp;Only applies to&nbsp;<font SIZE="-1">RLIMIT</font>&nbsp;of&nbsp;&#8216;fsize&#8217;,&nbsp;&#8216;data&#8217;,&nbsp;&#8216;stack&#8217;,&nbsp;&#8216;core&#8217;,&nbsp;&#8216;rss&#8217;,&nbsp;&#8216;as&#8217;,&nbsp;&#8216;memlock&#8217;,&nbsp;&#8216;msgqueue&#8217;. </p>
<p> <font SIZE="-1"><code>RLIMIT NUMBER</code></font> = number from 0 to max rlimit value.<br />
&nbsp;<wbr>&nbsp;Only applies to&nbsp;<font SIZE="-1">RLIMIT</font>&nbsp;of&nbsp;&#8216;ofile&#8217;,&nbsp;&#8216;nofile&#8217;,&nbsp;&#8216;locks&#8217;,&nbsp;&#8216;sigpending&#8217;,&nbsp;&#8216;nproc&#8217;,&nbsp;&#8216;rtprio&#8217;. </p>
<p> <font SIZE="-1"><code>RLIMIT TIME</code></font> = <i></i><font SIZE="-1"><i>NUMBER</i></font><i></i> ( &#8216;us&#8217; | &#8216;microsecond&#8217; | &#8216;microseconds&#8217; | &#8216;ms&#8217; | &#8216;millisecond&#8217; | &#8216;milliseconds&#8217; | &#8216;s&#8217; | &#8216;sec&#8217; | &#8216;second&#8217; | &#8216;seconds&#8217; | &#8216;min&#8217; | &#8216;minute&#8217; | &#8216;minutes&#8217; | &#8216;h&#8217; | &#8216;hour&#8217; | &#8216;hours&#8217; | &#8216;d&#8217; | &#8216;day&#8217; | &#8216;days&#8217; | &#8216;week&#8217; | &#8216;weeks&#8217; )<br />
&nbsp;<wbr>&nbsp;Only applies to&nbsp;<font SIZE="-1">RLIMIT</font>&nbsp;of&nbsp;&#8216;cpu&#8217;&nbsp;and&nbsp;&#8216;rttime&#8217;.&nbsp;<font SIZE="-1">RLIMIT</font>&nbsp;&#8216;cpu&#8217;&nbsp;only allows units&nbsp;&gt;=&nbsp;&#8216;seconds&#8217;. </p>
<p> <font SIZE="-1"><code>RLIMIT NICE</code></font> = a number between -20 and 19.<br />
&nbsp;<wbr>&nbsp;Only applies to&nbsp;<font SIZE="-1">RLIMIT</font>&nbsp;of&nbsp;&#8216;nice&#8217;. </p>
<p> <font SIZE="-1"><code>FILE RULE</code></font> = [ <i></i><font SIZE="-1"><i>QUALIFIERS</i></font><i></i> ] [ &#8216;owner&#8217; ] ( &#8216;file&#8217; | [ &#8216;file&#8217; ] ( <i></i><font SIZE="-1"><i>FILEGLOB</i></font><i></i> <i></i><font SIZE="-1"><i>ACCESS</i></font><i></i> | <i></i><font SIZE="-1"><i>ACCESS</i></font><i></i> <i></i><font SIZE="-1"><i>FILEGLOB</i></font><i></i> ) [ &#8216;-&gt;&#8217; <i></i><font SIZE="-1"><i>EXEC TARGET</i></font><i></i> ] ) </p>
<p> <font SIZE="-1"><code>FILEGLOB</code></font> = ( <i></i><font SIZE="-1"><i>QUOTED FILEGLOB</i></font><i></i> | <i></i><font SIZE="-1"><i>UNQUOTED FILEGLOB</i></font><i></i> ) </p>
<p> <font SIZE="-1"><code>QUOTED FILEGLOB</code></font> = &#8216;&quot;&#8217; <i></i><font SIZE="-1"><i>UNQUOTED FILEGLOB</i></font><i></i> &#8216;&quot;&#8217; </p>
<p> <font SIZE="-1"><code>UNQUOTED FILEGLOB</code></font> = (must start with &#8216;/&#8217; (after variable expansion), <font SIZE="-1"><code>AARE</code></font> have special meanings; see below. May include <i></i><font SIZE="-1"><i>VARIABLE</i></font><i></i>. Rules with embedded spaces or tabs must be quoted. Rules must end with &#8216;/&#8217; to apply to directories.) </p>
<p> <font SIZE="-1"><code>ACCESS</code></font> = ( &#8216;r&#8217; | &#8216;w&#8217; | &#8216;a&#8217; | &#8216;l&#8217; | &#8216;k&#8217; | &#8216;m&#8217; | <i></i><font SIZE="-1"><i>EXEC TRANSITION</i></font><i></i> )+ (not all combinations are allowed; see below.) </p>
<p> <font SIZE="-1"><code>EXEC TRANSITION</code></font> = ( &#8216;ix&#8217; | &#8216;ux&#8217; | &#8216;Ux&#8217; | &#8216;px&#8217; | &#8216;Px&#8217; | &#8216;cx&#8217; | &#8216;Cx&#8217; | &#8216;pix&#8217; | &#8216;Pix&#8217; | &#8216;cix&#8217; | &#8216;Cix&#8217; | &#8216;pux&#8217; | &#8216;PUx&#8217; | &#8216;cux&#8217; | &#8216;CUx&#8217; | &#8216;x&#8217; )<br />
&nbsp;<wbr>&nbsp;A bare&nbsp;&#8216;x&#8217;&nbsp;is only allowed in rules with the deny qualifier, everything else only without the deny qualifier. </p>
<p> <font SIZE="-1"><code>EXEC TARGET</code></font> = name<br />
&nbsp;<wbr>&nbsp;Requires&nbsp;<i></i><font SIZE="-1"><i>EXEC TRANSITION</i></font><i></i>&nbsp;specified. </p>
<p> <font SIZE="-1"><code>LINK RULE</code></font> = <i></i><font SIZE="-1"><i>QUALIFIERS</i></font><i></i> [ &#8216;owner&#8217; ] &#8216;link&#8217; [ &#8216;subset&#8217; ] <i></i><font SIZE="-1"><i>FILEGLOB</i></font><i></i> &#8216;-&gt;&#8217; <i></i><font SIZE="-1"><i>FILEGLOB</i></font><i></i> </p>
<p> <font SIZE="-1"><code>ALPHA</code></font> = (&#8216;a&#8217;, &#8216;b&#8217;, &#8216;c&#8217;, &#8230; &#8216;z&#8217;, &#8216;A&#8217;, &#8216;B&#8217;, &#8230; &#8216;Z&#8217;) </p>
<p> <font SIZE="-1"><code>ALPHANUMERIC</code></font> = (&#8216;0&#8217;, &#8216;1&#8217;, &#8216;2&#8217;, &#8230; &#8216;9&#8217;, &#8216;a&#8217;, &#8216;b&#8217;, &#8216;c&#8217;, &#8230; &#8216;z&#8217;, &#8216;A&#8217;, &#8216;B&#8217;, &#8230; &#8216;Z&#8217;) </p>
<p> <font SIZE="-1"><code>CHANGE_PROFILE RULE</code></font> = &#8216;change_profile&#8217; [ [ <i></i><font SIZE="-1"><i>EXEC MODE</i></font><i></i> ] <i></i><font SIZE="-1"><i>EXEC COND</i></font><i></i> ] [ &#8216;-&gt;&#8217; <i></i><font SIZE="-1"><i>PROFILE NAME</i></font><i></i> ] </p>
<p> <font SIZE="-1"><code>EXEC_MODE</code></font> = ( &#8216;safe&#8217; | &#8216;unsafe&#8217; ) </p>
<p> <font SIZE="-1"><code>EXEC COND</code></font> = <i></i><font SIZE="-1"><i>FILEGLOB</i></font><i></i></dl>
<p> All resources and programs need a full path. There may be any number of subprofiles (aka child profiles) in a profile, limited only by kernel memory. Subprofile names are limited to 974 characters. Child profiles can be used to confine an application in a special way, or when you want the child to be unconfined on the system, but confined when called from the parent. Hats are a special child profile that can be used with the <code><a href="/docs/linux/man/2-aa_change_hat/">aa_change_hat</a></code>(2) <font SIZE="-1">API</font> call. Applications written or modified to use <code><a href="/docs/linux/man/2-aa_change_hat/">aa_change_hat</a></code>(2) can take advantage of subprofiles to run under different confinements, dependent on program logic. Several <code><a href="/docs/linux/man/2-aa_change_hat/">aa_change_hat</a></code>(2)-aware applications exist, including an Apache module, <code><a href="/docs/linux/man/5-mod_apparmor/">mod_apparmor</a></code>(5); a <font SIZE="-1">PAM</font> module, pam_apparmor; and a Tomcat valve, tomcat_apparmor. Applications written or modified to use <code><a href="/docs/linux/man/2-change_profile/">change_profile</a></code>(2) transition permanently to the specified profile. libvirt is one such application.</p>
<h3>Profile Head</h3>
<p>The profile head consists of a required name that is unique and optional attachment conditionals and control flags. </p>
<p> <i>Name</i> </p>
<p> The name of the profile is its identifier. It is what is displayed during introspection (eg. ps -Z), and defines how the profile is referenced by policy rules for any policy interaction via ipc or domain changes. It is recommended that the name be kept short and have meaning for the application it is being applied eg. <i>firefox</i> for the firefox web browser or its functional role eg. log_admin. </p>
<p> If the name is an applications full absolute path name eg. <i>/usr/bin/firefox</i> and an exec attachment conditional is not specified the name is also used as the profile&#8217;s exec attachment conditional. This use however has been deprecated and is discouraged as it makes for long names that can make profile rules difficult to understand, and may not be fully displayed by some introspection tools. </p>
<p> <i>Attachment Conditionals</i> </p>
<p> The attachment conditionals are used during profile changes to determine whether a profile is a match for the proposed profile transition. The attachment conditionals are optional, how and when they are applied is determined by the specific condition(s) used. </p>
<p> When attachment conditionals are used, the attachment conditionals for all profiles in the namespace will be evaluated. The profile with the set of attachments that result in the best match will become the new profile after a transition operation. Attachments that don&#8217;t match will result in the profile not being available for transition. </p>
<p> If no conditionals are specified the profile will only be used if a transition explicitly specifies the profile name. </p>
<p> Exec Attachment Conditional </p>
<p> The exec attachment conditional governs how closely the profile matches an executable program. This conditional is only used during an exec operation when the matching exec rule specifies either a <code>px</code> or <code>cx</code> (or their derivatives) transition type. The exec attachment conditional will also be used by tasks that are <i>unconfined</i> as they use a <code>pix</code> transition rule. </p>
<p> If there are no attachment matches then it is up to the exec rule to determine what happens (fail or a fallback option). </p>
<p> Note: see profile <i>Name</i> for information around using the profile name as an attachment conditional. </p>
<p> Exec attachment conditionals can contain variable names and pattern matching. They use a longest left match heuristic to deterime the winner in the case of multiple matches at run time. The exact implementation of this resolution is kernel specific and has improved over time, while retaining backwards compatibility. If the heuristic can not determine a winner between multiple matches the exec will be denied. </p>
<p> Extended Attributes Attachment Conditional </p>
<p> AppArmor profiles have the ability to target files based on their <code><a href="/docs/linux/man/7-xattr/">xattr</a></code>(7) values in addition to their path. For example, the following profile matches files in /usr/bin with the attribute &#8220;security.apparmor&#8221; and value &#8220;trusted&#8221;: </p>
<pre> /usr/bin/* xattrs(security.apparmor=&quot;trusted&quot;) {
 # ...
 }</pre>
<p>See <code><a href="/docs/linux/man/7-apparmor_xattrs/">apparmor_xattrs</a></code>(7) for further details. </p>
<p> <i>Flags</i> </p>
<p> The profile flags allow modifying the behavior of the profile. If a profile flag is specified it takes priority over any conflicting flags that have been specified by rules in the profile body. </p>
<p> Profile Mode </p>
<p> The profile mode allow controlling the enforcement behavior of the profile rules. </p>
<p> If no mode is specified the profile defaults to <i>enforce</i> mode.</p>
<dl>
<dt><code>enforce</code> For a given action, if the profile rules do not grant permission the action will be denied, with an <i></i><font SIZE="-1"><i>EACCES</i></font><i></i> or <i></i><font SIZE="-1"><i>EPERM</i></font><i></i> error code returned to userspace, and the violation will be logged with a tag of the access being <font SIZE="-1"><code>DENIED</code></font>.</p>
<dd>
<dt><code>kill</code> This is a variant of enforce mode where in addition to returning <i></i><font SIZE="-1"><i>EACCES</i></font><i></i> or <i></i><font SIZE="-1"><i>EPERM</i></font><i></i> for a violation, the task is also sent a signal to kill it.</p>
<dd>
<dt><code>complain</code> For a given action, if the profile rules do not grant permission the action will be allowed, but the violation will be logged with a tag of the access being <font SIZE="-1"><code>ALLOWED</code></font>.</p>
<dd>
<dt><code>unconfined</code> This mode allows a task confined by the profile to behave as though they are <i>unconfined</i>. This mode allow for an unconfined behavior that can be later changed to confinement by using profile replacement. This mode is should not be used under regular deployment but can be useful during debugging and some system initialization scenarios.</p>
<dd></dl>
<p> Audit Mode </p>
<p> The audit mode allows control of how AppArmor messages are are logged to the audit system.</p>
<dl>
<dt><code>audit</code> This flag causes all actions whether allowed or denied to be logged.</p>
<dd></dl>
<p> Misc modes</p>
<dl>
<dt><code>mediate_deleted</code> This forces AppArmor to mediate deleted files as if they still exist in the file system.</p>
<dd>
<dt><code>attach_disconnected</code> This forces AppArmor to attach disconnected objects to the task&#8217;s namespace and mediate them as though they are part of the namespace. <font SIZE="-1">WARNING</font> this mode is unsafe and can result in aliasing and access to objects that should not be allowed. Its intent is a debug and policy development tool.</p>
<dd>
<dt><code>chroot_relative</code> This forces file names to be relative to a chroot and behave as if the chroot is a mount namespace.</p>
<dd></dl>
<h3>Access Modes</h3>
<p>File permission access modes consists of combinations of the following modes:</p>
<dl>
<dt><code>r</code></p>
<dd>&#8211; read</p>
<dt><code>w</code></p>
<dd>&#8211; write &#8212; conflicts with append</p>
<dt><code>a</code></p>
<dd>&#8211; append &#8212; conflicts with write</p>
<dt><code>ux</code></p>
<dd>&#8211; unconfined execute</p>
<dt><code>Ux</code></p>
<dd>&#8211; unconfined execute &#8212; scrub the environment</p>
<dt><code>px</code></p>
<dd>&#8211; discrete profile execute</p>
<dt><code>Px</code></p>
<dd>&#8211; discrete profile execute &#8212; scrub the environment</p>
<dt><code>cx</code></p>
<dd>&#8211; transition to subprofile on execute</p>
<dt><code>Cx</code></p>
<dd>&#8211; transition to subprofile on execute &#8212; scrub the environment</p>
<dt><code>ix</code></p>
<dd>&#8211; inherit execute</p>
<dt><code>pix</code></p>
<dd>&#8211; discrete profile execute with inherit fallback</p>
<dt><code>Pix</code></p>
<dd>&#8211; discrete profile execute with inherit fallback &#8212; scrub the environment</p>
<dt><code>cix</code></p>
<dd>&#8211; transition to subprofile on execute with inherit fallback</p>
<dt><code>Cix</code></p>
<dd>&#8211; transition to subprofile on execute with inherit fallback &#8212; scrub the environment</p>
<dt><code>pux</code></p>
<dd>&#8211; discrete profile execute with fallback to unconfined</p>
<dt><code>PUx</code></p>
<dd>&#8211; discrete profile execute with fallback to unconfined &#8212; scrub the environment</p>
<dt><code>cux</code></p>
<dd>&#8211; transition to subprofile on execute with fallback to unconfined</p>
<dt><code>CUx</code></p>
<dd>&#8211; transition to subprofile on execute with fallback to unconfined &#8212; scrub the environment</p>
<dt><code>deny x</code></p>
<dd>&#8211; disallow execute (in rules with the deny qualifier)</p>
<dt><code>m</code></p>
<dd>&#8211; allow <font SIZE="-1">PROT_EXEC</font> with <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) calls</p>
<dt><code>l</code></p>
<dd>&#8211; link</p>
<dt><code>k</code></p>
<dd>&#8211; lock</dl>
<h3>Access Modes Details</h3>
<dl>
<dt><code>r &#8211; Read mode</code></p>
<dd>Allows the program to have read access to the file or directory listing. Read access is required for shell scripts and other interpreted content.</p>
<dt><code>w &#8211; Write mode</code></p>
<dd>Allows the program to have write access to the file. Files and directories must have this permission if they are to be unlinked (removed.) Write mode is not required on a directory to rename or create files within the directory. </p>
<p> This mode conflicts with append mode.</p>
<dt><code>a &#8211; Append mode</code></p>
<dd>Allows the program to have a limited appending only write access to the file. Append mode will prevent an application from opening the file for write unless it passes the O_APPEND parameter flag on open. </p>
<p> The mode conflicts with Write mode.</p>
<dt><code>ux &#8211; Unconfined execute mode</code></p>
<dd>Allows the program to execute the program without any AppArmor profile being applied to the program. </p>
<p> This mode is useful when a confined program needs to be able to perform a privileged operation, such as rebooting the machine. By placing the privileged section in another executable and granting unconfined execution rights, it is possible to bypass the mandatory constraints imposed on all confined processes. For more information on what is constrained, see the <code><a href="/docs/linux/man/7-apparmor/">apparmor</a></code>(7) man page. </p>
<p> <font SIZE="-1"><code>WARNING</code></font> &#8216;ux&#8217; should only be used in very special cases. It enables the designated child processes to be run without any AppArmor protection. &#8216;ux&#8217; does not scrub the environment of variables such as <font SIZE="-1">LD_PRELOAD</font>; as a result, the calling domain may have an undue amount of influence over the callee. Use this mode only if the child absolutely must be run unconfined and <font SIZE="-1">LD_PRELOAD</font> must be used. Any profile using this mode provides negligible security. Use at your own risk. </p>
<p> Incompatible with other exec transition modes and the deny qualifier.</p>
<dt><code>Ux &#8211; unconfined execute &#8212; scrub the environment</code></p>
<dd>&#8216;Ux&#8217; allows the named program to run in &#8216;ux&#8217; mode, but AppArmor will invoke the Linux Kernel&#8217;s <code>unsafe_exec</code> routines to scrub the environment, similar to setuid programs. (See <code><a href="/docs/linux/man/8-ld-so/">ld.so</a></code>(8) for some information on setuid/setgid environment scrubbing.) </p>
<p> <font SIZE="-1"><code>WARNING</code></font> &#8216;Ux&#8217; should only be used in very special cases. It enables the designated child processes to be run without any AppArmor protection. Use this mode only if the child absolutely must be run unconfined. Use at your own risk. </p>
<p> Incompatible with other exec transition modes and the deny qualifier.</p>
<dt><code>px &#8211; Discrete Profile execute mode</code></p>
<dd>This mode requires that a discrete security profile is defined for a program executed and forces an AppArmor domain transition. If there is no profile defined then the access will be denied. </p>
<p> <font SIZE="-1"><code>WARNING</code></font> &#8216;px&#8217; does not scrub the environment of variables such as <font SIZE="-1">LD_PRELOAD</font>; as a result, the calling domain may have an undue amount of influence over the callee. </p>
<p> Incompatible with other exec transition modes and the deny qualifier.</p>
<dt><code>Px &#8211; Discrete Profile execute mode &#8212; scrub the environment</code></p>
<dd>&#8216;Px&#8217; allows the named program to run in &#8216;px&#8217; mode, but AppArmor will invoke the Linux Kernel&#8217;s <code>unsafe_exec</code> routines to scrub the environment, similar to setuid programs. (See <code><a href="/docs/linux/man/8-ld-so/">ld.so</a></code>(8) for some information on setuid/setgid environment scrubbing.) </p>
<p> Incompatible with other exec transition modes and the deny qualifier.</p>
<dt><code>cx &#8211; Transition to Subprofile execute mode</code></p>
<dd>This mode requires that a local security profile is defined and forces an AppArmor domain transition to the named profile. If there is no profile defined then the access will be denied. </p>
<p> <font SIZE="-1"><code>WARNING</code></font> &#8216;cx&#8217; does not scrub the environment of variables such as <font SIZE="-1">LD_PRELOAD</font>; as a result, the calling domain may have an undue amount of influence over the callee. </p>
<p> Incompatible with other exec transition modes and the deny qualifier.</p>
<dt><code>Cx &#8211; Transition to Subprofile execute mode &#8212; scrub the environment</code></p>
<dd>&#8216;Cx&#8217; allows the named program to run in &#8216;cx&#8217; mode, but AppArmor will invoke the Linux Kernel&#8217;s <code>unsafe_exec</code> routines to scrub the environment, similar to setuid programs. (See <code><a href="/docs/linux/man/8-ld-so/">ld.so</a></code>(8) for some information on setuid/setgid environment scrubbing.) </p>
<p> Incompatible with other exec transition modes and the deny qualifier.</p>
<dt><code>ix &#8211; Inherit execute mode</code></p>
<dd>Prevent the normal AppArmor domain transition on <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) when the profiled program executes the named program. Instead, the executed resource will inherit the current profile. </p>
<p> This mode is useful when a confined program needs to call another confined program without gaining the permissions of the target&#8217;s profile, or losing the permissions of the current profile. There is no version to scrub the environment because &#8216;ix&#8217; executions don&#8217;t change privileges. </p>
<p> Incompatible with other exec transition modes and the deny qualifier.</p>
<dt><code>Profile transition with inheritance fallback execute mode</code></p>
<dd>These modes attempt to perform a domain transition as specified by the matching permission (shown below) and if that transition fails to find the matching profile the domain transition proceeds using the &#8216;ix&#8217; transition mode. </p>
<pre> 'Pix' == 'Px' with fallback to 'ix'
 'pix' == 'px' with fallback to 'ix'
 'Cix' == 'Cx' with fallback to 'ix'
 'cix' == 'cx' with fallback to 'ix'</pre>
<p>Incompatible with other exec transition modes and the deny qualifier.</p>
<dt><code>Profile transition with unconfined fallback execute mode</code></p>
<dd>These modes attempt to perform a domain transition as specified by the matching permission (shown below) and if that transition fails to find the matching profile the domain transition proceeds using the &#8216;ux&#8217; transition mode if &#8216;pux&#8217;, &#8216;cux&#8217; or the &#8216;Ux&#8217; transition mode if &#8216;PUx&#8217;, &#8216;CUx&#8217; is used. </p>
<pre> 'PUx' == 'Px' with fallback to 'Ux'
 'pux' == 'px' with fallback to 'ux'
 'CUx' == 'Cx' with fallback to 'Ux'
 'cux' == 'cx' with fallback to 'ux'</pre>
<p>Incompatible with other exec transition modes and the deny qualifier.</p>
<dt><code>deny x &#8211; Deny execute</code></p>
<dd>For rules including the deny modifier, only &#8216;x&#8217; is allowed to deny execute. </p>
<p> The &#8216;ix&#8217;, &#8216;Px&#8217;, &#8216;px&#8217;, &#8216;Cx&#8217;, &#8216;cx&#8217; and the fallback modes conflict with the deny modifier.</p>
<dt><code>Directed profile transitions</code></p>
<dd>The directed (&#8216;px&#8217;, &#8216;Px&#8217;, &#8216;pix&#8217;, &#8216;Pix&#8217;, &#8216;pux&#8217;, &#8216;PUx&#8217;) profile and subprofile (&#8216;cx&#8217;, &#8216;Cx&#8217;, &#8216;cix&#8217;, &#8216;Cix&#8217;, &#8216;cux&#8217;, &#8216;CUx&#8217;) transitions normally determine the profile to transition to from the executable name. It is however possible to specify the name of the profile that the transition should use. </p>
<p> The name of the profile to transition to is specified using the &#8216;-&gt;&#8217; followed by the name of the profile to transition to. Eg. </p>
<pre> /bin/** px -&gt; profile,</pre>
<p>Incompatible with other exec transition modes.</p>
<dt><code>m &#8211; Allow executable mapping</code></p>
<dd>This mode allows a file to be mapped into memory using <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2)&#8217;s <font SIZE="-1">PROT_EXEC</font> flag. This flag marks the pages executable; it is used on some architectures to provide non-executable data pages, which can complicate exploit attempts. AppArmor uses this mode to limit which files a well-behaved program (or all programs on architectures that enforce non-executable memory access controls) may use as libraries, to limit the effect of invalid <code>-L</code> flags given to <code><a href="/docs/linux/man/1-ld/">ld</a></code>(1) and <font SIZE="-1"><code>LD_PRELOAD</code></font>, <font SIZE="-1"><code>LD_LIBRARY_PATH</code></font>, given to <code><a href="/docs/linux/man/8-ld-so/">ld.so</a></code>(8).</p>
<dt><code>l &#8211; Link mode</code></p>
<dd>Allows the program to be able to create a link with this name. When a link is created, the new link <font SIZE="-1"><code>MUST</code></font> have a subset of permissions as the original file (with the exception that the destination does not have to have link access.) If there is an &#8216;x&#8217; rule on the new link, it must match the original file exactly.</p>
<dt><code>k &#8211; lock mode</code></p>
<dd>Allows the program to be able lock a file with this name. This permission covers both advisory and mandatory locking.</p>
<dt><code>leading </code><font SIZE="-1"><code>OR</code></font><code> trailing access permissions</code></p>
<dd>File rules can be specified with the access permission either leading or trailing the file glob. Eg. </p>
<pre> rw /**, # leading permissions
 /** rw, # trailing permissions</pre>
<p>When leading permissions are used further rule options and context may be allowed, Eg. </p>
<pre> l /foo -&gt; /bar, # lead 'l' link permission is equivalent to link rules</pre>
</dl>
<h3>Link rules</h3>
<p>Link rules allow specifying permission to form a hard link as a link target pair. If the subset condition is specified then the permissions to access the link file must be a subset of the profiles permissions to access the target file. If there is an &#8216;x&#8217; rule on the new link, it must match the original file exactly. </p>
<p> Eg. </p>
<pre> /file1 r,
 /file2 rwk,
 /link* rw,
 link subset /link* -&gt; /**,</pre>
<p>The link rule allows linking of /link to both /file1 or /file2 by name however because the /link file has &#8216;rw&#8217; permissions it is not allowed to link to /file1 because that would grant an access path to /file1 with more permissions than the &#8216;r&#8217; permissions the profile specifies. </p>
<p> A link of /link to /file2 would be allowed because the &#8216;rw&#8217; permissions of /link are a subset of the &#8216;rwk&#8217; permissions for /file1. </p>
<p> The link rule is equivalent to specifying the &#8216;l&#8217; link permission as a leading permission with no other file access permissions. When this is done the link rule options can be specified. </p>
<p> The following link rule is equivalent to the &#8216;l&#8217; permission file rule </p>
<pre> link /foo -&gt; bar,
 l /foo -&gt; /bar,</pre>
<p>File rules that specify the &#8216;l&#8217; permission and don&#8217;t specify the extend link permissions map to link rules as follows. </p>
<pre> /foo l,
 l /foo,
 link subset /foo -&gt; /**,</pre>
<h3>Comments</h3>
<p>Comments start with # and may begin at any place within a line. The comment ends when the line ends. This is the same comment style as shell scripts.</p>
<h3>Capabilities</h3>
<p>The only capabilities a confined process may use may be enumerated; for the complete list, please refer to <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7). Note that granting some capabilities renders AppArmor confinement for that domain advisory; while <code><a href="/docs/linux/man/2-open/">open</a></code>(2), <code><a href="/docs/linux/man/2-read/">read</a></code>(2), <code><a href="/docs/linux/man/2-write/">write</a></code>(2), etc., will still return error when access is not granted, some capabilities allow loading kernel modules, arbitrary access to <font SIZE="-1">IPC,</font> ability to bypass discretionary access controls, and other operations that are typically reserved for the root user.</p>
<h3>Network Rules</h3>
<p>AppArmor supports simple coarse grained network mediation. The network rule restrict all <code><a href="/docs/linux/man/2-socket/">socket</a></code>(2) based operations. The mediation done is a coarse-grained check on whether a socket of a given type and family can be created, read, or written. There is no mediation based of port number or protocol beyond tcp, udp, and raw. Network <code><a href="/docs/linux/man/7-netlink/">netlink</a></code>(7) rules may only specify type &#8216;dgram&#8217; and &#8216;raw&#8217;. </p>
<p> AppArmor network rules are accumulated so that the granted network permissions are the union of all the listed network rule permissions. </p>
<p> AppArmor network rules are broad and general and become more restrictive as further information is specified. </p>
<p> eg. </p>
<pre> network, #allow access to all networking
 network tcp, #allow access to tcp
 network inet tcp, #allow access to tcp only for inet4 addresses
 network inet6 tcp, #allow access to tcp only for inet6 addresses
 network netlink raw, #allow access to AF_NETLINK SOCK_RAW</pre>
<h3>Mount Rules</h3>
<p>AppArmor supports mount mediation and allows specifying filesystem types and mount flags. The syntax of mount rules in AppArmor is based on the <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8) command syntax. Mount rules must contain one of the mount, remount or umount keywords, but all mount conditions are optional. Unspecified optional conditionals are assumed to match all entries (eg, not specifying fstype means all fstypes are matched). Due to the complexity of the mount command and how options may be specified, AppArmor allows specifying conditionals three different ways:</p>
<dl>
<dt>1.</p>
<dd>If a conditional is specified using &#8216;=&#8217;, then the rule only grants permission for mounts matching the exactly specified options. For example, an AppArmor policy with the following rule: </p>
<pre> mount options=ro /dev/foo -E&lt;gt&gt; /mnt/,</pre>
<p>Would match: </p>
<pre> $ mount -o ro /dev/foo /mnt</pre>
<p>but not either of these: </p>
<pre> $ mount -o ro,atime /dev/foo /mnt
 $ mount -o rw /dev/foo /mnt</pre>
<dt>2.</p>
<dd>If a conditional is specified using &#8216;in&#8217;, then the rule grants permission for mounts matching any combination of the specified options. For example, if an AppArmor policy has the following rule: </p>
<pre> mount options in (ro,atime) /dev/foo -&gt; /mnt/,</pre>
<p>all of these mount commands will match: </p>
<pre> $ mount -o ro /dev/foo /mnt
 $ mount -o ro,atime /dev/foo /mnt
 $ mount -o atime /dev/foo /mnt</pre>
<p>but none of these will: </p>
<pre> $ mount -o ro,sync /dev/foo /mnt
 $ mount -o ro,atime,sync /dev/foo /mnt
 $ mount -o rw /dev/foo /mnt
 $ mount -o rw,noatime /dev/foo /mnt
 $ mount /dev/foo /mnt</pre>
<dt>3.</p>
<dd>If multiple conditionals are specified in a single mount rule, then the rule grants permission for each set of options. This provides a shorthand when writing mount rules which might help to logically break up a conditional. For example, if an AppArmor policy has the following rule: </p>
<pre> mount options=ro options=atime</pre>
<p>both of these mount commands will match: </p>
<pre> $ mount -o ro /dev/foo /mnt
 $ mount -o atime /dev/foo /mnt</pre>
<p>but this one will not: </p>
<pre> $ mount -o ro,atime /dev/foo /mnt</pre>
</dl>
<p> Note that separate mount rules are distinct and the options do not accumulate. For example, these AppArmor mount rules: </p>
<pre> mount options=ro,
 mount options=atime,</pre>
<p>are not equivalent to either of these mount rules: </p>
<pre> mount options=(ro,atime),
 mount options in (ro,atime),</pre>
<p>To help clarify the flexibility and complexity of mount rules, here are some example rules with accompanying matching commands:</p>
<dl>
<dt><code>mount,</code></p>
<dd>the &#8216;mount&#8217; rule without any conditionals is the most generic and allows any mount. Equivalent to &#8216;mount fstype=** options=** ** -&gt; /**&#8217;.</p>
<dt><code>mount /dev/foo,</code></p>
<dd>allow mounting of /dev/foo anywhere with any options. Some matching mount commands: </p>
<pre> $ mount /dev/foo /mnt
 $ mount -t ext3 /dev/foo /mnt
 $ mount -t vfat /dev/foo /mnt
 $ mount -o ro,atime,noexec,nodiratime /dev/foo /srv/some/mountpoint</pre>
<dt><code>mount options=ro /dev/foo,</code></p>
<dd>allow mounting of /dev/foo anywhere, as read only. Some matching mount commands: </p>
<pre> $ mount -o ro /dev/foo /mnt
 $ mount -o ro /dev/foo /some/where/else</pre>
<dt><code>mount options=(ro,atime) /dev/foo,</code></p>
<dd>allow mount of /dev/foo anywhere, as read only and using inode access times. Some matching mount commands: </p>
<pre> $ mount -o ro,atime /dev/foo /mnt
 $ mount -o ro,atime /dev/foo /some/where/else</pre>
<dt><code>mount options in (ro,atime) /dev/foo,</code></p>
<dd>allow mount of /dev/foo anywhere using some combination of &#8216;ro&#8217; and &#8216;atime&#8217; (see above). Some matching mount commands: </p>
<pre> $ mount -o ro /dev/foo /mnt
 $ mount -o atime /dev/foo /some/where/else
 $ mount -o ro,atime /dev/foo /some/other/place</pre>
<dt><code>mount options=ro /dev/foo, mount options=atime /dev/foo,</code></p>
<dd>allow mount of /dev/foo anywhere as read only, and allow mount of /dev/foo anywhere using inode access times. Note this is expressed as two different rules. Matches: </p>
<pre> $ mount -o ro /dev/foo /mnt/1
 $ mount -o atime /dev/foo /mnt/2</pre>
<dt><code>mount -&gt; /mnt/**,</code></p>
<dd>allow mounting anything under a directory in /mnt/**. Some matching mount commands: </p>
<pre> $ mount /dev/foo1 /mnt/1
 $ mount -o ro,atime,noexec,nodiratime /dev/foo2 /mnt/deep/path/foo2</pre>
<dt><code>mount options=ro -&gt; /mnt/**,</code></p>
<dd>allow mounting anything under /mnt/**, as read only. Some matching mount commands: </p>
<pre> $ mount -o ro /dev/foo1 /mnt/1
 $ mount -o ro /dev/foo2 /mnt/deep/path/foo2</pre>
<dt><code>mount fstype=ext3 options=(rw,atime) /dev/sdb1 -&gt; /mnt/stick/,</code></p>
<dd>allow mounting an ext3 filesystem in /dev/sdb1 on /mnt/stick as read/write and using inode access times. Matches only: </p>
<pre> $ mount -o rw,atime /dev/sdb1 /mnt/stick</pre>
<dt><code>mount options=(ro, atime) options in (nodev, user) /dev/foo -&gt; /mnt/,</code></p>
<dd>allow mounting /dev/foo on /mmt/ read only and using inode access times or allow mounting /dev/foo on /mnt/ with some combination of &#8216;nodev&#8217; and &#8216;user&#8217;. Matches only: </p>
<pre> $ mount -o ro,atime /dev/foo /mnt
 $ mount -o nodev /dev/foo /mnt
 $ mount -o user /dev/foo /mnt
 $ mount -o nodev,user /dev/foo /mnt</pre>
</dl>
<h3>Message Queue rules</h3>
<p>AppArmor supports mediation of <font SIZE="-1">POSIX</font> and <font SIZE="-1">SYSV</font> message queues. </p>
<p> AppArmor Message Queue permissions are implied when a rule does not explicitly state an access list. By default, all Message Queue permissions are implied. </p>
<p> AppArmor Message Queue permissions become more restricted as further information is specified. Policy can be specified by determining its access mode, type, label, and message queue name. </p>
<p> Regarding access modes, &#8216;r&#8217; and &#8216;read&#8217; are used to read messages from the queue. &#8216;w&#8217; and &#8216;write&#8217; are used to write to the message queue. &#8216;create&#8217; is used to create the message queue, and &#8216;open&#8217; is used to get the message queue identifier when the queue is already created. &#8216;delete&#8217; is used to remove the message queue. The access modes to get and set attributes of the message queue are &#8216;setattr&#8217; and &#8216;getattr&#8217;. </p>
<p> The type of the policy can be either &#8216;posix&#8217; or &#8216;sysv&#8217;. This information is relevant when the message queue name is not specified, and when specified can be inferred by the queue name, since message queues&#8217; name for posix must start with &#8216;/&#8217;, and message queues&#8217; key for <font SIZE="-1">SYSV</font> must be a positive integer. </p>
<p> The policy label is the label assigned to the message queue when it is created. </p>
<p> The message queue name can be either a string starting with &#8216;/&#8217; if the type is <font SIZE="-1">POSIX,</font> or a positive integer if the type is <font SIZE="-1">SYSV.</font> If the type is not specified, then it will be inferred by the queue name. </p>
<p> Example AppArmor Message Queue rules: </p>
<pre> # Allow all Message Queue access
 mqueue,
 # Explicitly allow all Message Queue access,
 mqueue (create, open, delete, read, write, getattr, setattr),
 # Explicitly deny use of Message Queue
 deny mqueue,
 # Allow all access for POSIX queue of name /bar
 mqueue type=posix /bar,
 # Allow create permission for a SYSV queue of label foo
 mqueue create label=foo 123,</pre>
<h3>Pivot Root Rules</h3>
<p>AppArmor mediates changing of the root filesystem through the <code><a href="/docs/linux/man/2-pivot_root/">pivot_root</a></code>(2) system call. The syntax of &#8216;pivot_root&#8217; rules in AppArmor is based on the <code><a href="/docs/linux/man/2-pivot_root/">pivot_root</a></code>(2) system call parameters with the notable exception that the ordering is reversed. The path corresponding to the put_old parameter of <code><a href="/docs/linux/man/2-pivot_root/">pivot_root</a></code>(2) is optionally specified in the &#8216;pivot_root&#8217; rule using the &#8216;oldroot=&#8217; prefix. </p>
<p> AppArmor &#8216;pivot_root&#8217; rules can specify a profile transition to occur during the <code><a href="/docs/linux/man/2-pivot_root/">pivot_root</a></code>(2) system call. Note that AppArmor will only transition the process calling <code><a href="/docs/linux/man/2-pivot_root/">pivot_root</a></code>(2) to the new profile. </p>
<p> The paths specified in &#8216;pivot_root&#8217; rules must end with &#8216;/&#8217; since they are directories. </p>
<p> Here are some example &#8216;pivot_root&#8217; rules: </p>
<pre> # Allow any pivot
 pivot_root,
 # Allow pivoting to any new root directory and putting the old root
 # directory at /mnt/root/old/
 pivot_root oldroot=/mnt/root/old/,
 # Allow pivoting the root directory to /mnt/root/
 pivot_root /mnt/root/,
 # Allow pivoting to /mnt/root/ and putting the old root directory at
 # /mnt/root/old/
 pivot_root oldroot=/mnt/root/old/ /mnt/root/,
 # Allow pivoting to /mnt/root/, putting the old root directory at
 # /mnt/root/old/ and transition to the /mnt/root/sbin/init profile
 pivot_root oldroot=/mnt/root/old/ /mnt/root/ -&gt; /mnt/root/sbin/init,</pre>
<h3>PTrace rules</h3>
<p>AppArmor supports mediation of <code><a href="/docs/linux/man/2-ptrace/">ptrace</a></code>(2). AppArmor PTrace rules are accumulated so that the granted PTrace permissions are the union of all the listed PTrace rule permissions. </p>
<p> AppArmor PTrace permissions are implied when a rule does not explicitly state an access list. By default, all PTrace permissions are implied. </p>
<p> The trace and tracedby permissions govern <code><a href="/docs/linux/man/2-ptrace/">ptrace</a></code>(2) while read and readby govern certain <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5) filesystem accesses, <code><a href="/docs/linux/man/2-kcmp/">kcmp</a></code>(2), futexes (<code><a href="/docs/linux/man/2-get_robust_list/">get_robust_list</a></code>(2)) and perf trace events. </p>
<p> For a ptrace operation to be allowed the profile of the tracing process and the profile of the target task must both have the correct permissions. For example, the profile of the process attaching to another task must have the trace permission for the target task&#8217;s profile, and the task being traced must have the tracedby permission for the tracing process&#8217; profile. </p>
<p> Example AppArmor PTrace rules: </p>
<pre> # Allow all PTrace access
 ptrace,
 # Explicitly allow all PTrace access,
 ptrace (read, readby, trace, tracedby),
 # Explicitly deny use of <a href="//www.systutorials.com/docs/linux/man/2-ptrace/">ptrace</a>(2)
 deny ptrace (trace),
 # Allow unconfined processes (eg, a debugger) to ptrace us
 ptrace (readby, tracedby) peer=unconfined,
 # Allow ptrace of a process running under the /usr/bin/foo profile
 ptrace (trace) peer=/usr/bin/foo,</pre>
<h3>Signal rules</h3>
<p>AppArmor supports mediation of <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7). AppArmor signal rules are accumulated so that the granted signal permissions are the union of all the listed signal rule permissions. </p>
<p> AppArmor signal permissions are implied when a rule does not explicitly state an access list. By default, all signal permissions are implied. </p>
<p> For the sending of a signal to be allowed, the profile of the sending process and the profile of the target task must both have the correct permissions. For example, the profile of a process sending a signal to another task must have the send permission for the target task&#8217;s profile, and the task receiving the signal must have a receive permission for the sending process&#8217; profile. </p>
<p> Example AppArmor signal rules: </p>
<pre> # Allow all signal access
 signal,
 # Explicitly deny sending the HUP and INT signals
 deny signal (send) set=(hup, int),
 # Allow unconfined processes to send us signals
 signal (receive) peer=unconfined,
 # Allow sending of signals to a process running under the /usr/bin/foo
 # profile
 signal (send) peer=/usr/bin/foo,
 # Allow checking for PID existence
 signal (receive, send) set=(&quot;exists&quot;),
 # Allow us to signal ourselves using the built-in @{profile_name} variable
 signal peer=@{profile_name},
 # Allow two real-time signals
 signal set=(rtmin+0 rtmin+32),</pre>
<h3>DBus rules</h3>
<p>AppArmor supports DBus mediation. The mediation is performed in conjunction with the DBus daemon. The DBus daemon verifies that communications over the bus are permitted by AppArmor policy. </p>
<p> AppArmor DBus rules are accumulated so that the granted DBus permissions are the union of all the listed DBus rule permissions. </p>
<p> AppArmor DBus rules are broad and general and become more restrictive as further information is specified. Policy may be specified down to the interface member level (method or signal name), however the contents of messages are not examined. </p>
<p> Some AppArmor DBus permissions are not compatible with all AppArmor DBus rules. The &#8216;bind&#8217; permission cannot be used in message rules. The &#8216;send&#8217; and &#8216;receive&#8217; permissions cannot be used in service rules. The &#8216;eavesdrop&#8217; permission cannot be used in rules containing any conditionals outside of the &#8216;bus&#8217; conditional. </p>
<p> &#8216;r&#8217; and &#8216;read&#8217; are synonyms for &#8216;receive&#8217;. &#8216;w&#8217; and &#8216;write&#8217; are synonyms for &#8216;send&#8217;. &#8216;rw&#8217; is a synonym for both &#8216;send&#8217; and &#8216;receive&#8217;. </p>
<p> AppArmor DBus permissions are implied when a rule does not explicitly state an access list. By default, all DBus permissions are implied. Only message permissions are implied for message rules and only service permissions are implied for service rules. </p>
<p> Example AppArmor DBus rules: </p>
<pre> # Allow all DBus access
 dbus,
 # Explicitly allow all DBus access,
 dbus (send, receive, bind),
 # Deny send/receive/bind access to the session bus
 deny dbus bus=session,
 # Allow bind access for a particular name on any bus
 dbus bind name=com.example.ExampleName,
 # Allow receive access for a particular path and interface
 dbus receive path=/com/example/path interface=com.example.Interface,
 # Deny send/receive access to the system bus for a particular interface
 deny dbus bus=system interface=com.example.ExampleInterface,
 # Allow send access for a particular path, interface, member, and pair of
 # peer names:
 dbus send
 bus=session
 path=/com/example/path
 interface=com.example.Interface
 member=ExampleMethod
 peer=(name=(com.example.ExampleName1|com.example.ExampleName2)),
 # Allow receive access for all unconfined peers
 dbus receive peer=(label=unconfined),
 # Allow eavesdropping on the system bus
 dbus eavesdrop bus=system,
 # Allow and audit all eavesdropping
 audit dbus eavesdrop,</pre>
<h3>Unix socket rules</h3>
<p>AppArmor supports fine grained mediation of unix domain abstract and anonymous sockets. Unix domain sockets with file system paths are mediated via file access rules. </p>
<p> Abstract unix domain sockets is a nonportable Linux extension of unix domain sockets, see <code><a href="/docs/linux/man/7-unix/">unix</a></code>(7) for more information. </p>
<p> <i>Unix socket address paths</i> </p>
<p> The sun_path component (aka the socket address) of a unix domain socket is specified by the </p>
<pre> addr=</pre>
<p>conditional. If an address conditional is not specified as part of a rule then the rule matches both abstract and anonymous sockets. </p>
<p> In apparmor the address of an abstract unix domain socket begins with the <i>@</i> character, similar to how they are reported (as paths) by netstat -x. The address then follows and may contain pattern matching and any characters including the null character. In apparmor null characters must be specified by using an escape sequence <i>
