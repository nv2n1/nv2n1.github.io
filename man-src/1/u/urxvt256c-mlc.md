---
title: "urxvt256c-mlc(1)"
name: "urxvt256c-mlc"
section: "1"
letter: "u"
url: "/docs/linux/man/1-urxvt256c-mlc/"
description: "urxvt256c-mlc – control the urxvt256c-mld daemon"
---

<h2 class="name">NAME</h2>
<p> urxvt256c-mlc &#8211; control the urxvt256c-mld daemon </p>
<h2>SYNOPSIS</h2>
<p> <code>urxvt256c-mlc</code> [same options as for urxvt256c-ml]</p>
<h2>DESCRIPTION</h2>
<p> This manpage describes the <code>urxvt256c-mlc</code> client program. It connects to the <code>urxvt256c-mld</code> daemon and requests a new terminal window. It takes the same arguments as the <code>urxvt256c-ml</code> program. The environment will also be respected. Currently, it always returns immediately after contacting the daemon.</p>
<h2>OPTIONS</h2>
<p> If the first option is <code>-k</code>, <code>urxvt256c-mlc</code> tries to kill the daemon process and returns. </p>
<p> All options that are valid for <code>urxvt256c-ml</code> are valid for <code>urxvt256c-mlc</code>, too. Please note that options are interpreted in the context of the daemon process. However, as current working directory, process environment and any file descriptor (e.g. for <tt>&quot;-pty-fd&quot;</tt>) are preserved, this rarely makes a difference.</p>
<h2>EXIT STATUS</h2>
<p> If everything went well, urxvt256c-mlc returns with an exit status of <tt>0</tt>. If contacting the daemon fails, it exits with the exit status <tt>2</tt>. In all other error cases it returns with status <tt>1</tt>. </p>
<p> This can be used to implement auto-starting behaviour, by checking for an exit status of <tt>2</tt>, running <tt>&quot;urxvt256c-mld -f -q&quot;</tt> and retrying the call to urxvt256c-mlc, like this: </p>
<pre><code>
#!/ bin / sh
   urxvt256c-mlc "$@"
   if [ $? -eq 2 ];
   then
           urxvt256c -
       mld - q - o - f urxvt256c - mlc "$@" fi
</code></pre>
<h2>ENVIRONMENT</h2>
<p> All environment variables of the current process will be made available to the new instance, and will be interpreted as if <code>urxvt256c-ml</code> were started directly.</p>
<dl>
<dt><font SIZE="-1"><code>RXVT_SOCKET</code></font></p>
<dd> Both urxvt256c-mlc and urxvt256c-mld use the environment variable <i></i><font SIZE="-1"><i>RXVT_SOCKET</i></font><i></i> to create a listening socket and to contact the urxvt256c-mld, respectively. If the variable is missing, <i></i>$HOME<i>/.urxvt/urxvtd-&lt;nodename&gt;</i> is used. The variable must specify the absolute path of the socket to create.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-urxvt256c-ml/">urxvt256c-ml</a>(7), <a href="/docs/linux/man/1-urxvt256c-mld/">urxvt256c-mld</a>(1) </p>
<h2>Index</h2>
