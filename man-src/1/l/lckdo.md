---

title: "lckdo(1)"
name: "lckdo"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lckdo/"
description: "lckdo – run a program with a lock held"
---

<dl>
<dt> <code>lckdo</code> [options] {lockfile} {program} [arguments]</dt></dl>
<p> <code>lckdo</code></p>
<dd>runs a program with a lock held, in order to prevent multiple processes from running in parallel. Use just like <code>nice</code> or <code>nohup</code>. </dd>
<p> Now that util-linux contains a similar command named <code>flock</code>, lckdo is deprecated, and will be removed from some future version of moreutils.</p>
<h2>OPTIONS</h2>
<p> <code>-w</code></p>
<dl>
<dt>
</dt><dd> If the lock is already held by another process, wait for it to complete instead of failing immediately.</dd></dl>
<p> <code>-W {sec}</code></p>
<dl>
<dt>
</dt><dd> The same as -w but wait not more than sec seconds.</dd></dl>
<p> <code>-e</code></p>
<dl>
<dt>
</dt><dd> Execute the program directly without forking and waiting (keeps an extra file descriptor open).</dd></dl>
<p> <code>-E {nnn}</code></p>
<dl>
<dt>
</dt><dd> Set the file descriptor number to keep open when exec()ing (implies -e).</dd></dl>
<p> <code>-n</code></p>
<dl>
<dt>
</dt><dd> Do not create the lock file if it does not exist.</dd></dl>
<p> <code>-q</code></p>
<dl>
<dt>
</dt><dd> Produce no output if lock is already held.</dd></dl>
<p> <code>-s</code></p>
<dl>
<dt>
</dt><dd> Lock in shared (read) mode.</dd></dl>
<p> <code>-x</code></p>
<dl>
<dt>
</dt><dd> Lock in exclusive (write) mode (default).</dd></dl>
<p> <code>-t</code></p>
<dl>
<dt>
</dt><dd> Test for lock existence.</dd></dl>
<h2>EXIT STATUS</h2>
<p> If the lock was successfully acquired, the return value is that of the program invoked by <code>lckdo</code>. If the lock couldn&#8217;t be acquired, EX_TEMPFAIL is returned. If there was a problem opening/creating or locking the lock file, EX_CANTCREAT or EX_OSERR will be returned.</p>
<h2>AUTHOR</h2>
<p> Michael Tokarev </p>
