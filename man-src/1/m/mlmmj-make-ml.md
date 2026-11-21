---

title: "mlmmj-make-ml(1)"
name: "mlmmj-make-ml"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mlmmj-make-ml/"
description: "mlmmj-make-ml – create a mailing list for mlmmj"
---

<h2>NAME</h2>
<p> mlmmj-make-ml &#8211; create a mailing list for mlmmj</p>
<p> <code>mlmmj-make-ml</code> [<i>-h</i>] [<i>-L listname</i>] [<i>-s spooldir</i>] [<i>-a</i>] [<i>-c user</i>] [<i>-z</i>]</p>
<dl>
<dt> <code>-h</code>: Display help</dt>
<dt> <code>-L</code>: The name of the mailing list</dt>
<dt> <code>-s</code>: Your spool directory (default /var/spool/mlmmj)</dt>
<dt> <code>-a</code>: Create the needed entries in your /etc/aliases file</dt>
<dt> <code>-c</code>: User to chown the spool directory to (default not to chown at all)</dt>
<dt> <code>-z</code>: Do nothing for now</dt></dl>
<dd>This is an interactive script which creates the mailing list directory and thus the list itself for being run by mlmmj.</dd>
<h2>BUGS</h2>
<p> It&#8217;s not possible to create a list entirely on the command line.</p>
<h2>AUTHORS</h2>
<p> This manual page was written by the following persons:</p>
<dl>
<dt>
</dt><dd>S&oslash;ren Boll Overgaard &lt;boll [at] debian.org&gt; (based on html2man output)</dd>
<dt>
</dt><dd>Mads Martin J&oslash;rgensen &lt;mmj [at] mmj.dk&gt; </dd>
</dl>
