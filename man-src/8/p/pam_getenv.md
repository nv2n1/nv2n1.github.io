---
title: "pam_getenv(8)"
name: "pam_getenv"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_getenv/"
description: "pam_getenv – get environment variables from /etc/environment"
---

<p>pam_getenv &#8211; get environment variables from /etc/environment</p>
<h2>Synopsis</h2>
<p>pam_getenv <code>[-l] [-s]</code> <i>env_var</i></p>
<h2>Description</h2>
<p>This tool will print out the value of <i>env_var</i> from <i>/etc/environment</i>. It will attempt to expand environment variable references in the definition of <i>env_var</i> but will fail if <font SIZE="-1">PAM</font> items are expanded. The <code>-l</code> option indicates the script should return an environment variable related to default locale information. The <code>-s</code> option indicates that the script should return an system default environment variable. Currently neither the <code>-l</code> or <code>-s</code> options do anything. They are included because future versions of Debian may have a separate repository for the initial environment used by init scripts and for system locale information. These options will allow this script to be a stable interface even in that environment. </p>
