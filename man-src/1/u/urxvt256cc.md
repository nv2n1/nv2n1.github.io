---
title: "urxvt256cc(1)"
name: "urxvt256cc"
section: "1"
letter: "u"
url: "/docs/linux/man/1-urxvt256cc/"
description: "urxvt256cc – control the urxvt256cd daemon"
---

<h2 class="name">NAME</h2>
<p> urxvt256cc &#8211; control the urxvt256cd daemon </p>
<h2>SYNOPSIS</h2>
<p> <code>urxvt256cc</code> [same options as for urxvt256c]</p>
<h2>DESCRIPTION</h2>
<p> This manpage describes the <code>urxvt256cc</code> client program. It connects to the <code>urxvt256cd</code> daemon and requests a new terminal window. It takes the same arguments as the <code>urxvt256c</code> program. The environment will also be respected. Currently, it always returns immediately after contacting the daemon.</p>
<h2>OPTIONS</h2>
<p> If the first option is <code>-k</code>, <code>urxvt256cc</code> tries to kill the daemon process and returns. </p>
<p> All options that are valid for <code>urxvt256c</code> are valid for <code>urxvt256cc</code>, too. Please note that options are interpreted in the context of the daemon process. However, as current working directory, process environment and any file descriptor (e.g. for <tt>&quot;-pty-fd&quot;</tt>) are preserved, this rarely makes a difference.</p>
<h2>EXIT STATUS</h2>
<p> If everything went well, urxvt256cc returns with an exit status of <tt>0</tt>. If contacting the daemon fails, it exits with the exit status <tt>2</tt>. In all other error cases it returns with status <tt>1</tt>. </p>
<p> This can be used to implement auto-starting behaviour, by checking for an exit status of <tt>2</tt>, running <tt>&quot;urxvt256cd -f -q&quot;</tt> and retrying the call to urxvt256cc, like this: </p>
<pre><code>
#!/ bin / sh
   urxvt256cc "$@"
   if [ $? -eq 2 ];
   then
           urxvt256cd -
       q - o - f urxvt256cc "$@" fi
</code></pre>
<h2>ENVIRONMENT</h2>
<p> All environment variables of the current process will be made available to the new instance, and will be interpreted as if <code>urxvt256c</code> were started directly.</p>
<dl>
<dt><font SIZE="-1"><code>RXVT_SOCKET</code></font></p>
<dd> Both urxvt256cc and urxvt256cd use the environment variable <i></i><font SIZE="-1"><i>RXVT_SOCKET</i></font><i></i> to create a listening socket and to contact the urxvt256cd, respectively. If the variable is missing, <i></i>$HOME<i>/.urxvt/urxvtd-&lt;nodename&gt;</i> is used. The variable must specify the absolute path of the socket to create.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-urxvt256c/">urxvt256c</a>(7), <a href="/docs/linux/man/1-urxvt256cd/">urxvt256cd</a>(1) </p>
<h2>Index</h2>
