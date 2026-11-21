---

title: "prsync(1)"
name: "prsync"
section: "1"
letter: "p"
url: "/docs/linux/man/1-prsync/"
description: "prsync — parallel process kill program"
---

<p> <code>prsync</code> [<code>-vAraz</code>] [<code>-h</code> <i>hosts_file</i>] [<code>-H</code> [<i>user</i>@]<i>host</i>[:<i>port</i>]] [<code>-l</code> <i>user</i>] [<code>-p</code> <i>par</i>] [<code>-o</code> <i>outdir</i>] [<code>-e</code> <i>errdir</i>] [<code>-t</code> <i>timeout</i>] [<code>-O</code> <i>options</i>] [<code>-x</code> <i>args</i>] [<code>-X</code> <i>arg</i>] [<code>-S</code> <i>args</i>] <i>local</i> <i>remote</i> </p>
<p> <code>prsync</code> is a program for copying files in parallel to a number of hosts. It provides features such as passing a password to ssh, saving output to files, and timing out. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code><i> host_file</i></dt>
<dd>
</dd><dt><code>&#8211;hosts</code><i> host_file</i></dt>
<dd> Read hosts from the given <i>host_file</i>. Lines in the host file are of the form [<i>user</i>@]<i>host</i>[:<i>port</i>] and can include blank lines and comments (lines beginning with &quot;#&quot;). If multiple host files are given (the <code>-h</code> option is used more than once), then prsync behaves as though these files were concatenated together. If a host is specified multiple times, then prsync will connect the given number of times. </dd>
<dt><code>-H</code></dt>
<dd> [<i>user</i>@]<i>host</i>[:<i>port</i>]</dd>
<dt><code>&#8211;host</code></dt>
<dd> [<i>user</i>@]<i>host</i>[:<i>port</i>]</dd>
<dt><code>-H</code></dt>
<dd> &quot;[<i>user</i>@]<i>host</i>[:<i>port</i>] [ [<i>user</i>@]<i>host</i>[:<i>port</i> ] &#8230; ]&quot;</dd>
<dt><code>&#8211;host</code></dt>
<dd> &quot;[<i>user</i>@]<i>host</i>[:<i>port</i>] [ [<i>user</i>@]<i>host</i>[:<i>port</i> ] &#8230; ]&quot;</dd>
<dt>
</dt><dd> Add the given host strings to the list of hosts. This option may be given multiple times, and may be used in conjunction with the <code>-h</code> option. </dd>
<dt><code>-l</code><i> user</i></dt>
<dd>
</dd><dt><code>&#8211;user</code><i> user</i></dt>
<dd> Use the given username as the default for any host entries that don&#8217;t specifically specify a user. </dd>
<dt><code>-p</code><i> parallelism</i></dt>
<dd>
</dd><dt><code>&#8211;par</code><i> parallelism</i></dt>
<dd> Use the given number as the maximum number of concurrent connections. </dd>
<dt><code>-t</code><i> timeout</i></dt>
<dd>
</dd><dt><code>&#8211;timeout</code><i> timeout</i></dt>
<dd> Make connections time out after the given number of seconds. With a value of 0, prsync will not timeout any connections. </dd>
<dt><code>-o</code><i> outdir</i></dt>
<dd>
</dd><dt><code>&#8211;outdir</code><i> outdir</i></dt>
<dd> Save standard output to files in the given directory. Filenames are of the form [<i>user</i>@]<i>host</i>[:<i>port</i>][.<i>num</i>] where the user and port are only included for hosts that explicitly specify them. The number is a counter that is incremented each time for hosts that are specified more than once. </dd>
<dt><code>-e</code><i> errdir</i></dt>
<dd>
</dd><dt><code>&#8211;errdir</code><i> errdir</i></dt>
<dd> Save standard error to files in the given directory. Filenames are of the same form as with the <code>-o</code> option. </dd>
<dt><code>-x</code><i> args</i></dt>
<dd>
</dd><dt><code>&#8211;extra-args</code><i> args</i></dt>
<dd> Passes extra rsync command-line arguments (see the <code><a href="/docs/linux/man/1-rsync/">rsync</a></code>(1) man page for more information about rsync arguments). This option may be specified multiple times. The arguments are processed to split on whitespace, protect text within quotes, and escape with backslashes. To pass arguments without such processing, use the <code>-X</code> option instead. </dd>
<dt><code>-X</code><i> arg</i></dt>
<dd>
</dd><dt><code>&#8211;extra-arg</code><i> arg</i></dt>
<dd> Passes a single rsync command-line argument (see the <code><a href="/docs/linux/man/1-rsync/">rsync</a></code>(1) man page for more information about rsync arguments). Unlike the <code>-x</code> option, no processing is performed on the argument, including word splitting. To pass multiple command-line arguments, use the option once for each argument. </dd>
<dt><code>-O</code><i> options</i></dt>
<dd>
</dd><dt><code>&#8211;options</code><i> options</i></dt>
<dd> SSH options in the format used in the SSH configuration file (see the <code><a href="/docs/linux/man/5-ssh_config/">ssh_config</a></code>(5) man page for more information). This option may be specified multiple times. </dd>
<dt><code>-A</code></dt>
<dd>
</dd><dt><code>&#8211;askpass</code></dt>
<dd> Prompt for a password and pass it to ssh. The password may be used for either to unlock a key or for password authentication. The password is transferred in a fairly secure manner (e.g., it will not show up in argument lists). However, be aware that a root user on your system could potentially intercept the password. </dd>
<dt><code>-v</code></dt>
<dd>
</dd><dt><code>&#8211;verbose</code></dt>
<dd> Include error messages from rsync with the <code>-i</code> and <code>\</code> options. </dd>
<dt><code>-r</code></dt>
<dd>
</dd><dt><code>&#8211;recursive</code></dt>
<dd> Recursively copy directories. </dd>
<dt><code>-a</code></dt>
<dd>
</dd><dt><code>&#8211;archive</code></dt>
<dd> Use rsync archive mode (rsync&#8217;s -a option). </dd>
<dt><code>-z</code></dt>
<dd>
</dd><dt><code>&#8211;compress</code></dt>
<dd> Use rsync compression. </dd>
<dt><code>-S</code><i> args</i></dt>
<dd>
</dd><dt><code>&#8211;ssh-args</code><i> args</i></dt>
<dd> Passes extra SSH command-line arguments (see the <code><a href="/docs/linux/man/1-ssh/">ssh</a></code>(1) man page for more information about SSH arguments). The given value is appended to the ssh command (rsync&#8217;s -e option) without any processing. </dd>
</dl>
<h2>TIPS</h2>
<p> The ssh_config file can include an arbitrary number of Host sections. Each host entry specifies ssh options which apply only to the given host. Host definitions can even behave like aliases if the HostName option is included. This ssh feature, in combination with pssh host files, provides a tremendous amount of flexibility. </p>
<h2>EXIT STATUS</h2>
<p> The exit status codes from prsync are as follows: </p>
<dl>
<dt><code>0</code></dt>
<dd> Success </dd>
<dt><code>1</code></dt>
<dd> Miscellaneous error </dd>
<dt><code>2</code></dt>
<dd> Syntax or usage error </dd>
<dt><code>3</code></dt>
<dd> At least one process was killed by a signal or timed out. </dd>
<dt><code>4</code></dt>
<dd> All processes completed, but at least one rsync process reported an error (exit status other than 0). </dd>
</dl>
<h2>AUTHORS</h2>
<p> Written by Brent N. Chun &lt;bnc [at] theether.org&gt; and Andrew McNabb &lt;amcnabb [at] mcnabbs.org&gt;. </p>
<p> <a rel="nofollow" href="http://code.google.com/p/parallel-ssh/">http://code.google.com/p/parallel-ssh/</a> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-rsync/">rsync</a></code>(1), <code><a href="/docs/linux/man/1-ssh/">ssh</a></code>(1), <code><a href="/docs/linux/man/5-ssh_config/">ssh_config</a>(5),</code> <code><a href="/docs/linux/man/1-pssh/">pssh</a></code>(1), <code><a href="/docs/linux/man/1-prsync/">prsync</a></code>(1), <code><a href="/docs/linux/man/1-pslurp/">pslurp</a></code>(1), <code><a href="/docs/linux/man/1-pnuke/">pnuke</a></code>(1), </p>
