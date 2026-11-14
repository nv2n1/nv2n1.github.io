---
title: "gcin(1)"
name: "gcin"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gcin/"
description: "gcin – an input method server"
---

<h2>NAME</h2>
<p> gcin &#8211; an input method server</p>
<h2>SYNOPSIS</h2>
<p> <code>gcin</code> <code>[-h</code>|<code>-v</code>|<code>&#8211;version</code>] </p>
<h2>DESCRIPTION</h2>
<p> <code>gcin</code> is an input method(IM) server, which focused mainly on Traditional Chinese. It is also very useful for Simplified Chinese, Japanese, and many other languages. IM table format of gcin is almost as same as those of scim and xcin. Users may append their IMs to gcin very easily. The &quot;g&quot; of gcin means that it features a better GTK+ user interface. </p>
<p> If you are looking for configuration tool of gcin, please see the manpage of <code>gcin-setup</code>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, -v, &#8211;version</code></p>
<dd> Show version of gcin.</dl>
<h2>FILES</h2>
<dl>
<dt>/usr/share/gcin/table/gtab.list</p>
<dd> Input methods available for gcin. You may copy it to $HOME/.gcin/ and edit it as you like. If you have no $HOME/.gcin/gtab.list, /usr/share/gcin/table/gtab.list will be used.</p>
<dt>/usr/share/gcin/script/html-browser</p>
<dd> A file helps gcin finding html browsers when needed. You may add any compatible html browser to it.</p>
<dt>/usr/share/gcin/script/utf8-edit</p>
<dd> A file helps gcin finding text editors when needed. You may add any UTF-8 compatible text editor to it.</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt>LC_CTYPE</p>
<dd> For bash: export LC_CTYPE=zh_TW.UTF-8<br />
 For csh: setenv LC_CTYPE zh_TW.UTF-8</p>
<dt>XMODIFIERS</p>
<dd> For bash: export XMODIFIERS=@im=gcin<br />
 For csh: setenv XMODIFIERS @im=gcin</p>
<dt>GTK_IM_MODULE</p>
<dd> For bash: export GTK_IM_MODULE=gcin<br />
 For csh: setenv GTK_IM_MODULE gcin</p>
<dt>QT_IM_MODULE</p>
<dd> For bash: export QT_IM_MODULE=gcin<br />
 For csh: setenv QT_IM_MODULE gcin</p>
<dt>GCIN_CONNECT_MSG_ON</p>
<dd> Display messages for socket connections.</p>
<dt>GCIN_DBG_TMP</p>
<dd> Display additional debug messages.</p>
<dt>GCIN_ERR_COREDUMP</p>
<dd> Option for debugging.</p>
<dt>GCIN_IM_CLIENT_NO_AUTO_EXEC</p>
<dd> Disable auto-evoke in gcin protocol.</p>
<dt>GCIN_OUTPUT_FILTER</p>
<dd> Assign output filter to process data before the IM server send them to clients.</p>
<dt>GCIN_TABLE_DIR</p>
<dd> Assign directory for IM tables other then /usr/share/gcin/table.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gcin-setup/">gcin-setup</a></code>(1), <code><a href="/docs/linux/man/1-gcin2tab/">gcin2tab</a></code>(1), <code><a href="/docs/linux/man/1-phoa2d/">phoa2d</a></code>(1), <code><a href="/docs/linux/man/1-juyin-learn/">juyin-learn</a></code>(1), <code><a href="/docs/linux/man/1-gcin-message/">gcin-message</a></code>(1)</p>
<h2>AUTHORS</h2>
<dl>
<dt>Edward Der-Hua Liu</p>
<dd> Wrote gcin and associated tools.</p>
<dt>Friend of Chanjei IM, Malaysia &lt;<a rel="nofollow" href="http://www.chinesecj.com">www.chinesecj.com</a>&gt;</p>
<dd> Author of original Chanjei IM version 5 table.</p>
<dt>Dayi Co., Ltd. &lt;<a rel="nofollow" href="http://www.dayi.com">http://www.dayi.com</a>&gt;</p>
<dd> Author of Dayi IM. </p>
</dl>
<h2>Index</h2>
