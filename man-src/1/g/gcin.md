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
<dt><code>-h, -v, &#8211;version</code></dt>
<dd> Show version of gcin.</dd></dl>
<h2>FILES</h2>
<dl>
<dt>/usr/share/gcin/table/gtab.list</dt>
<dd> Input methods available for gcin. You may copy it to $HOME/.gcin/ and edit it as you like. If you have no $HOME/.gcin/gtab.list, /usr/share/gcin/table/gtab.list will be used.</dd>
<dt>/usr/share/gcin/script/html-browser</dt>
<dd> A file helps gcin finding html browsers when needed. You may add any compatible html browser to it.</dd>
<dt>/usr/share/gcin/script/utf8-edit</dt>
<dd> A file helps gcin finding text editors when needed. You may add any UTF-8 compatible text editor to it.</dd></dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt>LC_CTYPE</dt>
<dd> For bash: export LC_CTYPE=zh_TW.UTF-8<br />
 For csh: setenv LC_CTYPE zh_TW.UTF-8</dd>
<dt>XMODIFIERS</dt>
<dd> For bash: export XMODIFIERS=@im=gcin<br />
 For csh: setenv XMODIFIERS @im=gcin</dd>
<dt>GTK_IM_MODULE</dt>
<dd> For bash: export GTK_IM_MODULE=gcin<br />
 For csh: setenv GTK_IM_MODULE gcin</dd>
<dt>QT_IM_MODULE</dt>
<dd> For bash: export QT_IM_MODULE=gcin<br />
 For csh: setenv QT_IM_MODULE gcin</dd>
<dt>GCIN_CONNECT_MSG_ON</dt>
<dd> Display messages for socket connections.</dd>
<dt>GCIN_DBG_TMP</dt>
<dd> Display additional debug messages.</dd>
<dt>GCIN_ERR_COREDUMP</dt>
<dd> Option for debugging.</dd>
<dt>GCIN_IM_CLIENT_NO_AUTO_EXEC</dt>
<dd> Disable auto-evoke in gcin protocol.</dd>
<dt>GCIN_OUTPUT_FILTER</dt>
<dd> Assign output filter to process data before the IM server send them to clients.</dd>
<dt>GCIN_TABLE_DIR</dt>
<dd> Assign directory for IM tables other then /usr/share/gcin/table.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gcin-setup/">gcin-setup</a></code>(1), <code>gcin2tab</code>(1), <code><a href="/docs/linux/man/1-phoa2d/">phoa2d</a></code>(1), <code>juyin-learn</code>(1), <code><a href="/docs/linux/man/1-gcin-message/">gcin-message</a></code>(1)</p>
<h2>AUTHORS</h2>
<dl>
<dt>Edward Der-Hua Liu</dt>
<dd> Wrote gcin and associated tools.</dd>
<dt>Friend of Chanjei IM, Malaysia &lt;<a rel="nofollow" href="http://www.chinesecj.com">www.chinesecj.com</a>&gt;</dt>
<dd> Author of original Chanjei IM version 5 table.</dd>
<dt>Dayi Co., Ltd. &lt;<a rel="nofollow" href="http://www.dayi.com">http://www.dayi.com</a>&gt;</dt>
<dd> Author of Dayi IM. </dd>
</dl>
<h2>Index</h2>
