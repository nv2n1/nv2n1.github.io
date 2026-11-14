---
title: "systemd-environment-generator(7)"
name: "systemd-environment-generator"
section: "7"
letter: "s"
url: "/docs/linux/man/7-systemd-environment-generator/"
description: "systemd.environment-generator – systemd environment file generators"
---

<p>systemd.environment-generator &#8211; systemd environment file generators</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>/lib/systemd/system-environment-generators/some-generator</code></p>
<dt> <code>/usr/lib/systemd/user-environment-generators/some-generator</code></dl>
<pre>/run/systemd/system-environment-generators/*
/etc/systemd/system-environment-generators/*
/usr/local/lib/systemd/system-environment-generators/*
/lib/systemd/system-environment-generators/*</pre>
<pre>/run/systemd/user-environment-generators/*
/etc/systemd/user-environment-generators/*
/usr/local/lib/systemd/user-environment-generators/*
/usr/lib/systemd/user-environment-generators/*</pre>
<h2>Description</h2>
<dd>Generators are small executables that live in /lib/systemd/system-environment-generators/ and other directories listed above. <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) will execute those binaries very early at the startup of each manager and at configuration reload time, before running the generators described in <code><a href="/docs/linux/man/7-systemd-generator/">systemd.generator</a></code>(7) and before starting any units. Environment generators can override the environment that the manager exports to services and other processes. </p>
<p> Generators are loaded from a set of paths determined during compilation, as listed above. System and user environment generators are loaded from directories with names ending in system-environment-generators/ and user-environment-generators/, respectively. Generators found in directories listed earlier override the ones with the same name in directories lower in the list. A symlink to /dev/null or an empty file can be used to mask a generator, thereby preventing it from running. Please note that the order of the two directories with the highest priority is reversed with respect to the unit load path, and generators in /run/ overwrite those in /etc/. </p>
<p> After installing new generators or updating the configuration, <code>systemctl daemon-reload</code> may be executed. This will re-run all generators, updating environment configuration. It will be used for any services that are started subsequently. </p>
<p> Environment file generators are executed similarly to unit file generators described in <code><a href="/docs/linux/man/7-systemd-generator/">systemd.generator</a></code>(7), with the following differences: </p>
<dl>
<dd>&bull; Generators are executed sequentially in the alphanumerical order of the final component of their name. The output of each generator output is immediately parsed and used to update the environment for generators that run after that. Thus, later generators can use and/or modify the output of earlier generators.</dl>
<dl>
<dd>&bull; Generators are run by every manager instance, their output can be different for each user.</dl>
<p> It is recommended to use numerical prefixes for generator names to simplify ordering.</p>
<h2>Examples</h2>
<p><code>Example 1. A simple generator that extends an environment variable if a directory exists in the file system</code> </p>
<pre><code># 90 - rearrange - path.py

#!/ usr / bin / env python3

&quot;&quot;&quot;

Proof-of-concept systemd environment generator that makes sure that bin dirs
are always after matching sbin dirs in the path.
(Changes /sbin:/bin:/foo/bar to /bin:/sbin:/foo/bar.)

This generator shows how to override the configuration possibly created by
earlier generators. It would be easier to write in bash, but let's have it
in Python just to prove that we can, and to serve as a template for more
interesting generators.

&quot;&quot;&quot;

import os
import pathlib

def rearrange_bin_sbin(path):
    &quot;&quot;&quot;Make sure any pair of .../bin, .../sbin directories is in this order

    &gt;&gt;&gt; rearrange_bin_sbin('/bin:/sbin:/usr/sbin:/usr/bin')
    '/bin:/sbin:/usr/bin:/usr/sbin'
    &quot;&quot;&quot;
    items = [pathlib.Path(p) for p in path.split(':')]
    for i in range(len(items)):
        if 'sbin' in items[i].parts:
            ind = items[i].parts.index('sbin')
            bin = pathlib.Path(*items[i].parts[:ind], 'bin', *items[i].parts[ind+1:])
            if bin in items[i+1:]:
                j = i + 1 + items[i+1:].index(bin)
                items[i], items[j] = items[j], items[i]
    return ':'.join(p.as_posix() for p in items)

if __name__ == '__main__':
    path = os.environ['PATH'] # This should be always set.
#If it 's not, we' ll just crash, which is OK too.
    new = rearrange_bin_sbin(path)
    if new != path:
        print('PATH={}'.format(new))</code></pre>
<p> <code>Example 2. A more complicated generator which reads existing configuration and mutates one variable</code> </p>
<pre><code># 90 - rearrange - path.py

#!/ usr / bin / env python3

&quot;&quot;&quot;

Proof-of-concept systemd environment generator that makes sure that bin dirs
are always after matching sbin dirs in the path.
(Changes /sbin:/bin:/foo/bar to /bin:/sbin:/foo/bar.)

This generator shows how to override the configuration possibly created by
earlier generators. It would be easier to write in bash, but let's have it
in Python just to prove that we can, and to serve as a template for more
interesting generators.

&quot;&quot;&quot;

import os
import pathlib

def rearrange_bin_sbin(path):
    &quot;&quot;&quot;Make sure any pair of .../bin, .../sbin directories is in this order

    &gt;&gt;&gt; rearrange_bin_sbin('/bin:/sbin:/usr/sbin:/usr/bin')
    '/bin:/sbin:/usr/bin:/usr/sbin'
    &quot;&quot;&quot;
    items = [pathlib.Path(p) for p in path.split(':')]
    for i in range(len(items)):
        if 'sbin' in items[i].parts:
            ind = items[i].parts.index('sbin')
            bin = pathlib.Path(*items[i].parts[:ind], 'bin', *items[i].parts[ind+1:])
            if bin in items[i+1:]:
                j = i + 1 + items[i+1:].index(bin)
                items[i], items[j] = items[j], items[i]
    return ':'.join(p.as_posix() for p in items)

if __name__ == '__main__':
    path = os.environ['PATH'] # This should be always set.
#If it 's not, we' ll just crash, which is OK too.
    new = rearrange_bin_sbin(path)
    if new != path:
        print('PATH={}'.format(new))</code></pre>
<p> <code>Example 3. Debugging a generator</code></p>
<dl>
<dd>
<pre>SYSTEMD_LOG_LEVEL=debug VAR_A=something VAR_B=&quot;something else&quot; \
/lib/systemd/system-environment-generators/path-to-generator</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-systemd-environment-d-generator/">systemd-environment-d-generator</a></code>(8), <code><a href="/docs/linux/man/7-systemd-generator/">systemd.generator</a></code>(7), <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1) </p>
