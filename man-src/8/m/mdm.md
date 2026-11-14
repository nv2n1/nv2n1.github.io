---
title: "mdm(8)"
name: "mdm"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mdm/"
description: "mdm – MDM Display Manager"
---

<p>mdm &#8211; MDM Display Manager</p>
<h2>Synopsis</h2>
<p>mdm</p>
<h2>Description</h2>
<p><code>mdm</code> is the equivalent of <i><a href="//www.systutorials.com/docs/linux/man/1x-xdm/">xdm</a></i>(1x) or <i><a href="//www.systutorials.com/docs/linux/man/1x-wdm/">wdm</a></i>(1x), but uses the <font SIZE="-1">GNOME</font> libraries to provide a <font SIZE="-1">GNOME</font> look-and-feel. It provides the <font SIZE="-1">GNOME</font> equivalent of a &#8220;login:&#8221; prompt. </p>
<p> <code>mdm</code> reads <i>/etc/mdm/mdm.conf</i> for its configuration. For each local display, mdm starts an X server and runs <i><a href="//www.systutorials.com/docs/linux/man/8x-mdmlogin/">mdmlogin</a></i>(8x) on that display. The main mdm process also listens for <font SIZE="-1">XDMCP</font> requests from remote displays. These requests can either be direct, causing <code>mdm</code> to start a <i><a href="//www.systutorials.com/docs/linux/man/8x-mdmlogin/">mdmlogin</a></i>(8x) on the remote display, or indirect, causing a <i><a href="//www.systutorials.com/docs/linux/man/8x-mdmchooser/">mdmchooser</a></i>(8x) to be opened. </p>
<p> When managing a display, <code>mdm</code> attempts to execute <i>/etc/mdm/Init/</i><i>display</i>, or <i>/etc/mdm/Init/Default</i> if that does not exist. When a user logs in, <code>mdm</code> first attempts <i>/etc/mdm/PreSession/</i><i>display</i> (or <i>/etc/mdm/PreSession/Default</i>), and then one of the sessions in <i>/etc/mdm/Sessions</i>. When the session has completed, <code>mdm</code> attempts to run <i>/etc/mdm/PostSession/</i><i>display</i>, or <i>/etc/mdm/PostSession/</i><i>Default</i>. Of all these files, only the <i>/etc/mdm/Sessions</i> one is required to exist. </p>
<p> <code>mdm</code> maintains information about the displays it is managing in <i>/var/lib/mdm</i>. This includes xauth information, so this directory is not readable to normal users. </p>
<p> <code>mdm</code> uses <font SIZE="-1">PAM</font> to perform authentication using the config file <i>/etc/pam.d/mdm</i>.</p>
<h2>Author</h2>
<p>Martin Kasper Petersen &lt;mkp [at] SunSITE.auc.dk&gt; </p>
<p> This manual page written by Steve Haslam &lt;araqnid [at] debian.org&gt; for Debian GNU/Linux. Updated by Raphae.l Hertzog &lt;hertzog [at] debian.org&gt;. Updated by Ryan Murray &lt;rmurray [at] debian.org&gt;.</p>
